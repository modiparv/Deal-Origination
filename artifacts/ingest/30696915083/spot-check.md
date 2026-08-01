# Ingest spot-check

- database: `data/engine.db`
- latest run: `20260801T110308Z-60fdd6ad`
- companies in store: 200; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

Coverage @ 2024-12-31: 0/21 concepts available
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

## CLEVELAND SCIENTIFIC INSTITUTION (`gb:00191037`)

- registration: `00191037` (GB), status active, incorporated 1923-07-02
- classification: ['71129', '85600', '94120'] (sic_2007)
- records: 101 officers, 0 beneficial owners, 1 ownership statements, 2 security interests, 274 filings, 0 events, 3 source documents

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

## BSH PLANNING LIMITED (`gb:00498643`)

- registration: `00498643` (GB), status active, incorporated 1951-08-20
- classification: ['70229', '71112'] (sic_2007)
- records: 6 officers, 1 beneficial owners, 0 ownership statements, 5 security interests, 125 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | xbrli:pure | 2024-10-31 | 2025-07-09 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 156567 | GBP | 2024-10-31 | 2025-07-09 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 126333 | GBP | 2024-10-31 | 2025-07-09 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -30487 | GBP | 2024-10-31 | 2025-07-09 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 257 | GBP | 2024-10-31 | 2025-07-09 | filed | yes | `core:FixedAssets` | micro-entity |
| net_current_assets | -30234 | GBP | 2024-10-31 | 2025-07-09 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -29977 | GBP | 2024-10-31 | 2025-07-09 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2023-10-31 | 2024-07-08 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 142888 | GBP | 2023-10-31 | 2024-07-08 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 142888 | GBP | 2023-10-31 | 2025-07-09 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 106081 | GBP | 2023-10-31 | 2025-07-09 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 106081 | GBP | 2023-10-31 | 2024-07-08 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | -37015 | GBP | 2023-10-31 | 2025-07-09 | filed | yes | `core:Equity` | micro-entity |
| equity | -37015 | GBP | 2023-10-31 | 2024-07-08 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 302 | GBP | 2023-10-31 | 2025-07-09 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 302 | GBP | 2023-10-31 | 2024-07-08 | filed | no | `core:FixedAssets` | micro-entity |
| net_current_assets | -36807 | GBP | 2023-10-31 | 2025-07-09 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -36807 | GBP | 2023-10-31 | 2024-07-08 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -36505 | GBP | 2023-10-31 | 2025-07-09 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -36505 | GBP | 2023-10-31 | 2024-07-08 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 130113 | GBP | 2022-10-31 | 2024-07-08 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 88167 | GBP | 2022-10-31 | 2024-07-08 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -42077 | GBP | 2022-10-31 | 2024-07-08 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 355 | GBP | 2022-10-31 | 2024-07-08 | filed | yes | `core:FixedAssets` | micro-entity |
| net_current_assets `{'RestatementsFirstTimeAdoptionDimension': 'RestatedAmount'}` | -41946 | GBP | 2022-10-31 | 2024-07-08 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities `{'RestatementsFirstTimeAdoptionDimension': 'RestatedAmount'}` | -41591 | GBP | 2022-10-31 | 2024-07-08 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

Coverage @ 2025-10-29: 0/21 concepts available
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

## ARAL ESTATES LIMITED (`gb:00915706`)

- registration: `00915706` (GB), status active, incorporated 1967-09-19
- classification: ['71122'] (sic_2007)
- records: 5 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 109 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | iso4217:GBP | 2026-02-28 | 2026-06-19 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 990 | GBP | 2026-02-28 | 2026-06-19 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 482 | GBP | 2026-02-28 | 2026-06-19 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 508 | GBP | 2026-02-28 | 2026-06-19 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 508 | GBP | 2026-02-28 | 2026-06-19 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 508 | GBP | 2026-02-28 | 2026-06-19 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 508 | GBP | 2026-02-28 | 2026-06-19 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2025-02-28 | 2026-06-19 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2025-02-28 | 2025-07-21 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 8833 | GBP | 2025-02-28 | 2025-07-21 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 8833 | GBP | 2025-02-28 | 2026-06-19 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 8853 | GBP | 2025-02-28 | 2025-07-21 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 8853 | GBP | 2025-02-28 | 2026-06-19 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 20 | GBP | 2025-02-28 | 2025-07-21 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 20 | GBP | 2025-02-28 | 2026-06-19 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 20 | GBP | 2025-02-28 | 2026-06-19 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 20 | GBP | 2025-02-28 | 2025-07-21 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 20 | GBP | 2025-02-28 | 2025-07-21 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 20 | GBP | 2025-02-28 | 2026-06-19 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 20 | GBP | 2025-02-28 | 2026-06-19 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 20 | GBP | 2025-02-28 | 2025-07-21 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2024-02-28 | 2024-10-22 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2024-02-28 | 2025-07-21 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 14133 | GBP | 2024-02-28 | 2025-07-21 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 14133 | GBP | 2024-02-28 | 2024-10-22 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 14184 | GBP | 2024-02-28 | 2025-07-21 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 14184 | GBP | 2024-02-28 | 2024-10-22 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | 51 | GBP | 2024-02-28 | 2024-10-22 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 51 | GBP | 2024-02-28 | 2025-07-21 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2024-02-28 | 2024-10-22 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 51 | GBP | 2024-02-28 | 2025-07-21 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 51 | GBP | 2024-02-28 | 2024-10-22 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 51 | GBP | 2024-02-28 | 2025-07-21 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 51 | GBP | 2024-02-28 | 2024-10-22 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 51 | GBP | 2024-02-28 | 2025-07-21 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 51 | GBP | 2024-02-28 | 2024-10-22 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-02-28 | 2024-10-22 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 21847 | GBP | 2023-02-28 | 2024-10-22 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 34371 | GBP | 2023-02-28 | 2024-10-22 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 12524 | GBP | 2023-02-28 | 2024-10-22 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2023-02-28 | 2024-10-22 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 12524 | GBP | 2023-02-28 | 2024-10-22 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 12524 | GBP | 2023-02-28 | 2024-10-22 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 12524 | GBP | 2023-02-28 | 2024-10-22 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

