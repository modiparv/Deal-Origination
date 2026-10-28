# Ingest spot-check

- database: `data/engine.db`
- latest run: `20261028T075931Z-d5740246`
- companies in store: 37800; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## ARC TECHNOLOGY LIMITED (`gb:02523564`)

- registration: `02523564` (GB), status active, incorporated 1990-07-18
- classification: ['62012'] (sic_2007)
- records: 9 officers, 3 beneficial owners, 0 ownership statements, 2 security interests, 119 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## EUREKA BUSINESS SOLUTIONS LIMITED (`gb:03157652`)

- registration: `03157652` (GB), status active, incorporated 1996-02-12
- classification: ['62090'] (sic_2007)
- records: 6 officers, 1 beneficial owners, 0 ownership statements, 1 security interests, 92 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 6 | xbrli:pure | 2024-01-31 | 2024-10-28 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 38258 | GBP | 2024-01-31 | 2024-10-28 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 188841 | GBP | 2024-01-31 | 2024-10-28 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 158901 | GBP | 2024-01-31 | 2024-10-28 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 120643 | GBP | 2024-01-31 | 2024-10-28 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 120643 | GBP | 2024-01-31 | 2024-10-28 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -16469 | GBP | 2024-01-31 | 2024-10-28 | filed | yes | `core:Equity` | total-exemption-full |
| equity | -16369 | GBP | 2024-01-31 | 2024-10-28 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-01-31 | 2024-10-28 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | -16369 | GBP | 2024-01-31 | 2024-10-28 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -29940 | GBP | 2024-01-31 | 2024-10-28 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -15236 | GBP | 2024-01-31 | 2024-10-28 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 6 | xbrli:pure | 2023-01-31 | 2024-10-28 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 41843 | GBP | 2023-01-31 | 2024-10-28 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 151668 | GBP | 2023-01-31 | 2024-10-28 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 137533 | GBP | 2023-01-31 | 2024-10-28 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 95690 | GBP | 2023-01-31 | 2024-10-28 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 95690 | GBP | 2023-01-31 | 2024-10-28 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3504 | GBP | 2023-01-31 | 2024-10-28 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-01-31 | 2024-10-28 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 3604 | GBP | 2023-01-31 | 2024-10-28 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 3604 | GBP | 2023-01-31 | 2024-10-28 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -14135 | GBP | 2023-01-31 | 2024-10-28 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 5101 | GBP | 2023-01-31 | 2024-10-28 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## INTERCESSIONS LIMITED (`gb:03594192`)

- registration: `03594192` (GB), status active, incorporated 1998-07-07
- classification: ['62090'] (sic_2007)
- records: 10 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 92 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-07-31 | 2026-04-28 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| debtors | 39562 | EUR | 2025-07-31 | 2026-04-28 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 39560 | EUR | 2025-07-31 | 2026-04-28 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 39562 | EUR | 2025-07-31 | 2026-04-28 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | EUR | 2025-07-31 | 2026-04-28 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 39562 | EUR | 2025-07-31 | 2026-04-28 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 39562 | EUR | 2025-07-31 | 2026-04-28 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-07-31 | 2026-04-28 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-07-31 | 2024-12-23 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| debtors | 39562 | EUR | 2024-07-31 | 2024-12-23 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 39562 | EUR | 2024-07-31 | 2026-04-28 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 39560 | EUR | 2024-07-31 | 2024-12-23 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | EUR | 2024-07-31 | 2024-12-23 | filed | no | `core:Equity` | total-exemption-full |
| equity | 39562 | EUR | 2024-07-31 | 2024-12-23 | filed | no | `core:Equity` | total-exemption-full |
| equity | 39562 | EUR | 2024-07-31 | 2026-04-28 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 39560 | EUR | 2024-07-31 | 2026-04-28 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | EUR | 2024-07-31 | 2026-04-28 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 39562 | EUR | 2024-07-31 | 2024-12-23 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 39562 | EUR | 2024-07-31 | 2026-04-28 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 39562 | EUR | 2024-07-31 | 2024-12-23 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 39562 | EUR | 2024-07-31 | 2026-04-28 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-07-31 | 2024-12-23 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-07-31 | 2024-04-22 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| debtors | 39562 | EUR | 2023-07-31 | 2024-04-22 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 39562 | EUR | 2023-07-31 | 2024-12-23 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 39562 | EUR | 2023-07-31 | 2024-04-22 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | EUR | 2023-07-31 | 2024-04-22 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 39560 | EUR | 2023-07-31 | 2024-12-23 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 39560 | EUR | 2023-07-31 | 2024-04-22 | filed | no | `core:Equity` | total-exemption-full |
| equity | 39562 | EUR | 2023-07-31 | 2024-12-23 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | EUR | 2023-07-31 | 2024-12-23 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 39562 | EUR | 2023-07-31 | 2024-12-23 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 39562 | EUR | 2023-07-31 | 2024-04-22 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 39562 | EUR | 2023-07-31 | 2024-12-23 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 39562 | EUR | 2023-07-31 | 2024-04-22 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2022-07-31 | 2024-04-22 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| debtors | 39562 | EUR | 2022-07-31 | 2024-04-22 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 39562 | EUR | 2022-07-31 | 2024-04-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 39560 | EUR | 2022-07-31 | 2024-04-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | EUR | 2022-07-31 | 2024-04-22 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 39562 | EUR | 2022-07-31 | 2024-04-22 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 39562 | EUR | 2022-07-31 | 2024-04-22 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## B&P INTERACTIVE LIMITED (`gb:04009232`)

