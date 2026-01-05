# Repro Case 2 (Runnable Public Artifact)

이 폴더는 리뷰어/외부 연구자가 “evidence locator가 실제로 가리키는” 공개 가능한 입력/산출물을 사용해, Case 2의 핵심 개념(dual evidence + run manifest)을 end-to-end로 재현할 수 있도록 만든 최소 실행 패키지입니다.

## One-click reproduction

### Linux/macOS

```bash
make reproduce_case2
```

If `make` is not available:

```bash
python3 repro_case2/reproduce_case2.py
```

### Windows (CMD)

```bat
repro_case2\\reproduce_case2.bat
```

### Windows (PowerShell)

```powershell
.\repro_case2\reproduce_case2.ps1
```

If you prefer a direct Python command:

```powershell
py -3 repro_case2\reproduce_case2.py
```

## Outputs

생성 파일(기본 경로):

- `repro_case2/build/D1_drawing.pdf` (public drawing PDF, coordRef=public-grid-2400x3600)
- `repro_case2/build/S1_kds_standard.pdf` (public KDS standard PDF, includes KDS-C1)
- `repro_case2/build/S2_company_standard.pdf` (public company standard PDF, includes INT-C2/INT-C4)
- `repro_case2/outputs/violation_instances.csv` (full violation list with dual evidence locators)
- `repro_case2/outputs/table4_summary.csv` (per-rule summary; Table 4 format)
- `repro_case2/outputs/case2_eval_metrics.json` (TP/FP/FN + micro precision/recall/F1; deterministic)
- `repro_case2/outputs/run_manifest.json` (runId, tool versions, full sha256 for artifacts)
- `repro_case2/outputs/qa_run_example.json` (LLM run log example: prompts + retrieval + params + answer)

## Data sources (text-only, reproducible)

- `repro_case2/data/violations.json`: 13 example violations (R1:6, R3:4, R5:3) + locators
- `repro_case2/data/rules.json`: 10-rule metadata for summary tables
- `repro_case2/data/tex/`: LaTeX sources to generate public PDFs (D1/S1/S2)

## Notes

- 이 공개 재현 패키지는 “공개 가능한 데이터로 구조/재현 절차를 검증”하기 위한 것이며, 본문에 보고된 산업 데이터(익명화) 수치와 1:1 동일함을 전제하지 않습니다.
- LLM은 비결정성이 있으므로, `qa_run_example.json`에는 temperature=0 재현 모드와 함께 (system prompt/user prompt/retrieved evidence/answer) 기록 형식을 예시로 제공합니다.
