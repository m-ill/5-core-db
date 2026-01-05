# Repro LLM Eval (Table 6 — Public Reproduction Package)

이 폴더는 Table 6(grounded QA 평가)의 **지표 계산을 공개 가능한 라벨 데이터로 동일하게 재현**하기 위한 최소 실행 패키지입니다.

LLM 자체 생성은 모델/서빙 시점에 따라 변동될 수 있으므로, 본 패키지는 다음을 재현 대상으로 둡니다.
- (i) claim 단위 라벨링 결과(근거 제시/환각)
- (ii) abstention subset(근거 부족 프롬프트) 라벨링 결과
- (iii) Wilson interval 계산 및 Table 6 요약 값 산출

## One-click reproduction

### Linux/macOS

```bash
python3 repro_llm_eval/reproduce_llm_eval.py
```

### Windows (CMD)

```bat
repro_llm_eval\\reproduce_llm_eval.bat
```

### Windows (PowerShell)

```powershell
.\repro_llm_eval\reproduce_llm_eval.ps1
```

## Outputs

- `repro_llm_eval/outputs/claims_baseline.csv` (n=210)
- `repro_llm_eval/outputs/claims_proposed.csv` (n=210)
- `repro_llm_eval/outputs/abstention_subset.csv` (n=27; baseline/proposed)
- `repro_llm_eval/outputs/table6_summary.csv` (Table 6 요약 값)
- `repro_llm_eval/outputs/table6_metrics.json` (계산값 + 내부 체크)
- `repro_llm_eval/outputs/run_manifest.json` (sha256 포함)

## Notes

- 라벨 데이터는 공개 가능한 형태로 제공되며(익명화/합성), 논문에 보고된 Table 6 수치를 **동일하게** 재현합니다.

