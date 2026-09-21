# Ingest spot-check

- database: `data/engine.db`
- latest run: `20260921T074300Z-4940e9ad`
- companies in store: 9000; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## NOTTS. & DERBY CASH REGISTERS LIMITED (`gb:01572686`)

- registration: `01572686` (GB), status active, incorporated 1981-07-06
- classification: ['33140', '46690', '62090'] (sic_2007)
- records: 3 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 99 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 5 | xbrli:pure | 2025-08-31 | 2026-03-10 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 10705 | GBP | 2025-08-31 | 2026-03-10 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 94068 | GBP | 2025-08-31 | 2026-03-10 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 67363 | GBP | 2025-08-31 | 2026-03-10 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 3163 | GBP | 2025-08-31 | 2026-03-10 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 67363 | GBP | 2025-08-31 | 2026-03-10 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 85203 | GBP | 2025-08-31 | 2026-03-10 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 88366 | GBP | 2025-08-31 | 2026-03-10 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 5 | xbrli:pure | 2024-08-31 | 2025-05-20 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 5 | xbrli:pure | 2024-08-31 | 2026-03-10 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 8651 | GBP | 2024-08-31 | 2025-05-20 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 8651 | GBP | 2024-08-31 | 2026-03-10 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 106751 | GBP | 2024-08-31 | 2026-03-10 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 106751 | GBP | 2024-08-31 | 2025-05-20 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 82313 | GBP | 2024-08-31 | 2026-03-10 | filed | yes | `core:Equity` | micro-entity |
| equity | 82313 | GBP | 2024-08-31 | 2025-05-20 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 3326 | GBP | 2024-08-31 | 2026-03-10 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 3326 | GBP | 2024-08-31 | 2025-05-20 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | 82313 | GBP | 2024-08-31 | 2026-03-10 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 82313 | GBP | 2024-08-31 | 2025-05-20 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 100317 | GBP | 2024-08-31 | 2026-03-10 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 100317 | GBP | 2024-08-31 | 2025-05-20 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 103643 | GBP | 2024-08-31 | 2025-05-20 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 103643 | GBP | 2024-08-31 | 2026-03-10 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 5 | xbrli:pure | 2023-08-31 | 2025-05-20 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 5 | xbrli:pure | 2023-08-31 | 2024-05-02 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 24721 | GBP | 2023-08-31 | 2025-05-20 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 24721 | GBP | 2023-08-31 | 2024-05-02 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 142228 | GBP | 2023-08-31 | 2025-05-20 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 142228 | GBP | 2023-08-31 | 2024-05-02 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 101324 | GBP | 2023-08-31 | 2024-05-02 | filed | no | `core:Equity` | micro-entity |
| equity | 101324 | GBP | 2023-08-31 | 2025-05-20 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 4485 | GBP | 2023-08-31 | 2025-05-20 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 4485 | GBP | 2023-08-31 | 2024-05-02 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | 101324 | GBP | 2023-08-31 | 2025-05-20 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 101324 | GBP | 2023-08-31 | 2024-05-02 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 119234 | GBP | 2023-08-31 | 2024-05-02 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 119234 | GBP | 2023-08-31 | 2025-05-20 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 123719 | GBP | 2023-08-31 | 2024-05-02 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 123719 | GBP | 2023-08-31 | 2025-05-20 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 4 | xbrli:pure | 2022-08-31 | 2024-05-02 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 15768 | GBP | 2022-08-31 | 2024-05-02 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 111476 | GBP | 2022-08-31 | 2024-05-02 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 82307 | GBP | 2022-08-31 | 2024-05-02 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 5249 | GBP | 2022-08-31 | 2024-05-02 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 82307 | GBP | 2022-08-31 | 2024-05-02 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 97100 | GBP | 2022-08-31 | 2024-05-02 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 102349 | GBP | 2022-08-31 | 2024-05-02 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## PAUL EVANS (DESIGN) ASSOCIATES LIMITED (`gb:01972371`)

