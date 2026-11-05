# Ingest spot-check

- database: `data/engine.db`
- latest run: `20261105T090455Z-1d44f98e`
- companies in store: 44200; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## PIPER TEST & MEASUREMENT LIMITED (`gb:02668838`)

- registration: `02668838` (GB), status active, incorporated 1991-12-06
- classification: ['71129'] (sic_2007)
- records: 4 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 80 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | iso4217:GBP | 2024-12-31 | 2025-09-27 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2024-12-31 | 2025-09-27 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 62703 | GBP | 2024-12-31 | 2025-09-27 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 13391 | GBP | 2024-12-31 | 2025-09-27 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 49310 | GBP | 2024-12-31 | 2025-09-27 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2024-12-31 | 2025-09-27 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 49310 | GBP | 2024-12-31 | 2025-09-27 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 49312 | GBP | 2024-12-31 | 2025-09-27 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 49310 | GBP | 2024-12-31 | 2025-09-27 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2023-12-31 | 2024-09-30 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2023-12-31 | 2025-09-27 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2023-12-31 | 2025-09-27 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 72746 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 72746 | GBP | 2023-12-31 | 2025-09-27 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 39282 | GBP | 2023-12-31 | 2025-09-27 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 39282 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | 32364 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 32364 | GBP | 2023-12-31 | 2025-09-27 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 1098 | GBP | 2023-12-31 | 2025-09-27 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 1098 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `uk-core:FixedAssets` | micro-entity |
| net_assets | 32364 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 32364 | GBP | 2023-12-31 | 2025-09-27 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 33464 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 33464 | GBP | 2023-12-31 | 2025-09-27 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 32364 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 32364 | GBP | 2023-12-31 | 2025-09-27 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2022-12-31 | 2023-09-30 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2022-12-31 | 2024-09-30 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2022-12-31 | 2023-09-30 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 66558 | GBP | 2022-12-31 | 2023-09-30 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 66558 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 33564 | GBP | 2022-12-31 | 2023-09-30 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 33564 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 31514 | GBP | 2022-12-31 | 2023-09-30 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 31514 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 1478 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 1478 | GBP | 2022-12-31 | 2023-09-30 | filed | no | `uk-core:FixedAssets` | micro-entity |
| net_assets | 31514 | GBP | 2022-12-31 | 2023-09-30 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 31514 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 32994 | GBP | 2022-12-31 | 2023-09-30 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 32994 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 31514 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 31514 | GBP | 2022-12-31 | 2023-09-30 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2021-12-31 | 2023-09-30 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2021-12-31 | 2023-09-30 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 92108 | GBP | 2021-12-31 | 2023-09-30 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 55428 | GBP | 2021-12-31 | 2023-09-30 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 34694 | GBP | 2021-12-31 | 2023-09-30 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 1984 | GBP | 2021-12-31 | 2023-09-30 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 34694 | GBP | 2021-12-31 | 2023-09-30 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 36680 | GBP | 2021-12-31 | 2023-09-30 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 34694 | GBP | 2021-12-31 | 2023-09-30 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## KIMEX TECHNOLOGY LIMITED (`gb:03311013`)