Coverage @ 2026-02-28: 7/21 concepts available (average_employees, creditors_within_one_year, current_assets, equity, net_assets, net_current_assets, total_assets_less_current_liabilities)
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

## ANT INDUSTRIES LIMITED (`gb:01116596`)

- registration: `01116596` (GB), status active, incorporated 1973-06-05
- classification: ['71129'] (sic_2007)
- records: 3 officers, 1 beneficial owners, 0 ownership statements, 11 security interests, 120 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 60 | xbrli:pure | 2022-12-31 | 2023-11-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | full |
| cash | 281008 | GBP | 2022-12-31 | 2023-11-30 | filed | yes | `core:CashBankOnHand` | full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 898959 | GBP | 2022-12-31 | 2023-11-30 | filed | yes | `core:Creditors` | full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1309011 | GBP | 2022-12-31 | 2023-11-30 | filed | yes | `core:Creditors` | full |
| current_assets | 3989683 | GBP | 2022-12-31 | 2023-11-30 | filed | yes | `core:CurrentAssets` | full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1890501 | GBP | 2022-12-31 | 2023-11-30 | filed | yes | `core:Debtors` | full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 8662 | GBP | 2022-12-31 | 2023-11-30 | filed | yes | `core:Debtors` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3209659 | GBP | 2022-12-31 | 2023-11-30 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 396025 | GBP | 2022-12-31 | 2023-11-30 | filed | yes | `core:Equity` | full |
| equity | 3610684 | GBP | 2022-12-31 | 2023-11-30 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2750 | GBP | 2022-12-31 | 2023-11-30 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 2250 | GBP | 2022-12-31 | 2023-11-30 | filed | yes | `core:Equity` | full |
| fixed_assets | 1917812 | GBP | 2022-12-31 | 2023-11-30 | filed | yes | `core:FixedAssets` | full |
| gross_profit | 676616 | GBP | 2022-12-31 | 2023-11-30 | filed | yes | `core:GrossProfitLoss` | full |
| net_assets | 3610684 | GBP | 2022-12-31 | 2023-11-30 | filed | yes | `core:NetAssetsLiabilities` | full |
| net_current_assets | 2680672 | GBP | 2022-12-31 | 2023-11-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | full |
| operating_profit | 361085 | GBP | 2022-12-31 | 2023-11-30 | filed | yes | `core:OperatingProfitLoss` | full |
| profit_before_tax | 315981 | GBP | 2022-12-31 | 2023-11-30 | filed | yes | `core:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period | 430055 | GBP | 2022-12-31 | 2023-11-30 | filed | yes | `core:ProfitLoss` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 430055 | GBP | 2022-12-31 | 2023-11-30 | filed | yes | `core:ProfitLoss` | full |
| revenue `{'GeographicSegmentsDimension': 'RestWorldOutsideEurope'}` | 931660 | GBP | 2022-12-31 | 2023-11-30 | filed | yes | `core:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'Europe'}` | 2140479 | GBP | 2022-12-31 | 2023-11-30 | filed | yes | `core:TurnoverRevenue` | full |
| revenue | 6168002 | GBP | 2022-12-31 | 2023-11-30 | filed | yes | `core:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'UnitedKingdom'}` | 3095863 | GBP | 2022-12-31 | 2023-11-30 | filed | yes | `core:TurnoverRevenue` | full |
| staff_costs | 2469975 | GBP | 2022-12-31 | 2023-11-30 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | full |
| tax_charge | -114074 | GBP | 2022-12-31 | 2023-11-30 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| total_assets_less_current_liabilities | 4598484 | GBP | 2022-12-31 | 2023-11-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | full |
| average_employees | 70 | xbrli:pure | 2021-12-31 | 2023-11-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | full |
| cash | 750832 | GBP | 2021-12-31 | 2023-11-30 | filed | yes | `core:CashBankOnHand` | full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 1232080 | GBP | 2021-12-31 | 2023-11-30 | filed | yes | `core:Creditors` | full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1176955 | GBP | 2021-12-31 | 2023-11-30 | filed | yes | `core:Creditors` | full |
| current_assets | 4139888 | GBP | 2021-12-31 | 2023-11-30 | filed | yes | `core:CurrentAssets` | full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1435920 | GBP | 2021-12-31 | 2023-11-30 | filed | yes | `core:Debtors` | full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 2250 | GBP | 2021-12-31 | 2023-11-30 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 89610 | GBP | 2021-12-31 | 2023-11-30 | filed | yes | `core:Equity` | full |
| equity | 3381091 | GBP | 2021-12-31 | 2023-11-30 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3286481 | GBP | 2021-12-31 | 2023-11-30 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2750 | GBP | 2021-12-31 | 2023-11-30 | filed | yes | `core:Equity` | full |
| fixed_assets | 1714841 | GBP | 2021-12-31 | 2023-11-30 | filed | yes | `core:FixedAssets` | full |
| gross_profit | 320990 | GBP | 2021-12-31 | 2023-11-30 | filed | yes | `core:GrossProfitLoss` | full |
| net_assets | 3381091 | GBP | 2021-12-31 | 2023-11-30 | filed | yes | `core:NetAssetsLiabilities` | full |
| net_current_assets | 2962933 | GBP | 2021-12-31 | 2023-11-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | full |
| operating_profit | -265066 | GBP | 2021-12-31 | 2023-11-30 | filed | yes | `core:OperatingProfitLoss` | full |
| profit_before_tax | -314716 | GBP | 2021-12-31 | 2023-11-30 | filed | yes | `core:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period | -19102 | GBP | 2021-12-31 | 2023-11-30 | filed | yes | `core:ProfitLoss` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -19102 | GBP | 2021-12-31 | 2023-11-30 | filed | yes | `core:ProfitLoss` | full |
| revenue `{'GeographicSegmentsDimension': 'UnitedKingdom'}` | 4067701 | GBP | 2021-12-31 | 2023-11-30 | filed | yes | `core:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'Europe'}` | 2995344 | GBP | 2021-12-31 | 2023-11-30 | filed | yes | `core:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'RestWorldOutsideEurope'}` | 838711 | GBP | 2021-12-31 | 2023-11-30 | filed | yes | `core:TurnoverRevenue` | full |
| revenue | 7901756 | GBP | 2021-12-31 | 2023-11-30 | filed | yes | `core:TurnoverRevenue` | full |
| staff_costs | 3637720 | GBP | 2021-12-31 | 2023-11-30 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | full |
| tax_charge | -295614 | GBP | 2021-12-31 | 2023-11-30 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| total_assets_less_current_liabilities | 4677774 | GBP | 2021-12-31 | 2023-11-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | full |
| equity | 3777102 | GBP | 2020-12-31 | 2023-11-30 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 100144 | GBP | 2020-12-31 | 2023-11-30 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3671958 | GBP | 2020-12-31 | 2023-11-30 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 2250 | GBP | 2020-12-31 | 2023-11-30 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2750 | GBP | 2020-12-31 | 2023-11-30 | filed | yes | `core:Equity` | full |

