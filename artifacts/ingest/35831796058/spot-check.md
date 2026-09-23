# Ingest spot-check

- database: `data/engine.db`
- latest run: `20260923T072750Z-adfad488`
- companies in store: 10600; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## TRINITY ENGINEERING (NORTHAMPTON) LIMITED (`gb:01665797`)

- registration: `01665797` (GB), status active, incorporated 1982-09-21
- classification: ['71121'] (sic_2007)
- records: 6 officers, 2 beneficial owners, 0 ownership statements, 2 security interests, 104 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 5 | iso4217:GBP | 2024-09-30 | 2025-06-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 25212 | GBP | 2024-09-30 | 2025-06-30 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 15969 | GBP | 2024-09-30 | 2025-06-30 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 109516 | GBP | 2024-09-30 | 2025-06-30 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 99067 | GBP | 2024-09-30 | 2025-06-30 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 72855 | GBP | 2024-09-30 | 2025-06-30 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 72855 | GBP | 2024-09-30 | 2025-06-30 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-09-30 | 2025-06-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity | -11103 | GBP | 2024-09-30 | 2025-06-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -11203 | GBP | 2024-09-30 | 2025-06-30 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 15315 | GBP | 2024-09-30 | 2025-06-30 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | -11103 | GBP | 2024-09-30 | 2025-06-30 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -10449 | GBP | 2024-09-30 | 2025-06-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 4866 | GBP | 2024-09-30 | 2025-06-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 5 | iso4217:GBP | 2023-09-30 | 2025-06-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 5 | xbrli:pure | 2023-09-30 | 2024-06-28 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 129 | GBP | 2023-09-30 | 2025-06-30 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 129 | GBP | 2023-09-30 | 2024-06-28 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 20419 | GBP | 2023-09-30 | 2024-06-28 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 20419 | GBP | 2023-09-30 | 2025-06-30 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 148068 | GBP | 2023-09-30 | 2024-06-28 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 148068 | GBP | 2023-09-30 | 2025-06-30 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 137470 | GBP | 2023-09-30 | 2024-06-28 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 137470 | GBP | 2023-09-30 | 2025-06-30 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 136341 | GBP | 2023-09-30 | 2024-06-28 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 136341 | GBP | 2023-09-30 | 2025-06-30 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 136341 | GBP | 2023-09-30 | 2024-06-28 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 136341 | GBP | 2023-09-30 | 2025-06-30 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | -14104 | GBP | 2023-09-30 | 2024-06-28 | filed | no | `core:Equity` | total-exemption-full |
| equity | -14104 | GBP | 2023-09-30 | 2025-06-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-09-30 | 2025-06-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -14204 | GBP | 2023-09-30 | 2025-06-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -14204 | GBP | 2023-09-30 | 2024-06-28 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-09-30 | 2024-06-28 | filed | no | `core:Equity` | total-exemption-full |
| fixed_assets | 16913 | GBP | 2023-09-30 | 2025-06-30 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | -14104 | GBP | 2023-09-30 | 2024-06-28 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | -14104 | GBP | 2023-09-30 | 2025-06-30 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -10598 | GBP | 2023-09-30 | 2024-06-28 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -10598 | GBP | 2023-09-30 | 2025-06-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 6315 | GBP | 2023-09-30 | 2025-06-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 6315 | GBP | 2023-09-30 | 2024-06-28 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 6 | xbrli:pure | 2022-09-30 | 2024-06-28 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 6 | xbrli:pure | 2022-09-30 | 2023-06-30 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 30870 | GBP | 2022-09-30 | 2024-06-28 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 30870 | GBP | 2022-09-30 | 2023-06-30 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2022-09-30 | 2024-06-28 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 132892 | GBP | 2022-09-30 | 2023-06-30 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 132892 | GBP | 2022-09-30 | 2024-06-28 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 129710 | GBP | 2022-09-30 | 2024-06-28 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 129710 | GBP | 2022-09-30 | 2023-06-30 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 97840 | GBP | 2022-09-30 | 2023-06-30 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 97840 | GBP | 2022-09-30 | 2024-06-28 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 97840 | GBP | 2022-09-30 | 2023-06-30 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 97840 | GBP | 2022-09-30 | 2024-06-28 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 14063 | GBP | 2022-09-30 | 2024-06-28 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 13963 | GBP | 2022-09-30 | 2023-06-30 | filed | no | `core:Equity` | total-exemption-full |
| equity | 14063 | GBP | 2022-09-30 | 2023-06-30 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 13963 | GBP | 2022-09-30 | 2024-06-28 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2022-09-30 | 2023-06-30 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2022-09-30 | 2024-06-28 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 14063 | GBP | 2022-09-30 | 2024-06-28 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -3182 | GBP | 2022-09-30 | 2024-06-28 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -3182 | GBP | 2022-09-30 | 2023-06-30 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 14063 | GBP | 2022-09-30 | 2024-06-28 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 14063 | GBP | 2022-09-30 | 2023-06-30 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 7 | xbrli:pure | 2021-09-30 | 2023-06-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 53182 | GBP | 2021-09-30 | 2023-06-30 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 116429 | GBP | 2021-09-30 | 2023-06-30 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 149331 | GBP | 2021-09-30 | 2023-06-30 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 95149 | GBP | 2021-09-30 | 2023-06-30 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 95149 | GBP | 2021-09-30 | 2023-06-30 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 45611 | GBP | 2021-09-30 | 2023-06-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 45511 | GBP | 2021-09-30 | 2023-06-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2021-09-30 | 2023-06-30 | filed | yes | `core:Equity` | total-exemption-full |
| net_current_assets | 32902 | GBP | 2021-09-30 | 2023-06-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 45611 | GBP | 2021-09-30 | 2023-06-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## PRINTER MARKETING COMPANY LIMITED (`gb:02090367`)

