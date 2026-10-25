# Ingest spot-check

- database: `data/engine.db`
- latest run: `20261025T072116Z-31749e50`
- companies in store: 35400; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## KINGSLAKE INTERNATIONAL LIMITED (`gb:02470261`)

- registration: `02470261` (GB), status active, incorporated 1990-02-14
- classification: ['62020'] (sic_2007)
- records: 6 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 98 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.02 | xbrli:pure | 2026-03-31 | 2026-07-17 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 291978 | GBP | 2026-03-31 | 2026-07-17 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 529157 | GBP | 2026-03-31 | 2026-07-17 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 519549 | GBP | 2026-03-31 | 2026-07-17 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 227571 | GBP | 2026-03-31 | 2026-07-17 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 227571 | GBP | 2026-03-31 | 2026-07-17 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2877 | GBP | 2026-03-31 | 2026-07-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2026-03-31 | 2026-07-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 100 | GBP | 2026-03-31 | 2026-07-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 2977 | GBP | 2026-03-31 | 2026-07-17 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 12585 | GBP | 2026-03-31 | 2026-07-17 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_current_assets | -9608 | GBP | 2026-03-31 | 2026-07-17 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 2977 | GBP | 2026-03-31 | 2026-07-17 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0.02 | xbrli:pure | 2025-03-31 | 2025-10-13 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 0.02 | xbrli:pure | 2025-03-31 | 2026-07-17 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 644503 | GBP | 2025-03-31 | 2026-07-17 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 644503 | GBP | 2025-03-31 | 2025-10-13 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 585172 | GBP | 2025-03-31 | 2025-10-13 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 585172 | GBP | 2025-03-31 | 2026-07-17 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 865778 | GBP | 2025-03-31 | 2025-10-13 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 865778 | GBP | 2025-03-31 | 2026-07-17 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 221275 | GBP | 2025-03-31 | 2026-07-17 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 221275 | GBP | 2025-03-31 | 2026-07-17 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 221275 | GBP | 2025-03-31 | 2025-10-13 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 221275 | GBP | 2025-03-31 | 2025-10-13 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-03-31 | 2025-10-13 | filed | no | `core:Equity` | total-exemption-full |
| equity | 292475 | GBP | 2025-03-31 | 2026-07-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-03-31 | 2026-07-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 100 | GBP | 2025-03-31 | 2025-10-13 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 292375 | GBP | 2025-03-31 | 2025-10-13 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 292375 | GBP | 2025-03-31 | 2026-07-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 100 | GBP | 2025-03-31 | 2026-07-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 292475 | GBP | 2025-03-31 | 2025-10-13 | filed | no | `core:Equity` | total-exemption-full |
| fixed_assets | 11869 | GBP | 2025-03-31 | 2026-07-17 | filed | yes | `core:FixedAssets` | total-exemption-full |
| fixed_assets | 11869 | GBP | 2025-03-31 | 2025-10-13 | filed | no | `core:FixedAssets` | total-exemption-full |
| net_current_assets | 280606 | GBP | 2025-03-31 | 2025-10-13 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 280606 | GBP | 2025-03-31 | 2026-07-17 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 292475 | GBP | 2025-03-31 | 2025-10-13 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 292475 | GBP | 2025-03-31 | 2026-07-17 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-03-31 | 2024-07-23 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 0.02 | xbrli:pure | 2024-03-31 | 2025-10-13 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 513688 | GBP | 2024-03-31 | 2025-10-13 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 513688 | GBP | 2024-03-31 | 2024-07-23 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 283627 | GBP | 2024-03-31 | 2024-07-23 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 283627 | GBP | 2024-03-31 | 2025-10-13 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 698276 | GBP | 2024-03-31 | 2025-10-13 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 698276 | GBP | 2024-03-31 | 2024-07-23 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors | 184588 | GBP | 2024-03-31 | 2025-10-13 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 184588 | GBP | 2024-03-31 | 2024-07-23 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 184588 | GBP | 2024-03-31 | 2024-07-23 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 184588 | GBP | 2024-03-31 | 2025-10-13 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 426630 | GBP | 2024-03-31 | 2025-10-13 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 426630 | GBP | 2024-03-31 | 2024-07-23 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 426530 | GBP | 2024-03-31 | 2024-07-23 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 426530 | GBP | 2024-03-31 | 2025-10-13 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-03-31 | 2025-10-13 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 100 | GBP | 2024-03-31 | 2025-10-13 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-03-31 | 2024-07-23 | filed | no | `core:Equity` | total-exemption-full |
| fixed_assets | 11981 | GBP | 2024-03-31 | 2025-10-13 | filed | yes | `core:FixedAssets` | total-exemption-full |
| fixed_assets | 11981 | GBP | 2024-03-31 | 2024-07-23 | filed | no | `core:FixedAssets` | total-exemption-full |
| net_current_assets | 414649 | GBP | 2024-03-31 | 2024-07-23 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 414649 | GBP | 2024-03-31 | 2025-10-13 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 426630 | GBP | 2024-03-31 | 2024-07-23 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 426630 | GBP | 2024-03-31 | 2025-10-13 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-03-31 | 2024-07-23 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 394989 | GBP | 2023-03-31 | 2024-07-23 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 292300 | GBP | 2023-03-31 | 2024-07-23 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 721299 | GBP | 2023-03-31 | 2024-07-23 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 326310 | GBP | 2023-03-31 | 2024-07-23 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 326310 | GBP | 2023-03-31 | 2024-07-23 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 441258 | GBP | 2023-03-31 | 2024-07-23 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 441358 | GBP | 2023-03-31 | 2024-07-23 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-03-31 | 2024-07-23 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 12359 | GBP | 2023-03-31 | 2024-07-23 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_current_assets | 428999 | GBP | 2023-03-31 | 2024-07-23 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 441358 | GBP | 2023-03-31 | 2024-07-23 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2025-10-13: `{"superseded_document_id": "gb:02470261:doc:njCN2DrNs7xDcdAV8wcGVvJ-jeEFcdGDTPGBy1OkIBQ", "restatements": [{"concept": "average_employees", "period_end": "2024-03-31", "old_value": "2.0000", "new_valu`