Coverage @ 2024-12-31: 0/21 concepts available
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

## CULTURA TECHNOLOGIES LTD (`gb:01250877`)

- registration: `01250877` (GB), status active, incorporated 1976-03-24
- classification: ['62012'] (sic_2007)
- records: 20 officers, 2 beneficial owners, 0 ownership statements, 7 security interests, 169 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.39 | xbrli:pure | 2024-12-31 | 2025-09-16 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 50370 | GBP | 2024-12-31 | 2025-09-16 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 195771 | GBP | 2024-12-31 | 2025-09-16 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 2618 | GBP | 2024-12-31 | 2025-09-16 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1205334 | GBP | 2024-12-31 | 2025-09-16 | filed | yes | `core:Equity` | full |
| equity | 1454843 | GBP | 2024-12-31 | 2025-09-16 | filed | yes | `core:Equity` | full |
| profit_before_tax | 1328073 | GBP | 2024-12-31 | 2025-09-16 | filed | yes | `core:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1199570 | GBP | 2024-12-31 | 2025-09-16 | filed | yes | `core:ProfitLoss` | full |
| revenue | 6497611 | GBP | 2024-12-31 | 2025-09-16 | filed | yes | `core:TurnoverRevenue` | full |
| staff_costs | 2262300 | GBP | 2024-12-31 | 2025-09-16 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | full |
| tax_charge | 128503 | GBP | 2024-12-31 | 2025-09-16 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| average_employees | 0.42 | xbrli:pure | 2023-12-31 | 2025-09-16 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | full |
| average_employees | 42 | xbrli:pure | 2023-12-31 | 2024-08-05 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 2618 | GBP | 2023-12-31 | 2025-09-16 | filed | yes | `core:Equity` | full |
| equity | 1255273 | GBP | 2023-12-31 | 2024-08-05 | filed | no | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 195771 | GBP | 2023-12-31 | 2025-09-16 | filed | yes | `core:Equity` | full |
| equity | 1255273 | GBP | 2023-12-31 | 2025-09-16 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 2618 | GBP | 2023-12-31 | 2024-08-05 | filed | no | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1005764 | GBP | 2023-12-31 | 2025-09-16 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 195771 | GBP | 2023-12-31 | 2024-08-05 | filed | no | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 50370 | GBP | 2023-12-31 | 2024-08-05 | filed | no | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1005764 | GBP | 2023-12-31 | 2024-08-05 | filed | no | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 50370 | GBP | 2023-12-31 | 2025-09-16 | filed | yes | `core:Equity` | full |
| gross_profit `{'ContinuingDiscontinuedOperationsDimension': 'ContinuingOperations'}` | 1529408 | GBP | 2023-12-31 | 2024-08-05 | filed | yes | `core:GrossProfitLoss` | full |
| operating_profit `{'ContinuingDiscontinuedOperationsDimension': 'ContinuingOperations'}` | 888479 | GBP | 2023-12-31 | 2024-08-05 | filed | yes | `core:OperatingProfitLoss` | full |
| profit_before_tax | 887778 | GBP | 2023-12-31 | 2025-09-16 | filed | yes | `core:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_before_tax | 887778 | GBP | 2023-12-31 | 2024-08-05 | filed | no | `core:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 754893 | GBP | 2023-12-31 | 2025-09-16 | filed | yes | `core:ProfitLoss` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 754893 | GBP | 2023-12-31 | 2024-08-05 | filed | no | `core:ProfitLoss` | full |
| revenue | 6118516 | GBP | 2023-12-31 | 2025-09-16 | filed | yes | `core:TurnoverRevenue` | full |
| revenue | 6118516 | GBP | 2023-12-31 | 2024-08-05 | filed | no | `core:TurnoverRevenue` | full |
| staff_costs | 2151832 | GBP | 2023-12-31 | 2024-08-05 | filed | no | `core:StaffCostsEmployeeBenefitsExpense` | full |
| staff_costs | 2151832 | GBP | 2023-12-31 | 2025-09-16 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | full |
| tax_charge | 132885 | GBP | 2023-12-31 | 2025-09-16 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| tax_charge | 132885 | GBP | 2023-12-31 | 2024-08-05 | filed | no | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| average_employees | 44 | xbrli:pure | 2022-12-31 | 2024-08-05 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | full |
| average_employees | 44 | xbrli:pure | 2022-12-31 | 2023-08-04 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 195771 | GBP | 2022-12-31 | 2025-09-16 | filed | yes | `core:Equity` | full |
| equity | 1500380 | GBP | 2022-12-31 | 2023-08-04 | filed | no | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 50370 | GBP | 2022-12-31 | 2024-08-05 | filed | yes | `core:Equity` | full |
| equity | 1250871 | GBP | 2022-12-31 | 2025-09-16 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 2618 | GBP | 2022-12-31 | 2023-08-04 | filed | no | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 195771 | GBP | 2022-12-31 | 2023-08-04 | filed | no | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1250871 | GBP | 2022-12-31 | 2024-08-05 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 195771 | GBP | 2022-12-31 | 2024-08-05 | filed | no | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 2618 | GBP | 2022-12-31 | 2024-08-05 | filed | no | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1250871 | GBP | 2022-12-31 | 2023-08-04 | filed | no | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 50370 | GBP | 2022-12-31 | 2023-08-04 | filed | no | `core:Equity` | full |
| equity | 1500380 | GBP | 2022-12-31 | 2024-08-05 | filed | no | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 2618 | GBP | 2022-12-31 | 2025-09-16 | filed | yes | `core:Equity` | full |
| gross_profit | 1368291 | GBP | 2022-12-31 | 2024-08-05 | filed | yes | `core:GrossProfitLoss` | full |
| gross_profit `{'ContinuingDiscontinuedOperationsDimension': 'ContinuingOperations'}` | 1368291 | GBP | 2022-12-31 | 2023-08-04 | filed | yes | `core:GrossProfitLoss` | full |
| operating_profit | 803249 | GBP | 2022-12-31 | 2024-08-05 | filed | yes | `core:OperatingProfitLoss` | full |
| operating_profit `{'ContinuingDiscontinuedOperationsDimension': 'ContinuingOperations'}` | 803249 | GBP | 2022-12-31 | 2023-08-04 | filed | yes | `core:OperatingProfitLoss` | full |
| profit_before_tax | 801572 | GBP | 2022-12-31 | 2023-08-04 | filed | no | `core:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_before_tax | 801572 | GBP | 2022-12-31 | 2024-08-05 | filed | yes | `core:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 804820 | GBP | 2022-12-31 | 2024-08-05 | filed | yes | `core:ProfitLoss` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 804820 | GBP | 2022-12-31 | 2023-08-04 | filed | no | `core:ProfitLoss` | full |
| revenue | 5840922 | GBP | 2022-12-31 | 2023-08-04 | filed | no | `core:TurnoverRevenue` | full |
| revenue | 5840922 | GBP | 2022-12-31 | 2024-08-05 | filed | yes | `core:TurnoverRevenue` | full |
| staff_costs | 2355849 | GBP | 2022-12-31 | 2024-08-05 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | full |
| staff_costs | 2355849 | GBP | 2022-12-31 | 2023-08-04 | filed | no | `core:StaffCostsEmployeeBenefitsExpense` | full |
| tax_charge | -3248 | GBP | 2022-12-31 | 2023-08-04 | filed | no | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| tax_charge | -3248 | GBP | 2022-12-31 | 2024-08-05 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| average_employees | 48 | xbrli:pure | 2021-12-31 | 2023-08-04 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 50370 | GBP | 2021-12-31 | 2023-08-04 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 2618 | GBP | 2021-12-31 | 2023-08-04 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1446051 | GBP | 2021-12-31 | 2023-08-04 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 195771 | GBP | 2021-12-31 | 2023-08-04 | filed | yes | `core:Equity` | full |
| equity | 1695560 | GBP | 2021-12-31 | 2023-08-04 | filed | yes | `core:Equity` | full |
| gross_profit | 1726813 | GBP | 2021-12-31 | 2023-08-04 | filed | yes | `core:GrossProfitLoss` | full |
| operating_profit | 1267069 | GBP | 2021-12-31 | 2023-08-04 | filed | yes | `core:OperatingProfitLoss` | full |
| profit_before_tax | 1264196 | GBP | 2021-12-31 | 2023-08-04 | filed | yes | `core:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1230296 | GBP | 2021-12-31 | 2023-08-04 | filed | yes | `core:ProfitLoss` | full |
| revenue | 6367826 | GBP | 2021-12-31 | 2023-08-04 | filed | yes | `core:TurnoverRevenue` | full |
| staff_costs | 2777327 | GBP | 2021-12-31 | 2023-08-04 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | full |
| tax_charge | 33900 | GBP | 2021-12-31 | 2023-08-04 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 195771 | GBP | 2020-12-31 | 2023-08-04 | filed | yes | `core:Equity` | full |
| equity | 1515755 | GBP | 2020-12-31 | 2023-08-04 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 2618 | GBP | 2020-12-31 | 2023-08-04 | filed | yes | `core:Equity` | full |

