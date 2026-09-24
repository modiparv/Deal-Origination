# Ingest spot-check

- database: `data/engine.db`
- latest run: `20260924T071946Z-1cede0b8`
- companies in store: 11400; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## ASPENTECH LTD. (`gb:01703614`)

- registration: `01703614` (GB), status active, incorporated 1983-03-02
- classification: ['62020', '62090'] (sic_2007)
- records: 34 officers, 2 beneficial owners, 0 ownership statements, 10 security interests, 279 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## LOGITECH UK LIMITED (`gb:02133170`)

- registration: `02133170` (GB), status active, incorporated 1987-05-20
- classification: ['71121', '71129', '73110', '73200'] (sic_2007)
- records: 28 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 199 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## QUALTEC SYSTEMS LIMITED (`gb:02444962`)

- registration: `02444962` (GB), status active, incorporated 1989-11-21
- classification: ['62020'] (sic_2007)
- records: 2 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 94 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 5 | xbrli:pure | 2024-12-31 | 2025-03-31 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 173205 | GBP | 2024-12-31 | 2025-03-31 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 228239 | GBP | 2024-12-31 | 2025-03-31 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 55034 | GBP | 2024-12-31 | 2025-03-31 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 55034 | GBP | 2024-12-31 | 2025-03-31 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 148477 | GBP | 2024-12-31 | 2025-03-31 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 148579 | GBP | 2024-12-31 | 2025-03-31 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 102 | GBP | 2024-12-31 | 2025-03-31 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 148579 | GBP | 2024-12-31 | 2025-03-31 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 133997 | GBP | 2024-12-31 | 2025-03-31 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 148579 | GBP | 2024-12-31 | 2025-03-31 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 5 | xbrli:pure | 2023-12-31 | 2024-06-07 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 5 | xbrli:pure | 2023-12-31 | 2025-03-31 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 164429 | GBP | 2023-12-31 | 2024-06-07 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 164429 | GBP | 2023-12-31 | 2025-03-31 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 209239 | GBP | 2023-12-31 | 2025-03-31 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 209239 | GBP | 2023-12-31 | 2024-06-07 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 44810 | GBP | 2023-12-31 | 2025-03-31 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 44810 | GBP | 2023-12-31 | 2025-03-31 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 44810 | GBP | 2023-12-31 | 2024-06-07 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 44810 | GBP | 2023-12-31 | 2024-06-07 | filed | no | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 102 | GBP | 2023-12-31 | 2024-06-07 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 133438 | GBP | 2023-12-31 | 2024-06-07 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 133336 | GBP | 2023-12-31 | 2025-03-31 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 102 | GBP | 2023-12-31 | 2025-03-31 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 133336 | GBP | 2023-12-31 | 2024-06-07 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 133438 | GBP | 2023-12-31 | 2025-03-31 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 133438 | GBP | 2023-12-31 | 2025-03-31 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 133438 | GBP | 2023-12-31 | 2024-06-07 | filed | no | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 117820 | GBP | 2023-12-31 | 2024-06-07 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 117820 | GBP | 2023-12-31 | 2025-03-31 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 135229 | GBP | 2023-12-31 | 2025-03-31 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 135229 | GBP | 2023-12-31 | 2024-06-07 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 6 | xbrli:pure | 2022-12-31 | 2024-06-07 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 6 | xbrli:pure | 2022-12-31 | 2023-04-27 | filed | no | `ns6:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 133922 | GBP | 2022-12-31 | 2024-06-07 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 133922 | GBP | 2022-12-31 | 2023-04-27 | filed | no | `ns6:CashBankOnHand` | total-exemption-full |
| current_assets | 209118 | GBP | 2022-12-31 | 2024-06-07 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 209118 | GBP | 2022-12-31 | 2023-04-27 | filed | no | `ns6:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 72223 | GBP | 2022-12-31 | 2023-04-27 | filed | no | `ns6:Debtors` | total-exemption-full |
| debtors | 75196 | GBP | 2022-12-31 | 2024-06-07 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 75196 | GBP | 2022-12-31 | 2023-04-27 | filed | no | `ns6:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 75196 | GBP | 2022-12-31 | 2024-06-07 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 142112 | GBP | 2022-12-31 | 2024-06-07 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 102 | GBP | 2022-12-31 | 2024-06-07 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 142010 | GBP | 2022-12-31 | 2024-06-07 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 142111 | GBP | 2022-12-31 | 2023-04-27 | filed | no | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 142009 | GBP | 2022-12-31 | 2023-04-27 | filed | no | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 102 | GBP | 2022-12-31 | 2023-04-27 | filed | no | `ns6:Equity` | total-exemption-full |
| net_assets | 142111 | GBP | 2022-12-31 | 2023-04-27 | filed | no | `ns6:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 142112 | GBP | 2022-12-31 | 2024-06-07 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 130907 | GBP | 2022-12-31 | 2023-04-27 | filed | no | `ns6:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 126461 | GBP | 2022-12-31 | 2024-06-07 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 147485 | GBP | 2022-12-31 | 2024-06-07 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 151931 | GBP | 2022-12-31 | 2023-04-27 | filed | no | `ns6:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 6 | xbrli:pure | 2021-12-31 | 2023-04-27 | filed | yes | `ns6:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 186531 | GBP | 2021-12-31 | 2023-04-27 | filed | yes | `ns6:CashBankOnHand` | total-exemption-full |
| current_assets | 266860 | GBP | 2021-12-31 | 2023-04-27 | filed | yes | `ns6:CurrentAssets` | total-exemption-full |
| debtors | 80329 | GBP | 2021-12-31 | 2023-04-27 | filed | yes | `ns6:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 77356 | GBP | 2021-12-31 | 2023-04-27 | filed | yes | `ns6:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 102 | GBP | 2021-12-31 | 2023-04-27 | filed | yes | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 181881 | GBP | 2021-12-31 | 2023-04-27 | filed | yes | `ns6:Equity` | total-exemption-full |
| equity | 181983 | GBP | 2021-12-31 | 2023-04-27 | filed | yes | `ns6:Equity` | total-exemption-full |
| net_assets | 181983 | GBP | 2021-12-31 | 2023-04-27 | filed | yes | `ns6:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 179530 | GBP | 2021-12-31 | 2023-04-27 | filed | yes | `ns6:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 186762 | GBP | 2021-12-31 | 2023-04-27 | filed | yes | `ns6:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2024-06-07: `{"superseded_document_id": "gb:02444962:doc:NJDWDtDTDrQDj79quBTteG-5cIe1bZnPV64-coTmcGM", "restatements": [{"concept": "net_current_assets", "period_end": "2022-12-31", "old_value": "130907.0000", "ne`