## ASPREY SYSTEMS LTD (`gb:03096767`)

- registration: `03096767` (GB), status active, incorporated 1995-08-31
- classification: ['62090'] (sic_2007)
- records: 5 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 81 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-08-31 | 2026-04-20 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 41245 | GBP | 2025-08-31 | 2026-04-20 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 51957 | GBP | 2025-08-31 | 2026-04-20 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 74046 | GBP | 2025-08-31 | 2026-04-20 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 32801 | GBP | 2025-08-31 | 2026-04-20 | filed | yes | `core:Debtors` | total-exemption-full |
| net_assets | 27656 | GBP | 2025-08-31 | 2026-04-20 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 22089 | GBP | 2025-08-31 | 2026-04-20 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 29512 | GBP | 2025-08-31 | 2026-04-20 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-08-31 | 2025-01-30 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-08-31 | 2026-04-20 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 52033 | GBP | 2024-08-31 | 2025-01-30 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 52033 | GBP | 2024-08-31 | 2026-04-20 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 42798 | GBP | 2024-08-31 | 2026-04-20 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 42798 | GBP | 2024-08-31 | 2025-01-30 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 54697 | GBP | 2024-08-31 | 2026-04-20 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 54697 | GBP | 2024-08-31 | 2025-01-30 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 2664 | GBP | 2024-08-31 | 2026-04-20 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 2664 | GBP | 2024-08-31 | 2025-01-30 | filed | no | `core:Debtors` | total-exemption-full |
| net_assets | 20140 | GBP | 2024-08-31 | 2026-04-20 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 20140 | GBP | 2024-08-31 | 2025-01-30 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 11899 | GBP | 2024-08-31 | 2026-04-20 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 11899 | GBP | 2024-08-31 | 2025-01-30 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 22956 | GBP | 2024-08-31 | 2026-04-20 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 22956 | GBP | 2024-08-31 | 2025-01-30 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-08-31 | 2025-01-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-08-31 | 2024-03-05 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 51614 | GBP | 2023-08-31 | 2025-01-30 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 51614 | GBP | 2023-08-31 | 2024-03-05 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 47084 | GBP | 2023-08-31 | 2024-03-05 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 47084 | GBP | 2023-08-31 | 2025-01-30 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 69484 | GBP | 2023-08-31 | 2024-03-05 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 69484 | GBP | 2023-08-31 | 2025-01-30 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 17870 | GBP | 2023-08-31 | 2025-01-30 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 17870 | GBP | 2023-08-31 | 2024-03-05 | filed | no | `core:Debtors` | total-exemption-full |
| net_assets | 27815 | GBP | 2023-08-31 | 2025-01-30 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 27815 | GBP | 2023-08-31 | 2024-03-05 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 22400 | GBP | 2023-08-31 | 2025-01-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 22400 | GBP | 2023-08-31 | 2024-03-05 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 29085 | GBP | 2023-08-31 | 2025-01-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 29085 | GBP | 2023-08-31 | 2024-03-05 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2022-08-31 | 2024-03-05 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 63223 | GBP | 2022-08-31 | 2024-03-05 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 32277 | GBP | 2022-08-31 | 2024-03-05 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 119388 | GBP | 2022-08-31 | 2024-03-05 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 56165 | GBP | 2022-08-31 | 2024-03-05 | filed | yes | `core:Debtors` | total-exemption-full |
| net_assets | 93260 | GBP | 2022-08-31 | 2024-03-05 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 87111 | GBP | 2022-08-31 | 2024-03-05 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 94703 | GBP | 2022-08-31 | 2024-03-05 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## LOGICWEB LTD (`gb:03519526`)