Coverage @ 2024-12-31: 7/21 concepts available (average_employees, equity, profit_before_tax, profit_for_period, revenue, staff_costs, tax_charge)
- `cash`: filed_without_concept — absent though regime 'full' typically includes it
- `creditors_after_one_year`: filed_without_concept — absent though regime 'full' typically includes it
- `creditors_within_one_year`: filed_without_concept — absent though regime 'full' typically includes it
- `current_assets`: filed_without_concept — absent though regime 'full' typically includes it
- `debtors`: filed_without_concept — absent though regime 'full' typically includes it
- `depreciation_amortisation`: filed_without_concept — absent though regime 'full' typically includes it
- `fixed_assets`: filed_without_concept — absent though regime 'full' typically includes it
- `gross_profit`: filed_without_concept — absent though regime 'full' typically includes it
- `net_assets`: filed_without_concept — absent though regime 'full' typically includes it
- `net_current_assets`: filed_without_concept — absent though regime 'full' typically includes it
- `operating_profit`: filed_without_concept — absent though regime 'full' typically includes it
- `retained_earnings`: filed_without_concept — absent though regime 'full' typically includes it
- `share_capital`: filed_without_concept — absent though regime 'full' typically includes it
- `total_assets_less_current_liabilities`: filed_without_concept — absent though regime 'full' typically includes it

