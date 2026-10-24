# Ingest spot-check

- database: `data/engine.db`
- latest run: `20261024T065629Z-bdd5b381`
- companies in store: 34600; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## MFP TECHNOLOGY SERVICES (UK) LTD (`gb:02453476`)

- registration: `02453476` (GB), status active, incorporated 1989-12-18
- classification: ['62090'] (sic_2007)
- records: 13 officers, 0 beneficial owners, 1 ownership statements, 2 security interests, 125 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 6 | xbrli:pure | 2024-12-31 | 2025-12-19 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 56171 | GBP | 2024-12-31 | 2025-12-19 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 2384572 | GBP | 2024-12-31 | 2025-12-19 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 797979 | GBP | 2024-12-31 | 2025-12-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10000 | GBP | 2024-12-31 | 2025-12-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 787979 | GBP | 2024-12-31 | 2025-12-19 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 797979 | GBP | 2024-12-31 | 2025-12-19 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| average_employees | 7 | xbrli:pure | 2023-12-31 | 2025-12-19 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 88749 | GBP | 2023-12-31 | 2025-12-19 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 299483 | GBP | 2023-12-31 | 2025-12-19 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -74514 | GBP | 2023-12-31 | 2025-12-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10000 | GBP | 2023-12-31 | 2025-12-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity | -64514 | GBP | 2023-12-31 | 2025-12-19 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | -64514 | GBP | 2023-12-31 | 2025-12-19 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## FORCE 4 COMPUTING LIMITED (`gb:03074868`)

