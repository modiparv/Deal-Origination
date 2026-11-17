# Ingest spot-check

- database: `data/engine.db`
- latest run: `20261117T101826Z-daaae260`
- companies in store: 53800; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## FACTORY-FIT (UK) LIMITED (`gb:02842261`)

- registration: `02842261` (GB), status active, incorporated 1993-08-04
- classification: ['71129', '82990'] (sic_2007)
- records: 7 officers, 2 beneficial owners, 0 ownership statements, 1 security interests, 91 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 4 | xbrli:pure | 2025-12-31 | 2026-08-05 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 283283 | GBP | 2025-12-31 | 2026-08-05 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 186593 | GBP | 2025-12-31 | 2026-08-05 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 507483 | GBP | 2025-12-31 | 2026-08-05 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 221200 | GBP | 2025-12-31 | 2026-08-05 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 221200 | GBP | 2025-12-31 | 2026-08-05 | filed | yes | `core:Debtors` | total-exemption-full |
| net_assets | 328399 | GBP | 2025-12-31 | 2026-08-05 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 320890 | GBP | 2025-12-31 | 2026-08-05 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 330902 | GBP | 2025-12-31 | 2026-08-05 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 5 | xbrli:pure | 2024-12-31 | 2025-05-28 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 5 | xbrli:pure | 2024-12-31 | 2026-08-05 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 103275 | GBP | 2024-12-31 | 2026-08-05 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 103275 | GBP | 2024-12-31 | 2025-05-28 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 4396 | GBP | 2024-12-31 | 2025-05-28 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 4396 | GBP | 2024-12-31 | 2026-08-05 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 282816 | GBP | 2024-12-31 | 2025-05-28 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 282816 | GBP | 2024-12-31 | 2026-08-05 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 444958 | GBP | 2024-12-31 | 2025-05-28 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 444958 | GBP | 2024-12-31 | 2026-08-05 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 338683 | GBP | 2024-12-31 | 2026-08-05 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 338683 | GBP | 2024-12-31 | 2025-05-28 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 338683 | GBP | 2024-12-31 | 2025-05-28 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 338683 | GBP | 2024-12-31 | 2026-08-05 | filed | yes | `core:Debtors` | total-exemption-full |
| net_assets | 168033 | GBP | 2024-12-31 | 2026-08-05 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 168033 | GBP | 2024-12-31 | 2025-05-28 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 162142 | GBP | 2024-12-31 | 2026-08-05 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 162142 | GBP | 2024-12-31 | 2025-05-28 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 175858 | GBP | 2024-12-31 | 2026-08-05 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 175858 | GBP | 2024-12-31 | 2025-05-28 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 4 | xbrli:pure | 2023-12-31 | 2024-09-30 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 4 | xbrli:pure | 2023-12-31 | 2025-05-28 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 729190 | GBP | 2023-12-31 | 2025-05-28 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 729190 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 14793 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 14793 | GBP | 2023-12-31 | 2025-05-28 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 728671 | GBP | 2023-12-31 | 2025-05-28 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 728671 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 1242589 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 1242589 | GBP | 2023-12-31 | 2025-05-28 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 510399 | GBP | 2023-12-31 | 2025-05-28 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 510399 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 510399 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 510399 | GBP | 2023-12-31 | 2025-05-28 | filed | yes | `core:Debtors` | total-exemption-full |
| net_assets | 514129 | GBP | 2023-12-31 | 2025-05-28 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 514129 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 513918 | GBP | 2023-12-31 | 2025-05-28 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 513918 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 533924 | GBP | 2023-12-31 | 2025-05-28 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 533924 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 4 | xbrli:pure | 2022-12-31 | 2024-09-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 381992 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 25767 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 274614 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 644323 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 259331 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 259331 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:Debtors` | total-exemption-full |
| net_assets | 351156 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 369709 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 379327 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## S.M.J. CONSULTANCY LIMITED (`gb:03533775`)

- registration: `03533775` (GB), status active, incorporated 1998-03-24
- classification: ['62020', '62090'] (sic_2007)
- records: 5 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 79 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## SAGE ENGINEERING SOLUTIONS LIMITED (`gb:04120390`)

- registration: `04120390` (GB), status active, incorporated 2000-12-06
- classification: ['71129'] (sic_2007)
- records: 7 officers, 2 beneficial owners, 0 ownership statements, 2 security interests, 70 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-12-31 | 2026-09-25 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 256279 | GBP | 2025-12-31 | 2026-09-25 | filed | yes | `ns5:CashBankOnHand` | unaudited-abridged |
| current_assets | 942870 | GBP | 2025-12-31 | 2026-09-25 | filed | yes | `ns5:CurrentAssets` | unaudited-abridged |
| debtors | 686591 | GBP | 2025-12-31 | 2026-09-25 | filed | yes | `ns5:Debtors` | unaudited-abridged |
| equity | 1084362 | GBP | 2025-12-31 | 2026-09-25 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-12-31 | 2026-09-25 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1084262 | GBP | 2025-12-31 | 2026-09-25 | filed | yes | `ns5:Equity` | unaudited-abridged |
| fixed_assets | 336698 | GBP | 2025-12-31 | 2026-09-25 | filed | yes | `ns5:FixedAssets` | unaudited-abridged |
| net_current_assets | 747664 | GBP | 2025-12-31 | 2026-09-25 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 1084362 | GBP | 2025-12-31 | 2026-09-25 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 2 | xbrli:pure | 2024-12-31 | 2026-09-25 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| average_employees | 2 | xbrli:pure | 2024-12-31 | 2025-09-19 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 379482 | GBP | 2024-12-31 | 2026-09-25 | filed | yes | `ns5:CashBankOnHand` | unaudited-abridged |
| cash | 379482 | GBP | 2024-12-31 | 2025-09-19 | filed | no | `ns5:CashBankOnHand` | unaudited-abridged |
| current_assets | 941341 | GBP | 2024-12-31 | 2025-09-19 | filed | no | `ns5:CurrentAssets` | unaudited-abridged |
| current_assets | 941341 | GBP | 2024-12-31 | 2026-09-25 | filed | yes | `ns5:CurrentAssets` | unaudited-abridged |
| debtors | 561859 | GBP | 2024-12-31 | 2025-09-19 | filed | no | `ns5:Debtors` | unaudited-abridged |
| debtors | 561859 | GBP | 2024-12-31 | 2026-09-25 | filed | yes | `ns5:Debtors` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1158446 | GBP | 2024-12-31 | 2026-09-25 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity | 1158546 | GBP | 2024-12-31 | 2026-09-25 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-12-31 | 2025-09-19 | filed | no | `ns5:Equity` | unaudited-abridged |
| equity | 1158546 | GBP | 2024-12-31 | 2025-09-19 | filed | no | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1158446 | GBP | 2024-12-31 | 2025-09-19 | filed | no | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-12-31 | 2026-09-25 | filed | yes | `ns5:Equity` | unaudited-abridged |
| fixed_assets | 347856 | GBP | 2024-12-31 | 2026-09-25 | filed | yes | `ns5:FixedAssets` | unaudited-abridged |
| fixed_assets | 347856 | GBP | 2024-12-31 | 2025-09-19 | filed | no | `ns5:FixedAssets` | unaudited-abridged |
| net_assets | 1158546 | GBP | 2024-12-31 | 2025-09-19 | filed | yes | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 810690 | GBP | 2024-12-31 | 2026-09-25 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 810690 | GBP | 2024-12-31 | 2025-09-19 | filed | no | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 1158546 | GBP | 2024-12-31 | 2025-09-19 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 1158546 | GBP | 2024-12-31 | 2026-09-25 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 2 | xbrli:pure | 2023-12-31 | 2024-09-27 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| average_employees | 2 | xbrli:pure | 2023-12-31 | 2025-09-19 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 202978 | GBP | 2023-12-31 | 2025-09-19 | filed | yes | `ns5:CashBankOnHand` | unaudited-abridged |
| cash | 202978 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `ns5:CashBankOnHand` | unaudited-abridged |
| current_assets | 793451 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `ns5:CurrentAssets` | unaudited-abridged |
| current_assets | 793351 | GBP | 2023-12-31 | 2025-09-19 | filed | yes | `ns5:CurrentAssets` | unaudited-abridged |
| debtors | 490373 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `ns5:Debtors` | unaudited-abridged |
| debtors | 490373 | GBP | 2023-12-31 | 2025-09-19 | filed | yes | `ns5:Debtors` | unaudited-abridged |
| equity | 971093 | GBP | 2023-12-31 | 2025-09-19 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-12-31 | 2025-09-19 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 971091 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 971091 | GBP | 2023-12-31 | 2025-09-19 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity | 971093 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `ns5:Equity` | unaudited-abridged |
| fixed_assets | 359014 | GBP | 2023-12-31 | 2025-09-19 | filed | yes | `ns5:FixedAssets` | unaudited-abridged |
| net_assets | 971093 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_assets | 971093 | GBP | 2023-12-31 | 2025-09-19 | filed | yes | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 649661 | GBP | 2023-12-31 | 2025-09-19 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 649761 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 1008675 | GBP | 2023-12-31 | 2025-09-19 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 1008675 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 2 | xbrli:pure | 2022-12-31 | 2024-09-27 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 170017 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `ns5:CashBankOnHand` | unaudited-abridged |
| current_assets | 802299 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `ns5:CurrentAssets` | unaudited-abridged |
| debtors | 632182 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `ns5:Debtors` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1082055 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity | 1082057 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `ns5:Equity` | unaudited-abridged |
| net_assets | 1082057 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 747110 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 1117182 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |

_No coverage facts for the latest run._

- event restatement @ 2025-09-19: `{"superseded_document_id": "gb:04120390:doc:Llbbfz2vtb7u5fBYU0lSj4I6wJGvpGjM8u3L9Fl7-do", "restatements": [{"concept": "current_assets", "period_end": "2023-12-31", "old_value": "793451.0000", "new_va`

## QUALINET SOLUTIONS LTD (`gb:04716168`)

- registration: `04716168` (GB), status active, incorporated 2003-03-28
- classification: ['62090'] (sic_2007)
- records: 8 officers, 2 beneficial owners, 0 ownership statements, 1 security interests, 80 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 7 | xbrli:pure | 2025-03-31 | 2025-11-28 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 14652 | GBP | 2025-03-31 | 2025-11-28 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 15954 | GBP | 2025-03-31 | 2025-11-28 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 1302 | GBP | 2025-03-31 | 2025-11-28 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 1302 | GBP | 2025-03-31 | 2025-11-28 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 123113 | GBP | 2025-03-31 | 2025-11-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 4995 | GBP | 2025-03-31 | 2025-11-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 57 | GBP | 2025-03-31 | 2025-11-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 128165 | GBP | 2025-03-31 | 2025-11-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| fixed_assets | 127366 | GBP | 2025-03-31 | 2025-11-28 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| net_assets | 128165 | GBP | 2025-03-31 | 2025-11-28 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 827 | GBP | 2025-03-31 | 2025-11-28 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 128193 | GBP | 2025-03-31 | 2025-11-28 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 6 | xbrli:pure | 2024-03-31 | 2024-12-24 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 6 | xbrli:pure | 2024-03-31 | 2025-11-28 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 5144 | GBP | 2024-03-31 | 2024-12-24 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 5144 | GBP | 2024-03-31 | 2025-11-28 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 73242 | GBP | 2024-03-31 | 2025-11-28 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 73242 | GBP | 2024-03-31 | 2024-12-24 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 68098 | GBP | 2024-03-31 | 2024-12-24 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 68098 | GBP | 2024-03-31 | 2025-11-28 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 68098 | GBP | 2024-03-31 | 2024-12-24 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 68098 | GBP | 2024-03-31 | 2025-11-28 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 127278 | GBP | 2024-03-31 | 2025-11-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 4995 | GBP | 2024-03-31 | 2025-11-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 132330 | GBP | 2024-03-31 | 2024-12-24 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 57 | GBP | 2024-03-31 | 2025-11-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 4995 | GBP | 2024-03-31 | 2024-12-24 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 57 | GBP | 2024-03-31 | 2024-12-24 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 132330 | GBP | 2024-03-31 | 2025-11-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 127278 | GBP | 2024-03-31 | 2024-12-24 | filed | no | `ns5:Equity` | total-exemption-full |
| fixed_assets | 121776 | GBP | 2024-03-31 | 2025-11-28 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| fixed_assets | 121776 | GBP | 2024-03-31 | 2024-12-24 | filed | no | `ns5:FixedAssets` | total-exemption-full |
| net_assets | 132330 | GBP | 2024-03-31 | 2024-12-24 | filed | no | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 132330 | GBP | 2024-03-31 | 2025-11-28 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 43500 | GBP | 2024-03-31 | 2024-12-24 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 43500 | GBP | 2024-03-31 | 2025-11-28 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 165276 | GBP | 2024-03-31 | 2025-11-28 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 165276 | GBP | 2024-03-31 | 2024-12-24 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 3 | xbrli:pure | 2023-03-31 | 2024-12-24 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 3 | xbrli:pure | 2023-03-31 | 2023-11-22 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 8437 | GBP | 2023-03-31 | 2023-11-22 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 8437 | GBP | 2023-03-31 | 2024-12-24 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 76181 | GBP | 2023-03-31 | 2024-12-24 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 76181 | GBP | 2023-03-31 | 2023-11-22 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original'}` | 67744 | GBP | 2023-03-31 | 2023-11-22 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 67744 | GBP | 2023-03-31 | 2023-11-22 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 67744 | GBP | 2023-03-31 | 2024-12-24 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 67744 | GBP | 2023-03-31 | 2024-12-24 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'SharePremium'}` | 4995 | GBP | 2023-03-31 | 2023-11-22 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 4995 | GBP | 2023-03-31 | 2024-12-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 87317 | GBP | 2023-03-31 | 2024-12-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 57 | GBP | 2023-03-31 | 2023-11-22 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 95606 | GBP | 2023-03-31 | 2023-11-22 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 92369 | GBP | 2023-03-31 | 2024-12-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 57 | GBP | 2023-03-31 | 2024-12-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 100658 | GBP | 2023-03-31 | 2023-11-22 | filed | yes | `ns5:Equity` | total-exemption-full |
| fixed_assets | 61558 | GBP | 2023-03-31 | 2024-12-24 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| fixed_assets `{'OriginalRevisedDataDimension': 'Original'}` | 70705 | GBP | 2023-03-31 | 2023-11-22 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| net_assets `{'OriginalRevisedDataDimension': 'Original'}` | 100658 | GBP | 2023-03-31 | 2023-11-22 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 92369 | GBP | 2023-03-31 | 2024-12-24 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 61827 | GBP | 2023-03-31 | 2023-11-22 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 62685 | GBP | 2023-03-31 | 2024-12-24 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 124243 | GBP | 2023-03-31 | 2024-12-24 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 132532 | GBP | 2023-03-31 | 2023-11-22 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 3 | xbrli:pure | 2022-03-31 | 2023-11-22 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 52269 | GBP | 2022-03-31 | 2023-11-22 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 80792 | GBP | 2022-03-31 | 2023-11-22 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original'}` | 28523 | GBP | 2022-03-31 | 2023-11-22 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 28523 | GBP | 2022-03-31 | 2023-11-22 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 95305 | GBP | 2022-03-31 | 2023-11-22 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'SharePremium'}` | 4995 | GBP | 2022-03-31 | 2023-11-22 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 100357 | GBP | 2022-03-31 | 2023-11-22 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 57 | GBP | 2022-03-31 | 2023-11-22 | filed | yes | `ns5:Equity` | total-exemption-full |
| fixed_assets `{'OriginalRevisedDataDimension': 'Original'}` | 69619 | GBP | 2022-03-31 | 2023-11-22 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| net_assets `{'OriginalRevisedDataDimension': 'Original'}` | 100357 | GBP | 2022-03-31 | 2023-11-22 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 66460 | GBP | 2022-03-31 | 2023-11-22 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 136079 | GBP | 2022-03-31 | 2023-11-22 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## SANTAROSSA ARCHITECTURE LIMITED (`gb:05336805`)

- registration: `05336805` (GB), status active, incorporated 2005-01-19
- classification: ['71111'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 60 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2026-01-31 | 2026-10-14 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 20817 | GBP | 2026-01-31 | 2026-10-14 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 1867 | GBP | 2026-01-31 | 2026-10-14 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -18269 | GBP | 2026-01-31 | 2026-10-14 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 800 | GBP | 2026-01-31 | 2026-10-14 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | -18269 | GBP | 2026-01-31 | 2026-10-14 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -18950 | GBP | 2026-01-31 | 2026-10-14 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -18150 | GBP | 2026-01-31 | 2026-10-14 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2025-01-31 | 2026-10-14 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2025-01-31 | 2025-08-05 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 19736 | GBP | 2025-01-31 | 2025-08-05 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 19736 | GBP | 2025-01-31 | 2026-10-14 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 1867 | GBP | 2025-01-31 | 2026-10-14 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 1867 | GBP | 2025-01-31 | 2025-08-05 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | -18269 | GBP | 2025-01-31 | 2025-08-05 | filed | no | `core:Equity` | micro-entity |
| equity | -18269 | GBP | 2025-01-31 | 2026-10-14 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 800 | GBP | 2025-01-31 | 2025-08-05 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 800 | GBP | 2025-01-31 | 2026-10-14 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | -18269 | GBP | 2025-01-31 | 2025-08-05 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | -18269 | GBP | 2025-01-31 | 2026-10-14 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -17869 | GBP | 2025-01-31 | 2026-10-14 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -17869 | GBP | 2025-01-31 | 2025-08-05 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -17069 | GBP | 2025-01-31 | 2026-10-14 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -17069 | GBP | 2025-01-31 | 2025-08-05 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-01-31 | 2025-08-05 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-01-31 | 2024-10-24 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 19736 | GBP | 2024-01-31 | 2025-08-05 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 19736 | GBP | 2024-01-31 | 2024-10-24 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 1867 | GBP | 2024-01-31 | 2024-10-24 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 1867 | GBP | 2024-01-31 | 2025-08-05 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -18269 | GBP | 2024-01-31 | 2024-10-24 | filed | no | `core:Equity` | micro-entity |
| equity | -18269 | GBP | 2024-01-31 | 2025-08-05 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 800 | GBP | 2024-01-31 | 2025-08-05 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 800 | GBP | 2024-01-31 | 2024-10-24 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | -18269 | GBP | 2024-01-31 | 2024-10-24 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | -18269 | GBP | 2024-01-31 | 2025-08-05 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -17869 | GBP | 2024-01-31 | 2024-10-24 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -17869 | GBP | 2024-01-31 | 2025-08-05 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -17069 | GBP | 2024-01-31 | 2024-10-24 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -17069 | GBP | 2024-01-31 | 2025-08-05 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-01-31 | 2024-10-24 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 19736 | GBP | 2023-01-31 | 2024-10-24 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 1867 | GBP | 2023-01-31 | 2024-10-24 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -18269 | GBP | 2023-01-31 | 2024-10-24 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 800 | GBP | 2023-01-31 | 2024-10-24 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | -18269 | GBP | 2023-01-31 | 2024-10-24 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -17869 | GBP | 2023-01-31 | 2024-10-24 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -17069 | GBP | 2023-01-31 | 2024-10-24 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2026-10-14: `{"superseded_document_id": "gb:05336805:doc:wRUz6RLvkB73m11sfLuSMTGENTUU18rhckXOopKRRJo", "restatements": [{"concept": "average_employees", "period_end": "2025-01-31", "old_value": "1.0000", "new_valu`

## CREATIVE INTELLIGENCE LIMITED (`gb:05923785`)

- registration: `05923785` (GB), status active, incorporated 2006-09-04
- classification: ['62012', '62020', '63120', '82911'] (sic_2007)
- records: 3 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 69 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 6 | iso4217:GBP | 2025-12-31 | 2026-09-30 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 24158 | GBP | 2025-12-31 | 2026-09-30 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 9308 | GBP | 2025-12-31 | 2026-09-30 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 51811 | GBP | 2025-12-31 | 2026-09-30 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 64638 | GBP | 2025-12-31 | 2026-09-30 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 69076 | GBP | 2025-12-31 | 2026-09-30 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 64638 | GBP | 2025-12-31 | 2026-09-30 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 42503 | GBP | 2025-12-31 | 2026-09-30 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 111579 | GBP | 2025-12-31 | 2026-09-30 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 8 | iso4217:GBP | 2024-12-31 | 2026-09-30 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 8 | iso4217:GBP | 2024-12-31 | 2025-09-30 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 19678 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 19678 | GBP | 2024-12-31 | 2026-09-30 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 17325 | GBP | 2024-12-31 | 2026-09-30 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 17325 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 65740 | GBP | 2024-12-31 | 2026-09-30 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 65740 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 58534 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `core:Equity` | micro-entity |
| equity | 58534 | GBP | 2024-12-31 | 2026-09-30 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 55247 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 55247 | GBP | 2024-12-31 | 2026-09-30 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 58534 | GBP | 2024-12-31 | 2026-09-30 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 58534 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 48415 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 48415 | GBP | 2024-12-31 | 2026-09-30 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 103662 | GBP | 2024-12-31 | 2026-09-30 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 103662 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 7 | iso4217:GBP | 2023-12-31 | 2024-09-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 18245 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 18245 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 15664 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 15664 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 70862 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 70862 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 54394 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:Equity` | micro-entity |
| equity | 54394 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 39501 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 39501 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | 54394 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 54394 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 55198 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 55198 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 94699 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 94699 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 24624 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 13552 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 83180 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 49438 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 22038 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 49438 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 69628 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 91666 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## LINEKERPANDI LIMITED (`gb:06406014`)

- registration: `06406014` (GB), status active, incorporated 2007-10-22
- classification: ['59120', '59200', '62012', '74100'] (sic_2007)
- records: 2 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 43 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-10-31 | 2026-04-21 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 4952 | GBP | 2025-10-31 | 2026-04-21 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 8413 | GBP | 2025-10-31 | 2026-04-21 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 4597 | GBP | 2025-10-31 | 2026-04-21 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 1254 | GBP | 2025-10-31 | 2026-04-21 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 4597 | GBP | 2025-10-31 | 2026-04-21 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 3461 | GBP | 2025-10-31 | 2026-04-21 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 4715 | GBP | 2025-10-31 | 2026-04-21 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-10-31 | 2026-04-21 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-10-31 | 2025-05-12 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5423 | GBP | 2024-10-31 | 2026-04-21 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5423 | GBP | 2024-10-31 | 2025-05-12 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 9442 | GBP | 2024-10-31 | 2026-04-21 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 9442 | GBP | 2024-10-31 | 2025-05-12 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 4342 | GBP | 2024-10-31 | 2025-05-12 | filed | no | `core:Equity` | micro-entity |
| equity | 4342 | GBP | 2024-10-31 | 2026-04-21 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 441 | GBP | 2024-10-31 | 2026-04-21 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 441 | GBP | 2024-10-31 | 2025-05-12 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | 4342 | GBP | 2024-10-31 | 2026-04-21 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 4342 | GBP | 2024-10-31 | 2025-05-12 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 4019 | GBP | 2024-10-31 | 2026-04-21 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 4019 | GBP | 2024-10-31 | 2025-05-12 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 4460 | GBP | 2024-10-31 | 2025-05-12 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 4460 | GBP | 2024-10-31 | 2026-04-21 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-10-31 | 2025-05-12 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-10-31 | 2024-02-19 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5781 | GBP | 2023-10-31 | 2025-05-12 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 8131.96 | GBP | 2023-10-31 | 2024-02-19 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 8132 | GBP | 2023-10-31 | 2025-05-12 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 5391.02 | GBP | 2023-10-31 | 2024-02-19 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 5391 | GBP | 2023-10-31 | 2025-05-12 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 3154 | GBP | 2023-10-31 | 2025-05-12 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 3154.1 | GBP | 2023-10-31 | 2024-02-19 | filed | no | `uk-core:FixedAssets` | micro-entity |
| net_assets | 5391.02 | GBP | 2023-10-31 | 2024-02-19 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 5391 | GBP | 2023-10-31 | 2025-05-12 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 2351 | GBP | 2023-10-31 | 2025-05-12 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 2350.92 | GBP | 2023-10-31 | 2024-02-19 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 5505.02 | GBP | 2023-10-31 | 2024-02-19 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 5505 | GBP | 2023-10-31 | 2025-05-12 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2022-10-31 | 2024-02-19 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 11486.64 | GBP | 2022-10-31 | 2024-02-19 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 12667.71 | GBP | 2022-10-31 | 2024-02-19 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 6213.97 | GBP | 2022-10-31 | 2024-02-19 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 12667.71 | GBP | 2022-10-31 | 2024-02-19 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 6567.74 | GBP | 2022-10-31 | 2024-02-19 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 12781.71 | GBP | 2022-10-31 | 2024-02-19 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2025-05-12: `{"superseded_document_id": "gb:06406014:doc:z7GJ34xkajr5_MYmXd4UHKytm_FCsbeOibLOj4TV1u0", "restatements": [{"concept": "fixed_assets", "period_end": "2023-10-31", "old_value": "3154.1000", "new_value"`

## TECKSTONE LIMITED (`gb:06812469`)

- registration: `06812469` (GB), status active, incorporated 2009-02-06
- classification: ['62020'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 48 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | iso4217:GBP | 2026-02-28 | 2026-08-28 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2026-02-28 | 2026-08-28 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2026-02-28 | 2026-08-28 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 0 | GBP | 2026-02-28 | 2026-08-28 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 6 | GBP | 2026-02-28 | 2026-08-28 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2026-02-28 | 2026-08-28 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 6 | GBP | 2026-02-28 | 2026-08-28 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 0 | GBP | 2026-02-28 | 2026-08-28 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 6 | GBP | 2026-02-28 | 2026-08-28 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2025-02-28 | 2025-10-20 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2025-02-28 | 2026-08-28 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2025-02-28 | 2026-08-28 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2025-02-28 | 2025-10-20 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2025-02-28 | 2025-10-20 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2025-02-28 | 2026-08-28 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 0 | GBP | 2025-02-28 | 2025-10-20 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 0 | GBP | 2025-02-28 | 2026-08-28 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 6 | GBP | 2025-02-28 | 2025-10-20 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 6 | GBP | 2025-02-28 | 2026-08-28 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2025-02-28 | 2025-10-20 | filed | no | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 0 | GBP | 2025-02-28 | 2026-08-28 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 6 | GBP | 2025-02-28 | 2025-10-20 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 6 | GBP | 2025-02-28 | 2026-08-28 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 0 | GBP | 2025-02-28 | 2026-08-28 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 0 | GBP | 2025-02-28 | 2025-10-20 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 6 | GBP | 2025-02-28 | 2026-08-28 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 6 | GBP | 2025-02-28 | 2025-10-20 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-02-28 | 2024-10-14 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2024-02-28 | 2025-10-20 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2024-02-28 | 2024-10-14 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2024-02-28 | 2025-10-20 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2024-02-28 | 2024-10-14 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2024-02-28 | 2025-10-20 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 0 | GBP | 2024-02-28 | 2025-10-20 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 0 | GBP | 2024-02-28 | 2024-10-14 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | 6 | GBP | 2024-02-28 | 2025-10-20 | filed | yes | `uk-core:Equity` | micro-entity |
| equity | 6 | GBP | 2024-02-28 | 2024-10-14 | filed | no | `uk-core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2024-02-28 | 2024-10-14 | filed | no | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 0 | GBP | 2024-02-28 | 2025-10-20 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 6 | GBP | 2024-02-28 | 2025-10-20 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 6 | GBP | 2024-02-28 | 2024-10-14 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 0 | GBP | 2024-02-28 | 2025-10-20 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 0 | GBP | 2024-02-28 | 2024-10-14 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 6 | GBP | 2024-02-28 | 2025-10-20 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 6 | GBP | 2024-02-28 | 2024-10-14 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-02-28 | 2024-10-14 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2023-02-28 | 2024-10-14 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2023-02-28 | 2024-10-14 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 0 | GBP | 2023-02-28 | 2024-10-14 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 6 | GBP | 2023-02-28 | 2024-10-14 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2023-02-28 | 2024-10-14 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 6 | GBP | 2023-02-28 | 2024-10-14 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 0 | GBP | 2023-02-28 | 2024-10-14 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 6 | GBP | 2023-02-28 | 2024-10-14 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2025-10-20: `{"superseded_document_id": "gb:06812469:doc:2-4f-6GMhc4lCKoCeSSXk11QH6rgverqeznhsL2OcL4", "restatements": [{"concept": "average_employees", "period_end": "2024-02-28", "old_value": "1.0000", "new_valu`

## AAROO ASSOCIATES LTD (`gb:07321769`)

- registration: `07321769` (GB), status active, incorporated 2010-07-21
- classification: ['62020'] (sic_2007)
- records: 3 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 40 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | xbrli:pure | 2025-10-31 | 2026-07-27 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 94248 | GBP | 2025-10-31 | 2026-07-27 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 700 | GBP | 2025-10-31 | 2026-07-27 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 80547 | GBP | 2025-10-31 | 2026-07-27 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 14301 | GBP | 2025-10-31 | 2026-07-27 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 100 | GBP | 2025-10-31 | 2026-07-27 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 14301 | GBP | 2025-10-31 | 2026-07-27 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 79847 | GBP | 2025-10-31 | 2026-07-27 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 79947 | GBP | 2025-10-31 | 2026-07-27 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2024-10-31 | 2025-07-21 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | xbrli:pure | 2024-10-31 | 2026-07-27 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 93634 | GBP | 2024-10-31 | 2025-07-21 | filed | no | `core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 93634 | GBP | 2024-10-31 | 2026-07-27 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 403 | GBP | 2024-10-31 | 2025-07-21 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 403 | GBP | 2024-10-31 | 2026-07-27 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 80008 | GBP | 2024-10-31 | 2025-07-21 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 80008 | GBP | 2024-10-31 | 2026-07-27 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 13929 | GBP | 2024-10-31 | 2025-07-21 | filed | no | `core:Equity` | micro-entity |
| equity | 13929 | GBP | 2024-10-31 | 2026-07-27 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 100 | GBP | 2024-10-31 | 2026-07-27 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 100 | GBP | 2024-10-31 | 2025-07-21 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | 13929 | GBP | 2024-10-31 | 2025-07-21 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 13929 | GBP | 2024-10-31 | 2026-07-27 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 79605 | GBP | 2024-10-31 | 2025-07-21 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 79605 | GBP | 2024-10-31 | 2026-07-27 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 79705 | GBP | 2024-10-31 | 2025-07-21 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 79705 | GBP | 2024-10-31 | 2026-07-27 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2023-10-31 | 2025-07-21 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | xbrli:pure | 2023-10-31 | 2024-07-26 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 93114 | GBP | 2023-10-31 | 2025-07-21 | filed | yes | `core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 93114 | GBP | 2023-10-31 | 2024-07-26 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 794 | GBP | 2023-10-31 | 2025-07-21 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 794 | GBP | 2023-10-31 | 2024-07-26 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 81735 | GBP | 2023-10-31 | 2024-07-26 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 81735 | GBP | 2023-10-31 | 2025-07-21 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 12073 | GBP | 2023-10-31 | 2024-07-26 | filed | no | `core:Equity` | micro-entity |
| equity | 12073 | GBP | 2023-10-31 | 2025-07-21 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 100 | GBP | 2023-10-31 | 2025-07-21 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 100 | GBP | 2023-10-31 | 2024-07-26 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | 12073 | GBP | 2023-10-31 | 2025-07-21 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 12073 | GBP | 2023-10-31 | 2024-07-26 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 80941 | GBP | 2023-10-31 | 2024-07-26 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 80941 | GBP | 2023-10-31 | 2025-07-21 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 81041 | GBP | 2023-10-31 | 2025-07-21 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 81041 | GBP | 2023-10-31 | 2024-07-26 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2022-10-31 | 2024-07-26 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 24520 | GBP | 2022-10-31 | 2024-07-26 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 80527 | GBP | 2022-10-31 | 2024-07-26 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 94418 | GBP | 2022-10-31 | 2024-07-26 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 10529 | GBP | 2022-10-31 | 2024-07-26 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 100 | GBP | 2022-10-31 | 2024-07-26 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 10529 | GBP | 2022-10-31 | 2024-07-26 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 13891 | GBP | 2022-10-31 | 2024-07-26 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 13991 | GBP | 2022-10-31 | 2024-07-26 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._