- event restatement @ 2025-09-16: `{"superseded_document_id": "gb:01250877:doc:IFhgYf0aHHVLiyXVR1ICRbfy_zO18NvWANjOa95xFz4", "restatements": [{"concept": "equity", "period_end": "2022-12-31", "old_value": "1500380.0000", "new_value": "`

## TASCOMP LIMITED (`gb:01356854`)

- registration: `01356854` (GB), status active, incorporated 1978-03-10
- classification: ['47410', '62012'] (sic_2007)
- records: 8 officers, 1 beneficial owners, 0 ownership statements, 6 security interests, 119 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 20 | xbrli:pure | 2025-12-31 | 2026-05-28 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 371069 | GBP | 2025-12-31 | 2026-05-28 | filed | yes | `ns5:CashBankOnHand` | unaudited-abridged |
| current_assets | 1445661 | GBP | 2025-12-31 | 2026-05-28 | filed | yes | `ns5:CurrentAssets` | unaudited-abridged |
| debtors | 1055196 | GBP | 2025-12-31 | 2026-05-28 | filed | yes | `ns5:Debtors` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 905499 | GBP | 2025-12-31 | 2026-05-28 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 17957 | GBP | 2025-12-31 | 2026-05-28 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 952 | GBP | 2025-12-31 | 2026-05-28 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity | 933457 | GBP | 2025-12-31 | 2026-05-28 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 9049 | GBP | 2025-12-31 | 2026-05-28 | filed | yes | `ns5:Equity` | unaudited-abridged |
| net_assets | 933457 | GBP | 2025-12-31 | 2026-05-28 | filed | yes | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 794213 | GBP | 2025-12-31 | 2026-05-28 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 935044 | GBP | 2025-12-31 | 2026-05-28 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 21 | xbrli:pure | 2024-12-31 | 2026-05-28 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| average_employees | 21 | xbrli:pure | 2024-12-31 | 2025-07-31 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 242934 | GBP | 2024-12-31 | 2025-07-31 | filed | no | `ns5:CashBankOnHand` | unaudited-abridged |
| cash | 242934 | GBP | 2024-12-31 | 2026-05-28 | filed | yes | `ns5:CashBankOnHand` | unaudited-abridged |
| current_assets | 1019791 | GBP | 2024-12-31 | 2026-05-28 | filed | yes | `ns5:CurrentAssets` | unaudited-abridged |
| current_assets | 1019791 | GBP | 2024-12-31 | 2025-07-31 | filed | no | `ns5:CurrentAssets` | unaudited-abridged |
| debtors | 772559 | GBP | 2024-12-31 | 2025-07-31 | filed | no | `ns5:Debtors` | unaudited-abridged |
| debtors | 772559 | GBP | 2024-12-31 | 2026-05-28 | filed | yes | `ns5:Debtors` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 18522 | GBP | 2024-12-31 | 2026-05-28 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity | 704585 | GBP | 2024-12-31 | 2025-07-31 | filed | no | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 952 | GBP | 2024-12-31 | 2026-05-28 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity | 704585 | GBP | 2024-12-31 | 2026-05-28 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 676062 | GBP | 2024-12-31 | 2025-07-31 | filed | no | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 9049 | GBP | 2024-12-31 | 2025-07-31 | filed | no | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 952 | GBP | 2024-12-31 | 2025-07-31 | filed | no | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 676062 | GBP | 2024-12-31 | 2026-05-28 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 18522 | GBP | 2024-12-31 | 2025-07-31 | filed | no | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 9049 | GBP | 2024-12-31 | 2026-05-28 | filed | yes | `ns5:Equity` | unaudited-abridged |
| net_assets | 704585 | GBP | 2024-12-31 | 2026-05-28 | filed | yes | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_assets | 704585 | GBP | 2024-12-31 | 2025-07-31 | filed | no | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 549489 | GBP | 2024-12-31 | 2025-07-31 | filed | no | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 549489 | GBP | 2024-12-31 | 2026-05-28 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 708474 | GBP | 2024-12-31 | 2026-05-28 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 708474 | GBP | 2024-12-31 | 2025-07-31 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 20 | xbrli:pure | 2023-12-31 | 2024-09-26 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| average_employees | 20 | xbrli:pure | 2023-12-31 | 2025-07-31 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 343328 | GBP | 2023-12-31 | 2024-09-26 | filed | no | `ns5:CashBankOnHand` | unaudited-abridged |
| cash | 343328 | GBP | 2023-12-31 | 2025-07-31 | filed | yes | `ns5:CashBankOnHand` | unaudited-abridged |
| current_assets | 973716 | GBP | 2023-12-31 | 2025-07-31 | filed | yes | `ns5:CurrentAssets` | unaudited-abridged |
| current_assets | 973716 | GBP | 2023-12-31 | 2024-09-26 | filed | no | `ns5:CurrentAssets` | unaudited-abridged |
| debtors | 607032 | GBP | 2023-12-31 | 2024-09-26 | filed | no | `ns5:Debtors` | unaudited-abridged |
| debtors | 607032 | GBP | 2023-12-31 | 2025-07-31 | filed | yes | `ns5:Debtors` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 952 | GBP | 2023-12-31 | 2025-07-31 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 521100 | GBP | 2023-12-31 | 2025-07-31 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 952 | GBP | 2023-12-31 | 2024-09-26 | filed | no | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 9049 | GBP | 2023-12-31 | 2024-09-26 | filed | no | `ns5:Equity` | unaudited-abridged |
| equity | 550188 | GBP | 2023-12-31 | 2025-07-31 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 19087 | GBP | 2023-12-31 | 2025-07-31 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 521100 | GBP | 2023-12-31 | 2024-09-26 | filed | no | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 19087 | GBP | 2023-12-31 | 2024-09-26 | filed | no | `ns5:Equity` | unaudited-abridged |
| equity | 550188 | GBP | 2023-12-31 | 2024-09-26 | filed | no | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 9049 | GBP | 2023-12-31 | 2025-07-31 | filed | yes | `ns5:Equity` | unaudited-abridged |
| net_assets | 550188 | GBP | 2023-12-31 | 2025-07-31 | filed | yes | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_assets | 550188 | GBP | 2023-12-31 | 2024-09-26 | filed | no | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 417531 | GBP | 2023-12-31 | 2025-07-31 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 417531 | GBP | 2023-12-31 | 2024-09-26 | filed | no | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 552459 | GBP | 2023-12-31 | 2025-07-31 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 552459 | GBP | 2023-12-31 | 2024-09-26 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 19 | xbrli:pure | 2022-12-31 | 2024-09-26 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 311987 | GBP | 2022-12-31 | 2024-09-26 | filed | yes | `ns5:CashBankOnHand` | unaudited-abridged |
| current_assets | 1020419 | GBP | 2022-12-31 | 2024-09-26 | filed | yes | `ns5:CurrentAssets` | unaudited-abridged |
| debtors | 701089 | GBP | 2022-12-31 | 2024-09-26 | filed | yes | `ns5:Debtors` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 952 | GBP | 2022-12-31 | 2024-09-26 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity | 448634 | GBP | 2022-12-31 | 2024-09-26 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 418981 | GBP | 2022-12-31 | 2024-09-26 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 19652 | GBP | 2022-12-31 | 2024-09-26 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 9049 | GBP | 2022-12-31 | 2024-09-26 | filed | yes | `ns5:Equity` | unaudited-abridged |
| net_assets | 448634 | GBP | 2022-12-31 | 2024-09-26 | filed | yes | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 322429 | GBP | 2022-12-31 | 2024-09-26 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 448634 | GBP | 2022-12-31 | 2024-09-26 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |

