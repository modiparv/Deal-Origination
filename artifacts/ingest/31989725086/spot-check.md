# Ingest spot-check

- database: `data/engine.db`
- latest run: `20260817T030036Z-104da783`
- companies in store: 5000; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## PETER CLARK & SON (ELECTRICAL) LIMITED (`gb:01314363`)

- registration: `01314363` (GB), status active, incorporated 1977-05-20
- classification: ['47540', '62090'] (sic_2007)
- records: 3 officers, 1 beneficial owners, 0 ownership statements, 1 security interests, 89 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-06-30 | 2026-03-31 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 5205 | GBP | 2025-06-30 | 2026-03-31 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| equity | 44 | GBP | 2025-06-30 | 2026-03-31 | filed | yes | `frs-core:Equity` | micro-entity |
| fixed_assets | 100 | GBP | 2025-06-30 | 2026-03-31 | filed | yes | `frs-core:FixedAssets` | micro-entity |
| net_assets | 44 | GBP | 2025-06-30 | 2026-03-31 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 807 | GBP | 2025-06-30 | 2026-03-31 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 907 | GBP | 2025-06-30 | 2026-03-31 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-06-30 | 2026-03-31 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-06-30 | 2025-03-19 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 11235 | GBP | 2024-06-30 | 2026-03-31 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| current_assets | 11235 | GBP | 2024-06-30 | 2025-03-19 | filed | no | `frs-core:CurrentAssets` | micro-entity |
| equity | 2061 | GBP | 2024-06-30 | 2025-03-19 | filed | no | `frs-core:Equity` | micro-entity |
| equity | 2061 | GBP | 2024-06-30 | 2026-03-31 | filed | yes | `frs-core:Equity` | micro-entity |
| fixed_assets | 6443 | GBP | 2024-06-30 | 2026-03-31 | filed | yes | `frs-core:FixedAssets` | micro-entity |
| fixed_assets | 6443 | GBP | 2024-06-30 | 2025-03-19 | filed | no | `frs-core:FixedAssets` | micro-entity |
| net_assets | 2061 | GBP | 2024-06-30 | 2026-03-31 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 2061 | GBP | 2024-06-30 | 2025-03-19 | filed | no | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 9138 | GBP | 2024-06-30 | 2025-03-19 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 9138 | GBP | 2024-06-30 | 2026-03-31 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 15581 | GBP | 2024-06-30 | 2026-03-31 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 15581 | GBP | 2024-06-30 | 2025-03-19 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-06-30 | 2025-03-19 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-06-30 | 2024-03-28 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 103 | GBP | 2023-06-30 | 2024-03-28 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 103 | GBP | 2023-06-30 | 2025-03-19 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| current_assets | 103 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `frs-core:CurrentAssets` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3003 | GBP | 2023-06-30 | 2024-03-28 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 80 | GBP | 2023-06-30 | 2024-03-28 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity | 3083 | GBP | 2023-06-30 | 2025-03-19 | filed | yes | `frs-core:Equity` | micro-entity |
| fixed_assets | 7256 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `frs-core:FixedAssets` | total-exemption-full |
| fixed_assets | 7256 | GBP | 2023-06-30 | 2025-03-19 | filed | yes | `frs-core:FixedAssets` | micro-entity |
| net_assets | 3083 | GBP | 2023-06-30 | 2025-03-19 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 3083 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -3320 | GBP | 2023-06-30 | 2025-03-19 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -4173 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 3083 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 3936 | GBP | 2023-06-30 | 2025-03-19 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2022-06-30 | 2024-03-28 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 54 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 54 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 274 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 80 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 3851 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 354 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -3497 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 354 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2025-03-19: `{"superseded_document_id": "gb:01314363:doc:ypgrvaycnVgEaUODb6VDyNPEX0S9EsQm9f2PwdykGDw", "restatements": [{"concept": "net_current_assets", "period_end": "2023-06-30", "old_value": "-4173.0000", "new`

## CIVICA UK LIMITED (`gb:01628868`)

- registration: `01628868` (GB), status active, incorporated 1982-04-14
- classification: ['62090'] (sic_2007)
- records: 69 officers, 1 beneficial owners, 0 ownership statements, 17 security interests, 282 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## CM BEASY LIMITED (`gb:01865517`)