- registration: `03519526` (GB), status active, incorporated 1998-02-27
- classification: ['61200', '62020', '62090'] (sic_2007)
- records: 5 officers, 0 beneficial owners, 1 ownership statements, 0 security interests, 70 filings, 2 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | iso4217:GBP | 2025-02-28 | 2025-11-30 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 2988 | GBP | 2025-02-28 | 2025-11-30 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 2988 | GBP | 2025-02-28 | 2025-11-30 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 2988 | GBP | 2025-02-28 | 2025-11-30 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 2988 | GBP | 2025-02-28 | 2025-11-30 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 2988 | GBP | 2025-02-28 | 2025-11-30 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2024-02-28 | 2025-11-30 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | pure | 2024-02-28 | 2024-11-30 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 50000 | GBP | 2024-02-28 | 2024-11-30 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 24282 | GBP | 2024-02-28 | 2024-11-30 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 1697 | GBP | 2024-02-28 | 2025-11-30 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 177724 | GBP | 2024-02-28 | 2024-11-30 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | 1697 | GBP | 2024-02-28 | 2025-11-30 | filed | yes | `uk-core:Equity` | micro-entity |
| equity | 103442 | GBP | 2024-02-28 | 2024-11-30 | filed | no | `uk-core:Equity` | micro-entity |
| net_assets | 103442 | GBP | 2024-02-28 | 2024-11-30 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 1697 | GBP | 2024-02-28 | 2025-11-30 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 153442 | GBP | 2024-02-28 | 2024-11-30 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 1697 | GBP | 2024-02-28 | 2025-11-30 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 153442 | GBP | 2024-02-28 | 2024-11-30 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 1697 | GBP | 2024-02-28 | 2025-11-30 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-02-28 | 2023-11-30 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | pure | 2023-02-28 | 2024-11-30 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 50000 | GBP | 2023-02-28 | 2023-11-30 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 50000 | GBP | 2023-02-28 | 2024-11-30 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 19275 | GBP | 2023-02-28 | 2023-11-30 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 24282 | GBP | 2023-02-28 | 2024-11-30 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 172770 | GBP | 2023-02-28 | 2023-11-30 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 177724 | GBP | 2023-02-28 | 2024-11-30 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 103495 | GBP | 2023-02-28 | 2023-11-30 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 103442 | GBP | 2023-02-28 | 2024-11-30 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 103495 | GBP | 2023-02-28 | 2023-11-30 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 103442 | GBP | 2023-02-28 | 2024-11-30 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 153495 | GBP | 2023-02-28 | 2023-11-30 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 153442 | GBP | 2023-02-28 | 2024-11-30 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 153495 | GBP | 2023-02-28 | 2023-11-30 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 153442 | GBP | 2023-02-28 | 2024-11-30 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2022-02-28 | 2023-11-30 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 50000 | GBP | 2022-02-28 | 2023-11-30 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 19275 | GBP | 2022-02-28 | 2023-11-30 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 172770 | GBP | 2022-02-28 | 2023-11-30 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 103495 | GBP | 2022-02-28 | 2023-11-30 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 103495 | GBP | 2022-02-28 | 2023-11-30 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 153495 | GBP | 2022-02-28 | 2023-11-30 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 153495 | GBP | 2022-02-28 | 2023-11-30 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2024-11-30: `{"superseded_document_id": "gb:03519526:doc:UTbqyXIBmVNIjgsfat4nTqr5IWVvsn2a57FGuMfnm10", "restatements": [{"concept": "current_assets", "period_end": "2023-02-28", "old_value": "172770.0000", "new_va`
- event restatement @ 2025-11-30: `{"superseded_document_id": "gb:03519526:doc:O-ptPinWe8QS_H6OTL0ChegoN-mjx-1WEgEP6BHYKoA", "restatements": [{"concept": "current_assets", "period_end": "2024-02-28", "old_value": "177724.0000", "new_va`