- registration: `03074868` (GB), status active, incorporated 1995-07-03
- classification: ['62020'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 76 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | iso4217:GBP | 2025-03-31 | 2025-12-28 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 149468 | GBP | 2025-03-31 | 2025-12-28 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 3063 | GBP | 2025-03-31 | 2025-12-28 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 3369 | GBP | 2025-03-31 | 2025-12-28 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 149162 | GBP | 2025-03-31 | 2025-12-28 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2025-03-31 | 2025-12-28 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 149162 | GBP | 2025-03-31 | 2025-12-28 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 306 | GBP | 2025-03-31 | 2025-12-28 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 306 | GBP | 2025-03-31 | 2025-12-28 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-03-31 | 2025-12-28 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-03-31 | 2024-07-30 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 145352 | GBP | 2024-03-31 | 2025-12-28 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 144627 | GBP | 2024-03-31 | 2024-07-30 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 150 | GBP | 2024-03-31 | 2025-12-28 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 4639 | GBP | 2024-03-31 | 2025-12-28 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 2749 | GBP | 2024-03-31 | 2024-07-30 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | 140861 | GBP | 2024-03-31 | 2024-07-30 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 140861 | GBP | 2024-03-31 | 2025-12-28 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 2 | GBP | 2024-03-31 | 2024-07-30 | filed | no | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 2 | GBP | 2024-03-31 | 2025-12-28 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 140861 | GBP | 2024-03-31 | 2024-07-30 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 140861 | GBP | 2024-03-31 | 2025-12-28 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 4489 | GBP | 2024-03-31 | 2025-12-28 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 139988 | GBP | 2024-03-31 | 2024-07-30 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 139986 | GBP | 2024-03-31 | 2024-07-30 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 4491 | GBP | 2024-03-31 | 2025-12-28 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-03-31 | 2024-07-30 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-03-31 | 2023-12-31 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 130991 | GBP | 2023-03-31 | 2023-12-31 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 130991 | GBP | 2023-03-31 | 2024-07-30 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 3403 | GBP | 2023-03-31 | 2023-12-31 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 3403 | GBP | 2023-03-31 | 2024-07-30 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 126653 | GBP | 2023-03-31 | 2024-07-30 | filed | yes | `uk-core:Equity` | micro-entity |
| equity | 126653 | GBP | 2023-03-31 | 2023-12-31 | filed | no | `uk-core:Equity` | micro-entity |
| fixed_assets | 145 | GBP | 2023-03-31 | 2023-12-31 | filed | no | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 145 | GBP | 2023-03-31 | 2024-07-30 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 126653 | GBP | 2023-03-31 | 2024-07-30 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 126653 | GBP | 2023-03-31 | 2023-12-31 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 125698 | GBP | 2023-03-31 | 2024-07-30 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 125698 | GBP | 2023-03-31 | 2023-12-31 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 125553 | GBP | 2023-03-31 | 2023-12-31 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 125553 | GBP | 2023-03-31 | 2024-07-30 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2022-03-31 | 2023-12-31 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 116222 | GBP | 2022-03-31 | 2023-12-31 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 1856 | GBP | 2022-03-31 | 2023-12-31 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 113688 | GBP | 2022-03-31 | 2023-12-31 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 288 | GBP | 2022-03-31 | 2023-12-31 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 113688 | GBP | 2022-03-31 | 2023-12-31 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 112476 | GBP | 2022-03-31 | 2023-12-31 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 112188 | GBP | 2022-03-31 | 2023-12-31 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2025-12-28: `{"superseded_document_id": "gb:03074868:doc:IpXqvQRCMHlbNfY-4l99BFD22MrV3BhJkcj4UaTbKro", "restatements": [{"concept": "current_assets", "period_end": "2024-03-31", "old_value": "2749.0000", "new_valu`

## VALEMINSTER LIMITED (`gb:03492689`)

- registration: `03492689` (GB), status active, incorporated 1998-01-14
- classification: ['62020'] (sic_2007)
- records: 6 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 79 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | xbrli:pure | 2026-01-31 | 2026-05-28 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 111051 | GBP | 2026-01-31 | 2026-05-28 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| equity | 109801 | GBP | 2026-01-31 | 2026-05-28 | filed | yes | `frs-core:Equity` | micro-entity |
| net_assets | 109801 | GBP | 2026-01-31 | 2026-05-28 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 110161 | GBP | 2026-01-31 | 2026-05-28 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 110161 | GBP | 2026-01-31 | 2026-05-28 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2025-01-31 | 2026-05-28 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | xbrli:pure | 2025-01-31 | 2025-04-30 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 107002 | GBP | 2025-01-31 | 2025-04-30 | filed | no | `frs-core:CurrentAssets` | micro-entity |
| current_assets | 107002 | GBP | 2025-01-31 | 2026-05-28 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| equity | 106007 | GBP | 2025-01-31 | 2025-04-30 | filed | no | `frs-core:Equity` | micro-entity |
| equity | 106007 | GBP | 2025-01-31 | 2026-05-28 | filed | yes | `frs-core:Equity` | micro-entity |
| net_assets | 106007 | GBP | 2025-01-31 | 2025-04-30 | filed | no | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 106007 | GBP | 2025-01-31 | 2026-05-28 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 106361 | GBP | 2025-01-31 | 2026-05-28 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 106361 | GBP | 2025-01-31 | 2025-04-30 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 106361 | GBP | 2025-01-31 | 2026-05-28 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 106361 | GBP | 2025-01-31 | 2025-04-30 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2024-01-31 | 2024-05-08 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | xbrli:pure | 2024-01-31 | 2025-04-30 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 188 | GBP | 2024-01-31 | 2024-05-08 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 103815 | GBP | 2024-01-31 | 2024-05-08 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 103815 | GBP | 2024-01-31 | 2025-04-30 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| equity | 103274 | GBP | 2024-01-31 | 2024-05-08 | filed | no | `core:Equity` | micro-entity |
| equity | 103274 | GBP | 2024-01-31 | 2025-04-30 | filed | yes | `frs-core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2024-01-31 | 2024-05-08 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 103274 | GBP | 2024-01-31 | 2025-04-30 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 103274 | GBP | 2024-01-31 | 2024-05-08 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 103627 | GBP | 2024-01-31 | 2025-04-30 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 103627 | GBP | 2024-01-31 | 2024-05-08 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 103627 | GBP | 2024-01-31 | 2025-04-30 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 103627 | GBP | 2024-01-31 | 2024-05-08 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2023-01-31 | 2024-05-08 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 52 | GBP | 2023-01-31 | 2024-05-08 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 102876 | GBP | 2023-01-31 | 2024-05-08 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 102480 | GBP | 2023-01-31 | 2024-05-08 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 9 | GBP | 2023-01-31 | 2024-05-08 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 102480 | GBP | 2023-01-31 | 2024-05-08 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 102824 | GBP | 2023-01-31 | 2024-05-08 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 102833 | GBP | 2023-01-31 | 2024-05-08 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## AUCTANE, LIMITED (`gb:03870530`)

- registration: `03870530` (GB), status active, incorporated 1999-11-03
- classification: ['62020', '62090'] (sic_2007)
- records: 45 officers, 1 beneficial owners, 1 ownership statements, 6 security interests, 297 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## INTUITIVE SOFTWARE DESIGN LIMITED (`gb:04251429`)

- registration: `04251429` (GB), status active, incorporated 2001-07-12
- classification: ['62012'] (sic_2007)
- records: 6 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 68 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-07-31 | 2026-04-29 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| debtors | 39784 | GBP | 2025-07-31 | 2026-04-29 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 39784 | GBP | 2025-07-31 | 2026-04-29 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2124 | GBP | 2025-07-31 | 2026-04-29 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-07-31 | 2026-04-29 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 2224 | GBP | 2025-07-31 | 2026-04-29 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 2224 | GBP | 2025-07-31 | 2026-04-29 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -1880 | GBP | 2025-07-31 | 2026-04-29 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 3522 | GBP | 2025-07-31 | 2026-04-29 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-07-31 | 2026-04-29 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-07-31 | 2025-04-17 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 0 | GBP | 2024-07-31 | 2025-04-17 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 12941 | GBP | 2024-07-31 | 2025-04-17 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 12941 | GBP | 2024-07-31 | 2025-04-17 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 12941 | GBP | 2024-07-31 | 2025-04-17 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 12941 | GBP | 2024-07-31 | 2026-04-29 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 12941 | GBP | 2024-07-31 | 2026-04-29 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-07-31 | 2026-04-29 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -97 | GBP | 2024-07-31 | 2026-04-29 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -97 | GBP | 2024-07-31 | 2025-04-17 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 3 | GBP | 2024-07-31 | 2025-04-17 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 3 | GBP | 2024-07-31 | 2026-04-29 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-07-31 | 2025-04-17 | filed | no | `ns5:Equity` | total-exemption-full |
| net_assets | 3 | GBP | 2024-07-31 | 2026-04-29 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 3 | GBP | 2024-07-31 | 2025-04-17 | filed | no | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -6174 | GBP | 2024-07-31 | 2025-04-17 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -6174 | GBP | 2024-07-31 | 2026-04-29 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1452 | GBP | 2024-07-31 | 2026-04-29 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1452 | GBP | 2024-07-31 | 2025-04-17 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-07-31 | 2024-03-14 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-07-31 | 2025-04-17 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 32558 | GBP | 2023-07-31 | 2024-03-14 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 32558 | GBP | 2023-07-31 | 2025-04-17 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 62667 | GBP | 2023-07-31 | 2024-03-14 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 62667 | GBP | 2023-07-31 | 2025-04-17 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 30109 | GBP | 2023-07-31 | 2025-04-17 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 30109 | GBP | 2023-07-31 | 2024-03-14 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 30109 | GBP | 2023-07-31 | 2025-04-17 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 30109 | GBP | 2023-07-31 | 2024-03-14 | filed | no | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-07-31 | 2024-03-14 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 24221 | GBP | 2023-07-31 | 2025-04-17 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 24221 | GBP | 2023-07-31 | 2024-03-14 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-07-31 | 2025-04-17 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 24121 | GBP | 2023-07-31 | 2024-03-14 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 24121 | GBP | 2023-07-31 | 2025-04-17 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 24221 | GBP | 2023-07-31 | 2024-03-14 | filed | no | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 24221 | GBP | 2023-07-31 | 2025-04-17 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 15122 | GBP | 2023-07-31 | 2024-03-14 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 15122 | GBP | 2023-07-31 | 2025-04-17 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 26355 | GBP | 2023-07-31 | 2024-03-14 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 26355 | GBP | 2023-07-31 | 2025-04-17 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2022-07-31 | 2024-03-14 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 1710 | GBP | 2022-07-31 | 2024-03-14 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 29265 | GBP | 2022-07-31 | 2024-03-14 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 27555 | GBP | 2022-07-31 | 2024-03-14 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 27555 | GBP | 2022-07-31 | 2024-03-14 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 8002 | GBP | 2022-07-31 | 2024-03-14 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2022-07-31 | 2024-03-14 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 7902 | GBP | 2022-07-31 | 2024-03-14 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 8002 | GBP | 2022-07-31 | 2024-03-14 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 3355 | GBP | 2022-07-31 | 2024-03-14 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 9064 | GBP | 2022-07-31 | 2024-03-14 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## WORLDWIDE BOOK SERVICES LIMITED (`gb:04636376`)

- registration: `04636376` (GB), status active, incorporated 2003-01-14
- classification: ['49410', '52103', '62012', '62090'] (sic_2007)
- records: 13 officers, 6 beneficial owners, 0 ownership statements, 1 security interests, 96 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 41 | xbrli:pure | 2024-12-31 | 2025-07-18 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-12-31 | 2025-07-18 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1754033 | GBP | 2024-12-31 | 2025-07-18 | filed | yes | `core:Equity` | full |
| equity | 1754133 | GBP | 2024-12-31 | 2025-07-18 | filed | yes | `core:Equity` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 58730 | GBP | 2024-12-31 | 2025-07-18 | filed | yes | `core:ProfitLoss` | full |
| average_employees | 37 | xbrli:pure | 2023-12-31 | 2025-07-18 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1815303 | GBP | 2023-12-31 | 2025-07-18 | filed | yes | `core:Equity` | full |
| equity | 1815403 | GBP | 2023-12-31 | 2025-07-18 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-12-31 | 2025-07-18 | filed | yes | `core:Equity` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 544347 | GBP | 2023-12-31 | 2025-07-18 | filed | yes | `core:ProfitLoss` | full |
| equity `{'EquityClassesDimension': 'OtherMiscellaneousReserve'}` | 1722956 | GBP | 2022-12-31 | 2025-07-18 | filed | yes | `core:Equity` | full |

_No coverage facts for the latest run._

## STEDMANRS LIMITED (`gb:05045301`)

- registration: `05045301` (GB), status active, incorporated 2004-02-16
- classification: ['62020'] (sic_2007)
- records: 3 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 50 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2026-02-28 | 2026-04-21 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 70370 | GBP | 2026-02-28 | 2026-04-21 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity | 218928 | GBP | 2026-02-28 | 2026-04-21 | filed | yes | `ns5:Equity` | micro-entity |
| fixed_assets | 148558 | GBP | 2026-02-28 | 2026-04-21 | filed | yes | `ns5:FixedAssets` | micro-entity |
| net_current_assets | 70370 | GBP | 2026-02-28 | 2026-04-21 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 218928 | GBP | 2026-02-28 | 2026-04-21 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2025-02-28 | 2025-04-07 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2025-02-28 | 2026-04-21 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 70900 | GBP | 2025-02-28 | 2026-04-21 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| current_assets | 70900 | GBP | 2025-02-28 | 2025-04-07 | filed | no | `ns5:CurrentAssets` | micro-entity |
| equity | 210297 | GBP | 2025-02-28 | 2026-04-21 | filed | yes | `ns5:Equity` | micro-entity |
| equity | 210297 | GBP | 2025-02-28 | 2025-04-07 | filed | no | `ns5:Equity` | micro-entity |
| fixed_assets | 139359 | GBP | 2025-02-28 | 2026-04-21 | filed | yes | `ns5:FixedAssets` | micro-entity |
| fixed_assets | 139359 | GBP | 2025-02-28 | 2025-04-07 | filed | no | `ns5:FixedAssets` | micro-entity |
| net_current_assets | 70938 | GBP | 2025-02-28 | 2026-04-21 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 70938 | GBP | 2025-02-28 | 2025-04-07 | filed | no | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 210297 | GBP | 2025-02-28 | 2026-04-21 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 210297 | GBP | 2025-02-28 | 2025-04-07 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-02-29 | 2024-04-16 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-02-29 | 2025-04-07 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 82082 | GBP | 2024-02-29 | 2025-04-07 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| current_assets | 82082 | GBP | 2024-02-29 | 2024-04-16 | filed | no | `ns5:CurrentAssets` | micro-entity |
| equity | 208809 | GBP | 2024-02-29 | 2024-04-16 | filed | no | `ns5:Equity` | micro-entity |
| equity | 208809 | GBP | 2024-02-29 | 2025-04-07 | filed | yes | `ns5:Equity` | micro-entity |
| fixed_assets | 127017 | GBP | 2024-02-29 | 2024-04-16 | filed | no | `ns5:FixedAssets` | micro-entity |
| fixed_assets | 127017 | GBP | 2024-02-29 | 2025-04-07 | filed | yes | `ns5:FixedAssets` | micro-entity |
| net_current_assets | 81792 | GBP | 2024-02-29 | 2024-04-16 | filed | no | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 81792 | GBP | 2024-02-29 | 2025-04-07 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 208809 | GBP | 2024-02-29 | 2024-04-16 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 208809 | GBP | 2024-02-29 | 2025-04-07 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-02-28 | 2024-04-16 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 82546 | GBP | 2023-02-28 | 2024-04-16 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity | 204840 | GBP | 2023-02-28 | 2024-04-16 | filed | yes | `ns5:Equity` | micro-entity |
| fixed_assets | 122717 | GBP | 2023-02-28 | 2024-04-16 | filed | yes | `ns5:FixedAssets` | micro-entity |
| net_current_assets | 82123 | GBP | 2023-02-28 | 2024-04-16 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 204840 | GBP | 2023-02-28 | 2024-04-16 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## LITTLE MAN SOLUTIONS LIMITED (`gb:05422173`)

- registration: `05422173` (GB), status active, incorporated 2005-04-12
- classification: ['62020'] (sic_2007)
- records: 3 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 55 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | iso4217:GBP | 2026-03-31 | 2026-04-10 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 12646 | GBP | 2026-03-31 | 2026-04-10 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 134825 | GBP | 2026-03-31 | 2026-04-10 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 110694 | GBP | 2026-03-31 | 2026-04-10 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 6415 | GBP | 2026-03-31 | 2026-04-10 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 110694 | GBP | 2026-03-31 | 2026-04-10 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 122179 | GBP | 2026-03-31 | 2026-04-10 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 128594 | GBP | 2026-03-31 | 2026-04-10 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2025-03-31 | 2025-04-11 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | iso4217:GBP | 2025-03-31 | 2026-04-10 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| cash | 157514 | GBP | 2025-03-31 | 2025-04-11 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 18547 | GBP | 2025-03-31 | 2026-04-10 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 158864 | GBP | 2025-03-31 | 2026-04-10 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 171197 | GBP | 2025-03-31 | 2025-04-11 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 13683 | GBP | 2025-03-31 | 2025-04-11 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 13683 | GBP | 2025-03-31 | 2025-04-11 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 154007 | GBP | 2025-03-31 | 2025-04-11 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 153907 | GBP | 2025-03-31 | 2025-04-11 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-03-31 | 2025-04-11 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 154007 | GBP | 2025-03-31 | 2026-04-10 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 2309 | GBP | 2025-03-31 | 2026-04-10 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 154007 | GBP | 2025-03-31 | 2025-04-11 | filed | no | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 154007 | GBP | 2025-03-31 | 2026-04-10 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 152650 | GBP | 2025-03-31 | 2025-04-11 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 152650 | GBP | 2025-03-31 | 2026-04-10 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 154959 | GBP | 2025-03-31 | 2025-04-11 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 154959 | GBP | 2025-03-31 | 2026-04-10 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-03-31 | 2025-04-11 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-03-31 | 2024-04-23 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 196787 | GBP | 2024-03-31 | 2025-04-11 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 196787 | GBP | 2024-03-31 | 2024-04-23 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 199001 | GBP | 2024-03-31 | 2025-04-11 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 199001 | GBP | 2024-03-31 | 2024-04-23 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 2214 | GBP | 2024-03-31 | 2025-04-11 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 2214 | GBP | 2024-03-31 | 2024-04-23 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 2214 | GBP | 2024-03-31 | 2025-04-11 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2214 | GBP | 2024-03-31 | 2024-04-23 | filed | no | `ns5:Debtors` | total-exemption-full |
| equity | 190933 | GBP | 2024-03-31 | 2024-04-23 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 190933 | GBP | 2024-03-31 | 2025-04-11 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 190833 | GBP | 2024-03-31 | 2025-04-11 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 190833 | GBP | 2024-03-31 | 2024-04-23 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-03-31 | 2024-04-23 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-03-31 | 2025-04-11 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 190933 | GBP | 2024-03-31 | 2024-04-23 | filed | no | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 190933 | GBP | 2024-03-31 | 2025-04-11 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 186242 | GBP | 2024-03-31 | 2024-04-23 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 186242 | GBP | 2024-03-31 | 2025-04-11 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 191961 | GBP | 2024-03-31 | 2025-04-11 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 191961 | GBP | 2024-03-31 | 2024-04-23 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-03-31 | 2024-04-23 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 249276 | GBP | 2023-03-31 | 2024-04-23 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 268136 | GBP | 2023-03-31 | 2024-04-23 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 18860 | GBP | 2023-03-31 | 2024-04-23 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 18860 | GBP | 2023-03-31 | 2024-04-23 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-03-31 | 2024-04-23 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 265466 | GBP | 2023-03-31 | 2024-04-23 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 265566 | GBP | 2023-03-31 | 2024-04-23 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 265566 | GBP | 2023-03-31 | 2024-04-23 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 258959 | GBP | 2023-03-31 | 2024-04-23 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 267028 | GBP | 2023-03-31 | 2024-04-23 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2026-04-10: `{"superseded_document_id": "gb:05422173:doc:pdMh43HwDyBisp_gXQ6dlEvl1qrDOpyEsuPQMYeaEAk", "restatements": [{"concept": "current_assets", "period_end": "2025-03-31", "old_value": "171197.0000", "new_va`

## CADSTUDIOS (UK) LTD (`gb:05833438`)

- registration: `05833438` (GB), status active, incorporated 2006-05-31
- classification: ['71122'] (sic_2007)
- records: 3 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 51 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | iso4217:GBP | 2025-05-31 | 2026-02-16 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2025-05-31 | 2026-02-16 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2025-05-31 | 2026-02-16 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 869 | GBP | 2025-05-31 | 2026-02-16 | filed | yes | `core:CurrentAssets` | micro-entity |
| depreciation_amortisation | 0 | GBP | 2025-05-31 | 2026-02-16 | filed | yes | `core:DepreciationAmortisationImpairmentExpense` | micro-entity |
| equity | 869 | GBP | 2025-05-31 | 2026-02-16 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2025-05-31 | 2026-02-16 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 869 | GBP | 2025-05-31 | 2026-02-16 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 869 | GBP | 2025-05-31 | 2026-02-16 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| profit_for_period | 689 | GBP | 2025-05-31 | 2026-02-16 | filed | yes | `core:ProfitLoss` | micro-entity |
| revenue | 0 | GBP | 2025-05-31 | 2026-02-16 | filed | yes | `core:TurnoverRevenue` | micro-entity |
| staff_costs | 0 | GBP | 2025-05-31 | 2026-02-16 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | micro-entity |
| tax_charge | 0 | GBP | 2025-05-31 | 2026-02-16 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | micro-entity |
| total_assets_less_current_liabilities | 869 | GBP | 2025-05-31 | 2026-02-16 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-05-31 | 2025-02-23 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2024-05-31 | 2026-02-16 | filed | yes | `core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2024-05-31 | 2025-02-23 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2024-05-31 | 2025-02-23 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2024-05-31 | 2026-02-16 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 126 | GBP | 2024-05-31 | 2025-02-23 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 126 | GBP | 2024-05-31 | 2026-02-16 | filed | yes | `core:CurrentAssets` | micro-entity |
| depreciation_amortisation | 0 | GBP | 2024-05-31 | 2026-02-16 | filed | yes | `core:DepreciationAmortisationImpairmentExpense` | micro-entity |
| depreciation_amortisation | 0 | GBP | 2024-05-31 | 2025-02-23 | filed | no | `core:DepreciationAmortisationImpairmentExpense` | micro-entity |
| equity | 126 | GBP | 2024-05-31 | 2025-02-23 | filed | no | `core:Equity` | micro-entity |
| equity | 126 | GBP | 2024-05-31 | 2026-02-16 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2024-05-31 | 2025-02-23 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 0 | GBP | 2024-05-31 | 2026-02-16 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 126 | GBP | 2024-05-31 | 2026-02-16 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 126 | GBP | 2024-05-31 | 2025-02-23 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 126 | GBP | 2024-05-31 | 2026-02-16 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 126 | GBP | 2024-05-31 | 2025-02-23 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| profit_for_period | -140 | GBP | 2024-05-31 | 2025-02-23 | filed | no | `core:ProfitLoss` | micro-entity |
| profit_for_period | -140 | GBP | 2024-05-31 | 2026-02-16 | filed | yes | `core:ProfitLoss` | micro-entity |
| revenue | 0 | GBP | 2024-05-31 | 2026-02-16 | filed | yes | `core:TurnoverRevenue` | micro-entity |
| revenue | 0 | GBP | 2024-05-31 | 2025-02-23 | filed | no | `core:TurnoverRevenue` | micro-entity |
| staff_costs | 0 | GBP | 2024-05-31 | 2025-02-23 | filed | no | `core:StaffCostsEmployeeBenefitsExpense` | micro-entity |
| staff_costs | 0 | GBP | 2024-05-31 | 2026-02-16 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | micro-entity |
| tax_charge | 0 | GBP | 2024-05-31 | 2026-02-16 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | micro-entity |
| tax_charge | 0 | GBP | 2024-05-31 | 2025-02-23 | filed | no | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | micro-entity |
| total_assets_less_current_liabilities | 126 | GBP | 2024-05-31 | 2026-02-16 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 126 | GBP | 2024-05-31 | 2025-02-23 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-05-31 | 2024-01-27 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2023-05-31 | 2024-01-27 | filed | no | `core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2023-05-31 | 2025-02-23 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2023-05-31 | 2025-02-23 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2023-05-31 | 2024-01-27 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 171 | GBP | 2023-05-31 | 2025-02-23 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 171 | GBP | 2023-05-31 | 2024-01-27 | filed | no | `core:CurrentAssets` | micro-entity |
| depreciation_amortisation | 0 | GBP | 2023-05-31 | 2024-01-27 | filed | no | `core:DepreciationAmortisationImpairmentExpense` | micro-entity |
| depreciation_amortisation | 0 | GBP | 2023-05-31 | 2025-02-23 | filed | yes | `core:DepreciationAmortisationImpairmentExpense` | micro-entity |
| equity | 171 | GBP | 2023-05-31 | 2025-02-23 | filed | yes | `core:Equity` | micro-entity |
| equity | 171 | GBP | 2023-05-31 | 2024-01-27 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2023-05-31 | 2025-02-23 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 0 | GBP | 2023-05-31 | 2024-01-27 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | 171 | GBP | 2023-05-31 | 2025-02-23 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 171 | GBP | 2023-05-31 | 2024-01-27 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 171 | GBP | 2023-05-31 | 2025-02-23 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 171 | GBP | 2023-05-31 | 2024-01-27 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| profit_for_period | -502 | GBP | 2023-05-31 | 2024-01-27 | filed | no | `core:ProfitLoss` | micro-entity |
| profit_for_period | -502 | GBP | 2023-05-31 | 2025-02-23 | filed | yes | `core:ProfitLoss` | micro-entity |
| revenue | 0 | GBP | 2023-05-31 | 2024-01-27 | filed | no | `core:TurnoverRevenue` | micro-entity |
| revenue | 0 | GBP | 2023-05-31 | 2025-02-23 | filed | yes | `core:TurnoverRevenue` | micro-entity |
| staff_costs | 0 | GBP | 2023-05-31 | 2025-02-23 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | micro-entity |
| staff_costs | 0 | GBP | 2023-05-31 | 2024-01-27 | filed | no | `core:StaffCostsEmployeeBenefitsExpense` | micro-entity |
| tax_charge | 0 | GBP | 2023-05-31 | 2025-02-23 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | micro-entity |
| tax_charge | 0 | GBP | 2023-05-31 | 2024-01-27 | filed | no | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | micro-entity |
| total_assets_less_current_liabilities | 171 | GBP | 2023-05-31 | 2025-02-23 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 171 | GBP | 2023-05-31 | 2024-01-27 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2022-05-31 | 2024-01-27 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2022-05-31 | 2024-01-27 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 673 | GBP | 2022-05-31 | 2024-01-27 | filed | yes | `core:CurrentAssets` | micro-entity |
| depreciation_amortisation | 0 | GBP | 2022-05-31 | 2024-01-27 | filed | yes | `core:DepreciationAmortisationImpairmentExpense` | micro-entity |
| equity | 673 | GBP | 2022-05-31 | 2024-01-27 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2022-05-31 | 2024-01-27 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 673 | GBP | 2022-05-31 | 2024-01-27 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 673 | GBP | 2022-05-31 | 2024-01-27 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| profit_for_period | 409 | GBP | 2022-05-31 | 2024-01-27 | filed | yes | `core:ProfitLoss` | micro-entity |
| revenue | 576 | GBP | 2022-05-31 | 2024-01-27 | filed | yes | `core:TurnoverRevenue` | micro-entity |
| staff_costs | 0 | GBP | 2022-05-31 | 2024-01-27 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | micro-entity |
| tax_charge | 0 | GBP | 2022-05-31 | 2024-01-27 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | micro-entity |
| total_assets_less_current_liabilities | 673 | GBP | 2022-05-31 | 2024-01-27 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._