- registration: `01865517` (GB), status active, incorporated 1984-11-22
- classification: ['62020', '72190'] (sic_2007)
- records: 11 officers, 2 beneficial owners, 0 ownership statements, 2 security interests, 115 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | xbrli:pure | 2025-03-31 | 2025-12-15 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 209979 | GBP | 2025-03-31 | 2025-12-15 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 529919 | GBP | 2025-03-31 | 2025-12-15 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 319940 | GBP | 2025-03-31 | 2025-12-15 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -400278 | GBP | 2025-03-31 | 2025-12-15 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 102500 | GBP | 2025-03-31 | 2025-12-15 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 13875 | GBP | 2025-03-31 | 2025-12-15 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | -297778 | GBP | 2025-03-31 | 2025-12-15 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -311653 | GBP | 2025-03-31 | 2025-12-15 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -297778 | GBP | 2025-03-31 | 2025-12-15 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0 | xbrli:pure | 2024-03-31 | 2025-12-15 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 0 | xbrli:pure | 2024-03-31 | 2024-12-19 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 89026 | GBP | 2024-03-31 | 2025-12-15 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| cash | 89026 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 219747 | GBP | 2024-03-31 | 2025-12-15 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| current_assets | 219747 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 130721 | GBP | 2024-03-31 | 2025-12-15 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| debtors | 130721 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -194991 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 102500 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -194991 | GBP | 2024-03-31 | 2025-12-15 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 102500 | GBP | 2024-03-31 | 2025-12-15 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 17695 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `frs-core:FixedAssets` | total-exemption-full |
| fixed_assets | 17695 | GBP | 2024-03-31 | 2025-12-15 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | -92491 | GBP | 2024-03-31 | 2025-12-15 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | -92491 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -110186 | GBP | 2024-03-31 | 2025-12-15 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -110186 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -92491 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -92491 | GBP | 2024-03-31 | 2025-12-15 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0 | xbrli:pure | 2023-03-31 | 2024-12-19 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 0 | xbrli:pure | 2023-03-31 | 2023-11-21 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 122336 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 122336 | GBP | 2023-03-31 | 2023-11-21 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 254436 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 254436 | GBP | 2023-03-31 | 2023-11-21 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original'}` | 132100 | GBP | 2023-03-31 | 2023-11-21 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 132100 | GBP | 2023-03-31 | 2023-11-21 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 132100 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 29599 | GBP | 2023-03-31 | 2023-11-21 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -72901 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 102500 | GBP | 2023-03-31 | 2023-11-21 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 102500 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -72901 | GBP | 2023-03-31 | 2023-11-21 | filed | yes | `ns5:Equity` | total-exemption-full |
| fixed_assets | 17224 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 29599 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 12375 | GBP | 2023-03-31 | 2023-11-21 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 12375 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 29599 | GBP | 2023-03-31 | 2023-11-21 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 29599 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 0 | xbrli:pure | 2022-03-31 | 2023-11-21 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 437 | GBP | 2022-03-31 | 2023-11-21 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 250275 | GBP | 2022-03-31 | 2023-11-21 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 249838 | GBP | 2022-03-31 | 2023-11-21 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original'}` | 249838 | GBP | 2022-03-31 | 2023-11-21 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 199228 | GBP | 2022-03-31 | 2023-11-21 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 102500 | GBP | 2022-03-31 | 2023-11-21 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 96728 | GBP | 2022-03-31 | 2023-11-21 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 187933 | GBP | 2022-03-31 | 2023-11-21 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 199228 | GBP | 2022-03-31 | 2023-11-21 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

Coverage @ 2025-03-31: 9/21 concepts available (average_employees, cash, current_assets, debtors, equity, fixed_assets, net_assets, net_current_assets, total_assets_less_current_liabilities)
- `creditors_after_one_year`: filed_without_concept — absent though regime 'total-exemption-full' typically includes it
- `creditors_within_one_year`: filed_without_concept — absent though regime 'total-exemption-full' typically includes it
- `depreciation_amortisation`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `gross_profit`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `operating_profit`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `profit_before_tax`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `profit_for_period`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `retained_earnings`: filed_without_concept — absent though regime 'total-exemption-full' typically includes it
- `revenue`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `share_capital`: filed_without_concept — absent though regime 'total-exemption-full' typically includes it
- `staff_costs`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `tax_charge`: filed_without_concept — regime 'total-exemption-full' omits this concept

## INTERWORLD COMPUTERS LIMITED (`gb:02046516`)