- registration: `04009232` (GB), status active, incorporated 2000-06-06
- classification: ['62090'] (sic_2007)
- records: 3 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 70 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-06-30 | 2026-03-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 113975 | GBP | 2025-06-30 | 2026-03-30 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 16204 | GBP | 2025-06-30 | 2026-03-30 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 49191 | GBP | 2025-06-30 | 2026-03-30 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 143637 | GBP | 2025-06-30 | 2026-03-30 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 29662 | GBP | 2025-06-30 | 2026-03-30 | filed | yes | `core:Debtors` | total-exemption-full |
| net_assets | 89904 | GBP | 2025-06-30 | 2026-03-30 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 94446 | GBP | 2025-06-30 | 2026-03-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 106108 | GBP | 2025-06-30 | 2026-03-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-06-30 | 2025-03-20 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-06-30 | 2026-03-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 140500 | GBP | 2024-06-30 | 2025-03-20 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 140500 | GBP | 2024-06-30 | 2026-03-30 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 18982 | GBP | 2024-06-30 | 2026-03-30 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 18982 | GBP | 2024-06-30 | 2025-03-20 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 57654 | GBP | 2024-06-30 | 2026-03-30 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 57654 | GBP | 2024-06-30 | 2025-03-20 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 156151 | GBP | 2024-06-30 | 2025-03-20 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 156151 | GBP | 2024-06-30 | 2026-03-30 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 15651 | GBP | 2024-06-30 | 2026-03-30 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 15651 | GBP | 2024-06-30 | 2025-03-20 | filed | no | `core:Debtors` | total-exemption-full |
| net_assets | 92319 | GBP | 2024-06-30 | 2025-03-20 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 92319 | GBP | 2024-06-30 | 2026-03-30 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 98497 | GBP | 2024-06-30 | 2026-03-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 98497 | GBP | 2024-06-30 | 2025-03-20 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 111301 | GBP | 2024-06-30 | 2025-03-20 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 111301 | GBP | 2024-06-30 | 2026-03-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-06-30 | 2025-03-20 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-06-30 | 2024-03-04 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 153931 | GBP | 2023-06-30 | 2024-03-04 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 153931 | GBP | 2023-06-30 | 2025-03-20 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 21759 | GBP | 2023-06-30 | 2025-03-20 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 21759 | GBP | 2023-06-30 | 2024-03-04 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 63599 | GBP | 2023-06-30 | 2025-03-20 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 63599 | GBP | 2023-06-30 | 2024-03-04 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 166025 | GBP | 2023-06-30 | 2025-03-20 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 166025 | GBP | 2023-06-30 | 2024-03-04 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 12094 | GBP | 2023-06-30 | 2025-03-20 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 12094 | GBP | 2023-06-30 | 2024-03-04 | filed | no | `core:Debtors` | total-exemption-full |
| net_assets | 91721 | GBP | 2023-06-30 | 2025-03-20 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 91721 | GBP | 2023-06-30 | 2024-03-04 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 102426 | GBP | 2023-06-30 | 2025-03-20 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 102426 | GBP | 2023-06-30 | 2024-03-04 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 113480 | GBP | 2023-06-30 | 2025-03-20 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 113480 | GBP | 2023-06-30 | 2024-03-04 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2022-06-30 | 2024-03-04 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 138611 | GBP | 2022-06-30 | 2024-03-04 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 24537 | GBP | 2022-06-30 | 2024-03-04 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 53617 | GBP | 2022-06-30 | 2024-03-04 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 154981 | GBP | 2022-06-30 | 2024-03-04 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 16370 | GBP | 2022-06-30 | 2024-03-04 | filed | yes | `core:Debtors` | total-exemption-full |
| net_assets | 90960 | GBP | 2022-06-30 | 2024-03-04 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 101364 | GBP | 2022-06-30 | 2024-03-04 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 115497 | GBP | 2022-06-30 | 2024-03-04 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## MEDIA HAWK LIMITED (`gb:04432034`)