## MAYALS MANAGEMENT LIMITED (`gb:03905565`)

- registration: `03905565` (GB), status active, incorporated 2000-01-07
- classification: ['62090'] (sic_2007)
- records: 10 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 98 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | iso4217:GBP | 2025-03-31 | 2025-12-29 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 208267 | GBP | 2025-03-31 | 2025-12-29 | filed | yes | `uk-core:Creditors` | micro-entity |
| equity | 205522 | GBP | 2025-03-31 | 2025-12-29 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 2745 | GBP | 2025-03-31 | 2025-12-29 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 205522 | GBP | 2025-03-31 | 2025-12-29 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 208267 | GBP | 2025-03-31 | 2025-12-29 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 205522 | GBP | 2025-03-31 | 2025-12-29 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2024-03-31 | 2025-12-29 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2024-03-31 | 2024-12-16 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 188630 | GBP | 2024-03-31 | 2025-12-29 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 188630 | GBP | 2024-03-31 | 2024-12-16 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 0 | GBP | 2024-03-31 | 2024-12-16 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 185304 | GBP | 2024-03-31 | 2024-12-16 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 185304 | GBP | 2024-03-31 | 2025-12-29 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 3326 | GBP | 2024-03-31 | 2024-12-16 | filed | no | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 3326 | GBP | 2024-03-31 | 2025-12-29 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 185304 | GBP | 2024-03-31 | 2025-12-29 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 185304 | GBP | 2024-03-31 | 2024-12-16 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 188630 | GBP | 2024-03-31 | 2025-12-29 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 188630 | GBP | 2024-03-31 | 2024-12-16 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 185304 | GBP | 2024-03-31 | 2025-12-29 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 185304 | GBP | 2024-03-31 | 2024-12-16 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2023-03-31 | 2024-12-16 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 3 | iso4217:GBP | 2023-03-31 | 2024-03-26 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 164080 | GBP | 2023-03-31 | 2024-03-26 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 164080 | GBP | 2023-03-31 | 2024-12-16 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 650 | GBP | 2023-03-31 | 2024-03-26 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 650 | GBP | 2023-03-31 | 2024-12-16 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 159372 | GBP | 2023-03-31 | 2024-12-16 | filed | yes | `uk-core:Equity` | micro-entity |
| equity | 159372 | GBP | 2023-03-31 | 2024-03-26 | filed | no | `uk-core:Equity` | micro-entity |
| fixed_assets | 4058 | GBP | 2023-03-31 | 2024-03-26 | filed | no | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 4058 | GBP | 2023-03-31 | 2024-12-16 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 159372 | GBP | 2023-03-31 | 2024-03-26 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 159372 | GBP | 2023-03-31 | 2024-12-16 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 163430 | GBP | 2023-03-31 | 2024-12-16 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 163430 | GBP | 2023-03-31 | 2024-03-26 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 159372 | GBP | 2023-03-31 | 2024-12-16 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 159372 | GBP | 2023-03-31 | 2024-03-26 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 3 | iso4217:GBP | 2022-03-31 | 2024-03-26 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 132249 | GBP | 2022-03-31 | 2024-03-26 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 734 | GBP | 2022-03-31 | 2024-03-26 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 126636 | GBP | 2022-03-31 | 2024-03-26 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 4879 | GBP | 2022-03-31 | 2024-03-26 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 126636 | GBP | 2022-03-31 | 2024-03-26 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 131515 | GBP | 2022-03-31 | 2024-03-26 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 126636 | GBP | 2022-03-31 | 2024-03-26 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2024-12-16: `{"superseded_document_id": "gb:03905565:doc:xiJL4r4Mf7nQfYFv3sItRFyT6ZuTQ6-LbYLJ2P2mrHY", "restatements": [{"concept": "average_employees", "period_end": "2023-03-31", "old_value": "3.0000", "new_valu`