- registration: `02046516` (GB), status active, incorporated 1986-08-14
- classification: ['62020'] (sic_2007)
- records: 2 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 87 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | iso4217:GBP | 2025-08-31 | 2026-03-01 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 49081 | GBP | 2025-08-31 | 2026-03-01 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 20582 | GBP | 2025-08-31 | 2026-03-01 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 28431 | GBP | 2025-08-31 | 2026-03-01 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 68 | GBP | 2025-08-31 | 2026-03-01 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 28431 | GBP | 2025-08-31 | 2026-03-01 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 28499 | GBP | 2025-08-31 | 2026-03-01 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 28431 | GBP | 2025-08-31 | 2026-03-01 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-08-31 | 2025-04-27 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-08-31 | 2026-03-01 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 50831 | GBP | 2024-08-31 | 2026-03-01 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 50831 | GBP | 2024-08-31 | 2025-04-27 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 22869 | GBP | 2024-08-31 | 2025-04-27 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 22869 | GBP | 2024-08-31 | 2026-03-01 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 27877 | GBP | 2024-08-31 | 2025-04-27 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 27877 | GBP | 2024-08-31 | 2026-03-01 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 85 | GBP | 2024-08-31 | 2025-04-27 | filed | no | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 85 | GBP | 2024-08-31 | 2026-03-01 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 27877 | GBP | 2024-08-31 | 2026-03-01 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 27877 | GBP | 2024-08-31 | 2025-04-27 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 27962 | GBP | 2024-08-31 | 2026-03-01 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 27962 | GBP | 2024-08-31 | 2025-04-27 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 27877 | GBP | 2024-08-31 | 2025-04-27 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 27877 | GBP | 2024-08-31 | 2026-03-01 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-08-31 | 2025-04-27 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-08-31 | 2024-03-09 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 46163 | GBP | 2023-08-31 | 2025-04-27 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 46163 | GBP | 2023-08-31 | 2024-03-09 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 18628 | GBP | 2023-08-31 | 2025-04-27 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 18628 | GBP | 2023-08-31 | 2024-03-09 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 27429 | GBP | 2023-08-31 | 2025-04-27 | filed | yes | `uk-core:Equity` | micro-entity |
| equity | -27429 | GBP | 2023-08-31 | 2024-03-09 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 106 | GBP | 2023-08-31 | 2025-04-27 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 106 | GBP | 2023-08-31 | 2024-03-09 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | -27429 | GBP | 2023-08-31 | 2024-03-09 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 27429 | GBP | 2023-08-31 | 2025-04-27 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 27535 | GBP | 2023-08-31 | 2025-04-27 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -27535 | GBP | 2023-08-31 | 2024-03-09 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 27429 | GBP | 2023-08-31 | 2025-04-27 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -27429 | GBP | 2023-08-31 | 2024-03-09 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 40550 | GBP | 2022-08-31 | 2024-03-09 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 13577 | GBP | 2022-08-31 | 2024-03-09 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -26843 | GBP | 2022-08-31 | 2024-03-09 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 130 | GBP | 2022-08-31 | 2024-03-09 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | -26843 | GBP | 2022-08-31 | 2024-03-09 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -26973 | GBP | 2022-08-31 | 2024-03-09 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -26843 | GBP | 2022-08-31 | 2024-03-09 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

Coverage @ 2025-08-31: 8/21 concepts available (average_employees, creditors_within_one_year, current_assets, equity, fixed_assets, net_assets, net_current_assets, total_assets_less_current_liabilities)
- `cash`: filed_without_concept — regime 'micro-entity' omits this concept
- `creditors_after_one_year`: filed_without_concept — regime 'micro-entity' omits this concept
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

- event restatement @ 2025-04-27: `{"superseded_document_id": "gb:02046516:doc:r5FvutcsyXjvz3YKEanmqeBBHX6yGhJvE2Oj_6tY_rE", "restatements": [{"concept": "net_current_assets", "period_end": "2023-08-31", "old_value": "-27535.0000", "ne`

## MOVABLE TYPE LIMITED (`gb:02199624`)

