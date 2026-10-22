# Ingest spot-check

- database: `data/engine.db`
- latest run: `20261022T071343Z-81f636a1`
- companies in store: 33000; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## PEARLNOTE LIMITED (`gb:02413781`)

- registration: `02413781` (GB), status active, incorporated 1989-08-16
- classification: ['62012'] (sic_2007)
- records: 3 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 92 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-08-31 | 2026-05-28 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 4529 | GBP | 2025-08-31 | 2026-05-28 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 2390 | GBP | 2025-08-31 | 2026-05-28 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 863 | GBP | 2025-08-31 | 2026-05-28 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 3309 | GBP | 2025-08-31 | 2026-05-28 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 863 | GBP | 2025-08-31 | 2026-05-28 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -2139 | GBP | 2025-08-31 | 2026-05-28 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 1170 | GBP | 2025-08-31 | 2026-05-28 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-08-31 | 2026-05-28 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-08-31 | 2025-05-29 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2204 | GBP | 2024-08-31 | 2025-05-29 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2017 | GBP | 2024-08-31 | 2026-05-28 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 2403 | GBP | 2024-08-31 | 2025-05-29 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 2403 | GBP | 2024-08-31 | 2026-05-28 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 3078 | GBP | 2024-08-31 | 2025-05-29 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 3078 | GBP | 2024-08-31 | 2026-05-28 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 2879 | GBP | 2024-08-31 | 2026-05-28 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 2879 | GBP | 2024-08-31 | 2025-05-29 | filed | no | `uk-core:FixedAssets` | micro-entity |
| net_assets | 3078 | GBP | 2024-08-31 | 2025-05-29 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 3078 | GBP | 2024-08-31 | 2026-05-28 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 199 | GBP | 2024-08-31 | 2025-05-29 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 386 | GBP | 2024-08-31 | 2026-05-28 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 3265 | GBP | 2024-08-31 | 2026-05-28 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 3078 | GBP | 2024-08-31 | 2025-05-29 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-08-31 | 2024-05-30 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-08-31 | 2025-05-29 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2949 | GBP | 2023-08-31 | 2025-05-29 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2949 | GBP | 2023-08-31 | 2024-05-30 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 8210 | GBP | 2023-08-31 | 2024-05-30 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 8210 | GBP | 2023-08-31 | 2025-05-29 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 9100 | GBP | 2023-08-31 | 2025-05-29 | filed | yes | `uk-core:Equity` | micro-entity |
| equity | 9100 | GBP | 2023-08-31 | 2024-05-30 | filed | no | `uk-core:Equity` | micro-entity |
| fixed_assets | 3839 | GBP | 2023-08-31 | 2025-05-29 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 3839 | GBP | 2023-08-31 | 2024-05-30 | filed | no | `uk-core:FixedAssets` | micro-entity |
| net_assets | 9100 | GBP | 2023-08-31 | 2025-05-29 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 9100 | GBP | 2023-08-31 | 2024-05-30 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 5261 | GBP | 2023-08-31 | 2025-05-29 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 5261 | GBP | 2023-08-31 | 2024-05-30 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 9100 | GBP | 2023-08-31 | 2024-05-30 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 9100 | GBP | 2023-08-31 | 2025-05-29 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2022-08-31 | 2024-05-30 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 4613 | GBP | 2022-08-31 | 2024-05-30 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 26500 | GBP | 2022-08-31 | 2024-05-30 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 25081 | GBP | 2022-08-31 | 2024-05-30 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 3194 | GBP | 2022-08-31 | 2024-05-30 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 25081 | GBP | 2022-08-31 | 2024-05-30 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 21887 | GBP | 2022-08-31 | 2024-05-30 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 25081 | GBP | 2022-08-31 | 2024-05-30 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2026-05-28: `{"superseded_document_id": "gb:02413781:doc:qQhvj0iDWOBRIplyE7gqHkAC5FKtAvcnVy_Dt75a9tg", "restatements": [{"concept": "creditors_within_one_year", "period_end": "2024-08-31", "old_value": "2204.0000"`

## HEWLETT-PACKARD CDS LIMITED (`gb:03032971`)

- registration: `03032971` (GB), status active, incorporated 1995-03-14
- classification: ['62090'] (sic_2007)
- records: 38 officers, 1 beneficial owners, 0 ownership statements, 1 security interests, 193 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## ENTRUST IT SOUTH WEST LTD (`gb:03443660`)

