# Ingest spot-check

- database: `data/engine.db`
- latest run: `20260811T034541Z-099a09fb`
- companies in store: 1800; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## STOTFOLD ENGINEERING CO.LIMITED (`gb:00910564`)

- registration: `00910564` (GB), status active, incorporated 1967-07-13
- classification: ['71129'] (sic_2007)
- records: 5 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 102 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.03 | xbrli:pure | 2025-07-31 | 2026-04-16 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 31202 | GBP | 2025-07-31 | 2026-04-16 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 100646 | GBP | 2025-07-31 | 2026-04-16 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 69188 | GBP | 2025-07-31 | 2026-04-16 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 2204 | GBP | 2025-07-31 | 2026-04-16 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 69188 | GBP | 2025-07-31 | 2026-04-16 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 69444 | GBP | 2025-07-31 | 2026-04-16 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 71648 | GBP | 2025-07-31 | 2026-04-16 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0.02 | xbrli:pure | 2024-07-31 | 2026-04-16 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-07-31 | 2025-03-17 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 22497 | GBP | 2024-07-31 | 2026-04-16 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 22497 | GBP | 2024-07-31 | 2025-03-17 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 83145 | GBP | 2024-07-31 | 2026-04-16 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 83145 | GBP | 2024-07-31 | 2025-03-17 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 60756 | GBP | 2024-07-31 | 2026-04-16 | filed | yes | `core:Equity` | micro-entity |
| equity | 60756 | GBP | 2024-07-31 | 2025-03-17 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 2502 | GBP | 2024-07-31 | 2026-04-16 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 2502 | GBP | 2024-07-31 | 2025-03-17 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | 60756 | GBP | 2024-07-31 | 2026-04-16 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 60648 | GBP | 2024-07-31 | 2026-04-16 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 63150 | GBP | 2024-07-31 | 2026-04-16 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-07-31 | 2024-04-13 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-07-31 | 2025-03-17 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 20376 | GBP | 2023-07-31 | 2024-04-13 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 20376 | GBP | 2023-07-31 | 2025-03-17 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 137057 | GBP | 2023-07-31 | 2025-03-17 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 137057 | GBP | 2023-07-31 | 2024-04-13 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 116809 | GBP | 2023-07-31 | 2024-04-13 | filed | no | `core:Equity` | micro-entity |
| equity | 116809 | GBP | 2023-07-31 | 2025-03-17 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 2306 | GBP | 2023-07-31 | 2025-03-17 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 2306 | GBP | 2023-07-31 | 2024-04-13 | filed | no | `core:FixedAssets` | micro-entity |
| average_employees | 2 | xbrli:pure | 2022-07-31 | 2024-04-13 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5827 | GBP | 2022-07-31 | 2024-04-13 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 119714 | GBP | 2022-07-31 | 2024-04-13 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 114684 | GBP | 2022-07-31 | 2024-04-13 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 2316 | GBP | 2022-07-31 | 2024-04-13 | filed | yes | `core:FixedAssets` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2026-04-16: `{"superseded_document_id": "gb:00910564:doc:bwQylwpwptJqCwT24scF1i2RQz2ItQBDqEVxd0PW8eo", "restatements": [{"concept": "average_employees", "period_end": "2024-07-31", "old_value": "2.0000", "new_valu`

## GILMORE HANKEY KIRKE LIMITED (`gb:01192845`)

- registration: `01192845` (GB), status active, incorporated 1974-12-06
- classification: ['71111'] (sic_2007)
- records: 17 officers, 1 beneficial owners, 0 ownership statements, 4 security interests, 157 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## ARCONTECH LIMITED (`gb:01350766`)

- registration: `01350766` (GB), status active, incorporated 1978-01-31
- classification: ['62020', '62090'] (sic_2007)
- records: 12 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 131 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## INTERGRAPH (UK) LIMITED (`gb:01457814`)

- registration: `01457814` (GB), status active, incorporated 1979-10-30
- classification: ['62020'] (sic_2007)
- records: 29 officers, 3 beneficial owners, 0 ownership statements, 3 security interests, 177 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## CONTINENTAL LIMITED (`gb:01727463`)

