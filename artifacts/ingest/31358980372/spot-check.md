# Ingest spot-check

- database: `data/engine.db`
- latest run: `20260810T053359Z-e8cc4689`
- companies in store: 1000; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## ST. CHRISTOPHERS HOSPICE (`gb:00681880`)

- registration: `00681880` (GB), status active, incorporated 1961-01-27
- classification: ['86101'] (sic_2007)
- records: 90 officers, 0 beneficial owners, 1 ownership statements, 2 security interests, 286 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## SALES AUTOMATION SYSTEMS LIMITED (`gb:00946280`)

- registration: `00946280` (GB), status active, incorporated 1969-01-20
- classification: ['62090'] (sic_2007)
- records: 6 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 102 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-11-30 | 2026-01-13 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 53843 | GBP | 2025-11-30 | 2026-01-13 | filed | yes | `core:CashBankOnHand` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 20364 | GBP | 2025-11-30 | 2026-01-13 | filed | yes | `core:Creditors` | unaudited-abridged |
| current_assets | 53843 | GBP | 2025-11-30 | 2026-01-13 | filed | yes | `core:CurrentAssets` | unaudited-abridged |
| equity | 45479 | GBP | 2025-11-30 | 2026-01-13 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10 | GBP | 2025-11-30 | 2026-01-13 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 45469 | GBP | 2025-11-30 | 2026-01-13 | filed | yes | `core:Equity` | unaudited-abridged |
| fixed_assets | 12000 | GBP | 2025-11-30 | 2026-01-13 | filed | yes | `core:FixedAssets` | unaudited-abridged |
| net_assets | 45479 | GBP | 2025-11-30 | 2026-01-13 | filed | yes | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 33479 | GBP | 2025-11-30 | 2026-01-13 | filed | yes | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 45479 | GBP | 2025-11-30 | 2026-01-13 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 2 | xbrli:pure | 2024-11-30 | 2026-01-13 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| average_employees | 2 | xbrli:pure | 2024-11-30 | 2025-04-16 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 22894 | GBP | 2024-11-30 | 2025-04-16 | filed | no | `core:CashBankOnHand` | unaudited-abridged |
| cash | 22894 | GBP | 2024-11-30 | 2026-01-13 | filed | yes | `core:CashBankOnHand` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 21025 | GBP | 2024-11-30 | 2025-04-16 | filed | no | `core:Creditors` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 21025 | GBP | 2024-11-30 | 2026-01-13 | filed | yes | `core:Creditors` | unaudited-abridged |
| current_assets | 22894 | GBP | 2024-11-30 | 2026-01-13 | filed | yes | `core:CurrentAssets` | unaudited-abridged |
| current_assets | 22894 | GBP | 2024-11-30 | 2025-04-16 | filed | no | `core:CurrentAssets` | unaudited-abridged |
| equity | 13869 | GBP | 2024-11-30 | 2026-01-13 | filed | yes | `core:Equity` | unaudited-abridged |
| equity | 13869 | GBP | 2024-11-30 | 2025-04-16 | filed | no | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10 | GBP | 2024-11-30 | 2026-01-13 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 13859 | GBP | 2024-11-30 | 2026-01-13 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 13859 | GBP | 2024-11-30 | 2025-04-16 | filed | no | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10 | GBP | 2024-11-30 | 2025-04-16 | filed | no | `core:Equity` | unaudited-abridged |
| fixed_assets | 12000 | GBP | 2024-11-30 | 2026-01-13 | filed | yes | `core:FixedAssets` | unaudited-abridged |
| fixed_assets | 12000 | GBP | 2024-11-30 | 2025-04-16 | filed | no | `core:FixedAssets` | unaudited-abridged |
| net_assets | 13869 | GBP | 2024-11-30 | 2026-01-13 | filed | yes | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_assets | 13869 | GBP | 2024-11-30 | 2025-04-16 | filed | no | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 1869 | GBP | 2024-11-30 | 2025-04-16 | filed | no | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 1869 | GBP | 2024-11-30 | 2026-01-13 | filed | yes | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 13869 | GBP | 2024-11-30 | 2026-01-13 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 13869 | GBP | 2024-11-30 | 2025-04-16 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 2 | xbrli:pure | 2023-11-30 | 2024-01-12 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| average_employees | 2 | xbrli:pure | 2023-11-30 | 2025-04-16 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 25460 | GBP | 2023-11-30 | 2025-04-16 | filed | yes | `core:CashBankOnHand` | unaudited-abridged |
| cash | 25460 | GBP | 2023-11-30 | 2024-01-12 | filed | no | `core:CashBankOnHand` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 13844 | GBP | 2023-11-30 | 2025-04-16 | filed | yes | `core:Creditors` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 13844 | GBP | 2023-11-30 | 2024-01-12 | filed | no | `core:Creditors` | unaudited-abridged |
| current_assets | 25460 | GBP | 2023-11-30 | 2025-04-16 | filed | yes | `core:CurrentAssets` | unaudited-abridged |
| current_assets | 25460 | GBP | 2023-11-30 | 2024-01-12 | filed | no | `core:CurrentAssets` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10 | GBP | 2023-11-30 | 2025-04-16 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 23606 | GBP | 2023-11-30 | 2025-04-16 | filed | yes | `core:Equity` | unaudited-abridged |
| equity | 23616 | GBP | 2023-11-30 | 2025-04-16 | filed | yes | `core:Equity` | unaudited-abridged |
| equity | 23616 | GBP | 2023-11-30 | 2024-01-12 | filed | no | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 23606 | GBP | 2023-11-30 | 2024-01-12 | filed | no | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10 | GBP | 2023-11-30 | 2024-01-12 | filed | no | `core:Equity` | unaudited-abridged |
| fixed_assets | 12000 | GBP | 2023-11-30 | 2025-04-16 | filed | yes | `core:FixedAssets` | unaudited-abridged |
| fixed_assets | 12000 | GBP | 2023-11-30 | 2024-01-12 | filed | no | `core:FixedAssets` | unaudited-abridged |
| net_assets | 23616 | GBP | 2023-11-30 | 2024-01-12 | filed | no | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_assets | 23616 | GBP | 2023-11-30 | 2025-04-16 | filed | yes | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 11616 | GBP | 2023-11-30 | 2025-04-16 | filed | yes | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 11616 | GBP | 2023-11-30 | 2024-01-12 | filed | no | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 23616 | GBP | 2023-11-30 | 2024-01-12 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 23616 | GBP | 2023-11-30 | 2025-04-16 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 2 | xbrli:pure | 2022-11-30 | 2024-01-12 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 68761 | GBP | 2022-11-30 | 2024-01-12 | filed | yes | `core:CashBankOnHand` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 21080 | GBP | 2022-11-30 | 2024-01-12 | filed | yes | `core:Creditors` | unaudited-abridged |
| current_assets | 68761 | GBP | 2022-11-30 | 2024-01-12 | filed | yes | `core:CurrentAssets` | unaudited-abridged |
| equity | 63827 | GBP | 2022-11-30 | 2024-01-12 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10 | GBP | 2022-11-30 | 2024-01-12 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 63817 | GBP | 2022-11-30 | 2024-01-12 | filed | yes | `core:Equity` | unaudited-abridged |
| fixed_assets | 16146 | GBP | 2022-11-30 | 2024-01-12 | filed | yes | `core:FixedAssets` | unaudited-abridged |
| net_assets | 63827 | GBP | 2022-11-30 | 2024-01-12 | filed | yes | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 47681 | GBP | 2022-11-30 | 2024-01-12 | filed | yes | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 63827 | GBP | 2022-11-30 | 2024-01-12 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |

