# Ingest spot-check

- database: `data/engine.db`
- latest run: `20261122T092730Z-b03886ba`
- companies in store: 57800; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## MICROWARE 2000 LIMITED (`gb:02911290`)

- registration: `02911290` (GB), status active, incorporated 1994-03-22
- classification: ['62020'] (sic_2007)
- records: 5 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 72 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | iso4217:GBP | 2025-03-31 | 2025-12-27 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2025-03-31 | 2025-12-27 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2025-03-31 | 2025-12-27 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 100 | GBP | 2025-03-31 | 2025-12-27 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 101 | GBP | 2025-03-31 | 2025-12-27 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 1 | GBP | 2025-03-31 | 2025-12-27 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 101 | GBP | 2025-03-31 | 2025-12-27 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 100 | GBP | 2025-03-31 | 2025-12-27 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 101 | GBP | 2025-03-31 | 2025-12-27 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-03-31 | 2025-12-27 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-03-31 | 2024-12-23 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2024-03-31 | 2025-12-27 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2024-03-31 | 2025-12-27 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 100 | GBP | 2024-03-31 | 2025-12-27 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 100 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | 101 | GBP | 2024-03-31 | 2025-12-27 | filed | yes | `uk-core:Equity` | micro-entity |
| equity | 101 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `uk-core:Equity` | micro-entity |
| fixed_assets | 1 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 1 | GBP | 2024-03-31 | 2025-12-27 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 101 | GBP | 2024-03-31 | 2025-12-27 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 101 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 100 | GBP | 2024-03-31 | 2025-12-27 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 100 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 101 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 101 | GBP | 2024-03-31 | 2025-12-27 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-03-31 | 2023-12-29 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-03-31 | 2024-12-23 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2023-03-31 | 2023-12-29 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2023-03-31 | 2023-12-29 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 100 | GBP | 2023-03-31 | 2023-12-29 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 100 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 101 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `uk-core:Equity` | micro-entity |
| equity | 101 | GBP | 2023-03-31 | 2023-12-29 | filed | no | `uk-core:Equity` | micro-entity |
| fixed_assets | 1 | GBP | 2023-03-31 | 2023-12-29 | filed | no | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 1 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 101 | GBP | 2023-03-31 | 2023-12-29 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 101 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 100 | GBP | 2023-03-31 | 2023-12-29 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 100 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 101 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 101 | GBP | 2023-03-31 | 2023-12-29 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2022-03-31 | 2023-12-29 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2022-03-31 | 2023-12-29 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2022-03-31 | 2023-12-29 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 100 | GBP | 2022-03-31 | 2023-12-29 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 101 | GBP | 2022-03-31 | 2023-12-29 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 1 | GBP | 2022-03-31 | 2023-12-29 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 101 | GBP | 2022-03-31 | 2023-12-29 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 100 | GBP | 2022-03-31 | 2023-12-29 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 101 | GBP | 2022-03-31 | 2023-12-29 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## TAPIT LIMITED (`gb:03615694`)

