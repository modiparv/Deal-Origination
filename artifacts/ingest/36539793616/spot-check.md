# Ingest spot-check

- database: `data/engine.db`
- latest run: `20260929T075842Z-46a701ba`
- companies in store: 14600; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## A.P.H. COMPUTERS LIMITED (`gb:01850989`)

- registration: `01850989` (GB), status active, incorporated 1984-09-26
- classification: ['62090'] (sic_2007)
- records: 4 officers, 2 beneficial owners, 0 ownership statements, 2 security interests, 97 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 25 | xbrli:pure | 2025-09-30 | 2026-06-05 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 2140204 | GBP | 2025-09-30 | 2026-06-05 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments'}` | 49405 | GBP | 2025-09-30 | 2026-06-05 | filed | yes | `ns5:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 836657 | GBP | 2025-09-30 | 2026-06-05 | filed | yes | `ns5:Creditors` | total-exemption-full |
| current_assets | 2648036 | GBP | 2025-09-30 | 2026-06-05 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 346478 | GBP | 2025-09-30 | 2026-06-05 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1865595 | GBP | 2025-09-30 | 2026-06-05 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 1866595 | GBP | 2025-09-30 | 2026-06-05 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2025-09-30 | 2026-06-05 | filed | yes | `ns5:Equity` | total-exemption-full |
| fixed_assets | 127490 | GBP | 2025-09-30 | 2026-06-05 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| net_assets | 1866595 | GBP | 2025-09-30 | 2026-06-05 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1811379 | GBP | 2025-09-30 | 2026-06-05 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1938869 | GBP | 2025-09-30 | 2026-06-05 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 26 | xbrli:pure | 2024-09-30 | 2025-04-08 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 26 | xbrli:pure | 2024-09-30 | 2026-06-05 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 1683360 | GBP | 2024-09-30 | 2026-06-05 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 1683360 | GBP | 2024-09-30 | 2025-04-08 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2024-09-30 | 2026-06-05 | filed | yes | `ns5:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 816104 | GBP | 2024-09-30 | 2026-06-05 | filed | yes | `ns5:Creditors` | total-exemption-full |
| current_assets | 2219391 | GBP | 2024-09-30 | 2026-06-05 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 2219391 | GBP | 2024-09-30 | 2025-04-08 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 385509 | GBP | 2024-09-30 | 2025-04-08 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 385509 | GBP | 2024-09-30 | 2026-06-05 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 385509 | GBP | 2024-09-30 | 2025-04-08 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1516799 | GBP | 2024-09-30 | 2026-06-05 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2024-09-30 | 2026-06-05 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2024-09-30 | 2025-04-08 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 1517799 | GBP | 2024-09-30 | 2026-06-05 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1516800 | GBP | 2024-09-30 | 2025-04-08 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 1517800 | GBP | 2024-09-30 | 2025-04-08 | filed | no | `ns5:Equity` | total-exemption-full |
| fixed_assets | 139391 | GBP | 2024-09-30 | 2026-06-05 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| fixed_assets | 139391 | GBP | 2024-09-30 | 2025-04-08 | filed | no | `ns5:FixedAssets` | total-exemption-full |
| net_assets | 1517799 | GBP | 2024-09-30 | 2026-06-05 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 1517800 | GBP | 2024-09-30 | 2025-04-08 | filed | no | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1403288 | GBP | 2024-09-30 | 2025-04-08 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1403287 | GBP | 2024-09-30 | 2026-06-05 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 283427 | GBP | 2024-09-30 | 2025-04-08 | filed | yes | `ns5:ProfitLoss` | total-exemption-full |
| total_assets_less_current_liabilities | 1542679 | GBP | 2024-09-30 | 2025-04-08 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1542678 | GBP | 2024-09-30 | 2026-06-05 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 24 | xbrli:pure | 2023-09-30 | 2025-04-08 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 24 | xbrli:pure | 2023-09-30 | 2024-05-09 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 1453617 | GBP | 2023-09-30 | 2024-05-09 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 1453617 | GBP | 2023-09-30 | 2025-04-08 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 1911483 | GBP | 2023-09-30 | 2025-04-08 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 1911483 | GBP | 2023-09-30 | 2024-05-09 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 316101 | GBP | 2023-09-30 | 2025-04-08 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 316101 | GBP | 2023-09-30 | 2024-05-09 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 316101 | GBP | 2023-09-30 | 2024-05-09 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 316101 | GBP | 2023-09-30 | 2025-04-08 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1328373 | GBP | 2023-09-30 | 2024-05-09 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 1329373 | GBP | 2023-09-30 | 2024-05-09 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1328373 | GBP | 2023-09-30 | 2025-04-08 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 1329373 | GBP | 2023-09-30 | 2025-04-08 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2023-09-30 | 2025-04-08 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2023-09-30 | 2024-05-09 | filed | no | `ns5:Equity` | total-exemption-full |
| fixed_assets | 182096 | GBP | 2023-09-30 | 2025-04-08 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| fixed_assets | 182096 | GBP | 2023-09-30 | 2024-05-09 | filed | no | `ns5:FixedAssets` | total-exemption-full |
| net_assets | 1329373 | GBP | 2023-09-30 | 2024-05-09 | filed | no | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 1329373 | GBP | 2023-09-30 | 2025-04-08 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1154883 | GBP | 2023-09-30 | 2024-05-09 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1154883 | GBP | 2023-09-30 | 2025-04-08 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 287779 | GBP | 2023-09-30 | 2024-05-09 | filed | yes | `ns5:ProfitLoss` | total-exemption-full |
| total_assets_less_current_liabilities | 1336979 | GBP | 2023-09-30 | 2025-04-08 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1336979 | GBP | 2023-09-30 | 2024-05-09 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 22 | xbrli:pure | 2022-09-30 | 2024-05-09 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 1299680 | GBP | 2022-09-30 | 2024-05-09 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 1790272 | GBP | 2022-09-30 | 2024-05-09 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 348916 | GBP | 2022-09-30 | 2024-05-09 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 348916 | GBP | 2022-09-30 | 2024-05-09 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 1116594 | GBP | 2022-09-30 | 2024-05-09 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2022-09-30 | 2024-05-09 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1115594 | GBP | 2022-09-30 | 2024-05-09 | filed | yes | `ns5:Equity` | total-exemption-full |
| fixed_assets | 135512 | GBP | 2022-09-30 | 2024-05-09 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| net_assets | 1116594 | GBP | 2022-09-30 | 2024-05-09 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 986671 | GBP | 2022-09-30 | 2024-05-09 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1122183 | GBP | 2022-09-30 | 2024-05-09 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2026-06-05: `{"superseded_document_id": "gb:01850989:doc:hCCD2NgwlaXHWG3RWiETnTJDJE6hJOYL_pceuS5SsWE", "restatements": [{"concept": "net_current_assets", "period_end": "2024-09-30", "old_value": "1403288.0000", "n`

## PAV I.T. SERVICES LIMITED (`gb:02314882`)

- registration: `02314882` (GB), status active, incorporated 1988-11-09
- classification: ['62090'] (sic_2007)
- records: 16 officers, 3 beneficial owners, 0 ownership statements, 5 security interests, 208 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## ANGLO-EUROPEAN ENGINEERS LIMITED (`gb:02657930`)

- registration: `02657930` (GB), status active, incorporated 1991-10-28
- classification: ['71121'] (sic_2007)
- records: 6 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 82 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## S & S HEALTHCARE LIMITED (`gb:02924205`)

- registration: `02924205` (GB), status active, incorporated 1994-04-29
- classification: ['86102'] (sic_2007)
- records: 9 officers, 1 beneficial owners, 0 ownership statements, 4 security interests, 93 filings, 2 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.71 | xbrli:pure | 2025-03-31 | 2025-11-24 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | small |
| cash | 470445 | GBP | 2025-03-31 | 2025-11-24 | filed | yes | `core:CashBankOnHand` | small |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 2495 | GBP | 2025-03-31 | 2025-11-24 | filed | yes | `core:Creditors` | small |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 577839 | GBP | 2025-03-31 | 2025-11-24 | filed | yes | `core:Creditors` | small |
| current_assets | 559875 | GBP | 2025-03-31 | 2025-11-24 | filed | yes | `core:CurrentAssets` | small |
| debtors | 84983 | GBP | 2025-03-31 | 2025-11-24 | filed | yes | `core:Debtors` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 269721 | GBP | 2025-03-31 | 2025-11-24 | filed | yes | `core:Equity` | small |
| equity | 369741 | GBP | 2025-03-31 | 2025-11-24 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100020 | GBP | 2025-03-31 | 2025-11-24 | filed | yes | `core:Equity` | small |
| net_assets | 369741 | GBP | 2025-03-31 | 2025-11-24 | filed | yes | `core:NetAssetsLiabilities` | small |
| net_current_assets | -17964 | GBP | 2025-03-31 | 2025-11-24 | filed | yes | `core:NetCurrentAssetsLiabilities` | small |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 286680 | GBP | 2025-03-31 | 2025-11-24 | filed | yes | `core:ProfitLoss` | small |
| profit_for_period | 286680 | GBP | 2025-03-31 | 2025-11-24 | filed | yes | `core:ProfitLoss` | small |
| total_assets_less_current_liabilities | 388936 | GBP | 2025-03-31 | 2025-11-24 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | small |
| average_employees | 69 | xbrli:pure | 2024-03-31 | 2024-11-12 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | small |
| average_employees | 0.6900000000000001 | xbrli:pure | 2024-03-31 | 2025-11-24 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | small |
| cash | 326860 | GBP | 2024-03-31 | 2025-11-24 | filed | yes | `core:CashBankOnHand` | small |
| cash | 326860 | GBP | 2024-03-31 | 2024-11-12 | filed | no | `core:CashBankOnHand` | small |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 13334 | GBP | 2024-03-31 | 2025-11-24 | filed | yes | `core:Creditors` | small |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 13334 | GBP | 2024-03-31 | 2024-11-12 | filed | yes | `core:Creditors` | small |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 520319 | GBP | 2024-03-31 | 2025-11-24 | filed | yes | `core:Creditors` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 520319 | GBP | 2024-03-31 | 2024-11-12 | filed | yes | `core:Creditors` | small |
| current_assets | 491031 | GBP | 2024-03-31 | 2025-11-24 | filed | yes | `core:CurrentAssets` | small |
| current_assets | 491031 | GBP | 2024-03-31 | 2024-11-12 | filed | no | `core:CurrentAssets` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 159724 | GBP | 2024-03-31 | 2024-11-12 | filed | yes | `core:Debtors` | small |
| debtors | 159724 | GBP | 2024-03-31 | 2024-11-12 | filed | no | `core:Debtors` | small |
| debtors | 159724 | GBP | 2024-03-31 | 2025-11-24 | filed | yes | `core:Debtors` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 275041 | GBP | 2024-03-31 | 2024-11-12 | filed | no | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100020 | GBP | 2024-03-31 | 2024-11-12 | filed | no | `core:Equity` | small |
| equity | 375061 | GBP | 2024-03-31 | 2024-11-12 | filed | no | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100020 | GBP | 2024-03-31 | 2025-11-24 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 275041 | GBP | 2024-03-31 | 2025-11-24 | filed | yes | `core:Equity` | small |
| equity | 375061 | GBP | 2024-03-31 | 2025-11-24 | filed | yes | `core:Equity` | small |
| net_assets | 375061 | GBP | 2024-03-31 | 2024-11-12 | filed | no | `core:NetAssetsLiabilities` | small |
| net_assets | 375061 | GBP | 2024-03-31 | 2025-11-24 | filed | yes | `core:NetAssetsLiabilities` | small |
| net_current_assets | -29288 | GBP | 2024-03-31 | 2024-11-12 | filed | no | `core:NetCurrentAssetsLiabilities` | small |
| net_current_assets | -29288 | GBP | 2024-03-31 | 2025-11-24 | filed | yes | `core:NetCurrentAssetsLiabilities` | small |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 110641 | GBP | 2024-03-31 | 2024-11-12 | filed | no | `core:ProfitLoss` | small |
| profit_for_period | 110641 | GBP | 2024-03-31 | 2024-11-12 | filed | no | `core:ProfitLoss` | small |
| profit_for_period | 110641 | GBP | 2024-03-31 | 2025-11-24 | filed | yes | `core:ProfitLoss` | small |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 110641 | GBP | 2024-03-31 | 2025-11-24 | filed | yes | `core:ProfitLoss` | small |
| total_assets_less_current_liabilities | 417795 | GBP | 2024-03-31 | 2025-11-24 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | small |
| total_assets_less_current_liabilities | 417795 | GBP | 2024-03-31 | 2024-11-12 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | small |
| average_employees | 69 | xbrli:pure | 2023-03-31 | 2024-11-12 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | small |
| average_employees | 69 | xbrli:pure | 2023-03-31 | 2023-12-04 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | small |
| cash | 382309 | GBP | 2023-03-31 | 2024-11-12 | filed | yes | `core:CashBankOnHand` | small |
| cash | 382309 | GBP | 2023-03-31 | 2023-12-04 | filed | no | `core:CashBankOnHand` | small |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 23266 | GBP | 2023-03-31 | 2024-11-12 | filed | yes | `core:Creditors` | small |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 23266 | GBP | 2023-03-31 | 2023-12-04 | filed | no | `core:Creditors` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 413638 | GBP | 2023-03-31 | 2024-11-12 | filed | yes | `core:Creditors` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 413638 | GBP | 2023-03-31 | 2023-12-04 | filed | no | `core:Creditors` | small |
| current_assets | 592842 | GBP | 2023-03-31 | 2024-11-12 | filed | yes | `core:CurrentAssets` | small |
| current_assets | 592842 | GBP | 2023-03-31 | 2023-12-04 | filed | no | `core:CurrentAssets` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 206086 | GBP | 2023-03-31 | 2023-12-04 | filed | no | `core:Debtors` | small |
| debtors | 206086 | GBP | 2023-03-31 | 2023-12-04 | filed | no | `core:Debtors` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 206086 | GBP | 2023-03-31 | 2024-11-12 | filed | yes | `core:Debtors` | small |
| debtors | 206086 | GBP | 2023-03-31 | 2024-11-12 | filed | yes | `core:Debtors` | small |
| equity | 599420 | GBP | 2023-03-31 | 2024-11-12 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 527836 | GBP | 2023-03-31 | 2023-12-04 | filed | no | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 499400 | GBP | 2023-03-31 | 2025-11-24 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 499400 | GBP | 2023-03-31 | 2024-11-12 | filed | no | `core:Equity` | small |
| equity | 3187467 | GBP | 2023-03-31 | 2023-12-04 | filed | no | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 0 | GBP | 2023-03-31 | 2024-11-12 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100020 | GBP | 2023-03-31 | 2024-11-12 | filed | no | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100020 | GBP | 2023-03-31 | 2025-11-24 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100020 | GBP | 2023-03-31 | 2023-12-04 | filed | no | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 2559611 | GBP | 2023-03-31 | 2023-12-04 | filed | no | `core:Equity` | small |
| net_assets | 3187467 | GBP | 2023-03-31 | 2023-12-04 | filed | no | `core:NetAssetsLiabilities` | small |
| net_assets | 599420 | GBP | 2023-03-31 | 2024-11-12 | filed | yes | `core:NetAssetsLiabilities` | small |
| net_current_assets | 179204 | GBP | 2023-03-31 | 2024-11-12 | filed | yes | `core:NetCurrentAssetsLiabilities` | small |
| net_current_assets | 179204 | GBP | 2023-03-31 | 2023-12-04 | filed | no | `core:NetCurrentAssetsLiabilities` | small |
| profit_for_period | 138143 | GBP | 2023-03-31 | 2024-11-12 | filed | yes | `core:ProfitLoss` | small |
| profit_for_period | 148841 | GBP | 2023-03-31 | 2023-12-04 | filed | no | `core:ProfitLoss` | small |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 148841 | GBP | 2023-03-31 | 2023-12-04 | filed | no | `core:ProfitLoss` | small |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 138143 | GBP | 2023-03-31 | 2024-11-12 | filed | yes | `core:ProfitLoss` | small |
| total_assets_less_current_liabilities | 659386 | GBP | 2023-03-31 | 2024-11-12 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | small |
| total_assets_less_current_liabilities | 3811133 | GBP | 2023-03-31 | 2023-12-04 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | small |
| average_employees | 68 | xbrli:pure | 2022-03-31 | 2023-12-04 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | small |
| cash | 316979 | GBP | 2022-03-31 | 2023-12-04 | filed | yes | `core:CashBankOnHand` | small |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 33201 | GBP | 2022-03-31 | 2023-12-04 | filed | yes | `core:Creditors` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 357139 | GBP | 2022-03-31 | 2023-12-04 | filed | yes | `core:Creditors` | small |
| current_assets | 584363 | GBP | 2022-03-31 | 2023-12-04 | filed | yes | `core:CurrentAssets` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 267384 | GBP | 2022-03-31 | 2023-12-04 | filed | yes | `core:Debtors` | small |
| debtors | 267384 | GBP | 2022-03-31 | 2023-12-04 | filed | yes | `core:Debtors` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 536257 | GBP | 2022-03-31 | 2024-11-12 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 553995 | GBP | 2022-03-31 | 2023-12-04 | filed | no | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100020 | GBP | 2022-03-31 | 2023-12-04 | filed | no | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100020 | GBP | 2022-03-31 | 2024-11-12 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses', 'RestatementsFirstTimeAdoptionDimension': 'PriorPeriodIncreaseDecrease'}` | -17738 | GBP | 2022-03-31 | 2024-11-12 | filed | yes | `core:Equity` | small |
| equity | 3034456 | GBP | 2022-03-31 | 2023-12-04 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 2380441 | GBP | 2022-03-31 | 2023-12-04 | filed | yes | `core:Equity` | small |
| net_assets | 3034456 | GBP | 2022-03-31 | 2023-12-04 | filed | yes | `core:NetAssetsLiabilities` | small |
| net_current_assets | 227224 | GBP | 2022-03-31 | 2023-12-04 | filed | yes | `core:NetCurrentAssetsLiabilities` | small |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -57384 | GBP | 2022-03-31 | 2023-12-04 | filed | yes | `core:ProfitLoss` | small |
| profit_for_period | -57384 | GBP | 2022-03-31 | 2023-12-04 | filed | yes | `core:ProfitLoss` | small |
| total_assets_less_current_liabilities | 3601757 | GBP | 2022-03-31 | 2023-12-04 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100020 | GBP | 2021-03-31 | 2023-12-04 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 612513 | GBP | 2021-03-31 | 2023-12-04 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 2548107 | GBP | 2021-03-31 | 2023-12-04 | filed | yes | `core:Equity` | small |

_No coverage facts for the latest run._

- event restatement @ 2024-11-12: `{"superseded_document_id": "gb:02924205:doc:RqVfgO0wnubz5v7A0HQIZwW3LwylDFG01tLDgTyijLI", "restatements": [{"concept": "equity", "period_end": "2023-03-31", "old_value": "527836.0000", "new_value": "4`
- event restatement @ 2025-11-24: `{"superseded_document_id": "gb:02924205:doc:5A_6N2Yd5ErysCRc5LpiYD39dj9WeB_Vm8GKZSUGIvk", "restatements": [{"concept": "average_employees", "period_end": "2024-03-31", "old_value": "69.0000", "new_val`

## ACTIVEOPS PLC (`gb:03125867`)

- registration: `03125867` (GB), status active, incorporated 1995-11-14
- classification: ['62090', '63110', '70100', '82990'] (sic_2007)
- records: 28 officers, 0 beneficial owners, 1 ownership statements, 8 security interests, 208 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## ALTRAN UK LIMITED (`gb:03302507`)

- registration: `03302507` (GB), status active, incorporated 1997-01-15
- classification: ['71122'] (sic_2007)
- records: 39 officers, 1 beneficial owners, 1 ownership statements, 1 security interests, 179 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## WAA CHOSEN LIMITED (`gb:03477643`)

- registration: `03477643` (GB), status active, incorporated 1997-12-03
- classification: ['62012', '63110', '70210', '73110'] (sic_2007)
- records: 19 officers, 2 beneficial owners, 0 ownership statements, 5 security interests, 142 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.52 | xbrli:pure | 2025-12-31 | 2026-09-17 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 890633 | GBP | 2025-12-31 | 2026-09-17 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2025-12-31 | 2026-09-17 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1183206 | GBP | 2025-12-31 | 2026-09-17 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 2772579 | GBP | 2025-12-31 | 2026-09-17 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 1881946 | GBP | 2025-12-31 | 2026-09-17 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 908505 | GBP | 2025-12-31 | 2026-09-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 1707438 | GBP | 2025-12-31 | 2026-09-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 325933 | GBP | 2025-12-31 | 2026-09-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 473000 | GBP | 2025-12-31 | 2026-09-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 473000 | GBP | 2025-12-31 | 2026-09-17 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | -541443 | GBP | 2025-12-31 | 2026-09-17 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | 1707438 | GBP | 2025-12-31 | 2026-09-17 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1589373 | GBP | 2025-12-31 | 2026-09-17 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_before_tax | -29754 | GBP | 2025-12-31 | 2026-09-17 | filed | yes | `core:ProfitLossOnOrdinaryActivitiesBeforeTax` | total-exemption-full |
| profit_for_period | 213473 | GBP | 2025-12-31 | 2026-09-17 | filed | yes | `core:ProfitLoss` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 213473 | GBP | 2025-12-31 | 2026-09-17 | filed | yes | `core:ProfitLoss` | total-exemption-full |
| staff_costs | 2514375 | GBP | 2025-12-31 | 2026-09-17 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | total-exemption-full |
| tax_charge | -243227 | GBP | 2025-12-31 | 2026-09-17 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | total-exemption-full |
| total_assets_less_current_liabilities | 1707438 | GBP | 2025-12-31 | 2026-09-17 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 57 | xbrli:pure | 2024-12-31 | 2025-07-18 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 0.5700000000000001 | xbrli:pure | 2024-12-31 | 2026-09-17 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 2008163 | GBP | 2024-12-31 | 2025-07-18 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 2008163 | GBP | 2024-12-31 | 2026-09-17 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 20833 | GBP | 2024-12-31 | 2025-07-18 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 20833 | GBP | 2024-12-31 | 2026-09-17 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1408700 | GBP | 2024-12-31 | 2026-09-17 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1408700 | GBP | 2024-12-31 | 2025-07-18 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 4625085 | GBP | 2024-12-31 | 2025-07-18 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 4625085 | GBP | 2024-12-31 | 2026-09-17 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 2464266 | GBP | 2024-12-31 | 2025-07-18 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 2464266 | GBP | 2024-12-31 | 2026-09-17 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2513397 | GBP | 2024-12-31 | 2025-07-18 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 473000 | GBP | 2024-12-31 | 2026-09-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 3312330 | GBP | 2024-12-31 | 2025-07-18 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 325933 | GBP | 2024-12-31 | 2026-09-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 473000 | GBP | 2024-12-31 | 2026-09-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 3312330 | GBP | 2024-12-31 | 2026-09-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 473000 | GBP | 2024-12-31 | 2025-07-18 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 325933 | GBP | 2024-12-31 | 2025-07-18 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 473000 | GBP | 2024-12-31 | 2025-07-18 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2513397 | GBP | 2024-12-31 | 2026-09-17 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 134770 | GBP | 2024-12-31 | 2025-07-18 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | 3312330 | GBP | 2024-12-31 | 2025-07-18 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 3312330 | GBP | 2024-12-31 | 2026-09-17 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 3216385 | GBP | 2024-12-31 | 2026-09-17 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 3216385 | GBP | 2024-12-31 | 2025-07-18 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_before_tax | 445857 | GBP | 2024-12-31 | 2026-09-17 | filed | yes | `core:ProfitLossOnOrdinaryActivitiesBeforeTax` | total-exemption-full |
| profit_before_tax | 445857 | GBP | 2024-12-31 | 2025-07-18 | filed | no | `core:ProfitLossOnOrdinaryActivitiesBeforeTax` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 505665 | GBP | 2024-12-31 | 2026-09-17 | filed | yes | `core:ProfitLoss` | total-exemption-full |
| profit_for_period | 505665 | GBP | 2024-12-31 | 2026-09-17 | filed | yes | `core:ProfitLoss` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 505665 | GBP | 2024-12-31 | 2025-07-18 | filed | no | `core:ProfitLoss` | total-exemption-full |
| profit_for_period | 505665 | GBP | 2024-12-31 | 2025-07-18 | filed | no | `core:ProfitLoss` | total-exemption-full |
| staff_costs | 2665025 | GBP | 2024-12-31 | 2026-09-17 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | total-exemption-full |
| staff_costs | 2665025 | GBP | 2024-12-31 | 2025-07-18 | filed | no | `core:StaffCostsEmployeeBenefitsExpense` | total-exemption-full |
| tax_charge | -59808 | GBP | 2024-12-31 | 2025-07-18 | filed | no | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | total-exemption-full |
| tax_charge | -59808 | GBP | 2024-12-31 | 2026-09-17 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | total-exemption-full |
| total_assets_less_current_liabilities | 3351155 | GBP | 2024-12-31 | 2025-07-18 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 3351155 | GBP | 2024-12-31 | 2026-09-17 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 58 | xbrli:pure | 2023-12-31 | 2025-07-18 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 58 | xbrli:pure | 2023-12-31 | 2024-09-24 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | full |
| cash | 1183105 | GBP | 2023-12-31 | 2025-07-18 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 1183105 | GBP | 2023-12-31 | 2024-09-24 | filed | no | `core:CashBankOnHand` | full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 70833 | GBP | 2023-12-31 | 2025-07-18 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 70833 | GBP | 2023-12-31 | 2024-09-24 | filed | no | `core:Creditors` | full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1844332 | GBP | 2023-12-31 | 2024-09-24 | filed | no | `core:Creditors` | full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1844332 | GBP | 2023-12-31 | 2025-07-18 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 4567018 | GBP | 2023-12-31 | 2025-07-18 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 4567018 | GBP | 2023-12-31 | 2024-09-24 | filed | no | `core:CurrentAssets` | full |
| debtors | 3383913 | GBP | 2023-12-31 | 2025-07-18 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 3383913 | GBP | 2023-12-31 | 2024-09-24 | filed | no | `core:Debtors` | full |
| equity | 2882359 | GBP | 2023-12-31 | 2024-09-24 | filed | no | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 473000 | GBP | 2023-12-31 | 2024-09-24 | filed | no | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 473000 | GBP | 2023-12-31 | 2025-07-18 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2083426 | GBP | 2023-12-31 | 2026-09-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2083426 | GBP | 2023-12-31 | 2024-09-24 | filed | no | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 325933 | GBP | 2023-12-31 | 2025-07-18 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 473000 | GBP | 2023-12-31 | 2025-07-18 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 2882359 | GBP | 2023-12-31 | 2025-07-18 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2083426 | GBP | 2023-12-31 | 2025-07-18 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 325933 | GBP | 2023-12-31 | 2026-09-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 325933 | GBP | 2023-12-31 | 2024-09-24 | filed | no | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 473000 | GBP | 2023-12-31 | 2026-09-17 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 284207 | GBP | 2023-12-31 | 2024-09-24 | filed | no | `core:FixedAssets` | full |
| fixed_assets | 284207 | GBP | 2023-12-31 | 2025-07-18 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | 2882359 | GBP | 2023-12-31 | 2025-07-18 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 2882359 | GBP | 2023-12-31 | 2024-09-24 | filed | no | `core:NetAssetsLiabilities` | full |
| net_current_assets | 2722686 | GBP | 2023-12-31 | 2025-07-18 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 2722686 | GBP | 2023-12-31 | 2024-09-24 | filed | no | `core:NetCurrentAssetsLiabilities` | full |
| profit_before_tax | 364122 | GBP | 2023-12-31 | 2024-09-24 | filed | no | `core:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_before_tax | 364122 | GBP | 2023-12-31 | 2025-07-18 | filed | yes | `core:ProfitLossOnOrdinaryActivitiesBeforeTax` | total-exemption-full |
| profit_for_period | 287389 | GBP | 2023-12-31 | 2025-07-18 | filed | yes | `core:ProfitLoss` | total-exemption-full |
| profit_for_period | 287389 | GBP | 2023-12-31 | 2024-09-24 | filed | no | `core:ProfitLoss` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 287389 | GBP | 2023-12-31 | 2025-07-18 | filed | yes | `core:ProfitLoss` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 287389 | GBP | 2023-12-31 | 2024-09-24 | filed | no | `core:ProfitLoss` | full |
| staff_costs | 2672190 | GBP | 2023-12-31 | 2024-09-24 | filed | no | `core:StaffCostsEmployeeBenefitsExpense` | full |
| staff_costs | 2672190 | GBP | 2023-12-31 | 2025-07-18 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | total-exemption-full |
| tax_charge | 76733 | GBP | 2023-12-31 | 2024-09-24 | filed | no | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| tax_charge | 76733 | GBP | 2023-12-31 | 2025-07-18 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | total-exemption-full |
| total_assets_less_current_liabilities | 3006893 | GBP | 2023-12-31 | 2024-09-24 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | full |
| total_assets_less_current_liabilities | 3006893 | GBP | 2023-12-31 | 2025-07-18 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 59 | xbrli:pure | 2022-12-31 | 2024-09-24 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | full |
| cash | 1573781 | GBP | 2022-12-31 | 2024-09-24 | filed | yes | `core:CashBankOnHand` | full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 120833 | GBP | 2022-12-31 | 2024-09-24 | filed | yes | `core:Creditors` | full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2482987 | GBP | 2022-12-31 | 2024-09-24 | filed | yes | `core:Creditors` | full |
| current_assets | 4820743 | GBP | 2022-12-31 | 2024-09-24 | filed | yes | `core:CurrentAssets` | full |
| debtors | 3246962 | GBP | 2022-12-31 | 2024-09-24 | filed | yes | `core:Debtors` | full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 325933 | GBP | 2022-12-31 | 2025-07-18 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1849037 | GBP | 2022-12-31 | 2024-09-24 | filed | no | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 473000 | GBP | 2022-12-31 | 2025-07-18 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 473000 | GBP | 2022-12-31 | 2024-09-24 | filed | no | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 325933 | GBP | 2022-12-31 | 2024-09-24 | filed | no | `core:Equity` | full |
| equity | 2647970 | GBP | 2022-12-31 | 2024-09-24 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1849037 | GBP | 2022-12-31 | 2025-07-18 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 482310 | GBP | 2022-12-31 | 2024-09-24 | filed | yes | `core:FixedAssets` | full |
| net_assets | 2647970 | GBP | 2022-12-31 | 2024-09-24 | filed | yes | `core:NetAssetsLiabilities` | full |
| net_current_assets | 2337756 | GBP | 2022-12-31 | 2024-09-24 | filed | yes | `core:NetCurrentAssetsLiabilities` | full |
| profit_before_tax | 1412035 | GBP | 2022-12-31 | 2024-09-24 | filed | yes | `core:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1185828 | GBP | 2022-12-31 | 2024-09-24 | filed | yes | `core:ProfitLoss` | full |
| profit_for_period | 1185828 | GBP | 2022-12-31 | 2024-09-24 | filed | yes | `core:ProfitLoss` | full |
| staff_costs | 2652459 | GBP | 2022-12-31 | 2024-09-24 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | full |
| tax_charge | 226207 | GBP | 2022-12-31 | 2024-09-24 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| total_assets_less_current_liabilities | 2820066 | GBP | 2022-12-31 | 2024-09-24 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 663209 | GBP | 2021-12-31 | 2024-09-24 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 325933 | GBP | 2021-12-31 | 2024-09-24 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 473000 | GBP | 2021-12-31 | 2024-09-24 | filed | yes | `core:Equity` | full |

_No coverage facts for the latest run._

- event restatement @ 2026-09-17: `{"superseded_document_id": "gb:03477643:doc:y2nIf-yGH8nYtWmseqQL3LCl9-6w0KzFvlaTxfc_IyM", "restatements": [{"concept": "average_employees", "period_end": "2024-12-31", "old_value": "57.0000", "new_val`

## LIVEWIRES AUTOMATION LTD (`gb:03725855`)

- registration: `03725855` (GB), status active, incorporated 1999-03-03
- classification: ['62090'] (sic_2007)
- records: 4 officers, 2 beneficial owners, 1 ownership statements, 0 security interests, 70 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-03-31 | 2025-12-08 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 31540 | GBP | 2025-03-31 | 2025-12-08 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 35453 | GBP | 2025-03-31 | 2025-12-08 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 2508 | GBP | 2025-03-31 | 2025-12-08 | filed | yes | `core:Equity` | micro-entity |
| net_assets | 2508 | GBP | 2025-03-31 | 2025-12-08 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 3913 | GBP | 2025-03-31 | 2025-12-08 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 3913 | GBP | 2025-03-31 | 2025-12-08 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-03-31 | 2025-12-08 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2024-03-31 | 2024-08-27 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2024-03-31 | 2024-08-27 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 20050 | GBP | 2024-03-31 | 2024-08-27 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 18688 | GBP | 2024-03-31 | 2025-12-08 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 34738 | GBP | 2024-03-31 | 2025-12-08 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 34738 | GBP | 2024-03-31 | 2024-08-27 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | 14689 | GBP | 2024-03-31 | 2025-12-08 | filed | yes | `core:Equity` | micro-entity |
| equity | 14689 | GBP | 2024-03-31 | 2024-08-27 | filed | no | `uk-core:Equity` | micro-entity |
| fixed_assets | 1 | GBP | 2024-03-31 | 2025-12-08 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 1 | GBP | 2024-03-31 | 2024-08-27 | filed | no | `uk-core:FixedAssets` | micro-entity |
| net_assets | 14689 | GBP | 2024-03-31 | 2024-08-27 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 14689 | GBP | 2024-03-31 | 2025-12-08 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 14688 | GBP | 2024-03-31 | 2024-08-27 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 16050 | GBP | 2024-03-31 | 2025-12-08 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 14689 | GBP | 2024-03-31 | 2024-08-27 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 16051 | GBP | 2024-03-31 | 2025-12-08 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2023-03-31 | 2024-08-27 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2023-03-31 | 2023-12-14 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2023-03-31 | 2024-08-27 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2023-03-31 | 2023-12-14 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 35272 | GBP | 2023-03-31 | 2023-12-14 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 35272 | GBP | 2023-03-31 | 2024-08-27 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 25956 | GBP | 2023-03-31 | 2023-12-14 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 25956 | GBP | 2023-03-31 | 2024-08-27 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 9315 | GBP | 2023-03-31 | 2023-12-14 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 9315 | GBP | 2023-03-31 | 2024-08-27 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 1 | GBP | 2023-03-31 | 2024-08-27 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 1 | GBP | 2023-03-31 | 2023-12-14 | filed | no | `uk-core:FixedAssets` | micro-entity |
| net_assets | 9315 | GBP | 2023-03-31 | 2024-08-27 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 9315 | GBP | 2023-03-31 | 2023-12-14 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 9316 | GBP | 2023-03-31 | 2024-08-27 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 9316 | GBP | 2023-03-31 | 2023-12-14 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 9315 | GBP | 2023-03-31 | 2023-12-14 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 9315 | GBP | 2023-03-31 | 2024-08-27 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2022-03-31 | 2023-12-14 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2022-03-31 | 2023-12-14 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 13211 | GBP | 2022-03-31 | 2023-12-14 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 28034 | GBP | 2022-03-31 | 2023-12-14 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 14824 | GBP | 2022-03-31 | 2023-12-14 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 1 | GBP | 2022-03-31 | 2023-12-14 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 14824 | GBP | 2022-03-31 | 2023-12-14 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 14823 | GBP | 2022-03-31 | 2023-12-14 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 14824 | GBP | 2022-03-31 | 2023-12-14 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

Coverage @ 2025-03-31: 7/21 concepts available (average_employees, creditors_within_one_year, current_assets, equity, net_assets, net_current_assets, total_assets_less_current_liabilities)
- `cash`: filed_without_concept — regime 'micro-entity' omits this concept
- `creditors_after_one_year`: filed_without_concept — regime 'micro-entity' omits this concept
- `debtors`: filed_without_concept — regime 'micro-entity' omits this concept
- `depreciation_amortisation`: filed_without_concept — regime 'micro-entity' omits this concept
- `fixed_assets`: filed_without_concept — regime 'micro-entity' omits this concept
- `gross_profit`: filed_without_concept — regime 'micro-entity' omits this concept
- `operating_profit`: filed_without_concept — regime 'micro-entity' omits this concept
- `profit_before_tax`: filed_without_concept — regime 'micro-entity' omits this concept
- `profit_for_period`: filed_without_concept — regime 'micro-entity' omits this concept
- `retained_earnings`: filed_without_concept — regime 'micro-entity' omits this concept
- `revenue`: filed_without_concept — regime 'micro-entity' omits this concept
- `share_capital`: filed_without_concept — regime 'micro-entity' omits this concept
- `staff_costs`: filed_without_concept — regime 'micro-entity' omits this concept
- `tax_charge`: filed_without_concept — regime 'micro-entity' omits this concept

- event restatement @ 2025-12-08: `{"superseded_document_id": "gb:03725855:doc:N6ja1-xFF0CgKS6PCDIq7GAKSjOoCERuqlZpRAqepcY", "restatements": [{"concept": "creditors_within_one_year", "period_end": "2024-03-31", "old_value": "20050.0000`

## MAISON D'ETRE PROPERTIES LIMITED (`gb:04032789`)

- registration: `04032789` (GB), status active, incorporated 2000-07-13
- classification: ['71122'] (sic_2007)
- records: 4 officers, 2 beneficial owners, 0 ownership statements, 5 security interests, 81 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-07-31 | 2026-01-05 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 100 | GBP | 2025-07-31 | 2026-01-05 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 3487 | GBP | 2025-07-31 | 2026-01-05 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 3387 | GBP | 2025-07-31 | 2026-01-05 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 3387 | GBP | 2025-07-31 | 2026-01-05 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2025-07-31 | 2026-01-05 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 77 | GBP | 2025-07-31 | 2026-01-05 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 75 | GBP | 2025-07-31 | 2026-01-05 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | 77 | GBP | 2025-07-31 | 2026-01-05 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 77 | GBP | 2025-07-31 | 2026-01-05 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-07-31 | 2026-01-05 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-07-31 | 2025-04-01 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 78 | GBP | 2024-07-31 | 2026-01-05 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 78 | GBP | 2024-07-31 | 2025-04-01 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 8040 | GBP | 2024-07-31 | 2025-04-01 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 8040 | GBP | 2024-07-31 | 2026-01-05 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 7962 | GBP | 2024-07-31 | 2025-04-01 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 7962 | GBP | 2024-07-31 | 2026-01-05 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 7962 | GBP | 2024-07-31 | 2025-04-01 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 7962 | GBP | 2024-07-31 | 2026-01-05 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1970 | GBP | 2024-07-31 | 2026-01-05 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 1972 | GBP | 2024-07-31 | 2026-01-05 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1970 | GBP | 2024-07-31 | 2025-04-01 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-07-31 | 2025-04-01 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-07-31 | 2026-01-05 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 1972 | GBP | 2024-07-31 | 2025-04-01 | filed | no | `ns5:Equity` | total-exemption-full |
| net_current_assets | 1972 | GBP | 2024-07-31 | 2026-01-05 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1972 | GBP | 2024-07-31 | 2025-04-01 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1972 | GBP | 2024-07-31 | 2025-04-01 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1972 | GBP | 2024-07-31 | 2026-01-05 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-07-31 | 2025-04-01 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 2 | xbrli:pure | 2023-07-31 | 2024-01-09 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 86 | GBP | 2023-07-31 | 2025-04-01 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 86 | GBP | 2023-07-31 | 2024-01-09 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 2911 | GBP | 2023-07-31 | 2024-01-09 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 2911 | GBP | 2023-07-31 | 2025-04-01 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2825 | GBP | 2023-07-31 | 2024-01-09 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 2825 | GBP | 2023-07-31 | 2025-04-01 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 2825 | GBP | 2023-07-31 | 2025-04-01 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original'}` | 2825 | GBP | 2023-07-31 | 2024-01-09 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 0 | GBP | 2023-07-31 | 2025-04-01 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 2 | GBP | 2023-07-31 | 2024-01-09 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-07-31 | 2025-04-01 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 2 | GBP | 2023-07-31 | 2024-01-09 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 2 | GBP | 2023-07-31 | 2025-04-01 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 0 | GBP | 2023-07-31 | 2024-01-09 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets `{'OriginalRevisedDataDimension': 'Original'}` | 2 | GBP | 2023-07-31 | 2024-01-09 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 2 | GBP | 2023-07-31 | 2025-04-01 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 2 | GBP | 2023-07-31 | 2024-01-09 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 2 | GBP | 2023-07-31 | 2025-04-01 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 2 | GBP | 2023-07-31 | 2024-01-09 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 2 | xbrli:pure | 2022-07-31 | 2024-01-09 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 957 | GBP | 2022-07-31 | 2024-01-09 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 31051 | GBP | 2022-07-31 | 2024-01-09 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 30094 | GBP | 2022-07-31 | 2024-01-09 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original'}` | 30094 | GBP | 2022-07-31 | 2024-01-09 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 23029 | GBP | 2022-07-31 | 2024-01-09 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 23027 | GBP | 2022-07-31 | 2024-01-09 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 2 | GBP | 2022-07-31 | 2024-01-09 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets `{'OriginalRevisedDataDimension': 'Original'}` | 23029 | GBP | 2022-07-31 | 2024-01-09 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 22489 | GBP | 2022-07-31 | 2024-01-09 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 23156 | GBP | 2022-07-31 | 2024-01-09 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

Coverage @ 2025-07-31: 7/21 concepts available (average_employees, cash, current_assets, debtors, equity, net_current_assets, total_assets_less_current_liabilities)
- `creditors_after_one_year`: filed_without_concept — absent though regime 'total-exemption-full' typically includes it
- `creditors_within_one_year`: filed_without_concept — absent though regime 'total-exemption-full' typically includes it
- `depreciation_amortisation`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `fixed_assets`: filed_without_concept — absent though regime 'total-exemption-full' typically includes it
- `gross_profit`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `net_assets`: filed_without_concept — absent though regime 'total-exemption-full' typically includes it
- `operating_profit`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `profit_before_tax`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `profit_for_period`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `retained_earnings`: filed_without_concept — absent though regime 'total-exemption-full' typically includes it
- `revenue`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `share_capital`: filed_without_concept — absent though regime 'total-exemption-full' typically includes it
- `staff_costs`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `tax_charge`: filed_without_concept — regime 'total-exemption-full' omits this concept