- registration: `01972371` (GB), status active, incorporated 1985-12-18
- classification: ['71111'] (sic_2007)
- records: 6 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 95 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-06-30 | 2026-03-26 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 27047 | GBP | 2025-06-30 | 2026-03-26 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 4225 | GBP | 2025-06-30 | 2026-03-26 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -20957 | GBP | 2025-06-30 | 2026-03-26 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 1893 | GBP | 2025-06-30 | 2026-03-26 | filed | yes | `core:FixedAssets` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-06-30 | 2024-10-23 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-06-30 | 2026-03-26 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 22171 | GBP | 2024-06-30 | 2024-10-23 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 22171 | GBP | 2024-06-30 | 2026-03-26 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 1352 | GBP | 2024-06-30 | 2026-03-26 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 1352 | GBP | 2024-06-30 | 2024-10-23 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | -18323 | GBP | 2024-06-30 | 2026-03-26 | filed | yes | `core:Equity` | micro-entity |
| equity | -18323 | GBP | 2024-06-30 | 2024-10-23 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 2524 | GBP | 2024-06-30 | 2026-03-26 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 2524 | GBP | 2024-06-30 | 2024-10-23 | filed | no | `core:FixedAssets` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-06-30 | 2024-10-23 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-06-30 | 2024-03-27 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 16710 | GBP | 2023-06-30 | 2024-03-27 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 16710 | GBP | 2023-06-30 | 2024-10-23 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 1003 | GBP | 2023-06-30 | 2024-10-23 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 1003 | GBP | 2023-06-30 | 2024-03-27 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | -13434 | GBP | 2023-06-30 | 2024-10-23 | filed | yes | `core:Equity` | micro-entity |
| equity | -13434 | GBP | 2023-06-30 | 2024-03-27 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 2301 | GBP | 2023-06-30 | 2024-10-23 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 2301 | GBP | 2023-06-30 | 2024-03-27 | filed | no | `core:FixedAssets` | micro-entity |
| average_employees | 1 | xbrli:pure | 2022-06-30 | 2024-03-27 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 13734 | GBP | 2022-06-30 | 2024-03-27 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 2968 | GBP | 2022-06-30 | 2024-03-27 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -9630 | GBP | 2022-06-30 | 2024-03-27 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 3068 | GBP | 2022-06-30 | 2024-03-27 | filed | yes | `core:FixedAssets` | micro-entity |

_No coverage facts for the latest run._

## DEALCOMP LIMITED (`gb:02257959`)