Coverage @ 2025-12-31: 8/21 concepts available (average_employees, cash, current_assets, debtors, equity, net_assets, net_current_assets, total_assets_less_current_liabilities)
- `creditors_after_one_year`: filed_without_concept — absent though regime 'unaudited-abridged' typically includes it
- `creditors_within_one_year`: filed_without_concept — absent though regime 'unaudited-abridged' typically includes it
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

## CIGOL CONTROLS LIMITED (`gb:01404834`)

- registration: `01404834` (GB), status active, incorporated 1978-12-12
- classification: ['26512', '62012'] (sic_2007)
- records: 3 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 95 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-03-31 | 2025-11-03 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 7182 | GBP | 2025-03-31 | 2025-11-03 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 29486 | GBP | 2025-03-31 | 2025-11-03 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 23647 | GBP | 2025-03-31 | 2025-11-03 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 2500 | GBP | 2025-03-31 | 2025-11-03 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 23647 | GBP | 2025-03-31 | 2025-11-03 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 22497 | GBP | 2025-03-31 | 2025-11-03 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 24997 | GBP | 2025-03-31 | 2025-11-03 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-03-31 | 2025-11-03 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-03-31 | 2024-08-29 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 7591 | GBP | 2024-03-31 | 2024-08-29 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 7591 | GBP | 2024-03-31 | 2025-11-03 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 28358 | GBP | 2024-03-31 | 2024-08-29 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 28358 | GBP | 2024-03-31 | 2025-11-03 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 22685 | GBP | 2024-03-31 | 2024-08-29 | filed | no | `core:Equity` | micro-entity |
| equity | 22685 | GBP | 2024-03-31 | 2025-11-03 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 3000 | GBP | 2024-03-31 | 2024-08-29 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 3000 | GBP | 2024-03-31 | 2025-11-03 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 22685 | GBP | 2024-03-31 | 2024-08-29 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 22685 | GBP | 2024-03-31 | 2025-11-03 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 21000 | GBP | 2024-03-31 | 2025-11-03 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 21000 | GBP | 2024-03-31 | 2024-08-29 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 24000 | GBP | 2024-03-31 | 2024-08-29 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 24000 | GBP | 2024-03-31 | 2025-11-03 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-03-31 | 2023-08-21 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-03-31 | 2024-08-29 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 13609 | GBP | 2023-03-31 | 2024-08-29 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 13609 | GBP | 2023-03-31 | 2023-08-21 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 44618 | GBP | 2023-03-31 | 2024-08-29 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 44618 | GBP | 2023-03-31 | 2023-08-21 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 32972 | GBP | 2023-03-31 | 2024-08-29 | filed | yes | `core:Equity` | micro-entity |
| equity | 32972 | GBP | 2023-03-31 | 2023-08-21 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 3000 | GBP | 2023-03-31 | 2023-08-21 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 3000 | GBP | 2023-03-31 | 2024-08-29 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 32972 | GBP | 2023-03-31 | 2023-08-21 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 32972 | GBP | 2023-03-31 | 2024-08-29 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 31247 | GBP | 2023-03-31 | 2023-08-21 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 31247 | GBP | 2023-03-31 | 2024-08-29 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 34247 | GBP | 2023-03-31 | 2024-08-29 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 34247 | GBP | 2023-03-31 | 2023-08-21 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2022-03-31 | 2023-08-21 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 26310 | GBP | 2022-03-31 | 2023-08-21 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 63468 | GBP | 2022-03-31 | 2023-08-21 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 42576 | GBP | 2022-03-31 | 2023-08-21 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 6690 | GBP | 2022-03-31 | 2023-08-21 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 42576 | GBP | 2022-03-31 | 2023-08-21 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 37438 | GBP | 2022-03-31 | 2023-08-21 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 44128 | GBP | 2022-03-31 | 2023-08-21 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

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