## CHRIS STAPLE ASSOCIATES LIMITED (`gb:04297943`)

- registration: `04297943` (GB), status active, incorporated 2001-10-03
- classification: ['62090'] (sic_2007)
- records: 6 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 61 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-10-31 | 2026-07-15 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 10247 | GBP | 2025-10-31 | 2026-07-15 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 21461 | GBP | 2025-10-31 | 2026-07-15 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 8214 | GBP | 2025-10-31 | 2026-07-15 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 8214 | GBP | 2025-10-31 | 2026-07-15 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1237 | GBP | 2025-10-31 | 2026-07-15 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 1239 | GBP | 2025-10-31 | 2026-07-15 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2025-10-31 | 2026-07-15 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | 1213 | GBP | 2025-10-31 | 2026-07-15 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1239 | GBP | 2025-10-31 | 2026-07-15 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-10-31 | 2025-07-06 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-10-31 | 2026-07-15 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 7059 | GBP | 2024-10-31 | 2026-07-15 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 7059 | GBP | 2024-10-31 | 2025-07-06 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 11808 | GBP | 2024-10-31 | 2026-07-15 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 11808 | GBP | 2024-10-31 | 2025-07-06 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 749 | GBP | 2024-10-31 | 2025-07-06 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 749 | GBP | 2024-10-31 | 2026-07-15 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 749 | GBP | 2024-10-31 | 2025-07-06 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 749 | GBP | 2024-10-31 | 2026-07-15 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 568 | GBP | 2024-10-31 | 2025-07-06 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 566 | GBP | 2024-10-31 | 2026-07-15 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 566 | GBP | 2024-10-31 | 2025-07-06 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-10-31 | 2026-07-15 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-10-31 | 2025-07-06 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 568 | GBP | 2024-10-31 | 2026-07-15 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | 536 | GBP | 2024-10-31 | 2026-07-15 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 536 | GBP | 2024-10-31 | 2025-07-06 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 568 | GBP | 2024-10-31 | 2026-07-15 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 568 | GBP | 2024-10-31 | 2025-07-06 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-10-31 | 2025-07-06 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-10-31 | 2024-07-08 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 1593 | GBP | 2023-10-31 | 2025-07-06 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 1593 | GBP | 2023-10-31 | 2024-07-08 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 9968 | GBP | 2023-10-31 | 2025-07-06 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 9968 | GBP | 2023-10-31 | 2024-07-08 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 375 | GBP | 2023-10-31 | 2025-07-06 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 375 | GBP | 2023-10-31 | 2024-07-08 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 375 | GBP | 2023-10-31 | 2024-07-08 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 375 | GBP | 2023-10-31 | 2025-07-06 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 236 | GBP | 2023-10-31 | 2025-07-06 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 234 | GBP | 2023-10-31 | 2024-07-08 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 234 | GBP | 2023-10-31 | 2025-07-06 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 236 | GBP | 2023-10-31 | 2024-07-08 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-10-31 | 2025-07-06 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-10-31 | 2024-07-08 | filed | no | `ns5:Equity` | total-exemption-full |
| net_current_assets | 195 | GBP | 2023-10-31 | 2025-07-06 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 195 | GBP | 2023-10-31 | 2024-07-08 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 236 | GBP | 2023-10-31 | 2024-07-08 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 236 | GBP | 2023-10-31 | 2025-07-06 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2022-10-31 | 2024-07-08 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 22726 | GBP | 2022-10-31 | 2024-07-08 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 31563 | GBP | 2022-10-31 | 2024-07-08 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 837 | GBP | 2022-10-31 | 2024-07-08 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 837 | GBP | 2022-10-31 | 2024-07-08 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 11950 | GBP | 2022-10-31 | 2024-07-08 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 11952 | GBP | 2022-10-31 | 2024-07-08 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2022-10-31 | 2024-07-08 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | 11899 | GBP | 2022-10-31 | 2024-07-08 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 11952 | GBP | 2022-10-31 | 2024-07-08 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## BLUESKY SOFTWARE AND SOLUTIONS LTD (`gb:04688923`)