## PARAGON SIMULATION SERVICES LIMITED (`gb:02695731`)

- registration: `02695731` (GB), status active, incorporated 1992-03-10
- classification: ['62020'] (sic_2007)
- records: 4 officers, 2 beneficial owners, 0 ownership statements, 1 security interests, 83 filings, 2 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.03 | xbrli:pure | 2025-09-30 | 2026-06-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 81202 | GBP | 2025-09-30 | 2026-06-30 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 4506 | GBP | 2025-09-30 | 2026-06-30 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 181942 | GBP | 2025-09-30 | 2026-06-30 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 100740 | GBP | 2025-09-30 | 2026-06-30 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass3'}` | 60 | GBP | 2025-09-30 | 2026-06-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 177534 | GBP | 2025-09-30 | 2026-06-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 160 | GBP | 2025-09-30 | 2026-06-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 50 | GBP | 2025-09-30 | 2026-06-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass2'}` | 50 | GBP | 2025-09-30 | 2026-06-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 177694 | GBP | 2025-09-30 | 2026-06-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShares'}` | 160 | GBP | 2025-09-30 | 2026-06-30 | filed | yes | `core:Equity` | total-exemption-full |
| net_current_assets | 177436 | GBP | 2025-09-30 | 2026-06-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 177694 | GBP | 2025-09-30 | 2026-06-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0.03 | xbrli:pure | 2024-09-30 | 2025-09-29 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 0.03 | xbrli:pure | 2024-09-30 | 2026-06-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 93692 | GBP | 2024-09-30 | 2025-09-29 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 93692 | GBP | 2024-09-30 | 2026-06-30 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1650 | GBP | 2024-09-30 | 2025-09-29 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 11298 | GBP | 2024-09-30 | 2026-06-30 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 193099 | GBP | 2024-09-30 | 2025-09-29 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 191707 | GBP | 2024-09-30 | 2026-06-30 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 99407 | GBP | 2024-09-30 | 2025-09-29 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 98015 | GBP | 2024-09-30 | 2026-06-30 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 99407 | GBP | 2024-09-30 | 2025-09-29 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass2'}` | 50 | GBP | 2024-09-30 | 2025-09-29 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShares'}` | 160 | GBP | 2024-09-30 | 2026-06-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 50 | GBP | 2024-09-30 | 2026-06-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 50 | GBP | 2024-09-30 | 2025-09-29 | filed | no | `core:Equity` | total-exemption-full |
| equity | 193187 | GBP | 2024-09-30 | 2025-09-29 | filed | no | `core:Equity` | total-exemption-full |
| equity | 182147 | GBP | 2024-09-30 | 2026-06-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass3'}` | 60 | GBP | 2024-09-30 | 2026-06-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass2'}` | 50 | GBP | 2024-09-30 | 2026-06-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 160 | GBP | 2024-09-30 | 2026-06-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 181987 | GBP | 2024-09-30 | 2026-06-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass3'}` | 60 | GBP | 2024-09-30 | 2025-09-29 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 193027 | GBP | 2024-09-30 | 2025-09-29 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShares'}` | 160 | GBP | 2024-09-30 | 2025-09-29 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 160 | GBP | 2024-09-30 | 2025-09-29 | filed | no | `core:Equity` | total-exemption-full |
| net_current_assets | 180409 | GBP | 2024-09-30 | 2026-06-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 191449 | GBP | 2024-09-30 | 2025-09-29 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 193187 | GBP | 2024-09-30 | 2025-09-29 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 182147 | GBP | 2024-09-30 | 2026-06-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0.03 | xbrli:pure | 2023-09-30 | 2025-09-29 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 3 | xbrli:pure | 2023-09-30 | 2024-06-25 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 145735 | GBP | 2023-09-30 | 2024-06-25 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 145735 | GBP | 2023-09-30 | 2025-09-29 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2070 | GBP | 2023-09-30 | 2025-09-29 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2070 | GBP | 2023-09-30 | 2024-06-25 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 232409 | GBP | 2023-09-30 | 2025-09-29 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 232409 | GBP | 2023-09-30 | 2024-06-25 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 86674 | GBP | 2023-09-30 | 2024-06-25 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 86674 | GBP | 2023-09-30 | 2025-09-29 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 86674 | GBP | 2023-09-30 | 2025-09-29 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 86674 | GBP | 2023-09-30 | 2024-06-25 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 160 | GBP | 2023-09-30 | 2025-09-29 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 50 | GBP | 2023-09-30 | 2025-09-29 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShares'}` | 160 | GBP | 2023-09-30 | 2024-06-25 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 233397 | GBP | 2023-09-30 | 2025-09-29 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 233397 | GBP | 2023-09-30 | 2024-06-25 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShares'}` | 160 | GBP | 2023-09-30 | 2025-09-29 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass3'}` | 60 | GBP | 2023-09-30 | 2025-09-29 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 233557 | GBP | 2023-09-30 | 2025-09-29 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 160 | GBP | 2023-09-30 | 2024-06-25 | filed | no | `core:Equity` | total-exemption-full |
| equity | 233557 | GBP | 2023-09-30 | 2024-06-25 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass2'}` | 50 | GBP | 2023-09-30 | 2025-09-29 | filed | yes | `core:Equity` | total-exemption-full |
| net_current_assets | 230339 | GBP | 2023-09-30 | 2024-06-25 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 230339 | GBP | 2023-09-30 | 2025-09-29 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 233557 | GBP | 2023-09-30 | 2025-09-29 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 233557 | GBP | 2023-09-30 | 2024-06-25 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2022-09-30 | 2024-06-25 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 10036 | GBP | 2022-09-30 | 2024-06-25 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 24481 | GBP | 2022-09-30 | 2024-06-25 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 175296 | GBP | 2022-09-30 | 2024-06-25 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 165260 | GBP | 2022-09-30 | 2024-06-25 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 165260 | GBP | 2022-09-30 | 2024-06-25 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 150815 | GBP | 2022-09-30 | 2024-06-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 160 | GBP | 2022-09-30 | 2024-06-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShares'}` | 160 | GBP | 2022-09-30 | 2024-06-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 150655 | GBP | 2022-09-30 | 2024-06-25 | filed | yes | `core:Equity` | total-exemption-full |
| net_current_assets | 150815 | GBP | 2022-09-30 | 2024-06-25 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 150815 | GBP | 2022-09-30 | 2024-06-25 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2025-09-29: `{"superseded_document_id": "gb:02695731:doc:QRSJTDEj47ZK-uTmzx_03HCvi16LQqjrQ5oludUJcjY", "restatements": [{"concept": "average_employees", "period_end": "2023-09-30", "old_value": "3.0000", "new_valu`
- event restatement @ 2026-06-30: `{"superseded_document_id": "gb:02695731:doc:rWF8kbL3ud6gVK6RmyIW1Jt0hila281hQtzAIQx375w", "restatements": [{"concept": "debtors", "period_end": "2024-09-30", "old_value": "99407.0000", "new_value": "9`