## MAVERIDE LIMITED (`gb:01437958`)

- registration: `01437958` (GB), status active, incorporated 1979-07-18
- classification: ['71129'] (sic_2007)
- records: 5 officers, 1 beneficial owners, 1 ownership statements, 0 security interests, 94 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | xbrli:pure | 2022-09-30 | 2023-09-21 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 11595 | GBP | 2022-09-30 | 2023-09-21 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 29903 | GBP | 2022-09-30 | 2023-09-21 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 16558 | GBP | 2022-09-30 | 2023-09-21 | filed | yes | `core:Equity` | micro-entity |
| net_current_assets | 18308 | GBP | 2022-09-30 | 2023-09-21 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 18308 | GBP | 2022-09-30 | 2023-09-21 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 8855 | GBP | 2021-09-30 | 2023-09-21 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 49687 | GBP | 2021-09-30 | 2023-09-21 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 37832 | GBP | 2021-09-30 | 2023-09-21 | filed | yes | `core:Equity` | micro-entity |
| net_current_assets | 40832 | GBP | 2021-09-30 | 2023-09-21 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 40832 | GBP | 2021-09-30 | 2023-09-21 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

Coverage @ 2023-09-29: 0/21 concepts available
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

## RAPID COMPUTERS LIMITED (`gb:01524516`)