- registration: `04688923` (GB), status active, incorporated 2003-03-06
- classification: ['62090'] (sic_2007)
- records: 6 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 60 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | iso4217:GBP | 2025-03-31 | 2025-12-11 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 53359 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 181507 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 128638 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 490 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 128638 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 128148 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 128638 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-03-31 | 2024-11-25 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-03-31 | 2025-12-11 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 48377 | GBP | 2024-03-31 | 2024-11-25 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 48377 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 133677 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 133677 | GBP | 2024-03-31 | 2024-11-25 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | 86674 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `uk-core:Equity` | micro-entity |
| equity | 86674 | GBP | 2024-03-31 | 2024-11-25 | filed | no | `uk-core:Equity` | micro-entity |
| fixed_assets | 1374 | GBP | 2024-03-31 | 2024-11-25 | filed | no | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 1374 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 86674 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 86674 | GBP | 2024-03-31 | 2024-11-25 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 85300 | GBP | 2024-03-31 | 2024-11-25 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 85300 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 86674 | GBP | 2024-03-31 | 2024-11-25 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 86674 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-03-31 | 2024-11-25 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-03-31 | 2023-12-12 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 50859 | GBP | 2023-03-31 | 2023-12-12 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 50859 | GBP | 2023-03-31 | 2024-11-25 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 130977 | GBP | 2023-03-31 | 2023-12-12 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 130977 | GBP | 2023-03-31 | 2024-11-25 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 81717 | GBP | 2023-03-31 | 2023-12-12 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 81717 | GBP | 2023-03-31 | 2024-11-25 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 1599 | GBP | 2023-03-31 | 2023-12-12 | filed | no | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 1599 | GBP | 2023-03-31 | 2024-11-25 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 81717 | GBP | 2023-03-31 | 2024-11-25 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 81717 | GBP | 2023-03-31 | 2023-12-12 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 80118 | GBP | 2023-03-31 | 2024-11-25 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 80118 | GBP | 2023-03-31 | 2023-12-12 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 81717 | GBP | 2023-03-31 | 2023-12-12 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 81717 | GBP | 2023-03-31 | 2024-11-25 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2022-03-31 | 2023-12-12 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 47292 | GBP | 2022-03-31 | 2023-12-12 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 110057 | GBP | 2022-03-31 | 2023-12-12 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 65045 | GBP | 2022-03-31 | 2023-12-12 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 2280 | GBP | 2022-03-31 | 2023-12-12 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 65045 | GBP | 2022-03-31 | 2023-12-12 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 62765 | GBP | 2022-03-31 | 2023-12-12 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 65045 | GBP | 2022-03-31 | 2023-12-12 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## IBISHI LTD (`gb:05107075`)

- registration: `05107075` (GB), status active, incorporated 2004-04-20
- classification: ['62012', '62020', '62090'] (sic_2007)
- records: 5 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 79 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-03-31 | 2025-12-03 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 23859 | GBP | 2025-03-31 | 2025-12-03 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 9155 | GBP | 2025-03-31 | 2025-12-03 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 1789 | GBP | 2025-03-31 | 2025-12-03 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -31515 | GBP | 2025-03-31 | 2025-12-03 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 1 | GBP | 2025-03-31 | 2025-12-03 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | -31515 | GBP | 2025-03-31 | 2025-12-03 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -7093 | GBP | 2025-03-31 | 2025-12-03 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -7092 | GBP | 2025-03-31 | 2025-12-03 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-03-31 | 2025-12-03 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-03-31 | 2024-10-09 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 29244 | GBP | 2024-03-31 | 2025-12-03 | filed | yes | `core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 29244 | GBP | 2024-03-31 | 2024-10-09 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 9095 | GBP | 2024-03-31 | 2025-12-03 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 9095 | GBP | 2024-03-31 | 2024-10-09 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 3155 | GBP | 2024-03-31 | 2025-12-03 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 3155 | GBP | 2024-03-31 | 2024-10-09 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | -35651 | GBP | 2024-03-31 | 2025-12-03 | filed | yes | `core:Equity` | micro-entity |
| equity | -35651 | GBP | 2024-03-31 | 2024-10-09 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 121 | GBP | 2024-03-31 | 2024-10-09 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 121 | GBP | 2024-03-31 | 2025-12-03 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | -35651 | GBP | 2024-03-31 | 2025-12-03 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | -35651 | GBP | 2024-03-31 | 2024-10-09 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -5940 | GBP | 2024-03-31 | 2025-12-03 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -5940 | GBP | 2024-03-31 | 2024-10-09 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -5819 | GBP | 2024-03-31 | 2024-10-09 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -5819 | GBP | 2024-03-31 | 2025-12-03 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-03-31 | 2024-10-09 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-03-31 | 2023-11-29 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 34472 | GBP | 2023-03-31 | 2024-10-09 | filed | yes | `core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 34472 | GBP | 2023-03-31 | 2023-11-29 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 12167 | GBP | 2023-03-31 | 2024-10-09 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 12167 | GBP | 2023-03-31 | 2023-11-29 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 6713 | GBP | 2023-03-31 | 2023-11-29 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 6713 | GBP | 2023-03-31 | 2024-10-09 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -39824 | GBP | 2023-03-31 | 2023-11-29 | filed | no | `core:Equity` | micro-entity |
| equity | -39824 | GBP | 2023-03-31 | 2024-10-09 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 653 | GBP | 2023-03-31 | 2023-11-29 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 653 | GBP | 2023-03-31 | 2024-10-09 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | -39824 | GBP | 2023-03-31 | 2023-11-29 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | -39824 | GBP | 2023-03-31 | 2024-10-09 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -5441 | GBP | 2023-03-31 | 2023-11-29 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -5441 | GBP | 2023-03-31 | 2024-10-09 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -4788 | GBP | 2023-03-31 | 2023-11-29 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -4788 | GBP | 2023-03-31 | 2024-10-09 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2022-03-31 | 2023-11-29 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 39618 | GBP | 2022-03-31 | 2023-11-29 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 8423 | GBP | 2022-03-31 | 2023-11-29 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 9636 | GBP | 2022-03-31 | 2023-11-29 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -37921 | GBP | 2022-03-31 | 2023-11-29 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 1311 | GBP | 2022-03-31 | 2023-11-29 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | -37921 | GBP | 2022-03-31 | 2023-11-29 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 1226 | GBP | 2022-03-31 | 2023-11-29 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 2537 | GBP | 2022-03-31 | 2023-11-29 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## JASON DAVIES LIMITED (`gb:05493718`)

