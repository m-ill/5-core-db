# 5-core-db
**Evidence‑Linked 5‑Core Construction Data Integration and Audit‑Ready Design Compliance Checking**

This repository is a **reproducibility package** for the paper/manuscript on an **evidence‑linked (fine‑grained provenance) ontology knowledge graph** that unifies heterogeneous construction deliverables (“5‑core”) and enables **audit‑ready rule‑based compliance checking** and **grounded LLM reporting**.

> **Core idea:** Knowledge is stored as **assertions that must carry Evidence**.  
> If an assertion has **no Evidence link (`isDerivedFrom`)**, it **cannot be ingested** into the knowledge graph (traceability as an invariant).

---

## What this repo provides
- **Case 1 — Traceability Invariant Validation**  
  A minimal end‑to‑end reproduction showing that **every assertion in the KG is traceable** to at least one Evidence record with a **fine‑grained locator** (page+bbox / table cell / clause locator / timestamp).
- **Case 2 — Scaffold (Scaffolding) Compliance Checking**  
  A reproduction of rule‑based checking over a scaffold drawing dataset (anonymized/synthetic) where each violation is stored with **dual evidence**:
  - `E_actual`: evidence for extracted actual value (e.g., drawing bbox)
  - `E_clause`: evidence for the referenced clause/requirement (e.g., clause page+ID)
- **LLM Evaluation (Grounded Responses)**  
  A reproducible workflow for **data‑card bounded** question answering/report generation, where LLM outputs are constrained to retrieved Evidence/clauses.

---

## Concept glossary (quick)
- **5‑core data**: Drawing / Calculation·Analysis / 3D‑BIM / Document·Report / Field·Physical
- **Evidence**: a fine‑grained provenance unit that stores a locator  
  (e.g., `page+bbox`, `sheet+(row,col)`, `clauseId+page`, `timestamp`)
- **Traceability invariant**: “No Evidence → No assertion in KG”
- **Dual evidence** (for compliance results): actual evidence + clause evidence

---

## Repository structure
> The exact file names may evolve; the top‑level entry points are the three reproduction folders.

```

repro_case1/        # Case 1: traceability invariant validation
repro_case2/        # Case 2: scaffold compliance checking (rules R1–R10)
repro_llm_eval/     # LLM evaluation using data cards + evidence constraints
README.md

# (optional) data/         # synthetic/anonymized inputs

# (optional) figures/      # paper figures (SVG/PDF)

# (optional) requirements.txt

````

---

## Installation
### Prerequisites
- Python (recommended: 3.9+)
- A clean virtual environment is strongly recommended.

### Setup
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate

pip install -U pip
pip install -r requirements.txt
````

> If `requirements.txt` is not present in your branch, install dependencies described inside each `repro_*` folder.

---

## Reproducing the paper results

### Case 1 — Traceability invariant validation

```bash
python repro_case1/reproduce_case1.py
```

**Expected outcome**

* Outputs that summarize **Evidence coverage** (assertions with ≥1 Evidence / total assertions)
* A traceability audit that checks whether locators actually jump back to a valid source position
* A “rejection test” demonstrating that assertions without Evidence are blocked at ingestion

### Case 2 — Scaffold compliance checking

```bash
python repro_case2/reproduce_case2.py
```

**Expected outcome**

* Rule evaluation results (e.g., R1–R10) with **pass/fail**
* Violation instances stored with **dual evidence** (`E_actual`, `E_clause`)
* Optional accuracy metrics if ground truth labels are provided in the reproduction package

### LLM evaluation (data‑card bounded generation)

```bash
python repro_llm_eval/run_llm_eval.py
```

**Expected outcome**

* QA / report generation examples that cite Evidence (locator + clause)
* Evaluation logs for:

  * citation coverage (how many key claims include evidence)
  * hallucination rate (claims not supported by retrieved evidence)
  * abstention correctness (proper refusal when evidence is missing)

---

## Data availability & confidentiality

This repository is designed to be **publicly shareable** while preserving project confidentiality.

* **Real project identifiers** (project name, drawing numbers, internal codes) should not be published.
* **Standards / codes PDFs** (e.g., KDS documents) may be copyrighted; therefore, this repo provides:

  * anonymized clause IDs / locators
  * synthetic/anonymized sample inputs
  * reproduction scripts and minimal artifacts

If you want to reproduce with your own confidential project files, keep them **outside Git** and only store:

* file hashes, versions, and anonymized locators
* run manifests for reproducibility

---

## How to cite

If you use this repository, please cite the associated paper/manuscript and/or this GitHub repository.

### BibTeX (update metadata when the paper is finalized)

```bibtex
@article{5coredb_evidence_linked,
  title   = {Evidence-Linked 5-Core Construction Data Integration and Audit-Ready Design Compliance Checking},
  author  = {<Author list>},
  journal = {<Target journal / preprint>},
  year    = {2026},
  note    = {Reproducibility repository: https://github.com/m-ill/5-core-db}
}
```

> Recommended: add a `CITATION.cff` file to enable GitHub’s “Cite this repository” button.

---

## License

See the `LICENSE` file in this repository.

---

## Contact

* **Seok-Jae Heo** — [seokjae.heo@gmail.com](mailto:seokjae.heo@gmail.com)

---

## Korean summary (요약)

<details>
  <summary>한국어 요약 펼치기</summary>

본 저장소는 “증거연결형(evidence‑linked) 온톨로지 지식그래프” 기반 5‑core(도면/계산·분석/3D‑BIM/문서·보고서/현장·실물) 건설 데이터 통합 및
감사 가능한 준수검토(규칙 기반 자동검토)·근거 기반 LLM 응답을 위한 재현 패키지입니다.

핵심 원칙은 **모든 주장(assertion)은 최소 1개의 Evidence(isDerivedFrom)를 가져야만 저장 가능**하다는 ‘추적성 불변조건’이며,
준수검토 결과(Violation)는 **실제값 근거(E_actual) + 기준 근거(E_clause)**의 이중 근거(dual evidence)로 저장됩니다.

</details>