- registration: `03311013` (GB), status active, incorporated 1997-01-31
- classification: ['71111', '82110'] (sic_2007)
- records: 6 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 86 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-06-30 | 2026-06-30 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 0 | GBP | 2025-06-30 | 2026-06-30 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 0 | GBP | 2025-06-30 | 2026-06-30 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -24868 | GBP | 2025-06-30 | 2026-06-30 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-06-30 | 2026-06-30 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 29 | GBP | 2025-06-30 | 2026-06-30 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | -24768 | GBP | 2025-06-30 | 2026-06-30 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -24797 | GBP | 2025-06-30 | 2026-06-30 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -24768 | GBP | 2025-06-30 | 2026-06-30 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-06-30 | 2025-02-21 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-06-30 | 2026-06-30 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 4 | GBP | 2024-06-30 | 2025-02-21 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 4 | GBP | 2024-06-30 | 2026-06-30 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 4 | GBP | 2024-06-30 | 2026-06-30 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-06-30 | 2025-02-21 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -21336 | GBP | 2024-06-30 | 2026-06-30 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-06-30 | 2026-06-30 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -21336 | GBP | 2024-06-30 | 2025-02-21 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | -21236 | GBP | 2024-06-30 | 2025-02-21 | filed | yes | `ns5:Equity` | total-exemption-full |
| fixed_assets | 39 | GBP | 2024-06-30 | 2026-06-30 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | -21236 | GBP | 2024-06-30 | 2026-06-30 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -21275 | GBP | 2024-06-30 | 2026-06-30 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -21275 | GBP | 2024-06-30 | 2025-02-21 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -21236 | GBP | 2024-06-30 | 2025-02-21 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -21236 | GBP | 2024-06-30 | 2026-06-30 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-06-30 | 2025-02-21 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 1 | xbrli:pure | 2023-06-30 | 2024-03-28 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 369 | GBP | 2023-06-30 | 2024-03-28 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 369 | GBP | 2023-06-30 | 2025-02-21 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| equity | -16236 | GBP | 2023-06-30 | 2025-02-21 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | -16236 | GBP | 2023-06-30 | 2024-03-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -16336 | GBP | 2023-06-30 | 2025-02-21 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 100 | GBP | 2023-06-30 | 2024-03-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -16336 | GBP | 2023-06-30 | 2024-03-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-06-30 | 2025-02-21 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | -16287 | GBP | 2023-06-30 | 2025-02-21 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | -16287 | GBP | 2023-06-30 | 2024-03-28 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -16236 | GBP | 2023-06-30 | 2025-02-21 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | -16236 | GBP | 2023-06-30 | 2024-03-28 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 1 | xbrli:pure | 2022-06-30 | 2024-03-28 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 4 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 100 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | -13795 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -13895 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | -13871 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | -13795 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## PD COMMUNICATIONS LIMITED (`gb:03805834`)

