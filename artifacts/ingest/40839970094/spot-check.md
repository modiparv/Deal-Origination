# Ingest spot-check

- database: `data/engine.db`
- latest run: `20261029T080845Z-50b0efa7`
- companies in store: 38600; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## KEY COMPUTER APPLICATIONS LIMITED (`gb:02542478`)

- registration: `02542478` (GB), status active, incorporated 1990-09-24
- classification: ['62012', '62020', '62090'] (sic_2007)
- records: 6 officers, 1 beneficial owners, 1 ownership statements, 4 security interests, 106 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.59 | xbrli:pure | 2024-12-31 | 2025-09-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | small |
| cash | 379383 | GBP | 2024-12-31 | 2025-09-30 | filed | yes | `core:CashBankOnHand` | small |
| current_assets | 2796394 | GBP | 2024-12-31 | 2025-09-30 | filed | yes | `core:CurrentAssets` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2417011 | GBP | 2024-12-31 | 2025-09-30 | filed | yes | `core:Debtors` | small |
| debtors | 2417011 | GBP | 2024-12-31 | 2025-09-30 | filed | yes | `core:Debtors` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 60 | GBP | 2024-12-31 | 2025-09-30 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 678434 | GBP | 2024-12-31 | 2025-09-30 | filed | yes | `core:Equity` | small |
| equity | 678494 | GBP | 2024-12-31 | 2025-09-30 | filed | yes | `core:Equity` | small |
| fixed_assets | 358491 | GBP | 2024-12-31 | 2025-09-30 | filed | yes | `core:FixedAssets` | small |
| net_assets | 678494 | GBP | 2024-12-31 | 2025-09-30 | filed | yes | `core:NetAssetsLiabilities` | small |
| net_current_assets | 528355 | GBP | 2024-12-31 | 2025-09-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | small |
| total_assets_less_current_liabilities | 886846 | GBP | 2024-12-31 | 2025-09-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | small |
| average_employees | 61 | xbrli:pure | 2023-12-31 | 2024-12-24 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | small |
| average_employees | 0.61 | xbrli:pure | 2023-12-31 | 2025-09-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | small |
| cash | 226229 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:CashBankOnHand` | small |
| cash | 226229 | GBP | 2023-12-31 | 2024-12-24 | filed | no | `core:CashBankOnHand` | small |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 250023 | GBP | 2023-12-31 | 2024-12-24 | filed | yes | `core:Creditors` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2158494 | GBP | 2023-12-31 | 2024-12-24 | filed | yes | `core:Creditors` | small |
| current_assets | 2463849 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:CurrentAssets` | small |
| current_assets | 2463849 | GBP | 2023-12-31 | 2024-12-24 | filed | no | `core:CurrentAssets` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2237620 | GBP | 2023-12-31 | 2024-12-24 | filed | no | `core:Debtors` | small |
| debtors | 2237620 | GBP | 2023-12-31 | 2024-12-24 | filed | no | `core:Debtors` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2237620 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:Debtors` | small |
| debtors | 2237620 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:Debtors` | small |
| equity | 384667 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 384607 | GBP | 2023-12-31 | 2024-12-24 | filed | no | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 384607 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:Equity` | small |
| equity | 384667 | GBP | 2023-12-31 | 2024-12-24 | filed | no | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 60 | GBP | 2023-12-31 | 2024-12-24 | filed | no | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 60 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:Equity` | small |
| fixed_assets | 345359 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:FixedAssets` | small |
| net_assets | 384667 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:NetAssetsLiabilities` | small |
| net_assets | 384667 | GBP | 2023-12-31 | 2024-12-24 | filed | no | `core:NetAssetsLiabilities` | small |
| net_current_assets | 305355 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | small |
| net_current_assets | 305355 | GBP | 2023-12-31 | 2024-12-24 | filed | no | `core:NetCurrentAssetsLiabilities` | small |
| total_assets_less_current_liabilities | 650714 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | small |
| total_assets_less_current_liabilities | 650714 | GBP | 2023-12-31 | 2024-12-24 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | small |
| average_employees | 54 | xbrli:pure | 2022-12-31 | 2023-09-25 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 54 | xbrli:pure | 2022-12-31 | 2024-12-24 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | small |
| cash | 777678 | GBP | 2022-12-31 | 2024-12-24 | filed | yes | `core:CashBankOnHand` | small |
| cash | 777678 | GBP | 2022-12-31 | 2023-09-25 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 237721 | GBP | 2022-12-31 | 2023-09-25 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 237721 | GBP | 2022-12-31 | 2024-12-24 | filed | yes | `core:Creditors` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1766169 | GBP | 2022-12-31 | 2024-12-24 | filed | yes | `core:Creditors` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1766169 | GBP | 2022-12-31 | 2023-09-25 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 2290653 | GBP | 2022-12-31 | 2024-12-24 | filed | yes | `core:CurrentAssets` | small |
| current_assets | 2290653 | GBP | 2022-12-31 | 2023-09-25 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors | 1512975 | GBP | 2022-12-31 | 2023-09-25 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1512975 | GBP | 2022-12-31 | 2024-12-24 | filed | yes | `core:Debtors` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1512975 | GBP | 2022-12-31 | 2023-09-25 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 1512975 | GBP | 2022-12-31 | 2024-12-24 | filed | yes | `core:Debtors` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 468488 | GBP | 2022-12-31 | 2024-12-24 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 468488 | GBP | 2022-12-31 | 2023-09-25 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 60 | GBP | 2022-12-31 | 2023-09-25 | filed | no | `core:Equity` | total-exemption-full |
| equity | 468548 | GBP | 2022-12-31 | 2024-12-24 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 60 | GBP | 2022-12-31 | 2024-12-24 | filed | yes | `core:Equity` | small |
| equity | 468548 | GBP | 2022-12-31 | 2023-09-25 | filed | no | `core:Equity` | total-exemption-full |
| net_assets | 468548 | GBP | 2022-12-31 | 2024-12-24 | filed | yes | `core:NetAssetsLiabilities` | small |
| net_assets | 468548 | GBP | 2022-12-31 | 2023-09-25 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 524484 | GBP | 2022-12-31 | 2023-09-25 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 524484 | GBP | 2022-12-31 | 2024-12-24 | filed | yes | `core:NetCurrentAssetsLiabilities` | small |
| total_assets_less_current_liabilities | 730015 | GBP | 2022-12-31 | 2023-09-25 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 730015 | GBP | 2022-12-31 | 2024-12-24 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | small |
| average_employees | 46 | xbrli:pure | 2021-12-31 | 2023-09-25 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 860415 | GBP | 2021-12-31 | 2023-09-25 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 213750 | GBP | 2021-12-31 | 2023-09-25 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1602643 | GBP | 2021-12-31 | 2023-09-25 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 2196819 | GBP | 2021-12-31 | 2023-09-25 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 1336314 | GBP | 2021-12-31 | 2023-09-25 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1336314 | GBP | 2021-12-31 | 2023-09-25 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 435910 | GBP | 2021-12-31 | 2023-09-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 60 | GBP | 2021-12-31 | 2023-09-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 435850 | GBP | 2021-12-31 | 2023-09-25 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 435910 | GBP | 2021-12-31 | 2023-09-25 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 594176 | GBP | 2021-12-31 | 2023-09-25 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 653616 | GBP | 2021-12-31 | 2023-09-25 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2025-09-30: `{"superseded_document_id": "gb:02542478:doc:xPGfSdBsJgWe-6fCPVuumnZxDR1Z3FpYWe1162JjE28", "restatements": [{"concept": "average_employees", "period_end": "2023-12-31", "old_value": "61.0000", "new_val`