- registration: `02199624` (GB), status active, incorporated 1987-11-27
- classification: ['62012'] (sic_2007)
- records: 2 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 92 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-03-31 | 2025-12-01 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 16080 | GBP | 2025-03-31 | 2025-12-01 | filed | yes | `core:CashBankOnHand` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 16889 | GBP | 2025-03-31 | 2025-12-01 | filed | yes | `core:Creditors` | unaudited-abridged |
| current_assets | 27158 | GBP | 2025-03-31 | 2025-12-01 | filed | yes | `core:CurrentAssets` | unaudited-abridged |
| debtors | 11078 | GBP | 2025-03-31 | 2025-12-01 | filed | yes | `core:Debtors` | unaudited-abridged |
| equity | 11047 | GBP | 2025-03-31 | 2025-12-01 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2025-03-31 | 2025-12-01 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 11045 | GBP | 2025-03-31 | 2025-12-01 | filed | yes | `core:Equity` | unaudited-abridged |
| fixed_assets | 778 | GBP | 2025-03-31 | 2025-12-01 | filed | yes | `core:FixedAssets` | unaudited-abridged |
| net_assets | 11047 | GBP | 2025-03-31 | 2025-12-01 | filed | yes | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 10269 | GBP | 2025-03-31 | 2025-12-01 | filed | yes | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 11047 | GBP | 2025-03-31 | 2025-12-01 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 1 | xbrli:pure | 2024-03-31 | 2024-08-19 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| average_employees | 1 | xbrli:pure | 2024-03-31 | 2025-12-01 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 47459 | GBP | 2024-03-31 | 2024-08-19 | filed | no | `core:CashBankOnHand` | unaudited-abridged |
| cash | 47459 | GBP | 2024-03-31 | 2025-12-01 | filed | yes | `core:CashBankOnHand` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 26723 | GBP | 2024-03-31 | 2025-12-01 | filed | yes | `core:Creditors` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 26723 | GBP | 2024-03-31 | 2024-08-19 | filed | no | `core:Creditors` | unaudited-abridged |
| current_assets | 61926 | GBP | 2024-03-31 | 2025-12-01 | filed | yes | `core:CurrentAssets` | unaudited-abridged |
| current_assets | 61926 | GBP | 2024-03-31 | 2024-08-19 | filed | no | `core:CurrentAssets` | unaudited-abridged |
| debtors | 14467 | GBP | 2024-03-31 | 2025-12-01 | filed | yes | `core:Debtors` | unaudited-abridged |
| debtors | 14467 | GBP | 2024-03-31 | 2024-08-19 | filed | no | `core:Debtors` | unaudited-abridged |
| equity | 35796 | GBP | 2024-03-31 | 2024-08-19 | filed | no | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 35794 | GBP | 2024-03-31 | 2025-12-01 | filed | yes | `core:Equity` | unaudited-abridged |
| equity | 35796 | GBP | 2024-03-31 | 2025-12-01 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-03-31 | 2025-12-01 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-03-31 | 2024-08-19 | filed | no | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 35794 | GBP | 2024-03-31 | 2024-08-19 | filed | no | `core:Equity` | unaudited-abridged |
| fixed_assets | 593 | GBP | 2024-03-31 | 2024-08-19 | filed | no | `core:FixedAssets` | unaudited-abridged |
| fixed_assets | 593 | GBP | 2024-03-31 | 2025-12-01 | filed | yes | `core:FixedAssets` | unaudited-abridged |
| net_assets | 35796 | GBP | 2024-03-31 | 2025-12-01 | filed | yes | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_assets | 35796 | GBP | 2024-03-31 | 2024-08-19 | filed | no | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 35203 | GBP | 2024-03-31 | 2025-12-01 | filed | yes | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 35203 | GBP | 2024-03-31 | 2024-08-19 | filed | no | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 35796 | GBP | 2024-03-31 | 2025-12-01 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 35796 | GBP | 2024-03-31 | 2024-08-19 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 1 | xbrli:pure | 2023-03-31 | 2023-07-21 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| average_employees | 1 | xbrli:pure | 2023-03-31 | 2024-08-19 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 10984 | GBP | 2023-03-31 | 2024-08-19 | filed | yes | `core:CashBankOnHand` | unaudited-abridged |
| cash | 10984 | GBP | 2023-03-31 | 2023-07-21 | filed | no | `core:CashBankOnHand` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 8434 | GBP | 2023-03-31 | 2024-08-19 | filed | yes | `core:Creditors` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 8434 | GBP | 2023-03-31 | 2023-07-21 | filed | no | `core:Creditors` | unaudited-abridged |
| current_assets | 21329 | GBP | 2023-03-31 | 2024-08-19 | filed | yes | `core:CurrentAssets` | unaudited-abridged |
| current_assets | 21329 | GBP | 2023-03-31 | 2023-07-21 | filed | no | `core:CurrentAssets` | unaudited-abridged |
| debtors | 10345 | GBP | 2023-03-31 | 2024-08-19 | filed | yes | `core:Debtors` | unaudited-abridged |
| debtors | 10345 | GBP | 2023-03-31 | 2023-07-21 | filed | no | `core:Debtors` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-03-31 | 2023-07-21 | filed | no | `core:Equity` | unaudited-abridged |
| equity | 12990 | GBP | 2023-03-31 | 2024-08-19 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 12988 | GBP | 2023-03-31 | 2023-07-21 | filed | no | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 12988 | GBP | 2023-03-31 | 2024-08-19 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-03-31 | 2024-08-19 | filed | yes | `core:Equity` | unaudited-abridged |
| equity | 12990 | GBP | 2023-03-31 | 2023-07-21 | filed | no | `core:Equity` | unaudited-abridged |
| fixed_assets | 95 | GBP | 2023-03-31 | 2024-08-19 | filed | yes | `core:FixedAssets` | unaudited-abridged |
| fixed_assets | 95 | GBP | 2023-03-31 | 2023-07-21 | filed | no | `core:FixedAssets` | unaudited-abridged |
| net_assets | 12990 | GBP | 2023-03-31 | 2024-08-19 | filed | yes | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_assets | 12990 | GBP | 2023-03-31 | 2023-07-21 | filed | no | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 12895 | GBP | 2023-03-31 | 2024-08-19 | filed | yes | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 12895 | GBP | 2023-03-31 | 2023-07-21 | filed | no | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 12990 | GBP | 2023-03-31 | 2024-08-19 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 12990 | GBP | 2023-03-31 | 2023-07-21 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 1 | xbrli:pure | 2022-03-31 | 2023-07-21 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 37816 | GBP | 2022-03-31 | 2023-07-21 | filed | yes | `core:CashBankOnHand` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 16985 | GBP | 2022-03-31 | 2023-07-21 | filed | yes | `core:Creditors` | unaudited-abridged |
| current_assets | 41358 | GBP | 2022-03-31 | 2023-07-21 | filed | yes | `core:CurrentAssets` | unaudited-abridged |
| debtors | 3542 | GBP | 2022-03-31 | 2023-07-21 | filed | yes | `core:Debtors` | unaudited-abridged |
| equity | 24691 | GBP | 2022-03-31 | 2023-07-21 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2022-03-31 | 2023-07-21 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 24689 | GBP | 2022-03-31 | 2023-07-21 | filed | yes | `core:Equity` | unaudited-abridged |
| fixed_assets | 318 | GBP | 2022-03-31 | 2023-07-21 | filed | yes | `core:FixedAssets` | unaudited-abridged |
| net_assets | 24691 | GBP | 2022-03-31 | 2023-07-21 | filed | yes | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 24373 | GBP | 2022-03-31 | 2023-07-21 | filed | yes | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 24691 | GBP | 2022-03-31 | 2023-07-21 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |

_No coverage facts for the latest run._

## MCCARTHY TAYLOR SYSTEMS LIMITED (`gb:02339960`)

- registration: `02339960` (GB), status active, incorporated 1989-01-26
- classification: ['62012'] (sic_2007)
- records: 9 officers, 0 beneficial owners, 1 ownership statements, 0 security interests, 100 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 10 | xbrli:pure | 2025-07-31 | 2026-01-16 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 1208270 | GBP | 2025-07-31 | 2026-01-16 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 521516 | GBP | 2025-07-31 | 2026-01-16 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 1396487 | GBP | 2025-07-31 | 2026-01-16 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 188217 | GBP | 2025-07-31 | 2026-01-16 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 188217 | GBP | 2025-07-31 | 2026-01-16 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 1000 | GBP | 2025-07-31 | 2026-01-16 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 888676 | GBP | 2025-07-31 | 2026-01-16 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 889676 | GBP | 2025-07-31 | 2026-01-16 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 889676 | GBP | 2025-07-31 | 2026-01-16 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 874971 | GBP | 2025-07-31 | 2026-01-16 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 892284 | GBP | 2025-07-31 | 2026-01-16 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 10 | xbrli:pure | 2024-07-31 | 2026-01-16 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 10 | xbrli:pure | 2024-07-31 | 2025-02-12 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 909602 | GBP | 2024-07-31 | 2025-02-12 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 909602 | GBP | 2024-07-31 | 2026-01-16 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 489178 | GBP | 2024-07-31 | 2025-02-12 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 489178 | GBP | 2024-07-31 | 2026-01-16 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 1105261 | GBP | 2024-07-31 | 2025-02-12 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 1105261 | GBP | 2024-07-31 | 2026-01-16 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 195659 | GBP | 2024-07-31 | 2025-02-12 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 195659 | GBP | 2024-07-31 | 2025-02-12 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 195659 | GBP | 2024-07-31 | 2026-01-16 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 195659 | GBP | 2024-07-31 | 2026-01-16 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 620807 | GBP | 2024-07-31 | 2025-02-12 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 1000 | GBP | 2024-07-31 | 2025-02-12 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 1000 | GBP | 2024-07-31 | 2026-01-16 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 619807 | GBP | 2024-07-31 | 2025-02-12 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 619807 | GBP | 2024-07-31 | 2026-01-16 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 620807 | GBP | 2024-07-31 | 2026-01-16 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 620807 | GBP | 2024-07-31 | 2025-02-12 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 620807 | GBP | 2024-07-31 | 2026-01-16 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 616083 | GBP | 2024-07-31 | 2025-02-12 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 616083 | GBP | 2024-07-31 | 2026-01-16 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 623415 | GBP | 2024-07-31 | 2025-02-12 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 623415 | GBP | 2024-07-31 | 2026-01-16 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 13 | xbrli:pure | 2023-07-31 | 2024-04-03 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 13 | xbrli:pure | 2023-07-31 | 2025-02-12 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 1143262 | GBP | 2023-07-31 | 2024-04-03 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 1143262 | GBP | 2023-07-31 | 2025-02-12 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 415397 | GBP | 2023-07-31 | 2024-04-03 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 415397 | GBP | 2023-07-31 | 2025-02-12 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 1333646 | GBP | 2023-07-31 | 2025-02-12 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 1333646 | GBP | 2023-07-31 | 2024-04-03 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors | 190384 | GBP | 2023-07-31 | 2025-02-12 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 190384 | GBP | 2023-07-31 | 2024-04-03 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 190384 | GBP | 2023-07-31 | 2024-04-03 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 190384 | GBP | 2023-07-31 | 2025-02-12 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 925070 | GBP | 2023-07-31 | 2025-02-12 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 926070 | GBP | 2023-07-31 | 2024-04-03 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 1000 | GBP | 2023-07-31 | 2025-02-12 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 925070 | GBP | 2023-07-31 | 2024-04-03 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 926070 | GBP | 2023-07-31 | 2025-02-12 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 1000 | GBP | 2023-07-31 | 2024-04-03 | filed | no | `core:Equity` | total-exemption-full |
| net_assets | 926070 | GBP | 2023-07-31 | 2025-02-12 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 926070 | GBP | 2023-07-31 | 2024-04-03 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 918249 | GBP | 2023-07-31 | 2024-04-03 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 918249 | GBP | 2023-07-31 | 2025-02-12 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 928678 | GBP | 2023-07-31 | 2024-04-03 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 928678 | GBP | 2023-07-31 | 2025-02-12 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 14 | xbrli:pure | 2022-07-31 | 2024-04-03 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 817551 | GBP | 2022-07-31 | 2024-04-03 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 361977 | GBP | 2022-07-31 | 2024-04-03 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 985928 | GBP | 2022-07-31 | 2024-04-03 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 168377 | GBP | 2022-07-31 | 2024-04-03 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 168377 | GBP | 2022-07-31 | 2024-04-03 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 636708 | GBP | 2022-07-31 | 2024-04-03 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 1000 | GBP | 2022-07-31 | 2024-04-03 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 635708 | GBP | 2022-07-31 | 2024-04-03 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 636708 | GBP | 2022-07-31 | 2024-04-03 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 623951 | GBP | 2022-07-31 | 2024-04-03 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 639700 | GBP | 2022-07-31 | 2024-04-03 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## SUEDON LIMITED (`gb:02463026`)