- registration: `01727463` (GB), status active, incorporated 1983-05-31
- classification: ['62012', '62090'] (sic_2007)
- records: 8 officers, 3 beneficial owners, 0 ownership statements, 2 security interests, 127 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 11 | xbrli:pure | 2025-03-31 | 2025-12-19 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 48178 | GBP | 2025-03-31 | 2025-12-19 | filed | yes | `core:CashBankOnHand` | unaudited-abridged |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 36699 | GBP | 2025-03-31 | 2025-12-19 | filed | yes | `core:Creditors` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 206649 | GBP | 2025-03-31 | 2025-12-19 | filed | yes | `core:Creditors` | unaudited-abridged |
| current_assets | 616058 | GBP | 2025-03-31 | 2025-12-19 | filed | yes | `core:CurrentAssets` | unaudited-abridged |
| debtors | 527460 | GBP | 2025-03-31 | 2025-12-19 | filed | yes | `core:Debtors` | unaudited-abridged |
| equity | 636323 | GBP | 2025-03-31 | 2025-12-19 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 636223 | GBP | 2025-03-31 | 2025-12-19 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-03-31 | 2025-12-19 | filed | yes | `core:Equity` | unaudited-abridged |
| fixed_assets | 263613 | GBP | 2025-03-31 | 2025-12-19 | filed | yes | `core:FixedAssets` | unaudited-abridged |
| net_assets | 636323 | GBP | 2025-03-31 | 2025-12-19 | filed | yes | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 409409 | GBP | 2025-03-31 | 2025-12-19 | filed | yes | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 673022 | GBP | 2025-03-31 | 2025-12-19 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 11 | xbrli:pure | 2024-03-31 | 2024-12-20 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| average_employees | 11 | xbrli:pure | 2024-03-31 | 2025-12-19 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 50317 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:CashBankOnHand` | unaudited-abridged |
| cash | 50317 | GBP | 2024-03-31 | 2025-12-19 | filed | yes | `core:CashBankOnHand` | unaudited-abridged |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 44082 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:Creditors` | unaudited-abridged |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 44082 | GBP | 2024-03-31 | 2025-12-19 | filed | yes | `core:Creditors` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 168516 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:Creditors` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 168516 | GBP | 2024-03-31 | 2025-12-19 | filed | yes | `core:Creditors` | unaudited-abridged |
| current_assets | 610291 | GBP | 2024-03-31 | 2025-12-19 | filed | yes | `core:CurrentAssets` | unaudited-abridged |
| current_assets | 610291 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:CurrentAssets` | unaudited-abridged |
| debtors | 534183 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:Debtors` | unaudited-abridged |
| debtors | 534183 | GBP | 2024-03-31 | 2025-12-19 | filed | yes | `core:Debtors` | unaudited-abridged |
| equity | 707715 | GBP | 2024-03-31 | 2025-12-19 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-03-31 | 2025-12-19 | filed | yes | `core:Equity` | unaudited-abridged |
| equity | 707715 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 707615 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 707615 | GBP | 2024-03-31 | 2025-12-19 | filed | yes | `core:Equity` | unaudited-abridged |
| fixed_assets | 310022 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:FixedAssets` | unaudited-abridged |
| fixed_assets | 310022 | GBP | 2024-03-31 | 2025-12-19 | filed | yes | `core:FixedAssets` | unaudited-abridged |
| net_assets | 707715 | GBP | 2024-03-31 | 2025-12-19 | filed | yes | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_assets | 707715 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 441775 | GBP | 2024-03-31 | 2025-12-19 | filed | yes | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 441775 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 751797 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 751797 | GBP | 2024-03-31 | 2025-12-19 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 11 | xbrli:pure | 2023-03-31 | 2023-12-05 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| average_employees | 11 | xbrli:pure | 2023-03-31 | 2024-12-20 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 302248 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:CashBankOnHand` | unaudited-abridged |
| cash | 302248 | GBP | 2023-03-31 | 2023-12-05 | filed | no | `core:CashBankOnHand` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 315148 | GBP | 2023-03-31 | 2023-12-05 | filed | no | `core:Creditors` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 315147 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:Creditors` | unaudited-abridged |
| current_assets | 847184 | GBP | 2023-03-31 | 2023-12-05 | filed | no | `core:CurrentAssets` | unaudited-abridged |
| current_assets | 847184 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:CurrentAssets` | unaudited-abridged |
| debtors | 528487 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:Debtors` | unaudited-abridged |
| debtors | 528487 | GBP | 2023-03-31 | 2023-12-05 | filed | no | `core:Debtors` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 817184 | GBP | 2023-03-31 | 2023-12-05 | filed | no | `core:Equity` | unaudited-abridged |
| equity | 817284 | GBP | 2023-03-31 | 2023-12-05 | filed | no | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-03-31 | 2023-12-05 | filed | no | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 817185 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:Equity` | unaudited-abridged |
| equity | 817285 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:Equity` | unaudited-abridged |
| fixed_assets | 285248 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:FixedAssets` | unaudited-abridged |
| fixed_assets | 285248 | GBP | 2023-03-31 | 2023-12-05 | filed | no | `core:FixedAssets` | unaudited-abridged |
| net_assets | 817284 | GBP | 2023-03-31 | 2023-12-05 | filed | no | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_assets | 817285 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 532037 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 532036 | GBP | 2023-03-31 | 2023-12-05 | filed | no | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 817284 | GBP | 2023-03-31 | 2023-12-05 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 817285 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 11 | xbrli:pure | 2022-03-31 | 2023-12-05 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 46007 | GBP | 2022-03-31 | 2023-12-05 | filed | yes | `core:CashBankOnHand` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 294817 | GBP | 2022-03-31 | 2023-12-05 | filed | yes | `core:Creditors` | unaudited-abridged |
| current_assets | 769642 | GBP | 2022-03-31 | 2023-12-05 | filed | yes | `core:CurrentAssets` | unaudited-abridged |
| debtors | 709704 | GBP | 2022-03-31 | 2023-12-05 | filed | yes | `core:Debtors` | unaudited-abridged |
| equity | 778457 | GBP | 2022-03-31 | 2023-12-05 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2022-03-31 | 2023-12-05 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 778357 | GBP | 2022-03-31 | 2023-12-05 | filed | yes | `core:Equity` | unaudited-abridged |
| fixed_assets | 303632 | GBP | 2022-03-31 | 2023-12-05 | filed | yes | `core:FixedAssets` | unaudited-abridged |
| net_assets | 778457 | GBP | 2022-03-31 | 2023-12-05 | filed | yes | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 474825 | GBP | 2022-03-31 | 2023-12-05 | filed | yes | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 778457 | GBP | 2022-03-31 | 2023-12-05 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |

Coverage @ 2025-03-31: 11/21 concepts available (average_employees, cash, creditors_after_one_year, creditors_within_one_year, current_assets, debtors, equity, fixed_assets, net_assets, net_current_assets, total_assets_less_current_liabilities)
- `depreciation_amortisation`: filed_without_concept — regime 'unaudited-abridged' omits this concept
- `gross_profit`: filed_without_concept — regime 'unaudited-abridged' omits this concept
- `operating_profit`: filed_without_concept — regime 'unaudited-abridged' omits this concept
- `profit_before_tax`: filed_without_concept — regime 'unaudited-abridged' omits this concept
- `profit_for_period`: filed_without_concept — regime 'unaudited-abridged' omits this concept
- `retained_earnings`: filed_without_concept — absent though regime 'unaudited-abridged' typically includes it
- `revenue`: filed_without_concept — regime 'unaudited-abridged' omits this concept
- `share_capital`: filed_without_concept — absent though regime 'unaudited-abridged' typically includes it
- `staff_costs`: filed_without_concept — regime 'unaudited-abridged' omits this concept
- `tax_charge`: filed_without_concept — regime 'unaudited-abridged' omits this concept

- event restatement @ 2024-12-20: `{"superseded_document_id": "gb:01727463:doc:dIF_pHss564vLRapTHkg5P1SeHHnxl8yprvNtfl8GHo", "restatements": [{"concept": "creditors_within_one_year", "period_end": "2023-03-31", "old_value": "315148.000`

## B.C. & T. CONSULTANTS LIMITED (`gb:02056951`)

- registration: `02056951` (GB), status active, incorporated 1986-09-22
- classification: ['71121'] (sic_2007)
- records: 12 officers, 4 beneficial owners, 0 ownership statements, 4 security interests, 144 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.12 | xbrli:pure | 2024-12-31 | 2025-09-10 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 565882 | GBP | 2024-12-31 | 2025-09-10 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| current_assets | 1625083 | GBP | 2024-12-31 | 2025-09-10 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 926201 | GBP | 2024-12-31 | 2025-09-10 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 926201 | GBP | 2024-12-31 | 2025-09-10 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 760 | GBP | 2024-12-31 | 2025-09-10 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1314967 | GBP | 2024-12-31 | 2025-09-10 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 2250 | GBP | 2024-12-31 | 2025-09-10 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 1317977 | GBP | 2024-12-31 | 2025-09-10 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 1317977 | GBP | 2024-12-31 | 2025-09-10 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1244134 | GBP | 2024-12-31 | 2025-09-10 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1329472 | GBP | 2024-12-31 | 2025-09-10 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 10 | xbrli:pure | 2023-12-31 | 2024-06-12 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 0.1 | xbrli:pure | 2023-12-31 | 2025-09-10 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 848419 | GBP | 2023-12-31 | 2025-09-10 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 848419 | GBP | 2023-12-31 | 2024-06-12 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 1540441 | GBP | 2023-12-31 | 2024-06-12 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 1540441 | GBP | 2023-12-31 | 2025-09-10 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 654022 | GBP | 2023-12-31 | 2024-06-12 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 654022 | GBP | 2023-12-31 | 2024-06-12 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 654022 | GBP | 2023-12-31 | 2025-09-10 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 654022 | GBP | 2023-12-31 | 2025-09-10 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 2250 | GBP | 2023-12-31 | 2025-09-10 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 760 | GBP | 2023-12-31 | 2025-09-10 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 839063 | GBP | 2023-12-31 | 2025-09-10 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 836053 | GBP | 2023-12-31 | 2025-09-10 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 2250 | GBP | 2023-12-31 | 2024-06-12 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 760 | GBP | 2023-12-31 | 2024-06-12 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 836053 | GBP | 2023-12-31 | 2024-06-12 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 839063 | GBP | 2023-12-31 | 2024-06-12 | filed | no | `ns5:Equity` | total-exemption-full |
| net_assets | 839063 | GBP | 2023-12-31 | 2024-06-12 | filed | no | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 839063 | GBP | 2023-12-31 | 2025-09-10 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 777010 | GBP | 2023-12-31 | 2025-09-10 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 777010 | GBP | 2023-12-31 | 2024-06-12 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 848805 | GBP | 2023-12-31 | 2024-06-12 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 848805 | GBP | 2023-12-31 | 2025-09-10 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 7 | xbrli:pure | 2022-11-30 | 2024-06-12 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 366801 | GBP | 2022-11-30 | 2024-06-12 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 1810965 | GBP | 2022-11-30 | 2024-06-12 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1377504 | GBP | 2022-11-30 | 2024-06-12 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 1377504 | GBP | 2022-11-30 | 2024-06-12 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 773335 | GBP | 2022-11-30 | 2024-06-12 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 2250 | GBP | 2022-11-30 | 2024-06-12 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 750 | GBP | 2022-11-30 | 2024-06-12 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 770335 | GBP | 2022-11-30 | 2024-06-12 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 773335 | GBP | 2022-11-30 | 2024-06-12 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 754818 | GBP | 2022-11-30 | 2024-06-12 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 773335 | GBP | 2022-11-30 | 2024-06-12 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

Coverage @ 2024-12-31: 8/21 concepts available (average_employees, cash, current_assets, debtors, equity, net_assets, net_current_assets, total_assets_less_current_liabilities)
- `creditors_after_one_year`: filed_without_concept — absent though regime 'total-exemption-full' typically includes it
- `creditors_within_one_year`: filed_without_concept — absent though regime 'total-exemption-full' typically includes it
- `depreciation_amortisation`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `fixed_assets`: filed_without_concept — absent though regime 'total-exemption-full' typically includes it
- `gross_profit`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `operating_profit`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `profit_before_tax`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `profit_for_period`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `retained_earnings`: filed_without_concept — absent though regime 'total-exemption-full' typically includes it
- `revenue`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `share_capital`: filed_without_concept — absent though regime 'total-exemption-full' typically includes it
- `staff_costs`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `tax_charge`: filed_without_concept — regime 'total-exemption-full' omits this concept

- event restatement @ 2025-09-10: `{"superseded_document_id": "gb:02056951:doc:WV0iuF8bDRB5Kcf8yU0D-ft3FG380U2nFTbb4mHxyHk", "restatements": [{"concept": "average_employees", "period_end": "2023-12-31", "old_value": "10.0000", "new_val`

## R.P. DATA LIMITED (`gb:02277070`)

- registration: `02277070` (GB), status active, incorporated 1988-07-14
- classification: ['62020'] (sic_2007)
- records: 2 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 86 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | iso4217:GBP | 2025-06-30 | 2026-03-30 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 180 | GBP | 2025-06-30 | 2026-03-30 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 32152 | GBP | 2025-06-30 | 2026-03-30 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 31972 | GBP | 2025-06-30 | 2026-03-30 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 31972 | GBP | 2025-06-30 | 2026-03-30 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 31972 | GBP | 2025-06-30 | 2026-03-30 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 31972 | GBP | 2025-06-30 | 2026-03-30 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-06-30 | 2026-03-30 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-06-30 | 2025-03-28 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 300 | GBP | 2024-06-30 | 2025-03-28 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 300 | GBP | 2024-06-30 | 2026-03-30 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 32452 | GBP | 2024-06-30 | 2026-03-30 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 32452 | GBP | 2024-06-30 | 2025-03-28 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | 32152 | GBP | 2024-06-30 | 2026-03-30 | filed | yes | `uk-core:Equity` | micro-entity |
| equity | 32152 | GBP | 2024-06-30 | 2025-03-28 | filed | no | `uk-core:Equity` | micro-entity |
| net_assets | 32152 | GBP | 2024-06-30 | 2025-03-28 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 32152 | GBP | 2024-06-30 | 2026-03-30 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 32152 | GBP | 2024-06-30 | 2026-03-30 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 32152 | GBP | 2024-06-30 | 2025-03-28 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 32152 | GBP | 2024-06-30 | 2026-03-30 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 32152 | GBP | 2024-06-30 | 2025-03-28 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-06-30 | 2025-03-28 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-06-30 | 2024-03-28 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2023-06-30 | 2025-03-28 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 56452 | GBP | 2023-06-30 | 2025-03-28 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 56452 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | 56452 | GBP | 2023-06-30 | 2025-03-28 | filed | yes | `uk-core:Equity` | micro-entity |
| equity | 56452 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `uk-core:Equity` | micro-entity |
| net_assets | 56452 | GBP | 2023-06-30 | 2025-03-28 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 56452 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 56452 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 56452 | GBP | 2023-06-30 | 2025-03-28 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 56452 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 56452 | GBP | 2023-06-30 | 2025-03-28 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2022-06-30 | 2024-03-28 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2632 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 87209 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 84577 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 84577 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 84577 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 84577 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

Coverage @ 2025-06-30: 7/21 concepts available (average_employees, creditors_within_one_year, current_assets, equity, net_assets, net_current_assets, total_assets_less_current_liabilities)
- `cash`: filed_without_concept — regime 'micro-entity' omits this concept
- `creditors_after_one_year`: filed_without_concept — regime 'micro-entity' omits this concept
- `debtors`: filed_without_concept — regime 'micro-entity' omits this concept
- `depreciation_amortisation`: filed_without_concept — regime 'micro-entity' omits this concept
- `fixed_assets`: filed_without_concept — regime 'micro-entity' omits this concept
- `gross_profit`: filed_without_concept — regime 'micro-entity' omits this concept
- `operating_profit`: filed_without_concept — regime 'micro-entity' omits this concept
- `profit_before_tax`: filed_without_concept — regime 'micro-entity' omits this concept
- `profit_for_period`: filed_without_concept — regime 'micro-entity' omits this concept
- `retained_earnings`: filed_without_concept — regime 'micro-entity' omits this concept
- `revenue`: filed_without_concept — regime 'micro-entity' omits this concept
- `share_capital`: filed_without_concept — regime 'micro-entity' omits this concept
- `staff_costs`: filed_without_concept — regime 'micro-entity' omits this concept
- `tax_charge`: filed_without_concept — regime 'micro-entity' omits this concept

## CENTRAL DRIVE LIMITED (`gb:02462530`)

- registration: `02462530` (GB), status active, incorporated 1990-01-23
- classification: ['62020'] (sic_2007)
- records: 4 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 99 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | xbrli:pure | 2025-04-30 | 2025-09-25 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 12139 | GBP | 2025-04-30 | 2025-09-25 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 362364 | GBP | 2025-04-30 | 2025-09-25 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 350700 | GBP | 2025-04-30 | 2025-09-25 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 362364 | GBP | 2025-04-30 | 2025-09-25 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 12139 | GBP | 2025-04-30 | 2025-09-25 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 362839 | GBP | 2025-04-30 | 2025-09-25 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2024-04-30 | 2025-09-25 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | xbrli:pure | 2024-04-30 | 2024-12-15 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 14455 | GBP | 2024-04-30 | 2025-09-25 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 14455 | GBP | 2024-04-30 | 2024-12-15 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 363017 | GBP | 2024-04-30 | 2024-12-15 | filed | no | `core:Equity` | micro-entity |
| equity | 363017 | GBP | 2024-04-30 | 2025-09-25 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 349037 | GBP | 2024-04-30 | 2024-12-15 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 349037 | GBP | 2024-04-30 | 2025-09-25 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 363017 | GBP | 2024-04-30 | 2024-12-15 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 363017 | GBP | 2024-04-30 | 2025-09-25 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 14455 | GBP | 2024-04-30 | 2025-09-25 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 14455 | GBP | 2024-04-30 | 2024-12-15 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 363492 | GBP | 2024-04-30 | 2025-09-25 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 363492 | GBP | 2024-04-30 | 2024-12-15 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2023-04-30 | 2024-12-15 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | xbrli:pure | 2023-04-30 | 2024-01-15 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 54468 | GBP | 2023-04-30 | 2024-01-15 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 54468 | GBP | 2023-04-30 | 2024-12-15 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 446933 | GBP | 2023-04-30 | 2024-01-15 | filed | no | `core:Equity` | micro-entity |
| equity | 446933 | GBP | 2023-04-30 | 2024-12-15 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 392940 | GBP | 2023-04-30 | 2024-01-15 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 392940 | GBP | 2023-04-30 | 2024-12-15 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 446933 | GBP | 2023-04-30 | 2024-01-15 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 446933 | GBP | 2023-04-30 | 2024-12-15 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 54468 | GBP | 2023-04-30 | 2024-12-15 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 54468 | GBP | 2023-04-30 | 2024-01-15 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 447408 | GBP | 2023-04-30 | 2024-01-15 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 447408 | GBP | 2023-04-30 | 2024-12-15 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2022-04-30 | 2024-01-15 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 19819 | GBP | 2022-04-30 | 2024-01-15 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 470044 | GBP | 2022-04-30 | 2024-01-15 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 450700 | GBP | 2022-04-30 | 2024-01-15 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 470044 | GBP | 2022-04-30 | 2024-01-15 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 19819 | GBP | 2022-04-30 | 2024-01-15 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 470519 | GBP | 2022-04-30 | 2024-01-15 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

Coverage @ 2025-04-30: 7/21 concepts available (average_employees, current_assets, equity, fixed_assets, net_assets, net_current_assets, total_assets_less_current_liabilities)
- `cash`: filed_without_concept — regime 'micro-entity' omits this concept
- `creditors_after_one_year`: filed_without_concept — regime 'micro-entity' omits this concept
- `creditors_within_one_year`: filed_without_concept — absent though regime 'micro-entity' typically includes it
- `debtors`: filed_without_concept — regime 'micro-entity' omits this concept
- `depreciation_amortisation`: filed_without_concept — regime 'micro-entity' omits this concept
- `gross_profit`: filed_without_concept — regime 'micro-entity' omits this concept
- `operating_profit`: filed_without_concept — regime 'micro-entity' omits this concept
- `profit_before_tax`: filed_without_concept — regime 'micro-entity' omits this concept
- `profit_for_period`: filed_without_concept — regime 'micro-entity' omits this concept
- `retained_earnings`: filed_without_concept — regime 'micro-entity' omits this concept
- `revenue`: filed_without_concept — regime 'micro-entity' omits this concept
- `share_capital`: filed_without_concept — regime 'micro-entity' omits this concept
- `staff_costs`: filed_without_concept — regime 'micro-entity' omits this concept
- `tax_charge`: filed_without_concept — regime 'micro-entity' omits this concept

## PIPELINE TECHNOLOGY LIMITED (`gb:02654842`)

- registration: `02654842` (GB), status active, incorporated 1991-10-17
- classification: ['46620', '71121'] (sic_2007)
- records: 16 officers, 3 beneficial owners, 0 ownership statements, 2 security interests, 140 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.14 | xbrli:pure | 2024-12-31 | 2025-12-17 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 367343 | GBP | 2024-12-31 | 2025-12-17 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2024-12-31 | 2025-12-17 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 630351 | GBP | 2024-12-31 | 2025-12-17 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 2493008 | GBP | 2024-12-31 | 2025-12-17 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 1532591 | GBP | 2024-12-31 | 2025-12-17 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1532591 | GBP | 2024-12-31 | 2025-12-17 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1862094 | GBP | 2024-12-31 | 2025-12-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 46 | GBP | 2024-12-31 | 2025-12-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 1887194 | GBP | 2024-12-31 | 2025-12-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 24956 | GBP | 2024-12-31 | 2025-12-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 98 | GBP | 2024-12-31 | 2025-12-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShares'}` | 46 | GBP | 2024-12-31 | 2025-12-17 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 1887194 | GBP | 2024-12-31 | 2025-12-17 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1862657 | GBP | 2024-12-31 | 2025-12-17 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1887272 | GBP | 2024-12-31 | 2025-12-17 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0.13 | xbrli:pure | 2023-12-31 | 2025-12-17 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 13 | xbrli:pure | 2023-12-31 | 2024-08-06 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 495630 | GBP | 2023-12-31 | 2024-08-06 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 495630 | GBP | 2023-12-31 | 2025-12-17 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 1112 | GBP | 2023-12-31 | 2025-12-17 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 1112 | GBP | 2023-12-31 | 2024-08-06 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 908023 | GBP | 2023-12-31 | 2024-08-06 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 908023 | GBP | 2023-12-31 | 2025-12-17 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 2770575 | GBP | 2023-12-31 | 2025-12-17 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 2770575 | GBP | 2023-12-31 | 2024-08-06 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1731384 | GBP | 2023-12-31 | 2025-12-17 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1731384 | GBP | 2023-12-31 | 2024-08-06 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 1731384 | GBP | 2023-12-31 | 2024-08-06 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 1731384 | GBP | 2023-12-31 | 2025-12-17 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 24956 | GBP | 2023-12-31 | 2024-08-06 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShares'}` | 46 | GBP | 2023-12-31 | 2024-08-06 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 24956 | GBP | 2023-12-31 | 2025-12-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 98 | GBP | 2023-12-31 | 2024-08-06 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 46 | GBP | 2023-12-31 | 2025-12-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 1893648 | GBP | 2023-12-31 | 2025-12-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1868548 | GBP | 2023-12-31 | 2024-08-06 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1868548 | GBP | 2023-12-31 | 2025-12-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 98 | GBP | 2023-12-31 | 2025-12-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 1893648 | GBP | 2023-12-31 | 2024-08-06 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 46 | GBP | 2023-12-31 | 2024-08-06 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShares'}` | 46 | GBP | 2023-12-31 | 2025-12-17 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 1893648 | GBP | 2023-12-31 | 2025-12-17 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 1893648 | GBP | 2023-12-31 | 2024-08-06 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1862552 | GBP | 2023-12-31 | 2025-12-17 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1862552 | GBP | 2023-12-31 | 2024-08-06 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1897788 | GBP | 2023-12-31 | 2025-12-17 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1897788 | GBP | 2023-12-31 | 2024-08-06 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 13 | xbrli:pure | 2022-12-31 | 2023-09-29 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 13 | xbrli:pure | 2022-12-31 | 2024-08-06 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 463423 | GBP | 2022-12-31 | 2023-09-29 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 463423 | GBP | 2022-12-31 | 2024-08-06 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 7779 | GBP | 2022-12-31 | 2023-09-29 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 7779 | GBP | 2022-12-31 | 2024-08-06 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 512016 | GBP | 2022-12-31 | 2024-08-06 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 512016 | GBP | 2022-12-31 | 2023-09-29 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 2194470 | GBP | 2022-12-31 | 2023-09-29 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 2194470 | GBP | 2022-12-31 | 2024-08-06 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1298219 | GBP | 2022-12-31 | 2023-09-29 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1298219 | GBP | 2022-12-31 | 2024-08-06 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 1298219 | GBP | 2022-12-31 | 2024-08-06 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 1298219 | GBP | 2022-12-31 | 2023-09-29 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShares'}` | 46 | GBP | 2022-12-31 | 2023-09-29 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 24956 | GBP | 2022-12-31 | 2023-09-29 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShares'}` | 46 | GBP | 2022-12-31 | 2024-08-06 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 24956 | GBP | 2022-12-31 | 2024-08-06 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 98 | GBP | 2022-12-31 | 2023-09-29 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 98 | GBP | 2022-12-31 | 2024-08-06 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 46 | GBP | 2022-12-31 | 2023-09-29 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1685839 | GBP | 2022-12-31 | 2023-09-29 | filed | no | `core:Equity` | total-exemption-full |
| equity | 1710939 | GBP | 2022-12-31 | 2023-09-29 | filed | no | `core:Equity` | total-exemption-full |
| equity | 1710939 | GBP | 2022-12-31 | 2024-08-06 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1685839 | GBP | 2022-12-31 | 2024-08-06 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 46 | GBP | 2022-12-31 | 2024-08-06 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 1710939 | GBP | 2022-12-31 | 2024-08-06 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 1710939 | GBP | 2022-12-31 | 2023-09-29 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1682454 | GBP | 2022-12-31 | 2024-08-06 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1682454 | GBP | 2022-12-31 | 2023-09-29 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1722521 | GBP | 2022-12-31 | 2023-09-29 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1722521 | GBP | 2022-12-31 | 2024-08-06 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 13 | xbrli:pure | 2021-12-31 | 2023-09-29 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 688460 | GBP | 2021-12-31 | 2023-09-29 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2021-12-31 | 2023-09-29 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 993942 | GBP | 2021-12-31 | 2023-09-29 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 2497083 | GBP | 2021-12-31 | 2023-09-29 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 1499404 | GBP | 2021-12-31 | 2023-09-29 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1499404 | GBP | 2021-12-31 | 2023-09-29 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 98 | GBP | 2021-12-31 | 2023-09-29 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 46 | GBP | 2021-12-31 | 2023-09-29 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 1523006 | GBP | 2021-12-31 | 2023-09-29 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShares'}` | 46 | GBP | 2021-12-31 | 2023-09-29 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1497906 | GBP | 2021-12-31 | 2023-09-29 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 24956 | GBP | 2021-12-31 | 2023-09-29 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 1523006 | GBP | 2021-12-31 | 2023-09-29 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1503141 | GBP | 2021-12-31 | 2023-09-29 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1527089 | GBP | 2021-12-31 | 2023-09-29 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

Coverage @ 2024-12-31: 10/21 concepts available (average_employees, cash, creditors_after_one_year, creditors_within_one_year, current_assets, debtors, equity, net_assets, net_current_assets, total_assets_less_current_liabilities)
- `depreciation_amortisation`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `fixed_assets`: filed_without_concept — absent though regime 'total-exemption-full' typically includes it
- `gross_profit`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `operating_profit`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `profit_before_tax`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `profit_for_period`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `retained_earnings`: filed_without_concept — absent though regime 'total-exemption-full' typically includes it
- `revenue`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `share_capital`: filed_without_concept — absent though regime 'total-exemption-full' typically includes it
- `staff_costs`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `tax_charge`: filed_without_concept — regime 'total-exemption-full' omits this concept

- event restatement @ 2025-12-17: `{"superseded_document_id": "gb:02654842:doc:0EiFEpRwVipr1ynul737rlbkmYk6pzjUmAANgEStdI0", "restatements": [{"concept": "average_employees", "period_end": "2023-12-31", "old_value": "13.0000", "new_val`