Coverage @ 2025-11-30: 9/21 concepts available (average_employees, cash, creditors_within_one_year, current_assets, equity, fixed_assets, net_assets, net_current_assets, total_assets_less_current_liabilities)
- `creditors_after_one_year`: filed_without_concept — absent though regime 'unaudited-abridged' typically includes it
- `debtors`: filed_without_concept — absent though regime 'unaudited-abridged' typically includes it
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

## J.P. RADIA & CO. LIMITED (`gb:01098849`)

- registration: `01098849` (GB), status active, incorporated 1973-02-27
- classification: ['62030'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 94 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | xbrli:pure | 2025-03-31 | 2025-10-07 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 18641 | GBP | 2025-03-31 | 2025-10-07 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 9679 | GBP | 2025-03-31 | 2025-10-07 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 16038 | GBP | 2025-03-31 | 2025-10-07 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 25000 | GBP | 2025-03-31 | 2025-10-07 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 16038 | GBP | 2025-03-31 | 2025-10-07 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -8962 | GBP | 2025-03-31 | 2025-10-07 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 16038 | GBP | 2025-03-31 | 2025-10-07 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2024-03-31 | 2024-12-24 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | xbrli:pure | 2024-03-31 | 2025-10-07 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 16775 | GBP | 2024-03-31 | 2024-12-24 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 16775 | GBP | 2024-03-31 | 2025-10-07 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 9351 | GBP | 2024-03-31 | 2024-12-24 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 9351 | GBP | 2024-03-31 | 2025-10-07 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 17576 | GBP | 2024-03-31 | 2024-12-24 | filed | no | `core:Equity` | micro-entity |
| equity | 17576 | GBP | 2024-03-31 | 2025-10-07 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 25000 | GBP | 2024-03-31 | 2024-12-24 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 25000 | GBP | 2024-03-31 | 2025-10-07 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 17576 | GBP | 2024-03-31 | 2025-10-07 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 17576 | GBP | 2024-03-31 | 2024-12-24 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -7424 | GBP | 2024-03-31 | 2024-12-24 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -7424 | GBP | 2024-03-31 | 2025-10-07 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 17576 | GBP | 2024-03-31 | 2025-10-07 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 17576 | GBP | 2024-03-31 | 2024-12-24 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2023-03-31 | 2023-12-20 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | xbrli:pure | 2023-03-31 | 2024-12-24 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 21289 | GBP | 2023-03-31 | 2024-12-24 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 21289 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 14743 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 14743 | GBP | 2023-03-31 | 2024-12-24 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 18454 | GBP | 2023-03-31 | 2024-12-24 | filed | yes | `core:Equity` | micro-entity |
| equity | 18454 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 25000 | GBP | 2023-03-31 | 2024-12-24 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 25000 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | 18454 | GBP | 2023-03-31 | 2024-12-24 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 18454 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -6546 | GBP | 2023-03-31 | 2024-12-24 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -6546 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 18454 | GBP | 2023-03-31 | 2024-12-24 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 18454 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2022-03-31 | 2023-12-20 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 45023 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 34073 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 75496 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 21400 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 25000 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 21400 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 41423 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 66423 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

Coverage @ 2025-03-31: 8/21 concepts available (average_employees, creditors_within_one_year, current_assets, equity, fixed_assets, net_assets, net_current_assets, total_assets_less_current_liabilities)
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

## THERMAL DEVELOPMENTS LIMITED (`gb:01236039`)

- registration: `01236039` (GB), status active, incorporated 1975-12-02
- classification: ['71122'] (sic_2007)
- records: 3 officers, 1 beneficial owners, 0 ownership statements, 1 security interests, 87 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-12-31 | 2026-02-25 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2025-12-31 | 2026-02-25 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 35287 | GBP | 2025-12-31 | 2026-02-25 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 7917 | GBP | 2025-12-31 | 2026-02-25 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 49098 | GBP | 2025-12-31 | 2026-02-25 | filed | yes | `core:Equity` | micro-entity |
| net_assets | 49098 | GBP | 2025-12-31 | 2026-02-25 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -27370 | GBP | 2025-12-31 | 2026-02-25 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 49098 | GBP | 2025-12-31 | 2026-02-25 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-12-31 | 2026-02-25 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-12-31 | 2025-03-31 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2024-12-31 | 2025-03-31 | filed | no | `core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2024-12-31 | 2026-02-25 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 34119 | GBP | 2024-12-31 | 2025-03-31 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 34119 | GBP | 2024-12-31 | 2026-02-25 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 8938 | GBP | 2024-12-31 | 2026-02-25 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 8938 | GBP | 2024-12-31 | 2025-03-31 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 52024 | GBP | 2024-12-31 | 2025-03-31 | filed | no | `core:Equity` | micro-entity |
| equity | 52024 | GBP | 2024-12-31 | 2026-02-25 | filed | yes | `core:Equity` | micro-entity |
| net_assets | 52024 | GBP | 2024-12-31 | 2025-03-31 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 52024 | GBP | 2024-12-31 | 2026-02-25 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -25181 | GBP | 2024-12-31 | 2025-03-31 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -25181 | GBP | 2024-12-31 | 2026-02-25 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 52024 | GBP | 2024-12-31 | 2026-02-25 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 52024 | GBP | 2024-12-31 | 2025-03-31 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-12-31 | 2025-03-31 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-12-31 | 2024-02-07 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2023-12-31 | 2024-02-07 | filed | no | `core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2023-12-31 | 2025-03-31 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 39913 | GBP | 2023-12-31 | 2025-03-31 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 39913 | GBP | 2023-12-31 | 2024-02-07 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 13401 | GBP | 2023-12-31 | 2024-02-07 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 13401 | GBP | 2023-12-31 | 2025-03-31 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 51591 | GBP | 2023-12-31 | 2024-02-07 | filed | no | `core:Equity` | micro-entity |
| equity | 51591 | GBP | 2023-12-31 | 2025-03-31 | filed | yes | `core:Equity` | micro-entity |
| net_assets | 51591 | GBP | 2023-12-31 | 2025-03-31 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 51591 | GBP | 2023-12-31 | 2024-02-07 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -26512 | GBP | 2023-12-31 | 2024-02-07 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -26512 | GBP | 2023-12-31 | 2025-03-31 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 51591 | GBP | 2023-12-31 | 2024-02-07 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 51591 | GBP | 2023-12-31 | 2025-03-31 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2022-12-31 | 2024-02-07 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2022-12-31 | 2024-02-07 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 54025 | GBP | 2022-12-31 | 2024-02-07 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 25973 | GBP | 2022-12-31 | 2024-02-07 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 51148 | GBP | 2022-12-31 | 2024-02-07 | filed | yes | `core:Equity` | micro-entity |
| net_assets | 51148 | GBP | 2022-12-31 | 2024-02-07 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -28052 | GBP | 2022-12-31 | 2024-02-07 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 51148 | GBP | 2022-12-31 | 2024-02-07 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

Coverage @ 2025-12-31: 8/21 concepts available (average_employees, creditors_after_one_year, creditors_within_one_year, current_assets, equity, net_assets, net_current_assets, total_assets_less_current_liabilities)
- `cash`: filed_without_concept — regime 'micro-entity' omits this concept
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

## NWD ARCHITECTS LTD (`gb:01315851`)

- registration: `01315851` (GB), status active, incorporated 1977-06-01
- classification: ['71111'] (sic_2007)
- records: 10 officers, 2 beneficial owners, 0 ownership statements, 1 security interests, 109 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 10 | xbrli:pure | 2025-03-31 | 2025-08-13 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 102024 | GBP | 2025-03-31 | 2025-08-13 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 204205 | GBP | 2025-03-31 | 2025-08-13 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 102181 | GBP | 2025-03-31 | 2025-08-13 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 102181 | GBP | 2025-03-31 | 2025-08-13 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 119659 | GBP | 2025-03-31 | 2025-08-13 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-03-31 | 2025-08-13 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 119559 | GBP | 2025-03-31 | 2025-08-13 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | 110507 | GBP | 2025-03-31 | 2025-08-13 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 118306 | GBP | 2025-03-31 | 2025-08-13 | filed | yes | `ns5:ProfitLoss` | total-exemption-full |
| total_assets_less_current_liabilities | 119659 | GBP | 2025-03-31 | 2025-08-13 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 10 | xbrli:pure | 2024-03-31 | 2025-08-13 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 10 | xbrli:pure | 2024-03-31 | 2024-07-23 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 94119 | GBP | 2024-03-31 | 2024-07-23 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 94119 | GBP | 2024-03-31 | 2025-08-13 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 217697 | GBP | 2024-03-31 | 2024-07-23 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 217697 | GBP | 2024-03-31 | 2025-08-13 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 123578 | GBP | 2024-03-31 | 2024-07-23 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 123578 | GBP | 2024-03-31 | 2024-07-23 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 123578 | GBP | 2024-03-31 | 2025-08-13 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 123578 | GBP | 2024-03-31 | 2025-08-13 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 129253 | GBP | 2024-03-31 | 2024-07-23 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 129353 | GBP | 2024-03-31 | 2025-08-13 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-03-31 | 2025-08-13 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-03-31 | 2024-07-23 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 129353 | GBP | 2024-03-31 | 2024-07-23 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 129253 | GBP | 2024-03-31 | 2025-08-13 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | 119794 | GBP | 2024-03-31 | 2024-07-23 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 119794 | GBP | 2024-03-31 | 2025-08-13 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 130516 | GBP | 2024-03-31 | 2024-07-23 | filed | yes | `ns5:ProfitLoss` | total-exemption-full |
| total_assets_less_current_liabilities | 129353 | GBP | 2024-03-31 | 2024-07-23 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 129353 | GBP | 2024-03-31 | 2025-08-13 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 10 | xbrli:pure | 2023-03-31 | 2024-07-23 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 10 | xbrli:pure | 2023-03-31 | 2023-12-20 | filed | no | `ns6:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 88837 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `ns6:CashBankOnHand` | total-exemption-full |
| cash | 88837 | GBP | 2023-03-31 | 2024-07-23 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 210860 | GBP | 2023-03-31 | 2024-07-23 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 210860 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `ns6:CurrentAssets` | total-exemption-full |
| debtors | 122023 | GBP | 2023-03-31 | 2024-07-23 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 122023 | GBP | 2023-03-31 | 2024-07-23 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 122023 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `ns6:Debtors` | total-exemption-full |
| debtors | 122023 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `ns6:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 126737 | GBP | 2023-03-31 | 2024-07-23 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 126837 | GBP | 2023-03-31 | 2024-07-23 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-03-31 | 2024-07-23 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 126837 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 126737 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `ns6:Equity` | total-exemption-full |
| net_current_assets | 118336 | GBP | 2023-03-31 | 2024-07-23 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 118336 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `ns6:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 122064 | GBP | 2023-03-31 | 2023-12-20 | filed | yes | `ns6:ProfitLoss` | total-exemption-full |
| total_assets_less_current_liabilities | 126837 | GBP | 2023-03-31 | 2024-07-23 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 126837 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `ns6:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 7 | xbrli:pure | 2022-03-31 | 2023-12-20 | filed | yes | `ns6:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 80455 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `ns6:CashBankOnHand` | total-exemption-full |
| current_assets | 227295 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `ns6:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 146840 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `ns6:Debtors` | total-exemption-full |
| debtors | 146840 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `ns6:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `ns6:Equity` | total-exemption-full |
| equity | 125773 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 125673 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `ns6:Equity` | total-exemption-full |
| net_current_assets | 114282 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `ns6:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 125773 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `ns6:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

Coverage @ 2025-03-31: 8/21 concepts available (average_employees, cash, current_assets, debtors, equity, net_current_assets, profit_for_period, total_assets_less_current_liabilities)
- `creditors_after_one_year`: filed_without_concept — absent though regime 'total-exemption-full' typically includes it
- `creditors_within_one_year`: filed_without_concept — absent though regime 'total-exemption-full' typically includes it
- `depreciation_amortisation`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `fixed_assets`: filed_without_concept — absent though regime 'total-exemption-full' typically includes it
- `gross_profit`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `net_assets`: filed_without_concept — absent though regime 'total-exemption-full' typically includes it
- `operating_profit`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `profit_before_tax`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `retained_earnings`: filed_without_concept — absent though regime 'total-exemption-full' typically includes it
- `revenue`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `share_capital`: filed_without_concept — absent though regime 'total-exemption-full' typically includes it
- `staff_costs`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `tax_charge`: filed_without_concept — regime 'total-exemption-full' omits this concept

## WSP UK LIMITED (`gb:01383511`)

- registration: `01383511` (GB), status active, incorporated 1978-08-11
- classification: ['71122'] (sic_2007)
- records: 89 officers, 1 beneficial owners, 0 ownership statements, 8 security interests, 347 filings, 0 events, 3 source documents

_No figures persisted for this company._

Coverage @ 2025-12-31: 0/21 concepts available
- `average_employees`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `cash`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `creditors_after_one_year`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `creditors_within_one_year`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `current_assets`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `debtors`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `depreciation_amortisation`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `equity`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `fixed_assets`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `gross_profit`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `net_assets`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `net_current_assets`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `operating_profit`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `profit_before_tax`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `profit_for_period`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `retained_earnings`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `revenue`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `share_capital`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `staff_costs`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `tax_charge`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `total_assets_less_current_liabilities`: unparseable_format — no machine-readable rendition (content_type=application/pdf)

## OPTIO SYSTEMS LIMITED (`gb:01442610`)

- registration: `01442610` (GB), status active, incorporated 1979-08-08
- classification: ['62020'] (sic_2007)
- records: 14 officers, 2 beneficial owners, 0 ownership statements, 3 security interests, 143 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 20 | xbrli:pure | 2024-12-31 | 2025-07-01 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | small |
| cash | 674217 | GBP | 2024-12-31 | 2025-07-01 | filed | yes | `core:CashBankOnHand` | small |
| current_assets | 3772140 | GBP | 2024-12-31 | 2025-07-01 | filed | yes | `core:CurrentAssets` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 3050085 | GBP | 2024-12-31 | 2025-07-01 | filed | yes | `core:Debtors` | small |
| debtors | 3050085 | GBP | 2024-12-31 | 2025-07-01 | filed | yes | `core:Debtors` | small |
| equity | 2333856 | GBP | 2024-12-31 | 2025-07-01 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 1334 | GBP | 2024-12-31 | 2025-07-01 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2329522 | GBP | 2024-12-31 | 2025-07-01 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2001 | GBP | 2024-12-31 | 2025-07-01 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 999 | GBP | 2024-12-31 | 2025-07-01 | filed | yes | `core:Equity` | small |
| net_assets | 2333856 | GBP | 2024-12-31 | 2025-07-01 | filed | yes | `core:NetAssetsLiabilities` | small |
| net_current_assets | 2337727 | GBP | 2024-12-31 | 2025-07-01 | filed | yes | `core:NetCurrentAssetsLiabilities` | small |
| total_assets_less_current_liabilities | 2349227 | GBP | 2024-12-31 | 2025-07-01 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | small |
| average_employees | 19 | xbrli:pure | 2023-12-31 | 2025-07-01 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | small |
| average_employees | 19 | xbrli:pure | 2023-12-31 | 2024-12-23 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | small |
| cash | 602616 | GBP | 2023-12-31 | 2025-07-01 | filed | yes | `core:CashBankOnHand` | small |
| cash | 602616 | GBP | 2023-12-31 | 2024-12-23 | filed | no | `core:CashBankOnHand` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1325447 | GBP | 2023-12-31 | 2024-12-23 | filed | yes | `core:Creditors` | small |
| current_assets | 2925267 | GBP | 2023-12-31 | 2024-12-23 | filed | no | `core:CurrentAssets` | small |
| current_assets | 2925267 | GBP | 2023-12-31 | 2025-07-01 | filed | yes | `core:CurrentAssets` | small |
| debtors | 2260831 | GBP | 2023-12-31 | 2025-07-01 | filed | yes | `core:Debtors` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2260831 | GBP | 2023-12-31 | 2025-07-01 | filed | yes | `core:Debtors` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2260831 | GBP | 2023-12-31 | 2024-12-23 | filed | no | `core:Debtors` | small |
| debtors | 2260831 | GBP | 2023-12-31 | 2024-12-23 | filed | no | `core:Debtors` | small |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 999 | GBP | 2023-12-31 | 2024-12-23 | filed | no | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2001 | GBP | 2023-12-31 | 2024-12-23 | filed | no | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2001 | GBP | 2023-12-31 | 2025-07-01 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1598247 | GBP | 2023-12-31 | 2024-12-23 | filed | no | `core:Equity` | small |
| equity | 1602581 | GBP | 2023-12-31 | 2024-12-23 | filed | no | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 1334 | GBP | 2023-12-31 | 2025-07-01 | filed | yes | `core:Equity` | small |
| equity | 1602581 | GBP | 2023-12-31 | 2025-07-01 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 999 | GBP | 2023-12-31 | 2025-07-01 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1598247 | GBP | 2023-12-31 | 2025-07-01 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 1334 | GBP | 2023-12-31 | 2024-12-23 | filed | no | `core:Equity` | small |
| net_assets | 1602581 | GBP | 2023-12-31 | 2024-12-23 | filed | no | `core:NetAssetsLiabilities` | small |
| net_assets | 1602581 | GBP | 2023-12-31 | 2025-07-01 | filed | yes | `core:NetAssetsLiabilities` | small |
| net_current_assets | 1599820 | GBP | 2023-12-31 | 2024-12-23 | filed | no | `core:NetCurrentAssetsLiabilities` | small |
| net_current_assets | 1599820 | GBP | 2023-12-31 | 2025-07-01 | filed | yes | `core:NetCurrentAssetsLiabilities` | small |
| total_assets_less_current_liabilities | 1617952 | GBP | 2023-12-31 | 2024-12-23 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | small |
| total_assets_less_current_liabilities | 1617952 | GBP | 2023-12-31 | 2025-07-01 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | small |
| average_employees | 17 | xbrli:pure | 2022-12-31 | 2024-12-23 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | small |
| cash | 757718 | GBP | 2022-12-31 | 2024-12-23 | filed | yes | `core:CashBankOnHand` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1655372 | GBP | 2022-12-31 | 2024-12-23 | filed | yes | `core:Creditors` | small |
| current_assets | 2179662 | GBP | 2022-12-31 | 2024-12-23 | filed | yes | `core:CurrentAssets` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1206754 | GBP | 2022-12-31 | 2024-12-23 | filed | yes | `core:Debtors` | small |
| debtors | 1207767 | GBP | 2022-12-31 | 2024-12-23 | filed | yes | `core:Debtors` | small |
| equity | 543897 | GBP | 2022-12-31 | 2024-12-23 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 1334 | GBP | 2022-12-31 | 2024-12-23 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 999 | GBP | 2022-12-31 | 2024-12-23 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2001 | GBP | 2022-12-31 | 2024-12-23 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 539563 | GBP | 2022-12-31 | 2024-12-23 | filed | yes | `core:Equity` | small |
| net_assets | 543897 | GBP | 2022-12-31 | 2024-12-23 | filed | yes | `core:NetAssetsLiabilities` | small |
| net_current_assets | 524290 | GBP | 2022-12-31 | 2024-12-23 | filed | yes | `core:NetCurrentAssetsLiabilities` | small |
| total_assets_less_current_liabilities | 543897 | GBP | 2022-12-31 | 2024-12-23 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | small |

Coverage @ 2024-12-31: 8/21 concepts available (average_employees, cash, current_assets, debtors, equity, net_assets, net_current_assets, total_assets_less_current_liabilities)
- `creditors_after_one_year`: filed_without_concept — absent though regime 'small' typically includes it
- `creditors_within_one_year`: filed_without_concept — absent though regime 'small' typically includes it
- `depreciation_amortisation`: filed_without_concept — regime 'small' omits this concept
- `fixed_assets`: filed_without_concept — absent though regime 'small' typically includes it
- `gross_profit`: filed_without_concept — regime 'small' omits this concept
- `operating_profit`: filed_without_concept — regime 'small' omits this concept
- `profit_before_tax`: filed_without_concept — regime 'small' omits this concept
- `profit_for_period`: filed_without_concept — regime 'small' omits this concept
- `retained_earnings`: filed_without_concept — absent though regime 'small' typically includes it
- `revenue`: filed_without_concept — regime 'small' omits this concept
- `share_capital`: filed_without_concept — absent though regime 'small' typically includes it
- `staff_costs`: filed_without_concept — regime 'small' omits this concept
- `tax_charge`: filed_without_concept — regime 'small' omits this concept

## MCCARTHY GROUP LIMITED (`gb:01509617`)

- registration: `01509617` (GB), status active, incorporated 1980-07-29
- classification: ['71129'] (sic_2007)
- records: 6 officers, 1 beneficial owners, 0 ownership statements, 3 security interests, 124 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | xbrli:pure | 2025-01-31 | 2025-10-22 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 29980 | GBP | 2025-01-31 | 2025-10-22 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 30338 | GBP | 2025-01-31 | 2025-10-22 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 326668 | GBP | 2025-01-31 | 2025-10-22 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 296688 | GBP | 2025-01-31 | 2025-10-22 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 296688 | GBP | 2025-01-31 | 2025-10-22 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 57000 | GBP | 2025-01-31 | 2025-10-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 1056046 | GBP | 2025-01-31 | 2025-10-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 3000 | GBP | 2025-01-31 | 2025-10-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 169977 | GBP | 2025-01-31 | 2025-10-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 826069 | GBP | 2025-01-31 | 2025-10-22 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 759716 | GBP | 2025-01-31 | 2025-10-22 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | 1056046 | GBP | 2025-01-31 | 2025-10-22 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 296330 | GBP | 2025-01-31 | 2025-10-22 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1056046 | GBP | 2025-01-31 | 2025-10-22 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0.03 | xbrli:pure | 2024-01-31 | 2025-10-22 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 3 | xbrli:pure | 2024-01-31 | 2024-10-30 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 100665 | GBP | 2024-01-31 | 2024-10-30 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 100665 | GBP | 2024-01-31 | 2025-10-22 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 29910 | GBP | 2024-01-31 | 2024-10-30 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 29910 | GBP | 2024-01-31 | 2025-10-22 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 349847 | GBP | 2024-01-31 | 2024-10-30 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 349847 | GBP | 2024-01-31 | 2025-10-22 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 249182 | GBP | 2024-01-31 | 2024-10-30 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 249182 | GBP | 2024-01-31 | 2025-10-22 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 249182 | GBP | 2024-01-31 | 2025-10-22 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 249182 | GBP | 2024-01-31 | 2024-10-30 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 3000 | GBP | 2024-01-31 | 2024-10-30 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 3000 | GBP | 2024-01-31 | 2025-10-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 57000 | GBP | 2024-01-31 | 2025-10-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 858014 | GBP | 2024-01-31 | 2025-10-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 169977 | GBP | 2024-01-31 | 2024-10-30 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 57000 | GBP | 2024-01-31 | 2024-10-30 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 169977 | GBP | 2024-01-31 | 2025-10-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 858014 | GBP | 2024-01-31 | 2024-10-30 | filed | no | `core:Equity` | total-exemption-full |
| equity | 1087991 | GBP | 2024-01-31 | 2025-10-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 1087991 | GBP | 2024-01-31 | 2024-10-30 | filed | no | `core:Equity` | total-exemption-full |
| fixed_assets | 768715 | GBP | 2024-01-31 | 2025-10-22 | filed | yes | `core:FixedAssets` | total-exemption-full |
| fixed_assets | 768715 | GBP | 2024-01-31 | 2024-10-30 | filed | no | `core:FixedAssets` | total-exemption-full |
| net_assets | 1087991 | GBP | 2024-01-31 | 2025-10-22 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 1087991 | GBP | 2024-01-31 | 2024-10-30 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 319937 | GBP | 2024-01-31 | 2025-10-22 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 319937 | GBP | 2024-01-31 | 2024-10-30 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1088652 | GBP | 2024-01-31 | 2024-10-30 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1088652 | GBP | 2024-01-31 | 2025-10-22 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 3 | xbrli:pure | 2023-01-31 | 2024-10-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 3 | xbrli:pure | 2023-01-31 | 2023-06-22 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 274510 | GBP | 2023-01-31 | 2023-06-22 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 274510 | GBP | 2023-01-31 | 2024-10-30 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 65632 | GBP | 2023-01-31 | 2023-06-22 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 65632 | GBP | 2023-01-31 | 2024-10-30 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 375918 | GBP | 2023-01-31 | 2023-06-22 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 375918 | GBP | 2023-01-31 | 2024-10-30 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 101408 | GBP | 2023-01-31 | 2024-10-30 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 101408 | GBP | 2023-01-31 | 2023-06-22 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 101408 | GBP | 2023-01-31 | 2024-10-30 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 101408 | GBP | 2023-01-31 | 2023-06-22 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 3000 | GBP | 2023-01-31 | 2023-06-22 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 863157 | GBP | 2023-01-31 | 2024-10-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 1093134 | GBP | 2023-01-31 | 2023-06-22 | filed | no | `core:Equity` | total-exemption-full |
| equity | 1093134 | GBP | 2023-01-31 | 2024-10-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 57000 | GBP | 2023-01-31 | 2023-06-22 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 3000 | GBP | 2023-01-31 | 2024-10-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 57000 | GBP | 2023-01-31 | 2024-10-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 169977 | GBP | 2023-01-31 | 2023-06-22 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 169977 | GBP | 2023-01-31 | 2024-10-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 863157 | GBP | 2023-01-31 | 2023-06-22 | filed | no | `core:Equity` | total-exemption-full |
| fixed_assets | 784448 | GBP | 2023-01-31 | 2024-10-30 | filed | yes | `core:FixedAssets` | total-exemption-full |
| fixed_assets | 784448 | GBP | 2023-01-31 | 2023-06-22 | filed | no | `core:FixedAssets` | total-exemption-full |
| net_assets | 1093134 | GBP | 2023-01-31 | 2023-06-22 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 1093134 | GBP | 2023-01-31 | 2024-10-30 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 310286 | GBP | 2023-01-31 | 2024-10-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 310286 | GBP | 2023-01-31 | 2023-06-22 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1094734 | GBP | 2023-01-31 | 2023-06-22 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1094734 | GBP | 2023-01-31 | 2024-10-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 3 | xbrli:pure | 2022-01-31 | 2023-06-22 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 286989 | GBP | 2022-01-31 | 2023-06-22 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 27945 | GBP | 2022-01-31 | 2023-06-22 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 321787 | GBP | 2022-01-31 | 2023-06-22 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 34798 | GBP | 2022-01-31 | 2023-06-22 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 34798 | GBP | 2022-01-31 | 2023-06-22 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 57000 | GBP | 2022-01-31 | 2023-06-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 1091271 | GBP | 2022-01-31 | 2023-06-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 169977 | GBP | 2022-01-31 | 2023-06-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 3000 | GBP | 2022-01-31 | 2023-06-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 861294 | GBP | 2022-01-31 | 2023-06-22 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 799029 | GBP | 2022-01-31 | 2023-06-22 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | 1091271 | GBP | 2022-01-31 | 2023-06-22 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 293842 | GBP | 2022-01-31 | 2023-06-22 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1092871 | GBP | 2022-01-31 | 2023-06-22 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

Coverage @ 2025-01-31: 10/21 concepts available (average_employees, cash, creditors_within_one_year, current_assets, debtors, equity, fixed_assets, net_assets, net_current_assets, total_assets_less_current_liabilities)
- `creditors_after_one_year`: filed_without_concept — absent though regime 'total-exemption-full' typically includes it
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

- event restatement @ 2025-10-22: `{"superseded_document_id": "gb:01509617:doc:Ys2jdvPI9jktHKiBAdzRWMwNgXklJAaKoQgRXhXOAOc", "restatements": [{"concept": "average_employees", "period_end": "2024-01-31", "old_value": "3.0000", "new_valu`

## ARQIVA LIMITED (`gb:02487597`)

- registration: `02487597` (GB), status active, incorporated 1990-04-02
- classification: ['59113', '61900', '62090', '93290'] (sic_2007)
- records: 125 officers, 1 beneficial owners, 0 ownership statements, 25 security interests, 594 filings, 0 events, 3 source documents

_No figures persisted for this company._

Coverage @ 2025-06-30: 0/21 concepts available
- `average_employees`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `cash`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `creditors_after_one_year`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `creditors_within_one_year`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `current_assets`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `debtors`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `depreciation_amortisation`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `equity`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `fixed_assets`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `gross_profit`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `net_assets`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `net_current_assets`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `operating_profit`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `profit_before_tax`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `profit_for_period`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `retained_earnings`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `revenue`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `share_capital`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `staff_costs`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `tax_charge`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `total_assets_less_current_liabilities`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