## J2 CONSULTING LIMITED (`gb:03178330`)

- registration: `03178330` (GB), status active, incorporated 1996-03-26
- classification: ['62020'] (sic_2007)
- records: 5 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 83 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | xbrli:pure | 2025-03-31 | 2025-10-29 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 20373 | GBP | 2025-03-31 | 2025-10-29 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity | 7908 | GBP | 2025-03-31 | 2025-10-29 | filed | yes | `ns5:Equity` | micro-entity |
| fixed_assets | 7247 | GBP | 2025-03-31 | 2025-10-29 | filed | yes | `ns5:FixedAssets` | micro-entity |
| net_current_assets | 661 | GBP | 2025-03-31 | 2025-10-29 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 7908 | GBP | 2025-03-31 | 2025-10-29 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2024-03-31 | 2025-10-29 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | xbrli:pure | 2024-03-31 | 2024-07-31 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 61577 | GBP | 2024-03-31 | 2024-07-31 | filed | no | `ns5:CurrentAssets` | micro-entity |
| current_assets | 61577 | GBP | 2024-03-31 | 2025-10-29 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity | 42280 | GBP | 2024-03-31 | 2024-07-31 | filed | no | `ns5:Equity` | micro-entity |
| equity | 42280 | GBP | 2024-03-31 | 2025-10-29 | filed | yes | `ns5:Equity` | micro-entity |
| fixed_assets | 5888 | GBP | 2024-03-31 | 2025-10-29 | filed | yes | `ns5:FixedAssets` | micro-entity |
| fixed_assets | 5888 | GBP | 2024-03-31 | 2024-07-31 | filed | no | `ns5:FixedAssets` | micro-entity |
| net_current_assets | 36392 | GBP | 2024-03-31 | 2024-07-31 | filed | no | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 36392 | GBP | 2024-03-31 | 2025-10-29 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 42280 | GBP | 2024-03-31 | 2024-07-31 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 42280 | GBP | 2024-03-31 | 2025-10-29 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 0 | xbrli:pure | 2023-03-31 | 2023-12-12 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | xbrli:pure | 2023-03-31 | 2024-07-31 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 66602 | GBP | 2023-03-31 | 2024-07-31 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 66602 | GBP | 2023-03-31 | 2023-12-12 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 43593 | GBP | 2023-03-31 | 2023-12-12 | filed | yes | `ns5:Equity` | micro-entity |
| equity | 43593 | GBP | 2023-03-31 | 2024-07-31 | filed | yes | `ns5:Equity` | micro-entity |
| fixed_assets `{'OriginalRevisedDataDimension': 'Original'}` | 5914 | GBP | 2023-03-31 | 2023-12-12 | filed | yes | `ns5:FixedAssets` | micro-entity |
| fixed_assets | 5914 | GBP | 2023-03-31 | 2024-07-31 | filed | yes | `ns5:FixedAssets` | micro-entity |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 37679 | GBP | 2023-03-31 | 2023-12-12 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 37679 | GBP | 2023-03-31 | 2024-07-31 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 43593 | GBP | 2023-03-31 | 2023-12-12 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 43593 | GBP | 2023-03-31 | 2024-07-31 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 0 | xbrli:pure | 2022-03-31 | 2023-12-12 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 68542 | GBP | 2022-03-31 | 2023-12-12 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 50746 | GBP | 2022-03-31 | 2023-12-12 | filed | yes | `ns5:Equity` | micro-entity |
| fixed_assets `{'OriginalRevisedDataDimension': 'Original'}` | 6451 | GBP | 2022-03-31 | 2023-12-12 | filed | yes | `ns5:FixedAssets` | micro-entity |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 44295 | GBP | 2022-03-31 | 2023-12-12 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 50746 | GBP | 2022-03-31 | 2023-12-12 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## SELECTLINE TECHNOLOGY LIMITED (`gb:03619156`)