- registration: `04432034` (GB), status active, incorporated 2002-05-07
- classification: ['58290', '61900', '62020', '70229'] (sic_2007)
- records: 5 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 82 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.24 | xbrli:pure | 2025-03-31 | 2025-12-04 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 1358067 | GBP | 2025-03-31 | 2025-12-04 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 506749 | GBP | 2025-03-31 | 2025-12-04 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 1636993 | GBP | 2025-03-31 | 2025-12-04 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 278926 | GBP | 2025-03-31 | 2025-12-04 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 1160291 | GBP | 2025-03-31 | 2025-12-04 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1160091 | GBP | 2025-03-31 | 2025-12-04 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200 | GBP | 2025-03-31 | 2025-12-04 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 1160291 | GBP | 2025-03-31 | 2025-12-04 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1130244 | GBP | 2025-03-31 | 2025-12-04 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1168347 | GBP | 2025-03-31 | 2025-12-04 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 22 | xbrli:pure | 2024-03-31 | 2024-12-12 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 0.22 | xbrli:pure | 2024-03-31 | 2025-12-04 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 1440637 | GBP | 2024-03-31 | 2025-12-04 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 1440637 | GBP | 2024-03-31 | 2024-12-12 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 580309 | GBP | 2024-03-31 | 2025-12-04 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 580309 | GBP | 2024-03-31 | 2024-12-12 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 1704972 | GBP | 2024-03-31 | 2024-12-12 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 1704972 | GBP | 2024-03-31 | 2025-12-04 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 264335 | GBP | 2024-03-31 | 2025-12-04 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 264335 | GBP | 2024-03-31 | 2024-12-12 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1148796 | GBP | 2024-03-31 | 2025-12-04 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 1148996 | GBP | 2024-03-31 | 2024-12-12 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200 | GBP | 2024-03-31 | 2024-12-12 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1148796 | GBP | 2024-03-31 | 2024-12-12 | filed | no | `core:Equity` | total-exemption-full |
| equity | 1148996 | GBP | 2024-03-31 | 2025-12-04 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200 | GBP | 2024-03-31 | 2025-12-04 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 1148996 | GBP | 2024-03-31 | 2025-12-04 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 1148996 | GBP | 2024-03-31 | 2024-12-12 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1124663 | GBP | 2024-03-31 | 2025-12-04 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1124663 | GBP | 2024-03-31 | 2024-12-12 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1151944 | GBP | 2024-03-31 | 2024-12-12 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1151944 | GBP | 2024-03-31 | 2025-12-04 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 22 | xbrli:pure | 2023-03-31 | 2023-12-18 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 22 | xbrli:pure | 2023-03-31 | 2024-12-12 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 1367682 | GBP | 2023-03-31 | 2023-12-18 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 1367682 | GBP | 2023-03-31 | 2024-12-12 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 418237 | GBP | 2023-03-31 | 2023-12-18 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 418237 | GBP | 2023-03-31 | 2024-12-12 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 1576562 | GBP | 2023-03-31 | 2023-12-18 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 1576562 | GBP | 2023-03-31 | 2024-12-12 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 208880 | GBP | 2023-03-31 | 2024-12-12 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 208880 | GBP | 2023-03-31 | 2023-12-18 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 208880 | GBP | 2023-03-31 | 2023-12-18 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 1165598 | GBP | 2023-03-31 | 2024-12-12 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200 | GBP | 2023-03-31 | 2024-12-12 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 1165598 | GBP | 2023-03-31 | 2023-12-18 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1165398 | GBP | 2023-03-31 | 2023-12-18 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200 | GBP | 2023-03-31 | 2023-12-18 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1165398 | GBP | 2023-03-31 | 2024-12-12 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 1165598 | GBP | 2023-03-31 | 2023-12-18 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 1165598 | GBP | 2023-03-31 | 2024-12-12 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1158325 | GBP | 2023-03-31 | 2023-12-18 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1158325 | GBP | 2023-03-31 | 2024-12-12 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1167303 | GBP | 2023-03-31 | 2024-12-12 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1167303 | GBP | 2023-03-31 | 2023-12-18 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 20 | xbrli:pure | 2022-03-31 | 2023-12-18 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 1486695 | GBP | 2022-03-31 | 2023-12-18 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 372684 | GBP | 2022-03-31 | 2023-12-18 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 1709729 | GBP | 2022-03-31 | 2023-12-18 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 223034 | GBP | 2022-03-31 | 2023-12-18 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 223034 | GBP | 2022-03-31 | 2023-12-18 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 1343558 | GBP | 2022-03-31 | 2023-12-18 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200 | GBP | 2022-03-31 | 2023-12-18 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1343358 | GBP | 2022-03-31 | 2023-12-18 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 1343558 | GBP | 2022-03-31 | 2023-12-18 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1337045 | GBP | 2022-03-31 | 2023-12-18 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1345086 | GBP | 2022-03-31 | 2023-12-18 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2025-12-04: `{"superseded_document_id": "gb:04432034:doc:BLeUdvfr667odCERz76mrVhBLDD9FA8TvIjXmMrbyMs", "restatements": [{"concept": "average_employees", "period_end": "2024-03-31", "old_value": "22.0000", "new_val`