- registration: `03805834` (GB), status active, incorporated 1999-07-12
- classification: ['62020'] (sic_2007)
- records: 7 officers, 2 beneficial owners, 0 ownership statements, 1 security interests, 73 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-03-31 | 2025-06-24 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 10418 | GBP | 2025-03-31 | 2025-06-24 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 5066 | GBP | 2025-03-31 | 2025-06-24 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 27449 | GBP | 2025-03-31 | 2025-06-24 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 23887 | GBP | 2025-03-31 | 2025-06-24 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 13469 | GBP | 2025-03-31 | 2025-06-24 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 1023 | GBP | 2025-03-31 | 2025-06-24 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10 | GBP | 2025-03-31 | 2025-06-24 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1013 | GBP | 2025-03-31 | 2025-06-24 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 1023 | GBP | 2025-03-31 | 2025-06-24 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -3562 | GBP | 2025-03-31 | 2025-06-24 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 6089 | GBP | 2025-03-31 | 2025-06-24 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-03-31 | 2024-12-13 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-03-31 | 2025-06-24 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 1140 | GBP | 2024-03-31 | 2024-12-13 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 1140 | GBP | 2024-03-31 | 2025-06-24 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 8865 | GBP | 2024-03-31 | 2025-06-24 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 8865 | GBP | 2024-03-31 | 2024-12-13 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 10851 | GBP | 2024-03-31 | 2024-12-13 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 10851 | GBP | 2024-03-31 | 2025-06-24 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 23237 | GBP | 2024-03-31 | 2025-06-24 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 23237 | GBP | 2024-03-31 | 2024-12-13 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors | 22097 | GBP | 2024-03-31 | 2025-06-24 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 22097 | GBP | 2024-03-31 | 2024-12-13 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10 | GBP | 2024-03-31 | 2025-06-24 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 16379 | GBP | 2024-03-31 | 2025-06-24 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 16389 | GBP | 2024-03-31 | 2025-06-24 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10 | GBP | 2024-03-31 | 2024-12-13 | filed | no | `core:Equity` | total-exemption-full |
| equity | 16389 | GBP | 2024-03-31 | 2024-12-13 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 16379 | GBP | 2024-03-31 | 2024-12-13 | filed | no | `core:Equity` | total-exemption-full |
| net_assets | 16389 | GBP | 2024-03-31 | 2025-06-24 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 16389 | GBP | 2024-03-31 | 2024-12-13 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 12386 | GBP | 2024-03-31 | 2024-12-13 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 12386 | GBP | 2024-03-31 | 2025-06-24 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 25254 | GBP | 2024-03-31 | 2024-12-13 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 25254 | GBP | 2024-03-31 | 2025-06-24 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 4 | xbrli:pure | 2023-03-31 | 2023-12-06 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 3 | xbrli:pure | 2023-03-31 | 2024-12-13 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 104493 | GBP | 2023-03-31 | 2024-12-13 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 104493 | GBP | 2023-03-31 | 2023-12-06 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 12666 | GBP | 2023-03-31 | 2023-12-06 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 12666 | GBP | 2023-03-31 | 2024-12-13 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 72255 | GBP | 2023-03-31 | 2024-12-13 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 72255 | GBP | 2023-03-31 | 2023-12-06 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 106973 | GBP | 2023-03-31 | 2023-12-06 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 106973 | GBP | 2023-03-31 | 2024-12-13 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 2480 | GBP | 2023-03-31 | 2023-12-06 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 2480 | GBP | 2023-03-31 | 2024-12-13 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10 | GBP | 2023-03-31 | 2023-12-06 | filed | no | `core:Equity` | total-exemption-full |
| equity | 39209 | GBP | 2023-03-31 | 2024-12-13 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10 | GBP | 2023-03-31 | 2024-12-13 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 39199 | GBP | 2023-03-31 | 2024-12-13 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 39209 | GBP | 2023-03-31 | 2023-12-06 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 39199 | GBP | 2023-03-31 | 2023-12-06 | filed | no | `core:Equity` | total-exemption-full |
| net_assets | 39209 | GBP | 2023-03-31 | 2024-12-13 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 39209 | GBP | 2023-03-31 | 2023-12-06 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 34718 | GBP | 2023-03-31 | 2023-12-06 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 34718 | GBP | 2023-03-31 | 2024-12-13 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 51875 | GBP | 2023-03-31 | 2024-12-13 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 51875 | GBP | 2023-03-31 | 2023-12-06 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 3 | xbrli:pure | 2022-03-31 | 2023-12-06 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 21906 | GBP | 2022-03-31 | 2023-12-06 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 16467 | GBP | 2022-03-31 | 2023-12-06 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 97891 | GBP | 2022-03-31 | 2023-12-06 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 96229 | GBP | 2022-03-31 | 2023-12-06 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 74323 | GBP | 2022-03-31 | 2023-12-06 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2022-03-31 | 2023-12-06 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 1882 | GBP | 2022-03-31 | 2023-12-06 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1880 | GBP | 2022-03-31 | 2023-12-06 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 1882 | GBP | 2022-03-31 | 2023-12-06 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -1662 | GBP | 2022-03-31 | 2023-12-06 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 18349 | GBP | 2022-03-31 | 2023-12-06 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2024-12-13: `{"superseded_document_id": "gb:03805834:doc:05CcAFHdBTW2muPN0UDgPg0z_fkIokwiddZMQx4ePiQ", "restatements": [{"concept": "average_employees", "period_end": "2023-03-31", "old_value": "4.0000", "new_valu`

## ABSOLUTE CERTAINTY LIMITED (`gb:04295623`)

