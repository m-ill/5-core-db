# Repro Case 1 (Traceability Validation — Public Reproduction Package)

이 폴더는 Case 1(5-core 추적성 불변조건 검증)의 **정량 결과를 공개 가능한 합성/익명 데이터로 동일하게 재현**하기 위한 최소 실행 패키지입니다.

## One-click reproduction

### Linux/macOS

```bash
python3 repro_case1/reproduce_case1.py
```

### Windows (CMD)

```bat
repro_case1\\reproduce_case1.bat
```

### Windows (PowerShell)

```powershell
.\repro_case1\reproduce_case1.ps1
```

## Outputs

- `repro_case1/outputs/table2_panelA.csv`: Table 2 Panel A에 사용된 요약 지표(acceptance rate, rejection breakdown, locator audit 등)
- `repro_case1/outputs/case1_metrics.json`: 동일 지표의 JSON 요약 + 내부 검증 체크
- `repro_case1/outputs/rejection_reasons.csv`: 후보 assertion 거부 사유 분포(집계용)
- `repro_case1/outputs/locator_audit.csv`: locator validity 감사(60 샘플; 57 success, 3 fail) 상세
- `repro_case1/outputs/rejection_test_log.txt`: evidence 누락 200/200 거부 테스트 로그(요약)
- `repro_case1/outputs/run_manifest.json`: 산출물 sha256 및 실행 환경(runId 포함)

## Notes

- 본 패키지는 “공개 가능한 입력/산출물로 프로토콜과 수치를 재현”하기 위한 것이며, 산업 데이터 기반 원천 파일(DWG/표준문서)과 추출기 코드는 포함하지 않습니다.
- 논문 본문에 보고된 Case 1 수치(Table 2 Panel A, §4.3)는 본 패키지에서 동일하게 재현됩니다.

