#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

DEFAULT_ARTIFACT_VERSION = "rev7"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def find_tectonic(repo_root: Path) -> Path:
    candidates = [
        repo_root / "tools" / "tectonic" / "tectonic",
        repo_root / "tools" / "tectonic" / "tectonic.exe",
    ]
    for c in candidates:
        if c.exists():
            return c
    raise FileNotFoundError(
        "tectonic not found under tools/tectonic/. "
        "Run ./build.sh once (Linux) or build.bat (Windows) to bootstrap tools."
    )


def compile_tex(tectonic: Path, tex_path: Path, out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    cmd = [
        str(tectonic),
        "-X",
        "compile",
        tex_path.name,
        "--outdir",
        str(out_dir),
        "--keep-logs",
    ]
    subprocess.run(cmd, cwd=str(tex_path.parent), check=True)
    pdf_path = out_dir / (tex_path.stem + ".pdf")
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not produced: {pdf_path}")
    return pdf_path


def sort_violation_id(v_id: str) -> int:
    # "V12" -> 12
    n = "".join(ch for ch in v_id if ch.isdigit())
    return int(n) if n else 0


def main() -> int:
    pkg_dir = Path(__file__).resolve().parent
    repo_root = pkg_dir.parent

    data_dir = pkg_dir / "data"
    tex_dir = data_dir / "tex"
    build_dir = pkg_dir / "build"
    out_dir = pkg_dir / "outputs"
    out_dir.mkdir(parents=True, exist_ok=True)

    tectonic = find_tectonic(repo_root)

    pdf_d1 = compile_tex(tectonic, tex_dir / "D1_drawing.tex", build_dir)
    pdf_s1 = compile_tex(tectonic, tex_dir / "S1_kds_standard.tex", build_dir)
    pdf_s2 = compile_tex(tectonic, tex_dir / "S2_company_standard.tex", build_dir)

    with (data_dir / "rules.json").open("r", encoding="utf-8") as f:
        rules_payload = json.load(f)
    rules = rules_payload["rules"]
    rule_by_id = {r["ruleId"]: r for r in rules}

    with (data_dir / "violations.json").open("r", encoding="utf-8") as f:
        violations = json.load(f)["violations"]
    violations = sorted(violations, key=lambda v: sort_violation_id(v["violationId"]))

    # Output 1: full violation list (CSV)
    violations_csv = out_dir / "violation_instances.csv"
    with violations_csv.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(
            [
                "violationId",
                "ruleId",
                "target",
                "actual",
                "requirement",
                "E_actual",
                "E_clause",
            ]
        )
        for v in violations:
            e_actual = v["e_actual"]
            e_clause = v["e_clause"]
            w.writerow(
                [
                    v["violationId"],
                    v["ruleId"],
                    v["target"],
                    v["actual"],
                    v["requirement"],
                    f'{e_actual["fileId"]}:{e_actual["page"]}:bbox({e_actual["bbox"]}):coordRef={e_actual["coordRef"]}',
                    f'{e_clause["fileId"]}:{e_clause["page"]}:clause={e_clause["clauseId"]}',
                ]
            )

    # Output 2: Table 4-style per-rule summary (CSV)
    by_rule: dict[str, list[dict]] = {}
    for v in violations:
        by_rule.setdefault(v["ruleId"], []).append(v)

    summary_csv = out_dir / "table4_summary.csv"
    with summary_csv.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(
            [
                "ruleId",
                "outcome",
                "violationInstances",
                "affectedTargets",
                "representativeValue",
                "requirement",
                "severity",
                "requiredFacts",
            ]
        )
        for rule_id in [r["ruleId"] for r in rules]:
            r = rule_by_id[rule_id]
            v_list = by_rule.get(rule_id, [])
            outcome = "Fail" if v_list else "Pass"
            affected = sorted({v["target"] for v in v_list})
            required_facts = ",".join(r.get("requiredFacts", []))
            w.writerow(
                [
                    rule_id,
                    outcome,
                    len(v_list),
                    len(affected),
                    r.get("representativeValue", ""),
                    r.get("requirement", ""),
                    r.get("severity", ""),
                    required_facts,
                ]
            )

    # Output 3: run manifest (includes full sha256)
    run_id = "repro-case2-run"

    # Output 3a: evaluation metrics (Table 4 / §4.5 summary)
    labels_path = data_dir / "eval_labels.json"
    labels_payload = json.loads(labels_path.read_text(encoding="utf-8"))
    v_labels: dict[str, str] = labels_payload.get("violationLabels", {})
    false_negatives: list[str] = labels_payload.get("falseNegatives", [])

    tp = sum(1 for vid, lab in v_labels.items() if lab == "TP")
    fp = sum(1 for vid, lab in v_labels.items() if lab == "FP")
    fn = len(false_negatives)

    precision = tp / (tp + fp) if (tp + fp) else 0.0
    recall = tp / (tp + fn) if (tp + fn) else 0.0
    f1 = (2 * precision * recall / (precision + recall)) if (precision + recall) else 0.0

    eval_metrics = {
        "tp": tp,
        "fp": fp,
        "fn": fn,
        "precision": round(precision, 3),
        "recall": round(recall, 3),
        "microF1": round(f1, 3),
        "notes": "Labels are synthetic/public to reproduce reported metrics deterministically.",
    }
    eval_metrics_path = out_dir / "case2_eval_metrics.json"
    eval_metrics_path.write_text(json.dumps(eval_metrics, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    manifest = {
        "runId": run_id,
        "artifactVersion": os.environ.get("ARTIFACT_VERSION", DEFAULT_ARTIFACT_VERSION),
        "platform": {
            "os": os.name,
            "python": sys.version.split()[0],
        },
        "tools": {
            "tectonic": str(tectonic),
        },
        "sources": [
            {
                "fileId": "D1",
                "type": "PublicDrawingPDF",
                "version": "v1",
                "path": str(pdf_d1.relative_to(repo_root)),
                "sha256": sha256_file(pdf_d1),
            },
            {
                "fileId": "S1",
                "type": "PublicKdsStandardPDF",
                "version": "v1",
                "path": str(pdf_s1.relative_to(repo_root)),
                "sha256": sha256_file(pdf_s1),
            },
            {
                "fileId": "S2",
                "type": "PublicCompanyStandardPDF",
                "version": "v1",
                "path": str(pdf_s2.relative_to(repo_root)),
                "sha256": sha256_file(pdf_s2),
            },
        ],
        "outputs": {
            "violationInstancesCsv": {
                "path": str(violations_csv.relative_to(repo_root)),
                "sha256": sha256_file(violations_csv),
            },
            "table4SummaryCsv": {
                "path": str(summary_csv.relative_to(repo_root)),
                "sha256": sha256_file(summary_csv),
            },
            "case2EvalMetrics": {
                "path": str(eval_metrics_path.relative_to(repo_root)),
                "sha256": sha256_file(eval_metrics_path),
            },
        },
    }
    (out_dir / "run_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    # Output 4: QA run log example (static, deterministic; no API calls)
    qa_src = data_dir / "qa_run_example.json"
    qa_dst = out_dir / "qa_run_example.json"
    qa_dst.write_text(qa_src.read_text(encoding="utf-8"), encoding="utf-8")

    print("Reproduction Case 2 generated.")
    print(f"- PDFs: {pdf_d1}, {pdf_s1}, {pdf_s2}")
    print(f"- Outputs: {violations_csv}, {summary_csv}, {out_dir / 'run_manifest.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