## JONATHAN ALLEN LIMITED (`gb:04860493`)

- registration: `04860493` (GB), status active, incorporated 2003-08-08
- classification: ['71129'] (sic_2007)
- records: 4 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 56 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-08-31 | 2025-10-31 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 2012 | GBP | 2025-08-31 | 2025-10-31 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity | 389 | GBP | 2025-08-31 | 2025-10-31 | filed | yes | `ns5:Equity` | micro-entity |
| fixed_assets | 885 | GBP | 2025-08-31 | 2025-10-31 | filed | yes | `ns5:FixedAssets` | micro-entity |
| net_current_assets | -496 | GBP | 2025-08-31 | 2025-10-31 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 389 | GBP | 2025-08-31 | 2025-10-31 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-08-31 | 2024-12-13 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-08-31 | 2025-10-31 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 10011 | GBP | 2024-08-31 | 2025-10-31 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| current_assets | 10011 | GBP | 2024-08-31 | 2024-12-13 | filed | no | `ns5:CurrentAssets` | micro-entity |
| equity | 8251 | GBP | 2024-08-31 | 2024-12-13 | filed | no | `ns5:Equity` | micro-entity |
| equity | 8251 | GBP | 2024-08-31 | 2025-10-31 | filed | yes | `ns5:Equity` | micro-entity |
| fixed_assets | 2661 | GBP | 2024-08-31 | 2024-12-13 | filed | no | `ns5:FixedAssets` | micro-entity |
| fixed_assets | 2661 | GBP | 2024-08-31 | 2025-10-31 | filed | yes | `ns5:FixedAssets` | micro-entity |
| net_current_assets | 5590 | GBP | 2024-08-31 | 2025-10-31 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 5590 | GBP | 2024-08-31 | 2024-12-13 | filed | no | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 8251 | GBP | 2024-08-31 | 2024-12-13 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 8251 | GBP | 2024-08-31 | 2025-10-31 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 1 | xbrli:pure | 2023-08-31 | 2023-11-20 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-08-31 | 2024-12-13 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 14730 | GBP | 2023-08-31 | 2024-12-13 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 14730 | GBP | 2023-08-31 | 2023-11-20 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity | 12731 | GBP | 2023-08-31 | 2024-12-13 | filed | yes | `ns5:Equity` | micro-entity |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 12731 | GBP | 2023-08-31 | 2023-11-20 | filed | yes | `ns5:Equity` | micro-entity |
| fixed_assets | 4437 | GBP | 2023-08-31 | 2024-12-13 | filed | yes | `ns5:FixedAssets` | micro-entity |
| fixed_assets `{'OriginalRevisedDataDimension': 'Original'}` | 4437 | GBP | 2023-08-31 | 2023-11-20 | filed | yes | `ns5:FixedAssets` | micro-entity |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 8294 | GBP | 2023-08-31 | 2023-11-20 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 8294 | GBP | 2023-08-31 | 2024-12-13 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 12731 | GBP | 2023-08-31 | 2023-11-20 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 12731 | GBP | 2023-08-31 | 2024-12-13 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 1 | xbrli:pure | 2022-08-31 | 2023-11-20 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 10370 | GBP | 2022-08-31 | 2023-11-20 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 5480 | GBP | 2022-08-31 | 2023-11-20 | filed | yes | `ns5:Equity` | micro-entity |
| fixed_assets `{'OriginalRevisedDataDimension': 'Original'}` | 0 | GBP | 2022-08-31 | 2023-11-20 | filed | yes | `ns5:FixedAssets` | micro-entity |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 5480 | GBP | 2022-08-31 | 2023-11-20 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 5480 | GBP | 2022-08-31 | 2023-11-20 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## BRIAN HOOLAHAN LIMITED (`gb:05289471`)

