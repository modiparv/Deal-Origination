# Ingest spot-check

- database: `data/engine.db`
- latest run: `20260814T041005Z-b180fa32`
- companies in store: 3400; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## COMPUTER AND DESIGN SERVICES LIMITED (`gb:01161218`)

- registration: `01161218` (GB), status active, incorporated 1974-02-26
- classification: ['62012'] (sic_2007)
- records: 7 officers, 1 beneficial owners, 0 ownership statements, 3 security interests, 98 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 48 | xbrli:pure | 2025-02-28 | 2025-11-28 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | small |
| cash | 1830014 | GBP | 2025-02-28 | 2025-11-28 | filed | yes | `ns5:CashBankOnHand` | small |
| current_assets | 4556149 | GBP | 2025-02-28 | 2025-11-28 | filed | yes | `ns5:CurrentAssets` | small |
| debtors | 2726135 | GBP | 2025-02-28 | 2025-11-28 | filed | yes | `ns5:Debtors` | small |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 2726135 | GBP | 2025-02-28 | 2025-11-28 | filed | yes | `ns5:Debtors` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-02-28 | 2025-11-28 | filed | yes | `ns5:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1963011 | GBP | 2025-02-28 | 2025-11-28 | filed | yes | `ns5:Equity` | small |
| equity | 1963111 | GBP | 2025-02-28 | 2025-11-28 | filed | yes | `ns5:Equity` | small |
| fixed_assets | 69633 | GBP | 2025-02-28 | 2025-11-28 | filed | yes | `ns5:FixedAssets` | small |
| net_current_assets | 1893478 | GBP | 2025-02-28 | 2025-11-28 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | small |
| total_assets_less_current_liabilities | 1963111 | GBP | 2025-02-28 | 2025-11-28 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | small |
| average_employees | 37 | xbrli:pure | 2024-02-29 | 2024-11-27 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | small |
| average_employees | 37 | xbrli:pure | 2024-02-29 | 2025-11-28 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | small |
| cash | 1875037 | GBP | 2024-02-29 | 2024-11-27 | filed | no | `ns5:CashBankOnHand` | small |
| cash | 1875037 | GBP | 2024-02-29 | 2025-11-28 | filed | yes | `ns5:CashBankOnHand` | small |
| current_assets | 5254822 | GBP | 2024-02-29 | 2024-11-27 | filed | no | `ns5:CurrentAssets` | small |
| current_assets | 5254822 | GBP | 2024-02-29 | 2025-11-28 | filed | yes | `ns5:CurrentAssets` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 3379785 | GBP | 2024-02-29 | 2024-11-27 | filed | no | `ns5:Debtors` | small |
| debtors | 3379785 | GBP | 2024-02-29 | 2024-11-27 | filed | no | `ns5:Debtors` | small |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 3379785 | GBP | 2024-02-29 | 2025-11-28 | filed | yes | `ns5:Debtors` | small |
| debtors | 3379785 | GBP | 2024-02-29 | 2025-11-28 | filed | yes | `ns5:Debtors` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2210042 | GBP | 2024-02-29 | 2025-11-28 | filed | yes | `ns5:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2210042 | GBP | 2024-02-29 | 2024-11-27 | filed | no | `ns5:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-02-29 | 2024-11-27 | filed | no | `ns5:Equity` | small |
| equity | 2210142 | GBP | 2024-02-29 | 2025-11-28 | filed | yes | `ns5:Equity` | small |
| equity | 2210142 | GBP | 2024-02-29 | 2024-11-27 | filed | no | `ns5:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-02-29 | 2025-11-28 | filed | yes | `ns5:Equity` | small |
| fixed_assets | 70124 | GBP | 2024-02-29 | 2025-11-28 | filed | yes | `ns5:FixedAssets` | small |
| fixed_assets | 70124 | GBP | 2024-02-29 | 2024-11-27 | filed | no | `ns5:FixedAssets` | small |
| net_current_assets | 2140018 | GBP | 2024-02-29 | 2025-11-28 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | small |
| net_current_assets | 2140018 | GBP | 2024-02-29 | 2024-11-27 | filed | no | `ns5:NetCurrentAssetsLiabilities` | small |
| total_assets_less_current_liabilities | 2210142 | GBP | 2024-02-29 | 2024-11-27 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | small |
| total_assets_less_current_liabilities | 2210142 | GBP | 2024-02-29 | 2025-11-28 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | small |
| average_employees | 35 | xbrli:pure | 2023-02-28 | 2023-11-26 | filed | no | `ns6:AverageNumberEmployeesDuringPeriod` | small |
| average_employees | 35 | xbrli:pure | 2023-02-28 | 2024-11-27 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | small |
| cash | 2527794 | GBP | 2023-02-28 | 2023-11-26 | filed | no | `ns6:CashBankOnHand` | small |
| cash | 2527794 | GBP | 2023-02-28 | 2024-11-27 | filed | yes | `ns5:CashBankOnHand` | small |
| current_assets | 5585228 | GBP | 2023-02-28 | 2023-11-26 | filed | no | `ns6:CurrentAssets` | small |
| current_assets | 5585228 | GBP | 2023-02-28 | 2024-11-27 | filed | yes | `ns5:CurrentAssets` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 3057434 | GBP | 2023-02-28 | 2024-11-27 | filed | yes | `ns5:Debtors` | small |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 3057434 | GBP | 2023-02-28 | 2023-11-26 | filed | no | `ns6:Debtors` | small |
| debtors | 3057434 | GBP | 2023-02-28 | 2024-11-27 | filed | yes | `ns5:Debtors` | small |
| debtors | 3057434 | GBP | 2023-02-28 | 2023-11-26 | filed | no | `ns6:Debtors` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-02-28 | 2023-11-26 | filed | no | `ns6:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2352309 | GBP | 2023-02-28 | 2023-11-26 | filed | no | `ns6:Equity` | small |
| equity | 2352409 | GBP | 2023-02-28 | 2023-11-26 | filed | no | `ns6:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2352309 | GBP | 2023-02-28 | 2024-11-27 | filed | yes | `ns5:Equity` | small |
| equity | 2352409 | GBP | 2023-02-28 | 2024-11-27 | filed | yes | `ns5:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-02-28 | 2024-11-27 | filed | yes | `ns5:Equity` | small |
| fixed_assets | 49381 | GBP | 2023-02-28 | 2023-11-26 | filed | no | `ns6:FixedAssets` | small |
| fixed_assets | 49381 | GBP | 2023-02-28 | 2024-11-27 | filed | yes | `ns5:FixedAssets` | small |
| net_current_assets | 2303028 | GBP | 2023-02-28 | 2023-11-26 | filed | no | `ns6:NetCurrentAssetsLiabilities` | small |
| net_current_assets | 2303028 | GBP | 2023-02-28 | 2024-11-27 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | small |
| total_assets_less_current_liabilities | 2352409 | GBP | 2023-02-28 | 2023-11-26 | filed | no | `ns6:TotalAssetsLessCurrentLiabilities` | small |
| total_assets_less_current_liabilities | 2352409 | GBP | 2023-02-28 | 2024-11-27 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | small |
| average_employees | 34 | xbrli:pure | 2022-02-28 | 2023-11-26 | filed | yes | `ns6:AverageNumberEmployeesDuringPeriod` | small |
| cash | 3109105 | GBP | 2022-02-28 | 2023-11-26 | filed | yes | `ns6:CashBankOnHand` | small |
| current_assets | 5229880 | GBP | 2022-02-28 | 2023-11-26 | filed | yes | `ns6:CurrentAssets` | small |
| debtors | 2120775 | GBP | 2022-02-28 | 2023-11-26 | filed | yes | `ns6:Debtors` | small |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 2120775 | GBP | 2022-02-28 | 2023-11-26 | filed | yes | `ns6:Debtors` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2127064 | GBP | 2022-02-28 | 2023-11-26 | filed | yes | `ns6:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2022-02-28 | 2023-11-26 | filed | yes | `ns6:Equity` | small |
| equity | 2127164 | GBP | 2022-02-28 | 2023-11-26 | filed | yes | `ns6:Equity` | small |
| fixed_assets | 40360 | GBP | 2022-02-28 | 2023-11-26 | filed | yes | `ns6:FixedAssets` | small |
| net_current_assets | 2086804 | GBP | 2022-02-28 | 2023-11-26 | filed | yes | `ns6:NetCurrentAssetsLiabilities` | small |
| total_assets_less_current_liabilities | 2127164 | GBP | 2022-02-28 | 2023-11-26 | filed | yes | `ns6:TotalAssetsLessCurrentLiabilities` | small |