- registration: `02463026` (GB), status active, incorporated 1990-01-24
- classification: ['62020'] (sic_2007)
- records: 2 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 83 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | iso4217:GBP | 2026-01-30 | 2026-03-02 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2026-01-30 | 2026-03-02 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2026-01-30 | 2026-03-02 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 0 | GBP | 2026-01-30 | 2026-03-02 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 0 | GBP | 2026-01-30 | 2026-03-02 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2026-01-30 | 2026-03-02 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 0 | GBP | 2026-01-30 | 2026-03-02 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 0 | GBP | 2026-01-30 | 2026-03-02 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 0 | GBP | 2026-01-30 | 2026-03-02 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2025-01-30 | 2025-02-14 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2025-01-30 | 2026-03-02 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2025-01-30 | 2026-03-02 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2025-01-30 | 2025-02-14 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2025-01-30 | 2025-02-14 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2025-01-30 | 2026-03-02 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 0 | GBP | 2025-01-30 | 2025-02-14 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 0 | GBP | 2025-01-30 | 2026-03-02 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 0 | GBP | 2025-01-30 | 2025-02-14 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 0 | GBP | 2025-01-30 | 2026-03-02 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2025-01-30 | 2026-03-02 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 0 | GBP | 2025-01-30 | 2025-02-14 | filed | no | `uk-core:FixedAssets` | micro-entity |
| net_assets | 0 | GBP | 2025-01-30 | 2026-03-02 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 0 | GBP | 2025-01-30 | 2025-02-14 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 0 | GBP | 2025-01-30 | 2026-03-02 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 0 | GBP | 2025-01-30 | 2025-02-14 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 0 | GBP | 2025-01-30 | 2025-02-14 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 0 | GBP | 2025-01-30 | 2026-03-02 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2024-01-30 | 2024-12-03 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2024-01-30 | 2025-02-14 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2024-01-30 | 2024-12-03 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2024-01-30 | 2025-02-14 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2024-01-30 | 2025-02-14 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2024-01-30 | 2024-12-03 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 0 | GBP | 2024-01-30 | 2025-02-14 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 0 | GBP | 2024-01-30 | 2024-12-03 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | 0 | GBP | 2024-01-30 | 2024-12-03 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 0 | GBP | 2024-01-30 | 2025-02-14 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2024-01-30 | 2024-12-03 | filed | no | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 0 | GBP | 2024-01-30 | 2025-02-14 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 0 | GBP | 2024-01-30 | 2025-02-14 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 0 | GBP | 2024-01-30 | 2024-12-03 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 0 | GBP | 2024-01-30 | 2024-12-03 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 0 | GBP | 2024-01-30 | 2025-02-14 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 0 | GBP | 2024-01-30 | 2025-02-14 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 0 | GBP | 2024-01-30 | 2024-12-03 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2023-01-30 | 2024-12-03 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2023-01-30 | 2024-12-03 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2023-01-30 | 2024-12-03 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 0 | GBP | 2023-01-30 | 2024-12-03 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 0 | GBP | 2023-01-30 | 2024-12-03 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2023-01-30 | 2024-12-03 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 0 | GBP | 2023-01-30 | 2024-12-03 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 0 | GBP | 2023-01-30 | 2024-12-03 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 0 | GBP | 2023-01-30 | 2024-12-03 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## APRIL TRAINING EXECUTIVE LIMITED (`gb:02577354`)

