# Ingest spot-check

- database: `data/engine.db`
- latest run: `20261110T092303Z-8f911cce`
- companies in store: 48200; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## I.T. CONTRACT MANAGEMENT LIMITED (`gb:02739000`)

- registration: `02739000` (GB), status active, incorporated 1992-08-12
- classification: ['62020'] (sic_2007)
- records: 9 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 99 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | iso4217:GBP | 2025-08-31 | 2026-08-27 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2025-08-31 | 2026-08-27 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 35894 | GBP | 2025-08-31 | 2026-08-27 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 249847 | GBP | 2025-08-31 | 2026-08-27 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 213455 | GBP | 2025-08-31 | 2026-08-27 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 2 | GBP | 2025-08-31 | 2026-08-27 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 213455 | GBP | 2025-08-31 | 2026-08-27 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 213953 | GBP | 2025-08-31 | 2026-08-27 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 213955 | GBP | 2025-08-31 | 2026-08-27 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-08-31 | 2025-05-22 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-08-31 | 2026-08-27 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2024-08-31 | 2026-08-27 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 67675 | GBP | 2024-08-31 | 2025-05-22 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 66415 | GBP | 2024-08-31 | 2026-08-27 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 282824 | GBP | 2024-08-31 | 2026-08-27 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 282824 | GBP | 2024-08-31 | 2025-05-22 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | 215151 | GBP | 2024-08-31 | 2025-05-22 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 215151 | GBP | 2024-08-31 | 2026-08-27 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 2 | GBP | 2024-08-31 | 2025-05-22 | filed | no | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 2 | GBP | 2024-08-31 | 2026-08-27 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 215151 | GBP | 2024-08-31 | 2026-08-27 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 215151 | GBP | 2024-08-31 | 2025-05-22 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 215149 | GBP | 2024-08-31 | 2025-05-22 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 216409 | GBP | 2024-08-31 | 2026-08-27 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 215151 | GBP | 2024-08-31 | 2025-05-22 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 216411 | GBP | 2024-08-31 | 2026-08-27 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-08-31 | 2025-05-22 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-08-31 | 2024-09-23 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 29532 | GBP | 2023-08-31 | 2025-05-22 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 29532 | GBP | 2023-08-31 | 2024-09-23 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 247348 | GBP | 2023-08-31 | 2025-05-22 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 247348 | GBP | 2023-08-31 | 2024-09-23 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | 217818 | GBP | 2023-08-31 | 2024-09-23 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 217818 | GBP | 2023-08-31 | 2025-05-22 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 2 | GBP | 2023-08-31 | 2024-09-23 | filed | no | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 2 | GBP | 2023-08-31 | 2025-05-22 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 217818 | GBP | 2023-08-31 | 2025-05-22 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 217818 | GBP | 2023-08-31 | 2024-09-23 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 217816 | GBP | 2023-08-31 | 2025-05-22 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 217816 | GBP | 2023-08-31 | 2024-09-23 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 217818 | GBP | 2023-08-31 | 2025-05-22 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 217818 | GBP | 2023-08-31 | 2024-09-23 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2022-08-31 | 2024-09-23 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 56998 | GBP | 2022-08-31 | 2024-09-23 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 257875 | GBP | 2022-08-31 | 2024-09-23 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 200919 | GBP | 2022-08-31 | 2024-09-23 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 42 | GBP | 2022-08-31 | 2024-09-23 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 200919 | GBP | 2022-08-31 | 2024-09-23 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 200877 | GBP | 2022-08-31 | 2024-09-23 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 200919 | GBP | 2022-08-31 | 2024-09-23 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2026-08-27: `{"superseded_document_id": "gb:02739000:doc:6ADfDgTtD1lf_WBzIoSCY04C1xd9EWxdVivgDJWH_SY", "restatements": [{"concept": "creditors_within_one_year", "period_end": "2024-08-31", "old_value": "67675.0000`

## LEARN EASY LIMITED (`gb:03413403`)