_No coverage facts for the latest run._

## PEMBROKE DESIGN LIMITED (`gb:01431184`)

- registration: `01431184` (GB), status active, incorporated 1979-06-19
- classification: ['71111'] (sic_2007)
- records: 6 officers, 3 beneficial owners, 0 ownership statements, 6 security interests, 113 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 7 | xbrli:pure | 2025-03-31 | 2025-06-19 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 7035 | GBP | 2025-03-31 | 2025-06-19 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 145096 | GBP | 2025-03-31 | 2025-06-19 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 106406 | GBP | 2025-03-31 | 2025-06-19 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 106406 | GBP | 2025-03-31 | 2025-06-19 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200 | GBP | 2025-03-31 | 2025-06-19 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 119664 | GBP | 2025-03-31 | 2025-06-19 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 119464 | GBP | 2025-03-31 | 2025-06-19 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 119664 | GBP | 2025-03-31 | 2025-06-19 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 13544 | GBP | 2025-03-31 | 2025-06-19 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 121802 | GBP | 2025-03-31 | 2025-06-19 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 7 | xbrli:pure | 2024-03-31 | 2025-06-19 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 7 | xbrli:pure | 2024-03-31 | 2024-12-17 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 10179 | GBP | 2024-03-31 | 2024-12-17 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 10179 | GBP | 2024-03-31 | 2025-06-19 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 181904 | GBP | 2024-03-31 | 2025-06-19 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 181904 | GBP | 2024-03-31 | 2024-12-17 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 142025 | GBP | 2024-03-31 | 2024-12-17 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 142025 | GBP | 2024-03-31 | 2025-06-19 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 142025 | GBP | 2024-03-31 | 2025-06-19 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 142025 | GBP | 2024-03-31 | 2024-12-17 | filed | no | `ns5:Debtors` | total-exemption-full |
| equity | 158644 | GBP | 2024-03-31 | 2024-12-17 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 158444 | GBP | 2024-03-31 | 2025-06-19 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 158444 | GBP | 2024-03-31 | 2024-12-17 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200 | GBP | 2024-03-31 | 2024-12-17 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200 | GBP | 2024-03-31 | 2025-06-19 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 158644 | GBP | 2024-03-31 | 2025-06-19 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 158644 | GBP | 2024-03-31 | 2025-06-19 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 158644 | GBP | 2024-03-31 | 2024-12-17 | filed | no | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 60838 | GBP | 2024-03-31 | 2024-12-17 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 60838 | GBP | 2024-03-31 | 2025-06-19 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 170985 | GBP | 2024-03-31 | 2025-06-19 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 170985 | GBP | 2024-03-31 | 2024-12-17 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 7 | xbrli:pure | 2023-03-31 | 2024-12-17 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 7 | xbrli:pure | 2023-03-31 | 2023-10-02 | filed | no | `ns6:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 5054 | GBP | 2023-03-31 | 2024-12-17 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 5054 | GBP | 2023-03-31 | 2023-10-02 | filed | no | `ns6:CashBankOnHand` | total-exemption-full |
| current_assets | 175024 | GBP | 2023-03-31 | 2023-10-02 | filed | no | `ns6:CurrentAssets` | total-exemption-full |
| current_assets | 175024 | GBP | 2023-03-31 | 2024-12-17 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 133185 | GBP | 2023-03-31 | 2023-10-02 | filed | no | `ns6:Debtors` | total-exemption-full |
| debtors | 133185 | GBP | 2023-03-31 | 2023-10-02 | filed | no | `ns6:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 133185 | GBP | 2023-03-31 | 2024-12-17 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 133185 | GBP | 2023-03-31 | 2024-12-17 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 151000 | GBP | 2023-03-31 | 2024-12-17 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200 | GBP | 2023-03-31 | 2023-10-02 | filed | no | `ns6:Equity` | total-exemption-full |
| equity | 151200 | GBP | 2023-03-31 | 2024-12-17 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 151200 | GBP | 2023-03-31 | 2023-10-02 | filed | no | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 151000 | GBP | 2023-03-31 | 2023-10-02 | filed | no | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200 | GBP | 2023-03-31 | 2024-12-17 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 151200 | GBP | 2023-03-31 | 2023-10-02 | filed | no | `ns6:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 151200 | GBP | 2023-03-31 | 2024-12-17 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 63624 | GBP | 2023-03-31 | 2023-10-02 | filed | no | `ns6:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 63624 | GBP | 2023-03-31 | 2024-12-17 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 174209 | GBP | 2023-03-31 | 2024-12-17 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 174209 | GBP | 2023-03-31 | 2023-10-02 | filed | no | `ns6:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 8 | xbrli:pure | 2022-03-31 | 2023-10-02 | filed | yes | `ns6:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 12608 | GBP | 2022-03-31 | 2023-10-02 | filed | yes | `ns6:CashBankOnHand` | total-exemption-full |
| current_assets | 187614 | GBP | 2022-03-31 | 2023-10-02 | filed | yes | `ns6:CurrentAssets` | total-exemption-full |
| debtors | 136256 | GBP | 2022-03-31 | 2023-10-02 | filed | yes | `ns6:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 136256 | GBP | 2022-03-31 | 2023-10-02 | filed | yes | `ns6:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200 | GBP | 2022-03-31 | 2023-10-02 | filed | yes | `ns6:Equity` | total-exemption-full |
| equity | 139176 | GBP | 2022-03-31 | 2023-10-02 | filed | yes | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 138976 | GBP | 2022-03-31 | 2023-10-02 | filed | yes | `ns6:Equity` | total-exemption-full |
| net_assets | 139176 | GBP | 2022-03-31 | 2023-10-02 | filed | yes | `ns6:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 68676 | GBP | 2022-03-31 | 2023-10-02 | filed | yes | `ns6:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 181240 | GBP | 2022-03-31 | 2023-10-02 | filed | yes | `ns6:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## CLIPPER SERVICES LIMITED (`gb:01705668`)

- registration: `01705668` (GB), status active, incorporated 1983-03-10
- classification: ['62090'] (sic_2007)
- records: 3 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 95 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | iso4217:GBP | 2025-08-31 | 2026-03-24 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 4126 | GBP | 2025-08-31 | 2026-03-24 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 2369 | GBP | 2025-08-31 | 2026-03-24 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 1654 | GBP | 2025-08-31 | 2026-03-24 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 103 | GBP | 2025-08-31 | 2026-03-24 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 1654 | GBP | 2025-08-31 | 2026-03-24 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 1757 | GBP | 2025-08-31 | 2026-03-24 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 1654 | GBP | 2025-08-31 | 2026-03-24 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2024-08-31 | 2025-03-26 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2024-08-31 | 2026-03-24 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 4577 | GBP | 2024-08-31 | 2025-03-26 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 4577 | GBP | 2024-08-31 | 2026-03-24 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 5249 | GBP | 2024-08-31 | 2025-03-26 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 5249 | GBP | 2024-08-31 | 2026-03-24 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 775 | GBP | 2024-08-31 | 2025-03-26 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 775 | GBP | 2024-08-31 | 2026-03-24 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 103 | GBP | 2024-08-31 | 2026-03-24 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 103 | GBP | 2024-08-31 | 2025-03-26 | filed | no | `uk-core:FixedAssets` | micro-entity |
| net_assets | 775 | GBP | 2024-08-31 | 2025-03-26 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 775 | GBP | 2024-08-31 | 2026-03-24 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 672 | GBP | 2024-08-31 | 2025-03-26 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 672 | GBP | 2024-08-31 | 2026-03-24 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 775 | GBP | 2024-08-31 | 2025-03-26 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 775 | GBP | 2024-08-31 | 2026-03-24 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2023-03-31 | 2025-03-26 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2841 | GBP | 2023-03-31 | 2025-03-26 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 3104 | GBP | 2023-03-31 | 2025-03-26 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 2009 | GBP | 2023-03-31 | 2025-03-26 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 1746 | GBP | 2023-03-31 | 2025-03-26 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 2009 | GBP | 2023-03-31 | 2025-03-26 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 263 | GBP | 2023-03-31 | 2025-03-26 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 2009 | GBP | 2023-03-31 | 2025-03-26 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

Coverage @ 2025-08-31: 8/21 concepts available (average_employees, creditors_within_one_year, current_assets, equity, fixed_assets, net_assets, net_current_assets, total_assets_less_current_liabilities)
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

## DESIGNSPAN LIMITED (`gb:01934305`)

- registration: `01934305` (GB), status active, incorporated 1985-07-29
- classification: ['71121'] (sic_2007)
- records: 4 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 87 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-08-31 | 2026-05-30 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 37757 | GBP | 2025-08-31 | 2026-05-30 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 56413 | GBP | 2025-08-31 | 2026-05-30 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 18656 | GBP | 2025-08-31 | 2026-05-30 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 18656 | GBP | 2025-08-31 | 2026-05-30 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 23883 | GBP | 2025-08-31 | 2026-05-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2025-08-31 | 2026-05-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 22883 | GBP | 2025-08-31 | 2026-05-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | 23262 | GBP | 2025-08-31 | 2026-05-30 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 23883 | GBP | 2025-08-31 | 2026-05-30 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-08-31 | 2026-05-30 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-08-31 | 2025-05-25 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 36417 | GBP | 2024-08-31 | 2026-05-30 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 36417 | GBP | 2024-08-31 | 2025-05-25 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 53611 | GBP | 2024-08-31 | 2025-05-25 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 53611 | GBP | 2024-08-31 | 2026-05-30 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 17194 | GBP | 2024-08-31 | 2025-05-25 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 17194 | GBP | 2024-08-31 | 2026-05-30 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 17194 | GBP | 2024-08-31 | 2025-05-25 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 17194 | GBP | 2024-08-31 | 2026-05-30 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2024-08-31 | 2026-05-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 21368 | GBP | 2024-08-31 | 2025-05-25 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 22368 | GBP | 2024-08-31 | 2025-05-25 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 22368 | GBP | 2024-08-31 | 2026-05-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2024-08-31 | 2025-05-25 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 21368 | GBP | 2024-08-31 | 2026-05-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | 21483 | GBP | 2024-08-31 | 2025-05-25 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 21483 | GBP | 2024-08-31 | 2026-05-30 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 22368 | GBP | 2024-08-31 | 2025-05-25 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 22368 | GBP | 2024-08-31 | 2026-05-30 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-08-31 | 2024-05-26 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-08-31 | 2025-05-25 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 50169 | GBP | 2023-08-31 | 2024-05-26 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 50169 | GBP | 2023-08-31 | 2025-05-25 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 58784 | GBP | 2023-08-31 | 2025-05-25 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 58784 | GBP | 2023-08-31 | 2024-05-26 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 8615 | GBP | 2023-08-31 | 2025-05-25 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 8615 | GBP | 2023-08-31 | 2024-05-26 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 8615 | GBP | 2023-08-31 | 2024-05-26 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 8615 | GBP | 2023-08-31 | 2025-05-25 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2023-08-31 | 2024-05-26 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 40559 | GBP | 2023-08-31 | 2025-05-25 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2023-08-31 | 2025-05-25 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 40559 | GBP | 2023-08-31 | 2024-05-26 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 41559 | GBP | 2023-08-31 | 2024-05-26 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 41559 | GBP | 2023-08-31 | 2025-05-25 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | 40814 | GBP | 2023-08-31 | 2024-05-26 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 40814 | GBP | 2023-08-31 | 2025-05-25 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 41559 | GBP | 2023-08-31 | 2025-05-25 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 41559 | GBP | 2023-08-31 | 2024-05-26 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2022-08-31 | 2024-05-26 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 35515 | GBP | 2022-08-31 | 2024-05-26 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 45595 | GBP | 2022-08-31 | 2024-05-26 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 10080 | GBP | 2022-08-31 | 2024-05-26 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 10080 | GBP | 2022-08-31 | 2024-05-26 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 29847 | GBP | 2022-08-31 | 2024-05-26 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 28847 | GBP | 2022-08-31 | 2024-05-26 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2022-08-31 | 2024-05-26 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | 29312 | GBP | 2022-08-31 | 2024-05-26 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 29847 | GBP | 2022-08-31 | 2024-05-26 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

Coverage @ 2025-08-31: 7/21 concepts available (average_employees, cash, current_assets, debtors, equity, net_current_assets, total_assets_less_current_liabilities)
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

## QUARTZ SCIENTIFIC COMPUTING LIMITED (`gb:02126524`)

- registration: `02126524` (GB), status active, incorporated 1987-04-28
- classification: ['71129', '71200', '72190'] (sic_2007)
- records: 9 officers, 1 beneficial owners, 0 ownership statements, 1 security interests, 119 filings, 2 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.08 | xbrli:pure | 2025-03-31 | 2025-12-05 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 209338 | GBP | 2025-03-31 | 2025-12-05 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| current_assets | 333956 | GBP | 2025-03-31 | 2025-12-05 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 124618 | GBP | 2025-03-31 | 2025-12-05 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 124618 | GBP | 2025-03-31 | 2025-12-05 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 284357 | GBP | 2025-03-31 | 2025-12-05 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-03-31 | 2025-12-05 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 284257 | GBP | 2025-03-31 | 2025-12-05 | filed | yes | `core:Equity` | total-exemption-full |
| net_current_assets | 223779 | GBP | 2025-03-31 | 2025-12-05 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 284357 | GBP | 2025-03-31 | 2025-12-05 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0.08 | xbrli:pure | 2024-03-31 | 2025-12-05 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 8 | xbrli:pure | 2024-03-31 | 2024-12-13 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | small |
| cash | 153411 | GBP | 2024-03-31 | 2024-12-13 | filed | no | `core:CashBankOnHand` | small |
| cash | 153411 | GBP | 2024-03-31 | 2025-12-05 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 95516 | GBP | 2024-03-31 | 2024-12-13 | filed | yes | `core:Creditors` | small |
| current_assets | 280857 | GBP | 2024-03-31 | 2024-12-13 | filed | no | `core:CurrentAssets` | small |
| current_assets | 280857 | GBP | 2024-03-31 | 2025-12-05 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 127446 | GBP | 2024-03-31 | 2025-12-05 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 127446 | GBP | 2024-03-31 | 2025-12-05 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 127446 | GBP | 2024-03-31 | 2024-12-13 | filed | no | `core:Debtors` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 127446 | GBP | 2024-03-31 | 2024-12-13 | filed | no | `core:Debtors` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-03-31 | 2024-12-13 | filed | no | `core:Equity` | small |
| equity | 213210 | GBP | 2024-03-31 | 2024-12-13 | filed | no | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 213110 | GBP | 2024-03-31 | 2025-12-05 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 213210 | GBP | 2024-03-31 | 2025-12-05 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 213110 | GBP | 2024-03-31 | 2024-12-13 | filed | no | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-03-31 | 2025-12-05 | filed | yes | `core:Equity` | total-exemption-full |
| net_current_assets | 185341 | GBP | 2024-03-31 | 2025-12-05 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 185341 | GBP | 2024-03-31 | 2024-12-13 | filed | no | `core:NetCurrentAssetsLiabilities` | small |
| total_assets_less_current_liabilities | 213210 | GBP | 2024-03-31 | 2025-12-05 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 213210 | GBP | 2024-03-31 | 2024-12-13 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | small |
| average_employees | 8 | xbrli:pure | 2023-03-31 | 2023-12-20 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | small |
| average_employees | 8 | xbrli:pure | 2023-03-31 | 2024-12-13 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | small |
| cash | 29242 | GBP | 2023-03-31 | 2024-12-13 | filed | yes | `core:CashBankOnHand` | small |
| cash | 29242 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `core:CashBankOnHand` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 66856 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `core:Creditors` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 66856 | GBP | 2023-03-31 | 2024-12-13 | filed | yes | `core:Creditors` | small |
| current_assets | 183684 | GBP | 2023-03-31 | 2024-12-13 | filed | yes | `core:CurrentAssets` | small |
| current_assets | 183684 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `core:CurrentAssets` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 154442 | GBP | 2023-03-31 | 2024-12-13 | filed | yes | `core:Debtors` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 119336 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `core:Debtors` | small |
| debtors | 154442 | GBP | 2023-03-31 | 2024-12-13 | filed | yes | `core:Debtors` | small |
| debtors | 119336 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `core:Debtors` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-03-31 | 2024-12-13 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 151564 | GBP | 2023-03-31 | 2024-12-13 | filed | yes | `core:Equity` | small |
| equity | 151664 | GBP | 2023-03-31 | 2024-12-13 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 151564 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `core:Equity` | small |
| equity | 151664 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `core:Equity` | small |
| net_current_assets | 116828 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `core:NetCurrentAssetsLiabilities` | small |
| net_current_assets | 116828 | GBP | 2023-03-31 | 2024-12-13 | filed | yes | `core:NetCurrentAssetsLiabilities` | small |
| total_assets_less_current_liabilities | 151664 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | small |
| total_assets_less_current_liabilities | 151664 | GBP | 2023-03-31 | 2024-12-13 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | small |
| average_employees | 8 | xbrli:pure | 2022-03-31 | 2023-12-20 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | small |
| cash | 142762 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `core:CashBankOnHand` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 78859 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `core:Creditors` | small |
| current_assets | 279771 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `core:CurrentAssets` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 97870 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `core:Debtors` | small |
| debtors | 97870 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `core:Debtors` | small |
| equity | 244457 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 244357 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `core:Equity` | small |
| net_current_assets | 200912 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `core:NetCurrentAssetsLiabilities` | small |
| total_assets_less_current_liabilities | 244457 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | small |

Coverage @ 2025-03-31: 7/21 concepts available (average_employees, cash, current_assets, debtors, equity, net_current_assets, total_assets_less_current_liabilities)
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

- event restatement @ 2024-12-13: `{"superseded_document_id": "gb:02126524:doc:qyHQpo-hL5UPAyV3idE3EVyJgMkl6XXpo7kLEqtddx0", "restatements": [{"concept": "debtors", "period_end": "2023-03-31", "old_value": "119336.0000", "new_value": "`
- event restatement @ 2025-12-05: `{"superseded_document_id": "gb:02126524:doc:J03Eu3rVKLvI2hlcg-IHs2b31yMHPbxoXN7H5fO5G44", "restatements": [{"concept": "average_employees", "period_end": "2024-03-31", "old_value": "8.0000", "new_valu`

## WATCHGROWTH LIMITED (`gb:02283307`)

- registration: `02283307` (GB), status active, incorporated 1988-08-03
- classification: ['71121', '85600'] (sic_2007)
- records: 4 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 98 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-09-30 | 2026-01-29 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 6728 | GBP | 2025-09-30 | 2026-01-29 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 10852 | GBP | 2025-09-30 | 2026-01-29 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 4124 | GBP | 2025-09-30 | 2026-01-29 | filed | yes | `core:Equity` | micro-entity |
| net_assets | 4124 | GBP | 2025-09-30 | 2026-01-29 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 4124 | GBP | 2025-09-30 | 2026-01-29 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 4124 | GBP | 2025-09-30 | 2026-01-29 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-09-30 | 2024-12-06 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-09-30 | 2026-01-29 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5947 | GBP | 2024-09-30 | 2026-01-29 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5947 | GBP | 2024-09-30 | 2024-12-06 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 24604 | GBP | 2024-09-30 | 2024-12-06 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 24604 | GBP | 2024-09-30 | 2026-01-29 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 18657 | GBP | 2024-09-30 | 2026-01-29 | filed | yes | `core:Equity` | micro-entity |
| equity | 18657 | GBP | 2024-09-30 | 2024-12-06 | filed | no | `core:Equity` | micro-entity |
| net_assets | 18657 | GBP | 2024-09-30 | 2026-01-29 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 18657 | GBP | 2024-09-30 | 2024-12-06 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 18657 | GBP | 2024-09-30 | 2026-01-29 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 18657 | GBP | 2024-09-30 | 2024-12-06 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 18657 | GBP | 2024-09-30 | 2024-12-06 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 18657 | GBP | 2024-09-30 | 2026-01-29 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-09-30 | 2024-04-23 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-09-30 | 2024-12-06 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 22223 | GBP | 2023-09-30 | 2024-12-06 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 22223 | GBP | 2023-09-30 | 2024-04-23 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 57595 | GBP | 2023-09-30 | 2024-04-23 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 57595 | GBP | 2023-09-30 | 2024-12-06 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 35372 | GBP | 2023-09-30 | 2024-12-06 | filed | yes | `core:Equity` | micro-entity |
| equity | 35372 | GBP | 2023-09-30 | 2024-04-23 | filed | no | `core:Equity` | micro-entity |
| net_assets | 35372 | GBP | 2023-09-30 | 2024-04-23 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 35372 | GBP | 2023-09-30 | 2024-12-06 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 35372 | GBP | 2023-09-30 | 2024-12-06 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 35372 | GBP | 2023-09-30 | 2024-04-23 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 35372 | GBP | 2023-09-30 | 2024-04-23 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 35372 | GBP | 2023-09-30 | 2024-12-06 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2022-09-30 | 2024-04-23 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 20588 | GBP | 2022-09-30 | 2024-04-23 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 48050 | GBP | 2022-09-30 | 2024-04-23 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 27462 | GBP | 2022-09-30 | 2024-04-23 | filed | yes | `core:Equity` | micro-entity |
| net_assets | 27462 | GBP | 2022-09-30 | 2024-04-23 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 27462 | GBP | 2022-09-30 | 2024-04-23 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 27462 | GBP | 2022-09-30 | 2024-04-23 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## GRAFX DIGITAL TECHNOLOGIES LTD. (`gb:02431554`)

- registration: `02431554` (GB), status active, incorporated 1989-10-11
- classification: ['62020', '62090'] (sic_2007)
- records: 13 officers, 2 beneficial owners, 0 ownership statements, 5 security interests, 141 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-10-31 | 2026-07-29 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 283 | GBP | 2025-10-31 | 2026-07-29 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 55128 | GBP | 2025-10-31 | 2026-07-29 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 54845 | GBP | 2025-10-31 | 2026-07-29 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 54845 | GBP | 2025-10-31 | 2026-07-29 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 20300 | GBP | 2025-10-31 | 2026-07-29 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | -22809 | GBP | 2025-10-31 | 2026-07-29 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -43109 | GBP | 2025-10-31 | 2026-07-29 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | -22809 | GBP | 2025-10-31 | 2026-07-29 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -21911 | GBP | 2025-10-31 | 2026-07-29 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -21911 | GBP | 2025-10-31 | 2026-07-29 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-10-31 | 2025-07-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 8 | GBP | 2024-10-31 | 2026-07-29 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 8 | GBP | 2024-10-31 | 2025-07-30 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 11651 | GBP | 2024-10-31 | 2025-07-30 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 42204 | GBP | 2024-10-31 | 2025-07-30 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 54927 | GBP | 2024-10-31 | 2026-07-29 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 54927 | GBP | 2024-10-31 | 2025-07-30 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors | 54919 | GBP | 2024-10-31 | 2026-07-29 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 54919 | GBP | 2024-10-31 | 2026-07-29 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 54919 | GBP | 2024-10-31 | 2025-07-30 | filed | no | `core:Debtors` | total-exemption-full |
| equity | 1072 | GBP | 2024-10-31 | 2026-07-29 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 20300 | GBP | 2024-10-31 | 2025-07-30 | filed | no | `core:Equity` | total-exemption-full |
| equity | 1072 | GBP | 2024-10-31 | 2025-07-30 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 20300 | GBP | 2024-10-31 | 2026-07-29 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -19228 | GBP | 2024-10-31 | 2025-07-30 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -19228 | GBP | 2024-10-31 | 2026-07-29 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 1072 | GBP | 2024-10-31 | 2026-07-29 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 1072 | GBP | 2024-10-31 | 2025-07-30 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 12723 | GBP | 2024-10-31 | 2025-07-30 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 12723 | GBP | 2024-10-31 | 2026-07-29 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 12723 | GBP | 2024-10-31 | 2026-07-29 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 12723 | GBP | 2024-10-31 | 2025-07-30 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-10-31 | 2024-05-07 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-10-31 | 2025-07-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 1333 | GBP | 2023-10-31 | 2024-05-07 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 1333 | GBP | 2023-10-31 | 2025-07-30 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 16518 | GBP | 2023-10-31 | 2025-07-30 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 16518 | GBP | 2023-10-31 | 2024-05-07 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 58158 | GBP | 2023-10-31 | 2024-05-07 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 58158 | GBP | 2023-10-31 | 2025-07-30 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 74676 | GBP | 2023-10-31 | 2024-05-07 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 74676 | GBP | 2023-10-31 | 2025-07-30 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 73343 | GBP | 2023-10-31 | 2024-05-07 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 73343 | GBP | 2023-10-31 | 2025-07-30 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -20300 | GBP | 2023-10-31 | 2024-05-07 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 20300 | GBP | 2023-10-31 | 2025-07-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 20300 | GBP | 2023-10-31 | 2024-05-07 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -20300 | GBP | 2023-10-31 | 2025-07-30 | filed | yes | `core:Equity` | total-exemption-full |
| net_current_assets | 16518 | GBP | 2023-10-31 | 2025-07-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 16518 | GBP | 2023-10-31 | 2024-05-07 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 16518 | GBP | 2023-10-31 | 2025-07-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 16518 | GBP | 2023-10-31 | 2024-05-07 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 7 | xbrli:pure | 2023-03-31 | 2024-05-07 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 70295 | GBP | 2023-03-31 | 2024-05-07 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 22437 | GBP | 2023-03-31 | 2024-05-07 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 66289 | GBP | 2023-03-31 | 2024-05-07 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 113768 | GBP | 2023-03-31 | 2024-05-07 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 43471 | GBP | 2023-03-31 | 2024-05-07 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 20300 | GBP | 2023-03-31 | 2024-05-07 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 26832 | GBP | 2023-03-31 | 2024-05-07 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 6532 | GBP | 2023-03-31 | 2024-05-07 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 26832 | GBP | 2023-03-31 | 2024-05-07 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 47479 | GBP | 2023-03-31 | 2024-05-07 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 49474 | GBP | 2023-03-31 | 2024-05-07 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## PARSONS BRINCKERHOFF LTD (`gb:02554514`)

- registration: `02554514` (GB), status active, incorporated 1990-11-01
- classification: ['71129'] (sic_2007)
- records: 48 officers, 1 beneficial owners, 0 ownership statements, 9 security interests, 260 filings, 0 events, 3 source documents

_No figures persisted for this company._

Coverage @ 2024-12-31: 0/21 concepts available
- `average_employees`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `cash`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `creditors_after_one_year`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `creditors_within_one_year`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `current_assets`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `debtors`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `depreciation_amortisation`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `equity`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `fixed_assets`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `gross_profit`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `net_assets`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `net_current_assets`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `operating_profit`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `profit_before_tax`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `profit_for_period`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `retained_earnings`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `revenue`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `share_capital`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `staff_costs`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `tax_charge`: unparseable_format — no machine-readable rendition (content_type=application/pdf)
- `total_assets_less_current_liabilities`: unparseable_format — no machine-readable rendition (content_type=application/pdf)

## APPLICATION ENGINEERING & MAINTENANCE LIMITED (`gb:02677615`)

- registration: `02677615` (GB), status active, incorporated 1992-01-15
- classification: ['71129'] (sic_2007)
- records: 3 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 78 filings, 2 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 3 | xbrli:pure | 2025-07-31 | 2026-07-12 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 121114 | GBP | 2025-07-31 | 2026-07-12 | filed | yes | `ns5:Creditors` | micro-entity |
| current_assets | 204491 | GBP | 2025-07-31 | 2026-07-12 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity | 83811 | GBP | 2025-07-31 | 2026-07-12 | filed | yes | `ns5:Equity` | micro-entity |
| fixed_assets | 1058 | GBP | 2025-07-31 | 2026-07-12 | filed | yes | `ns5:FixedAssets` | micro-entity |
| net_assets | 83811 | GBP | 2025-07-31 | 2026-07-12 | filed | yes | `ns5:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 85553 | GBP | 2025-07-31 | 2026-07-12 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 86611 | GBP | 2025-07-31 | 2026-07-12 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 3 | xbrli:pure | 2024-07-31 | 2025-03-25 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 3 | xbrli:pure | 2024-07-31 | 2026-07-12 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 101150 | GBP | 2024-07-31 | 2025-03-25 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 101151 | GBP | 2024-07-31 | 2026-07-12 | filed | yes | `ns5:Creditors` | micro-entity |
| current_assets | 206251 | GBP | 2024-07-31 | 2025-03-25 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 206251 | GBP | 2024-07-31 | 2026-07-12 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity | 105658 | GBP | 2024-07-31 | 2025-03-25 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 105658 | GBP | 2024-07-31 | 2026-07-12 | filed | yes | `ns5:Equity` | micro-entity |
| fixed_assets | 1549 | GBP | 2024-07-31 | 2025-03-25 | filed | no | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 1549 | GBP | 2024-07-31 | 2026-07-12 | filed | yes | `ns5:FixedAssets` | micro-entity |
| net_assets | 105658 | GBP | 2024-07-31 | 2026-07-12 | filed | yes | `ns5:NetAssetsLiabilities` | micro-entity |
| net_assets | 105658 | GBP | 2024-07-31 | 2025-03-25 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 106824 | GBP | 2024-07-31 | 2025-03-25 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 106823 | GBP | 2024-07-31 | 2026-07-12 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 108372 | GBP | 2024-07-31 | 2026-07-12 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 108373 | GBP | 2024-07-31 | 2025-03-25 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 3 | xbrli:pure | 2023-07-31 | 2025-03-25 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 3 | xbrli:pure | 2023-07-31 | 2024-03-13 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 169383 | GBP | 2023-07-31 | 2024-03-13 | filed | yes | `uk-core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'OriginalRevisedDataDimension': 'Original'}` | 112502 | GBP | 2023-07-31 | 2024-03-13 | filed | yes | `uk-core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 109366 | GBP | 2023-07-31 | 2025-03-25 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 232372 | GBP | 2023-07-31 | 2024-03-13 | filed | no | `uk-core:CurrentAssets` | total-exemption-full |
| current_assets | 230434 | GBP | 2023-07-31 | 2025-03-25 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'OriginalRevisedDataDimension': 'Original'}` | 60491 | GBP | 2023-07-31 | 2024-03-13 | filed | yes | `uk-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses', 'OriginalRevisedDataDimension': 'Original'}` | 121774 | GBP | 2023-07-31 | 2024-03-13 | filed | yes | `uk-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 100 | GBP | 2023-07-31 | 2024-03-13 | filed | yes | `uk-core:Equity` | total-exemption-full |
| equity | 121874 | GBP | 2023-07-31 | 2024-03-13 | filed | no | `uk-core:Equity` | total-exemption-full |
| equity | 121874 | GBP | 2023-07-31 | 2025-03-25 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 2004 | GBP | 2023-07-31 | 2025-03-25 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 2004 | GBP | 2023-07-31 | 2024-03-13 | filed | no | `uk-core:FixedAssets` | total-exemption-full |
| net_assets | 121874 | GBP | 2023-07-31 | 2025-03-25 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 121874 | GBP | 2023-07-31 | 2024-03-13 | filed | no | `uk-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 119870 | GBP | 2023-07-31 | 2024-03-13 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 123006 | GBP | 2023-07-31 | 2025-03-25 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 125010 | GBP | 2023-07-31 | 2025-03-25 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 121874 | GBP | 2023-07-31 | 2024-03-13 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 3 | xbrli:pure | 2022-07-31 | 2024-03-13 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 235067 | GBP | 2022-07-31 | 2024-03-13 | filed | yes | `uk-core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'OriginalRevisedDataDimension': 'Original'}` | 154222 | GBP | 2022-07-31 | 2024-03-13 | filed | yes | `uk-core:Creditors` | total-exemption-full |
| current_assets | 285934 | GBP | 2022-07-31 | 2024-03-13 | filed | yes | `uk-core:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'OriginalRevisedDataDimension': 'Original'}` | 49297 | GBP | 2022-07-31 | 2024-03-13 | filed | yes | `uk-core:Debtors` | total-exemption-full |
| equity | 135534 | GBP | 2022-07-31 | 2024-03-13 | filed | yes | `uk-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 100 | GBP | 2022-07-31 | 2024-03-13 | filed | yes | `uk-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses', 'OriginalRevisedDataDimension': 'Original'}` | 135434 | GBP | 2022-07-31 | 2024-03-13 | filed | yes | `uk-core:Equity` | total-exemption-full |
| fixed_assets | 3822 | GBP | 2022-07-31 | 2024-03-13 | filed | yes | `uk-core:FixedAssets` | total-exemption-full |
| net_assets | 135534 | GBP | 2022-07-31 | 2024-03-13 | filed | yes | `uk-core:NetAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 135534 | GBP | 2022-07-31 | 2024-03-13 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2025-03-25: `{"superseded_document_id": "gb:02677615:doc:qcyPFiBnjvh5AslRvGX_nr02Aj26eUiW6Bx_fYBIYbI", "restatements": [{"concept": "current_assets", "period_end": "2023-07-31", "old_value": "232372.0000", "new_va`
- event restatement @ 2026-07-12: `{"superseded_document_id": "gb:02677615:doc:PfvTEwjoWYket_u8KM-nEwy_THSkQhdWeXNPiwwh4GU", "restatements": [{"concept": "net_current_assets", "period_end": "2024-07-31", "old_value": "106824.0000", "ne`
