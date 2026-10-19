# Ingest spot-check

- database: `data/engine.db`
- latest run: `20261019T072502Z-b3d14ee4`
- companies in store: 30600; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## PERSONAL COMPUTER SOLUTIONS LIMITED (`gb:02354856`)

- registration: `02354856` (GB), status active, incorporated 1989-03-03
- classification: ['62090'] (sic_2007)
- records: 3 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 85 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | iso4217:GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 7106 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 7332 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:CurrentAssets` | micro-entity |
| depreciation_amortisation | 0 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:DepreciationAmortisationImpairmentExpense` | micro-entity |
| equity | 226 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 226 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 226 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| profit_for_period | -11 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:ProfitLoss` | micro-entity |
| revenue | 1559 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:TurnoverRevenue` | micro-entity |
| staff_costs | 200 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | micro-entity |
| tax_charge | 0 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | micro-entity |
| total_assets_less_current_liabilities | 226 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2024-03-31 | 2024-12-20 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 8456 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 8456 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 8693 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 8693 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:CurrentAssets` | micro-entity |
| depreciation_amortisation | 0 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:DepreciationAmortisationImpairmentExpense` | micro-entity |
| depreciation_amortisation | 0 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:DepreciationAmortisationImpairmentExpense` | micro-entity |
| equity | 237 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:Equity` | micro-entity |
| equity | 237 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 0 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | 237 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 237 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 237 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 237 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| profit_for_period | -37 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:ProfitLoss` | micro-entity |
| profit_for_period | -37 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:ProfitLoss` | micro-entity |
| revenue | 1496 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:TurnoverRevenue` | micro-entity |
| revenue | 1496 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:TurnoverRevenue` | micro-entity |
| staff_costs | 200 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:StaffCostsEmployeeBenefitsExpense` | micro-entity |
| staff_costs | 200 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | micro-entity |
| tax_charge | 0 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | micro-entity |
| tax_charge | 0 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | micro-entity |
| total_assets_less_current_liabilities | 237 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 237 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2023-03-31 | 2023-12-29 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2023-03-31 | 2023-12-29 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 7051 | GBP | 2023-03-31 | 2023-12-29 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 7051 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 7325 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 7325 | GBP | 2023-03-31 | 2023-12-29 | filed | no | `core:CurrentAssets` | micro-entity |
| depreciation_amortisation | 0 | GBP | 2023-03-31 | 2023-12-29 | filed | no | `core:DepreciationAmortisationImpairmentExpense` | micro-entity |
| depreciation_amortisation | 0 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:DepreciationAmortisationImpairmentExpense` | micro-entity |
| equity | 274 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:Equity` | micro-entity |
| equity | 274 | GBP | 2023-03-31 | 2023-12-29 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 0 | GBP | 2023-03-31 | 2023-12-29 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | 274 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 274 | GBP | 2023-03-31 | 2023-12-29 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 274 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 274 | GBP | 2023-03-31 | 2023-12-29 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| profit_for_period | -33 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:ProfitLoss` | micro-entity |
| profit_for_period | -33 | GBP | 2023-03-31 | 2023-12-29 | filed | no | `core:ProfitLoss` | micro-entity |
| revenue | 2672 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:TurnoverRevenue` | micro-entity |
| revenue | 2672 | GBP | 2023-03-31 | 2023-12-29 | filed | no | `core:TurnoverRevenue` | micro-entity |
| staff_costs | 500 | GBP | 2023-03-31 | 2023-12-29 | filed | no | `core:StaffCostsEmployeeBenefitsExpense` | micro-entity |
| staff_costs | 500 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | micro-entity |
| tax_charge | 0 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | micro-entity |
| tax_charge | 0 | GBP | 2023-03-31 | 2023-12-29 | filed | no | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | micro-entity |
| total_assets_less_current_liabilities | 274 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 274 | GBP | 2023-03-31 | 2023-12-29 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2022-03-31 | 2023-12-29 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5203 | GBP | 2022-03-31 | 2023-12-29 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 5510 | GBP | 2022-03-31 | 2023-12-29 | filed | yes | `core:CurrentAssets` | micro-entity |
| depreciation_amortisation | 0 | GBP | 2022-03-31 | 2023-12-29 | filed | yes | `core:DepreciationAmortisationImpairmentExpense` | micro-entity |
| equity | 307 | GBP | 2022-03-31 | 2023-12-29 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2022-03-31 | 2023-12-29 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 307 | GBP | 2022-03-31 | 2023-12-29 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 307 | GBP | 2022-03-31 | 2023-12-29 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| profit_for_period | -8 | GBP | 2022-03-31 | 2023-12-29 | filed | yes | `core:ProfitLoss` | micro-entity |
| revenue | 2880 | GBP | 2022-03-31 | 2023-12-29 | filed | yes | `core:TurnoverRevenue` | micro-entity |
| staff_costs | 1000 | GBP | 2022-03-31 | 2023-12-29 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | micro-entity |
| tax_charge | 0 | GBP | 2022-03-31 | 2023-12-29 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | micro-entity |
| total_assets_less_current_liabilities | 307 | GBP | 2022-03-31 | 2023-12-29 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## BANXIA SOFTWARE LIMITED (`gb:02966533`)

- registration: `02966533` (GB), status active, incorporated 1994-09-09
- classification: ['62090'] (sic_2007)
- records: 5 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 82 filings, 2 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-09-30 | 2026-05-01 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 565 | GBP | 2025-09-30 | 2026-05-01 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 8291 | GBP | 2025-09-30 | 2026-05-01 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 15378 | GBP | 2025-09-30 | 2026-05-01 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 8987 | GBP | 2025-09-30 | 2026-05-01 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 15378 | GBP | 2025-09-30 | 2026-05-01 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 7726 | GBP | 2025-09-30 | 2026-05-01 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 16713 | GBP | 2025-09-30 | 2026-05-01 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-09-30 | 2026-05-01 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-09-30 | 2025-05-01 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 7535 | GBP | 2024-09-30 | 2025-05-01 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 7536 | GBP | 2024-09-30 | 2026-05-01 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 34091 | GBP | 2024-09-30 | 2025-05-01 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 34092 | GBP | 2024-09-30 | 2026-05-01 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 30035 | GBP | 2024-09-30 | 2025-05-01 | filed | no | `core:Equity` | micro-entity |
| equity | 30035 | GBP | 2024-09-30 | 2026-05-01 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 5064 | GBP | 2024-09-30 | 2025-05-01 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 5064 | GBP | 2024-09-30 | 2026-05-01 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 30035 | GBP | 2024-09-30 | 2026-05-01 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 30035 | GBP | 2024-09-30 | 2025-05-01 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 26556 | GBP | 2024-09-30 | 2026-05-01 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 26556 | GBP | 2024-09-30 | 2025-05-01 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 31620 | GBP | 2024-09-30 | 2025-05-01 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 31620 | GBP | 2024-09-30 | 2026-05-01 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-09-30 | 2025-05-01 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-09-30 | 2024-06-26 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 12823 | GBP | 2023-09-30 | 2024-06-26 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 12823 | GBP | 2023-09-30 | 2025-05-01 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 38157 | GBP | 2023-09-30 | 2024-06-26 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 38158 | GBP | 2023-09-30 | 2025-05-01 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 28683 | GBP | 2023-09-30 | 2025-05-01 | filed | yes | `core:Equity` | micro-entity |
| equity | 28682 | GBP | 2023-09-30 | 2024-06-26 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 6078 | GBP | 2023-09-30 | 2024-06-26 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 6078 | GBP | 2023-09-30 | 2025-05-01 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 28682 | GBP | 2023-09-30 | 2024-06-26 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 28683 | GBP | 2023-09-30 | 2025-05-01 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 25334 | GBP | 2023-09-30 | 2024-06-26 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 25335 | GBP | 2023-09-30 | 2025-05-01 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 31412 | GBP | 2023-09-30 | 2024-06-26 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 31413 | GBP | 2023-09-30 | 2025-05-01 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2022-09-30 | 2024-06-26 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 18261 | GBP | 2022-09-30 | 2024-06-26 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 45017 | GBP | 2022-09-30 | 2024-06-26 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 30467 | GBP | 2022-09-30 | 2024-06-26 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 6231 | GBP | 2022-09-30 | 2024-06-26 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 30467 | GBP | 2022-09-30 | 2024-06-26 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 26756 | GBP | 2022-09-30 | 2024-06-26 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 32987 | GBP | 2022-09-30 | 2024-06-26 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2025-05-01: `{"superseded_document_id": "gb:02966533:doc:WnrD99NINE-JsWSGEOY6nPDTL1cmEy3lAfRVpdg1msU", "restatements": [{"concept": "current_assets", "period_end": "2023-09-30", "old_value": "38157.0000", "new_val`
- event restatement @ 2026-05-01: `{"superseded_document_id": "gb:02966533:doc:byCFtcBU8B5rH1NNCThcW0NS2eQmfYbBldQ9VO9pgvU", "restatements": [{"concept": "current_assets", "period_end": "2024-09-30", "old_value": "34091.0000", "new_val`

## INET INFOTECH LIMITED (`gb:03357659`)

- registration: `03357659` (GB), status active, incorporated 1997-04-22
- classification: ['62020'] (sic_2007)
- records: 8 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 86 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-03-31 | 2025-11-24 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 15385 | GBP | 2025-03-31 | 2025-11-24 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 194806 | GBP | 2025-03-31 | 2025-11-24 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 196490 | GBP | 2025-03-31 | 2025-11-24 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 17857 | GBP | 2025-03-31 | 2025-11-24 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 196490 | GBP | 2025-03-31 | 2025-11-24 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 179928 | GBP | 2025-03-31 | 2025-11-24 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 197785 | GBP | 2025-03-31 | 2025-11-24 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-03-31 | 2025-11-24 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-03-31 | 2024-10-31 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 27247 | GBP | 2024-03-31 | 2024-10-31 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 27247 | GBP | 2024-03-31 | 2025-11-24 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 161727 | GBP | 2024-03-31 | 2025-11-24 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 161727 | GBP | 2024-03-31 | 2024-10-31 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 154915 | GBP | 2024-03-31 | 2024-10-31 | filed | no | `core:Equity` | micro-entity |
| equity | 154915 | GBP | 2024-03-31 | 2025-11-24 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 20678 | GBP | 2024-03-31 | 2024-10-31 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 20678 | GBP | 2024-03-31 | 2025-11-24 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 154915 | GBP | 2024-03-31 | 2024-10-31 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 154915 | GBP | 2024-03-31 | 2025-11-24 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 135629 | GBP | 2024-03-31 | 2024-10-31 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 135629 | GBP | 2024-03-31 | 2025-11-24 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 156307 | GBP | 2024-03-31 | 2024-10-31 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 156307 | GBP | 2024-03-31 | 2025-11-24 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-03-31 | 2024-10-31 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-03-31 | 2023-12-04 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 12835 | GBP | 2023-03-31 | 2023-12-04 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 12835 | GBP | 2023-03-31 | 2024-10-31 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 112791 | GBP | 2023-03-31 | 2023-12-04 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 112791 | GBP | 2023-03-31 | 2024-10-31 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 102785 | GBP | 2023-03-31 | 2023-12-04 | filed | no | `core:Equity` | micro-entity |
| equity | 102785 | GBP | 2023-03-31 | 2024-10-31 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 3392 | GBP | 2023-03-31 | 2023-12-04 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 3392 | GBP | 2023-03-31 | 2024-10-31 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 102785 | GBP | 2023-03-31 | 2023-12-04 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 102785 | GBP | 2023-03-31 | 2024-10-31 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 100756 | GBP | 2023-03-31 | 2024-10-31 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 100756 | GBP | 2023-03-31 | 2023-12-04 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 104148 | GBP | 2023-03-31 | 2024-10-31 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 104148 | GBP | 2023-03-31 | 2023-12-04 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2022-03-31 | 2023-12-04 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 11431 | GBP | 2022-03-31 | 2023-12-04 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 67911 | GBP | 2022-03-31 | 2023-12-04 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 59262 | GBP | 2022-03-31 | 2023-12-04 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 3496 | GBP | 2022-03-31 | 2023-12-04 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 59262 | GBP | 2022-03-31 | 2023-12-04 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 57198 | GBP | 2022-03-31 | 2023-12-04 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 60694 | GBP | 2022-03-31 | 2023-12-04 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## P.K.R. ENGINEERING SERVICES LIMITED (`gb:03690341`)

- registration: `03690341` (GB), status active, incorporated 1998-12-30
- classification: ['43210', '71121'] (sic_2007)
- records: 6 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 71 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | iso4217:GBP | 2025-12-31 | 2026-02-14 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 1500 | GBP | 2025-12-31 | 2026-02-14 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 16501 | GBP | 2025-12-31 | 2026-02-14 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 4826 | GBP | 2025-12-31 | 2026-02-14 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 148 | GBP | 2025-12-31 | 2026-02-14 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 16800 | GBP | 2025-12-31 | 2026-02-14 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 148 | GBP | 2025-12-31 | 2026-02-14 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 11675 | GBP | 2025-12-31 | 2026-02-14 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 5125 | GBP | 2025-12-31 | 2026-02-14 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-12-31 | 2026-02-14 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-12-31 | 2025-03-04 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 4500 | GBP | 2024-12-31 | 2025-03-04 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 4500 | GBP | 2024-12-31 | 2026-02-14 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 30367 | GBP | 2024-12-31 | 2025-03-04 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 30367 | GBP | 2024-12-31 | 2026-02-14 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 22319 | GBP | 2024-12-31 | 2025-03-04 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 22319 | GBP | 2024-12-31 | 2026-02-14 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 2 | GBP | 2024-12-31 | 2026-02-14 | filed | yes | `uk-core:Equity` | micro-entity |
| equity | 2 | GBP | 2024-12-31 | 2025-03-04 | filed | no | `uk-core:Equity` | micro-entity |
| fixed_assets | 16000 | GBP | 2024-12-31 | 2026-02-14 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 16000 | GBP | 2024-12-31 | 2025-03-04 | filed | no | `uk-core:FixedAssets` | micro-entity |
| net_assets | 2 | GBP | 2024-12-31 | 2025-03-04 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 2 | GBP | 2024-12-31 | 2026-02-14 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 8048 | GBP | 2024-12-31 | 2025-03-04 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 8048 | GBP | 2024-12-31 | 2026-02-14 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 7952 | GBP | 2024-12-31 | 2025-03-04 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 7952 | GBP | 2024-12-31 | 2026-02-14 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-12-31 | 2025-03-04 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-12-31 | 2024-02-15 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 6000 | GBP | 2023-12-31 | 2024-02-15 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 6000 | GBP | 2023-12-31 | 2025-03-04 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 32656 | GBP | 2023-12-31 | 2025-03-04 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 32656 | GBP | 2023-12-31 | 2024-02-15 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 27061 | GBP | 2023-12-31 | 2024-02-15 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 27061 | GBP | 2023-12-31 | 2025-03-04 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 8 | GBP | 2023-12-31 | 2024-02-15 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 8 | GBP | 2023-12-31 | 2025-03-04 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 15000 | GBP | 2023-12-31 | 2025-03-04 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 15000 | GBP | 2023-12-31 | 2024-02-15 | filed | no | `uk-core:FixedAssets` | micro-entity |
| net_assets | 8 | GBP | 2023-12-31 | 2025-03-04 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 8 | GBP | 2023-12-31 | 2024-02-15 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 5595 | GBP | 2023-12-31 | 2025-03-04 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 5595 | GBP | 2023-12-31 | 2024-02-15 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 9405 | GBP | 2023-12-31 | 2024-02-15 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 9405 | GBP | 2023-12-31 | 2025-03-04 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2022-12-31 | 2024-02-15 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 9000 | GBP | 2022-12-31 | 2024-02-15 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 19080 | GBP | 2022-12-31 | 2024-02-15 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 16664 | GBP | 2022-12-31 | 2024-02-15 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 4 | GBP | 2022-12-31 | 2024-02-15 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 15000 | GBP | 2022-12-31 | 2024-02-15 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 4 | GBP | 2022-12-31 | 2024-02-15 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 2416 | GBP | 2022-12-31 | 2024-02-15 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 12584 | GBP | 2022-12-31 | 2024-02-15 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## VIZAR LIMITED (`gb:04028575`)

- registration: `04028575` (GB), status active, incorporated 2000-07-06
- classification: ['62020'] (sic_2007)
- records: 4 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 66 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | xbrli:pure | 2025-07-31 | 2026-03-26 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 11813 | GBP | 2025-07-31 | 2026-03-26 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 14726 | GBP | 2025-07-31 | 2026-03-26 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 4544 | GBP | 2025-07-31 | 2026-03-26 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 4367 | GBP | 2025-07-31 | 2026-03-26 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 4544 | GBP | 2025-07-31 | 2026-03-26 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 2913 | GBP | 2025-07-31 | 2026-03-26 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 7280 | GBP | 2025-07-31 | 2026-03-26 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2024-07-31 | 2025-04-14 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | xbrli:pure | 2024-07-31 | 2026-03-26 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 10250 | GBP | 2024-07-31 | 2026-03-26 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 10249 | GBP | 2024-07-31 | 2025-04-14 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 22773 | GBP | 2024-07-31 | 2026-03-26 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 22773 | GBP | 2024-07-31 | 2025-04-14 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 13629 | GBP | 2024-07-31 | 2025-04-14 | filed | no | `core:Equity` | micro-entity |
| equity | 13628 | GBP | 2024-07-31 | 2026-03-26 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 2845 | GBP | 2024-07-31 | 2025-04-14 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 2845 | GBP | 2024-07-31 | 2026-03-26 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 13628 | GBP | 2024-07-31 | 2026-03-26 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 13629 | GBP | 2024-07-31 | 2025-04-14 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 12523 | GBP | 2024-07-31 | 2026-03-26 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 12524 | GBP | 2024-07-31 | 2025-04-14 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 15369 | GBP | 2024-07-31 | 2025-04-14 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 15368 | GBP | 2024-07-31 | 2026-03-26 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2023-07-31 | 2025-04-14 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | xbrli:pure | 2023-07-31 | 2024-03-25 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 9933 | GBP | 2023-07-31 | 2025-04-14 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 9933 | GBP | 2023-07-31 | 2024-03-25 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 20445 | GBP | 2023-07-31 | 2024-03-25 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 20445 | GBP | 2023-07-31 | 2025-04-14 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 12976 | GBP | 2023-07-31 | 2025-04-14 | filed | yes | `core:Equity` | micro-entity |
| equity | 12976 | GBP | 2023-07-31 | 2024-03-25 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 3794 | GBP | 2023-07-31 | 2025-04-14 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 3794 | GBP | 2023-07-31 | 2024-03-25 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | 12976 | GBP | 2023-07-31 | 2024-03-25 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 12976 | GBP | 2023-07-31 | 2025-04-14 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 10512 | GBP | 2023-07-31 | 2024-03-25 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 10512 | GBP | 2023-07-31 | 2025-04-14 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 14306 | GBP | 2023-07-31 | 2025-04-14 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 14306 | GBP | 2023-07-31 | 2024-03-25 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2022-07-31 | 2024-03-25 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 7651 | GBP | 2022-07-31 | 2024-03-25 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 17032 | GBP | 2022-07-31 | 2024-03-25 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 12815 | GBP | 2022-07-31 | 2024-03-25 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 4393 | GBP | 2022-07-31 | 2024-03-25 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 12815 | GBP | 2022-07-31 | 2024-03-25 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 9381 | GBP | 2022-07-31 | 2024-03-25 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 13774 | GBP | 2022-07-31 | 2024-03-25 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2026-03-26: `{"superseded_document_id": "gb:04028575:doc:rYbiv3EbhVxezryBE3icj3JO2oY9j671qagso2GG1DE", "restatements": [{"concept": "creditors_within_one_year", "period_end": "2024-07-31", "old_value": "10249.0000`

## ABTEC COMPUTER SOLUTIONS LTD (`gb:04368980`)

- registration: `04368980` (GB), status active, incorporated 2002-02-07
- classification: ['62090'] (sic_2007)
- records: 10 officers, 5 beneficial owners, 1 ownership statements, 0 security interests, 99 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.19 | xbrli:pure | 2026-02-28 | 2026-07-22 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 246242 | GBP | 2026-02-28 | 2026-07-22 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2026-02-28 | 2026-07-22 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1002866 | GBP | 2026-02-28 | 2026-07-22 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 1100707 | GBP | 2026-02-28 | 2026-07-22 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 723367 | GBP | 2026-02-28 | 2026-07-22 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 119 | GBP | 2026-02-28 | 2026-07-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 166195 | GBP | 2026-02-28 | 2026-07-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 166314 | GBP | 2026-02-28 | 2026-07-22 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 166314 | GBP | 2026-02-28 | 2026-07-22 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 97841 | GBP | 2026-02-28 | 2026-07-22 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 189139 | GBP | 2026-02-28 | 2026-07-22 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0.19 | xbrli:pure | 2025-02-28 | 2026-07-22 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 19 | xbrli:pure | 2025-02-28 | 2025-05-21 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 93362 | GBP | 2025-02-28 | 2026-07-22 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 93362 | GBP | 2025-02-28 | 2025-05-21 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 4734 | GBP | 2025-02-28 | 2026-07-22 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 813127 | GBP | 2025-02-28 | 2026-07-22 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 768810 | GBP | 2025-02-28 | 2025-05-21 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 768810 | GBP | 2025-02-28 | 2026-07-22 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 585181 | GBP | 2025-02-28 | 2025-05-21 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 585181 | GBP | 2025-02-28 | 2026-07-22 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 585181 | GBP | 2025-02-28 | 2025-05-21 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 49161 | GBP | 2025-02-28 | 2026-07-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 49161 | GBP | 2025-02-28 | 2025-05-21 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 119 | GBP | 2025-02-28 | 2025-05-21 | filed | no | `core:Equity` | total-exemption-full |
| equity | 49280 | GBP | 2025-02-28 | 2026-07-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 119 | GBP | 2025-02-28 | 2026-07-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 49280 | GBP | 2025-02-28 | 2025-05-21 | filed | no | `core:Equity` | total-exemption-full |
| net_assets | 49280 | GBP | 2025-02-28 | 2025-05-21 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 49280 | GBP | 2025-02-28 | 2026-07-22 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -44317 | GBP | 2025-02-28 | 2026-07-22 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -44317 | GBP | 2025-02-28 | 2025-05-21 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 86791 | GBP | 2025-02-28 | 2025-05-21 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 86791 | GBP | 2025-02-28 | 2026-07-22 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 18 | xbrli:pure | 2024-02-29 | 2025-05-21 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 18 | xbrli:pure | 2024-02-29 | 2024-10-15 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 171031 | GBP | 2024-02-29 | 2025-05-21 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 171031 | GBP | 2024-02-29 | 2024-10-15 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 39296 | GBP | 2024-02-29 | 2024-10-15 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 607456 | GBP | 2024-02-29 | 2024-10-15 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 583540 | GBP | 2024-02-29 | 2024-10-15 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 583540 | GBP | 2024-02-29 | 2025-05-21 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 283725 | GBP | 2024-02-29 | 2024-10-15 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 283725 | GBP | 2024-02-29 | 2025-05-21 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 283725 | GBP | 2024-02-29 | 2025-05-21 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 283725 | GBP | 2024-02-29 | 2024-10-15 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 21439 | GBP | 2024-02-29 | 2024-10-15 | filed | no | `core:Equity` | total-exemption-full |
| equity | 21558 | GBP | 2024-02-29 | 2024-10-15 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 21439 | GBP | 2024-02-29 | 2025-05-21 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 21558 | GBP | 2024-02-29 | 2025-05-21 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 119 | GBP | 2024-02-29 | 2025-05-21 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 119 | GBP | 2024-02-29 | 2024-10-15 | filed | no | `core:Equity` | total-exemption-full |
| net_assets | 21558 | GBP | 2024-02-29 | 2025-05-21 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 21558 | GBP | 2024-02-29 | 2024-10-15 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -23916 | GBP | 2024-02-29 | 2024-10-15 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -23916 | GBP | 2024-02-29 | 2025-05-21 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 88362 | GBP | 2024-02-29 | 2024-10-15 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 88362 | GBP | 2024-02-29 | 2025-05-21 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 18 | xbrli:pure | 2023-02-28 | 2024-10-15 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 100230 | GBP | 2023-02-28 | 2024-10-15 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 24167 | GBP | 2023-02-28 | 2024-10-15 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 526681 | GBP | 2023-02-28 | 2024-10-15 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 646016 | GBP | 2023-02-28 | 2024-10-15 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 433549 | GBP | 2023-02-28 | 2024-10-15 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 433549 | GBP | 2023-02-28 | 2024-10-15 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 132975 | GBP | 2023-02-28 | 2024-10-15 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 119 | GBP | 2023-02-28 | 2024-10-15 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 132856 | GBP | 2023-02-28 | 2024-10-15 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 132975 | GBP | 2023-02-28 | 2024-10-15 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 119335 | GBP | 2023-02-28 | 2024-10-15 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 166011 | GBP | 2023-02-28 | 2024-10-15 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2026-07-22: `{"superseded_document_id": "gb:04368980:doc:6Imo5f0u1vSfYPSbcEAJnEq9mUPWEljP8MQJih7V8cU", "restatements": [{"concept": "average_employees", "period_end": "2025-02-28", "old_value": "19.0000", "new_val`

## RANKINE I.T. LTD (`gb:04708687`)

- registration: `04708687` (GB), status active, incorporated 2003-03-24
- classification: ['62020'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 58 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2026-03-31 | 2026-08-28 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 36987 | GBP | 2026-03-31 | 2026-08-28 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2026-03-31 | 2026-08-28 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 48730 | GBP | 2026-03-31 | 2026-08-28 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 11743 | GBP | 2026-03-31 | 2026-08-28 | filed | yes | `core:Equity` | micro-entity |
| net_assets | 11743 | GBP | 2026-03-31 | 2026-08-28 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 48730 | GBP | 2026-03-31 | 2026-08-28 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 48730 | GBP | 2026-03-31 | 2026-08-28 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2025-03-31 | 2025-07-12 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2025-03-31 | 2026-08-28 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 38549 | GBP | 2025-03-31 | 2026-08-28 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 38775 | GBP | 2025-03-31 | 2025-07-12 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2025-03-31 | 2026-08-28 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 52939 | GBP | 2025-03-31 | 2025-07-12 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 52939 | GBP | 2025-03-31 | 2026-08-28 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 14390 | GBP | 2025-03-31 | 2026-08-28 | filed | yes | `core:Equity` | micro-entity |
| equity | 14164 | GBP | 2025-03-31 | 2025-07-12 | filed | no | `core:Equity` | micro-entity |
| net_assets | 14390 | GBP | 2025-03-31 | 2026-08-28 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 14164 | GBP | 2025-03-31 | 2025-07-12 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 52939 | GBP | 2025-03-31 | 2026-08-28 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 14164 | GBP | 2025-03-31 | 2025-07-12 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 52939 | GBP | 2025-03-31 | 2026-08-28 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 14164 | GBP | 2025-03-31 | 2025-07-12 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-03-31 | 2024-11-10 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 35334 | GBP | 2024-03-31 | 2025-07-12 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 35334 | GBP | 2024-03-31 | 2024-11-10 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 58644 | GBP | 2024-03-31 | 2024-11-10 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 58644 | GBP | 2024-03-31 | 2025-07-12 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 23310 | GBP | 2024-03-31 | 2025-07-12 | filed | yes | `core:Equity` | micro-entity |
| equity | 23310 | GBP | 2024-03-31 | 2024-11-10 | filed | no | `core:Equity` | micro-entity |
| net_assets | 23310 | GBP | 2024-03-31 | 2024-11-10 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 23310 | GBP | 2024-03-31 | 2025-07-12 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 23310 | GBP | 2024-03-31 | 2025-07-12 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 23310 | GBP | 2024-03-31 | 2024-11-10 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| profit_for_period | -1188 | GBP | 2024-03-31 | 2024-11-10 | filed | yes | `core:ProfitLoss` | micro-entity |
| revenue | 25041 | GBP | 2024-03-31 | 2024-11-10 | filed | yes | `core:TurnoverRevenue` | micro-entity |
| staff_costs | 13254 | GBP | 2024-03-31 | 2024-11-10 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | micro-entity |
| total_assets_less_current_liabilities | 23310 | GBP | 2024-03-31 | 2024-11-10 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 23310 | GBP | 2024-03-31 | 2025-07-12 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 12378 | GBP | 2023-03-31 | 2024-11-10 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 61876 | GBP | 2023-03-31 | 2024-11-10 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 49498 | GBP | 2023-03-31 | 2024-11-10 | filed | yes | `core:Equity` | micro-entity |
| net_assets | 49498 | GBP | 2023-03-31 | 2024-11-10 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 49498 | GBP | 2023-03-31 | 2024-11-10 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| profit_for_period | 2432 | GBP | 2023-03-31 | 2024-11-10 | filed | yes | `core:ProfitLoss` | micro-entity |
| revenue | 23486 | GBP | 2023-03-31 | 2024-11-10 | filed | yes | `core:TurnoverRevenue` | micro-entity |
| staff_costs | 12421 | GBP | 2023-03-31 | 2024-11-10 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | micro-entity |
| tax_charge | 571 | GBP | 2023-03-31 | 2024-11-10 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | micro-entity |
| total_assets_less_current_liabilities | 49498 | GBP | 2023-03-31 | 2024-11-10 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2026-08-28: `{"superseded_document_id": "gb:04708687:doc:M3VhZjCpZYttzgFrDEAnmrktfm-e4ZU4_yPq-y3rois", "restatements": [{"concept": "creditors_within_one_year", "period_end": "2025-03-31", "old_value": "38775.0000`

## ATLAS COMPUTER SYSTEMS LIMITED (`gb:05078708`)

- registration: `05078708` (GB), status active, incorporated 2004-03-19
- classification: ['62012'] (sic_2007)
- records: 13 officers, 3 beneficial owners, 0 ownership statements, 0 security interests, 142 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## PTLGATEWAY LIMITED (`gb:05409330`)

- registration: `05409330` (GB), status active, incorporated 2005-03-31
- classification: ['62020'] (sic_2007)
- records: 4 officers, 3 beneficial owners, 0 ownership statements, 0 security interests, 58 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2026-03-31 | 2026-06-08 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 96544 | GBP | 2026-03-31 | 2026-06-08 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 96539 | GBP | 2026-03-31 | 2026-06-08 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 96544 | GBP | 2026-03-31 | 2026-06-08 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 0 | GBP | 2026-03-31 | 2026-06-08 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -1995 | GBP | 2026-03-31 | 2026-06-08 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 5 | GBP | 2026-03-31 | 2026-06-08 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2000 | GBP | 2026-03-31 | 2026-06-08 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 5 | GBP | 2026-03-31 | 2026-06-08 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 5 | GBP | 2026-03-31 | 2026-06-08 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 5 | GBP | 2026-03-31 | 2026-06-08 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 3 | xbrli:pure | 2025-03-31 | 2025-06-19 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 3 | xbrli:pure | 2025-03-31 | 2026-06-08 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 207665 | GBP | 2025-03-31 | 2025-06-19 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 207665 | GBP | 2025-03-31 | 2026-06-08 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 94417 | GBP | 2025-03-31 | 2025-06-19 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 94417 | GBP | 2025-03-31 | 2026-06-08 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 221802 | GBP | 2025-03-31 | 2025-06-19 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 221802 | GBP | 2025-03-31 | 2026-06-08 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 14137 | GBP | 2025-03-31 | 2025-06-19 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 14137 | GBP | 2025-03-31 | 2026-06-08 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 118741 | GBP | 2025-03-31 | 2026-06-08 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 116741 | GBP | 2025-03-31 | 2025-06-19 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2000 | GBP | 2025-03-31 | 2026-06-08 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 118741 | GBP | 2025-03-31 | 2025-06-19 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 116741 | GBP | 2025-03-31 | 2026-06-08 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2000 | GBP | 2025-03-31 | 2025-06-19 | filed | no | `core:Equity` | total-exemption-full |
| net_assets | 118741 | GBP | 2025-03-31 | 2025-06-19 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 118741 | GBP | 2025-03-31 | 2026-06-08 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 127385 | GBP | 2025-03-31 | 2025-06-19 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 127385 | GBP | 2025-03-31 | 2026-06-08 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 127385 | GBP | 2025-03-31 | 2025-06-19 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 127385 | GBP | 2025-03-31 | 2026-06-08 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 3 | xbrli:pure | 2024-03-31 | 2025-06-19 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 3 | xbrli:pure | 2024-03-31 | 2024-07-08 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 374931 | GBP | 2024-03-31 | 2024-07-08 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 374931 | GBP | 2024-03-31 | 2025-06-19 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 147729 | GBP | 2024-03-31 | 2025-06-19 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 147729 | GBP | 2024-03-31 | 2024-07-08 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 385922 | GBP | 2024-03-31 | 2025-06-19 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 385922 | GBP | 2024-03-31 | 2024-07-08 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors | 10991 | GBP | 2024-03-31 | 2024-07-08 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 10991 | GBP | 2024-03-31 | 2025-06-19 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2000 | GBP | 2024-03-31 | 2024-07-08 | filed | no | `core:Equity` | total-exemption-full |
| equity | 229549 | GBP | 2024-03-31 | 2025-06-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2000 | GBP | 2024-03-31 | 2025-06-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 227549 | GBP | 2024-03-31 | 2024-07-08 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 227549 | GBP | 2024-03-31 | 2025-06-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 229549 | GBP | 2024-03-31 | 2024-07-08 | filed | no | `core:Equity` | total-exemption-full |
| net_assets | 229549 | GBP | 2024-03-31 | 2025-06-19 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 229549 | GBP | 2024-03-31 | 2024-07-08 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 238193 | GBP | 2024-03-31 | 2025-06-19 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 238193 | GBP | 2024-03-31 | 2024-07-08 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 238193 | GBP | 2024-03-31 | 2025-06-19 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 238193 | GBP | 2024-03-31 | 2024-07-08 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 4 | xbrli:pure | 2023-03-31 | 2024-07-08 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 411964 | GBP | 2023-03-31 | 2024-07-08 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 130429 | GBP | 2023-03-31 | 2024-07-08 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 425851 | GBP | 2023-03-31 | 2024-07-08 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 11602 | GBP | 2023-03-31 | 2024-07-08 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2000 | GBP | 2023-03-31 | 2024-07-08 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 286778 | GBP | 2023-03-31 | 2024-07-08 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 284778 | GBP | 2023-03-31 | 2024-07-08 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 286778 | GBP | 2023-03-31 | 2024-07-08 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 295422 | GBP | 2023-03-31 | 2024-07-08 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 295422 | GBP | 2023-03-31 | 2024-07-08 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._