- registration: `05493718` (GB), status active, incorporated 2005-06-28
- classification: ['62012'] (sic_2007)
- records: 2 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 52 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.01 | xbrli:pure | 2025-06-30 | 2026-03-11 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 28999 | GBP | 2025-06-30 | 2026-03-11 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 29007 | GBP | 2025-06-30 | 2026-03-11 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 8 | GBP | 2025-06-30 | 2026-03-11 | filed | yes | `core:Equity` | micro-entity |
| net_assets | 8 | GBP | 2025-06-30 | 2026-03-11 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 8 | GBP | 2025-06-30 | 2026-03-11 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-06-30 | 2025-03-13 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0.01 | xbrli:pure | 2024-06-30 | 2026-03-11 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 11320 | GBP | 2024-06-30 | 2025-03-13 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 11320 | GBP | 2024-06-30 | 2026-03-11 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 27959 | GBP | 2024-06-30 | 2026-03-11 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 27959 | GBP | 2024-06-30 | 2025-03-13 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 16639 | GBP | 2024-06-30 | 2026-03-11 | filed | yes | `core:Equity` | micro-entity |
| equity | 16639 | GBP | 2024-06-30 | 2025-03-13 | filed | no | `core:Equity` | micro-entity |
| net_assets | 16639 | GBP | 2024-06-30 | 2026-03-11 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 16639 | GBP | 2024-06-30 | 2026-03-11 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-06-30 | 2024-03-27 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-06-30 | 2025-03-13 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 20472 | GBP | 2023-06-30 | 2024-03-27 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 20472 | GBP | 2023-06-30 | 2025-03-13 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 31485 | GBP | 2023-06-30 | 2025-03-13 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 31485 | GBP | 2023-06-30 | 2024-03-27 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 11013 | GBP | 2023-06-30 | 2024-03-27 | filed | no | `core:Equity` | micro-entity |
| equity | 11013 | GBP | 2023-06-30 | 2025-03-13 | filed | yes | `core:Equity` | micro-entity |
| average_employees | 1 | xbrli:pure | 2022-06-30 | 2024-03-27 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 17657 | GBP | 2022-06-30 | 2024-03-27 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 34491 | GBP | 2022-06-30 | 2024-03-27 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 16834 | GBP | 2022-06-30 | 2024-03-27 | filed | yes | `core:Equity` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2026-03-11: `{"superseded_document_id": "gb:05493718:doc:2HRZbvBK7An8Ajh4rEL_RdcK4OqNHG6j524dZ8gCWag", "restatements": [{"concept": "average_employees", "period_end": "2024-06-30", "old_value": "1.0000", "new_valu`