- registration: `03413403` (GB), status active, incorporated 1997-08-01
- classification: ['62020'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 68 filings, 2 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | iso4217:GBP | 2025-06-30 | 2026-02-16 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 158476 | GBP | 2025-06-30 | 2026-02-16 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 322 | GBP | 2025-06-30 | 2026-02-16 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 122 | GBP | 2025-06-30 | 2026-02-16 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 158676 | GBP | 2025-06-30 | 2026-02-16 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 158676 | GBP | 2025-06-30 | 2026-02-16 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 200 | GBP | 2025-06-30 | 2026-02-16 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 200 | GBP | 2025-06-30 | 2026-02-16 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2024-06-30 | 2026-02-16 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2024-06-30 | 2024-12-02 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 1548476 | GBP | 2024-06-30 | 2024-12-02 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 158476 | GBP | 2024-06-30 | 2026-02-16 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 322 | GBP | 2024-06-30 | 2026-02-16 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 322 | GBP | 2024-06-30 | 2024-12-02 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 122 | GBP | 2024-06-30 | 2024-12-02 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 122 | GBP | 2024-06-30 | 2026-02-16 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 158676 | GBP | 2024-06-30 | 2026-02-16 | filed | yes | `uk-core:Equity` | micro-entity |
| equity | 1548676 | GBP | 2024-06-30 | 2024-12-02 | filed | no | `uk-core:Equity` | micro-entity |
| net_assets | 158676 | GBP | 2024-06-30 | 2026-02-16 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 1548676 | GBP | 2024-06-30 | 2024-12-02 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 200 | GBP | 2024-06-30 | 2026-02-16 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 200 | GBP | 2024-06-30 | 2024-12-02 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 200 | GBP | 2024-06-30 | 2026-02-16 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 200 | GBP | 2024-06-30 | 2024-12-02 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2023-06-30 | 2024-12-02 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | xbrli:pure | 2023-06-30 | 2023-07-10 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 122 | GBP | 2023-06-30 | 2023-07-10 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 1548476 | GBP | 2023-06-30 | 2024-12-02 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 1548476 | GBP | 2023-06-30 | 2023-07-10 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 322 | GBP | 2023-06-30 | 2024-12-02 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 322 | GBP | 2023-06-30 | 2023-07-10 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 122 | GBP | 2023-06-30 | 2024-12-02 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | -1548676 | GBP | 2023-06-30 | 2023-07-10 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -1548678 | GBP | 2023-06-30 | 2023-07-10 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 1548676 | GBP | 2023-06-30 | 2024-12-02 | filed | yes | `uk-core:Equity` | micro-entity |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-06-30 | 2023-07-10 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 1548676 | GBP | 2023-06-30 | 2024-12-02 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | -1548676 | GBP | 2023-06-30 | 2023-07-10 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 200 | GBP | 2023-06-30 | 2024-12-02 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -200 | GBP | 2023-06-30 | 2023-07-10 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 200 | GBP | 2023-06-30 | 2024-12-02 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -200 | GBP | 2023-06-30 | 2023-07-10 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2022-06-30 | 2023-07-10 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 122 | GBP | 2022-06-30 | 2023-07-10 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 1548476 | GBP | 2022-06-30 | 2023-07-10 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 322 | GBP | 2022-06-30 | 2023-07-10 | filed | yes | `core:Creditors` | total-exemption-full |
| equity | -1548676 | GBP | 2022-06-30 | 2023-07-10 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -1548678 | GBP | 2022-06-30 | 2023-07-10 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2022-06-30 | 2023-07-10 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | -1548676 | GBP | 2022-06-30 | 2023-07-10 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -200 | GBP | 2022-06-30 | 2023-07-10 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -200 | GBP | 2022-06-30 | 2023-07-10 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2024-12-02: `{"superseded_document_id": "gb:03413403:doc:2n5SajCz83k1u6-RCQln1XhKQMPqz4BgiH7cig8PE8w", "restatements": [{"concept": "net_current_assets", "period_end": "2023-06-30", "old_value": "-200.0000", "new_`
- event restatement @ 2026-02-16: `{"superseded_document_id": "gb:03413403:doc:9dfGRy_7ffM_gq33NKB5Q-RMZPqZHxVpFSlZHd4hhfc", "restatements": [{"concept": "creditors_after_one_year", "period_end": "2024-06-30", "old_value": "1548476.000`

## MAIDENHURST LIMITED (`gb:03931470`)

- registration: `03931470` (GB), status active, incorporated 2000-02-23
- classification: ['62020', '63110', '82990'] (sic_2007)
- records: 13 officers, 1 beneficial owners, 1 ownership statements, 0 security interests, 87 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 4 | xbrli:pure | 2026-02-28 | 2026-08-21 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 5900 | GBP | 2026-02-28 | 2026-08-21 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 223114 | GBP | 2026-02-28 | 2026-08-21 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 5900 | GBP | 2026-02-28 | 2026-08-21 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2026-02-28 | 2026-08-21 | filed | yes | `core:Equity` | total-exemption-full |
| equity | -165422 | GBP | 2026-02-28 | 2026-08-21 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -165522 | GBP | 2026-02-28 | 2026-08-21 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 51792 | GBP | 2026-02-28 | 2026-08-21 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | -165422 | GBP | 2026-02-28 | 2026-08-21 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -217214 | GBP | 2026-02-28 | 2026-08-21 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_before_tax | -17129 | GBP | 2026-02-28 | 2026-08-21 | filed | yes | `core:ProfitLossOnOrdinaryActivitiesBeforeTax` | total-exemption-full |
| total_assets_less_current_liabilities | -165422 | GBP | 2026-02-28 | 2026-08-21 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 4 | xbrli:pure | 2025-02-28 | 2026-08-21 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 4 | xbrli:pure | 2025-02-28 | 2025-08-15 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| cash | 5789 | GBP | 2025-02-28 | 2026-08-21 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 206073 | GBP | 2025-02-28 | 2026-08-21 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 203913 | GBP | 2025-02-28 | 2025-08-15 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 5789 | GBP | 2025-02-28 | 2026-08-21 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 5789 | GBP | 2025-02-28 | 2025-08-15 | filed | no | `core:CurrentAssets` | micro-entity |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-02-28 | 2026-08-21 | filed | yes | `core:Equity` | total-exemption-full |
| equity | -148293 | GBP | 2025-02-28 | 2025-08-15 | filed | no | `core:Equity` | micro-entity |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -148393 | GBP | 2025-02-28 | 2026-08-21 | filed | yes | `core:Equity` | total-exemption-full |
| equity | -148293 | GBP | 2025-02-28 | 2026-08-21 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 51991 | GBP | 2025-02-28 | 2025-08-15 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 51991 | GBP | 2025-02-28 | 2026-08-21 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | -148293 | GBP | 2025-02-28 | 2025-08-15 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | -148293 | GBP | 2025-02-28 | 2026-08-21 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -198124 | GBP | 2025-02-28 | 2025-08-15 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -200284 | GBP | 2025-02-28 | 2026-08-21 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_before_tax | -25169 | GBP | 2025-02-28 | 2026-08-21 | filed | yes | `core:ProfitLossOnOrdinaryActivitiesBeforeTax` | total-exemption-full |
| total_assets_less_current_liabilities | -148293 | GBP | 2025-02-28 | 2026-08-21 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -146133 | GBP | 2025-02-28 | 2025-08-15 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 4 | xbrli:pure | 2024-02-29 | 2024-07-09 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 4 | xbrli:pure | 2024-02-29 | 2025-08-15 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 179858 | GBP | 2024-02-29 | 2025-08-15 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 179858 | GBP | 2024-02-29 | 2024-07-09 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 6352 | GBP | 2024-02-29 | 2025-08-15 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 6352 | GBP | 2024-02-29 | 2024-07-09 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | -123124 | GBP | 2024-02-29 | 2024-07-09 | filed | no | `core:Equity` | micro-entity |
| equity | -123124 | GBP | 2024-02-29 | 2025-08-15 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 52212 | GBP | 2024-02-29 | 2024-07-09 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 52212 | GBP | 2024-02-29 | 2025-08-15 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | -123124 | GBP | 2024-02-29 | 2024-07-09 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | -123124 | GBP | 2024-02-29 | 2025-08-15 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -173506 | GBP | 2024-02-29 | 2024-07-09 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -173506 | GBP | 2024-02-29 | 2025-08-15 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -121294 | GBP | 2024-02-29 | 2025-08-15 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -121294 | GBP | 2024-02-29 | 2024-07-09 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 4 | xbrli:pure | 2023-02-28 | 2024-07-09 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 148099 | GBP | 2023-02-28 | 2024-07-09 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 7109 | GBP | 2023-02-28 | 2024-07-09 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -108214 | GBP | 2023-02-28 | 2024-07-09 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 52458 | GBP | 2023-02-28 | 2024-07-09 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | -108214 | GBP | 2023-02-28 | 2024-07-09 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -140990 | GBP | 2023-02-28 | 2024-07-09 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -88532 | GBP | 2023-02-28 | 2024-07-09 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2026-08-21: `{"superseded_document_id": "gb:03931470:doc:nVRs0_qqEe2o0IIVyC9_IN2ghpkjt3TIux9I9evuDBY", "restatements": [{"concept": "creditors_within_one_year", "period_end": "2025-02-28", "old_value": "203913.000`

## ANALYTIC EYE LTD (`gb:04471248`)

- registration: `04471248` (GB), status active, incorporated 2002-06-27
- classification: ['62012'] (sic_2007)
- records: 4 officers, 2 beneficial owners, 1 ownership statements, 1 security interests, 85 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.02 | xbrli:pure | 2025-06-30 | 2026-03-12 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 3797 | GBP | 2025-06-30 | 2026-03-12 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 33439 | GBP | 2025-06-30 | 2026-03-12 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 28219 | GBP | 2025-06-30 | 2026-03-12 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 557 | GBP | 2025-06-30 | 2026-03-12 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 28219 | GBP | 2025-06-30 | 2026-03-12 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 29642 | GBP | 2025-06-30 | 2026-03-12 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 30199 | GBP | 2025-06-30 | 2026-03-12 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0.02 | xbrli:pure | 2024-06-30 | 2026-03-12 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-06-30 | 2024-10-10 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5232 | GBP | 2024-06-30 | 2024-10-10 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5232 | GBP | 2024-06-30 | 2026-03-12 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 42887 | GBP | 2024-06-30 | 2024-10-10 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 42887 | GBP | 2024-06-30 | 2026-03-12 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 36761 | GBP | 2024-06-30 | 2024-10-10 | filed | no | `core:Equity` | micro-entity |
| equity | 36761 | GBP | 2024-06-30 | 2026-03-12 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 741 | GBP | 2024-06-30 | 2024-10-10 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 741 | GBP | 2024-06-30 | 2026-03-12 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 36761 | GBP | 2024-06-30 | 2026-03-12 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 37655 | GBP | 2024-06-30 | 2026-03-12 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 38396 | GBP | 2024-06-30 | 2026-03-12 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-06-30 | 2024-10-10 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-06-30 | 2023-11-16 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 9350 | GBP | 2023-06-30 | 2023-11-16 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 9350 | GBP | 2023-06-30 | 2024-10-10 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 64427 | GBP | 2023-06-30 | 2024-10-10 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 64427 | GBP | 2023-06-30 | 2023-11-16 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 54504 | GBP | 2023-06-30 | 2023-11-16 | filed | no | `core:Equity` | micro-entity |
| equity | 54504 | GBP | 2023-06-30 | 2024-10-10 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 987 | GBP | 2023-06-30 | 2023-11-16 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 987 | GBP | 2023-06-30 | 2024-10-10 | filed | yes | `core:FixedAssets` | micro-entity |
| average_employees | 2 | xbrli:pure | 2022-06-30 | 2023-11-16 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 7509 | GBP | 2022-06-30 | 2023-11-16 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 68858 | GBP | 2022-06-30 | 2023-11-16 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 61517 | GBP | 2022-06-30 | 2023-11-16 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 1318 | GBP | 2022-06-30 | 2023-11-16 | filed | yes | `core:FixedAssets` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2026-03-12: `{"superseded_document_id": "gb:04471248:doc:H-hT_4tuBYkDILb_PvkIq5ufABodfvLHiM3De-feuyE", "restatements": [{"concept": "average_employees", "period_end": "2024-06-30", "old_value": "2.0000", "new_valu`

## IMPORTED CAST PRODUCTS LIMITED (`gb:05030615`)

- registration: `05030615` (GB), status active, incorporated 2004-01-30
- classification: ['71129'] (sic_2007)
- records: 6 officers, 3 beneficial owners, 0 ownership statements, 0 security interests, 61 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2026-01-31 | 2026-08-14 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 632847 | GBP | 2026-01-31 | 2026-08-14 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 7378 | GBP | 2026-01-31 | 2026-08-14 | filed | yes | `ns5:Creditors` | total-exemption-full |
| current_assets | 673355 | GBP | 2026-01-31 | 2026-08-14 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 40508 | GBP | 2026-01-31 | 2026-08-14 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2026-01-31 | 2026-08-14 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 671789 | GBP | 2026-01-31 | 2026-08-14 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 671689 | GBP | 2026-01-31 | 2026-08-14 | filed | yes | `ns5:Equity` | total-exemption-full |
| fixed_assets | 5812 | GBP | 2026-01-31 | 2026-08-14 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| net_assets | 671789 | GBP | 2026-01-31 | 2026-08-14 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 665977 | GBP | 2026-01-31 | 2026-08-14 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 671789 | GBP | 2026-01-31 | 2026-08-14 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2025-01-31 | 2026-08-14 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2025-01-31 | 2025-07-04 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 676660 | GBP | 2025-01-31 | 2025-07-04 | filed | no | `uk-core:CashBankOnHand` | total-exemption-full |
| cash | 676660 | GBP | 2025-01-31 | 2026-08-14 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 70727 | GBP | 2025-01-31 | 2025-07-04 | filed | yes | `uk-core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 70726 | GBP | 2025-01-31 | 2026-08-14 | filed | yes | `ns5:Creditors` | total-exemption-full |
| current_assets | 709624 | GBP | 2025-01-31 | 2025-07-04 | filed | no | `uk-core:CurrentAssets` | total-exemption-full |
| current_assets | 677528 | GBP | 2025-01-31 | 2026-08-14 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 868 | GBP | 2025-01-31 | 2026-08-14 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 645251 | GBP | 2025-01-31 | 2025-07-04 | filed | no | `uk-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 645252 | GBP | 2025-01-31 | 2026-08-14 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-01-31 | 2026-08-14 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-01-31 | 2025-07-04 | filed | no | `uk-core:Equity` | total-exemption-full |
| equity | 645351 | GBP | 2025-01-31 | 2025-07-04 | filed | no | `uk-core:Equity` | total-exemption-full |
| equity | 645352 | GBP | 2025-01-31 | 2026-08-14 | filed | yes | `ns5:Equity` | total-exemption-full |
| fixed_assets | 6454 | GBP | 2025-01-31 | 2026-08-14 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| fixed_assets | 6454 | GBP | 2025-01-31 | 2025-07-04 | filed | no | `uk-core:FixedAssets` | total-exemption-full |
| net_assets | 645351 | GBP | 2025-01-31 | 2025-07-04 | filed | no | `uk-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 613256 | GBP | 2025-01-31 | 2026-08-14 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 606802 | GBP | 2025-01-31 | 2026-08-14 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 638897 | GBP | 2025-01-31 | 2025-07-04 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 645351 | GBP | 2025-01-31 | 2025-07-04 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 613256 | GBP | 2025-01-31 | 2026-08-14 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-01-31 | 2024-05-31 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-01-31 | 2025-07-04 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 488551 | GBP | 2024-01-31 | 2025-07-04 | filed | yes | `uk-core:CashBankOnHand` | total-exemption-full |
| cash | 488551 | GBP | 2024-01-31 | 2024-05-31 | filed | no | `uk-core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 67421 | GBP | 2024-01-31 | 2025-07-04 | filed | yes | `uk-core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 67421 | GBP | 2024-01-31 | 2024-05-31 | filed | no | `uk-core:Creditors` | total-exemption-full |
| current_assets | 493299 | GBP | 2024-01-31 | 2025-07-04 | filed | yes | `uk-core:CurrentAssets` | total-exemption-full |
| current_assets | 493299 | GBP | 2024-01-31 | 2024-05-31 | filed | no | `uk-core:CurrentAssets` | total-exemption-full |
| equity | 433469 | GBP | 2024-01-31 | 2024-05-31 | filed | no | `uk-core:Equity` | total-exemption-full |
| equity | 433469 | GBP | 2024-01-31 | 2025-07-04 | filed | yes | `uk-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-01-31 | 2025-07-04 | filed | yes | `uk-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-01-31 | 2024-05-31 | filed | no | `uk-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 433369 | GBP | 2024-01-31 | 2025-07-04 | filed | yes | `uk-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 433369 | GBP | 2024-01-31 | 2024-05-31 | filed | no | `uk-core:Equity` | total-exemption-full |
| fixed_assets | 7591 | GBP | 2024-01-31 | 2025-07-04 | filed | yes | `uk-core:FixedAssets` | total-exemption-full |
| fixed_assets | 7591 | GBP | 2024-01-31 | 2024-05-31 | filed | no | `uk-core:FixedAssets` | total-exemption-full |
| net_assets | 433469 | GBP | 2024-01-31 | 2024-05-31 | filed | no | `uk-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 433469 | GBP | 2024-01-31 | 2025-07-04 | filed | yes | `uk-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 425878 | GBP | 2024-01-31 | 2024-05-31 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 433469 | GBP | 2024-01-31 | 2025-07-04 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 433469 | GBP | 2024-01-31 | 2024-05-31 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-01-31 | 2024-05-31 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 260950 | GBP | 2023-01-31 | 2024-05-31 | filed | yes | `uk-core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 47787 | GBP | 2023-01-31 | 2024-05-31 | filed | yes | `uk-core:Creditors` | total-exemption-full |
| current_assets | 265800 | GBP | 2023-01-31 | 2024-05-31 | filed | yes | `uk-core:CurrentAssets` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 225678 | GBP | 2023-01-31 | 2024-05-31 | filed | yes | `uk-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-01-31 | 2024-05-31 | filed | yes | `uk-core:Equity` | total-exemption-full |
| equity | 225778 | GBP | 2023-01-31 | 2024-05-31 | filed | yes | `uk-core:Equity` | total-exemption-full |
| fixed_assets | 7765 | GBP | 2023-01-31 | 2024-05-31 | filed | yes | `uk-core:FixedAssets` | total-exemption-full |
| net_assets | 225778 | GBP | 2023-01-31 | 2024-05-31 | filed | yes | `uk-core:NetAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 225778 | GBP | 2023-01-31 | 2024-05-31 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2026-08-14: `{"superseded_document_id": "gb:05030615:doc:KZUpDCPgy56MOv6ra8GTKprj9xftcVYRGKjT-KyNjHE", "restatements": [{"concept": "current_assets", "period_end": "2025-01-31", "old_value": "709624.0000", "new_va`

## FRACSOFT LIMITED (`gb:05561191`)

- registration: `05561191` (GB), status active, incorporated 2005-09-12
- classification: ['62090'] (sic_2007)
- records: 5 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 69 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | iso4217:GBP | 2025-09-30 | 2026-09-24 | filed | yes | `pt:AverageNumberEmployeesDuringPeriod` | micro-entity |
| net_assets | -275403 | GBP | 2025-09-30 | 2026-09-24 | filed | yes | `pt:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -274685 | GBP | 2025-09-30 | 2026-09-24 | filed | yes | `pt:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -271201 | GBP | 2025-09-30 | 2026-09-24 | filed | yes | `pt:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2024-09-30 | 2025-06-30 | filed | yes | `pt:AverageNumberEmployeesDuringPeriod` | micro-entity |
| net_assets | -248995 | GBP | 2024-09-30 | 2026-09-24 | filed | yes | `pt:NetAssetsLiabilities` | micro-entity |
| net_assets | -248995 | GBP | 2024-09-30 | 2025-06-30 | filed | no | `pt:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -248436 | GBP | 2024-09-30 | 2025-06-30 | filed | yes | `pt:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -245948 | GBP | 2024-09-30 | 2026-09-24 | filed | yes | `pt:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -245948 | GBP | 2024-09-30 | 2025-06-30 | filed | no | `pt:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2023-09-30 | 2024-06-26 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 253028 | GBP | 2023-09-30 | 2024-06-26 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 22004 | GBP | 2023-09-30 | 2024-06-26 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 227990 | GBP | 2023-09-30 | 2024-06-26 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 3034 | GBP | 2023-09-30 | 2024-06-26 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | -227990 | GBP | 2023-09-30 | 2025-06-30 | filed | yes | `pt:NetAssetsLiabilities` | micro-entity |
| net_assets | 227990 | GBP | 2023-09-30 | 2024-06-26 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 231024 | GBP | 2023-09-30 | 2024-06-26 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 227990 | GBP | 2023-09-30 | 2024-06-26 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -223830 | GBP | 2023-09-30 | 2025-06-30 | filed | yes | `pt:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2022-09-30 | 2024-06-26 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 228653 | GBP | 2022-09-30 | 2024-06-26 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 55550 | GBP | 2022-09-30 | 2024-06-26 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 169404 | GBP | 2022-09-30 | 2024-06-26 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 3699 | GBP | 2022-09-30 | 2024-06-26 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 169404 | GBP | 2022-09-30 | 2024-06-26 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 173103 | GBP | 2022-09-30 | 2024-06-26 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 169404 | GBP | 2022-09-30 | 2024-06-26 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2025-06-30: `{"superseded_document_id": "gb:05561191:doc:4uy7fJjb0x_7JQPeZihfYuUmDNLxFZuEhhYRcQxGhYE", "restatements": [{"concept": "total_assets_less_current_liabilities", "period_end": "2023-09-30", "old_value":`

## OCEAN INFORMATICS UK LIMITED (`gb:06066175`)

- registration: `06066175` (GB), status active, incorporated 2007-01-24
- classification: ['58290', '62020', '62090'] (sic_2007)
- records: 9 officers, 0 beneficial owners, 1 ownership statements, 0 security interests, 72 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-06-30 | 2026-03-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 173496 | GBP | 2025-06-30 | 2026-03-30 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 9331 | GBP | 2025-06-30 | 2026-03-30 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 154869 | GBP | 2025-06-30 | 2026-03-30 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -129402 | GBP | 2025-06-30 | 2026-03-30 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 2396 | GBP | 2025-06-30 | 2026-03-30 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | -129402 | GBP | 2025-06-30 | 2026-03-30 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 151468 | GBP | 2025-06-30 | 2026-03-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 153864 | GBP | 2025-06-30 | 2026-03-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-06-30 | 2026-03-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-06-30 | 2025-03-27 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 223767 | GBP | 2024-06-30 | 2025-03-27 | filed | no | `core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 223767 | GBP | 2024-06-30 | 2026-03-30 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 9486 | GBP | 2024-06-30 | 2025-03-27 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 9486 | GBP | 2024-06-30 | 2026-03-30 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 280524 | GBP | 2024-06-30 | 2025-03-27 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 280524 | GBP | 2024-06-30 | 2026-03-30 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -62415 | GBP | 2024-06-30 | 2026-03-30 | filed | yes | `core:Equity` | micro-entity |
| equity | -62415 | GBP | 2024-06-30 | 2025-03-27 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 1477 | GBP | 2024-06-30 | 2026-03-30 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 1477 | GBP | 2024-06-30 | 2025-03-27 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | -62415 | GBP | 2024-06-30 | 2025-03-27 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | -62415 | GBP | 2024-06-30 | 2026-03-30 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 283887 | GBP | 2024-06-30 | 2025-03-27 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 283887 | GBP | 2024-06-30 | 2026-03-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 285364 | GBP | 2024-06-30 | 2026-03-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 285364 | GBP | 2024-06-30 | 2025-03-27 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-06-30 | 2024-03-30 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-06-30 | 2025-03-27 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 265168 | GBP | 2023-06-30 | 2025-03-27 | filed | yes | `core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 265168 | GBP | 2023-06-30 | 2024-03-30 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | -2914 | GBP | 2023-06-30 | 2024-03-30 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | -2914 | GBP | 2023-06-30 | 2025-03-27 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 302086 | GBP | 2023-06-30 | 2024-03-30 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 302086 | GBP | 2023-06-30 | 2025-03-27 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -62567 | GBP | 2023-06-30 | 2025-03-27 | filed | yes | `core:Equity` | micro-entity |
| equity | -62567 | GBP | 2023-06-30 | 2024-03-30 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 2830 | GBP | 2023-06-30 | 2025-03-27 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 2830 | GBP | 2023-06-30 | 2024-03-30 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | -62567 | GBP | 2023-06-30 | 2025-03-27 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | -62567 | GBP | 2023-06-30 | 2024-03-30 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 313418 | GBP | 2023-06-30 | 2025-03-27 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 313418 | GBP | 2023-06-30 | 2024-03-30 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 316248 | GBP | 2023-06-30 | 2024-03-30 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 316248 | GBP | 2023-06-30 | 2025-03-27 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2022-06-30 | 2024-03-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 286265 | GBP | 2022-06-30 | 2024-03-30 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | -7567 | GBP | 2022-06-30 | 2024-03-30 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 337596 | GBP | 2022-06-30 | 2024-03-30 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -53568 | GBP | 2022-06-30 | 2024-03-30 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 1642 | GBP | 2022-06-30 | 2024-03-30 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | -53568 | GBP | 2022-06-30 | 2024-03-30 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 345411 | GBP | 2022-06-30 | 2024-03-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 347053 | GBP | 2022-06-30 | 2024-03-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## K & M PIPE SYSTEMS LIMITED (`gb:06478931`)

- registration: `06478931` (GB), status active, incorporated 2008-01-21
- classification: ['71129'] (sic_2007)
- records: 5 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 54 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2026-03-31 | 2026-07-14 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 1005701 | GBP | 2026-03-31 | 2026-07-14 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 806251 | GBP | 2026-03-31 | 2026-07-14 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 1335723 | GBP | 2026-03-31 | 2026-07-14 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 330022 | GBP | 2026-03-31 | 2026-07-14 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 330022 | GBP | 2026-03-31 | 2026-07-14 | filed | yes | `core:Debtors` | total-exemption-full |
| net_assets | 569179 | GBP | 2026-03-31 | 2026-07-14 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 529472 | GBP | 2026-03-31 | 2026-07-14 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 586906 | GBP | 2026-03-31 | 2026-07-14 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2025-03-31 | 2025-07-25 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2025-03-31 | 2026-07-14 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 522661 | GBP | 2025-03-31 | 2025-07-25 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 522661 | GBP | 2025-03-31 | 2026-07-14 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 96300 | GBP | 2025-03-31 | 2025-07-25 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 96300 | GBP | 2025-03-31 | 2026-07-14 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 560657 | GBP | 2025-03-31 | 2026-07-14 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 560657 | GBP | 2025-03-31 | 2025-07-25 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 37996 | GBP | 2025-03-31 | 2025-07-25 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 37996 | GBP | 2025-03-31 | 2025-07-25 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 37996 | GBP | 2025-03-31 | 2026-07-14 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 37996 | GBP | 2025-03-31 | 2026-07-14 | filed | yes | `core:Debtors` | total-exemption-full |
| net_assets | 594217 | GBP | 2025-03-31 | 2026-07-14 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 594217 | GBP | 2025-03-31 | 2025-07-25 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 464357 | GBP | 2025-03-31 | 2025-07-25 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 464357 | GBP | 2025-03-31 | 2026-07-14 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 629106 | GBP | 2025-03-31 | 2025-07-25 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 629106 | GBP | 2025-03-31 | 2026-07-14 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-03-31 | 2025-07-25 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 517091 | GBP | 2024-03-31 | 2025-07-25 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 84124 | GBP | 2024-03-31 | 2025-07-25 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 584551 | GBP | 2024-03-31 | 2025-07-25 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 67460 | GBP | 2024-03-31 | 2025-07-25 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 67460 | GBP | 2024-03-31 | 2025-07-25 | filed | yes | `core:Debtors` | total-exemption-full |
| net_assets | 626763 | GBP | 2024-03-31 | 2025-07-25 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 500427 | GBP | 2024-03-31 | 2025-07-25 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 666335 | GBP | 2024-03-31 | 2025-07-25 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## GATESHEAD TRADING COMPANY LIMITED (`gb:06873659`)

- registration: `06873659` (GB), status active, incorporated 2009-04-08
- classification: ['41201', '41202', '71111', '78109'] (sic_2007)
- records: 13 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 64 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.04 | xbrli:pure | 2025-03-31 | 2025-12-17 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | small |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5890 | GBP | 2025-03-31 | 2025-12-17 | filed | yes | `core:Creditors` | small |
| debtors | 20854 | GBP | 2025-03-31 | 2025-12-17 | filed | yes | `core:Debtors` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 20854 | GBP | 2025-03-31 | 2025-12-17 | filed | yes | `core:Debtors` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 14963 | GBP | 2025-03-31 | 2025-12-17 | filed | yes | `core:Equity` | small |
| equity | 14964 | GBP | 2025-03-31 | 2025-12-17 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2025-03-31 | 2025-12-17 | filed | yes | `core:Equity` | small |
| net_current_assets | 14964 | GBP | 2025-03-31 | 2025-12-17 | filed | yes | `core:NetCurrentAssetsLiabilities` | small |
| average_employees | 0.04 | xbrli:pure | 2024-03-31 | 2025-12-17 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | small |
| average_employees | 4 | xbrli:pure | 2024-03-31 | 2024-12-23 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 3291 | GBP | 2024-03-31 | 2024-12-23 | filed | yes | `core:Creditors` | small |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 3291 | GBP | 2024-03-31 | 2025-12-17 | filed | yes | `core:Creditors` | small |
| debtors | 26431 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:Debtors` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 26431 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:Debtors` | small |
| debtors | 26431 | GBP | 2024-03-31 | 2025-12-17 | filed | yes | `core:Debtors` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 26431 | GBP | 2024-03-31 | 2025-12-17 | filed | yes | `core:Debtors` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 23139 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 23139 | GBP | 2024-03-31 | 2025-12-17 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2024-03-31 | 2025-12-17 | filed | yes | `core:Equity` | small |
| equity | 23140 | GBP | 2024-03-31 | 2025-12-17 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:Equity` | small |
| equity | 23140 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:Equity` | small |
| net_current_assets | 23140 | GBP | 2024-03-31 | 2025-12-17 | filed | yes | `core:NetCurrentAssetsLiabilities` | small |
| net_current_assets | 23140 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:NetCurrentAssetsLiabilities` | small |
| average_employees | 4 | xbrli:pure | 2023-03-31 | 2024-12-23 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 196882 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:Creditors` | small |
| debtors | 263884 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:Debtors` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 263884 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:Debtors` | small |
| equity | 67002 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 67001 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:Equity` | small |
| net_current_assets | 67002 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:NetCurrentAssetsLiabilities` | small |

_No coverage facts for the latest run._

- event restatement @ 2025-12-17: `{"superseded_document_id": "gb:06873659:doc:M4u6G2aTJ4xNNY8Z9x2Wa7liHtwqVI9iUv6CfoHtk5g", "restatements": [{"concept": "average_employees", "period_end": "2024-03-31", "old_value": "4.0000", "new_valu`