- registration: `02090367` (GB), status active, incorporated 1987-01-16
- classification: ['62030'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 90 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2024-12-31 | 2025-08-06 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 19682 | GBP | 2024-12-31 | 2025-08-06 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| equity | 3248 | GBP | 2024-12-31 | 2025-08-06 | filed | yes | `frs-core:Equity` | micro-entity |
| net_assets | 3248 | GBP | 2024-12-31 | 2025-08-06 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 3248 | GBP | 2024-12-31 | 2025-08-06 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 3248 | GBP | 2024-12-31 | 2025-08-06 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-12-31 | 2025-08-06 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-12-31 | 2024-08-30 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 20409 | GBP | 2023-12-31 | 2025-08-06 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| current_assets | 20409 | GBP | 2023-12-31 | 2024-08-30 | filed | no | `frs-core:CurrentAssets` | micro-entity |
| equity | 3975 | GBP | 2023-12-31 | 2024-08-30 | filed | no | `frs-core:Equity` | micro-entity |
| equity | 3975 | GBP | 2023-12-31 | 2025-08-06 | filed | yes | `frs-core:Equity` | micro-entity |
| net_assets | 3975 | GBP | 2023-12-31 | 2025-08-06 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 3975 | GBP | 2023-12-31 | 2024-08-30 | filed | no | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 3975 | GBP | 2023-12-31 | 2025-08-06 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 3975 | GBP | 2023-12-31 | 2024-08-30 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 3975 | GBP | 2023-12-31 | 2024-08-30 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 3975 | GBP | 2023-12-31 | 2025-08-06 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2022-12-31 | 2024-08-30 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2022-12-31 | 2023-08-28 | filed | yes | `pt:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 21724 | GBP | 2022-12-31 | 2024-08-30 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| equity | 5321 | GBP | 2022-12-31 | 2024-08-30 | filed | yes | `frs-core:Equity` | micro-entity |
| net_assets | 5321 | GBP | 2022-12-31 | 2024-08-30 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 5321 | GBP | 2022-12-31 | 2023-08-28 | filed | no | `pt:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 5321 | GBP | 2022-12-31 | 2024-08-30 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 5321 | GBP | 2022-12-31 | 2023-08-28 | filed | no | `pt:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 5321 | GBP | 2022-12-31 | 2023-08-28 | filed | no | `pt:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 5321 | GBP | 2022-12-31 | 2024-08-30 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| net_assets | 6828 | GBP | 2021-12-31 | 2023-08-28 | filed | yes | `pt:NetAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 6828 | GBP | 2021-12-31 | 2023-08-28 | filed | yes | `pt:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## LINTON EXPLORATION LIMITED (`gb:02384390`)

- registration: `02384390` (GB), status active, incorporated 1989-05-15
- classification: ['62090'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 98 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | iso4217:GBP | 2026-01-31 | 2026-03-17 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2026-01-31 | 2026-03-17 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 11333 | GBP | 2026-01-31 | 2026-03-17 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 497 | GBP | 2026-01-31 | 2026-03-17 | filed | yes | `core:CurrentAssets` | micro-entity |
| depreciation_amortisation | 0 | GBP | 2026-01-31 | 2026-03-17 | filed | yes | `core:DepreciationAmortisationImpairmentExpense` | micro-entity |
| equity | -10736 | GBP | 2026-01-31 | 2026-03-17 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2026-01-31 | 2026-03-17 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | -10736 | GBP | 2026-01-31 | 2026-03-17 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -10836 | GBP | 2026-01-31 | 2026-03-17 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| profit_for_period | 1738 | GBP | 2026-01-31 | 2026-03-17 | filed | yes | `core:ProfitLoss` | micro-entity |
| revenue | 24582 | GBP | 2026-01-31 | 2026-03-17 | filed | yes | `core:TurnoverRevenue` | micro-entity |
| staff_costs | 0 | GBP | 2026-01-31 | 2026-03-17 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | micro-entity |
| tax_charge | 407 | GBP | 2026-01-31 | 2026-03-17 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | micro-entity |
| total_assets_less_current_liabilities | -10736 | GBP | 2026-01-31 | 2026-03-17 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2025-01-31 | 2025-10-21 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2025-01-31 | 2026-03-17 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 11333 | GBP | 2025-01-31 | 2026-03-17 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 11333 | GBP | 2025-01-31 | 2025-10-21 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 497 | GBP | 2025-01-31 | 2026-03-17 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 497 | GBP | 2025-01-31 | 2025-10-21 | filed | no | `core:CurrentAssets` | micro-entity |
| depreciation_amortisation | 0 | GBP | 2025-01-31 | 2026-03-17 | filed | yes | `core:DepreciationAmortisationImpairmentExpense` | micro-entity |
| equity | -10736 | GBP | 2025-01-31 | 2026-03-17 | filed | yes | `core:Equity` | micro-entity |
| equity | -10736 | GBP | 2025-01-31 | 2025-10-21 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2025-01-31 | 2026-03-17 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | -10736 | GBP | 2025-01-31 | 2025-10-21 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | -10736 | GBP | 2025-01-31 | 2026-03-17 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -10836 | GBP | 2025-01-31 | 2026-03-17 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -10836 | GBP | 2025-01-31 | 2025-10-21 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| profit_for_period | -1032 | GBP | 2025-01-31 | 2026-03-17 | filed | yes | `core:ProfitLoss` | micro-entity |
| profit_for_period | -1032 | GBP | 2025-01-31 | 2025-10-21 | filed | no | `core:ProfitLoss` | micro-entity |
| revenue | 29564 | GBP | 2025-01-31 | 2026-03-17 | filed | yes | `core:TurnoverRevenue` | micro-entity |
| revenue | 29564 | GBP | 2025-01-31 | 2025-10-21 | filed | no | `core:TurnoverRevenue` | micro-entity |
| staff_costs | 0 | GBP | 2025-01-31 | 2026-03-17 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | micro-entity |
| tax_charge | 0 | GBP | 2025-01-31 | 2026-03-17 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | micro-entity |
| tax_charge | 0 | GBP | 2025-01-31 | 2025-10-21 | filed | no | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | micro-entity |
| total_assets_less_current_liabilities | -10736 | GBP | 2025-01-31 | 2026-03-17 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -10736 | GBP | 2025-01-31 | 2025-10-21 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-01-31 | 2024-10-27 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 11333 | GBP | 2024-01-31 | 2025-10-21 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 11333 | GBP | 2024-01-31 | 2024-10-27 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 497 | GBP | 2024-01-31 | 2025-10-21 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 497 | GBP | 2024-01-31 | 2024-10-27 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | -10736 | GBP | 2024-01-31 | 2025-10-21 | filed | yes | `core:Equity` | micro-entity |
| equity | 10736 | GBP | 2024-01-31 | 2024-10-27 | filed | no | `uk-core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2024-01-31 | 2024-10-27 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 10736 | GBP | 2024-01-31 | 2024-10-27 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | -10736 | GBP | 2024-01-31 | 2025-10-21 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -10836 | GBP | 2024-01-31 | 2025-10-21 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 10836 | GBP | 2024-01-31 | 2024-10-27 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| profit_for_period | 1074 | GBP | 2024-01-31 | 2025-10-21 | filed | yes | `core:ProfitLoss` | micro-entity |
| revenue | 4546 | GBP | 2024-01-31 | 2025-10-21 | filed | yes | `core:TurnoverRevenue` | micro-entity |
| tax_charge | 251 | GBP | 2024-01-31 | 2025-10-21 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | micro-entity |
| total_assets_less_current_liabilities | -10736 | GBP | 2024-01-31 | 2025-10-21 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 10736 | GBP | 2024-01-31 | 2024-10-27 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-01-31 | 2024-10-27 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 11333 | GBP | 2023-01-31 | 2024-10-27 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 502 | GBP | 2023-01-31 | 2024-10-27 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 10731 | GBP | 2023-01-31 | 2024-10-27 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2023-01-31 | 2024-10-27 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 10731 | GBP | 2023-01-31 | 2024-10-27 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 10831 | GBP | 2023-01-31 | 2024-10-27 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 10731 | GBP | 2023-01-31 | 2024-10-27 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2025-10-21: `{"superseded_document_id": "gb:02384390:doc:3W1jO26OOSUqbpeF59i2wdGGpfNvwaX1Aj5T6bPQWfM", "restatements": [{"concept": "net_current_assets", "period_end": "2024-01-31", "old_value": "10836.0000", "new`

## PREMIER SYSTEM SOLUTIONS LIMITED (`gb:02626325`)

- registration: `02626325` (GB), status active, incorporated 1991-07-03
- classification: ['62090'] (sic_2007)
- records: 5 officers, 2 beneficial owners, 0 ownership statements, 1 security interests, 94 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-07-31 | 2026-02-02 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 9717 | GBP | 2025-07-31 | 2026-02-02 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 25144 | GBP | 2025-07-31 | 2026-02-02 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 15007 | GBP | 2025-07-31 | 2026-02-02 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 780 | GBP | 2025-07-31 | 2026-02-02 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 15007 | GBP | 2025-07-31 | 2026-02-02 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 15427 | GBP | 2025-07-31 | 2026-02-02 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 16207 | GBP | 2025-07-31 | 2026-02-02 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-07-31 | 2026-02-02 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-07-31 | 2025-04-28 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 4039 | GBP | 2024-07-31 | 2026-02-02 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 4039 | GBP | 2024-07-31 | 2025-04-28 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 15086 | GBP | 2024-07-31 | 2026-02-02 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 15086 | GBP | 2024-07-31 | 2025-04-28 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 11406 | GBP | 2024-07-31 | 2025-04-28 | filed | no | `core:Equity` | micro-entity |
| equity | 11406 | GBP | 2024-07-31 | 2026-02-02 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 1559 | GBP | 2024-07-31 | 2025-04-28 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 1559 | GBP | 2024-07-31 | 2026-02-02 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 11406 | GBP | 2024-07-31 | 2025-04-28 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 11406 | GBP | 2024-07-31 | 2026-02-02 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 11047 | GBP | 2024-07-31 | 2026-02-02 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 11047 | GBP | 2024-07-31 | 2025-04-28 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 12606 | GBP | 2024-07-31 | 2025-04-28 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 12606 | GBP | 2024-07-31 | 2026-02-02 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 3 | xbrli:pure | 2023-07-31 | 2025-04-28 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 3 | xbrli:pure | 2023-07-31 | 2024-04-30 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 7785 | GBP | 2023-07-31 | 2025-04-28 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 22411 | GBP | 2023-07-31 | 2024-04-30 | filed | no | `frs-core:CurrentAssets` | micro-entity |
| current_assets | 22411 | GBP | 2023-07-31 | 2025-04-28 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 16712 | GBP | 2023-07-31 | 2025-04-28 | filed | yes | `core:Equity` | micro-entity |
| equity | 16712 | GBP | 2023-07-31 | 2024-04-30 | filed | no | `frs-core:Equity` | micro-entity |
| fixed_assets | 2338 | GBP | 2023-07-31 | 2025-04-28 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 2338 | GBP | 2023-07-31 | 2024-04-30 | filed | no | `frs-core:FixedAssets` | micro-entity |
| net_assets | 16712 | GBP | 2023-07-31 | 2024-04-30 | filed | no | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 16712 | GBP | 2023-07-31 | 2025-04-28 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 14626 | GBP | 2023-07-31 | 2025-04-28 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 14626 | GBP | 2023-07-31 | 2024-04-30 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 16964 | GBP | 2023-07-31 | 2024-04-30 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 16964 | GBP | 2023-07-31 | 2025-04-28 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 3 | xbrli:pure | 2022-07-31 | 2024-04-30 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 21636 | GBP | 2022-07-31 | 2024-04-30 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| equity | 15261 | GBP | 2022-07-31 | 2024-04-30 | filed | yes | `frs-core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2022-07-31 | 2024-04-30 | filed | yes | `frs-core:FixedAssets` | micro-entity |
| net_assets | 15261 | GBP | 2022-07-31 | 2024-04-30 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 18743 | GBP | 2022-07-31 | 2024-04-30 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 18743 | GBP | 2022-07-31 | 2024-04-30 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## RED FOX SYSTEMS CONSULTANTS LIMITED (`gb:02842502`)

- registration: `02842502` (GB), status active, incorporated 1993-08-05
- classification: ['71129'] (sic_2007)
- records: 5 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 71 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2024-08-31 | 2025-05-08 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| fixed_assets | 1590 | GBP | 2024-08-31 | 2025-05-08 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 27293 | GBP | 2024-08-31 | 2025-05-08 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-08-31 | 2025-05-08 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-08-31 | 2024-04-23 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| fixed_assets | 1387 | GBP | 2023-08-31 | 2024-04-23 | filed | no | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 1387 | GBP | 2023-08-31 | 2025-05-08 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 26051 | GBP | 2023-08-31 | 2024-04-23 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 26051 | GBP | 2023-08-31 | 2025-05-08 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2022-08-31 | 2024-04-23 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| fixed_assets | 1849 | GBP | 2022-08-31 | 2024-04-23 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 30223 | GBP | 2022-08-31 | 2024-04-23 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |

_No coverage facts for the latest run._

## HUSCOCELL LIMITED (`gb:03029613`)

- registration: `03029613` (GB), status active, incorporated 1995-03-06
- classification: ['62011'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 69 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | xbrli:pure | 2025-03-31 | 2025-12-23 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 92719 | GBP | 2025-03-31 | 2025-12-23 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity | 86484 | GBP | 2025-03-31 | 2025-12-23 | filed | yes | `ns5:Equity` | micro-entity |
| net_current_assets | 86484 | GBP | 2025-03-31 | 2025-12-23 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 86484 | GBP | 2025-03-31 | 2025-12-23 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2024-03-31 | 2024-12-30 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | xbrli:pure | 2024-03-31 | 2025-12-23 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 93569 | GBP | 2024-03-31 | 2025-12-23 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| current_assets | 93569 | GBP | 2024-03-31 | 2024-12-30 | filed | no | `ns5:CurrentAssets` | micro-entity |
| equity | 87435 | GBP | 2024-03-31 | 2024-12-30 | filed | no | `ns5:Equity` | micro-entity |
| equity | 87435 | GBP | 2024-03-31 | 2025-12-23 | filed | yes | `ns5:Equity` | micro-entity |
| net_current_assets | 87435 | GBP | 2024-03-31 | 2024-12-30 | filed | no | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 87435 | GBP | 2024-03-31 | 2025-12-23 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 87435 | GBP | 2024-03-31 | 2025-12-23 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 87435 | GBP | 2024-03-31 | 2024-12-30 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2023-03-31 | 2024-12-30 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 0 | xbrli:pure | 2023-03-31 | 2023-12-17 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 94059 | GBP | 2023-03-31 | 2023-12-17 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| current_assets | 94059 | GBP | 2023-03-31 | 2024-12-30 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity | 88121 | GBP | 2023-03-31 | 2024-12-30 | filed | yes | `ns5:Equity` | micro-entity |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 88121 | GBP | 2023-03-31 | 2023-12-17 | filed | yes | `ns5:Equity` | micro-entity |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 88121 | GBP | 2023-03-31 | 2023-12-17 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 88121 | GBP | 2023-03-31 | 2024-12-30 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 88121 | GBP | 2023-03-31 | 2023-12-17 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 88121 | GBP | 2023-03-31 | 2024-12-30 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 0 | xbrli:pure | 2022-03-31 | 2023-12-17 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 94918 | GBP | 2022-03-31 | 2023-12-17 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 89031 | GBP | 2022-03-31 | 2023-12-17 | filed | yes | `ns5:Equity` | micro-entity |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 89031 | GBP | 2022-03-31 | 2023-12-17 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 89031 | GBP | 2022-03-31 | 2023-12-17 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## NETGUIDES LIMITED (`gb:03184437`)

- registration: `03184437` (GB), status active, incorporated 1996-04-11
- classification: ['62020'] (sic_2007)
- records: 4 officers, 3 beneficial owners, 0 ownership statements, 2 security interests, 108 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 10 | xbrli:pure | 2025-04-30 | 2025-11-24 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 153313 | GBP | 2025-04-30 | 2025-11-24 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 226684 | GBP | 2025-04-30 | 2025-11-24 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 73371 | GBP | 2025-04-30 | 2025-11-24 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 73371 | GBP | 2025-04-30 | 2025-11-24 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 105945 | GBP | 2025-04-30 | 2025-11-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 250 | GBP | 2025-04-30 | 2025-11-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 176396 | GBP | 2025-04-30 | 2025-11-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 70201 | GBP | 2025-04-30 | 2025-11-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| fixed_assets | 138 | GBP | 2025-04-30 | 2025-11-24 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| net_current_assets | 176258 | GBP | 2025-04-30 | 2025-11-24 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 176396 | GBP | 2025-04-30 | 2025-11-24 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 10 | xbrli:pure | 2024-04-30 | 2025-11-24 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 10 | xbrli:pure | 2024-04-30 | 2024-12-02 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 122909 | GBP | 2024-04-30 | 2024-12-02 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 122909 | GBP | 2024-04-30 | 2025-11-24 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 199141 | GBP | 2024-04-30 | 2024-12-02 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 199141 | GBP | 2024-04-30 | 2025-11-24 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 76232 | GBP | 2024-04-30 | 2024-12-02 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 76232 | GBP | 2024-04-30 | 2025-11-24 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 76232 | GBP | 2024-04-30 | 2024-12-02 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 76232 | GBP | 2024-04-30 | 2025-11-24 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 104842 | GBP | 2024-04-30 | 2025-11-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 250 | GBP | 2024-04-30 | 2024-12-02 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -1353 | GBP | 2024-04-30 | 2024-12-02 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -1353 | GBP | 2024-04-30 | 2025-11-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 105945 | GBP | 2024-04-30 | 2025-11-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 104842 | GBP | 2024-04-30 | 2024-12-02 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 250 | GBP | 2024-04-30 | 2025-11-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 105945 | GBP | 2024-04-30 | 2024-12-02 | filed | no | `ns5:Equity` | total-exemption-full |
| fixed_assets | 1490 | GBP | 2024-04-30 | 2025-11-24 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| fixed_assets | 1490 | GBP | 2024-04-30 | 2024-12-02 | filed | no | `ns5:FixedAssets` | total-exemption-full |
| net_current_assets | 103352 | GBP | 2024-04-30 | 2024-12-02 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 103352 | GBP | 2024-04-30 | 2025-11-24 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 104842 | GBP | 2024-04-30 | 2024-12-02 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 104842 | GBP | 2024-04-30 | 2025-11-24 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 10 | xbrli:pure | 2023-04-30 | 2024-12-02 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 10 | xbrli:pure | 2023-04-30 | 2023-10-11 | filed | no | `ns6:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 128184 | GBP | 2023-04-30 | 2023-10-11 | filed | no | `ns6:CashBankOnHand` | total-exemption-full |
| cash | 128184 | GBP | 2023-04-30 | 2024-12-02 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 196425 | GBP | 2023-04-30 | 2023-10-11 | filed | no | `ns6:CurrentAssets` | total-exemption-full |
| current_assets | 196425 | GBP | 2023-04-30 | 2024-12-02 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 68241 | GBP | 2023-04-30 | 2024-12-02 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 68241 | GBP | 2023-04-30 | 2024-12-02 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 68241 | GBP | 2023-04-30 | 2023-10-11 | filed | no | `ns6:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 68241 | GBP | 2023-04-30 | 2023-10-11 | filed | no | `ns6:Debtors` | total-exemption-full |
| equity | 107926 | GBP | 2023-04-30 | 2023-10-11 | filed | no | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 250 | GBP | 2023-04-30 | 2023-10-11 | filed | no | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1731 | GBP | 2023-04-30 | 2023-10-11 | filed | no | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1731 | GBP | 2023-04-30 | 2024-12-02 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 105945 | GBP | 2023-04-30 | 2023-10-11 | filed | no | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 250 | GBP | 2023-04-30 | 2024-12-02 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 105945 | GBP | 2023-04-30 | 2024-12-02 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 107926 | GBP | 2023-04-30 | 2024-12-02 | filed | yes | `ns5:Equity` | total-exemption-full |
| fixed_assets | 2930 | GBP | 2023-04-30 | 2023-10-11 | filed | no | `ns6:FixedAssets` | total-exemption-full |
| fixed_assets | 2930 | GBP | 2023-04-30 | 2024-12-02 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| net_current_assets | 104996 | GBP | 2023-04-30 | 2024-12-02 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 104996 | GBP | 2023-04-30 | 2023-10-11 | filed | no | `ns6:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 107926 | GBP | 2023-04-30 | 2024-12-02 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 107926 | GBP | 2023-04-30 | 2023-10-11 | filed | no | `ns6:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 10 | xbrli:pure | 2022-04-30 | 2023-10-11 | filed | yes | `ns6:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 117265 | GBP | 2022-04-30 | 2023-10-11 | filed | yes | `ns6:CashBankOnHand` | total-exemption-full |
| current_assets | 181094 | GBP | 2022-04-30 | 2023-10-11 | filed | yes | `ns6:CurrentAssets` | total-exemption-full |
| debtors | 63829 | GBP | 2022-04-30 | 2023-10-11 | filed | yes | `ns6:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 63829 | GBP | 2022-04-30 | 2023-10-11 | filed | yes | `ns6:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -6089 | GBP | 2022-04-30 | 2023-10-11 | filed | yes | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 250 | GBP | 2022-04-30 | 2023-10-11 | filed | yes | `ns6:Equity` | total-exemption-full |
| equity | 100106 | GBP | 2022-04-30 | 2023-10-11 | filed | yes | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 105945 | GBP | 2022-04-30 | 2023-10-11 | filed | yes | `ns6:Equity` | total-exemption-full |
| fixed_assets | 1419 | GBP | 2022-04-30 | 2023-10-11 | filed | yes | `ns6:FixedAssets` | total-exemption-full |
| net_current_assets | 98687 | GBP | 2022-04-30 | 2023-10-11 | filed | yes | `ns6:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 100106 | GBP | 2022-04-30 | 2023-10-11 | filed | yes | `ns6:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## PEPPERHALL LIMITED (`gb:03327159`)

- registration: `03327159` (GB), status active, incorporated 1997-03-04
- classification: ['86102'] (sic_2007)
- records: 12 officers, 1 beneficial owners, 1 ownership statements, 11 security interests, 119 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1.1400000000000001 | xbrli:pure | 2025-09-30 | 2026-06-29 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | small |
| cash | 63460 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `core:CashBankOnHand` | small |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 971133 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `core:Creditors` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 767641 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `core:Creditors` | small |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 767641 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `core:Creditors` | small |
| current_assets | 1354639 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `core:CurrentAssets` | small |
| debtors | 1291179 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `core:Debtors` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `core:Equity` | small |
| equity | 1077281 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1077181 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `core:Equity` | small |
| net_assets | 1077281 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `core:NetAssetsLiabilities` | small |
| net_current_assets | 586998 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `core:NetCurrentAssetsLiabilities` | small |
| total_assets_less_current_liabilities | 2134990 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | small |
| average_employees | 103 | xbrli:pure | 2024-09-30 | 2025-06-17 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | small |
| average_employees | 1.03 | xbrli:pure | 2024-09-30 | 2026-06-29 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | small |
| cash | 14168 | GBP | 2024-09-30 | 2025-06-17 | filed | no | `core:CashBankOnHand` | small |
| cash | 14168 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `core:CashBankOnHand` | small |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 806667 | GBP | 2024-09-30 | 2025-06-17 | filed | yes | `core:Creditors` | small |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 806667 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `core:Creditors` | small |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 621325 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `core:Creditors` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 621325 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `core:Creditors` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 621325 | GBP | 2024-09-30 | 2025-06-17 | filed | no | `core:Creditors` | small |
| current_assets | 512489 | GBP | 2024-09-30 | 2025-06-17 | filed | no | `core:CurrentAssets` | small |
| current_assets | 512489 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `core:CurrentAssets` | small |
| debtors | 498321 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `core:Debtors` | small |
| debtors | 498321 | GBP | 2024-09-30 | 2025-06-17 | filed | no | `core:Debtors` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 498321 | GBP | 2024-09-30 | 2025-06-17 | filed | yes | `core:Debtors` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 445794 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 445794 | GBP | 2024-09-30 | 2025-06-17 | filed | no | `core:Equity` | small |
| equity | 445894 | GBP | 2024-09-30 | 2025-06-17 | filed | no | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-09-30 | 2025-06-17 | filed | no | `core:Equity` | small |
| equity | 445894 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `core:Equity` | small |
| net_assets | 445894 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `core:NetAssetsLiabilities` | small |
| net_assets | 445894 | GBP | 2024-09-30 | 2025-06-17 | filed | no | `core:NetAssetsLiabilities` | small |
| net_current_assets | -108836 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `core:NetCurrentAssetsLiabilities` | small |
| net_current_assets | -108836 | GBP | 2024-09-30 | 2025-06-17 | filed | no | `core:NetCurrentAssetsLiabilities` | small |
| total_assets_less_current_liabilities | 1335218 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | small |
| total_assets_less_current_liabilities | 1335218 | GBP | 2024-09-30 | 2025-06-17 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | small |
| average_employees | 83 | xbrli:pure | 2023-09-30 | 2024-06-26 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | small |
| average_employees | 83 | xbrli:pure | 2023-09-30 | 2025-06-17 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | small |
| cash | 2781 | GBP | 2023-09-30 | 2024-06-26 | filed | no | `core:CashBankOnHand` | small |
| cash | 2781 | GBP | 2023-09-30 | 2025-06-17 | filed | yes | `core:CashBankOnHand` | small |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 16667 | GBP | 2023-09-30 | 2024-06-26 | filed | no | `core:Creditors` | small |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 16667 | GBP | 2023-09-30 | 2025-06-17 | filed | yes | `core:Creditors` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1467996 | GBP | 2023-09-30 | 2024-06-26 | filed | no | `core:Creditors` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1467996 | GBP | 2023-09-30 | 2025-06-17 | filed | yes | `core:Creditors` | small |
| current_assets | 544085 | GBP | 2023-09-30 | 2025-06-17 | filed | yes | `core:CurrentAssets` | small |
| current_assets | 544085 | GBP | 2023-09-30 | 2024-06-26 | filed | no | `core:CurrentAssets` | small |
| debtors | 541304 | GBP | 2023-09-30 | 2024-06-26 | filed | no | `core:Debtors` | small |
| debtors | 541304 | GBP | 2023-09-30 | 2025-06-17 | filed | yes | `core:Debtors` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 541304 | GBP | 2023-09-30 | 2025-06-17 | filed | yes | `core:Debtors` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 541304 | GBP | 2023-09-30 | 2024-06-26 | filed | no | `core:Debtors` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 444991 | GBP | 2023-09-30 | 2024-06-26 | filed | no | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 444991 | GBP | 2023-09-30 | 2025-06-17 | filed | yes | `core:Equity` | small |
| equity | 445091 | GBP | 2023-09-30 | 2024-06-26 | filed | no | `core:Equity` | small |
| equity | 445091 | GBP | 2023-09-30 | 2025-06-17 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-09-30 | 2025-06-17 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-09-30 | 2024-06-26 | filed | no | `core:Equity` | small |
| net_assets | 445091 | GBP | 2023-09-30 | 2025-06-17 | filed | yes | `core:NetAssetsLiabilities` | small |
| net_assets | 445091 | GBP | 2023-09-30 | 2024-06-26 | filed | no | `core:NetAssetsLiabilities` | small |
| net_current_assets | -923911 | GBP | 2023-09-30 | 2024-06-26 | filed | no | `core:NetCurrentAssetsLiabilities` | small |
| net_current_assets | -923911 | GBP | 2023-09-30 | 2025-06-17 | filed | yes | `core:NetCurrentAssetsLiabilities` | small |
| total_assets_less_current_liabilities | 544372 | GBP | 2023-09-30 | 2024-06-26 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | small |
| total_assets_less_current_liabilities | 544372 | GBP | 2023-09-30 | 2025-06-17 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | small |
| average_employees | 93 | xbrli:pure | 2022-03-31 | 2024-06-26 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | small |
| cash | 152 | GBP | 2022-03-31 | 2024-06-26 | filed | yes | `core:CashBankOnHand` | small |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 61552 | GBP | 2022-03-31 | 2024-06-26 | filed | yes | `core:Creditors` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1032622 | GBP | 2022-03-31 | 2024-06-26 | filed | yes | `core:Creditors` | small |
| current_assets | 124161 | GBP | 2022-03-31 | 2024-06-26 | filed | yes | `core:CurrentAssets` | small |
| debtors | 124009 | GBP | 2022-03-31 | 2024-06-26 | filed | yes | `core:Debtors` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 124009 | GBP | 2022-03-31 | 2024-06-26 | filed | yes | `core:Debtors` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2022-03-31 | 2024-06-26 | filed | yes | `core:Equity` | small |
| equity | 442290 | GBP | 2022-03-31 | 2024-06-26 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 442190 | GBP | 2022-03-31 | 2024-06-26 | filed | yes | `core:Equity` | small |
| net_assets | 442290 | GBP | 2022-03-31 | 2024-06-26 | filed | yes | `core:NetAssetsLiabilities` | small |
| net_current_assets | -908461 | GBP | 2022-03-31 | 2024-06-26 | filed | yes | `core:NetCurrentAssetsLiabilities` | small |
| total_assets_less_current_liabilities | 559593 | GBP | 2022-03-31 | 2024-06-26 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | small |

_No coverage facts for the latest run._

- event restatement @ 2026-06-29: `{"superseded_document_id": "gb:03327159:doc:P2fDhnyrB64FatRXwd2fZrq9cVihE5xk55LlughoC00", "restatements": [{"concept": "average_employees", "period_end": "2024-09-30", "old_value": "103.0000", "new_va`

## LIGHTNET LIMITED (`gb:03472224`)

- registration: `03472224` (GB), status active, incorporated 1997-11-27
- classification: ['62090'] (sic_2007)
- records: 5 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 79 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 3 | xbrli:pure | 2025-12-31 | 2026-05-27 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 143582 | GBP | 2025-12-31 | 2026-05-27 | filed | yes | `core:CashBankOnHand` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 100855 | GBP | 2025-12-31 | 2026-05-27 | filed | yes | `core:Creditors` | unaudited-abridged |
| current_assets | 177582 | GBP | 2025-12-31 | 2026-05-27 | filed | yes | `core:CurrentAssets` | unaudited-abridged |
| debtors | 34000 | GBP | 2025-12-31 | 2026-05-27 | filed | yes | `core:Debtors` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'OtherReservesSubtotal'}` | 150 | GBP | 2025-12-31 | 2026-05-27 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 150 | GBP | 2025-12-31 | 2026-05-27 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 258135 | GBP | 2025-12-31 | 2026-05-27 | filed | yes | `core:Equity` | unaudited-abridged |
| equity | 258435 | GBP | 2025-12-31 | 2026-05-27 | filed | yes | `core:Equity` | unaudited-abridged |
| net_assets | 258435 | GBP | 2025-12-31 | 2026-05-27 | filed | yes | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 76727 | GBP | 2025-12-31 | 2026-05-27 | filed | yes | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 258435 | GBP | 2025-12-31 | 2026-05-27 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 2 | xbrli:pure | 2024-12-31 | 2026-05-27 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| average_employees | 2 | xbrli:pure | 2024-12-31 | 2025-07-29 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 121821 | GBP | 2024-12-31 | 2026-05-27 | filed | yes | `core:CashBankOnHand` | unaudited-abridged |
| cash | 121821 | GBP | 2024-12-31 | 2025-07-29 | filed | no | `core:CashBankOnHand` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 86405 | GBP | 2024-12-31 | 2025-07-29 | filed | no | `core:Creditors` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 86405 | GBP | 2024-12-31 | 2026-05-27 | filed | yes | `core:Creditors` | unaudited-abridged |
| current_assets | 179372 | GBP | 2024-12-31 | 2025-07-29 | filed | no | `core:CurrentAssets` | unaudited-abridged |
| current_assets | 179372 | GBP | 2024-12-31 | 2026-05-27 | filed | yes | `core:CurrentAssets` | unaudited-abridged |
| debtors | 57551 | GBP | 2024-12-31 | 2025-07-29 | filed | no | `core:Debtors` | unaudited-abridged |
| debtors | 57551 | GBP | 2024-12-31 | 2026-05-27 | filed | yes | `core:Debtors` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 150 | GBP | 2024-12-31 | 2025-07-29 | filed | no | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 280571 | GBP | 2024-12-31 | 2026-05-27 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 280571 | GBP | 2024-12-31 | 2025-07-29 | filed | no | `core:Equity` | unaudited-abridged |
| equity | 280871 | GBP | 2024-12-31 | 2025-07-29 | filed | no | `core:Equity` | unaudited-abridged |
| equity | 280871 | GBP | 2024-12-31 | 2026-05-27 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'OtherReservesSubtotal'}` | 150 | GBP | 2024-12-31 | 2025-07-29 | filed | no | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 150 | GBP | 2024-12-31 | 2026-05-27 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'OtherReservesSubtotal'}` | 150 | GBP | 2024-12-31 | 2026-05-27 | filed | yes | `core:Equity` | unaudited-abridged |
| net_assets | 280871 | GBP | 2024-12-31 | 2026-05-27 | filed | yes | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_assets | 280871 | GBP | 2024-12-31 | 2025-07-29 | filed | no | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 92967 | GBP | 2024-12-31 | 2026-05-27 | filed | yes | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 92967 | GBP | 2024-12-31 | 2025-07-29 | filed | no | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 280871 | GBP | 2024-12-31 | 2025-07-29 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 280871 | GBP | 2024-12-31 | 2026-05-27 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 2 | xbrli:pure | 2023-12-31 | 2025-07-29 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| average_employees | 2 | xbrli:pure | 2023-12-31 | 2024-08-15 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 104798 | GBP | 2023-12-31 | 2024-08-15 | filed | no | `core:CashBankOnHand` | unaudited-abridged |
| cash | 104798 | GBP | 2023-12-31 | 2025-07-29 | filed | yes | `core:CashBankOnHand` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 74908 | GBP | 2023-12-31 | 2025-07-29 | filed | yes | `core:Creditors` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 74908 | GBP | 2023-12-31 | 2024-08-15 | filed | no | `core:Creditors` | unaudited-abridged |
| current_assets | 162349 | GBP | 2023-12-31 | 2025-07-29 | filed | yes | `core:CurrentAssets` | unaudited-abridged |
| current_assets | 162349 | GBP | 2023-12-31 | 2024-08-15 | filed | no | `core:CurrentAssets` | unaudited-abridged |
| debtors | 57551 | GBP | 2023-12-31 | 2025-07-29 | filed | yes | `core:Debtors` | unaudited-abridged |
| debtors | 57551 | GBP | 2023-12-31 | 2024-08-15 | filed | no | `core:Debtors` | unaudited-abridged |
| equity | 262857 | GBP | 2023-12-31 | 2024-08-15 | filed | no | `core:Equity` | unaudited-abridged |
| equity | 262857 | GBP | 2023-12-31 | 2025-07-29 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 262557 | GBP | 2023-12-31 | 2024-08-15 | filed | no | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'OtherReservesSubtotal'}` | 150 | GBP | 2023-12-31 | 2025-07-29 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 262557 | GBP | 2023-12-31 | 2025-07-29 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 150 | GBP | 2023-12-31 | 2024-08-15 | filed | no | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'OtherReservesSubtotal'}` | 150 | GBP | 2023-12-31 | 2024-08-15 | filed | no | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 150 | GBP | 2023-12-31 | 2025-07-29 | filed | yes | `core:Equity` | unaudited-abridged |
| net_assets | 262857 | GBP | 2023-12-31 | 2025-07-29 | filed | yes | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_assets | 262857 | GBP | 2023-12-31 | 2024-08-15 | filed | no | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 87441 | GBP | 2023-12-31 | 2025-07-29 | filed | yes | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 87441 | GBP | 2023-12-31 | 2024-08-15 | filed | no | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 262857 | GBP | 2023-12-31 | 2024-08-15 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 262857 | GBP | 2023-12-31 | 2025-07-29 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 2 | xbrli:pure | 2022-12-31 | 2024-08-15 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 158332 | GBP | 2022-12-31 | 2024-08-15 | filed | yes | `core:CashBankOnHand` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 142467 | GBP | 2022-12-31 | 2024-08-15 | filed | yes | `core:Creditors` | unaudited-abridged |
| current_assets | 229408 | GBP | 2022-12-31 | 2024-08-15 | filed | yes | `core:CurrentAssets` | unaudited-abridged |
| debtors | 71076 | GBP | 2022-12-31 | 2024-08-15 | filed | yes | `core:Debtors` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 265799 | GBP | 2022-12-31 | 2024-08-15 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'OtherReservesSubtotal'}` | 150 | GBP | 2022-12-31 | 2024-08-15 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 150 | GBP | 2022-12-31 | 2024-08-15 | filed | yes | `core:Equity` | unaudited-abridged |
| equity | 266099 | GBP | 2022-12-31 | 2024-08-15 | filed | yes | `core:Equity` | unaudited-abridged |
| net_assets | 266099 | GBP | 2022-12-31 | 2024-08-15 | filed | yes | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 86941 | GBP | 2022-12-31 | 2024-08-15 | filed | yes | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 266099 | GBP | 2022-12-31 | 2024-08-15 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |

Coverage @ 2025-12-31: 9/21 concepts available (average_employees, cash, creditors_within_one_year, current_assets, debtors, equity, net_assets, net_current_assets, total_assets_less_current_liabilities)
- `creditors_after_one_year`: filed_without_concept — absent though regime 'unaudited-abridged' typically includes it
- `depreciation_amortisation`: filed_without_concept — regime 'unaudited-abridged' omits this concept
- `fixed_assets`: filed_without_concept — absent though regime 'unaudited-abridged' typically includes it
- `gross_profit`: filed_without_concept — regime 'unaudited-abridged' omits this concept
- `operating_profit`: filed_without_concept — regime 'unaudited-abridged' omits this concept
- `profit_before_tax`: filed_without_concept — regime 'unaudited-abridged' omits this concept
- `profit_for_period`: filed_without_concept — regime 'unaudited-abridged' omits this concept
- `retained_earnings`: filed_without_concept — absent though regime 'unaudited-abridged' typically includes it
- `revenue`: filed_without_concept — regime 'unaudited-abridged' omits this concept
- `share_capital`: filed_without_concept — absent though regime 'unaudited-abridged' typically includes it
- `staff_costs`: filed_without_concept — regime 'unaudited-abridged' omits this concept
- `tax_charge`: filed_without_concept — regime 'unaudited-abridged' omits this concept