- registration: `03443660` (GB), status active, incorporated 1997-10-02
- classification: ['62020', '62090', '95110'] (sic_2007)
- records: 8 officers, 2 beneficial owners, 0 ownership statements, 1 security interests, 95 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 8 | xbrli:pure | 2025-03-31 | 2025-09-11 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 787 | GBP | 2025-03-31 | 2025-09-11 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 74882 | GBP | 2025-03-31 | 2025-09-11 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 74095 | GBP | 2025-03-31 | 2025-09-11 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 41280 | GBP | 2025-03-31 | 2025-09-11 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-03-31 | 2025-09-11 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 13395 | GBP | 2025-03-31 | 2025-09-11 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 41380 | GBP | 2025-03-31 | 2025-09-11 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 27985 | GBP | 2025-03-31 | 2025-09-11 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 41380 | GBP | 2025-03-31 | 2025-09-11 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 5 | xbrli:pure | 2024-03-31 | 2024-12-13 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 5 | xbrli:pure | 2024-03-31 | 2025-09-11 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 13416 | GBP | 2024-03-31 | 2024-12-13 | filed | no | `frs-core:CashBankOnHand` | total-exemption-full |
| cash | 13416 | GBP | 2024-03-31 | 2025-09-11 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 43532 | GBP | 2024-03-31 | 2024-12-13 | filed | no | `frs-core:CurrentAssets` | total-exemption-full |
| current_assets | 43532 | GBP | 2024-03-31 | 2025-09-11 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments'}` | 0 | GBP | 2024-03-31 | 2024-12-13 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| debtors | 30116 | GBP | 2024-03-31 | 2024-12-13 | filed | no | `frs-core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 30116 | GBP | 2024-03-31 | 2024-12-13 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| debtors | 30116 | GBP | 2024-03-31 | 2025-09-11 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 32535 | GBP | 2024-03-31 | 2025-09-11 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 32535 | GBP | 2024-03-31 | 2024-12-13 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-03-31 | 2025-09-11 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-03-31 | 2024-12-13 | filed | no | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 2679 | GBP | 2024-03-31 | 2025-09-11 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| fixed_assets | 2679 | GBP | 2024-03-31 | 2024-12-13 | filed | no | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 32635 | GBP | 2024-03-31 | 2024-12-13 | filed | no | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 32635 | GBP | 2024-03-31 | 2025-09-11 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 25205 | GBP | 2024-03-31 | 2024-12-13 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 25205 | GBP | 2024-03-31 | 2025-09-11 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 27884 | GBP | 2024-03-31 | 2024-12-13 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 27884 | GBP | 2024-03-31 | 2025-09-11 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-03-31 | 2023-12-20 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-03-31 | 2024-12-13 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 2290 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `frs-core:CashBankOnHand` | total-exemption-full |
| cash | 2290 | GBP | 2023-03-31 | 2024-12-13 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 26894 | GBP | 2023-03-31 | 2024-12-13 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| current_assets | 26894 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `frs-core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments'}` | 17250 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `frs-core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 7354 | GBP | 2023-03-31 | 2024-12-13 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| debtors | 24604 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `frs-core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments'}` | 17250 | GBP | 2023-03-31 | 2024-12-13 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| debtors | 24604 | GBP | 2023-03-31 | 2024-12-13 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 7354 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 0 | GBP | 2023-03-31 | 2024-12-13 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 26741 | GBP | 2023-03-31 | 2024-12-13 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses', 'RestatementsFirstTimeAdoptionDimension': 'RestatedAmount'}` | 26741 | GBP | 2023-03-31 | 2023-12-20 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 2089 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `frs-core:FixedAssets` | total-exemption-full |
| fixed_assets | 2089 | GBP | 2023-03-31 | 2024-12-13 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 26741 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 26741 | GBP | 2023-03-31 | 2024-12-13 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 24652 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 24652 | GBP | 2023-03-31 | 2024-12-13 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 26741 | GBP | 2023-03-31 | 2024-12-13 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 26741 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2022-03-31 | 2023-12-20 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 6378 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 26743 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 20365 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments'}` | 20000 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 365 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses', 'RestatementsFirstTimeAdoptionDimension': 'RestatedAmount'}` | 26054 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 460 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 26054 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 25594 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 26054 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## ASSEMBLY MEDIA LIMITED (`gb:03799115`)