- registration: `02257959` (GB), status active, incorporated 1988-05-13
- classification: ['62090'] (sic_2007)
- records: 3 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 95 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2024-08-31 | 2025-11-25 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 3310 | GBP | 2024-08-31 | 2025-11-25 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -108450 | GBP | 2024-08-31 | 2025-11-25 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-08-31 | 2025-11-25 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | -102802 | GBP | 2024-08-31 | 2025-11-25 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 5548 | GBP | 2024-08-31 | 2025-11-25 | filed | yes | `ns5:Equity` | total-exemption-full |
| fixed_assets | 63123 | GBP | 2024-08-31 | 2025-11-25 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| net_assets | -102802 | GBP | 2024-08-31 | 2025-11-25 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -160788 | GBP | 2024-08-31 | 2025-11-25 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -97665 | GBP | 2024-08-31 | 2025-11-25 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 1 | xbrli:pure | 2023-08-31 | 2024-02-06 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-08-31 | 2025-11-25 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 3511 | GBP | 2023-08-31 | 2025-11-25 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 3511 | GBP | 2023-08-31 | 2024-02-06 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -93690 | GBP | 2023-08-31 | 2025-11-25 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-08-31 | 2025-11-25 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | -88042 | GBP | 2023-08-31 | 2025-11-25 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RevaluationReserve'}` | 5548 | GBP | 2023-08-31 | 2024-02-06 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | -88042 | GBP | 2023-08-31 | 2024-02-06 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 5548 | GBP | 2023-08-31 | 2025-11-25 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 100 | GBP | 2023-08-31 | 2024-02-06 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -93690 | GBP | 2023-08-31 | 2024-02-06 | filed | yes | `ns5:Equity` | total-exemption-full |
| fixed_assets `{'OriginalRevisedDataDimension': 'Original'}` | 67387 | GBP | 2023-08-31 | 2024-02-06 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| fixed_assets | 67387 | GBP | 2023-08-31 | 2025-11-25 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| net_assets | -88042 | GBP | 2023-08-31 | 2025-11-25 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets `{'OriginalRevisedDataDimension': 'Original'}` | -88042 | GBP | 2023-08-31 | 2024-02-06 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -150292 | GBP | 2023-08-31 | 2025-11-25 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | -150292 | GBP | 2023-08-31 | 2024-02-06 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -82905 | GBP | 2023-08-31 | 2025-11-25 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | -82905 | GBP | 2023-08-31 | 2024-02-06 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 1 | xbrli:pure | 2022-08-31 | 2024-02-06 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 1 | xbrli:pure | 2022-08-31 | 2024-02-06 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 55786 | GBP | 2022-08-31 | 2024-02-06 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 55786 | GBP | 2022-08-31 | 2024-02-06 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 55786 | GBP | 2022-08-31 | 2024-02-06 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original'}` | 0 | GBP | 2022-08-31 | 2024-02-06 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -82126 | GBP | 2022-08-31 | 2024-02-06 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 100 | GBP | 2022-08-31 | 2024-02-06 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | -71475 | GBP | 2022-08-31 | 2024-02-06 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RevaluationReserve'}` | 10551 | GBP | 2022-08-31 | 2024-02-06 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RevaluationReserve'}` | 10551 | GBP | 2022-08-31 | 2024-02-06 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | -71472 | GBP | 2022-08-31 | 2024-02-06 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 100 | GBP | 2022-08-31 | 2024-02-06 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -82123 | GBP | 2022-08-31 | 2024-02-06 | filed | yes | `ns5:Equity` | total-exemption-full |
| fixed_assets `{'OriginalRevisedDataDimension': 'Original'}` | 73455 | GBP | 2022-08-31 | 2024-02-06 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| fixed_assets `{'OriginalRevisedDataDimension': 'Original'}` | 73455 | GBP | 2022-08-31 | 2024-02-06 | filed | no | `ns5:FixedAssets` | total-exemption-full |
| net_assets `{'OriginalRevisedDataDimension': 'Original'}` | -71475 | GBP | 2022-08-31 | 2024-02-06 | filed | no | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets `{'OriginalRevisedDataDimension': 'Original'}` | -71472 | GBP | 2022-08-31 | 2024-02-06 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | -138615 | GBP | 2022-08-31 | 2024-02-06 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | -138618 | GBP | 2022-08-31 | 2024-02-06 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | -65163 | GBP | 2022-08-31 | 2024-02-06 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | -65160 | GBP | 2022-08-31 | 2024-02-06 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 1 | xbrli:pure | 2021-08-31 | 2024-02-06 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 176713 | GBP | 2021-08-31 | 2024-02-06 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 176943 | GBP | 2021-08-31 | 2024-02-06 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original'}` | 230 | GBP | 2021-08-31 | 2024-02-06 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 100 | GBP | 2021-08-31 | 2024-02-06 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RevaluationReserve'}` | 17558 | GBP | 2021-08-31 | 2024-02-06 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | -51321 | GBP | 2021-08-31 | 2024-02-06 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -68979 | GBP | 2021-08-31 | 2024-02-06 | filed | yes | `ns5:Equity` | total-exemption-full |
| fixed_assets `{'OriginalRevisedDataDimension': 'Original'}` | 81321 | GBP | 2021-08-31 | 2024-02-06 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| net_assets `{'OriginalRevisedDataDimension': 'Original'}` | -51321 | GBP | 2021-08-31 | 2024-02-06 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | -124581 | GBP | 2021-08-31 | 2024-02-06 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | -43260 | GBP | 2021-08-31 | 2024-02-06 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2024-02-06: `{"superseded_document_id": "gb:02257959:doc:kVq_zZ876LiHvuRaChecAbZG4Qz2SDgvKNumMkUg9Pk", "restatements": [{"concept": "net_current_assets", "period_end": "2022-08-31", "old_value": "-138618.0000", "n`

## A.S.C. (CENTRAL) LIMITED (`gb:02483748`)

- registration: `02483748` (GB), status active, incorporated 1990-03-22
- classification: ['62030'] (sic_2007)
- records: 6 officers, 1 beneficial owners, 0 ownership statements, 1 security interests, 96 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-03-31 | 2025-12-11 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 507283 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 314980 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 589296 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 79513 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 280411 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 100 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 280511 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 280511 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 274316 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-03-31 | 2025-12-11 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-03-31 | 2024-12-19 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 458949 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 458949 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 299142 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 299142 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 514935 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 514935 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors | 52991 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 52991 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 223611 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 100 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 223511 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 100 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 223611 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 223511 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 223611 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 223611 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 215793 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 215793 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-03-31 | 2024-01-30 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-03-31 | 2024-12-19 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 498175 | GBP | 2023-03-31 | 2024-01-30 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 498175 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 369608 | GBP | 2023-03-31 | 2024-01-30 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 369608 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 559711 | GBP | 2023-03-31 | 2024-01-30 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 559711 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 58541 | GBP | 2023-03-31 | 2024-01-30 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 58541 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 198705 | GBP | 2023-03-31 | 2024-01-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-03-31 | 2024-01-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 100 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 198605 | GBP | 2023-03-31 | 2024-01-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 198705 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 198605 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 198705 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 198705 | GBP | 2023-03-31 | 2024-01-30 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 190103 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 190103 | GBP | 2023-03-31 | 2024-01-30 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2022-03-31 | 2024-01-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 367508 | GBP | 2022-03-31 | 2024-01-30 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 289571 | GBP | 2022-03-31 | 2024-01-30 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 437785 | GBP | 2022-03-31 | 2024-01-30 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 68277 | GBP | 2022-03-31 | 2024-01-30 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 154099 | GBP | 2022-03-31 | 2024-01-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2022-03-31 | 2024-01-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 153999 | GBP | 2022-03-31 | 2024-01-30 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 154099 | GBP | 2022-03-31 | 2024-01-30 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 148214 | GBP | 2022-03-31 | 2024-01-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## QUESTADAPT LIMITED (`gb:02684445`)

- registration: `02684445` (GB), status active, incorporated 1992-02-05
- classification: ['62012', '62020'] (sic_2007)
- records: 5 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 83 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | xbrli:pure | 2025-02-28 | 2025-11-21 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 824 | GBP | 2025-02-28 | 2025-11-21 | filed | yes | `uk-core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2025-02-28 | 2025-11-21 | filed | yes | `uk-core:Creditors` | total-exemption-full |
| current_assets | 3953 | GBP | 2025-02-28 | 2025-11-21 | filed | yes | `uk-core:CurrentAssets` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2025-02-28 | 2025-11-21 | filed | yes | `uk-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3951 | GBP | 2025-02-28 | 2025-11-21 | filed | yes | `uk-core:Equity` | total-exemption-full |
| equity | 3953 | GBP | 2025-02-28 | 2025-11-21 | filed | yes | `uk-core:Equity` | total-exemption-full |
| net_assets | 3953 | GBP | 2025-02-28 | 2025-11-21 | filed | yes | `uk-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 3953 | GBP | 2025-02-28 | 2025-11-21 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 3953 | GBP | 2025-02-28 | 2025-11-21 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0 | xbrli:pure | 2024-02-28 | 2024-11-26 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 11784 | GBP | 2024-02-28 | 2025-11-21 | filed | yes | `uk-core:CashBankOnHand` | total-exemption-full |
| cash | 11784 | GBP | 2024-02-28 | 2024-11-26 | filed | no | `uk-core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 3664 | GBP | 2024-02-28 | 2024-11-26 | filed | no | `uk-core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 3664 | GBP | 2024-02-28 | 2025-11-21 | filed | yes | `uk-core:Creditors` | total-exemption-full |
| current_assets | 11784 | GBP | 2024-02-28 | 2025-11-21 | filed | yes | `uk-core:CurrentAssets` | total-exemption-full |
| current_assets | 11784 | GBP | 2024-02-28 | 2024-11-26 | filed | no | `uk-core:CurrentAssets` | total-exemption-full |
| equity | 8120 | GBP | 2024-02-28 | 2025-11-21 | filed | yes | `uk-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 8118 | GBP | 2024-02-28 | 2024-11-26 | filed | no | `uk-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-02-28 | 2024-11-26 | filed | no | `uk-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-02-28 | 2025-11-21 | filed | yes | `uk-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 8118 | GBP | 2024-02-28 | 2025-11-21 | filed | yes | `uk-core:Equity` | total-exemption-full |
| equity | 8120 | GBP | 2024-02-28 | 2024-11-26 | filed | no | `uk-core:Equity` | total-exemption-full |
| net_assets | 8120 | GBP | 2024-02-28 | 2024-11-26 | filed | no | `uk-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 8120 | GBP | 2024-02-28 | 2025-11-21 | filed | yes | `uk-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 8120 | GBP | 2024-02-28 | 2024-11-26 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 8120 | GBP | 2024-02-28 | 2025-11-21 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 8120 | GBP | 2024-02-28 | 2024-11-26 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0 | xbrli:pure | 2023-02-28 | 2023-11-24 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 7858 | GBP | 2023-02-28 | 2023-11-24 | filed | no | `uk-core:CashBankOnHand` | total-exemption-full |
| cash | 7858 | GBP | 2023-02-28 | 2024-11-26 | filed | yes | `uk-core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'OriginalRevisedDataDimension': 'Original'}` | 3111 | GBP | 2023-02-28 | 2023-11-24 | filed | yes | `uk-core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 3111 | GBP | 2023-02-28 | 2024-11-26 | filed | yes | `uk-core:Creditors` | total-exemption-full |
| current_assets | 13770 | GBP | 2023-02-28 | 2023-11-24 | filed | no | `uk-core:CurrentAssets` | total-exemption-full |
| current_assets | 13770 | GBP | 2023-02-28 | 2024-11-26 | filed | yes | `uk-core:CurrentAssets` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 10657 | GBP | 2023-02-28 | 2024-11-26 | filed | yes | `uk-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 2 | GBP | 2023-02-28 | 2023-11-24 | filed | yes | `uk-core:Equity` | total-exemption-full |
| equity | 10659 | GBP | 2023-02-28 | 2024-11-26 | filed | yes | `uk-core:Equity` | total-exemption-full |
| equity | 10659 | GBP | 2023-02-28 | 2023-11-24 | filed | no | `uk-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses', 'OriginalRevisedDataDimension': 'Original'}` | 10657 | GBP | 2023-02-28 | 2023-11-24 | filed | yes | `uk-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-02-28 | 2024-11-26 | filed | yes | `uk-core:Equity` | total-exemption-full |
| net_assets | 10659 | GBP | 2023-02-28 | 2023-11-24 | filed | no | `uk-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 10659 | GBP | 2023-02-28 | 2024-11-26 | filed | yes | `uk-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 10659 | GBP | 2023-02-28 | 2023-11-24 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 10659 | GBP | 2023-02-28 | 2024-11-26 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 10659 | GBP | 2023-02-28 | 2023-11-24 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2022-02-28 | 2023-11-24 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 53278 | GBP | 2022-02-28 | 2023-11-24 | filed | yes | `uk-core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'OriginalRevisedDataDimension': 'Original'}` | 17418 | GBP | 2022-02-28 | 2023-11-24 | filed | yes | `uk-core:Creditors` | total-exemption-full |
| current_assets | 53278 | GBP | 2022-02-28 | 2023-11-24 | filed | yes | `uk-core:CurrentAssets` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses', 'OriginalRevisedDataDimension': 'Original'}` | 35858 | GBP | 2022-02-28 | 2023-11-24 | filed | yes | `uk-core:Equity` | total-exemption-full |
| equity | 35860 | GBP | 2022-02-28 | 2023-11-24 | filed | yes | `uk-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 2 | GBP | 2022-02-28 | 2023-11-24 | filed | yes | `uk-core:Equity` | total-exemption-full |
| net_assets | 35860 | GBP | 2022-02-28 | 2023-11-24 | filed | yes | `uk-core:NetAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 35860 | GBP | 2022-02-28 | 2023-11-24 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## SPOTLIGHT SERVICES (UK) LIMITED (`gb:02918815`)

- registration: `02918815` (GB), status active, incorporated 1994-04-13
- classification: ['62030', '82990', '90030'] (sic_2007)
- records: 5 officers, 2 beneficial owners, 1 ownership statements, 0 security interests, 78 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | iso4217:GBP | 2025-03-31 | 2025-12-29 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 7791 | GBP | 2025-03-31 | 2025-12-29 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 28243 | GBP | 2025-03-31 | 2025-12-29 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 20597 | GBP | 2025-03-31 | 2025-12-29 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 845 | GBP | 2025-03-31 | 2025-12-29 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 20597 | GBP | 2025-03-31 | 2025-12-29 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 20452 | GBP | 2025-03-31 | 2025-12-29 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 21297 | GBP | 2025-03-31 | 2025-12-29 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-03-31 | 2024-12-24 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 9202 | GBP | 2024-03-31 | 2025-12-29 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 9202 | GBP | 2024-03-31 | 2024-12-24 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 137762 | GBP | 2024-03-31 | 2025-12-29 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 137762 | GBP | 2024-03-31 | 2024-12-24 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 130855 | GBP | 2024-03-31 | 2024-12-24 | filed | no | `core:Equity` | micro-entity |
| equity | 130855 | GBP | 2024-03-31 | 2025-12-29 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 2995 | GBP | 2024-03-31 | 2024-12-24 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 2995 | GBP | 2024-03-31 | 2025-12-29 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 130855 | GBP | 2024-03-31 | 2024-12-24 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 130855 | GBP | 2024-03-31 | 2025-12-29 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 128560 | GBP | 2024-03-31 | 2024-12-24 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 128560 | GBP | 2024-03-31 | 2025-12-29 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 131555 | GBP | 2024-03-31 | 2024-12-24 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 131555 | GBP | 2024-03-31 | 2025-12-29 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-03-31 | 2023-12-15 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 31771 | GBP | 2023-03-31 | 2024-12-24 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 31771 | GBP | 2023-03-31 | 2023-12-15 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 289246 | GBP | 2023-03-31 | 2023-12-15 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 289246 | GBP | 2023-03-31 | 2024-12-24 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 259610 | GBP | 2023-03-31 | 2024-12-24 | filed | yes | `core:Equity` | micro-entity |
| equity | 259610 | GBP | 2023-03-31 | 2023-12-15 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 2785 | GBP | 2023-03-31 | 2024-12-24 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 2785 | GBP | 2023-03-31 | 2023-12-15 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | 259610 | GBP | 2023-03-31 | 2023-12-15 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 259610 | GBP | 2023-03-31 | 2024-12-24 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 257475 | GBP | 2023-03-31 | 2023-12-15 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 257475 | GBP | 2023-03-31 | 2024-12-24 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 260260 | GBP | 2023-03-31 | 2024-12-24 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 260260 | GBP | 2023-03-31 | 2023-12-15 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 35133 | GBP | 2022-03-31 | 2023-12-15 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 227272 | GBP | 2022-03-31 | 2023-12-15 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 192511 | GBP | 2022-03-31 | 2023-12-15 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 1022 | GBP | 2022-03-31 | 2023-12-15 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 192511 | GBP | 2022-03-31 | 2023-12-15 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 192139 | GBP | 2022-03-31 | 2023-12-15 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 193161 | GBP | 2022-03-31 | 2023-12-15 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## MCLEAN ARCHITECTS LIMITED (`gb:03115715`)

- registration: `03115715` (GB), status active, incorporated 1995-10-19
- classification: ['71129'] (sic_2007)
- records: 19 officers, 6 beneficial owners, 0 ownership statements, 1 security interests, 133 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.12 | xbrli:pure | 2025-11-30 | 2026-06-19 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 156 | GBP | 2025-11-30 | 2026-06-19 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 326649 | GBP | 2025-11-30 | 2026-06-19 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 357894 | GBP | 2025-11-30 | 2026-06-19 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 357738 | GBP | 2025-11-30 | 2026-06-19 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 357738 | GBP | 2025-11-30 | 2026-06-19 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -30457 | GBP | 2025-11-30 | 2026-06-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShares'}` | 63412 | GBP | 2025-11-30 | 2026-06-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass2'}` | 78 | GBP | 2025-11-30 | 2026-06-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 63412 | GBP | 2025-11-30 | 2026-06-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 39643 | GBP | 2025-11-30 | 2026-06-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 63334 | GBP | 2025-11-30 | 2026-06-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 6688 | GBP | 2025-11-30 | 2026-06-19 | filed | yes | `core:Equity` | total-exemption-full |
| net_current_assets | 31245 | GBP | 2025-11-30 | 2026-06-19 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 39643 | GBP | 2025-11-30 | 2026-06-19 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 12 | xbrli:pure | 2024-11-30 | 2025-06-16 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 0.12 | xbrli:pure | 2024-11-30 | 2026-06-19 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 156 | GBP | 2024-11-30 | 2026-06-19 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 156 | GBP | 2024-11-30 | 2025-06-16 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 367123 | GBP | 2024-11-30 | 2025-06-16 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 367123 | GBP | 2024-11-30 | 2026-06-19 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 376859 | GBP | 2024-11-30 | 2025-06-16 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 376859 | GBP | 2024-11-30 | 2026-06-19 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 376703 | GBP | 2024-11-30 | 2026-06-19 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 376703 | GBP | 2024-11-30 | 2026-06-19 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 376703 | GBP | 2024-11-30 | 2025-06-16 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 376703 | GBP | 2024-11-30 | 2025-06-16 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 63334 | GBP | 2024-11-30 | 2026-06-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -47830 | GBP | 2024-11-30 | 2026-06-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass2'}` | 78 | GBP | 2024-11-30 | 2026-06-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShares'}` | 63412 | GBP | 2024-11-30 | 2025-06-16 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShares'}` | 63412 | GBP | 2024-11-30 | 2026-06-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 22270 | GBP | 2024-11-30 | 2026-06-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 6688 | GBP | 2024-11-30 | 2025-06-16 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -47830 | GBP | 2024-11-30 | 2025-06-16 | filed | no | `core:Equity` | total-exemption-full |
| equity | 22270 | GBP | 2024-11-30 | 2025-06-16 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 63412 | GBP | 2024-11-30 | 2026-06-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 6688 | GBP | 2024-11-30 | 2026-06-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 63412 | GBP | 2024-11-30 | 2025-06-16 | filed | no | `core:Equity` | total-exemption-full |
| net_current_assets | 9736 | GBP | 2024-11-30 | 2025-06-16 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 9736 | GBP | 2024-11-30 | 2026-06-19 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 22270 | GBP | 2024-11-30 | 2026-06-19 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 22270 | GBP | 2024-11-30 | 2025-06-16 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 12 | xbrli:pure | 2023-11-30 | 2025-06-16 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 12 | xbrli:pure | 2023-11-30 | 2024-05-02 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 156 | GBP | 2023-11-30 | 2024-05-02 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 156 | GBP | 2023-11-30 | 2025-06-16 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 357861 | GBP | 2023-11-30 | 2024-05-02 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 357861 | GBP | 2023-11-30 | 2025-06-16 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 377162 | GBP | 2023-11-30 | 2024-05-02 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 377162 | GBP | 2023-11-30 | 2025-06-16 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 377006 | GBP | 2023-11-30 | 2025-06-16 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 377006 | GBP | 2023-11-30 | 2025-06-16 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 377006 | GBP | 2023-11-30 | 2024-05-02 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 377006 | GBP | 2023-11-30 | 2024-05-02 | filed | no | `core:Debtors` | total-exemption-full |
| equity | 32490 | GBP | 2023-11-30 | 2024-05-02 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -37610 | GBP | 2023-11-30 | 2024-05-02 | filed | no | `core:Equity` | total-exemption-full |
| equity | 32490 | GBP | 2023-11-30 | 2025-06-16 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 6688 | GBP | 2023-11-30 | 2024-05-02 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 63412 | GBP | 2023-11-30 | 2025-06-16 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 6688 | GBP | 2023-11-30 | 2025-06-16 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 63412 | GBP | 2023-11-30 | 2024-05-02 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -37610 | GBP | 2023-11-30 | 2025-06-16 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShares'}` | 63412 | GBP | 2023-11-30 | 2025-06-16 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShares'}` | 63412 | GBP | 2023-11-30 | 2024-05-02 | filed | no | `core:Equity` | total-exemption-full |
| net_current_assets | 19301 | GBP | 2023-11-30 | 2025-06-16 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 19301 | GBP | 2023-11-30 | 2024-05-02 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 32490 | GBP | 2023-11-30 | 2024-05-02 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 32490 | GBP | 2023-11-30 | 2025-06-16 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 11 | xbrli:pure | 2022-11-30 | 2024-05-02 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 156 | GBP | 2022-11-30 | 2024-05-02 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 431714 | GBP | 2022-11-30 | 2024-05-02 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 411830 | GBP | 2022-11-30 | 2024-05-02 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 411674 | GBP | 2022-11-30 | 2024-05-02 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 411674 | GBP | 2022-11-30 | 2024-05-02 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -82272 | GBP | 2022-11-30 | 2024-05-02 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 6688 | GBP | 2022-11-30 | 2024-05-02 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 63412 | GBP | 2022-11-30 | 2024-05-02 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShares'}` | 63412 | GBP | 2022-11-30 | 2024-05-02 | filed | yes | `core:Equity` | total-exemption-full |
| equity | -12172 | GBP | 2022-11-30 | 2024-05-02 | filed | yes | `core:Equity` | total-exemption-full |
| net_current_assets | -19884 | GBP | 2022-11-30 | 2024-05-02 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -12172 | GBP | 2022-11-30 | 2024-05-02 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2026-06-19: `{"superseded_document_id": "gb:03115715:doc:nG3AxD8ebySLLGjk2MUS8yKi4TjfKssRyeZ7pBoIE1k", "restatements": [{"concept": "average_employees", "period_end": "2024-11-30", "old_value": "12.0000", "new_val`