- registration: `03615694` (GB), status active, incorporated 1998-08-14
- classification: ['62090'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 70 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-09-30 | 2026-02-11 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 110891 | GBP | 2025-09-30 | 2026-02-11 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| equity | 76492 | GBP | 2025-09-30 | 2026-02-11 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 76490 | GBP | 2025-09-30 | 2026-02-11 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2025-09-30 | 2026-02-11 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | 76491 | GBP | 2025-09-30 | 2026-02-11 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 76492 | GBP | 2025-09-30 | 2026-02-11 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-09-30 | 2026-02-11 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-09-30 | 2025-02-17 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 105803 | GBP | 2024-09-30 | 2026-02-11 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 105803 | GBP | 2024-09-30 | 2025-02-17 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| equity | 74891 | GBP | 2024-09-30 | 2026-02-11 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 74889 | GBP | 2024-09-30 | 2025-02-17 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 74891 | GBP | 2024-09-30 | 2025-02-17 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-09-30 | 2025-02-17 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-09-30 | 2026-02-11 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 74889 | GBP | 2024-09-30 | 2026-02-11 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | 74890 | GBP | 2024-09-30 | 2025-02-17 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 74890 | GBP | 2024-09-30 | 2026-02-11 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 74891 | GBP | 2024-09-30 | 2025-02-17 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 74891 | GBP | 2024-09-30 | 2026-02-11 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 2 | xbrli:pure | 2023-09-30 | 2024-02-16 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-09-30 | 2025-02-17 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 107377 | GBP | 2023-09-30 | 2025-02-17 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 107377 | GBP | 2023-09-30 | 2024-02-16 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 78460 | GBP | 2023-09-30 | 2024-02-16 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 78460 | GBP | 2023-09-30 | 2025-02-17 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 78458 | GBP | 2023-09-30 | 2025-02-17 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-09-30 | 2025-02-17 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 2 | GBP | 2023-09-30 | 2024-02-16 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 78458 | GBP | 2023-09-30 | 2024-02-16 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | 78459 | GBP | 2023-09-30 | 2025-02-17 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 78459 | GBP | 2023-09-30 | 2024-02-16 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 78460 | GBP | 2023-09-30 | 2024-02-16 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 78460 | GBP | 2023-09-30 | 2025-02-17 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 2 | xbrli:pure | 2022-09-30 | 2024-02-16 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 108176 | GBP | 2022-09-30 | 2024-02-16 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 83590 | GBP | 2022-09-30 | 2024-02-16 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 2 | GBP | 2022-09-30 | 2024-02-16 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 83592 | GBP | 2022-09-30 | 2024-02-16 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 83591 | GBP | 2022-09-30 | 2024-02-16 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 83592 | GBP | 2022-09-30 | 2024-02-16 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## ALWAYS ON MOBILE LIMITED (`gb:04253593`)

- registration: `04253593` (GB), status active, incorporated 2001-07-17
- classification: ['62012'] (sic_2007)
- records: 6 officers, 3 beneficial owners, 0 ownership statements, 1 security interests, 88 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 4 | xbrli:pure | 2024-11-30 | 2025-08-29 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 11137 | GBP | 2024-11-30 | 2025-08-29 | filed | yes | `ns5:CashBankOnHand` | unaudited-abridged |
| current_assets | 116791 | GBP | 2024-11-30 | 2025-08-29 | filed | yes | `ns5:CurrentAssets` | unaudited-abridged |
| debtors | 105654 | GBP | 2024-11-30 | 2025-08-29 | filed | yes | `ns5:Debtors` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 108 | GBP | 2024-11-30 | 2025-08-29 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity | 426 | GBP | 2024-11-30 | 2025-08-29 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 318 | GBP | 2024-11-30 | 2025-08-29 | filed | yes | `ns5:Equity` | unaudited-abridged |
| net_assets | 426 | GBP | 2024-11-30 | 2025-08-29 | filed | yes | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 1467 | GBP | 2024-11-30 | 2025-08-29 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 9012 | GBP | 2024-11-30 | 2025-08-29 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 4 | xbrli:pure | 2023-11-30 | 2024-09-30 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| average_employees | 4 | xbrli:pure | 2023-11-30 | 2025-08-29 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 68040 | GBP | 2023-11-30 | 2024-09-30 | filed | no | `ns5:CashBankOnHand` | unaudited-abridged |
| cash | 68040 | GBP | 2023-11-30 | 2025-08-29 | filed | yes | `ns5:CashBankOnHand` | unaudited-abridged |
| current_assets | 157136 | GBP | 2023-11-30 | 2025-08-29 | filed | yes | `ns5:CurrentAssets` | unaudited-abridged |
| current_assets | 157136 | GBP | 2023-11-30 | 2024-09-30 | filed | no | `ns5:CurrentAssets` | unaudited-abridged |
| debtors | 89096 | GBP | 2023-11-30 | 2024-09-30 | filed | no | `ns5:Debtors` | unaudited-abridged |
| debtors | 89096 | GBP | 2023-11-30 | 2025-08-29 | filed | yes | `ns5:Debtors` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 102532 | GBP | 2023-11-30 | 2025-08-29 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 102532 | GBP | 2023-11-30 | 2024-09-30 | filed | no | `ns5:Equity` | unaudited-abridged |
| equity | 102640 | GBP | 2023-11-30 | 2024-09-30 | filed | no | `ns5:Equity` | unaudited-abridged |
| equity | 102640 | GBP | 2023-11-30 | 2025-08-29 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 108 | GBP | 2023-11-30 | 2025-08-29 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 108 | GBP | 2023-11-30 | 2024-09-30 | filed | no | `ns5:Equity` | unaudited-abridged |
| net_assets | 102640 | GBP | 2023-11-30 | 2025-08-29 | filed | yes | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_assets | 102640 | GBP | 2023-11-30 | 2024-09-30 | filed | no | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 94548 | GBP | 2023-11-30 | 2024-09-30 | filed | no | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 94548 | GBP | 2023-11-30 | 2025-08-29 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 104538 | GBP | 2023-11-30 | 2025-08-29 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 104538 | GBP | 2023-11-30 | 2024-09-30 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 4 | xbrli:pure | 2022-11-30 | 2024-09-30 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 4 | xbrli:pure | 2022-11-30 | 2023-08-31 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 175793 | GBP | 2022-11-30 | 2024-09-30 | filed | yes | `ns5:CashBankOnHand` | unaudited-abridged |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 175793 | GBP | 2022-11-30 | 2023-08-31 | filed | yes | `ns5:CashBankOnHand` | unaudited-abridged |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 271953 | GBP | 2022-11-30 | 2023-08-31 | filed | yes | `ns5:CurrentAssets` | unaudited-abridged |
| current_assets | 271953 | GBP | 2022-11-30 | 2024-09-30 | filed | yes | `ns5:CurrentAssets` | unaudited-abridged |
| debtors | 96160 | GBP | 2022-11-30 | 2024-09-30 | filed | yes | `ns5:Debtors` | unaudited-abridged |
| debtors `{'OriginalRevisedDataDimension': 'Original'}` | 96160 | GBP | 2022-11-30 | 2023-08-31 | filed | yes | `ns5:Debtors` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 157251 | GBP | 2022-11-30 | 2024-09-30 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 100 | GBP | 2022-11-30 | 2023-08-31 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 157251 | GBP | 2022-11-30 | 2023-08-31 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity | 157351 | GBP | 2022-11-30 | 2024-09-30 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 157351 | GBP | 2022-11-30 | 2023-08-31 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2022-11-30 | 2024-09-30 | filed | yes | `ns5:Equity` | unaudited-abridged |
| net_assets `{'OriginalRevisedDataDimension': 'Original'}` | 157351 | GBP | 2022-11-30 | 2023-08-31 | filed | yes | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_assets | 157351 | GBP | 2022-11-30 | 2024-09-30 | filed | yes | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 150211 | GBP | 2022-11-30 | 2023-08-31 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 150211 | GBP | 2022-11-30 | 2024-09-30 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 159731 | GBP | 2022-11-30 | 2024-09-30 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 159731 | GBP | 2022-11-30 | 2023-08-31 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 4 | xbrli:pure | 2021-11-30 | 2023-08-31 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 176213 | GBP | 2021-11-30 | 2023-08-31 | filed | yes | `ns5:CashBankOnHand` | unaudited-abridged |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 290832 | GBP | 2021-11-30 | 2023-08-31 | filed | yes | `ns5:CurrentAssets` | unaudited-abridged |
| debtors `{'OriginalRevisedDataDimension': 'Original'}` | 114619 | GBP | 2021-11-30 | 2023-08-31 | filed | yes | `ns5:Debtors` | unaudited-abridged |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 182985 | GBP | 2021-11-30 | 2023-08-31 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 1 | GBP | 2021-11-30 | 2023-08-31 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 182986 | GBP | 2021-11-30 | 2023-08-31 | filed | yes | `ns5:Equity` | unaudited-abridged |
| net_assets `{'OriginalRevisedDataDimension': 'Original'}` | 182986 | GBP | 2021-11-30 | 2023-08-31 | filed | yes | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 174405 | GBP | 2021-11-30 | 2023-08-31 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 184999 | GBP | 2021-11-30 | 2023-08-31 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |

_No coverage facts for the latest run._

## MARTIN SZCZERBICKI ASSOCIATES LIMITED (`gb:04916345`)

- registration: `04916345` (GB), status active, incorporated 2003-09-30
- classification: ['71111'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 57 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-09-30 | 2026-06-29 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 2686 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 6419 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 3733 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 618 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 617 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | 214 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 618 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-09-30 | 2025-06-27 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-09-30 | 2026-06-29 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 13176 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 13176 | GBP | 2024-09-30 | 2025-06-27 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 15328 | GBP | 2024-09-30 | 2025-06-27 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 15328 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 2152 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 2152 | GBP | 2024-09-30 | 2025-06-27 | filed | no | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 9705 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 9706 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 9706 | GBP | 2024-09-30 | 2025-06-27 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 9705 | GBP | 2024-09-30 | 2025-06-27 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2024-09-30 | 2025-06-27 | filed | no | `ns5:Equity` | total-exemption-full |
| net_current_assets | 9625 | GBP | 2024-09-30 | 2025-06-27 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 9625 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 9706 | GBP | 2024-09-30 | 2025-06-27 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 9706 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-09-30 | 2025-06-27 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-09-30 | 2024-06-27 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 316 | GBP | 2023-09-30 | 2025-06-27 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 316 | GBP | 2023-09-30 | 2024-06-27 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 316 | GBP | 2023-09-30 | 2025-06-27 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 0 | GBP | 2023-09-30 | 2025-06-27 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | -5604 | GBP | 2023-09-30 | 2024-06-27 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -5605 | GBP | 2023-09-30 | 2025-06-27 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2023-09-30 | 2024-06-27 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | -5604 | GBP | 2023-09-30 | 2025-06-27 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -5605 | GBP | 2023-09-30 | 2024-06-27 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2023-09-30 | 2025-06-27 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | -5699 | GBP | 2023-09-30 | 2025-06-27 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -5699 | GBP | 2023-09-30 | 2024-06-27 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -5604 | GBP | 2023-09-30 | 2024-06-27 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -5604 | GBP | 2023-09-30 | 2025-06-27 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2022-09-30 | 2024-06-27 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 8129 | GBP | 2022-09-30 | 2024-06-27 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 600 | GBP | 2022-09-30 | 2024-06-27 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2022-09-30 | 2024-06-27 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 601 | GBP | 2022-09-30 | 2024-06-27 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | 469 | GBP | 2022-09-30 | 2024-06-27 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 601 | GBP | 2022-09-30 | 2024-06-27 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## MARAD LIMITED (`gb:05557808`)

- registration: `05557808` (GB), status active, incorporated 2005-09-08
- classification: ['71122'] (sic_2007)
- records: 5 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 53 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-03-31 | 2026-03-27 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 7799 | GBP | 2025-03-31 | 2026-03-27 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 12509 | GBP | 2025-03-31 | 2026-03-27 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 4710 | GBP | 2025-03-31 | 2026-03-27 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | -1478 | GBP | 2025-03-31 | 2026-03-27 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -1578 | GBP | 2025-03-31 | 2026-03-27 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-03-31 | 2026-03-27 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | -2740 | GBP | 2025-03-31 | 2026-03-27 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -1478 | GBP | 2025-03-31 | 2026-03-27 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-03-31 | 2025-03-31 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-03-31 | 2026-03-27 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 3624 | GBP | 2024-03-31 | 2025-03-31 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 3624 | GBP | 2024-03-31 | 2026-03-27 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 31690 | GBP | 2024-03-31 | 2026-03-27 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 31690 | GBP | 2024-03-31 | 2025-03-31 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 28066 | GBP | 2024-03-31 | 2026-03-27 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 28066 | GBP | 2024-03-31 | 2025-03-31 | filed | no | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-03-31 | 2025-03-31 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 16671 | GBP | 2024-03-31 | 2026-03-27 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 16771 | GBP | 2024-03-31 | 2026-03-27 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 16771 | GBP | 2024-03-31 | 2025-03-31 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 16671 | GBP | 2024-03-31 | 2025-03-31 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-03-31 | 2026-03-27 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | 16499 | GBP | 2024-03-31 | 2025-03-31 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 16499 | GBP | 2024-03-31 | 2026-03-27 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 16771 | GBP | 2024-03-31 | 2026-03-27 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 16771 | GBP | 2024-03-31 | 2025-03-31 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-03-31 | 2025-03-31 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 25495 | GBP | 2023-03-31 | 2025-03-31 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 108476 | GBP | 2023-03-31 | 2025-03-31 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 82981 | GBP | 2023-03-31 | 2025-03-31 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 71195 | GBP | 2023-03-31 | 2025-03-31 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-03-31 | 2025-03-31 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 71295 | GBP | 2023-03-31 | 2025-03-31 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | 70777 | GBP | 2023-03-31 | 2025-03-31 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 71295 | GBP | 2023-03-31 | 2025-03-31 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## SINTHETTIKS LTD (`gb:06161510`)

- registration: `06161510` (GB), status active, incorporated 2007-03-15
- classification: ['62020'] (sic_2007)
- records: 2 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 52 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-03-31 | 2025-12-30 | filed | yes | `uk-frs102:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `uk-frs102:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 46783 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `uk-frs102:Creditors` | micro-entity |
| current_assets | 112996 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `uk-frs102:CurrentAssets` | micro-entity |
| equity | 68289 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `uk-frs102:Equity` | micro-entity |
| fixed_assets | 2076 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `uk-frs102:FixedAssets` | micro-entity |
| net_assets | 68289 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `uk-frs102:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 66213 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `uk-frs102:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 68289 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `uk-frs102:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-03-31 | 2024-12-16 | filed | yes | `uk-frs102:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2024-03-31 | 2024-12-16 | filed | no | `uk-frs102:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `uk-frs102:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 20623 | GBP | 2024-03-31 | 2024-12-16 | filed | no | `uk-frs102:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 20623 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `uk-frs102:Creditors` | micro-entity |
| current_assets | 84537 | GBP | 2024-03-31 | 2024-12-16 | filed | no | `uk-frs102:CurrentAssets` | micro-entity |
| current_assets | 84537 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `uk-frs102:CurrentAssets` | micro-entity |
| equity | 66742 | GBP | 2024-03-31 | 2024-12-16 | filed | no | `uk-frs102:Equity` | micro-entity |
| equity | 66742 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `uk-frs102:Equity` | micro-entity |
| fixed_assets | 2828 | GBP | 2024-03-31 | 2024-12-16 | filed | no | `uk-frs102:FixedAssets` | micro-entity |
| fixed_assets | 2828 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `uk-frs102:FixedAssets` | micro-entity |
| net_assets | 66742 | GBP | 2024-03-31 | 2024-12-16 | filed | no | `uk-frs102:NetAssetsLiabilities` | micro-entity |
| net_assets | 66742 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `uk-frs102:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 63914 | GBP | 2024-03-31 | 2024-12-16 | filed | no | `uk-frs102:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 63914 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `uk-frs102:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 66742 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `uk-frs102:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 66742 | GBP | 2024-03-31 | 2024-12-16 | filed | no | `uk-frs102:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-03-31 | 2023-10-28 | filed | yes | `uk-frs102:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2023-03-31 | 2023-10-28 | filed | no | `uk-frs102:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2023-03-31 | 2024-12-16 | filed | yes | `uk-frs102:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | -8 | GBP | 2023-03-31 | 2023-10-28 | filed | no | `uk-frs102:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | -8 | GBP | 2023-03-31 | 2024-12-16 | filed | yes | `uk-frs102:Creditors` | micro-entity |
| current_assets | 42760 | GBP | 2023-03-31 | 2024-12-16 | filed | yes | `uk-frs102:CurrentAssets` | micro-entity |
| current_assets | 42760 | GBP | 2023-03-31 | 2023-10-28 | filed | no | `uk-frs102:CurrentAssets` | micro-entity |
| equity | 43831 | GBP | 2023-03-31 | 2024-12-16 | filed | yes | `uk-frs102:Equity` | micro-entity |
| equity | 43831 | GBP | 2023-03-31 | 2023-10-28 | filed | no | `uk-frs102:Equity` | micro-entity |
| fixed_assets | 1063 | GBP | 2023-03-31 | 2023-10-28 | filed | no | `uk-frs102:FixedAssets` | micro-entity |
| fixed_assets | 1063 | GBP | 2023-03-31 | 2024-12-16 | filed | yes | `uk-frs102:FixedAssets` | micro-entity |
| net_assets | 43831 | GBP | 2023-03-31 | 2024-12-16 | filed | yes | `uk-frs102:NetAssetsLiabilities` | micro-entity |
| net_assets | 43831 | GBP | 2023-03-31 | 2023-10-28 | filed | no | `uk-frs102:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 42768 | GBP | 2023-03-31 | 2024-12-16 | filed | yes | `uk-frs102:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 42768 | GBP | 2023-03-31 | 2023-10-28 | filed | no | `uk-frs102:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 43831 | GBP | 2023-03-31 | 2024-12-16 | filed | yes | `uk-frs102:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 43831 | GBP | 2023-03-31 | 2023-10-28 | filed | no | `uk-frs102:TotalAssetsLessCurrentLiabilities` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2022-03-31 | 2023-10-28 | filed | yes | `uk-frs102:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 8100 | GBP | 2022-03-31 | 2023-10-28 | filed | yes | `uk-frs102:Creditors` | micro-entity |
| current_assets | 53407 | GBP | 2022-03-31 | 2023-10-28 | filed | yes | `uk-frs102:CurrentAssets` | micro-entity |
| equity | 47213 | GBP | 2022-03-31 | 2023-10-28 | filed | yes | `uk-frs102:Equity` | micro-entity |
| fixed_assets | 1906 | GBP | 2022-03-31 | 2023-10-28 | filed | yes | `uk-frs102:FixedAssets` | micro-entity |
| net_assets | 47213 | GBP | 2022-03-31 | 2023-10-28 | filed | yes | `uk-frs102:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 45307 | GBP | 2022-03-31 | 2023-10-28 | filed | yes | `uk-frs102:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 47213 | GBP | 2022-03-31 | 2023-10-28 | filed | yes | `uk-frs102:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## SCHOOLS DATA SERVICES LTD (`gb:06620436`)

- registration: `06620436` (GB), status active, incorporated 2008-06-16
- classification: ['62090'] (sic_2007)
- records: 3 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 54 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 4 | iso4217:GBP | 2026-06-30 | 2026-11-05 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 9106 | GBP | 2026-06-30 | 2026-11-05 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 67812 | GBP | 2026-06-30 | 2026-11-05 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 64596 | GBP | 2026-06-30 | 2026-11-05 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 7854 | GBP | 2026-06-30 | 2026-11-05 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 64596 | GBP | 2026-06-30 | 2026-11-05 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 58706 | GBP | 2026-06-30 | 2026-11-05 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 66560 | GBP | 2026-06-30 | 2026-11-05 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 3 | iso4217:GBP | 2025-06-30 | 2026-02-10 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 3 | iso4217:GBP | 2025-06-30 | 2026-11-05 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 3475 | GBP | 2025-06-30 | 2026-02-10 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 3475 | GBP | 2025-06-30 | 2026-11-05 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 71878 | GBP | 2025-06-30 | 2026-02-10 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 71878 | GBP | 2025-06-30 | 2026-11-05 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 70851 | GBP | 2025-06-30 | 2026-11-05 | filed | yes | `uk-core:Equity` | micro-entity |
| equity | 70851 | GBP | 2025-06-30 | 2026-02-10 | filed | no | `uk-core:Equity` | micro-entity |
| fixed_assets | 4703 | GBP | 2025-06-30 | 2026-11-05 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 4703 | GBP | 2025-06-30 | 2026-02-10 | filed | no | `uk-core:FixedAssets` | micro-entity |
| net_assets | 70851 | GBP | 2025-06-30 | 2026-02-10 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 70851 | GBP | 2025-06-30 | 2026-11-05 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 68403 | GBP | 2025-06-30 | 2026-11-05 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 68403 | GBP | 2025-06-30 | 2026-02-10 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 73106 | GBP | 2025-06-30 | 2026-11-05 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 73106 | GBP | 2025-06-30 | 2026-02-10 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 3 | iso4217:GBP | 2024-06-30 | 2024-10-25 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 3 | iso4217:GBP | 2024-06-30 | 2026-02-10 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 21928 | GBP | 2024-06-30 | 2026-02-10 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 21928 | GBP | 2024-06-30 | 2024-10-25 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 51496 | GBP | 2024-06-30 | 2026-02-10 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 51496 | GBP | 2024-06-30 | 2024-10-25 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | 34505 | GBP | 2024-06-30 | 2026-02-10 | filed | yes | `uk-core:Equity` | micro-entity |
| equity | 34505 | GBP | 2024-06-30 | 2024-10-25 | filed | no | `uk-core:Equity` | micro-entity |
| fixed_assets | 6095 | GBP | 2024-06-30 | 2026-02-10 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 6095 | GBP | 2024-06-30 | 2024-10-25 | filed | no | `uk-core:FixedAssets` | micro-entity |
| net_assets | 34505 | GBP | 2024-06-30 | 2026-02-10 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 34505 | GBP | 2024-06-30 | 2024-10-25 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 29568 | GBP | 2024-06-30 | 2024-10-25 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 29568 | GBP | 2024-06-30 | 2026-02-10 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 35663 | GBP | 2024-06-30 | 2024-10-25 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 35663 | GBP | 2024-06-30 | 2026-02-10 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 3 | iso4217:GBP | 2023-06-30 | 2024-10-25 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 17185 | GBP | 2023-06-30 | 2024-10-25 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 28310 | GBP | 2023-06-30 | 2024-10-25 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 15728 | GBP | 2023-06-30 | 2024-10-25 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 5682 | GBP | 2023-06-30 | 2024-10-25 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 15728 | GBP | 2023-06-30 | 2024-10-25 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 11125 | GBP | 2023-06-30 | 2024-10-25 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 16807 | GBP | 2023-06-30 | 2024-10-25 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## EXPLORE AND CREATE LIMITED (`gb:07046637`)

- registration: `07046637` (GB), status active, incorporated 2009-10-16
- classification: ['62011', '62012'] (sic_2007)
- records: 1 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 53 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | xbrli:pure | 2025-10-31 | 2026-07-10 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 146.47 | GBP | 2025-10-31 | 2026-07-10 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | -753.53 | GBP | 2025-10-31 | 2026-07-10 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | -753.53 | GBP | 2025-10-31 | 2026-07-10 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -753.53 | GBP | 2025-10-31 | 2026-07-10 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -753.53 | GBP | 2025-10-31 | 2026-07-10 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2024-10-31 | 2025-06-23 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | xbrli:pure | 2024-10-31 | 2026-07-10 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 102.45 | GBP | 2024-10-31 | 2025-06-23 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 102.45 | GBP | 2024-10-31 | 2026-07-10 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | -497.55 | GBP | 2024-10-31 | 2025-06-23 | filed | no | `uk-core:Equity` | micro-entity |
| equity | -497.55 | GBP | 2024-10-31 | 2026-07-10 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | -497.55 | GBP | 2024-10-31 | 2025-06-23 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | -497.55 | GBP | 2024-10-31 | 2026-07-10 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -497.55 | GBP | 2024-10-31 | 2026-07-10 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -497.55 | GBP | 2024-10-31 | 2025-06-23 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -497.55 | GBP | 2024-10-31 | 2025-06-23 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -497.55 | GBP | 2024-10-31 | 2026-07-10 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2023-10-31 | 2024-07-02 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | xbrli:pure | 2023-10-31 | 2025-06-23 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 265.31 | GBP | 2023-10-31 | 2024-07-02 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 265.31 | GBP | 2023-10-31 | 2025-06-23 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | -134.69 | GBP | 2023-10-31 | 2025-06-23 | filed | yes | `uk-core:Equity` | micro-entity |
| equity | -134.69 | GBP | 2023-10-31 | 2024-07-02 | filed | no | `uk-core:Equity` | micro-entity |
| net_assets | -134.69 | GBP | 2023-10-31 | 2024-07-02 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | -134.69 | GBP | 2023-10-31 | 2025-06-23 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -134.69 | GBP | 2023-10-31 | 2024-07-02 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -134.69 | GBP | 2023-10-31 | 2025-06-23 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -134.69 | GBP | 2023-10-31 | 2025-06-23 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -134.69 | GBP | 2023-10-31 | 2024-07-02 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2022-10-31 | 2024-07-02 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 395.59 | GBP | 2022-10-31 | 2024-07-02 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 195.59 | GBP | 2022-10-31 | 2024-07-02 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 195.59 | GBP | 2022-10-31 | 2024-07-02 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 195.59 | GBP | 2022-10-31 | 2024-07-02 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 195.59 | GBP | 2022-10-31 | 2024-07-02 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## MPH GLOBAL LIMITED (`gb:07418069`)

- registration: `07418069` (GB), status active, incorporated 2010-10-25
- classification: ['62090'] (sic_2007)
- records: 1 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 37 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-03-31 | 2025-10-24 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 579 | GBP | 2025-03-31 | 2025-10-24 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 12504 | GBP | 2025-03-31 | 2025-10-24 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 11925 | GBP | 2025-03-31 | 2025-10-24 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -12260 | GBP | 2025-03-31 | 2025-10-24 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-03-31 | 2025-10-24 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 163 | GBP | 2025-03-31 | 2025-10-24 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | -12160 | GBP | 2025-03-31 | 2025-10-24 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -5522 | GBP | 2025-03-31 | 2025-10-24 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -5359 | GBP | 2025-03-31 | 2025-10-24 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-03-31 | 2025-10-24 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-03-31 | 2024-09-26 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 829 | GBP | 2024-03-31 | 2024-09-26 | filed | no | `frs-core:CashBankOnHand` | total-exemption-full |
| cash | 829 | GBP | 2024-03-31 | 2025-10-24 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 9176 | GBP | 2024-03-31 | 2025-10-24 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| current_assets | 9176 | GBP | 2024-03-31 | 2024-09-26 | filed | no | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 8347 | GBP | 2024-03-31 | 2024-09-26 | filed | no | `frs-core:Debtors` | total-exemption-full |
| debtors | 8347 | GBP | 2024-03-31 | 2025-10-24 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-03-31 | 2025-10-24 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -12725 | GBP | 2024-03-31 | 2025-10-24 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -12725 | GBP | 2024-03-31 | 2024-09-26 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-03-31 | 2024-09-26 | filed | no | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 218 | GBP | 2024-03-31 | 2025-10-24 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| fixed_assets | 218 | GBP | 2024-03-31 | 2024-09-26 | filed | no | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | -12625 | GBP | 2024-03-31 | 2024-09-26 | filed | no | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | -12625 | GBP | 2024-03-31 | 2025-10-24 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -4512 | GBP | 2024-03-31 | 2024-09-26 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -4512 | GBP | 2024-03-31 | 2025-10-24 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -4294 | GBP | 2024-03-31 | 2024-09-26 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -4294 | GBP | 2024-03-31 | 2025-10-24 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-03-31 | 2023-11-06 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-03-31 | 2024-09-26 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 443 | GBP | 2023-03-31 | 2024-09-26 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| cash | 443 | GBP | 2023-03-31 | 2023-11-06 | filed | no | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 4470 | GBP | 2023-03-31 | 2024-09-26 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| current_assets | 4470 | GBP | 2023-03-31 | 2023-11-06 | filed | no | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 4027 | GBP | 2023-03-31 | 2024-09-26 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| debtors | 4027 | GBP | 2023-03-31 | 2023-11-06 | filed | no | `frs-core:Debtors` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -15763 | GBP | 2023-03-31 | 2023-11-06 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -15763 | GBP | 2023-03-31 | 2024-09-26 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-03-31 | 2024-09-26 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-03-31 | 2023-11-06 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 221 | GBP | 2023-03-31 | 2023-11-06 | filed | no | `frs-core:FixedAssets` | total-exemption-full |
| fixed_assets | 221 | GBP | 2023-03-31 | 2024-09-26 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | -15663 | GBP | 2023-03-31 | 2023-11-06 | filed | no | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | -15663 | GBP | 2023-03-31 | 2024-09-26 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -6061 | GBP | 2023-03-31 | 2023-11-06 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -6061 | GBP | 2023-03-31 | 2024-09-26 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -5840 | GBP | 2023-03-31 | 2024-09-26 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -5840 | GBP | 2023-03-31 | 2023-11-06 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2022-03-31 | 2023-11-06 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 13172 | GBP | 2022-03-31 | 2023-11-06 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 13645 | GBP | 2022-03-31 | 2023-11-06 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 473 | GBP | 2022-03-31 | 2023-11-06 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2022-03-31 | 2023-11-06 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -13361 | GBP | 2022-03-31 | 2023-11-06 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 354 | GBP | 2022-03-31 | 2023-11-06 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | -13261 | GBP | 2022-03-31 | 2023-11-06 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -2408 | GBP | 2022-03-31 | 2023-11-06 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -2054 | GBP | 2022-03-31 | 2023-11-06 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._