- registration: `02577354` (GB), status active, incorporated 1991-01-28
- classification: ['62012'] (sic_2007)
- records: 6 officers, 3 beneficial owners, 0 ownership statements, 0 security interests, 90 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-01-31 | 2025-10-26 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 39598 | GBP | 2025-01-31 | 2025-10-26 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| equity | 38223 | GBP | 2025-01-31 | 2025-10-26 | filed | yes | `frs-core:Equity` | micro-entity |
| fixed_assets | 2232 | GBP | 2025-01-31 | 2025-10-26 | filed | yes | `frs-core:FixedAssets` | micro-entity |
| net_assets | 38223 | GBP | 2025-01-31 | 2025-10-26 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 36561 | GBP | 2025-01-31 | 2025-10-26 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 38793 | GBP | 2025-01-31 | 2025-10-26 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-01-31 | 2024-10-25 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-01-31 | 2025-10-26 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 42549 | GBP | 2024-01-31 | 2025-10-26 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| current_assets | 42549 | GBP | 2024-01-31 | 2024-10-25 | filed | no | `frs-core:CurrentAssets` | micro-entity |
| equity | 42015 | GBP | 2024-01-31 | 2025-10-26 | filed | yes | `frs-core:Equity` | micro-entity |
| equity | 42015 | GBP | 2024-01-31 | 2024-10-25 | filed | no | `frs-core:Equity` | micro-entity |
| fixed_assets | 1041 | GBP | 2024-01-31 | 2025-10-26 | filed | yes | `frs-core:FixedAssets` | micro-entity |
| fixed_assets | 1041 | GBP | 2024-01-31 | 2024-10-25 | filed | no | `frs-core:FixedAssets` | micro-entity |
| net_assets | 42015 | GBP | 2024-01-31 | 2025-10-26 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 42015 | GBP | 2024-01-31 | 2024-10-25 | filed | no | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 40974 | GBP | 2024-01-31 | 2024-10-25 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 40974 | GBP | 2024-01-31 | 2025-10-26 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 42015 | GBP | 2024-01-31 | 2024-10-25 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 42015 | GBP | 2024-01-31 | 2025-10-26 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-01-31 | 2024-10-25 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-01-31 | 2023-10-31 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 40947 | GBP | 2023-01-31 | 2024-10-25 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| current_assets | 40947 | GBP | 2023-01-31 | 2023-10-31 | filed | no | `frs-core:CurrentAssets` | micro-entity |
| equity | 41664 | GBP | 2023-01-31 | 2023-10-31 | filed | no | `frs-core:Equity` | micro-entity |
| equity | 41664 | GBP | 2023-01-31 | 2024-10-25 | filed | yes | `frs-core:Equity` | micro-entity |
| fixed_assets | 1562 | GBP | 2023-01-31 | 2024-10-25 | filed | yes | `frs-core:FixedAssets` | micro-entity |
| fixed_assets | 1562 | GBP | 2023-01-31 | 2023-10-31 | filed | no | `frs-core:FixedAssets` | micro-entity |
| net_assets | 41664 | GBP | 2023-01-31 | 2023-10-31 | filed | no | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 41664 | GBP | 2023-01-31 | 2024-10-25 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 40102 | GBP | 2023-01-31 | 2024-10-25 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 40102 | GBP | 2023-01-31 | 2023-10-31 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 41664 | GBP | 2023-01-31 | 2023-10-31 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 41664 | GBP | 2023-01-31 | 2024-10-25 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2022-01-31 | 2023-10-31 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 51643 | GBP | 2022-01-31 | 2023-10-31 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| equity | 50365 | GBP | 2022-01-31 | 2023-10-31 | filed | yes | `frs-core:Equity` | micro-entity |
| fixed_assets | 2082 | GBP | 2022-01-31 | 2023-10-31 | filed | yes | `frs-core:FixedAssets` | micro-entity |
| net_assets | 50365 | GBP | 2022-01-31 | 2023-10-31 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 48283 | GBP | 2022-01-31 | 2023-10-31 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 50365 | GBP | 2022-01-31 | 2023-10-31 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