- registration: `05289471` (GB), status active, incorporated 2004-11-17
- classification: ['71111'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 55 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | iso4217:GBP | 2025-11-30 | 2026-08-27 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 3803 | GBP | 2025-11-30 | 2026-08-27 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 12519 | GBP | 2025-11-30 | 2026-08-27 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 8716 | GBP | 2025-11-30 | 2026-08-27 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 8716 | GBP | 2025-11-30 | 2026-08-27 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 8716 | GBP | 2025-11-30 | 2026-08-27 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 8716 | GBP | 2025-11-30 | 2026-08-27 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2024-11-30 | 2026-08-27 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2024-11-30 | 2025-08-29 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2098 | GBP | 2024-11-30 | 2025-08-29 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2098 | GBP | 2024-11-30 | 2026-08-27 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 5121 | GBP | 2024-11-30 | 2025-08-29 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 5121 | GBP | 2024-11-30 | 2026-08-27 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 3023 | GBP | 2024-11-30 | 2026-08-27 | filed | yes | `uk-core:Equity` | micro-entity |
| equity | 3023 | GBP | 2024-11-30 | 2025-08-29 | filed | no | `uk-core:Equity` | micro-entity |
| net_assets | 3023 | GBP | 2024-11-30 | 2026-08-27 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 3023 | GBP | 2024-11-30 | 2025-08-29 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 3023 | GBP | 2024-11-30 | 2026-08-27 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 3023 | GBP | 2024-11-30 | 2025-08-29 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 3023 | GBP | 2024-11-30 | 2026-08-27 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 3023 | GBP | 2024-11-30 | 2025-08-29 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2023-11-30 | 2025-08-29 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2023-11-30 | 2024-08-30 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5593 | GBP | 2023-11-30 | 2025-08-29 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5593 | GBP | 2023-11-30 | 2024-08-30 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 6618 | GBP | 2023-11-30 | 2024-08-30 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 6618 | GBP | 2023-11-30 | 2025-08-29 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 1025 | GBP | 2023-11-30 | 2024-08-30 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 1025 | GBP | 2023-11-30 | 2025-08-29 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 1025 | GBP | 2023-11-30 | 2024-08-30 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 1025 | GBP | 2023-11-30 | 2025-08-29 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 1025 | GBP | 2023-11-30 | 2025-08-29 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 1025 | GBP | 2023-11-30 | 2024-08-30 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 1025 | GBP | 2023-11-30 | 2024-08-30 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 1025 | GBP | 2023-11-30 | 2025-08-29 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2022-11-30 | 2024-08-30 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 3155 | GBP | 2022-11-30 | 2024-08-30 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 3535 | GBP | 2022-11-30 | 2024-08-30 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 380 | GBP | 2022-11-30 | 2024-08-30 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 380 | GBP | 2022-11-30 | 2024-08-30 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 380 | GBP | 2022-11-30 | 2024-08-30 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 380 | GBP | 2022-11-30 | 2024-08-30 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## DMT SOFTWARE LIMITED (`gb:05709343`)

- registration: `05709343` (GB), status active, incorporated 2006-02-14
- classification: ['62090'] (sic_2007)
- records: 5 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 60 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2026-03-31 | 2026-06-01 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 35062 | GBP | 2026-03-31 | 2026-06-01 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity | 1411 | GBP | 2026-03-31 | 2026-06-01 | filed | yes | `ns5:Equity` | micro-entity |
| fixed_assets | 21502 | GBP | 2026-03-31 | 2026-06-01 | filed | yes | `ns5:FixedAssets` | micro-entity |
| net_assets | 1411 | GBP | 2026-03-31 | 2026-06-01 | filed | yes | `ns5:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -721 | GBP | 2026-03-31 | 2026-06-01 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 20781 | GBP | 2026-03-31 | 2026-06-01 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2025-03-31 | 2026-06-01 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2025-03-31 | 2025-06-03 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 31208 | GBP | 2025-03-31 | 2025-06-03 | filed | no | `ns5:CurrentAssets` | micro-entity |
| current_assets | 31258 | GBP | 2025-03-31 | 2026-06-01 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity | 889 | GBP | 2025-03-31 | 2025-06-03 | filed | no | `ns5:Equity` | micro-entity |
| equity | 889 | GBP | 2025-03-31 | 2026-06-01 | filed | yes | `ns5:Equity` | micro-entity |
| fixed_assets | 27445 | GBP | 2025-03-31 | 2026-06-01 | filed | yes | `ns5:FixedAssets` | micro-entity |
| fixed_assets | 27445 | GBP | 2025-03-31 | 2025-06-03 | filed | no | `ns5:FixedAssets` | micro-entity |
| net_assets | 889 | GBP | 2025-03-31 | 2025-06-03 | filed | no | `ns5:NetAssetsLiabilities` | micro-entity |
| net_assets | 889 | GBP | 2025-03-31 | 2026-06-01 | filed | yes | `ns5:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -423 | GBP | 2025-03-31 | 2025-06-03 | filed | no | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -423 | GBP | 2025-03-31 | 2026-06-01 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 27022 | GBP | 2025-03-31 | 2026-06-01 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 27022 | GBP | 2025-03-31 | 2025-06-03 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-03-31 | 2024-06-27 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-03-31 | 2025-06-03 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 35495 | GBP | 2024-03-31 | 2025-06-03 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| current_assets | 35495 | GBP | 2024-03-31 | 2024-06-27 | filed | no | `ns5:CurrentAssets` | micro-entity |
| equity | 1007 | GBP | 2024-03-31 | 2025-06-03 | filed | yes | `ns5:Equity` | micro-entity |
| equity | 1007 | GBP | 2024-03-31 | 2024-06-27 | filed | no | `ns5:Equity` | micro-entity |
| fixed_assets | 34176 | GBP | 2024-03-31 | 2024-06-27 | filed | no | `ns5:FixedAssets` | micro-entity |
| fixed_assets | 34176 | GBP | 2024-03-31 | 2025-06-03 | filed | yes | `ns5:FixedAssets` | micro-entity |
| net_assets | 1007 | GBP | 2024-03-31 | 2025-06-03 | filed | yes | `ns5:NetAssetsLiabilities` | micro-entity |
| net_assets | 1007 | GBP | 2024-03-31 | 2024-06-27 | filed | no | `ns5:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 3224 | GBP | 2024-03-31 | 2024-06-27 | filed | no | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 3224 | GBP | 2024-03-31 | 2025-06-03 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 37400 | GBP | 2024-03-31 | 2025-06-03 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 37400 | GBP | 2024-03-31 | 2024-06-27 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-03-31 | 2024-06-27 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 29589 | GBP | 2023-03-31 | 2024-06-27 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity | 164 | GBP | 2023-03-31 | 2024-06-27 | filed | yes | `ns5:Equity` | micro-entity |
| fixed_assets | 41025 | GBP | 2023-03-31 | 2024-06-27 | filed | yes | `ns5:FixedAssets` | micro-entity |
| net_assets | 164 | GBP | 2023-03-31 | 2024-06-27 | filed | yes | `ns5:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 5724 | GBP | 2023-03-31 | 2024-06-27 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 46749 | GBP | 2023-03-31 | 2024-06-27 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2026-06-01: `{"superseded_document_id": "gb:05709343:doc:w9ioZKgD0EENtBcFIb5K6hz__kDUq54_CUA-dqlX88o", "restatements": [{"concept": "current_assets", "period_end": "2025-03-31", "old_value": "31208.0000", "new_val`

## KULSANJ CONSULTING LIMITED (`gb:06265809`)

- registration: `06265809` (GB), status active, incorporated 2007-06-01
- classification: ['62020', '96090'] (sic_2007)
- records: 2 officers, 3 beneficial owners, 0 ownership statements, 0 security interests, 57 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2022-06-30 | 2023-09-19 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 65 | GBP | 2022-06-30 | 2023-09-19 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 86447 | GBP | 2022-06-30 | 2023-09-19 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 85506 | GBP | 2022-06-30 | 2023-09-19 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 84962 | GBP | 2022-06-30 | 2023-09-19 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 84897 | GBP | 2022-06-30 | 2023-09-19 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 303009 | GBP | 2022-06-30 | 2023-09-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2022-06-30 | 2023-09-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 303109 | GBP | 2022-06-30 | 2023-09-19 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 390100 | GBP | 2022-06-30 | 2023-09-19 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | 303109 | GBP | 2022-06-30 | 2023-09-19 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -544 | GBP | 2022-06-30 | 2023-09-19 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 389556 | GBP | 2022-06-30 | 2023-09-19 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2021-06-30 | 2023-09-19 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2021-06-30 | 2022-03-30 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 558 | GBP | 2021-06-30 | 2023-09-19 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 558 | GBP | 2021-06-30 | 2022-03-30 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 99000 | GBP | 2021-06-30 | 2022-03-30 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 99000 | GBP | 2021-06-30 | 2023-09-19 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 85889 | GBP | 2021-06-30 | 2022-03-30 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 85889 | GBP | 2021-06-30 | 2023-09-19 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 98558 | GBP | 2021-06-30 | 2022-03-30 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 98558 | GBP | 2021-06-30 | 2023-09-19 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 98000 | GBP | 2021-06-30 | 2023-09-19 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 98000 | GBP | 2021-06-30 | 2022-03-30 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 303669 | GBP | 2021-06-30 | 2023-09-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2021-06-30 | 2022-03-30 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2021-06-30 | 2023-09-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 303769 | GBP | 2021-06-30 | 2022-03-30 | filed | no | `core:Equity` | total-exemption-full |
| equity | 303769 | GBP | 2021-06-30 | 2023-09-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 303669 | GBP | 2021-06-30 | 2022-03-30 | filed | no | `core:Equity` | total-exemption-full |
| fixed_assets | 390100 | GBP | 2021-06-30 | 2023-09-19 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | 303769 | GBP | 2021-06-30 | 2022-03-30 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 303769 | GBP | 2021-06-30 | 2023-09-19 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 12669 | GBP | 2021-06-30 | 2022-03-30 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 12669 | GBP | 2021-06-30 | 2023-09-19 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 402769 | GBP | 2021-06-30 | 2023-09-19 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 402769 | GBP | 2021-06-30 | 2022-03-30 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2020-06-30 | 2021-06-29 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 263 | GBP | 2020-06-30 | 2021-06-29 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 86523 | GBP | 2020-06-30 | 2021-06-29 | filed | yes | `core:Creditors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2020-06-30 | 2021-06-29 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 306800 | GBP | 2020-06-30 | 2021-06-29 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 306700 | GBP | 2020-06-30 | 2021-06-29 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 393060 | GBP | 2020-06-30 | 2021-06-29 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | 306800 | GBP | 2020-06-30 | 2021-06-29 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -86260 | GBP | 2020-06-30 | 2021-06-29 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |

Coverage @ 2022-06-30: 11/21 concepts available (average_employees, cash, creditors_after_one_year, creditors_within_one_year, current_assets, debtors, equity, fixed_assets, net_assets, net_current_assets, total_assets_less_current_liabilities)
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

- event restatement @ 2023-09-19: `{"superseded_document_id": "gb:06265809:doc:iXk99sdQMunD8CaYr6pHL-IQsCI0tKeF0rRVLs3eyA4", "restatements": [{"concept": "average_employees", "period_end": "2021-06-30", "old_value": "2.0000", "new_valu`