## MEDISTAT SOFTWARE (UK) LTD. (`gb:02900154`)

- registration: `02900154` (GB), status active, incorporated 1994-02-18
- classification: ['62020'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 75 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-03-31 | 2025-12-17 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 1773 | GBP | 2025-03-31 | 2025-12-17 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity | -4712 | GBP | 2025-03-31 | 2025-12-17 | filed | yes | `ns5:Equity` | micro-entity |
| fixed_assets | 676 | GBP | 2025-03-31 | 2025-12-17 | filed | yes | `ns5:FixedAssets` | micro-entity |
| net_current_assets | -5388 | GBP | 2025-03-31 | 2025-12-17 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -4712 | GBP | 2025-03-31 | 2025-12-17 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-03-31 | 2025-12-17 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-03-31 | 2024-12-23 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 3855 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `ns5:CurrentAssets` | micro-entity |
| current_assets | 3855 | GBP | 2024-03-31 | 2025-12-17 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity | -5645 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `ns5:Equity` | micro-entity |
| equity | -5645 | GBP | 2024-03-31 | 2025-12-17 | filed | yes | `ns5:Equity` | micro-entity |
| fixed_assets | 901 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `ns5:FixedAssets` | micro-entity |
| fixed_assets | 901 | GBP | 2024-03-31 | 2025-12-17 | filed | yes | `ns5:FixedAssets` | micro-entity |
| net_current_assets | -6546 | GBP | 2024-03-31 | 2025-12-17 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -6546 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -5645 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -5645 | GBP | 2024-03-31 | 2025-12-17 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 1 | xbrli:pure | 2023-03-31 | 2023-12-21 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-03-31 | 2024-12-23 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 7282 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 7282 | GBP | 2023-03-31 | 2023-12-21 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | -1008 | GBP | 2023-03-31 | 2023-12-21 | filed | yes | `ns5:Equity` | micro-entity |
| equity | -1008 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `ns5:Equity` | micro-entity |
| fixed_assets `{'OriginalRevisedDataDimension': 'Original'}` | 1201 | GBP | 2023-03-31 | 2023-12-21 | filed | yes | `ns5:FixedAssets` | micro-entity |
| fixed_assets | 1201 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `ns5:FixedAssets` | micro-entity |
| net_current_assets | -2209 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | -2209 | GBP | 2023-03-31 | 2023-12-21 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | -1008 | GBP | 2023-03-31 | 2023-12-21 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -1008 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 1 | xbrli:pure | 2022-03-31 | 2023-12-21 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 3679 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | -12942 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `ns5:Equity` | micro-entity |
| fixed_assets `{'OriginalRevisedDataDimension': 'Original'}` | 1601 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `ns5:FixedAssets` | micro-entity |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | -14543 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | -12942 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |

Coverage @ 2025-03-31: 6/21 concepts available (average_employees, current_assets, equity, fixed_assets, net_current_assets, total_assets_less_current_liabilities)
- `cash`: filed_without_concept — regime 'micro-entity' omits this concept
- `creditors_after_one_year`: filed_without_concept — regime 'micro-entity' omits this concept
- `creditors_within_one_year`: filed_without_concept — absent though regime 'micro-entity' typically includes it
- `debtors`: filed_without_concept — regime 'micro-entity' omits this concept
- `depreciation_amortisation`: filed_without_concept — regime 'micro-entity' omits this concept
- `gross_profit`: filed_without_concept — regime 'micro-entity' omits this concept
- `net_assets`: filed_without_concept — absent though regime 'micro-entity' typically includes it
- `operating_profit`: filed_without_concept — regime 'micro-entity' omits this concept
- `profit_before_tax`: filed_without_concept — regime 'micro-entity' omits this concept
- `profit_for_period`: filed_without_concept — regime 'micro-entity' omits this concept
- `retained_earnings`: filed_without_concept — regime 'micro-entity' omits this concept
- `revenue`: filed_without_concept — regime 'micro-entity' omits this concept
- `share_capital`: filed_without_concept — regime 'micro-entity' omits this concept
- `staff_costs`: filed_without_concept — regime 'micro-entity' omits this concept
- `tax_charge`: filed_without_concept — regime 'micro-entity' omits this concept

## THAMES COMPUTING LIMITED (`gb:03064177`)

- registration: `03064177` (GB), status active, incorporated 1995-06-05
- classification: ['59200', '62012', '74909'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 78 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | iso4217:GBP | 2025-11-30 | 2026-08-27 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 24684 | GBP | 2025-11-30 | 2026-08-27 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 1011 | GBP | 2025-11-30 | 2026-08-27 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 23673 | GBP | 2025-11-30 | 2026-08-27 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 23673 | GBP | 2025-11-30 | 2026-08-27 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 1011 | GBP | 2025-11-30 | 2026-08-27 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 1011 | GBP | 2025-11-30 | 2026-08-27 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2024-11-30 | 2026-08-27 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2024-11-30 | 2025-08-28 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 20984 | GBP | 2024-11-30 | 2026-08-27 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 20984 | GBP | 2024-11-30 | 2025-08-28 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 1793 | GBP | 2024-11-30 | 2026-08-27 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 1793 | GBP | 2024-11-30 | 2025-08-28 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | 19191 | GBP | 2024-11-30 | 2025-08-28 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 19191 | GBP | 2024-11-30 | 2026-08-27 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 19191 | GBP | 2024-11-30 | 2025-08-28 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 19191 | GBP | 2024-11-30 | 2026-08-27 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 1793 | GBP | 2024-11-30 | 2025-08-28 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 1793 | GBP | 2024-11-30 | 2026-08-27 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 1793 | GBP | 2024-11-30 | 2025-08-28 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 1793 | GBP | 2024-11-30 | 2026-08-27 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2023-11-30 | 2024-08-28 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2023-11-30 | 2025-08-28 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 15764 | GBP | 2023-11-30 | 2025-08-28 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 15764 | GBP | 2023-11-30 | 2024-08-28 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 396 | GBP | 2023-11-30 | 2025-08-28 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 396 | GBP | 2023-11-30 | 2024-08-28 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | -15368 | GBP | 2023-11-30 | 2024-08-28 | filed | no | `core:Equity` | micro-entity |
| equity | 15368 | GBP | 2023-11-30 | 2025-08-28 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 15368 | GBP | 2023-11-30 | 2025-08-28 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | -15368 | GBP | 2023-11-30 | 2024-08-28 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 396 | GBP | 2023-11-30 | 2025-08-28 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 396 | GBP | 2023-11-30 | 2024-08-28 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 396 | GBP | 2023-11-30 | 2024-08-28 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 396 | GBP | 2023-11-30 | 2025-08-28 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 12428 | GBP | 2022-11-30 | 2024-08-28 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 601 | GBP | 2022-11-30 | 2024-08-28 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -11827 | GBP | 2022-11-30 | 2024-08-28 | filed | yes | `core:Equity` | micro-entity |
| net_assets | -11827 | GBP | 2022-11-30 | 2024-08-28 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 601 | GBP | 2022-11-30 | 2024-08-28 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 601 | GBP | 2022-11-30 | 2024-08-28 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2025-08-28: `{"superseded_document_id": "gb:03064177:doc:lU4RiFciHcZgDbZlfl_888EGU1wwDZfr4dRVH8W04e0", "restatements": [{"concept": "net_assets", "period_end": "2023-11-30", "old_value": "-15368.0000", "new_value"`

## FINANCIAL SOFTWARE (UK) LIMITED (`gb:03209919`)

- registration: `03209919` (GB), status active, incorporated 1996-06-10
- classification: ['62020', '74909'] (sic_2007)
- records: 7 officers, 3 beneficial owners, 1 ownership statements, 0 security interests, 91 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | iso4217:GBP | 2025-06-30 | 2026-03-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 83775 | GBP | 2025-06-30 | 2026-03-30 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 127603 | GBP | 2025-06-30 | 2026-03-30 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -46172 | GBP | 2025-06-30 | 2026-03-30 | filed | yes | `core:Equity` | micro-entity |
| net_assets | -46172 | GBP | 2025-06-30 | 2026-03-30 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 127603 | GBP | 2025-06-30 | 2026-03-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 127603 | GBP | 2025-06-30 | 2026-03-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2024-06-30 | 2025-03-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 85842 | GBP | 2024-06-30 | 2025-03-30 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 85842 | GBP | 2024-06-30 | 2026-03-30 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 23137 | GBP | 2024-06-30 | 2026-03-30 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 23137 | GBP | 2024-06-30 | 2025-03-30 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | -62705 | GBP | 2024-06-30 | 2026-03-30 | filed | yes | `core:Equity` | micro-entity |
| equity | -62705 | GBP | 2024-06-30 | 2025-03-30 | filed | no | `core:Equity` | micro-entity |
| net_assets | -62705 | GBP | 2024-06-30 | 2026-03-30 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | -62705 | GBP | 2024-06-30 | 2025-03-30 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -62705 | GBP | 2024-06-30 | 2026-03-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -62705 | GBP | 2024-06-30 | 2025-03-30 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -62705 | GBP | 2024-06-30 | 2026-03-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -62705 | GBP | 2024-06-30 | 2025-03-30 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2023-06-30 | 2024-03-27 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2023-06-30 | 2025-03-30 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 76690 | GBP | 2023-06-30 | 2024-03-27 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 76690 | GBP | 2023-06-30 | 2025-03-30 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 17532 | GBP | 2023-06-30 | 2024-03-27 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 17532 | GBP | 2023-06-30 | 2025-03-30 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -59158 | GBP | 2023-06-30 | 2024-03-27 | filed | no | `core:Equity` | micro-entity |
| equity | -59158 | GBP | 2023-06-30 | 2025-03-30 | filed | yes | `core:Equity` | micro-entity |
| net_assets | -59158 | GBP | 2023-06-30 | 2025-03-30 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | -59158 | GBP | 2023-06-30 | 2024-03-27 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -59158 | GBP | 2023-06-30 | 2025-03-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -59158 | GBP | 2023-06-30 | 2024-03-27 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -59158 | GBP | 2023-06-30 | 2024-03-27 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -59158 | GBP | 2023-06-30 | 2025-03-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 61734 | GBP | 2022-06-30 | 2024-03-27 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 21 | GBP | 2022-06-30 | 2024-03-27 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -61713 | GBP | 2022-06-30 | 2024-03-27 | filed | yes | `core:Equity` | micro-entity |
| net_assets | -61713 | GBP | 2022-06-30 | 2024-03-27 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -61713 | GBP | 2022-06-30 | 2024-03-27 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -61713 | GBP | 2022-06-30 | 2024-03-27 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## DISTRIBUTED SYSTEMS PROFESSIONAL SERVICES LIMITED (`gb:03350984`)

- registration: `03350984` (GB), status active, incorporated 1997-04-11
- classification: ['62020'] (sic_2007)
- records: 5 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 80 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | iso4217:GBP | 2025-07-31 | 2026-06-10 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 7818 | GBP | 2025-07-31 | 2026-06-10 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 3490 | GBP | 2025-07-31 | 2026-06-10 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 3715 | GBP | 2025-07-31 | 2026-06-10 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 613 | GBP | 2025-07-31 | 2026-06-10 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 3715 | GBP | 2025-07-31 | 2026-06-10 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 4328 | GBP | 2025-07-31 | 2026-06-10 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 3715 | GBP | 2025-07-31 | 2026-06-10 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-07-31 | 2026-06-10 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-07-31 | 2024-11-12 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 12831 | GBP | 2024-07-31 | 2026-06-10 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 9207 | GBP | 2024-07-31 | 2024-11-12 | filed | no | `ns5:CurrentAssets` | micro-entity |
| current_assets | 9207 | GBP | 2024-07-31 | 2026-06-10 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 2398 | GBP | 2024-07-31 | 2026-06-10 | filed | yes | `uk-core:Equity` | micro-entity |
| equity | -2398 | GBP | 2024-07-31 | 2024-11-12 | filed | no | `ns5:Equity` | micro-entity |
| fixed_assets | 1226 | GBP | 2024-07-31 | 2026-06-10 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 1226 | GBP | 2024-07-31 | 2024-11-12 | filed | no | `ns5:FixedAssets` | micro-entity |
| net_assets | 2398 | GBP | 2024-07-31 | 2026-06-10 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -3624 | GBP | 2024-07-31 | 2024-11-12 | filed | no | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 3624 | GBP | 2024-07-31 | 2026-06-10 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 2398 | GBP | 2024-07-31 | 2026-06-10 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -2398 | GBP | 2024-07-31 | 2024-11-12 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-07-31 | 2024-03-26 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| average_employees | 2 | xbrli:pure | 2023-07-31 | 2024-11-12 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| cash | 12033 | GBP | 2023-07-31 | 2024-03-26 | filed | yes | `ns5:CashBankOnHand` | unaudited-abridged |
| current_assets | 24287 | GBP | 2023-07-31 | 2024-03-26 | filed | no | `ns5:CurrentAssets` | unaudited-abridged |
| current_assets | 24287 | GBP | 2023-07-31 | 2024-11-12 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| debtors | 12254 | GBP | 2023-07-31 | 2024-03-26 | filed | yes | `ns5:Debtors` | unaudited-abridged |
| equity | 8947 | GBP | 2023-07-31 | 2024-11-12 | filed | yes | `ns5:Equity` | micro-entity |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 8946 | GBP | 2023-07-31 | 2024-03-26 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2023-07-31 | 2024-03-26 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity | 8947 | GBP | 2023-07-31 | 2024-03-26 | filed | no | `ns5:Equity` | unaudited-abridged |
| fixed_assets | 2512 | GBP | 2023-07-31 | 2024-11-12 | filed | yes | `ns5:FixedAssets` | micro-entity |
| net_current_assets | 6435 | GBP | 2023-07-31 | 2024-11-12 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 6435 | GBP | 2023-07-31 | 2024-03-26 | filed | no | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 8947 | GBP | 2023-07-31 | 2024-11-12 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 8947 | GBP | 2023-07-31 | 2024-03-26 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 2 | xbrli:pure | 2022-07-31 | 2024-03-26 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 12686 | GBP | 2022-07-31 | 2024-03-26 | filed | yes | `ns5:CashBankOnHand` | unaudited-abridged |
| current_assets | 31330 | GBP | 2022-07-31 | 2024-03-26 | filed | yes | `ns5:CurrentAssets` | unaudited-abridged |
| debtors | 18644 | GBP | 2022-07-31 | 2024-03-26 | filed | yes | `ns5:Debtors` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 8680 | GBP | 2022-07-31 | 2024-03-26 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity | 8681 | GBP | 2022-07-31 | 2024-03-26 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2022-07-31 | 2024-03-26 | filed | yes | `ns5:Equity` | unaudited-abridged |
| net_current_assets | 5051 | GBP | 2022-07-31 | 2024-03-26 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 8681 | GBP | 2022-07-31 | 2024-03-26 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |

Coverage @ 2025-07-31: 8/21 concepts available (average_employees, creditors_within_one_year, current_assets, equity, fixed_assets, net_assets, net_current_assets, total_assets_less_current_liabilities)
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

- event restatement @ 2026-06-10: `{"superseded_document_id": "gb:03350984:doc:RDppl9GmAs7Bz2c45GXmTaUtLxeAsPEBpURMkeIXVHI", "restatements": [{"concept": "net_current_assets", "period_end": "2024-07-31", "old_value": "-3624.0000", "new`

## CRANTOCK LIMITED (`gb:03482300`)

- registration: `03482300` (GB), status active, incorporated 1997-12-17
- classification: ['62020'] (sic_2007)
- records: 5 officers, 2 beneficial owners, 0 ownership statements, 5 security interests, 82 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-12-31 | 2026-07-29 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 5042 | GBP | 2025-12-31 | 2026-07-29 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 6117 | GBP | 2025-12-31 | 2026-07-29 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 1075 | GBP | 2025-12-31 | 2026-07-29 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 733657 | GBP | 2025-12-31 | 2026-07-29 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 460807 | GBP | 2025-12-31 | 2026-07-29 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2025-12-31 | 2026-07-29 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 272848 | GBP | 2025-12-31 | 2026-07-29 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 733657 | GBP | 2025-12-31 | 2026-07-29 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 404 | GBP | 2025-12-31 | 2026-07-29 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1015404 | GBP | 2025-12-31 | 2026-07-29 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-12-31 | 2026-07-29 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-12-31 | 2025-09-09 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 110500 | GBP | 2024-12-31 | 2025-09-09 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 110500 | GBP | 2024-12-31 | 2026-07-29 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 110500 | GBP | 2024-12-31 | 2026-07-29 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 0 | GBP | 2024-12-31 | 2026-07-29 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 559807 | GBP | 2024-12-31 | 2025-09-09 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 307393 | GBP | 2024-12-31 | 2026-07-29 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 867202 | GBP | 2024-12-31 | 2025-09-09 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 307393 | GBP | 2024-12-31 | 2025-09-09 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-12-31 | 2025-09-09 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 867202 | GBP | 2024-12-31 | 2026-07-29 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-12-31 | 2026-07-29 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 559807 | GBP | 2024-12-31 | 2026-07-29 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 867202 | GBP | 2024-12-31 | 2025-09-09 | filed | no | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 867202 | GBP | 2024-12-31 | 2026-07-29 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 7449 | GBP | 2024-12-31 | 2026-07-29 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 7449 | GBP | 2024-12-31 | 2025-09-09 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1154449 | GBP | 2024-12-31 | 2025-09-09 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1154449 | GBP | 2024-12-31 | 2026-07-29 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-12-31 | 2024-09-06 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-12-31 | 2025-09-09 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 22936 | GBP | 2023-12-31 | 2025-09-09 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 22936 | GBP | 2023-12-31 | 2024-09-06 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 232033 | GBP | 2023-12-31 | 2025-09-09 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 531262 | GBP | 2023-12-31 | 2024-09-06 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 232033 | GBP | 2023-12-31 | 2024-09-06 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 763297 | GBP | 2023-12-31 | 2024-09-06 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-12-31 | 2024-09-06 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 531262 | GBP | 2023-12-31 | 2025-09-09 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 763297 | GBP | 2023-12-31 | 2025-09-09 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-12-31 | 2025-09-09 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 763297 | GBP | 2023-12-31 | 2024-09-06 | filed | no | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 763297 | GBP | 2023-12-31 | 2025-09-09 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 9974 | GBP | 2023-12-31 | 2025-09-09 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 9974 | GBP | 2023-12-31 | 2024-09-06 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1234974 | GBP | 2023-12-31 | 2025-09-09 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1234974 | GBP | 2023-12-31 | 2024-09-06 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2022-12-31 | 2024-09-06 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 72899 | GBP | 2022-12-31 | 2024-09-06 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 230887 | GBP | 2022-12-31 | 2024-09-06 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 557015 | GBP | 2022-12-31 | 2024-09-06 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2022-12-31 | 2024-09-06 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 787904 | GBP | 2022-12-31 | 2024-09-06 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 787904 | GBP | 2022-12-31 | 2024-09-06 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 28605 | GBP | 2022-12-31 | 2024-09-06 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1258605 | GBP | 2022-12-31 | 2024-09-06 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._