- registration: `04295623` (GB), status active, incorporated 2001-09-28
- classification: ['62020'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 59 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | xbrli:pure | 2026-02-28 | 2026-09-18 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 240 | GBP | 2026-02-28 | 2026-09-18 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 63167 | GBP | 2026-02-28 | 2026-09-18 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 62927 | GBP | 2026-02-28 | 2026-09-18 | filed | yes | `core:Equity` | micro-entity |
| net_assets | 62927 | GBP | 2026-02-28 | 2026-09-18 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 62927 | GBP | 2026-02-28 | 2026-09-18 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 62927 | GBP | 2026-02-28 | 2026-09-18 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2025-02-28 | 2026-09-18 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | xbrli:pure | 2025-02-28 | 2025-10-21 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 240 | GBP | 2025-02-28 | 2026-09-18 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 240 | GBP | 2025-02-28 | 2025-10-21 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 65734 | GBP | 2025-02-28 | 2026-09-18 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 65734 | GBP | 2025-02-28 | 2025-10-21 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 65494 | GBP | 2025-02-28 | 2025-10-21 | filed | no | `core:Equity` | micro-entity |
| equity | 65494 | GBP | 2025-02-28 | 2026-09-18 | filed | yes | `core:Equity` | micro-entity |
| net_assets | 65494 | GBP | 2025-02-28 | 2026-09-18 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 65494 | GBP | 2025-02-28 | 2025-10-21 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 65494 | GBP | 2025-02-28 | 2025-10-21 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 65494 | GBP | 2025-02-28 | 2026-09-18 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 65494 | GBP | 2025-02-28 | 2026-09-18 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 65494 | GBP | 2025-02-28 | 2025-10-21 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2024-02-29 | 2024-08-23 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | xbrli:pure | 2024-02-29 | 2025-10-21 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 240 | GBP | 2024-02-29 | 2025-10-21 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 240 | GBP | 2024-02-29 | 2024-08-23 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 69272 | GBP | 2024-02-29 | 2024-08-23 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 69272 | GBP | 2024-02-29 | 2025-10-21 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 69032 | GBP | 2024-02-29 | 2024-08-23 | filed | no | `core:Equity` | micro-entity |
| equity | 69032 | GBP | 2024-02-29 | 2025-10-21 | filed | yes | `core:Equity` | micro-entity |
| net_assets | 69032 | GBP | 2024-02-29 | 2025-10-21 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 69032 | GBP | 2024-02-29 | 2024-08-23 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 69032 | GBP | 2024-02-29 | 2025-10-21 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 69032 | GBP | 2024-02-29 | 2024-08-23 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 69032 | GBP | 2024-02-29 | 2024-08-23 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 69032 | GBP | 2024-02-29 | 2025-10-21 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2023-02-28 | 2024-08-23 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 240 | GBP | 2023-02-28 | 2024-08-23 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 72747 | GBP | 2023-02-28 | 2024-08-23 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 72507 | GBP | 2023-02-28 | 2024-08-23 | filed | yes | `core:Equity` | micro-entity |
| net_assets | 72507 | GBP | 2023-02-28 | 2024-08-23 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 72507 | GBP | 2023-02-28 | 2024-08-23 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 72507 | GBP | 2023-02-28 | 2024-08-23 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## C.J.G. ASSOCIATES LIMITED (`gb:04787302`)

- registration: `04787302` (GB), status active, incorporated 2003-06-04
- classification: ['61900', '62020'] (sic_2007)
- records: 6 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 67 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-06-30 | 2026-03-22 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 12774 | GBP | 2025-06-30 | 2026-03-22 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 67698 | GBP | 2025-06-30 | 2026-03-22 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 82817 | GBP | 2025-06-30 | 2026-03-22 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 48708 | GBP | 2025-06-30 | 2026-03-22 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 35934 | GBP | 2025-06-30 | 2026-03-22 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 7237 | GBP | 2025-06-30 | 2026-03-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 7247 | GBP | 2025-06-30 | 2026-03-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10 | GBP | 2025-06-30 | 2026-03-22 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 7247 | GBP | 2025-06-30 | 2026-03-22 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -34109 | GBP | 2025-06-30 | 2026-03-22 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 83944 | GBP | 2025-06-30 | 2026-03-22 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-06-30 | 2025-03-14 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-06-30 | 2026-03-22 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 5647 | GBP | 2024-06-30 | 2025-03-14 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 5647 | GBP | 2024-06-30 | 2026-03-22 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 15750 | GBP | 2024-06-30 | 2026-03-22 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 15750 | GBP | 2024-06-30 | 2025-03-14 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 55611 | GBP | 2024-06-30 | 2025-03-14 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 55611 | GBP | 2024-06-30 | 2026-03-22 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 41998 | GBP | 2024-06-30 | 2025-03-14 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 41998 | GBP | 2024-06-30 | 2026-03-22 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 36351 | GBP | 2024-06-30 | 2026-03-22 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 36351 | GBP | 2024-06-30 | 2025-03-14 | filed | no | `core:Debtors` | total-exemption-full |
| equity | 35191 | GBP | 2024-06-30 | 2025-03-14 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 35181 | GBP | 2024-06-30 | 2025-03-14 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10 | GBP | 2024-06-30 | 2026-03-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10 | GBP | 2024-06-30 | 2025-03-14 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 35181 | GBP | 2024-06-30 | 2026-03-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 35191 | GBP | 2024-06-30 | 2026-03-22 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 35191 | GBP | 2024-06-30 | 2026-03-22 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 35191 | GBP | 2024-06-30 | 2025-03-14 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -13613 | GBP | 2024-06-30 | 2026-03-22 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -13613 | GBP | 2024-06-30 | 2025-03-14 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 71418 | GBP | 2024-06-30 | 2026-03-22 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 71418 | GBP | 2024-06-30 | 2025-03-14 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-06-30 | 2025-03-14 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-06-30 | 2024-03-28 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 133568 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 133568 | GBP | 2023-06-30 | 2025-03-14 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 24750 | GBP | 2023-06-30 | 2025-03-14 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 24750 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 194487 | GBP | 2023-06-30 | 2025-03-14 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 194487 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 231417 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 231417 | GBP | 2023-06-30 | 2025-03-14 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 97849 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 97849 | GBP | 2023-06-30 | 2025-03-14 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 121866 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `core:Equity` | total-exemption-full |
| equity | 121876 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 121866 | GBP | 2023-06-30 | 2025-03-14 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10 | GBP | 2023-06-30 | 2025-03-14 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 121876 | GBP | 2023-06-30 | 2025-03-14 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `core:Equity` | total-exemption-full |
| net_assets | 121876 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 121876 | GBP | 2023-06-30 | 2025-03-14 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 36930 | GBP | 2023-06-30 | 2025-03-14 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 36930 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 146626 | GBP | 2023-06-30 | 2025-03-14 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 146626 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 3 | xbrli:pure | 2022-06-30 | 2024-03-28 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 20817 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 33750 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 119664 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 147936 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 127119 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 63789 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 63799 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 63799 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 28272 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 97549 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## AUTOMOTIVE DATA SOLUTIONS LIMITED (`gb:05296129`)

- registration: `05296129` (GB), status active, incorporated 2004-11-24
- classification: ['62020'] (sic_2007)
- records: 5 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 50 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-11-30 | 2026-07-21 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 318 | GBP | 2025-11-30 | 2026-07-21 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 3480 | GBP | 2025-11-30 | 2026-07-21 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 3162 | GBP | 2025-11-30 | 2026-07-21 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | -767 | GBP | 2025-11-30 | 2026-07-21 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -768 | GBP | 2025-11-30 | 2026-07-21 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2025-11-30 | 2026-07-21 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | -767 | GBP | 2025-11-30 | 2026-07-21 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -771 | GBP | 2025-11-30 | 2026-07-21 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -1037 | GBP | 2025-11-30 | 2026-07-21 | filed | yes | `ns5:ProfitLoss` | total-exemption-full |
| total_assets_less_current_liabilities | -766 | GBP | 2025-11-30 | 2026-07-21 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-11-30 | 2026-07-21 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-11-30 | 2025-08-29 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 3191 | GBP | 2024-11-30 | 2026-07-21 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 3191 | GBP | 2024-11-30 | 2025-08-29 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 6112 | GBP | 2024-11-30 | 2026-07-21 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 6112 | GBP | 2024-11-30 | 2025-08-29 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 2921 | GBP | 2024-11-30 | 2026-07-21 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 2921 | GBP | 2024-11-30 | 2025-08-29 | filed | no | `ns5:Debtors` | total-exemption-full |
| equity | 270 | GBP | 2024-11-30 | 2025-08-29 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 269 | GBP | 2024-11-30 | 2025-08-29 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2024-11-30 | 2026-07-21 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2024-11-30 | 2025-08-29 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 269 | GBP | 2024-11-30 | 2026-07-21 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 270 | GBP | 2024-11-30 | 2026-07-21 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 270 | GBP | 2024-11-30 | 2025-08-29 | filed | no | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 270 | GBP | 2024-11-30 | 2026-07-21 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 260 | GBP | 2024-11-30 | 2026-07-21 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 260 | GBP | 2024-11-30 | 2025-08-29 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 273 | GBP | 2024-11-30 | 2025-08-29 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 273 | GBP | 2024-11-30 | 2026-07-21 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-11-30 | 2024-08-27 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-11-30 | 2025-08-29 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 8487 | GBP | 2023-11-30 | 2025-08-29 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 8487 | GBP | 2023-11-30 | 2024-08-27 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 16887 | GBP | 2023-11-30 | 2024-08-27 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 16887 | GBP | 2023-11-30 | 2025-08-29 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 8400 | GBP | 2023-11-30 | 2024-08-27 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 8400 | GBP | 2023-11-30 | 2025-08-29 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 8400 | GBP | 2023-11-30 | 2024-08-27 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2023-11-30 | 2025-08-29 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -5450 | GBP | 2023-11-30 | 2025-08-29 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | -5449 | GBP | 2023-11-30 | 2024-08-27 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2023-11-30 | 2024-08-27 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | -5449 | GBP | 2023-11-30 | 2025-08-29 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -5450 | GBP | 2023-11-30 | 2024-08-27 | filed | no | `ns5:Equity` | total-exemption-full |
| net_assets | -5449 | GBP | 2023-11-30 | 2024-08-27 | filed | no | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | -5449 | GBP | 2023-11-30 | 2025-08-29 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -5765 | GBP | 2023-11-30 | 2025-08-29 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -5765 | GBP | 2023-11-30 | 2024-08-27 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -5343 | GBP | 2023-11-30 | 2024-08-27 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -5343 | GBP | 2023-11-30 | 2025-08-29 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2022-11-30 | 2024-08-27 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 7102 | GBP | 2022-11-30 | 2024-08-27 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 49816 | GBP | 2022-11-30 | 2024-08-27 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 42714 | GBP | 2022-11-30 | 2024-08-27 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 42714 | GBP | 2022-11-30 | 2024-08-27 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 17521 | GBP | 2022-11-30 | 2024-08-27 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 17522 | GBP | 2022-11-30 | 2024-08-27 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2022-11-30 | 2024-08-27 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 17522 | GBP | 2022-11-30 | 2024-08-27 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 16600 | GBP | 2022-11-30 | 2024-08-27 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 17738 | GBP | 2022-11-30 | 2024-08-27 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## N GOLD SOLUTIONS LTD (`gb:05777796`)

- registration: `05777796` (GB), status active, incorporated 2006-04-11
- classification: ['62020'] (sic_2007)
- records: 2 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 52 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | iso4217:GBP | 2025-04-30 | 2026-04-30 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 17050 | GBP | 2025-04-30 | 2026-04-30 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 35537 | GBP | 2025-04-30 | 2026-04-30 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 55571 | GBP | 2025-04-30 | 2026-04-30 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 2984 | GBP | 2025-04-30 | 2026-04-30 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 2984 | GBP | 2025-04-30 | 2026-04-30 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 20034 | GBP | 2025-04-30 | 2026-04-30 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 20034 | GBP | 2025-04-30 | 2026-04-30 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2024-04-30 | 2026-04-30 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-04-30 | 2025-04-30 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 25550 | GBP | 2024-04-30 | 2026-04-30 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 25550 | GBP | 2024-04-30 | 2025-04-30 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 30037 | GBP | 2024-04-30 | 2026-04-30 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 30037 | GBP | 2024-04-30 | 2025-04-30 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 61071 | GBP | 2024-04-30 | 2026-04-30 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 61071 | GBP | 2024-04-30 | 2025-04-30 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | 5484 | GBP | 2024-04-30 | 2026-04-30 | filed | yes | `uk-core:Equity` | micro-entity |
| equity | 5484 | GBP | 2024-04-30 | 2025-04-30 | filed | no | `uk-core:Equity` | micro-entity |
| net_assets | 5484 | GBP | 2024-04-30 | 2026-04-30 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 5484 | GBP | 2024-04-30 | 2025-04-30 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 31034 | GBP | 2024-04-30 | 2025-04-30 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 31034 | GBP | 2024-04-30 | 2026-04-30 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 31034 | GBP | 2024-04-30 | 2026-04-30 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 31034 | GBP | 2024-04-30 | 2025-04-30 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-04-30 | 2024-04-30 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-04-30 | 2025-04-30 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 30000 | GBP | 2023-04-30 | 2025-04-30 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 30000 | GBP | 2023-04-30 | 2024-04-30 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 36537 | GBP | 2023-04-30 | 2024-04-30 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 36537 | GBP | 2023-04-30 | 2025-04-30 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 67571 | GBP | 2023-04-30 | 2025-04-30 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 67571 | GBP | 2023-04-30 | 2024-04-30 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | 1034 | GBP | 2023-04-30 | 2024-04-30 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 1034 | GBP | 2023-04-30 | 2025-04-30 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 1034 | GBP | 2023-04-30 | 2025-04-30 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 1034 | GBP | 2023-04-30 | 2024-04-30 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 31034 | GBP | 2023-04-30 | 2024-04-30 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 31034 | GBP | 2023-04-30 | 2025-04-30 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 31034 | GBP | 2023-04-30 | 2025-04-30 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 31034 | GBP | 2023-04-30 | 2024-04-30 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2022-04-30 | 2024-04-30 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 30000 | GBP | 2022-04-30 | 2024-04-30 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 36537 | GBP | 2022-04-30 | 2024-04-30 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 67571 | GBP | 2022-04-30 | 2024-04-30 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 1034 | GBP | 2022-04-30 | 2024-04-30 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 1034 | GBP | 2022-04-30 | 2024-04-30 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 31034 | GBP | 2022-04-30 | 2024-04-30 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 31034 | GBP | 2022-04-30 | 2024-04-30 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2026-04-30: `{"superseded_document_id": "gb:05777796:doc:2x5Hh6XXTwKH-5kDYhLyVBn2RXoGvBZXa-QHNERhReo", "restatements": [{"concept": "average_employees", "period_end": "2024-04-30", "old_value": "1.0000", "new_valu`

## JSGM LTD (`gb:06213860`)

- registration: `06213860` (GB), status active, incorporated 2007-04-16
- classification: ['71121'] (sic_2007)
- records: 2 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 44 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 3 | iso4217:GBP | 2025-03-31 | 2025-12-23 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5926 | GBP | 2025-03-31 | 2025-12-23 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 102379 | GBP | 2025-03-31 | 2025-12-23 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 101504 | GBP | 2025-03-31 | 2025-12-23 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 5051 | GBP | 2025-03-31 | 2025-12-23 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 101504 | GBP | 2025-03-31 | 2025-12-23 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 96453 | GBP | 2025-03-31 | 2025-12-23 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 101504 | GBP | 2025-03-31 | 2025-12-23 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 3 | iso4217:GBP | 2024-03-31 | 2024-12-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 53717 | GBP | 2024-03-31 | 2025-12-23 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 41112 | GBP | 2024-03-31 | 2024-12-30 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 225777 | GBP | 2024-03-31 | 2024-12-30 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 211381 | GBP | 2024-03-31 | 2025-12-23 | filed | yes | `core:CurrentAssets` | micro-entity |
| depreciation_amortisation | 2993 | GBP | 2024-03-31 | 2024-12-30 | filed | yes | `core:DepreciationAmortisationImpairmentExpense` | micro-entity |
| equity | 191399 | GBP | 2024-03-31 | 2024-12-30 | filed | no | `core:Equity` | micro-entity |
| equity | 164398 | GBP | 2024-03-31 | 2025-12-23 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 6734 | GBP | 2024-03-31 | 2025-12-23 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 6734 | GBP | 2024-03-31 | 2024-12-30 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | 164398 | GBP | 2024-03-31 | 2025-12-23 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 191399 | GBP | 2024-03-31 | 2024-12-30 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 184665 | GBP | 2024-03-31 | 2024-12-30 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 157664 | GBP | 2024-03-31 | 2025-12-23 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| profit_for_period | 170156 | GBP | 2024-03-31 | 2024-12-30 | filed | yes | `core:ProfitLoss` | micro-entity |
| revenue | 255738 | GBP | 2024-03-31 | 2024-12-30 | filed | yes | `core:TurnoverRevenue` | micro-entity |
| staff_costs | 35365 | GBP | 2024-03-31 | 2024-12-30 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | micro-entity |
| tax_charge | 39912 | GBP | 2024-03-31 | 2024-12-30 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | micro-entity |
| total_assets_less_current_liabilities | 164398 | GBP | 2024-03-31 | 2025-12-23 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 191399 | GBP | 2024-03-31 | 2024-12-30 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1200 | GBP | 2023-03-31 | 2024-12-30 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 49472 | GBP | 2023-03-31 | 2024-12-30 | filed | yes | `core:CurrentAssets` | micro-entity |
| depreciation_amortisation | 3723 | GBP | 2023-03-31 | 2024-12-30 | filed | yes | `core:DepreciationAmortisationImpairmentExpense` | micro-entity |
| equity | 57251 | GBP | 2023-03-31 | 2024-12-30 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 8979 | GBP | 2023-03-31 | 2024-12-30 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 57251 | GBP | 2023-03-31 | 2024-12-30 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 48272 | GBP | 2023-03-31 | 2024-12-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| profit_for_period | 28029 | GBP | 2023-03-31 | 2024-12-30 | filed | yes | `core:ProfitLoss` | micro-entity |
| revenue | 62835 | GBP | 2023-03-31 | 2024-12-30 | filed | yes | `core:TurnoverRevenue` | micro-entity |
| staff_costs | 9668 | GBP | 2023-03-31 | 2024-12-30 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | micro-entity |
| tax_charge | 6575 | GBP | 2023-03-31 | 2024-12-30 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | micro-entity |
| total_assets_less_current_liabilities | 57251 | GBP | 2023-03-31 | 2024-12-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2025-12-23: `{"superseded_document_id": "gb:06213860:doc:OLBuwslXXMWEyrH7lZ8mys9xU5LqXzJroUuJWdjMZ3I", "restatements": [{"concept": "current_assets", "period_end": "2024-03-31", "old_value": "225777.0000", "new_va`

## UKBIZONLINE LTD (`gb:06581635`)

- registration: `06581635` (GB), status active, incorporated 2008-04-30
- classification: ['62090'] (sic_2007)
- records: 2 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 47 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | xbrli:pure | 2025-04-30 | 2026-01-22 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 35001 | GBP | 2025-04-30 | 2026-01-22 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 2998 | GBP | 2025-04-30 | 2026-01-22 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -32003 | GBP | 2025-04-30 | 2026-01-22 | filed | yes | `core:Equity` | micro-entity |
| net_assets | -32003 | GBP | 2025-04-30 | 2026-01-22 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -32003 | GBP | 2025-04-30 | 2026-01-22 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -32003 | GBP | 2025-04-30 | 2026-01-22 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2024-04-30 | 2026-01-22 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | xbrli:pure | 2024-04-30 | 2025-01-21 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 28782 | GBP | 2024-04-30 | 2025-01-21 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 28782 | GBP | 2024-04-30 | 2026-01-22 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 1533 | GBP | 2024-04-30 | 2025-01-21 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 1533 | GBP | 2024-04-30 | 2026-01-22 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -27249 | GBP | 2024-04-30 | 2026-01-22 | filed | yes | `core:Equity` | micro-entity |
| equity | -27249 | GBP | 2024-04-30 | 2025-01-21 | filed | no | `core:Equity` | micro-entity |
| net_assets | -27249 | GBP | 2024-04-30 | 2026-01-22 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | -27249 | GBP | 2024-04-30 | 2025-01-21 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -27249 | GBP | 2024-04-30 | 2025-01-21 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -27249 | GBP | 2024-04-30 | 2026-01-22 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -27249 | GBP | 2024-04-30 | 2025-01-21 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -27249 | GBP | 2024-04-30 | 2026-01-22 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2023-04-30 | 2025-01-21 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | xbrli:pure | 2023-04-30 | 2024-01-26 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 27684 | GBP | 2023-04-30 | 2024-01-26 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 27684 | GBP | 2023-04-30 | 2025-01-21 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 1615 | GBP | 2023-04-30 | 2024-01-26 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 1615 | GBP | 2023-04-30 | 2025-01-21 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -26069 | GBP | 2023-04-30 | 2025-01-21 | filed | yes | `core:Equity` | micro-entity |
| equity | -26069 | GBP | 2023-04-30 | 2024-01-26 | filed | no | `core:Equity` | micro-entity |
| net_assets | -26069 | GBP | 2023-04-30 | 2024-01-26 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | -26069 | GBP | 2023-04-30 | 2025-01-21 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -26069 | GBP | 2023-04-30 | 2024-01-26 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -26069 | GBP | 2023-04-30 | 2025-01-21 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -26069 | GBP | 2023-04-30 | 2025-01-21 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -26069 | GBP | 2023-04-30 | 2024-01-26 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2022-04-30 | 2024-01-26 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 30619 | GBP | 2022-04-30 | 2024-01-26 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 1999 | GBP | 2022-04-30 | 2024-01-26 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -28620 | GBP | 2022-04-30 | 2024-01-26 | filed | yes | `core:Equity` | micro-entity |
| net_assets | -28620 | GBP | 2022-04-30 | 2024-01-26 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -28620 | GBP | 2022-04-30 | 2024-01-26 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -28620 | GBP | 2022-04-30 | 2024-01-26 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._