- registration: `01524516` (GB), status active, incorporated 1980-10-27
- classification: ['61200', '61900', '62020', '62090'] (sic_2007)
- records: 2 officers, 3 beneficial owners, 0 ownership statements, 3 security interests, 99 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 17 | xbrli:pure | 2024-12-31 | 2025-08-28 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 342787 | GBP | 2024-12-31 | 2025-08-28 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 1451896 | GBP | 2024-12-31 | 2025-08-28 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 910107 | GBP | 2024-12-31 | 2025-08-28 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 910107 | GBP | 2024-12-31 | 2025-08-28 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 221385 | GBP | 2024-12-31 | 2025-08-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 476385 | GBP | 2024-12-31 | 2025-08-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 255000 | GBP | 2024-12-31 | 2025-08-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 476385 | GBP | 2024-12-31 | 2025-08-28 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 462916 | GBP | 2024-12-31 | 2025-08-28 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 534674 | GBP | 2024-12-31 | 2025-08-28 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 17 | xbrli:pure | 2023-12-31 | 2025-08-28 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 17 | xbrli:pure | 2023-12-31 | 2024-08-19 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 71212 | GBP | 2023-12-31 | 2024-08-19 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 71212 | GBP | 2023-12-31 | 2025-08-28 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 1403588 | GBP | 2023-12-31 | 2025-08-28 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 1403588 | GBP | 2023-12-31 | 2024-08-19 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 940000 | GBP | 2023-12-31 | 2024-08-19 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 940000 | GBP | 2023-12-31 | 2025-08-28 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 940000 | GBP | 2023-12-31 | 2024-08-19 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 940000 | GBP | 2023-12-31 | 2025-08-28 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 404464 | GBP | 2023-12-31 | 2024-08-19 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 404464 | GBP | 2023-12-31 | 2025-08-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 255000 | GBP | 2023-12-31 | 2025-08-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 149464 | GBP | 2023-12-31 | 2025-08-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 149464 | GBP | 2023-12-31 | 2024-08-19 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 255000 | GBP | 2023-12-31 | 2024-08-19 | filed | no | `ns5:Equity` | total-exemption-full |
| net_assets | 404464 | GBP | 2023-12-31 | 2025-08-28 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 404464 | GBP | 2023-12-31 | 2024-08-19 | filed | no | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 394790 | GBP | 2023-12-31 | 2025-08-28 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 394790 | GBP | 2023-12-31 | 2024-08-19 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 490467 | GBP | 2023-12-31 | 2025-08-28 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 490467 | GBP | 2023-12-31 | 2024-08-19 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 17 | xbrli:pure | 2022-12-31 | 2024-08-19 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 17 | xbrli:pure | 2022-12-31 | 2023-07-25 | filed | no | `ns6:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 303331 | GBP | 2022-12-31 | 2023-07-25 | filed | no | `ns6:CashBankOnHand` | total-exemption-full |
| cash | 303331 | GBP | 2022-12-31 | 2024-08-19 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 1560340 | GBP | 2022-12-31 | 2023-07-25 | filed | no | `ns6:CurrentAssets` | total-exemption-full |
| current_assets | 1560340 | GBP | 2022-12-31 | 2024-08-19 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 820879 | GBP | 2022-12-31 | 2024-08-19 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 820879 | GBP | 2022-12-31 | 2024-08-19 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 820879 | GBP | 2022-12-31 | 2023-07-25 | filed | no | `ns6:Debtors` | total-exemption-full |
| debtors | 820879 | GBP | 2022-12-31 | 2023-07-25 | filed | no | `ns6:Debtors` | total-exemption-full |
| equity | 332934 | GBP | 2022-12-31 | 2023-07-25 | filed | no | `ns6:Equity` | total-exemption-full |
| equity | 332934 | GBP | 2022-12-31 | 2024-08-19 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 77934 | GBP | 2022-12-31 | 2023-07-25 | filed | no | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 255000 | GBP | 2022-12-31 | 2024-08-19 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 77934 | GBP | 2022-12-31 | 2024-08-19 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 255000 | GBP | 2022-12-31 | 2023-07-25 | filed | no | `ns6:Equity` | total-exemption-full |
| net_assets | 332934 | GBP | 2022-12-31 | 2023-07-25 | filed | no | `ns6:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 332934 | GBP | 2022-12-31 | 2024-08-19 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 457723 | GBP | 2022-12-31 | 2024-08-19 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 457723 | GBP | 2022-12-31 | 2023-07-25 | filed | no | `ns6:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 501512 | GBP | 2022-12-31 | 2023-07-25 | filed | no | `ns6:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 501512 | GBP | 2022-12-31 | 2024-08-19 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 18 | xbrli:pure | 2021-12-31 | 2023-07-25 | filed | yes | `ns6:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 269742 | GBP | 2021-12-31 | 2023-07-25 | filed | yes | `ns6:CashBankOnHand` | total-exemption-full |
| current_assets | 1749229 | GBP | 2021-12-31 | 2023-07-25 | filed | yes | `ns6:CurrentAssets` | total-exemption-full |
| debtors | 1040813 | GBP | 2021-12-31 | 2023-07-25 | filed | yes | `ns6:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 1040813 | GBP | 2021-12-31 | 2023-07-25 | filed | yes | `ns6:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 95006 | GBP | 2021-12-31 | 2023-07-25 | filed | yes | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 255000 | GBP | 2021-12-31 | 2023-07-25 | filed | yes | `ns6:Equity` | total-exemption-full |
| equity | 350006 | GBP | 2021-12-31 | 2023-07-25 | filed | yes | `ns6:Equity` | total-exemption-full |
| net_assets | 350006 | GBP | 2021-12-31 | 2023-07-25 | filed | yes | `ns6:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 586985 | GBP | 2021-12-31 | 2023-07-25 | filed | yes | `ns6:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 637103 | GBP | 2021-12-31 | 2023-07-25 | filed | yes | `ns6:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

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