## FIRSTM LIMITED (`gb:03287784`)

- registration: `03287784` (GB), status active, incorporated 1996-12-04
- classification: ['62012'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 71 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | xbrli:pure | 2024-12-31 | 2025-09-16 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 1360 | GBP | 2024-12-31 | 2025-09-16 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity | 2837 | GBP | 2024-12-31 | 2025-09-16 | filed | yes | `ns5:Equity` | micro-entity |
| net_assets | -2837 | GBP | 2024-12-31 | 2025-09-16 | filed | yes | `ns5:NetAssetsLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2023-12-31 | 2024-09-14 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 563 | GBP | 2023-12-31 | 2025-09-16 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| current_assets | 563 | GBP | 2023-12-31 | 2024-09-14 | filed | no | `ns5:CurrentAssets` | micro-entity |
| equity | 1237 | GBP | 2023-12-31 | 2025-09-16 | filed | yes | `ns5:Equity` | micro-entity |
| equity | -1237 | GBP | 2023-12-31 | 2024-09-14 | filed | no | `ns5:Equity` | micro-entity |
| net_assets | -1237 | GBP | 2023-12-31 | 2025-09-16 | filed | yes | `ns5:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -1237 | GBP | 2023-12-31 | 2024-09-14 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -1237 | GBP | 2023-12-31 | 2024-09-14 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2022-12-31 | 2024-09-14 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 1902 | GBP | 2022-12-31 | 2024-09-14 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity | 83 | GBP | 2022-12-31 | 2024-09-14 | filed | yes | `ns5:Equity` | micro-entity |
| net_current_assets | 83 | GBP | 2022-12-31 | 2024-09-14 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 83 | GBP | 2022-12-31 | 2024-09-14 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2025-09-16: `{"superseded_document_id": "gb:03287784:doc:E8Pr7bi6TuTaIfkj3AlJhSG1Yn_THjxNRtSoayjwMKY", "restatements": [{"concept": "equity", "period_end": "2023-12-31", "old_value": "-1237.0000", "new_value": "12`

## STRIDE TREGLOWN GROUP PLC (`gb:03464501`)

- registration: `03464501` (GB), status active, incorporated 1997-11-12
- classification: ['71111'] (sic_2007)
- records: 34 officers, 23 beneficial owners, 0 ownership statements, 0 security interests, 194 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._