Coverage @ 2025-01-31: 7/21 concepts available (average_employees, current_assets, equity, fixed_assets, net_assets, net_current_assets, total_assets_less_current_liabilities)
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

## THURRA LIMITED (`gb:02686271`)

- registration: `02686271` (GB), status active, incorporated 1992-02-11
- classification: ['71129', '71200'] (sic_2007)
- records: 8 officers, 4 beneficial owners, 0 ownership statements, 0 security interests, 112 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 30 | xbrli:pure | 2024-12-31 | 2025-09-17 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 59261 | GBP | 2024-12-31 | 2025-09-17 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 1103233 | GBP | 2024-12-31 | 2025-09-17 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 1043972 | GBP | 2024-12-31 | 2025-09-17 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1212661 | GBP | 2024-12-31 | 2025-09-17 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-12-31 | 2025-09-17 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 516244 | GBP | 2024-12-31 | 2025-09-17 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 1212761 | GBP | 2024-12-31 | 2025-09-17 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 705477 | GBP | 2024-12-31 | 2025-09-17 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1221721 | GBP | 2024-12-31 | 2025-09-17 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 20 | xbrli:pure | 2023-12-31 | 2024-08-31 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 20 | xbrli:pure | 2023-12-31 | 2025-09-17 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 346332 | GBP | 2023-12-31 | 2025-09-17 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| cash | 346332 | GBP | 2023-12-31 | 2024-08-31 | filed | no | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 1334766 | GBP | 2023-12-31 | 2024-08-31 | filed | no | `frs-core:CurrentAssets` | total-exemption-full |
| current_assets | 1334766 | GBP | 2023-12-31 | 2025-09-17 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 988434 | GBP | 2023-12-31 | 2025-09-17 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| debtors | 988434 | GBP | 2023-12-31 | 2024-08-31 | filed | no | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-12-31 | 2024-08-31 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1268345 | GBP | 2023-12-31 | 2025-09-17 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-12-31 | 2025-09-17 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1268345 | GBP | 2023-12-31 | 2024-08-31 | filed | no | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 377092 | GBP | 2023-12-31 | 2025-09-17 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| fixed_assets | 377092 | GBP | 2023-12-31 | 2024-08-31 | filed | no | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 1268445 | GBP | 2023-12-31 | 2025-09-17 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 1268445 | GBP | 2023-12-31 | 2024-08-31 | filed | no | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 891476 | GBP | 2023-12-31 | 2024-08-31 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 891476 | GBP | 2023-12-31 | 2025-09-17 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1268568 | GBP | 2023-12-31 | 2024-08-31 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1268568 | GBP | 2023-12-31 | 2025-09-17 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 17 | xbrli:pure | 2023-03-31 | 2024-08-31 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 17 | xbrli:pure | 2023-03-31 | 2023-12-12 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 156689 | GBP | 2023-03-31 | 2024-08-31 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| cash | 156689 | GBP | 2023-03-31 | 2023-12-12 | filed | no | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 1050203 | GBP | 2023-03-31 | 2024-08-31 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| current_assets | 1050203 | GBP | 2023-03-31 | 2023-12-12 | filed | no | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 893514 | GBP | 2023-03-31 | 2024-08-31 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| debtors | 893514 | GBP | 2023-03-31 | 2023-12-12 | filed | no | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1171019 | GBP | 2023-03-31 | 2023-12-12 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-03-31 | 2024-08-31 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-03-31 | 2023-12-12 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1171019 | GBP | 2023-03-31 | 2024-08-31 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 321174 | GBP | 2023-03-31 | 2023-12-12 | filed | no | `frs-core:FixedAssets` | total-exemption-full |
| fixed_assets | 321174 | GBP | 2023-03-31 | 2024-08-31 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 1171119 | GBP | 2023-03-31 | 2024-08-31 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 1171119 | GBP | 2023-03-31 | 2023-12-12 | filed | no | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 850447 | GBP | 2023-03-31 | 2023-12-12 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 850447 | GBP | 2023-03-31 | 2024-08-31 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1171621 | GBP | 2023-03-31 | 2023-12-12 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1171621 | GBP | 2023-03-31 | 2024-08-31 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 12 | xbrli:pure | 2022-03-31 | 2023-12-12 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 147081 | GBP | 2022-03-31 | 2023-12-12 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 1200294 | GBP | 2022-03-31 | 2023-12-12 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 1053213 | GBP | 2022-03-31 | 2023-12-12 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1062809 | GBP | 2022-03-31 | 2023-12-12 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2022-03-31 | 2023-12-12 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 51528 | GBP | 2022-03-31 | 2023-12-12 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 1062909 | GBP | 2022-03-31 | 2023-12-12 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1015242 | GBP | 2022-03-31 | 2023-12-12 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1066770 | GBP | 2022-03-31 | 2023-12-12 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._