- registration: `03799115` (GB), status active, incorporated 1999-07-01
- classification: ['62090'] (sic_2007)
- records: 17 officers, 1 beneficial owners, 0 ownership statements, 1 security interests, 93 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.28 | xbrli:pure | 2025-06-30 | 2026-03-25 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 7373533 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:Creditors` | small |
| debtors | 10451087 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:Debtors` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3077552 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 2 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:Equity` | small |
| equity | 3077554 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:Equity` | small |
| net_current_assets | 3077554 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:NetCurrentAssetsLiabilities` | small |
| average_employees | 32 | xbrli:pure | 2024-06-30 | 2025-03-26 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | full |
| average_employees | 0.32 | xbrli:pure | 2024-06-30 | 2026-03-25 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 7559876 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:Creditors` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 7559876 | GBP | 2024-06-30 | 2025-03-26 | filed | no | `core:Creditors` | full |
| current_assets | 9475289 | GBP | 2024-06-30 | 2025-03-26 | filed | yes | `core:CurrentAssets` | full |
| debtors | 9475289 | GBP | 2024-06-30 | 2025-03-26 | filed | no | `core:Debtors` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 9475289 | GBP | 2024-06-30 | 2025-03-26 | filed | yes | `core:Debtors` | full |
| debtors | 9475289 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:Debtors` | small |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 2 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:Equity` | small |
| equity | 1915413 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1915411 | GBP | 2024-06-30 | 2025-03-26 | filed | no | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-06-30 | 2025-03-26 | filed | no | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1915411 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:Equity` | small |
| equity | 1915413 | GBP | 2024-06-30 | 2025-03-26 | filed | no | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:Equity` | small |
| net_current_assets | 1915413 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:NetCurrentAssetsLiabilities` | small |
| net_current_assets | 1915413 | GBP | 2024-06-30 | 2025-03-26 | filed | no | `core:NetCurrentAssetsLiabilities` | full |
| profit_before_tax | 368823 | GBP | 2024-06-30 | 2025-03-26 | filed | yes | `core:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period | 265122 | GBP | 2024-06-30 | 2025-03-26 | filed | yes | `core:ProfitLoss` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 265122 | GBP | 2024-06-30 | 2025-03-26 | filed | yes | `core:ProfitLoss` | full |
| staff_costs | 2547367 | GBP | 2024-06-30 | 2025-03-26 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | full |
| tax_charge | 103701 | GBP | 2024-06-30 | 2025-03-26 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| average_employees | 40 | xbrli:pure | 2023-06-30 | 2025-03-26 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5894348 | GBP | 2023-06-30 | 2025-03-26 | filed | yes | `core:Creditors` | full |
| current_assets | 7544639 | GBP | 2023-06-30 | 2025-03-26 | filed | yes | `core:CurrentAssets` | full |
| debtors | 7484456 | GBP | 2023-06-30 | 2025-03-26 | filed | yes | `core:Debtors` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 7484456 | GBP | 2023-06-30 | 2025-03-26 | filed | yes | `core:Debtors` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1650289 | GBP | 2023-06-30 | 2025-03-26 | filed | yes | `core:Equity` | full |
| equity | 1650291 | GBP | 2023-06-30 | 2025-03-26 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-06-30 | 2025-03-26 | filed | yes | `core:Equity` | full |
| net_current_assets | 1650291 | GBP | 2023-06-30 | 2025-03-26 | filed | yes | `core:NetCurrentAssetsLiabilities` | full |
| profit_before_tax | 474697 | GBP | 2023-06-30 | 2025-03-26 | filed | yes | `core:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period | 372178 | GBP | 2023-06-30 | 2025-03-26 | filed | yes | `core:ProfitLoss` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 372178 | GBP | 2023-06-30 | 2025-03-26 | filed | yes | `core:ProfitLoss` | full |
| staff_costs | 3527968 | GBP | 2023-06-30 | 2025-03-26 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | full |
| tax_charge | 102519 | GBP | 2023-06-30 | 2025-03-26 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2022-06-30 | 2025-03-26 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2778111 | GBP | 2022-06-30 | 2025-03-26 | filed | yes | `core:Equity` | full |

_No coverage facts for the latest run._

- event restatement @ 2026-03-25: `{"superseded_document_id": "gb:03799115:doc:jM6jFfEWgm3xcxLZfYuk9GunTsRQM0izvwEaTNr_X2Y", "restatements": [{"concept": "average_employees", "period_end": "2024-06-30", "old_value": "32.0000", "new_val`

## USE YOUR BRAIN LIMITED (`gb:04162675`)

- registration: `04162675` (GB), status active, incorporated 2001-02-19
- classification: ['62090'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 62 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | iso4217:GBP | 2025-02-28 | 2025-11-17 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 4732 | GBP | 2025-02-28 | 2025-11-17 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 40692 | GBP | 2025-02-28 | 2025-11-17 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 41185 | GBP | 2025-02-28 | 2025-11-17 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 5225 | GBP | 2025-02-28 | 2025-11-17 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 41185 | GBP | 2025-02-28 | 2025-11-17 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 35960 | GBP | 2025-02-28 | 2025-11-17 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 41185 | GBP | 2025-02-28 | 2025-11-17 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-02-28 | 2025-11-17 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-02-28 | 2024-11-20 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 4420 | GBP | 2024-02-28 | 2025-11-17 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 4420 | GBP | 2024-02-28 | 2024-11-20 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 31678 | GBP | 2024-02-28 | 2024-11-20 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 31678 | GBP | 2024-02-28 | 2025-11-17 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 33067 | GBP | 2024-02-28 | 2024-11-20 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 33067 | GBP | 2024-02-28 | 2025-11-17 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 5809 | GBP | 2024-02-28 | 2025-11-17 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 5809 | GBP | 2024-02-28 | 2024-11-20 | filed | no | `uk-core:FixedAssets` | micro-entity |
| net_assets | 33067 | GBP | 2024-02-28 | 2024-11-20 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 33067 | GBP | 2024-02-28 | 2025-11-17 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 27258 | GBP | 2024-02-28 | 2024-11-20 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 27258 | GBP | 2024-02-28 | 2025-11-17 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 33067 | GBP | 2024-02-28 | 2025-11-17 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 33067 | GBP | 2024-02-28 | 2024-11-20 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-02-28 | 2024-11-20 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-02-28 | 2023-11-22 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 4584 | GBP | 2023-02-28 | 2023-11-22 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 4584 | GBP | 2023-02-28 | 2024-11-20 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 24062 | GBP | 2023-02-28 | 2024-11-20 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 24062 | GBP | 2023-02-28 | 2023-11-22 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | 26025 | GBP | 2023-02-28 | 2023-11-22 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 26025 | GBP | 2023-02-28 | 2024-11-20 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 6547 | GBP | 2023-02-28 | 2024-11-20 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 6547 | GBP | 2023-02-28 | 2023-11-22 | filed | no | `uk-core:FixedAssets` | micro-entity |
| net_assets | 26025 | GBP | 2023-02-28 | 2024-11-20 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 26025 | GBP | 2023-02-28 | 2023-11-22 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 19478 | GBP | 2023-02-28 | 2023-11-22 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 19478 | GBP | 2023-02-28 | 2024-11-20 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 26025 | GBP | 2023-02-28 | 2023-11-22 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 26025 | GBP | 2023-02-28 | 2024-11-20 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2022-02-28 | 2023-11-22 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 3570 | GBP | 2022-02-28 | 2023-11-22 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 14435 | GBP | 2022-02-28 | 2023-11-22 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 15733 | GBP | 2022-02-28 | 2023-11-22 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 4868 | GBP | 2022-02-28 | 2023-11-22 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 15733 | GBP | 2022-02-28 | 2023-11-22 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 10865 | GBP | 2022-02-28 | 2023-11-22 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 15733 | GBP | 2022-02-28 | 2023-11-22 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## WAYFINDING CONSULTANTS LTD (`gb:04534084`)

- registration: `04534084` (GB), status active, incorporated 2002-09-12
- classification: ['71111'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 64 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-09-30 | 2026-02-06 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 4291 | GBP | 2025-09-30 | 2026-02-06 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 22731 | GBP | 2025-09-30 | 2026-02-06 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 16862 | GBP | 2025-09-30 | 2026-02-06 | filed | yes | `core:Equity` | micro-entity |
| net_assets | 16862 | GBP | 2025-09-30 | 2026-02-06 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 18440 | GBP | 2025-09-30 | 2026-02-06 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-09-30 | 2026-02-06 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-09-30 | 2025-01-15 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 13430 | GBP | 2024-09-30 | 2025-01-15 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 13430 | GBP | 2024-09-30 | 2026-02-06 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 45230 | GBP | 2024-09-30 | 2025-01-15 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 45230 | GBP | 2024-09-30 | 2026-02-06 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 30270 | GBP | 2024-09-30 | 2026-02-06 | filed | yes | `core:Equity` | micro-entity |
| equity | 30270 | GBP | 2024-09-30 | 2025-01-15 | filed | no | `core:Equity` | micro-entity |
| net_assets | 30270 | GBP | 2024-09-30 | 2026-02-06 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 30270 | GBP | 2024-09-30 | 2025-01-15 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 31800 | GBP | 2024-09-30 | 2025-01-15 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 31800 | GBP | 2024-09-30 | 2026-02-06 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-09-30 | 2025-01-15 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-09-30 | 2024-01-11 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 10481 | GBP | 2023-09-30 | 2024-01-11 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 10481 | GBP | 2023-09-30 | 2025-01-15 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 49690 | GBP | 2023-09-30 | 2025-01-15 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 49690 | GBP | 2023-09-30 | 2024-01-11 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 37859 | GBP | 2023-09-30 | 2024-01-11 | filed | no | `core:Equity` | micro-entity |
| equity | 37859 | GBP | 2023-09-30 | 2025-01-15 | filed | yes | `core:Equity` | micro-entity |
| net_assets | 37859 | GBP | 2023-09-30 | 2024-01-11 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 37859 | GBP | 2023-09-30 | 2025-01-15 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 39209 | GBP | 2023-09-30 | 2025-01-15 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 39209 | GBP | 2023-09-30 | 2024-01-11 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2022-09-30 | 2024-01-11 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2890 | GBP | 2022-09-30 | 2024-01-11 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 34641 | GBP | 2022-09-30 | 2024-01-11 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 30431 | GBP | 2022-09-30 | 2024-01-11 | filed | yes | `core:Equity` | micro-entity |
| net_assets | 30431 | GBP | 2022-09-30 | 2024-01-11 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 31751 | GBP | 2022-09-30 | 2024-01-11 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## IDENTYSOL LIMITED (`gb:04917057`)

- registration: `04917057` (GB), status active, incorporated 2003-10-01
- classification: ['58110', '62011', '62090'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 1 security interests, 67 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-10-31 | 2026-07-31 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| current_assets | 6358 | GBP | 2025-10-31 | 2026-07-31 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 6358 | GBP | 2025-10-31 | 2026-07-31 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 6358 | GBP | 2025-10-31 | 2026-07-31 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -87380 | GBP | 2025-10-31 | 2026-07-31 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | -45891 | GBP | 2025-10-31 | 2026-07-31 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 12160 | GBP | 2025-10-31 | 2026-07-31 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 29329 | GBP | 2025-10-31 | 2026-07-31 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | -45891 | GBP | 2025-10-31 | 2026-07-31 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -45891 | GBP | 2025-10-31 | 2026-07-31 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-10-31 | 2025-10-09 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-10-31 | 2026-07-31 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 0 | GBP | 2024-10-31 | 2025-10-09 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 10020 | GBP | 2024-10-31 | 2026-07-31 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 10020 | GBP | 2024-10-31 | 2025-10-09 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 5942 | GBP | 2024-10-31 | 2025-10-09 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 5942 | GBP | 2024-10-31 | 2026-07-31 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 5942 | GBP | 2024-10-31 | 2026-07-31 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 5942 | GBP | 2024-10-31 | 2025-10-09 | filed | no | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 12160 | GBP | 2024-10-31 | 2025-10-09 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | -44129 | GBP | 2024-10-31 | 2025-10-09 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -85618 | GBP | 2024-10-31 | 2026-07-31 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | -44129 | GBP | 2024-10-31 | 2026-07-31 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 29329 | GBP | 2024-10-31 | 2026-07-31 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 12160 | GBP | 2024-10-31 | 2026-07-31 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 29329 | GBP | 2024-10-31 | 2025-10-09 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -85618 | GBP | 2024-10-31 | 2025-10-09 | filed | no | `ns5:Equity` | total-exemption-full |
| net_current_assets | -44129 | GBP | 2024-10-31 | 2025-10-09 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -44129 | GBP | 2024-10-31 | 2026-07-31 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -44129 | GBP | 2024-10-31 | 2026-07-31 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -44129 | GBP | 2024-10-31 | 2025-10-09 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-10-31 | 2025-10-09 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-10-31 | 2024-04-10 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 4 | GBP | 2023-10-31 | 2024-04-10 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 4 | GBP | 2023-10-31 | 2025-10-09 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 8684 | GBP | 2023-10-31 | 2025-10-09 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 8684 | GBP | 2023-10-31 | 2024-04-10 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 4602 | GBP | 2023-10-31 | 2024-04-10 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 4602 | GBP | 2023-10-31 | 2025-10-09 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 4602 | GBP | 2023-10-31 | 2025-10-09 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 4602 | GBP | 2023-10-31 | 2024-04-10 | filed | no | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 29329 | GBP | 2023-10-31 | 2025-10-09 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -86522 | GBP | 2023-10-31 | 2025-10-09 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | -45033 | GBP | 2023-10-31 | 2024-04-10 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -86522 | GBP | 2023-10-31 | 2024-04-10 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 12160 | GBP | 2023-10-31 | 2025-10-09 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 29329 | GBP | 2023-10-31 | 2024-04-10 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 12160 | GBP | 2023-10-31 | 2024-04-10 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | -45033 | GBP | 2023-10-31 | 2025-10-09 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | -45033 | GBP | 2023-10-31 | 2024-04-10 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -45033 | GBP | 2023-10-31 | 2025-10-09 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -45033 | GBP | 2023-10-31 | 2025-10-09 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -45033 | GBP | 2023-10-31 | 2024-04-10 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2022-10-31 | 2024-04-10 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 4 | GBP | 2022-10-31 | 2024-04-10 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 6390 | GBP | 2022-10-31 | 2024-04-10 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 6386 | GBP | 2022-10-31 | 2024-04-10 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 6386 | GBP | 2022-10-31 | 2024-04-10 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 29329 | GBP | 2022-10-31 | 2024-04-10 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | -32017 | GBP | 2022-10-31 | 2024-04-10 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -73506 | GBP | 2022-10-31 | 2024-04-10 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 12160 | GBP | 2022-10-31 | 2024-04-10 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | -32017 | GBP | 2022-10-31 | 2024-04-10 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -32017 | GBP | 2022-10-31 | 2024-04-10 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## PLANNING ADDITIONS LIMITED (`gb:05283700`)

- registration: `05283700` (GB), status active, incorporated 2004-11-11
- classification: ['71111'] (sic_2007)
- records: 2 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 55 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-11-30 | 2026-09-24 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 105972 | GBP | 2025-11-30 | 2026-09-24 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 106812 | GBP | 2025-11-30 | 2026-09-24 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 840 | GBP | 2025-11-30 | 2026-09-24 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2025-11-30 | 2026-09-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 17180 | GBP | 2025-11-30 | 2026-09-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 17182 | GBP | 2025-11-30 | 2026-09-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 17182 | GBP | 2025-11-30 | 2026-09-24 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 17153 | GBP | 2025-11-30 | 2026-09-24 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 21299 | GBP | 2025-11-30 | 2026-09-24 | filed | yes | `ns5:ProfitLoss` | total-exemption-full |
| total_assets_less_current_liabilities | 17218 | GBP | 2025-11-30 | 2026-09-24 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 3 | xbrli:pure | 2024-11-30 | 2026-09-24 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 3 | xbrli:pure | 2024-11-30 | 2025-09-03 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 89260 | GBP | 2024-11-30 | 2025-09-03 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 89260 | GBP | 2024-11-30 | 2026-09-24 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 90100 | GBP | 2024-11-30 | 2025-09-03 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 90100 | GBP | 2024-11-30 | 2026-09-24 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 840 | GBP | 2024-11-30 | 2025-09-03 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 840 | GBP | 2024-11-30 | 2026-09-24 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-11-30 | 2026-09-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -4119 | GBP | 2024-11-30 | 2025-09-03 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -4119 | GBP | 2024-11-30 | 2026-09-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | -4117 | GBP | 2024-11-30 | 2026-09-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-11-30 | 2025-09-03 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | -4117 | GBP | 2024-11-30 | 2025-09-03 | filed | no | `ns5:Equity` | total-exemption-full |
| net_assets | -4117 | GBP | 2024-11-30 | 2025-09-03 | filed | no | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | -4117 | GBP | 2024-11-30 | 2026-09-24 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -4168 | GBP | 2024-11-30 | 2026-09-24 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -4168 | GBP | 2024-11-30 | 2025-09-03 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 7395 | GBP | 2024-11-30 | 2025-09-03 | filed | yes | `ns5:ProfitLoss` | total-exemption-full |
| total_assets_less_current_liabilities | -4081 | GBP | 2024-11-30 | 2026-09-24 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -4081 | GBP | 2024-11-30 | 2025-09-03 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 3 | xbrli:pure | 2023-11-30 | 2024-11-30 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 3 | xbrli:pure | 2023-11-30 | 2025-09-03 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 76487 | GBP | 2023-11-30 | 2024-11-30 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 76487 | GBP | 2023-11-30 | 2025-09-03 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 77327 | GBP | 2023-11-30 | 2024-11-30 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 77327 | GBP | 2023-11-30 | 2025-09-03 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 840 | GBP | 2023-11-30 | 2025-09-03 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 840 | GBP | 2023-11-30 | 2024-11-30 | filed | no | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 8486 | GBP | 2023-11-30 | 2025-09-03 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 8486 | GBP | 2023-11-30 | 2024-11-30 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-11-30 | 2025-09-03 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 8488 | GBP | 2023-11-30 | 2024-11-30 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-11-30 | 2024-11-30 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 8488 | GBP | 2023-11-30 | 2025-09-03 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 8488 | GBP | 2023-11-30 | 2025-09-03 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 8488 | GBP | 2023-11-30 | 2024-11-30 | filed | no | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 28409 | GBP | 2023-11-30 | 2025-09-03 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 28409 | GBP | 2023-11-30 | 2024-11-30 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 16618 | GBP | 2023-11-30 | 2024-11-30 | filed | yes | `ns5:ProfitLoss` | total-exemption-full |
| total_assets_less_current_liabilities | 28524 | GBP | 2023-11-30 | 2024-11-30 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 28524 | GBP | 2023-11-30 | 2025-09-03 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2022-11-30 | 2024-11-30 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 133855 | GBP | 2022-11-30 | 2024-11-30 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 134695 | GBP | 2022-11-30 | 2024-11-30 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 840 | GBP | 2022-11-30 | 2024-11-30 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 1870 | GBP | 2022-11-30 | 2024-11-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2022-11-30 | 2024-11-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1868 | GBP | 2022-11-30 | 2024-11-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 1870 | GBP | 2022-11-30 | 2024-11-30 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 106205 | GBP | 2022-11-30 | 2024-11-30 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 106359 | GBP | 2022-11-30 | 2024-11-30 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## SAV LONDON LIMITED (`gb:05763681`)

- registration: `05763681` (GB), status active, incorporated 2006-03-31
- classification: ['62090'] (sic_2007)
- records: 2 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 50 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.03 | xbrli:pure | 2025-04-30 | 2025-11-17 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 651447 | GBP | 2025-04-30 | 2025-11-17 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 246578 | GBP | 2025-04-30 | 2025-11-17 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 658694 | GBP | 2025-04-30 | 2025-11-17 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 7247 | GBP | 2025-04-30 | 2025-11-17 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 7247 | GBP | 2025-04-30 | 2025-11-17 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 1250273 | GBP | 2025-04-30 | 2025-11-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2025-04-30 | 2025-11-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 1 | GBP | 2025-04-30 | 2025-11-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3082909 | GBP | 2025-04-30 | 2025-11-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 4333183 | GBP | 2025-04-30 | 2025-11-17 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 3923760 | GBP | 2025-04-30 | 2025-11-17 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | 4333183 | GBP | 2025-04-30 | 2025-11-17 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 412116 | GBP | 2025-04-30 | 2025-11-17 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 4335876 | GBP | 2025-04-30 | 2025-11-17 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 5 | xbrli:pure | 2024-04-30 | 2024-12-24 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 0.05 | xbrli:pure | 2024-04-30 | 2025-11-17 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 323438 | GBP | 2024-04-30 | 2024-12-24 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 323438 | GBP | 2024-04-30 | 2025-11-17 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 224323 | GBP | 2024-04-30 | 2025-11-17 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 224323 | GBP | 2024-04-30 | 2024-12-24 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 334117 | GBP | 2024-04-30 | 2024-12-24 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 334117 | GBP | 2024-04-30 | 2025-11-17 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 10679 | GBP | 2024-04-30 | 2025-11-17 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 10679 | GBP | 2024-04-30 | 2024-12-24 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 10679 | GBP | 2024-04-30 | 2024-12-24 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 10679 | GBP | 2024-04-30 | 2025-11-17 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 3208145 | GBP | 2024-04-30 | 2024-12-24 | filed | no | `core:Equity` | total-exemption-full |
| equity | 3208145 | GBP | 2024-04-30 | 2025-11-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3208144 | GBP | 2024-04-30 | 2024-12-24 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2024-04-30 | 2024-12-24 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3208144 | GBP | 2024-04-30 | 2025-11-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2024-04-30 | 2025-11-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 1 | GBP | 2024-04-30 | 2025-11-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 0 | GBP | 2024-04-30 | 2025-11-17 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 3100950 | GBP | 2024-04-30 | 2025-11-17 | filed | yes | `core:FixedAssets` | total-exemption-full |
| fixed_assets | 3100950 | GBP | 2024-04-30 | 2024-12-24 | filed | no | `core:FixedAssets` | total-exemption-full |
| net_assets | 3208145 | GBP | 2024-04-30 | 2025-11-17 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 3208145 | GBP | 2024-04-30 | 2024-12-24 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 109794 | GBP | 2024-04-30 | 2025-11-17 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 109794 | GBP | 2024-04-30 | 2024-12-24 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 3210744 | GBP | 2024-04-30 | 2025-11-17 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 3210744 | GBP | 2024-04-30 | 2024-12-24 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 5 | xbrli:pure | 2023-04-30 | 2023-12-08 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 5 | xbrli:pure | 2023-04-30 | 2024-12-24 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 494163 | GBP | 2023-04-30 | 2024-12-24 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 494163 | GBP | 2023-04-30 | 2023-12-08 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 217139 | GBP | 2023-04-30 | 2023-12-08 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 217139 | GBP | 2023-04-30 | 2024-12-24 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 606825 | GBP | 2023-04-30 | 2024-12-24 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 606825 | GBP | 2023-04-30 | 2023-12-08 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors | 112662 | GBP | 2023-04-30 | 2024-12-24 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 112662 | GBP | 2023-04-30 | 2023-12-08 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 112662 | GBP | 2023-04-30 | 2023-12-08 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 112662 | GBP | 2023-04-30 | 2024-12-24 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2465266 | GBP | 2023-04-30 | 2023-12-08 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2023-04-30 | 2023-12-08 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 0 | GBP | 2023-04-30 | 2025-11-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 2465267 | GBP | 2023-04-30 | 2024-12-24 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2023-04-30 | 2024-12-24 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 2465267 | GBP | 2023-04-30 | 2023-12-08 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2465266 | GBP | 2023-04-30 | 2024-12-24 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 2078113 | GBP | 2023-04-30 | 2024-12-24 | filed | yes | `core:FixedAssets` | total-exemption-full |
| fixed_assets | 2078113 | GBP | 2023-04-30 | 2023-12-08 | filed | no | `core:FixedAssets` | total-exemption-full |
| net_assets | 2465267 | GBP | 2023-04-30 | 2023-12-08 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 2465267 | GBP | 2023-04-30 | 2024-12-24 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 389686 | GBP | 2023-04-30 | 2024-12-24 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 389686 | GBP | 2023-04-30 | 2023-12-08 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 2467799 | GBP | 2023-04-30 | 2024-12-24 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 2467799 | GBP | 2023-04-30 | 2023-12-08 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 5 | xbrli:pure | 2022-04-30 | 2023-12-08 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 407520 | GBP | 2022-04-30 | 2023-12-08 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 191705 | GBP | 2022-04-30 | 2023-12-08 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 444587 | GBP | 2022-04-30 | 2023-12-08 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 37067 | GBP | 2022-04-30 | 2023-12-08 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 37067 | GBP | 2022-04-30 | 2023-12-08 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 1803813 | GBP | 2022-04-30 | 2023-12-08 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2022-04-30 | 2023-12-08 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1803812 | GBP | 2022-04-30 | 2023-12-08 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 1553505 | GBP | 2022-04-30 | 2023-12-08 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | 1803813 | GBP | 2022-04-30 | 2023-12-08 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 252882 | GBP | 2022-04-30 | 2023-12-08 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1806387 | GBP | 2022-04-30 | 2023-12-08 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

Coverage @ 2025-04-30: 10/21 concepts available (average_employees, cash, creditors_within_one_year, current_assets, debtors, equity, fixed_assets, net_assets, net_current_assets, total_assets_less_current_liabilities)
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

- event restatement @ 2025-11-17: `{"superseded_document_id": "gb:05763681:doc:vUfJUhYkeRXh4dJM95ILlnC1Ioyn5Dmuh-qPMYKAoE4", "restatements": [{"concept": "average_employees", "period_end": "2024-04-30", "old_value": "5.0000", "new_valu`
