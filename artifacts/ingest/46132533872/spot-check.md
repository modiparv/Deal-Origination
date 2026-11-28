# Ingest spot-check

- database: `data/engine.db`
- latest run: `20261128T095338Z-b9c98cfe`
- companies in store: 61800; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## ANALYTECH LIMITED (`gb:02972427`)

- registration: `02972427` (GB), status active, incorporated 1994-09-29
- classification: ['62090'] (sic_2007)
- records: 6 officers, 3 beneficial owners, 0 ownership statements, 0 security interests, 83 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.03 | xbrli:pure | 2024-12-31 | 2025-08-27 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 19737 | GBP | 2024-12-31 | 2025-08-27 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 136366 | GBP | 2024-12-31 | 2025-08-27 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 121962 | GBP | 2024-12-31 | 2025-08-27 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 199 | GBP | 2024-12-31 | 2025-08-27 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 121962 | GBP | 2024-12-31 | 2025-08-27 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 121763 | GBP | 2024-12-31 | 2025-08-27 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 121962 | GBP | 2024-12-31 | 2025-08-27 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0.03 | xbrli:pure | 2023-12-31 | 2025-08-27 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 3 | xbrli:pure | 2023-12-31 | 2024-09-30 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 33778 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 33778 | GBP | 2023-12-31 | 2025-08-27 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 190036 | GBP | 2023-12-31 | 2025-08-27 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 190036 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 159298 | GBP | 2023-12-31 | 2025-08-27 | filed | yes | `core:Equity` | micro-entity |
| equity | 159298 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 265 | GBP | 2023-12-31 | 2025-08-27 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 265 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | 159298 | GBP | 2023-12-31 | 2025-08-27 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 159033 | GBP | 2023-12-31 | 2025-08-27 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 159298 | GBP | 2023-12-31 | 2025-08-27 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 3 | xbrli:pure | 2022-12-31 | 2024-09-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 3 | xbrli:pure | 2022-12-31 | 2023-07-31 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 26428 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 26428 | GBP | 2022-12-31 | 2023-07-31 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 193004 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 193004 | GBP | 2022-12-31 | 2023-07-31 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 174729 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:Equity` | micro-entity |
| equity | 174729 | GBP | 2022-12-31 | 2023-07-31 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 353 | GBP | 2022-12-31 | 2023-07-31 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 353 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 174729 | GBP | 2022-12-31 | 2023-07-31 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 174376 | GBP | 2022-12-31 | 2023-07-31 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 174729 | GBP | 2022-12-31 | 2023-07-31 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 3 | xbrli:pure | 2021-12-31 | 2023-07-31 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 19442 | GBP | 2021-12-31 | 2023-07-31 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 218878 | GBP | 2021-12-31 | 2023-07-31 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 211880 | GBP | 2021-12-31 | 2023-07-31 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 342 | GBP | 2021-12-31 | 2023-07-31 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 211880 | GBP | 2021-12-31 | 2023-07-31 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 211538 | GBP | 2021-12-31 | 2023-07-31 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 211880 | GBP | 2021-12-31 | 2023-07-31 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2025-08-27: `{"superseded_document_id": "gb:02972427:doc:QICAIlhxHg5o6OctWQRzFQc9MJik_0_43TyNI2fO3VU", "restatements": [{"concept": "average_employees", "period_end": "2023-12-31", "old_value": "3.0000", "new_valu`

## PURPLE PENGUIN DESIGN LIMITED (`gb:03700583`)

- registration: `03700583` (GB), status active, incorporated 1999-01-25
- classification: ['18129', '62090', '63120'] (sic_2007)
- records: 6 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 81 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-04-30 | 2025-12-17 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 111 | GBP | 2025-04-30 | 2025-12-17 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 14418 | GBP | 2025-04-30 | 2025-12-17 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 17204 | GBP | 2025-04-30 | 2025-12-17 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 4094 | GBP | 2025-04-30 | 2025-12-17 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 1984 | GBP | 2025-04-30 | 2025-12-17 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 4094 | GBP | 2025-04-30 | 2025-12-17 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 3135 | GBP | 2025-04-30 | 2025-12-17 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 5119 | GBP | 2025-04-30 | 2025-12-17 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-04-30 | 2024-11-19 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-04-30 | 2025-12-17 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 2645 | GBP | 2024-04-30 | 2024-11-19 | filed | no | `core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 2645 | GBP | 2024-04-30 | 2025-12-17 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 12281 | GBP | 2024-04-30 | 2025-12-17 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 12281 | GBP | 2024-04-30 | 2024-11-19 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 18475 | GBP | 2024-04-30 | 2025-12-17 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 18475 | GBP | 2024-04-30 | 2024-11-19 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 5595 | GBP | 2024-04-30 | 2025-12-17 | filed | yes | `core:Equity` | micro-entity |
| equity | 5595 | GBP | 2024-04-30 | 2024-11-19 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 2644 | GBP | 2024-04-30 | 2024-11-19 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 2644 | GBP | 2024-04-30 | 2025-12-17 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 5595 | GBP | 2024-04-30 | 2025-12-17 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 5595 | GBP | 2024-04-30 | 2024-11-19 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 6862 | GBP | 2024-04-30 | 2025-12-17 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 6862 | GBP | 2024-04-30 | 2024-11-19 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 9506 | GBP | 2024-04-30 | 2024-11-19 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 9506 | GBP | 2024-04-30 | 2025-12-17 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-04-30 | 2023-12-14 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-04-30 | 2024-11-19 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 5181 | GBP | 2023-04-30 | 2024-11-19 | filed | yes | `core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 5181 | GBP | 2023-04-30 | 2023-12-14 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 21038 | GBP | 2023-04-30 | 2023-12-14 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 21038 | GBP | 2023-04-30 | 2024-11-19 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 35675 | GBP | 2023-04-30 | 2023-12-14 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 35675 | GBP | 2023-04-30 | 2024-11-19 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 12380 | GBP | 2023-04-30 | 2023-12-14 | filed | no | `core:Equity` | micro-entity |
| equity | 12380 | GBP | 2023-04-30 | 2024-11-19 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 3525 | GBP | 2023-04-30 | 2024-11-19 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 3525 | GBP | 2023-04-30 | 2023-12-14 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | 12380 | GBP | 2023-04-30 | 2023-12-14 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 12380 | GBP | 2023-04-30 | 2024-11-19 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 15341 | GBP | 2023-04-30 | 2024-11-19 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 15341 | GBP | 2023-04-30 | 2023-12-14 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 18866 | GBP | 2023-04-30 | 2023-12-14 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 18866 | GBP | 2023-04-30 | 2024-11-19 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2022-04-30 | 2023-12-14 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 7718 | GBP | 2022-04-30 | 2023-12-14 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 21351 | GBP | 2022-04-30 | 2023-12-14 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 47444 | GBP | 2022-04-30 | 2023-12-14 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 8918 | GBP | 2022-04-30 | 2023-12-14 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 1509 | GBP | 2022-04-30 | 2023-12-14 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 8918 | GBP | 2022-04-30 | 2023-12-14 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 30273 | GBP | 2022-04-30 | 2023-12-14 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 31782 | GBP | 2022-04-30 | 2023-12-14 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## AMILAH CONSULTING LIMITED (`gb:04388928`)

- registration: `04388928` (GB), status active, incorporated 2002-03-07
- classification: ['62090'] (sic_2007)
- records: 4 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 70 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-03-31 | 2025-12-22 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 36152 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 88534 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 52382 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 52382 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 43932 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 43942 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 43942 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 66066 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 70929 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-03-31 | 2024-11-11 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-03-31 | 2025-12-22 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 145981 | GBP | 2024-03-31 | 2024-11-11 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 145981 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 170971 | GBP | 2024-03-31 | 2024-11-11 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 170971 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 24990 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 24990 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 24990 | GBP | 2024-03-31 | 2024-11-11 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 24990 | GBP | 2024-03-31 | 2024-11-11 | filed | no | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10 | GBP | 2024-03-31 | 2024-11-11 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 69094 | GBP | 2024-03-31 | 2024-11-11 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 69084 | GBP | 2024-03-31 | 2024-11-11 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 69094 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 69084 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 69094 | GBP | 2024-03-31 | 2024-11-11 | filed | no | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 69094 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 95523 | GBP | 2024-03-31 | 2024-11-11 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 95523 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 101241 | GBP | 2024-03-31 | 2024-11-11 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 101241 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 1 | xbrli:pure | 2023-03-31 | 2023-11-24 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-03-31 | 2024-11-11 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 99823 | GBP | 2023-03-31 | 2024-11-11 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 99823 | GBP | 2023-03-31 | 2023-11-24 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 128944 | GBP | 2023-03-31 | 2024-11-11 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 128944 | GBP | 2023-03-31 | 2023-11-24 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 29121 | GBP | 2023-03-31 | 2024-11-11 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 29121 | GBP | 2023-03-31 | 2023-11-24 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original'}` | 29121 | GBP | 2023-03-31 | 2023-11-24 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 29121 | GBP | 2023-03-31 | 2024-11-11 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 10 | GBP | 2023-03-31 | 2023-11-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 36918 | GBP | 2023-03-31 | 2023-11-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 36918 | GBP | 2023-03-31 | 2024-11-11 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 36908 | GBP | 2023-03-31 | 2023-11-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 36908 | GBP | 2023-03-31 | 2024-11-11 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10 | GBP | 2023-03-31 | 2024-11-11 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets `{'OriginalRevisedDataDimension': 'Original'}` | 36918 | GBP | 2023-03-31 | 2023-11-24 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 36918 | GBP | 2023-03-31 | 2024-11-11 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 66925 | GBP | 2023-03-31 | 2024-11-11 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 66925 | GBP | 2023-03-31 | 2023-11-24 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 73762 | GBP | 2023-03-31 | 2023-11-24 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 73762 | GBP | 2023-03-31 | 2024-11-11 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 2 | xbrli:pure | 2022-03-31 | 2023-11-24 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 41991 | GBP | 2022-03-31 | 2023-11-24 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 57483 | GBP | 2022-03-31 | 2023-11-24 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 15492 | GBP | 2022-03-31 | 2023-11-24 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original'}` | 15492 | GBP | 2022-03-31 | 2023-11-24 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 3947 | GBP | 2022-03-31 | 2023-11-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 10 | GBP | 2022-03-31 | 2023-11-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3937 | GBP | 2022-03-31 | 2023-11-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets `{'OriginalRevisedDataDimension': 'Original'}` | 3947 | GBP | 2022-03-31 | 2023-11-24 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 40635 | GBP | 2022-03-31 | 2023-11-24 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 47081 | GBP | 2022-03-31 | 2023-11-24 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## PATEL TAYLOR ARCHITECTS LIMITED (`gb:05096844`)

- registration: `05096844` (GB), status active, incorporated 2004-04-06
- classification: ['71111'] (sic_2007)
- records: 5 officers, 2 beneficial owners, 0 ownership statements, 1 security interests, 75 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 32 | xbrli:pure | 2025-04-30 | 2025-12-09 | filed | yes | `d:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 296351 | GBP | 2025-04-30 | 2025-12-09 | filed | yes | `d:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 541285 | GBP | 2025-04-30 | 2025-12-09 | filed | yes | `d:Creditors` | total-exemption-full |
| current_assets | 7651947 | GBP | 2025-04-30 | 2025-12-09 | filed | yes | `d:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 7355596 | GBP | 2025-04-30 | 2025-12-09 | filed | yes | `d:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-04-30 | 2025-12-09 | filed | yes | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 7692311 | GBP | 2025-04-30 | 2025-12-09 | filed | yes | `d:Equity` | total-exemption-full |
| equity | 7692411 | GBP | 2025-04-30 | 2025-12-09 | filed | yes | `d:Equity` | total-exemption-full |
| fixed_assets | 581749 | GBP | 2025-04-30 | 2025-12-09 | filed | yes | `d:FixedAssets` | total-exemption-full |
| net_assets | 7692411 | GBP | 2025-04-30 | 2025-12-09 | filed | yes | `d:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 7110662 | GBP | 2025-04-30 | 2025-12-09 | filed | yes | `d:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 7692411 | GBP | 2025-04-30 | 2025-12-09 | filed | yes | `d:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 39 | xbrli:pure | 2024-04-30 | 2025-12-09 | filed | yes | `d:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 39 | xbrli:pure | 2024-04-30 | 2024-10-23 | filed | no | `d:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 226890 | GBP | 2024-04-30 | 2024-10-23 | filed | no | `d:CashBankOnHand` | total-exemption-full |
| cash | 226890 | GBP | 2024-04-30 | 2025-12-09 | filed | yes | `d:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 755903 | GBP | 2024-04-30 | 2025-12-09 | filed | yes | `d:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 755903 | GBP | 2024-04-30 | 2024-10-23 | filed | no | `d:Creditors` | total-exemption-full |
| current_assets | 8683524 | GBP | 2024-04-30 | 2025-12-09 | filed | yes | `d:CurrentAssets` | total-exemption-full |
| current_assets | 8683524 | GBP | 2024-04-30 | 2024-10-23 | filed | no | `d:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 8456634 | GBP | 2024-04-30 | 2025-12-09 | filed | yes | `d:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 8456634 | GBP | 2024-04-30 | 2024-10-23 | filed | no | `d:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 8065739 | GBP | 2024-04-30 | 2025-12-09 | filed | yes | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-04-30 | 2025-12-09 | filed | yes | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-04-30 | 2024-10-23 | filed | no | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 8065739 | GBP | 2024-04-30 | 2024-10-23 | filed | no | `d:Equity` | total-exemption-full |
| equity | 8065839 | GBP | 2024-04-30 | 2025-12-09 | filed | yes | `d:Equity` | total-exemption-full |
| equity | 8065839 | GBP | 2024-04-30 | 2024-10-23 | filed | no | `d:Equity` | total-exemption-full |
| fixed_assets | 138218 | GBP | 2024-04-30 | 2025-12-09 | filed | yes | `d:FixedAssets` | total-exemption-full |
| fixed_assets | 138218 | GBP | 2024-04-30 | 2024-10-23 | filed | no | `d:FixedAssets` | total-exemption-full |
| net_assets | 8065839 | GBP | 2024-04-30 | 2025-12-09 | filed | yes | `d:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 8065839 | GBP | 2024-04-30 | 2024-10-23 | filed | no | `d:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 7927621 | GBP | 2024-04-30 | 2024-10-23 | filed | no | `d:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 7927621 | GBP | 2024-04-30 | 2025-12-09 | filed | yes | `d:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 8065839 | GBP | 2024-04-30 | 2024-10-23 | filed | no | `d:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 8065839 | GBP | 2024-04-30 | 2025-12-09 | filed | yes | `d:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 41 | xbrli:pure | 2023-04-30 | 2024-02-12 | filed | no | `d:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 41 | xbrli:pure | 2023-04-30 | 2024-10-23 | filed | yes | `d:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 274929 | GBP | 2023-04-30 | 2024-02-12 | filed | no | `d:CashBankOnHand` | total-exemption-full |
| cash | 274929 | GBP | 2023-04-30 | 2024-10-23 | filed | yes | `d:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 609352 | GBP | 2023-04-30 | 2024-10-23 | filed | yes | `d:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 609352 | GBP | 2023-04-30 | 2024-02-12 | filed | no | `d:Creditors` | total-exemption-full |
| current_assets | 6995397 | GBP | 2023-04-30 | 2024-02-12 | filed | no | `d:CurrentAssets` | total-exemption-full |
| current_assets | 6995397 | GBP | 2023-04-30 | 2024-10-23 | filed | yes | `d:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 6692636 | GBP | 2023-04-30 | 2024-02-12 | filed | no | `d:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 6692636 | GBP | 2023-04-30 | 2024-10-23 | filed | yes | `d:Debtors` | total-exemption-full |
| equity | 6986617 | GBP | 2023-04-30 | 2024-10-23 | filed | yes | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 6986517 | GBP | 2023-04-30 | 2024-10-23 | filed | yes | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 6986517 | GBP | 2023-04-30 | 2024-02-12 | filed | no | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-04-30 | 2024-02-12 | filed | no | `d:Equity` | total-exemption-full |
| equity | 6986617 | GBP | 2023-04-30 | 2024-02-12 | filed | no | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-04-30 | 2024-10-23 | filed | yes | `d:Equity` | total-exemption-full |
| fixed_assets | 600572 | GBP | 2023-04-30 | 2024-10-23 | filed | yes | `d:FixedAssets` | total-exemption-full |
| fixed_assets | 600572 | GBP | 2023-04-30 | 2024-02-12 | filed | no | `d:FixedAssets` | total-exemption-full |
| net_assets | 6986617 | GBP | 2023-04-30 | 2024-02-12 | filed | no | `d:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 6986617 | GBP | 2023-04-30 | 2024-10-23 | filed | yes | `d:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 6386045 | GBP | 2023-04-30 | 2024-10-23 | filed | yes | `d:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 6386045 | GBP | 2023-04-30 | 2024-02-12 | filed | no | `d:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 6986617 | GBP | 2023-04-30 | 2024-02-12 | filed | no | `d:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 6986617 | GBP | 2023-04-30 | 2024-10-23 | filed | yes | `d:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 44 | xbrli:pure | 2022-04-30 | 2024-02-12 | filed | yes | `d:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 250872 | GBP | 2022-04-30 | 2024-02-12 | filed | yes | `d:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 672894 | GBP | 2022-04-30 | 2024-02-12 | filed | yes | `d:Creditors` | total-exemption-full |
| current_assets | 7694857 | GBP | 2022-04-30 | 2024-02-12 | filed | yes | `d:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 7423686 | GBP | 2022-04-30 | 2024-02-12 | filed | yes | `d:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2022-04-30 | 2024-02-12 | filed | yes | `d:Equity` | total-exemption-full |
| equity | 7565565 | GBP | 2022-04-30 | 2024-02-12 | filed | yes | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 7565465 | GBP | 2022-04-30 | 2024-02-12 | filed | yes | `d:Equity` | total-exemption-full |
| fixed_assets | 543602 | GBP | 2022-04-30 | 2024-02-12 | filed | yes | `d:FixedAssets` | total-exemption-full |
| net_assets | 7565565 | GBP | 2022-04-30 | 2024-02-12 | filed | yes | `d:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 7021963 | GBP | 2022-04-30 | 2024-02-12 | filed | yes | `d:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 7565565 | GBP | 2022-04-30 | 2024-02-12 | filed | yes | `d:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## CAREFREE MANAGEMENT LIMITED (`gb:05769227`)

- registration: `05769227` (GB), status active, incorporated 2006-04-04
- classification: ['62012'] (sic_2007)
- records: 8 officers, 4 beneficial owners, 0 ownership statements, 1 security interests, 72 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.17 | xbrli:pure | 2025-04-30 | 2026-01-27 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 87585 | GBP | 2025-04-30 | 2026-01-27 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| current_assets | 264629 | GBP | 2025-04-30 | 2026-01-27 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 177044 | GBP | 2025-04-30 | 2026-01-27 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 177044 | GBP | 2025-04-30 | 2026-01-27 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-04-30 | 2026-01-27 | filed | yes | `core:Equity` | total-exemption-full |
| equity | -551846 | GBP | 2025-04-30 | 2026-01-27 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -551946 | GBP | 2025-04-30 | 2026-01-27 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | -551846 | GBP | 2025-04-30 | 2026-01-27 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -112112 | GBP | 2025-04-30 | 2026-01-27 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -51846 | GBP | 2025-04-30 | 2026-01-27 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 17 | xbrli:pure | 2024-04-30 | 2025-04-29 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 0.17 | xbrli:pure | 2024-04-30 | 2026-01-27 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 80703 | GBP | 2024-04-30 | 2025-04-29 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 80703 | GBP | 2024-04-30 | 2026-01-27 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 756056 | GBP | 2024-04-30 | 2025-04-29 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 380706 | GBP | 2024-04-30 | 2025-04-29 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 380706 | GBP | 2024-04-30 | 2026-01-27 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 300003 | GBP | 2024-04-30 | 2025-04-29 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 300003 | GBP | 2024-04-30 | 2025-04-29 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 300003 | GBP | 2024-04-30 | 2026-01-27 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 300003 | GBP | 2024-04-30 | 2026-01-27 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -307322 | GBP | 2024-04-30 | 2025-04-29 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-04-30 | 2025-04-29 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -307322 | GBP | 2024-04-30 | 2026-01-27 | filed | yes | `core:Equity` | total-exemption-full |
| equity | -307222 | GBP | 2024-04-30 | 2026-01-27 | filed | yes | `core:Equity` | total-exemption-full |
| equity | -307222 | GBP | 2024-04-30 | 2025-04-29 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-04-30 | 2026-01-27 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | -307222 | GBP | 2024-04-30 | 2026-01-27 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -375350 | GBP | 2024-04-30 | 2025-04-29 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -375350 | GBP | 2024-04-30 | 2026-01-27 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -307222 | GBP | 2024-04-30 | 2025-04-29 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -307222 | GBP | 2024-04-30 | 2026-01-27 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 21 | xbrli:pure | 2023-04-30 | 2025-04-29 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 21 | xbrli:pure | 2023-04-30 | 2024-01-26 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 71831 | GBP | 2023-04-30 | 2025-04-29 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 71831 | GBP | 2023-04-30 | 2024-01-26 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 294829 | GBP | 2023-04-30 | 2025-04-29 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 294829 | GBP | 2023-04-30 | 2024-01-26 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 285066 | GBP | 2023-04-30 | 2024-01-26 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 285066 | GBP | 2023-04-30 | 2025-04-29 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 213235 | GBP | 2023-04-30 | 2025-04-29 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 213235 | GBP | 2023-04-30 | 2024-01-26 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 213235 | GBP | 2023-04-30 | 2025-04-29 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 14896 | GBP | 2023-04-30 | 2025-04-29 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 14796 | GBP | 2023-04-30 | 2025-04-29 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-04-30 | 2025-04-29 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-04-30 | 2024-01-26 | filed | no | `core:Equity` | total-exemption-full |
| equity | 14896 | GBP | 2023-04-30 | 2024-01-26 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 14796 | GBP | 2023-04-30 | 2024-01-26 | filed | no | `core:Equity` | total-exemption-full |
| net_assets | 14896 | GBP | 2023-04-30 | 2024-01-26 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -9763 | GBP | 2023-04-30 | 2024-01-26 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -9763 | GBP | 2023-04-30 | 2025-04-29 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 14896 | GBP | 2023-04-30 | 2025-04-29 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 14896 | GBP | 2023-04-30 | 2024-01-26 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 25 | xbrli:pure | 2022-04-30 | 2024-01-26 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 194307 | GBP | 2022-04-30 | 2024-01-26 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 262270 | GBP | 2022-04-30 | 2024-01-26 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 457514 | GBP | 2022-04-30 | 2024-01-26 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 263207 | GBP | 2022-04-30 | 2024-01-26 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 224154 | GBP | 2022-04-30 | 2024-01-26 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 224254 | GBP | 2022-04-30 | 2024-01-26 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2022-04-30 | 2024-01-26 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 224254 | GBP | 2022-04-30 | 2024-01-26 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 195244 | GBP | 2022-04-30 | 2024-01-26 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 224254 | GBP | 2022-04-30 | 2024-01-26 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2026-01-27: `{"superseded_document_id": "gb:05769227:doc:fNHuqmuFUtGdS1sMWRcRf_gIjvzKQ9t5buYBSZg9lBU", "restatements": [{"concept": "average_employees", "period_end": "2024-04-30", "old_value": "17.0000", "new_val`

## PIPER TECHNICAL SERVICES LIMITED (`gb:06360595`)

- registration: `06360595` (GB), status active, incorporated 2007-09-04
- classification: ['71122'] (sic_2007)
- records: 2 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 43 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-09-30 | 2026-04-27 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 22949 | GBP | 2025-09-30 | 2026-04-27 | filed | yes | `core:CashBankOnHand` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 23052 | GBP | 2025-09-30 | 2026-04-27 | filed | yes | `core:Creditors` | unaudited-abridged |
| current_assets | 23347 | GBP | 2025-09-30 | 2026-04-27 | filed | yes | `core:CurrentAssets` | unaudited-abridged |
| debtors | 398 | GBP | 2025-09-30 | 2026-04-27 | filed | yes | `core:Debtors` | unaudited-abridged |
| equity | 295 | GBP | 2025-09-30 | 2026-04-27 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2025-09-30 | 2026-04-27 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 294 | GBP | 2025-09-30 | 2026-04-27 | filed | yes | `core:Equity` | unaudited-abridged |
| net_assets | 295 | GBP | 2025-09-30 | 2026-04-27 | filed | yes | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 295 | GBP | 2025-09-30 | 2026-04-27 | filed | yes | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 295 | GBP | 2025-09-30 | 2026-04-27 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 2 | xbrli:pure | 2024-09-30 | 2026-04-27 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| average_employees | 2 | xbrli:pure | 2024-09-30 | 2025-05-07 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 39893 | GBP | 2024-09-30 | 2025-05-07 | filed | no | `core:CashBankOnHand` | unaudited-abridged |
| cash | 39893 | GBP | 2024-09-30 | 2026-04-27 | filed | yes | `core:CashBankOnHand` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 39503 | GBP | 2024-09-30 | 2025-05-07 | filed | no | `core:Creditors` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 39503 | GBP | 2024-09-30 | 2026-04-27 | filed | yes | `core:Creditors` | unaudited-abridged |
| current_assets | 40477 | GBP | 2024-09-30 | 2026-04-27 | filed | yes | `core:CurrentAssets` | unaudited-abridged |
| current_assets | 40477 | GBP | 2024-09-30 | 2025-05-07 | filed | no | `core:CurrentAssets` | unaudited-abridged |
| debtors | 584 | GBP | 2024-09-30 | 2025-05-07 | filed | no | `core:Debtors` | unaudited-abridged |
| debtors | 584 | GBP | 2024-09-30 | 2026-04-27 | filed | yes | `core:Debtors` | unaudited-abridged |
| equity | 974 | GBP | 2024-09-30 | 2026-04-27 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 973 | GBP | 2024-09-30 | 2026-04-27 | filed | yes | `core:Equity` | unaudited-abridged |
| equity | 974 | GBP | 2024-09-30 | 2025-05-07 | filed | no | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 973 | GBP | 2024-09-30 | 2025-05-07 | filed | no | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2024-09-30 | 2025-05-07 | filed | no | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2024-09-30 | 2026-04-27 | filed | yes | `core:Equity` | unaudited-abridged |
| net_assets | 974 | GBP | 2024-09-30 | 2025-05-07 | filed | no | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_assets | 974 | GBP | 2024-09-30 | 2026-04-27 | filed | yes | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 974 | GBP | 2024-09-30 | 2025-05-07 | filed | no | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 974 | GBP | 2024-09-30 | 2026-04-27 | filed | yes | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 974 | GBP | 2024-09-30 | 2026-04-27 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 974 | GBP | 2024-09-30 | 2025-05-07 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 1 | xbrli:pure | 2023-09-30 | 2024-02-26 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| average_employees | 2 | xbrli:pure | 2023-09-30 | 2025-05-07 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 48326 | GBP | 2023-09-30 | 2025-05-07 | filed | yes | `core:CashBankOnHand` | unaudited-abridged |
| cash | 48326 | GBP | 2023-09-30 | 2024-02-26 | filed | no | `core:CashBankOnHand` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 49221 | GBP | 2023-09-30 | 2024-02-26 | filed | no | `core:Creditors` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 49221 | GBP | 2023-09-30 | 2025-05-07 | filed | yes | `core:Creditors` | unaudited-abridged |
| current_assets | 49258 | GBP | 2023-09-30 | 2024-02-26 | filed | no | `core:CurrentAssets` | unaudited-abridged |
| current_assets | 49258 | GBP | 2023-09-30 | 2025-05-07 | filed | yes | `core:CurrentAssets` | unaudited-abridged |
| debtors | 932 | GBP | 2023-09-30 | 2025-05-07 | filed | yes | `core:Debtors` | unaudited-abridged |
| debtors | 932 | GBP | 2023-09-30 | 2024-02-26 | filed | no | `core:Debtors` | unaudited-abridged |
| equity | 37 | GBP | 2023-09-30 | 2024-02-26 | filed | no | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2023-09-30 | 2024-02-26 | filed | no | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 36 | GBP | 2023-09-30 | 2024-02-26 | filed | no | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 36 | GBP | 2023-09-30 | 2025-05-07 | filed | yes | `core:Equity` | unaudited-abridged |
| equity | 37 | GBP | 2023-09-30 | 2025-05-07 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2023-09-30 | 2025-05-07 | filed | yes | `core:Equity` | unaudited-abridged |
| net_assets | 37 | GBP | 2023-09-30 | 2025-05-07 | filed | yes | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_assets | 37 | GBP | 2023-09-30 | 2024-02-26 | filed | no | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 37 | GBP | 2023-09-30 | 2024-02-26 | filed | no | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 37 | GBP | 2023-09-30 | 2025-05-07 | filed | yes | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 37 | GBP | 2023-09-30 | 2025-05-07 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 37 | GBP | 2023-09-30 | 2024-02-26 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 1 | xbrli:pure | 2022-09-30 | 2024-02-26 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 736 | GBP | 2022-09-30 | 2024-02-26 | filed | yes | `core:CashBankOnHand` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 29292 | GBP | 2022-09-30 | 2024-02-26 | filed | yes | `core:Creditors` | unaudited-abridged |
| current_assets | 4967 | GBP | 2022-09-30 | 2024-02-26 | filed | yes | `core:CurrentAssets` | unaudited-abridged |
| debtors | 4231 | GBP | 2022-09-30 | 2024-02-26 | filed | yes | `core:Debtors` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -24326 | GBP | 2022-09-30 | 2024-02-26 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2022-09-30 | 2024-02-26 | filed | yes | `core:Equity` | unaudited-abridged |
| equity | -24325 | GBP | 2022-09-30 | 2024-02-26 | filed | yes | `core:Equity` | unaudited-abridged |
| net_assets | -24325 | GBP | 2022-09-30 | 2024-02-26 | filed | yes | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | -24325 | GBP | 2022-09-30 | 2024-02-26 | filed | yes | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | -24325 | GBP | 2022-09-30 | 2024-02-26 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |

_No coverage facts for the latest run._

- event restatement @ 2025-05-07: `{"superseded_document_id": "gb:06360595:doc:3XndAJRUYHcwaVYVbc1tbxud2jiwhLvC3OzNo5SlRzc", "restatements": [{"concept": "average_employees", "period_end": "2023-09-30", "old_value": "1.0000", "new_valu`

## UPSIDEUP LIMITED (`gb:06830564`)

- registration: `06830564` (GB), status active, incorporated 2009-02-26
- classification: ['62012', '64209'] (sic_2007)
- records: 6 officers, 0 beneficial owners, 1 ownership statements, 0 security interests, 103 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | iso4217:GBP | 2023-03-31 | 2024-06-05 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 64185 | GBP | 2023-03-31 | 2024-06-05 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1124343 | GBP | 2023-03-31 | 2024-06-05 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 1029185 | GBP | 2023-03-31 | 2024-06-05 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 1186007 | GBP | 2023-03-31 | 2024-06-05 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 1345350 | GBP | 2023-03-31 | 2024-06-05 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 1186007 | GBP | 2023-03-31 | 2024-06-05 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 95158 | GBP | 2023-03-31 | 2024-06-05 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 1250192 | GBP | 2023-03-31 | 2024-06-05 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2022-03-31 | 2024-06-03 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2022-03-31 | 2024-06-05 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 64185 | GBP | 2022-03-31 | 2024-06-03 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 64185 | GBP | 2022-03-31 | 2024-06-05 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1047652 | GBP | 2022-03-31 | 2024-06-05 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1047652 | GBP | 2022-03-31 | 2024-06-03 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 973471 | GBP | 2022-03-31 | 2024-06-05 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 973471 | GBP | 2022-03-31 | 2024-06-03 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | 1206984 | GBP | 2022-03-31 | 2024-06-05 | filed | yes | `uk-core:Equity` | micro-entity |
| equity | 1206984 | GBP | 2022-03-31 | 2024-06-03 | filed | no | `uk-core:Equity` | micro-entity |
| fixed_assets | 1345350 | GBP | 2022-03-31 | 2024-06-05 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 1345350 | GBP | 2022-03-31 | 2024-06-03 | filed | no | `uk-core:FixedAssets` | micro-entity |
| net_assets | 1206984 | GBP | 2022-03-31 | 2024-06-05 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 1206984 | GBP | 2022-03-31 | 2024-06-03 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 74181 | GBP | 2022-03-31 | 2024-06-05 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 74181 | GBP | 2022-03-31 | 2024-06-03 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 1271169 | GBP | 2022-03-31 | 2024-06-05 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 1271169 | GBP | 2022-03-31 | 2024-06-03 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2021-03-31 | 2024-06-03 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2021-03-31 | 2024-05-31 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 64185 | GBP | 2021-03-31 | 2024-05-31 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 64185 | GBP | 2021-03-31 | 2024-06-03 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 965107 | GBP | 2021-03-31 | 2024-05-31 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 965107 | GBP | 2021-03-31 | 2024-06-03 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 897440 | GBP | 2021-03-31 | 2024-06-03 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 897440 | GBP | 2021-03-31 | 2024-05-31 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | 1213498 | GBP | 2021-03-31 | 2024-05-31 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 1213498 | GBP | 2021-03-31 | 2024-06-03 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 1345350 | GBP | 2021-03-31 | 2024-05-31 | filed | no | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 1345350 | GBP | 2021-03-31 | 2024-06-03 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 1213498 | GBP | 2021-03-31 | 2024-06-03 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 1213498 | GBP | 2021-03-31 | 2024-05-31 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 67667 | GBP | 2021-03-31 | 2024-06-03 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 67667 | GBP | 2021-03-31 | 2024-05-31 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 1277683 | GBP | 2021-03-31 | 2024-06-03 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 1277683 | GBP | 2021-03-31 | 2024-05-31 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2020-03-31 | 2024-05-31 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 64185 | GBP | 2020-03-31 | 2024-05-31 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 711832 | GBP | 2020-03-31 | 2024-05-31 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 589787 | GBP | 2020-03-31 | 2024-05-31 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 1159120 | GBP | 2020-03-31 | 2024-05-31 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 1345350 | GBP | 2020-03-31 | 2024-05-31 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 1159120 | GBP | 2020-03-31 | 2024-05-31 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 122045 | GBP | 2020-03-31 | 2024-05-31 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 1223305 | GBP | 2020-03-31 | 2024-05-31 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## NOODLFROOT LTD (`gb:07245048`)

- registration: `07245048` (GB), status active, incorporated 2010-05-06
- classification: ['62012'] (sic_2007)
- records: 5 officers, 4 beneficial owners, 0 ownership statements, 0 security interests, 54 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | xbrli:pure | 2025-05-31 | 2026-02-24 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 127 | GBP | 2025-05-31 | 2026-02-24 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 6740 | GBP | 2025-05-31 | 2026-02-24 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 243 | GBP | 2025-05-31 | 2026-02-24 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 116 | GBP | 2025-05-31 | 2026-02-24 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 132 | GBP | 2025-05-31 | 2026-02-24 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 132 | GBP | 2025-05-31 | 2026-02-24 | filed | yes | `core:Equity` | total-exemption-full |
| equity | -6497 | GBP | 2025-05-31 | 2026-02-24 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -6629 | GBP | 2025-05-31 | 2026-02-24 | filed | yes | `core:Equity` | total-exemption-full |
| net_current_assets | -6497 | GBP | 2025-05-31 | 2026-02-24 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| average_employees | 0 | xbrli:pure | 2024-05-31 | 2026-02-24 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 0 | xbrli:pure | 2024-05-31 | 2025-01-06 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 324 | GBP | 2024-05-31 | 2026-02-24 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 324 | GBP | 2024-05-31 | 2025-01-06 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 4250 | GBP | 2024-05-31 | 2025-01-06 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 4250 | GBP | 2024-05-31 | 2026-02-24 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 447 | GBP | 2024-05-31 | 2026-02-24 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 447 | GBP | 2024-05-31 | 2025-01-06 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors | 123 | GBP | 2024-05-31 | 2026-02-24 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 123 | GBP | 2024-05-31 | 2025-01-06 | filed | no | `core:Debtors` | total-exemption-full |
| equity | -3803 | GBP | 2024-05-31 | 2025-01-06 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 132 | GBP | 2024-05-31 | 2026-02-24 | filed | yes | `core:Equity` | total-exemption-full |
| equity | -3803 | GBP | 2024-05-31 | 2026-02-24 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 132 | GBP | 2024-05-31 | 2025-01-06 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 132 | GBP | 2024-05-31 | 2026-02-24 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -3935 | GBP | 2024-05-31 | 2025-01-06 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -3935 | GBP | 2024-05-31 | 2026-02-24 | filed | yes | `core:Equity` | total-exemption-full |
| net_current_assets | -3803 | GBP | 2024-05-31 | 2025-01-06 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -3803 | GBP | 2024-05-31 | 2026-02-24 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -3803 | GBP | 2024-05-31 | 2025-01-06 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0 | xbrli:pure | 2023-05-31 | 2025-01-06 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 0 | xbrli:pure | 2023-05-31 | 2023-12-07 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 162 | GBP | 2023-05-31 | 2023-12-07 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 162 | GBP | 2023-05-31 | 2025-01-06 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1795 | GBP | 2023-05-31 | 2025-01-06 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1795 | GBP | 2023-05-31 | 2023-12-07 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 460 | GBP | 2023-05-31 | 2023-12-07 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 460 | GBP | 2023-05-31 | 2025-01-06 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 298 | GBP | 2023-05-31 | 2023-12-07 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 298 | GBP | 2023-05-31 | 2025-01-06 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | -1006 | GBP | 2023-05-31 | 2023-12-07 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 132 | GBP | 2023-05-31 | 2023-12-07 | filed | no | `core:Equity` | total-exemption-full |
| equity | -1006 | GBP | 2023-05-31 | 2025-01-06 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -1138 | GBP | 2023-05-31 | 2025-01-06 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -1138 | GBP | 2023-05-31 | 2023-12-07 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 132 | GBP | 2023-05-31 | 2025-01-06 | filed | yes | `core:Equity` | total-exemption-full |
| net_current_assets | -1335 | GBP | 2023-05-31 | 2023-12-07 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -1335 | GBP | 2023-05-31 | 2025-01-06 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -1006 | GBP | 2023-05-31 | 2023-12-07 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -1006 | GBP | 2023-05-31 | 2025-01-06 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0 | xbrli:pure | 2022-05-31 | 2023-12-07 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 1833 | GBP | 2022-05-31 | 2023-12-07 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 950 | GBP | 2022-05-31 | 2023-12-07 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 1875 | GBP | 2022-05-31 | 2023-12-07 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 42 | GBP | 2022-05-31 | 2023-12-07 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2390 | GBP | 2022-05-31 | 2023-12-07 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 2522 | GBP | 2022-05-31 | 2023-12-07 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 132 | GBP | 2022-05-31 | 2023-12-07 | filed | yes | `core:Equity` | total-exemption-full |
| net_current_assets | 925 | GBP | 2022-05-31 | 2023-12-07 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 2522 | GBP | 2022-05-31 | 2023-12-07 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## TRM TECHNOLOGY LTD (`gb:07642327`)

- registration: `07642327` (GB), status active, incorporated 2011-05-20
- classification: ['62020', '85320'] (sic_2007)
- records: 5 officers, 3 beneficial owners, 0 ownership statements, 0 security interests, 50 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 6 | iso4217:GBP | 2025-05-31 | 2026-01-19 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 106288 | GBP | 2025-05-31 | 2026-01-19 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 6696 | GBP | 2025-05-31 | 2026-01-19 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 123238 | GBP | 2025-05-31 | 2026-01-19 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 139154 | GBP | 2025-05-31 | 2026-01-19 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 4000 | GBP | 2025-05-31 | 2026-01-19 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 28866 | GBP | 2025-05-31 | 2026-01-19 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 32866 | GBP | 2025-05-31 | 2026-01-19 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 4 | GBP | 2025-05-31 | 2026-01-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 49480 | GBP | 2025-05-31 | 2026-01-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 49484 | GBP | 2025-05-31 | 2026-01-19 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 40264 | GBP | 2025-05-31 | 2026-01-19 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | 49484 | GBP | 2025-05-31 | 2026-01-19 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 15916 | GBP | 2025-05-31 | 2026-01-19 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 56180 | GBP | 2025-05-31 | 2026-01-19 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 5 | iso4217:GBP | 2024-05-31 | 2026-01-19 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 5 | iso4217:GBP | 2024-05-31 | 2024-12-19 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 76700 | GBP | 2024-05-31 | 2026-01-19 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 76700 | GBP | 2024-05-31 | 2024-12-19 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 11573 | GBP | 2024-05-31 | 2024-12-19 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 11573 | GBP | 2024-05-31 | 2026-01-19 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 75981 | GBP | 2024-05-31 | 2026-01-19 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 75981 | GBP | 2024-05-31 | 2024-12-19 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 78191 | GBP | 2024-05-31 | 2024-12-19 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 78191 | GBP | 2024-05-31 | 2026-01-19 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 1491 | GBP | 2024-05-31 | 2026-01-19 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2024-05-31 | 2026-01-19 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1491 | GBP | 2024-05-31 | 2026-01-19 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1491 | GBP | 2024-05-31 | 2024-12-19 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 1491 | GBP | 2024-05-31 | 2024-12-19 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-05-31 | 2026-01-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 19797 | GBP | 2024-05-31 | 2024-12-19 | filed | no | `core:Equity` | total-exemption-full |
| equity | 19797 | GBP | 2024-05-31 | 2026-01-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 19795 | GBP | 2024-05-31 | 2024-12-19 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-05-31 | 2024-12-19 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 19795 | GBP | 2024-05-31 | 2026-01-19 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 29160 | GBP | 2024-05-31 | 2026-01-19 | filed | yes | `core:FixedAssets` | total-exemption-full |
| fixed_assets | 29160 | GBP | 2024-05-31 | 2024-12-19 | filed | no | `core:FixedAssets` | total-exemption-full |
| net_assets | 19797 | GBP | 2024-05-31 | 2026-01-19 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 19797 | GBP | 2024-05-31 | 2024-12-19 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 2210 | GBP | 2024-05-31 | 2026-01-19 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 2210 | GBP | 2024-05-31 | 2024-12-19 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 31370 | GBP | 2024-05-31 | 2024-12-19 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 31370 | GBP | 2024-05-31 | 2026-01-19 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 4 | iso4217:GBP | 2023-05-31 | 2023-12-11 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 4 | iso4217:GBP | 2023-05-31 | 2024-12-19 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 45295 | GBP | 2023-05-31 | 2024-12-19 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 16329 | GBP | 2023-05-31 | 2023-12-11 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 16329 | GBP | 2023-05-31 | 2024-12-19 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 91600 | GBP | 2023-05-31 | 2024-12-19 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 91601 | GBP | 2023-05-31 | 2023-12-11 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 96812 | GBP | 2023-05-31 | 2023-12-11 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 96812 | GBP | 2023-05-31 | 2024-12-19 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 51517 | GBP | 2023-05-31 | 2024-12-19 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 51517 | GBP | 2023-05-31 | 2024-12-19 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-05-31 | 2024-12-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 20204 | GBP | 2023-05-31 | 2024-12-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 20205 | GBP | 2023-05-31 | 2023-12-11 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 20206 | GBP | 2023-05-31 | 2024-12-19 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 31323 | GBP | 2023-05-31 | 2024-12-19 | filed | yes | `core:FixedAssets` | total-exemption-full |
| fixed_assets | 31323 | GBP | 2023-05-31 | 2023-12-11 | filed | no | `uk-core:FixedAssets` | micro-entity |
| net_assets | 20206 | GBP | 2023-05-31 | 2024-12-19 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 20205 | GBP | 2023-05-31 | 2023-12-11 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 5212 | GBP | 2023-05-31 | 2024-12-19 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 5211 | GBP | 2023-05-31 | 2023-12-11 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 36534 | GBP | 2023-05-31 | 2023-12-11 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 36535 | GBP | 2023-05-31 | 2024-12-19 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 4 | iso4217:GBP | 2022-05-31 | 2023-12-11 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 12512 | GBP | 2022-05-31 | 2023-12-11 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 112230 | GBP | 2022-05-31 | 2023-12-11 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 107494 | GBP | 2022-05-31 | 2023-12-11 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 136 | GBP | 2022-05-31 | 2023-12-11 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 17384 | GBP | 2022-05-31 | 2023-12-11 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 136 | GBP | 2022-05-31 | 2023-12-11 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 4736 | GBP | 2022-05-31 | 2023-12-11 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 12648 | GBP | 2022-05-31 | 2023-12-11 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2024-12-19: `{"superseded_document_id": "gb:07642327:doc:0j9eJvUKz8tJpTDVRCQlyJVrKp620wzgA6Zm50-Q8mg", "restatements": [{"concept": "creditors_within_one_year", "period_end": "2023-05-31", "old_value": "91601.0000`