## I-GALAXY MEDIA LIMITED (`gb:05881572`)

- registration: `05881572` (GB), status active, incorporated 2006-07-19
- classification: ['59111', '59112', '59113', '62090'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 53 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | iso4217:GBP | 2025-07-31 | 2026-04-29 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2025-07-31 | 2026-04-29 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 23525 | GBP | 2025-07-31 | 2026-04-29 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 10824 | GBP | 2025-07-31 | 2026-04-29 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 2563 | GBP | 2025-07-31 | 2026-04-29 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 15264 | GBP | 2025-07-31 | 2026-04-29 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 2563 | GBP | 2025-07-31 | 2026-04-29 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 12701 | GBP | 2025-07-31 | 2026-04-29 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 2563 | GBP | 2025-07-31 | 2026-04-29 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2024-07-31 | 2025-04-30 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2024-07-31 | 2026-04-29 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 29863 | GBP | 2024-07-31 | 2025-04-30 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2024-07-31 | 2026-04-29 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 29863 | GBP | 2024-07-31 | 2026-04-29 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5519 | GBP | 2024-07-31 | 2025-04-30 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 24624 | GBP | 2024-07-31 | 2025-04-30 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 24624 | GBP | 2024-07-31 | 2026-04-29 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 10025 | GBP | 2024-07-31 | 2026-04-29 | filed | yes | `uk-core:Equity` | micro-entity |
| equity | 4506 | GBP | 2024-07-31 | 2025-04-30 | filed | no | `uk-core:Equity` | micro-entity |
| fixed_assets | 15264 | GBP | 2024-07-31 | 2026-04-29 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 15264 | GBP | 2024-07-31 | 2025-04-30 | filed | no | `uk-core:FixedAssets` | micro-entity |
| net_assets | 4506 | GBP | 2024-07-31 | 2025-04-30 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 10025 | GBP | 2024-07-31 | 2026-04-29 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 19105 | GBP | 2024-07-31 | 2025-04-30 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 5239 | GBP | 2024-07-31 | 2026-04-29 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 10025 | GBP | 2024-07-31 | 2026-04-29 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 34369 | GBP | 2024-07-31 | 2025-04-30 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2023-07-31 | 2024-04-21 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2023-07-31 | 2025-04-30 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 36342 | GBP | 2023-07-31 | 2025-04-30 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 36342 | GBP | 2023-07-31 | 2024-04-21 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5607 | GBP | 2023-07-31 | 2024-04-21 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5607 | GBP | 2023-07-31 | 2025-04-30 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 35394 | GBP | 2023-07-31 | 2025-04-30 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 35394 | GBP | 2023-07-31 | 2024-04-21 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | 8709 | GBP | 2023-07-31 | 2024-04-21 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 8709 | GBP | 2023-07-31 | 2025-04-30 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 15264 | GBP | 2023-07-31 | 2024-04-21 | filed | no | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 15264 | GBP | 2023-07-31 | 2025-04-30 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 8709 | GBP | 2023-07-31 | 2025-04-30 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 8709 | GBP | 2023-07-31 | 2024-04-21 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 29787 | GBP | 2023-07-31 | 2024-04-21 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 29787 | GBP | 2023-07-31 | 2025-04-30 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 45051 | GBP | 2023-07-31 | 2024-04-21 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 45051 | GBP | 2023-07-31 | 2025-04-30 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2022-07-31 | 2024-04-21 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 42957 | GBP | 2022-07-31 | 2024-04-21 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 20818 | GBP | 2022-07-31 | 2024-04-21 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 64760 | GBP | 2022-07-31 | 2024-04-21 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 16792 | GBP | 2022-07-31 | 2024-04-21 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 15807 | GBP | 2022-07-31 | 2024-04-21 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 16792 | GBP | 2022-07-31 | 2024-04-21 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 43942 | GBP | 2022-07-31 | 2024-04-21 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 59749 | GBP | 2022-07-31 | 2024-04-21 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2026-04-29: `{"superseded_document_id": "gb:05881572:doc:J9KFzET-6b6aLnqZuhzUBmPxOE4JmNk6b2dSSqb0eaA", "restatements": [{"concept": "creditors_within_one_year", "period_end": "2024-07-31", "old_value": "5519.0000"`