- registration: `03619156` (GB), status active, incorporated 1998-08-20
- classification: ['62020'] (sic_2007)
- records: 5 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 78 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2021-12-31 | 2022-07-13 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 1106 | GBP | 2021-12-31 | 2022-07-13 | filed | yes | `frs-core:CashBankOnHand` | unaudited-abridged |
| current_assets | 1203 | GBP | 2021-12-31 | 2022-07-13 | filed | yes | `frs-core:CurrentAssets` | unaudited-abridged |
| debtors | 97 | GBP | 2021-12-31 | 2022-07-13 | filed | yes | `frs-core:Debtors` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 4 | GBP | 2021-12-31 | 2022-07-13 | filed | yes | `frs-core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -14021 | GBP | 2021-12-31 | 2022-07-13 | filed | yes | `frs-core:Equity` | unaudited-abridged |
| net_assets | -14017 | GBP | 2021-12-31 | 2022-07-13 | filed | yes | `frs-core:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | -1667 | GBP | 2021-12-31 | 2022-07-13 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | -1667 | GBP | 2021-12-31 | 2022-07-13 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 1 | xbrli:pure | 2020-12-31 | 2021-03-16 | filed | no | `ns6:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 0 | xbrli:pure | 2020-12-31 | 2022-07-13 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 6037 | GBP | 2020-12-31 | 2021-03-16 | filed | no | `ns6:CashBankOnHand` | total-exemption-full |
| cash | 0 | GBP | 2020-12-31 | 2022-07-13 | filed | yes | `frs-core:CashBankOnHand` | unaudited-abridged |
| current_assets | 6243 | GBP | 2020-12-31 | 2021-03-16 | filed | no | `ns6:CurrentAssets` | total-exemption-full |
| current_assets | 206 | GBP | 2020-12-31 | 2022-07-13 | filed | yes | `frs-core:CurrentAssets` | unaudited-abridged |
| debtors | 206 | GBP | 2020-12-31 | 2021-03-16 | filed | no | `ns6:Debtors` | total-exemption-full |
| debtors | 206 | GBP | 2020-12-31 | 2022-07-13 | filed | yes | `frs-core:Debtors` | unaudited-abridged |
| equity | -7681 | GBP | 2020-12-31 | 2021-03-16 | filed | yes | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 4 | GBP | 2020-12-31 | 2022-07-13 | filed | yes | `frs-core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -7685 | GBP | 2020-12-31 | 2021-03-16 | filed | no | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 4 | GBP | 2020-12-31 | 2021-03-16 | filed | no | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -7685 | GBP | 2020-12-31 | 2022-07-13 | filed | yes | `frs-core:Equity` | unaudited-abridged |
| net_assets | -7681 | GBP | 2020-12-31 | 2021-03-16 | filed | no | `ns6:NetAssetsLiabilities` | total-exemption-full |
| net_assets | -7681 | GBP | 2020-12-31 | 2022-07-13 | filed | yes | `frs-core:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | -7681 | GBP | 2020-12-31 | 2022-07-13 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 5319 | GBP | 2020-12-31 | 2021-03-16 | filed | no | `ns6:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -8512 | GBP | 2020-12-31 | 2021-03-16 | filed | yes | `ns6:ProfitLoss` | total-exemption-full |
| total_assets_less_current_liabilities | 5319 | GBP | 2020-12-31 | 2021-03-16 | filed | no | `ns6:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -7681 | GBP | 2020-12-31 | 2022-07-13 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 1 | xbrli:pure | 2019-12-31 | 2020-04-03 | filed | no | `ns6:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2019-12-31 | 2021-03-16 | filed | yes | `ns6:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 17254 | GBP | 2019-12-31 | 2020-04-03 | filed | no | `ns6:CashBankOnHand` | total-exemption-full |
| cash | 17254 | GBP | 2019-12-31 | 2021-03-16 | filed | yes | `ns6:CashBankOnHand` | total-exemption-full |
| current_assets | 17254 | GBP | 2019-12-31 | 2021-03-16 | filed | yes | `ns6:CurrentAssets` | total-exemption-full |
| current_assets | 17254 | GBP | 2019-12-31 | 2020-04-03 | filed | no | `ns6:CurrentAssets` | total-exemption-full |
| debtors | 0 | GBP | 2019-12-31 | 2020-04-03 | filed | no | `ns6:Debtors` | total-exemption-full |
| debtors | 0 | GBP | 2019-12-31 | 2021-03-16 | filed | yes | `ns6:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 5980 | GBP | 2019-12-31 | 2020-04-03 | filed | no | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 4 | GBP | 2019-12-31 | 2021-03-16 | filed | yes | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 4 | GBP | 2019-12-31 | 2020-04-03 | filed | no | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 5980 | GBP | 2019-12-31 | 2021-03-16 | filed | yes | `ns6:Equity` | total-exemption-full |
| equity | 5984 | GBP | 2019-12-31 | 2020-04-03 | filed | no | `ns6:Equity` | total-exemption-full |
| equity | 5984 | GBP | 2019-12-31 | 2021-03-16 | filed | yes | `ns6:Equity` | total-exemption-full |
| net_assets | 5984 | GBP | 2019-12-31 | 2021-03-16 | filed | yes | `ns6:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 5984 | GBP | 2019-12-31 | 2021-03-16 | filed | yes | `ns6:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 5984 | GBP | 2019-12-31 | 2020-04-03 | filed | no | `ns6:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 31717 | GBP | 2019-12-31 | 2020-04-03 | filed | yes | `ns6:ProfitLoss` | total-exemption-full |
| total_assets_less_current_liabilities | 5984 | GBP | 2019-12-31 | 2020-04-03 | filed | no | `ns6:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 5984 | GBP | 2019-12-31 | 2021-03-16 | filed | yes | `ns6:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2018-12-31 | 2020-04-03 | filed | yes | `ns6:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 49041 | GBP | 2018-12-31 | 2020-04-03 | filed | yes | `ns6:CashBankOnHand` | total-exemption-full |
| current_assets | 49641 | GBP | 2018-12-31 | 2020-04-03 | filed | yes | `ns6:CurrentAssets` | total-exemption-full |
| debtors | 600 | GBP | 2018-12-31 | 2020-04-03 | filed | yes | `ns6:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 31656 | GBP | 2018-12-31 | 2020-04-03 | filed | yes | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 4 | GBP | 2018-12-31 | 2020-04-03 | filed | yes | `ns6:Equity` | total-exemption-full |
| equity | 31660 | GBP | 2018-12-31 | 2020-04-03 | filed | yes | `ns6:Equity` | total-exemption-full |
| net_current_assets | 31660 | GBP | 2018-12-31 | 2020-04-03 | filed | yes | `ns6:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 31660 | GBP | 2018-12-31 | 2020-04-03 | filed | yes | `ns6:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2022-07-13: `{"superseded_document_id": "gb:03619156:doc:Q9R57x1loRom1Ibyte4hLcHHAIDy-gfpXHH56-a599o", "restatements": [{"concept": "cash", "period_end": "2020-12-31", "old_value": "6037.0000", "new_value": "0.000`

## ESL CLOUD SOLUTIONS LIMITED (`gb:04045202`)

- registration: `04045202` (GB), status active, incorporated 2000-08-02
- classification: ['62090'] (sic_2007)
- records: 5 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 82 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2024-12-31 | 2025-09-25 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| debtors | 24809 | GBP | 2024-12-31 | 2025-09-25 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 24809 | GBP | 2024-12-31 | 2025-09-25 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-12-31 | 2025-09-25 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | -201797 | GBP | 2024-12-31 | 2025-09-25 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -201897 | GBP | 2024-12-31 | 2025-09-25 | filed | yes | `ns5:Equity` | total-exemption-full |
| fixed_assets | 2 | GBP | 2024-12-31 | 2025-09-25 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| net_current_assets | -201799 | GBP | 2024-12-31 | 2025-09-25 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -201797 | GBP | 2024-12-31 | 2025-09-25 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-12-31 | 2025-09-25 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-12-31 | 2024-09-23 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| debtors | 18662 | GBP | 2023-12-31 | 2024-09-23 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 18662 | GBP | 2023-12-31 | 2025-09-25 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 18662 | GBP | 2023-12-31 | 2024-09-23 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 18662 | GBP | 2023-12-31 | 2025-09-25 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-12-31 | 2024-09-23 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | -210354 | GBP | 2023-12-31 | 2025-09-25 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-12-31 | 2025-09-25 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -210454 | GBP | 2023-12-31 | 2024-09-23 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -210454 | GBP | 2023-12-31 | 2025-09-25 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | -210354 | GBP | 2023-12-31 | 2024-09-23 | filed | no | `ns5:Equity` | total-exemption-full |
| fixed_assets | 2 | GBP | 2023-12-31 | 2025-09-25 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| fixed_assets | 2 | GBP | 2023-12-31 | 2024-09-23 | filed | no | `ns5:FixedAssets` | total-exemption-full |
| net_current_assets | -210356 | GBP | 2023-12-31 | 2024-09-23 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -210356 | GBP | 2023-12-31 | 2025-09-25 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -210354 | GBP | 2023-12-31 | 2024-09-23 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -210354 | GBP | 2023-12-31 | 2025-09-25 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2022-12-31 | 2024-09-23 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2022-12-31 | 2023-06-26 | filed | no | `ns6:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 12680 | GBP | 2022-12-31 | 2024-09-23 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 12680 | GBP | 2022-12-31 | 2024-09-23 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 12680 | GBP | 2022-12-31 | 2023-06-26 | filed | no | `ns6:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 12680 | GBP | 2022-12-31 | 2023-06-26 | filed | no | `ns6:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2022-12-31 | 2024-09-23 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2022-12-31 | 2023-06-26 | filed | no | `ns6:Equity` | total-exemption-full |
| equity | -216838 | GBP | 2022-12-31 | 2023-06-26 | filed | no | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -216938 | GBP | 2022-12-31 | 2024-09-23 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -216938 | GBP | 2022-12-31 | 2023-06-26 | filed | no | `ns6:Equity` | total-exemption-full |
| equity | -216838 | GBP | 2022-12-31 | 2024-09-23 | filed | yes | `ns5:Equity` | total-exemption-full |
| fixed_assets | 267 | GBP | 2022-12-31 | 2024-09-23 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| fixed_assets | 267 | GBP | 2022-12-31 | 2023-06-26 | filed | no | `ns6:FixedAssets` | total-exemption-full |
| net_current_assets | -217105 | GBP | 2022-12-31 | 2024-09-23 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -217105 | GBP | 2022-12-31 | 2023-06-26 | filed | no | `ns6:NetCurrentAssetsLiabilities` | total-exemption-full |
| operating_profit | 5366 | GBP | 2022-12-31 | 2023-06-26 | filed | yes | `ns6:OperatingProfitLoss` | total-exemption-full |
| profit_before_tax | 2789 | GBP | 2022-12-31 | 2023-06-26 | filed | yes | `ns6:ProfitLossOnOrdinaryActivitiesBeforeTax` | total-exemption-full |
| profit_for_period | 2789 | GBP | 2022-12-31 | 2023-06-26 | filed | yes | `ns6:ProfitLoss` | total-exemption-full |
| revenue | 3000 | GBP | 2022-12-31 | 2023-06-26 | filed | yes | `ns6:TurnoverRevenue` | total-exemption-full |
| tax_charge | 0 | GBP | 2022-12-31 | 2023-06-26 | filed | yes | `ns6:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | total-exemption-full |
| total_assets_less_current_liabilities | -216838 | GBP | 2022-12-31 | 2024-09-23 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -216838 | GBP | 2022-12-31 | 2023-06-26 | filed | no | `ns6:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2021-12-31 | 2023-06-26 | filed | yes | `ns6:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| debtors | 12783 | GBP | 2021-12-31 | 2023-06-26 | filed | yes | `ns6:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 12783 | GBP | 2021-12-31 | 2023-06-26 | filed | yes | `ns6:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2021-12-31 | 2023-06-26 | filed | yes | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -219727 | GBP | 2021-12-31 | 2023-06-26 | filed | yes | `ns6:Equity` | total-exemption-full |
| equity | -219627 | GBP | 2021-12-31 | 2023-06-26 | filed | yes | `ns6:Equity` | total-exemption-full |
| fixed_assets | 586 | GBP | 2021-12-31 | 2023-06-26 | filed | yes | `ns6:FixedAssets` | total-exemption-full |
| net_current_assets | -220213 | GBP | 2021-12-31 | 2023-06-26 | filed | yes | `ns6:NetCurrentAssetsLiabilities` | total-exemption-full |
| operating_profit | -4698 | GBP | 2021-12-31 | 2023-06-26 | filed | yes | `ns6:OperatingProfitLoss` | total-exemption-full |
| profit_before_tax | -6774 | GBP | 2021-12-31 | 2023-06-26 | filed | yes | `ns6:ProfitLossOnOrdinaryActivitiesBeforeTax` | total-exemption-full |
| profit_for_period | -6774 | GBP | 2021-12-31 | 2023-06-26 | filed | yes | `ns6:ProfitLoss` | total-exemption-full |
| revenue | 1000 | GBP | 2021-12-31 | 2023-06-26 | filed | yes | `ns6:TurnoverRevenue` | total-exemption-full |
| tax_charge | 0 | GBP | 2021-12-31 | 2023-06-26 | filed | yes | `ns6:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | total-exemption-full |
| total_assets_less_current_liabilities | -219627 | GBP | 2021-12-31 | 2023-06-26 | filed | yes | `ns6:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -212953 | GBP | 2020-12-31 | 2023-06-26 | filed | yes | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2020-12-31 | 2023-06-26 | filed | yes | `ns6:Equity` | total-exemption-full |
| equity | -212853 | GBP | 2020-12-31 | 2023-06-26 | filed | yes | `ns6:Equity` | total-exemption-full |

_No coverage facts for the latest run._

## SIGNUM CORPORATE COMMUNICATIONS LIMITED (`gb:04473901`)

- registration: `04473901` (GB), status active, incorporated 2002-06-29
- classification: ['61100', '62030'] (sic_2007)
- records: 5 officers, 1 beneficial owners, 0 ownership statements, 2 security interests, 73 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 8 | iso4217:GBP | 2025-03-31 | 2026-03-27 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 130000 | GBP | 2025-03-31 | 2026-03-27 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 102538 | GBP | 2025-03-31 | 2026-03-27 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 135501 | GBP | 2025-03-31 | 2026-03-27 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 62237 | GBP | 2025-03-31 | 2026-03-27 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 129956 | GBP | 2025-03-31 | 2026-03-27 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 62237 | GBP | 2025-03-31 | 2026-03-27 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 62281 | GBP | 2025-03-31 | 2026-03-27 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 192237 | GBP | 2025-03-31 | 2026-03-27 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 8 | iso4217:GBP | 2024-03-31 | 2026-03-27 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 9 | iso4217:GBP | 2024-03-31 | 2024-12-31 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 149167 | GBP | 2024-03-31 | 2026-03-27 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 149167 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 103583 | GBP | 2024-03-31 | 2026-03-27 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 103583 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 167554 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 167554 | GBP | 2024-03-31 | 2026-03-27 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 62846 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 62846 | GBP | 2024-03-31 | 2026-03-27 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 128720 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 128720 | GBP | 2024-03-31 | 2026-03-27 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 62846 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 62846 | GBP | 2024-03-31 | 2026-03-27 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 83293 | GBP | 2024-03-31 | 2026-03-27 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 83293 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 212013 | GBP | 2024-03-31 | 2026-03-27 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 212013 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 9 | iso4217:GBP | 2023-03-31 | 2024-12-31 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 9 | iso4217:GBP | 2023-03-31 | 2023-12-29 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 174167 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 174167 | GBP | 2023-03-31 | 2023-12-29 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 127307 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 127307 | GBP | 2023-03-31 | 2023-12-29 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 246547 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 246547 | GBP | 2023-03-31 | 2023-12-29 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | 90682 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `uk-core:Equity` | micro-entity |
| equity | 90682 | GBP | 2023-03-31 | 2023-12-29 | filed | no | `uk-core:Equity` | micro-entity |
| fixed_assets | 107789 | GBP | 2023-03-31 | 2023-12-29 | filed | no | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 107789 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 90682 | GBP | 2023-03-31 | 2023-12-29 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 90682 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 157060 | GBP | 2023-03-31 | 2023-12-29 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 157060 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 264849 | GBP | 2023-03-31 | 2023-12-29 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 264849 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 9 | iso4217:GBP | 2022-03-31 | 2023-12-29 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2022-03-31 | 2023-12-29 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 189111 | GBP | 2022-03-31 | 2023-12-29 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 344554 | GBP | 2022-03-31 | 2023-12-29 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 311277 | GBP | 2022-03-31 | 2023-12-29 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 121017 | GBP | 2022-03-31 | 2023-12-29 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 311277 | GBP | 2022-03-31 | 2023-12-29 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 190260 | GBP | 2022-03-31 | 2023-12-29 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 311277 | GBP | 2022-03-31 | 2023-12-29 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2026-03-27: `{"superseded_document_id": "gb:04473901:doc:RhksADwFO5wTu13FGvsI8eD6_NbdRIExKL-jBGqkpSM", "restatements": [{"concept": "average_employees", "period_end": "2024-03-31", "old_value": "9.0000", "new_valu`

## GILCON SURVEYS LIMITED (`gb:04921963`)

- registration: `04921963` (GB), status active, incorporated 2003-10-06
- classification: ['71129'] (sic_2007)
- records: 3 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 54 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-10-31 | 2026-02-13 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2025-10-31 | 2026-09-28 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | None |
| cash | 37190 | GBP | 2025-10-31 | 2026-09-28 | filed | yes | `ns5:CashBankOnHand` | None |
| cash | 37190 | GBP | 2025-10-31 | 2026-02-13 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 41990 | GBP | 2025-10-31 | 2026-02-13 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 41990 | GBP | 2025-10-31 | 2026-09-28 | filed | yes | `ns5:CurrentAssets` | None |
| debtors | 4800 | GBP | 2025-10-31 | 2026-09-28 | filed | yes | `ns5:Debtors` | None |
| debtors | 4800 | GBP | 2025-10-31 | 2026-02-13 | filed | no | `ns5:Debtors` | total-exemption-full |
| equity | 2033 | GBP | 2025-10-31 | 2026-02-13 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2025-10-31 | 2026-09-28 | filed | yes | `ns5:Equity` | None |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2025-10-31 | 2026-02-13 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2032 | GBP | 2025-10-31 | 2026-02-13 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 20033 | GBP | 2025-10-31 | 2026-09-28 | filed | yes | `ns5:Equity` | None |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 20032 | GBP | 2025-10-31 | 2026-09-28 | filed | yes | `ns5:Equity` | None |
| net_current_assets | 2033 | GBP | 2025-10-31 | 2026-02-13 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 20033 | GBP | 2025-10-31 | 2026-09-28 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | None |
| total_assets_less_current_liabilities | 20033 | GBP | 2025-10-31 | 2026-09-28 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | None |
| total_assets_less_current_liabilities | 2033 | GBP | 2025-10-31 | 2026-02-13 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-10-31 | 2026-09-28 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | None |
| average_employees | 1 | xbrli:pure | 2024-10-31 | 2025-01-10 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-10-31 | 2026-02-13 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 37021 | GBP | 2024-10-31 | 2026-02-13 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 37021 | GBP | 2024-10-31 | 2026-09-28 | filed | yes | `ns5:CashBankOnHand` | None |
| cash | 37021 | GBP | 2024-10-31 | 2025-01-10 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 40061 | GBP | 2024-10-31 | 2026-09-28 | filed | yes | `ns5:CurrentAssets` | None |
| current_assets | 40061 | GBP | 2024-10-31 | 2026-02-13 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 40061 | GBP | 2024-10-31 | 2025-01-10 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 3040 | GBP | 2024-10-31 | 2026-02-13 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 3040 | GBP | 2024-10-31 | 2026-09-28 | filed | yes | `ns5:Debtors` | None |
| debtors | 3040 | GBP | 2024-10-31 | 2025-01-10 | filed | no | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2024-10-31 | 2026-09-28 | filed | yes | `ns5:Equity` | None |
| equity | 13046 | GBP | 2024-10-31 | 2026-09-28 | filed | yes | `ns5:Equity` | None |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 13045 | GBP | 2024-10-31 | 2025-01-10 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2024-10-31 | 2026-02-13 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 13046 | GBP | 2024-10-31 | 2025-01-10 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 13045 | GBP | 2024-10-31 | 2026-02-13 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2024-10-31 | 2025-01-10 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 13045 | GBP | 2024-10-31 | 2026-09-28 | filed | yes | `ns5:Equity` | None |
| equity | 13046 | GBP | 2024-10-31 | 2026-02-13 | filed | no | `ns5:Equity` | total-exemption-full |
| net_current_assets | 13046 | GBP | 2024-10-31 | 2025-01-10 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 13046 | GBP | 2024-10-31 | 2026-02-13 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 13046 | GBP | 2024-10-31 | 2026-09-28 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | None |
| total_assets_less_current_liabilities | 13046 | GBP | 2024-10-31 | 2025-01-10 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 13046 | GBP | 2024-10-31 | 2026-02-13 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 13046 | GBP | 2024-10-31 | 2026-09-28 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | None |
| average_employees | 1 | xbrli:pure | 2023-10-31 | 2025-01-10 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 11248 | GBP | 2023-10-31 | 2025-01-10 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 15166 | GBP | 2023-10-31 | 2025-01-10 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 3918 | GBP | 2023-10-31 | 2025-01-10 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2023-10-31 | 2025-01-10 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 545 | GBP | 2023-10-31 | 2025-01-10 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 544 | GBP | 2023-10-31 | 2025-01-10 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | 545 | GBP | 2023-10-31 | 2025-01-10 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 545 | GBP | 2023-10-31 | 2025-01-10 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2026-09-28: `{"superseded_document_id": "gb:04921963:doc:43-5UV76vntpTKPY5z7cS5S73lhMIi3uwklMlXjbr4s", "restatements": [{"concept": "net_current_assets", "period_end": "2025-10-31", "old_value": "2033.0000", "new_`

## ATLAS INDUSTRIES (UK) LIMITED (`gb:05353195`)

- registration: `05353195` (GB), status active, incorporated 2005-02-04
- classification: ['71111', '71129'] (sic_2007)
- records: 9 officers, 1 beneficial owners, 1 ownership statements, 1 security interests, 80 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## PMOWORKS (UK) LIMITED (`gb:05771484`)

- registration: `05771484` (GB), status active, incorporated 2006-04-06
- classification: ['62020'] (sic_2007)
- records: 5 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 56 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | xbrli:pure | 2025-04-30 | 2025-12-17 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 88 | GBP | 2025-04-30 | 2025-12-17 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 732 | GBP | 2025-04-30 | 2025-12-17 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 644 | GBP | 2025-04-30 | 2025-12-17 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | -30980 | GBP | 2025-04-30 | 2025-12-17 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2025-04-30 | 2025-12-17 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -30981 | GBP | 2025-04-30 | 2025-12-17 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | -30980 | GBP | 2025-04-30 | 2025-12-17 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -25396 | GBP | 2025-04-30 | 2025-12-17 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -25396 | GBP | 2025-04-30 | 2025-12-17 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-04-30 | 2025-01-20 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-04-30 | 2025-12-17 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 63 | GBP | 2024-04-30 | 2025-12-17 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 63 | GBP | 2024-04-30 | 2025-01-20 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 823 | GBP | 2024-04-30 | 2025-12-17 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 823 | GBP | 2024-04-30 | 2025-01-20 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 760 | GBP | 2024-04-30 | 2025-12-17 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 760 | GBP | 2024-04-30 | 2025-01-20 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 760 | GBP | 2024-04-30 | 2025-01-20 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -26008 | GBP | 2024-04-30 | 2025-12-17 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | -26007 | GBP | 2024-04-30 | 2025-01-20 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2024-04-30 | 2025-12-17 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | -26007 | GBP | 2024-04-30 | 2025-12-17 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -26008 | GBP | 2024-04-30 | 2025-01-20 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2024-04-30 | 2025-01-20 | filed | no | `ns5:Equity` | total-exemption-full |
| net_assets | -26007 | GBP | 2024-04-30 | 2025-12-17 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | -26007 | GBP | 2024-04-30 | 2025-01-20 | filed | no | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -13345 | GBP | 2024-04-30 | 2025-01-20 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -13345 | GBP | 2024-04-30 | 2025-12-17 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -13345 | GBP | 2024-04-30 | 2025-12-17 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -13345 | GBP | 2024-04-30 | 2025-01-20 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 1 | xbrli:pure | 2023-04-30 | 2023-10-16 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-04-30 | 2025-01-20 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 905 | GBP | 2023-04-30 | 2025-01-20 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 905 | GBP | 2023-04-30 | 2023-10-16 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 10965 | GBP | 2023-04-30 | 2025-01-20 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 10965 | GBP | 2023-04-30 | 2023-10-16 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 10060 | GBP | 2023-04-30 | 2025-01-20 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original'}` | 10060 | GBP | 2023-04-30 | 2023-10-16 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 10060 | GBP | 2023-04-30 | 2023-10-16 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 10060 | GBP | 2023-04-30 | 2025-01-20 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2023-04-30 | 2025-01-20 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 4153 | GBP | 2023-04-30 | 2023-10-16 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 1 | GBP | 2023-04-30 | 2023-10-16 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 4153 | GBP | 2023-04-30 | 2025-01-20 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 4152 | GBP | 2023-04-30 | 2023-10-16 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 4152 | GBP | 2023-04-30 | 2025-01-20 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 4153 | GBP | 2023-04-30 | 2025-01-20 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets `{'OriginalRevisedDataDimension': 'Original'}` | 4153 | GBP | 2023-04-30 | 2023-10-16 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 5865 | GBP | 2023-04-30 | 2023-10-16 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 5865 | GBP | 2023-04-30 | 2025-01-20 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 20846 | GBP | 2023-04-30 | 2023-10-16 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 20846 | GBP | 2023-04-30 | 2025-01-20 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 2 | xbrli:pure | 2022-04-30 | 2023-10-16 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 1 | GBP | 2022-04-30 | 2023-10-16 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 62752 | GBP | 2022-04-30 | 2023-10-16 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original'}` | 62751 | GBP | 2022-04-30 | 2023-10-16 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 62751 | GBP | 2022-04-30 | 2023-10-16 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 2958 | GBP | 2022-04-30 | 2023-10-16 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2957 | GBP | 2022-04-30 | 2023-10-16 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 1 | GBP | 2022-04-30 | 2023-10-16 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets `{'OriginalRevisedDataDimension': 'Original'}` | 2958 | GBP | 2022-04-30 | 2023-10-16 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 6659 | GBP | 2022-04-30 | 2023-10-16 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 24143 | GBP | 2022-04-30 | 2023-10-16 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## DATA DAM LTD (`gb:06331634`)

- registration: `06331634` (GB), status active, incorporated 2007-08-02
- classification: ['62030'] (sic_2007)
- records: 2 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 41 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | xbrli:pure | 2025-08-31 | 2025-11-20 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 66215 | GBP | 2025-08-31 | 2025-11-20 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 27082 | GBP | 2025-08-31 | 2025-11-20 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -39708 | GBP | 2025-08-31 | 2025-11-20 | filed | yes | `core:Equity` | micro-entity |
| net_assets | -39708 | GBP | 2025-08-31 | 2025-11-20 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -39133 | GBP | 2025-08-31 | 2025-11-20 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -39133 | GBP | 2025-08-31 | 2025-11-20 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2024-08-31 | 2024-10-03 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | xbrli:pure | 2024-08-31 | 2025-11-20 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 3373 | GBP | 2024-08-31 | 2025-11-20 | filed | yes | `core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 3373 | GBP | 2024-08-31 | 2024-10-03 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 56585 | GBP | 2024-08-31 | 2024-10-03 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 56585 | GBP | 2024-08-31 | 2025-11-20 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 26204 | GBP | 2024-08-31 | 2024-10-03 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 26204 | GBP | 2024-08-31 | 2025-11-20 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -34329 | GBP | 2024-08-31 | 2025-11-20 | filed | yes | `core:Equity` | micro-entity |
| equity | -34329 | GBP | 2024-08-31 | 2024-10-03 | filed | no | `core:Equity` | micro-entity |
| net_assets | -34329 | GBP | 2024-08-31 | 2024-10-03 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | -34329 | GBP | 2024-08-31 | 2025-11-20 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -30381 | GBP | 2024-08-31 | 2024-10-03 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -30381 | GBP | 2024-08-31 | 2025-11-20 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -30381 | GBP | 2024-08-31 | 2024-10-03 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -30381 | GBP | 2024-08-31 | 2025-11-20 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2023-08-31 | 2024-10-03 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | xbrli:pure | 2023-08-31 | 2024-04-15 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 7063 | GBP | 2023-08-31 | 2024-10-03 | filed | yes | `core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 7063 | GBP | 2023-08-31 | 2024-04-15 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 22755 | GBP | 2023-08-31 | 2024-10-03 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 22755 | GBP | 2023-08-31 | 2024-04-15 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 23989 | GBP | 2023-08-31 | 2024-04-15 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 23989 | GBP | 2023-08-31 | 2024-10-03 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -6404 | GBP | 2023-08-31 | 2024-10-03 | filed | yes | `core:Equity` | micro-entity |
| equity | -6404 | GBP | 2023-08-31 | 2024-04-15 | filed | no | `core:Equity` | micro-entity |
| net_assets | -6404 | GBP | 2023-08-31 | 2024-10-03 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | -6404 | GBP | 2023-08-31 | 2024-04-15 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 1234 | GBP | 2023-08-31 | 2024-04-15 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 1234 | GBP | 2023-08-31 | 2024-10-03 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 1234 | GBP | 2023-08-31 | 2024-10-03 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 1234 | GBP | 2023-08-31 | 2024-04-15 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2022-08-31 | 2024-04-15 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 10743 | GBP | 2022-08-31 | 2024-04-15 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 14251 | GBP | 2022-08-31 | 2024-04-15 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 15760 | GBP | 2022-08-31 | 2024-04-15 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -9758 | GBP | 2022-08-31 | 2024-04-15 | filed | yes | `core:Equity` | micro-entity |
| net_assets | -9758 | GBP | 2022-08-31 | 2024-04-15 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 1509 | GBP | 2022-08-31 | 2024-04-15 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 1509 | GBP | 2022-08-31 | 2024-04-15 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._
