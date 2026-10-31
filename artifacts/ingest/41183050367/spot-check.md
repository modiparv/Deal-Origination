# Ingest spot-check

- database: `data/engine.db`
- latest run: `20261031T080439Z-f609bf18`
- companies in store: 40200; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## ADFLEX LIMITED (`gb:02579576`)

- registration: `02579576` (GB), status active, incorporated 1991-02-04
- classification: ['62090'] (sic_2007)
- records: 5 officers, 1 beneficial owners, 0 ownership statements, 5 security interests, 101 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 16 | xbrli:pure | 2025-02-28 | 2025-09-19 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 2954290 | GBP | 2025-02-28 | 2025-09-19 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 3643091 | GBP | 2025-02-28 | 2025-09-19 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 688801 | GBP | 2025-02-28 | 2025-09-19 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 688801 | GBP | 2025-02-28 | 2025-09-19 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'FurtherSpecificReserve1ComponentTotalEquity'}` | 578836 | GBP | 2025-02-28 | 2025-09-19 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2025-02-28 | 2025-09-19 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3421972 | GBP | 2025-02-28 | 2025-09-19 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 4000810 | GBP | 2025-02-28 | 2025-09-19 | filed | yes | `ns5:Equity` | total-exemption-full |
| fixed_assets | 803864 | GBP | 2025-02-28 | 2025-09-19 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| net_assets | 4000810 | GBP | 2025-02-28 | 2025-09-19 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 3296421 | GBP | 2025-02-28 | 2025-09-19 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 103066 | GBP | 2025-02-28 | 2025-09-19 | filed | yes | `ns5:ProfitLoss` | total-exemption-full |
| profit_for_period | 103066 | GBP | 2025-02-28 | 2025-09-19 | filed | yes | `ns5:ProfitLoss` | total-exemption-full |
| total_assets_less_current_liabilities | 4100285 | GBP | 2025-02-28 | 2025-09-19 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 15 | xbrli:pure | 2024-02-29 | 2024-11-28 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 15 | xbrli:pure | 2024-02-29 | 2025-09-19 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 3144126 | GBP | 2024-02-29 | 2024-11-28 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 3144126 | GBP | 2024-02-29 | 2025-09-19 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 3711129 | GBP | 2024-02-29 | 2024-11-28 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 3711129 | GBP | 2024-02-29 | 2025-09-19 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 567003 | GBP | 2024-02-29 | 2025-09-19 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 567003 | GBP | 2024-02-29 | 2024-11-28 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 567003 | GBP | 2024-02-29 | 2024-11-28 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 567003 | GBP | 2024-02-29 | 2025-09-19 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-02-29 | 2024-11-28 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 3927074 | GBP | 2024-02-29 | 2024-11-28 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3368906 | GBP | 2024-02-29 | 2024-11-28 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'FurtherSpecificReserve1ComponentTotalEquity'}` | 558166 | GBP | 2024-02-29 | 2025-09-19 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'FurtherSpecificReserve1ComponentTotalEquity'}` | 558166 | GBP | 2024-02-29 | 2024-11-28 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3368906 | GBP | 2024-02-29 | 2025-09-19 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 3927074 | GBP | 2024-02-29 | 2025-09-19 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-02-29 | 2025-09-19 | filed | yes | `ns5:Equity` | total-exemption-full |
| fixed_assets | 805360 | GBP | 2024-02-29 | 2025-09-19 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| fixed_assets | 805360 | GBP | 2024-02-29 | 2024-11-28 | filed | no | `ns5:FixedAssets` | total-exemption-full |
| net_assets | 3927074 | GBP | 2024-02-29 | 2025-09-19 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 3927074 | GBP | 2024-02-29 | 2024-11-28 | filed | no | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 3239346 | GBP | 2024-02-29 | 2025-09-19 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 3239346 | GBP | 2024-02-29 | 2024-11-28 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 303546 | GBP | 2024-02-29 | 2024-11-28 | filed | yes | `ns5:ProfitLoss` | total-exemption-full |
| profit_for_period | 303546 | GBP | 2024-02-29 | 2024-11-28 | filed | yes | `ns5:ProfitLoss` | total-exemption-full |
| total_assets_less_current_liabilities | 4044706 | GBP | 2024-02-29 | 2025-09-19 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 4044706 | GBP | 2024-02-29 | 2024-11-28 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 13 | xbrli:pure | 2023-02-28 | 2024-11-28 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 13 | xbrli:pure | 2023-02-28 | 2023-06-21 | filed | no | `ns6:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 3005342 | GBP | 2023-02-28 | 2023-06-21 | filed | no | `ns6:CashBankOnHand` | total-exemption-full |
| cash | 3005342 | GBP | 2023-02-28 | 2024-11-28 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 3459270 | GBP | 2023-02-28 | 2023-06-21 | filed | no | `ns6:CurrentAssets` | total-exemption-full |
| current_assets | 3459270 | GBP | 2023-02-28 | 2024-11-28 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 453928 | GBP | 2023-02-28 | 2023-06-21 | filed | no | `ns6:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 453928 | GBP | 2023-02-28 | 2024-11-28 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 453928 | GBP | 2023-02-28 | 2023-06-21 | filed | no | `ns6:Debtors` | total-exemption-full |
| debtors | 453928 | GBP | 2023-02-28 | 2024-11-28 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-02-28 | 2024-11-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-02-28 | 2023-06-21 | filed | no | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3305360 | GBP | 2023-02-28 | 2024-11-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 3863528 | GBP | 2023-02-28 | 2023-06-21 | filed | no | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'FurtherSpecificReserve1ComponentTotalEquity'}` | 558166 | GBP | 2023-02-28 | 2023-06-21 | filed | no | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'FurtherSpecificReserve1ComponentTotalEquity'}` | 558166 | GBP | 2023-02-28 | 2024-11-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3305360 | GBP | 2023-02-28 | 2023-06-21 | filed | no | `ns6:Equity` | total-exemption-full |
| equity | 3863528 | GBP | 2023-02-28 | 2024-11-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| fixed_assets | 797873 | GBP | 2023-02-28 | 2023-06-21 | filed | no | `ns6:FixedAssets` | total-exemption-full |
| fixed_assets | 797873 | GBP | 2023-02-28 | 2024-11-28 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| net_assets | 3863528 | GBP | 2023-02-28 | 2024-11-28 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 3863528 | GBP | 2023-02-28 | 2023-06-21 | filed | no | `ns6:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 3183287 | GBP | 2023-02-28 | 2024-11-28 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 3183287 | GBP | 2023-02-28 | 2023-06-21 | filed | no | `ns6:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 405456 | GBP | 2023-02-28 | 2023-06-21 | filed | yes | `ns6:ProfitLoss` | total-exemption-full |
| profit_for_period | 405456 | GBP | 2023-02-28 | 2023-06-21 | filed | yes | `ns6:ProfitLoss` | total-exemption-full |
| total_assets_less_current_liabilities | 3981160 | GBP | 2023-02-28 | 2023-06-21 | filed | no | `ns6:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 3981160 | GBP | 2023-02-28 | 2024-11-28 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 13 | xbrli:pure | 2022-02-28 | 2023-06-21 | filed | yes | `ns6:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 2534390 | GBP | 2022-02-28 | 2023-06-21 | filed | yes | `ns6:CashBankOnHand` | total-exemption-full |
| current_assets | 3304442 | GBP | 2022-02-28 | 2023-06-21 | filed | yes | `ns6:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 770052 | GBP | 2022-02-28 | 2023-06-21 | filed | yes | `ns6:Debtors` | total-exemption-full |
| debtors | 770052 | GBP | 2022-02-28 | 2023-06-21 | filed | yes | `ns6:Debtors` | total-exemption-full |
| equity | 3593072 | GBP | 2022-02-28 | 2023-06-21 | filed | yes | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'FurtherSpecificReserve1ComponentTotalEquity'}` | 558166 | GBP | 2022-02-28 | 2023-06-21 | filed | yes | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3034904 | GBP | 2022-02-28 | 2023-06-21 | filed | yes | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2022-02-28 | 2023-06-21 | filed | yes | `ns6:Equity` | total-exemption-full |
| fixed_assets | 805497 | GBP | 2022-02-28 | 2023-06-21 | filed | yes | `ns6:FixedAssets` | total-exemption-full |
| net_assets | 3593072 | GBP | 2022-02-28 | 2023-06-21 | filed | yes | `ns6:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 3071070 | GBP | 2022-02-28 | 2023-06-21 | filed | yes | `ns6:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 3876567 | GBP | 2022-02-28 | 2023-06-21 | filed | yes | `ns6:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## INCA DATA SERVICES LIMITED (`gb:03216976`)

- registration: `03216976` (GB), status active, incorporated 1996-06-26
- classification: ['62020'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 78 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-09-30 | 2025-10-24 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 222974 | GBP | 2025-09-30 | 2025-10-24 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 222974 | GBP | 2025-09-30 | 2025-10-24 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 0 | GBP | 2025-09-30 | 2025-10-24 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 3 | GBP | 2025-09-30 | 2025-10-24 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 219753 | GBP | 2025-09-30 | 2025-10-24 | filed | yes | `frs-core:Equity` | total-exemption-full |
| net_assets | 219756 | GBP | 2025-09-30 | 2025-10-24 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 219756 | GBP | 2025-09-30 | 2025-10-24 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 219756 | GBP | 2025-09-30 | 2025-10-24 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-09-30 | 2025-09-04 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-09-30 | 2025-10-24 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 251513 | GBP | 2024-09-30 | 2025-10-24 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| cash | 251513 | GBP | 2024-09-30 | 2025-09-04 | filed | no | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 252003 | GBP | 2024-09-30 | 2025-10-24 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| current_assets | 252003 | GBP | 2024-09-30 | 2025-09-04 | filed | no | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 490 | GBP | 2024-09-30 | 2025-09-04 | filed | no | `frs-core:Debtors` | total-exemption-full |
| debtors | 490 | GBP | 2024-09-30 | 2025-10-24 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 3 | GBP | 2024-09-30 | 2025-10-24 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 262943 | GBP | 2024-09-30 | 2025-09-04 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 262943 | GBP | 2024-09-30 | 2025-10-24 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 3 | GBP | 2024-09-30 | 2025-09-04 | filed | no | `frs-core:Equity` | total-exemption-full |
| net_assets | 262946 | GBP | 2024-09-30 | 2025-10-24 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 262946 | GBP | 2024-09-30 | 2025-09-04 | filed | no | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 262946 | GBP | 2024-09-30 | 2025-09-04 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 262946 | GBP | 2024-09-30 | 2025-10-24 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 262946 | GBP | 2024-09-30 | 2025-09-04 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 262946 | GBP | 2024-09-30 | 2025-10-24 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-09-30 | 2024-06-20 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-09-30 | 2025-09-04 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 372362 | GBP | 2023-09-30 | 2025-09-04 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 373362 | GBP | 2023-09-30 | 2024-06-20 | filed | no | `ns5:CurrentAssets` | micro-entity |
| current_assets | 372800 | GBP | 2023-09-30 | 2025-09-04 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 438 | GBP | 2023-09-30 | 2025-09-04 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 334529 | GBP | 2023-09-30 | 2025-09-04 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 3 | GBP | 2023-09-30 | 2025-09-04 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity | 334532 | GBP | 2023-09-30 | 2024-06-20 | filed | yes | `ns5:Equity` | micro-entity |
| net_assets | 334532 | GBP | 2023-09-30 | 2025-09-04 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 334532 | GBP | 2023-09-30 | 2025-09-04 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 334532 | GBP | 2023-09-30 | 2024-06-20 | filed | no | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 334532 | GBP | 2023-09-30 | 2025-09-04 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 334532 | GBP | 2023-09-30 | 2024-06-20 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2022-09-30 | 2024-06-20 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 330203 | GBP | 2022-09-30 | 2024-06-20 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity | 293645 | GBP | 2022-09-30 | 2024-06-20 | filed | yes | `ns5:Equity` | micro-entity |
| net_current_assets | 293645 | GBP | 2022-09-30 | 2024-06-20 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 293645 | GBP | 2022-09-30 | 2024-06-20 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2025-09-04: `{"superseded_document_id": "gb:03216976:doc:23AW6hkCrm_iwSkLrcpOfZNJ9uUBZuWt1hhjgWQSbEI", "restatements": [{"concept": "current_assets", "period_end": "2023-09-30", "old_value": "373362.0000", "new_va`

## SYMPATEC LIMITED (`gb:03671355`)

- registration: `03671355` (GB), status active, incorporated 1998-11-20
- classification: ['71129'] (sic_2007)
- records: 7 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 81 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 7 | xbrli:pure | 2024-12-31 | 2025-09-23 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | small |
| cash | 1840332 | GBP | 2024-12-31 | 2025-09-23 | filed | yes | `core:CashBankOnHand` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1129918 | GBP | 2024-12-31 | 2025-09-23 | filed | yes | `core:Creditors` | small |
| current_assets | 2656915 | GBP | 2024-12-31 | 2025-09-23 | filed | yes | `core:CurrentAssets` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 364522 | GBP | 2024-12-31 | 2025-09-23 | filed | yes | `core:Debtors` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 364522 | GBP | 2024-12-31 | 2025-09-23 | filed | yes | `core:Debtors` | small |
| net_assets | 1594992 | GBP | 2024-12-31 | 2025-09-23 | filed | yes | `core:NetAssetsLiabilities` | small |
| net_current_assets | 1526997 | GBP | 2024-12-31 | 2025-09-23 | filed | yes | `core:NetCurrentAssetsLiabilities` | small |
| average_employees | 7 | xbrli:pure | 2023-12-31 | 2025-09-23 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | small |
| average_employees | 7 | xbrli:pure | 2023-12-31 | 2024-11-21 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | small |
| cash | 1676808 | GBP | 2023-12-31 | 2024-11-21 | filed | no | `core:CashBankOnHand` | small |
| cash | 1676808 | GBP | 2023-12-31 | 2025-09-23 | filed | yes | `core:CashBankOnHand` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 935449 | GBP | 2023-12-31 | 2025-09-23 | filed | yes | `core:Creditors` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 935449 | GBP | 2023-12-31 | 2024-11-21 | filed | no | `core:Creditors` | small |
| current_assets | 2467323 | GBP | 2023-12-31 | 2025-09-23 | filed | yes | `core:CurrentAssets` | small |
| current_assets | 2467323 | GBP | 2023-12-31 | 2024-11-21 | filed | no | `core:CurrentAssets` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 316377 | GBP | 2023-12-31 | 2024-11-21 | filed | no | `core:Debtors` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 316377 | GBP | 2023-12-31 | 2025-09-23 | filed | yes | `core:Debtors` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 316377 | GBP | 2023-12-31 | 2024-11-21 | filed | no | `core:Debtors` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 316377 | GBP | 2023-12-31 | 2025-09-23 | filed | yes | `core:Debtors` | small |
| net_assets | 1574918 | GBP | 2023-12-31 | 2024-11-21 | filed | no | `core:NetAssetsLiabilities` | small |
| net_assets | 1574918 | GBP | 2023-12-31 | 2025-09-23 | filed | yes | `core:NetAssetsLiabilities` | small |
| net_current_assets | 1531874 | GBP | 2023-12-31 | 2025-09-23 | filed | yes | `core:NetCurrentAssetsLiabilities` | small |
| net_current_assets | 1531874 | GBP | 2023-12-31 | 2024-11-21 | filed | no | `core:NetCurrentAssetsLiabilities` | small |
| average_employees | 5 | xbrli:pure | 2022-12-31 | 2024-11-21 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | small |
| average_employees | 5 | xbrli:pure | 2022-12-31 | 2023-09-29 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | small |
| cash | 1634116 | GBP | 2022-12-31 | 2023-09-29 | filed | no | `core:CashBankOnHand` | small |
| cash | 1634116 | GBP | 2022-12-31 | 2024-11-21 | filed | yes | `core:CashBankOnHand` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 997004 | GBP | 2022-12-31 | 2023-09-29 | filed | no | `core:Creditors` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 997004 | GBP | 2022-12-31 | 2024-11-21 | filed | yes | `core:Creditors` | small |
| current_assets | 2517187 | GBP | 2022-12-31 | 2023-09-29 | filed | no | `core:CurrentAssets` | small |
| current_assets | 2517187 | GBP | 2022-12-31 | 2024-11-21 | filed | yes | `core:CurrentAssets` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 533952 | GBP | 2022-12-31 | 2024-11-21 | filed | yes | `core:Debtors` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 533952 | GBP | 2022-12-31 | 2024-11-21 | filed | yes | `core:Debtors` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 533952 | GBP | 2022-12-31 | 2023-09-29 | filed | no | `core:Debtors` | small |
| net_assets | 1613287 | GBP | 2022-12-31 | 2024-11-21 | filed | yes | `core:NetAssetsLiabilities` | small |
| net_assets | 1613287 | GBP | 2022-12-31 | 2023-09-29 | filed | no | `core:NetAssetsLiabilities` | small |
| net_current_assets | 1520183 | GBP | 2022-12-31 | 2023-09-29 | filed | no | `core:NetCurrentAssetsLiabilities` | small |
| net_current_assets | 1520183 | GBP | 2022-12-31 | 2024-11-21 | filed | yes | `core:NetCurrentAssetsLiabilities` | small |
| average_employees | 8 | xbrli:pure | 2021-12-31 | 2023-09-29 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | small |
| cash | 1086932 | GBP | 2021-12-31 | 2023-09-29 | filed | yes | `core:CashBankOnHand` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 592589 | GBP | 2021-12-31 | 2023-09-29 | filed | yes | `core:Creditors` | small |
| current_assets | 1973441 | GBP | 2021-12-31 | 2023-09-29 | filed | yes | `core:CurrentAssets` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 482395 | GBP | 2021-12-31 | 2023-09-29 | filed | yes | `core:Debtors` | small |
| net_assets | 1467765 | GBP | 2021-12-31 | 2023-09-29 | filed | yes | `core:NetAssetsLiabilities` | small |
| net_current_assets | 1380852 | GBP | 2021-12-31 | 2023-09-29 | filed | yes | `core:NetCurrentAssetsLiabilities` | small |

_No coverage facts for the latest run._

## ASPEN STROMB CONSULTANCY LIMITED (`gb:04114026`)

- registration: `04114026` (GB), status active, incorporated 2000-11-24
- classification: ['62090', '78109'] (sic_2007)
- records: 5 officers, 1 beneficial owners, 0 ownership statements, 1 security interests, 72 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-12-31 | 2026-08-19 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 354182 | GBP | 2025-12-31 | 2026-08-19 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 2868446 | GBP | 2025-12-31 | 2026-08-19 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 2514264 | GBP | 2025-12-31 | 2026-08-19 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 2514264 | GBP | 2025-12-31 | 2026-08-19 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 1798125 | GBP | 2025-12-31 | 2026-08-19 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1798123 | GBP | 2025-12-31 | 2026-08-19 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2025-12-31 | 2026-08-19 | filed | yes | `ns5:Equity` | total-exemption-full |
| fixed_assets | 200472 | GBP | 2025-12-31 | 2026-08-19 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| net_assets | 1798125 | GBP | 2025-12-31 | 2026-08-19 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1597653 | GBP | 2025-12-31 | 2026-08-19 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1798125 | GBP | 2025-12-31 | 2026-08-19 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-12-31 | 2025-09-12 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-12-31 | 2026-08-19 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 530703 | GBP | 2024-12-31 | 2026-08-19 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 530703 | GBP | 2024-12-31 | 2025-09-12 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 1906351 | GBP | 2024-12-31 | 2026-08-19 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 1906351 | GBP | 2024-12-31 | 2025-09-12 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 1375648 | GBP | 2024-12-31 | 2025-09-12 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 1375648 | GBP | 2024-12-31 | 2025-09-12 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 1375648 | GBP | 2024-12-31 | 2026-08-19 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 1375648 | GBP | 2024-12-31 | 2026-08-19 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 1545827 | GBP | 2024-12-31 | 2026-08-19 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 1545827 | GBP | 2024-12-31 | 2025-09-12 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-12-31 | 2025-09-12 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1545825 | GBP | 2024-12-31 | 2026-08-19 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-12-31 | 2026-08-19 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1545825 | GBP | 2024-12-31 | 2025-09-12 | filed | no | `ns5:Equity` | total-exemption-full |
| fixed_assets | 200951 | GBP | 2024-12-31 | 2026-08-19 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| fixed_assets | 200951 | GBP | 2024-12-31 | 2025-09-12 | filed | no | `ns5:FixedAssets` | total-exemption-full |
| net_assets | 1545827 | GBP | 2024-12-31 | 2025-09-12 | filed | no | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 1545827 | GBP | 2024-12-31 | 2026-08-19 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1349043 | GBP | 2024-12-31 | 2025-09-12 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1349043 | GBP | 2024-12-31 | 2026-08-19 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1549994 | GBP | 2024-12-31 | 2026-08-19 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1549994 | GBP | 2024-12-31 | 2025-09-12 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-12-31 | 2024-08-27 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-12-31 | 2025-09-12 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 1757342 | GBP | 2023-12-31 | 2024-08-27 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 1757342 | GBP | 2023-12-31 | 2025-09-12 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 2030977 | GBP | 2023-12-31 | 2025-09-12 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 2030977 | GBP | 2023-12-31 | 2024-08-27 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 273635 | GBP | 2023-12-31 | 2024-08-27 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 273635 | GBP | 2023-12-31 | 2024-08-27 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 273635 | GBP | 2023-12-31 | 2025-09-12 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 273635 | GBP | 2023-12-31 | 2025-09-12 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 1437073 | GBP | 2023-12-31 | 2025-09-12 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1437071 | GBP | 2023-12-31 | 2025-09-12 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-12-31 | 2025-09-12 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 1437073 | GBP | 2023-12-31 | 2024-08-27 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-12-31 | 2024-08-27 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1437071 | GBP | 2023-12-31 | 2024-08-27 | filed | no | `ns5:Equity` | total-exemption-full |
| fixed_assets | 1 | GBP | 2023-12-31 | 2025-09-12 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| net_assets | 1437073 | GBP | 2023-12-31 | 2025-09-12 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 1437073 | GBP | 2023-12-31 | 2024-08-27 | filed | no | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1451239 | GBP | 2023-12-31 | 2024-08-27 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1451239 | GBP | 2023-12-31 | 2025-09-12 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1451240 | GBP | 2023-12-31 | 2025-09-12 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1451240 | GBP | 2023-12-31 | 2024-08-27 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2022-12-31 | 2024-08-27 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 426449 | GBP | 2022-12-31 | 2024-08-27 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 2154145 | GBP | 2022-12-31 | 2024-08-27 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1727696 | GBP | 2022-12-31 | 2024-08-27 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 1727696 | GBP | 2022-12-31 | 2024-08-27 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1316301 | GBP | 2022-12-31 | 2024-08-27 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 1316303 | GBP | 2022-12-31 | 2024-08-27 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2022-12-31 | 2024-08-27 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 1316303 | GBP | 2022-12-31 | 2024-08-27 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1340469 | GBP | 2022-12-31 | 2024-08-27 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1340470 | GBP | 2022-12-31 | 2024-08-27 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## AOXOMOXOA LIMITED (`gb:04565402`)

- registration: `04565402` (GB), status active, incorporated 2002-10-17
- classification: ['62020'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 56 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-10-31 | 2026-07-28 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 380 | GBP | 2025-10-31 | 2026-07-28 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| equity | -67082 | GBP | 2025-10-31 | 2026-07-28 | filed | yes | `frs-core:Equity` | micro-entity |
| fixed_assets | 1407 | GBP | 2025-10-31 | 2026-07-28 | filed | yes | `frs-core:FixedAssets` | micro-entity |
| net_assets | -67082 | GBP | 2025-10-31 | 2026-07-28 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -67739 | GBP | 2025-10-31 | 2026-07-28 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -66332 | GBP | 2025-10-31 | 2026-07-28 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-10-31 | 2025-07-02 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-10-31 | 2026-07-28 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 380 | GBP | 2024-10-31 | 2026-07-28 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| current_assets | 380 | GBP | 2024-10-31 | 2025-07-02 | filed | no | `frs-core:CurrentAssets` | micro-entity |
| equity | -67082 | GBP | 2024-10-31 | 2025-07-02 | filed | no | `frs-core:Equity` | micro-entity |
| equity | -67082 | GBP | 2024-10-31 | 2026-07-28 | filed | yes | `frs-core:Equity` | micro-entity |
| fixed_assets | 1407 | GBP | 2024-10-31 | 2026-07-28 | filed | yes | `frs-core:FixedAssets` | micro-entity |
| fixed_assets | 1407 | GBP | 2024-10-31 | 2025-07-02 | filed | no | `frs-core:FixedAssets` | micro-entity |
| net_assets | -67082 | GBP | 2024-10-31 | 2025-07-02 | filed | no | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_assets | -67082 | GBP | 2024-10-31 | 2026-07-28 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -67739 | GBP | 2024-10-31 | 2026-07-28 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -67739 | GBP | 2024-10-31 | 2025-07-02 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -66332 | GBP | 2024-10-31 | 2025-07-02 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -66332 | GBP | 2024-10-31 | 2026-07-28 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-10-31 | 2024-06-26 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-10-31 | 2025-07-02 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 380 | GBP | 2023-10-31 | 2025-07-02 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| current_assets | 380 | GBP | 2023-10-31 | 2024-06-26 | filed | no | `frs-core:CurrentAssets` | micro-entity |
| equity | -67082 | GBP | 2023-10-31 | 2025-07-02 | filed | yes | `frs-core:Equity` | micro-entity |
| equity | -67082 | GBP | 2023-10-31 | 2024-06-26 | filed | no | `frs-core:Equity` | micro-entity |
| fixed_assets | 1407 | GBP | 2023-10-31 | 2024-06-26 | filed | no | `frs-core:FixedAssets` | micro-entity |
| fixed_assets | 1407 | GBP | 2023-10-31 | 2025-07-02 | filed | yes | `frs-core:FixedAssets` | micro-entity |
| net_assets | -67082 | GBP | 2023-10-31 | 2024-06-26 | filed | no | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_assets | -67082 | GBP | 2023-10-31 | 2025-07-02 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -67739 | GBP | 2023-10-31 | 2024-06-26 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -67739 | GBP | 2023-10-31 | 2025-07-02 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -66332 | GBP | 2023-10-31 | 2024-06-26 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -66332 | GBP | 2023-10-31 | 2025-07-02 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2022-10-31 | 2024-06-26 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 2809 | GBP | 2022-10-31 | 2024-06-26 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| equity | -60153 | GBP | 2022-10-31 | 2024-06-26 | filed | yes | `frs-core:Equity` | micro-entity |
| fixed_assets | 5150 | GBP | 2022-10-31 | 2024-06-26 | filed | yes | `frs-core:FixedAssets` | micro-entity |
| net_assets | -60153 | GBP | 2022-10-31 | 2024-06-26 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -63793 | GBP | 2022-10-31 | 2024-06-26 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -58643 | GBP | 2022-10-31 | 2024-06-26 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## AMIGO SOFTWARE LTD (`gb:05032613`)

- registration: `05032613` (GB), status active, incorporated 2004-02-03
- classification: ['62090'] (sic_2007)
- records: 5 officers, 5 beneficial owners, 0 ownership statements, 0 security interests, 69 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | iso4217:GBP | 2025-02-28 | 2026-07-10 | filed | yes | `pt:AverageNumberEmployeesDuringPeriod` | micro-entity |
| net_assets | 14395 | GBP | 2025-02-28 | 2026-07-10 | filed | yes | `pt:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 13857 | GBP | 2025-02-28 | 2026-07-10 | filed | yes | `pt:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 14395 | GBP | 2025-02-28 | 2026-07-10 | filed | yes | `pt:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-02-28 | 2025-02-28 | filed | yes | `pt:AverageNumberEmployeesDuringPeriod` | micro-entity |
| net_assets | 146182 | GBP | 2024-02-28 | 2025-02-28 | filed | no | `pt:NetAssetsLiabilities` | micro-entity |
| net_assets | 146182 | GBP | 2024-02-28 | 2026-07-10 | filed | yes | `pt:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 145549 | GBP | 2024-02-28 | 2025-02-28 | filed | yes | `pt:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 146182 | GBP | 2024-02-28 | 2025-02-28 | filed | no | `pt:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 146182 | GBP | 2024-02-28 | 2026-07-10 | filed | yes | `pt:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-02-28 | 2024-02-27 | filed | yes | `pt:AverageNumberEmployeesDuringPeriod` | micro-entity |
| net_assets | 242915 | GBP | 2023-02-28 | 2025-02-28 | filed | yes | `pt:NetAssetsLiabilities` | micro-entity |
| net_assets | 242915 | GBP | 2023-02-28 | 2024-02-27 | filed | no | `pt:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 242170 | GBP | 2023-02-28 | 2024-02-27 | filed | yes | `pt:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 242915 | GBP | 2023-02-28 | 2024-02-27 | filed | no | `pt:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 242915 | GBP | 2023-02-28 | 2025-02-28 | filed | yes | `pt:TotalAssetsLessCurrentLiabilities` | micro-entity |
| net_assets | 39412 | GBP | 2022-02-28 | 2024-02-27 | filed | yes | `pt:NetAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 39412 | GBP | 2022-02-28 | 2024-02-27 | filed | yes | `pt:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## FINA SYSTEMS LTD. (`gb:05471543`)

- registration: `05471543` (GB), status active, incorporated 2005-06-03
- classification: ['62020'] (sic_2007)
- records: 5 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 77 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2026-03-31 | 2026-08-28 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 34702 | GBP | 2026-03-31 | 2026-08-28 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 40318 | GBP | 2026-03-31 | 2026-08-28 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 5616 | GBP | 2026-03-31 | 2026-08-28 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 5616 | GBP | 2026-03-31 | 2026-08-28 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 13878 | GBP | 2026-03-31 | 2026-08-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 101 | GBP | 2026-03-31 | 2026-08-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 13979 | GBP | 2026-03-31 | 2026-08-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 13979 | GBP | 2026-03-31 | 2026-08-28 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 7093 | GBP | 2026-03-31 | 2026-08-28 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 39534 | GBP | 2026-03-31 | 2026-08-28 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2025-03-31 | 2026-08-28 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2025-03-31 | 2025-10-07 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 19589 | GBP | 2025-03-31 | 2026-08-28 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 19589 | GBP | 2025-03-31 | 2025-10-07 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 45275 | GBP | 2025-03-31 | 2026-08-28 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 45275 | GBP | 2025-03-31 | 2025-10-07 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 25686 | GBP | 2025-03-31 | 2025-10-07 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 25686 | GBP | 2025-03-31 | 2026-08-28 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 7470 | GBP | 2025-03-31 | 2026-08-28 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 5117 | GBP | 2025-03-31 | 2025-10-07 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 5016 | GBP | 2025-03-31 | 2025-10-07 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 101 | GBP | 2025-03-31 | 2025-10-07 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 5117 | GBP | 2025-03-31 | 2026-08-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 101 | GBP | 2025-03-31 | 2026-08-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 5016 | GBP | 2025-03-31 | 2026-08-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 5117 | GBP | 2025-03-31 | 2026-08-28 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 3138 | GBP | 2025-03-31 | 2025-10-07 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 3138 | GBP | 2025-03-31 | 2026-08-28 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 5117 | GBP | 2025-03-31 | 2026-08-28 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 5117 | GBP | 2025-03-31 | 2025-10-07 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-03-31 | 2025-10-07 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-03-31 | 2024-12-23 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 15717 | GBP | 2024-03-31 | 2025-10-07 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 15717 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 37617 | GBP | 2024-03-31 | 2024-12-23 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 73381 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 73380 | GBP | 2024-03-31 | 2025-10-07 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 57664 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 57663 | GBP | 2024-03-31 | 2025-10-07 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 57664 | GBP | 2024-03-31 | 2024-12-23 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-03-31 | 2025-10-07 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 38041 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:Equity` | total-exemption-full |
| equity | 38141 | GBP | 2024-03-31 | 2025-10-07 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 38041 | GBP | 2024-03-31 | 2025-10-07 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 38141 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:Equity` | total-exemption-full |
| net_current_assets | 35764 | GBP | 2024-03-31 | 2025-10-07 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 35764 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 38141 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 38141 | GBP | 2024-03-31 | 2025-10-07 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-03-31 | 2024-12-23 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 22409 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 30675 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 91311 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 68902 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 68902 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 63231 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 63131 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:Equity` | total-exemption-full |
| net_current_assets | 60636 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 63231 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2025-10-07: `{"superseded_document_id": "gb:05471543:doc:hrKp4M7zV3quWW8PpTLmeXbVSP5iF80zVK1sbkjIyHA", "restatements": [{"concept": "debtors", "period_end": "2024-03-31", "old_value": "57664.0000", "new_value": "5`

## FUSION ELECTRICAL ENGINEERING SERVICES LIMITED (`gb:05913575`)

- registration: `05913575` (GB), status active, incorporated 2006-08-22
- classification: ['43210', '71122', '71129'] (sic_2007)
- records: 2 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 46 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-10-31 | 2026-07-27 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 4524 | GBP | 2025-10-31 | 2026-07-27 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| equity | 1659 | GBP | 2025-10-31 | 2026-07-27 | filed | yes | `frs-core:Equity` | micro-entity |
| fixed_assets | 213 | GBP | 2025-10-31 | 2026-07-27 | filed | yes | `frs-core:FixedAssets` | micro-entity |
| net_assets | 1659 | GBP | 2025-10-31 | 2026-07-27 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 2220 | GBP | 2025-10-31 | 2026-07-27 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 2433 | GBP | 2025-10-31 | 2026-07-27 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-10-31 | 2025-07-29 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-10-31 | 2026-07-27 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 11609 | GBP | 2024-10-31 | 2025-07-29 | filed | no | `frs-core:CurrentAssets` | micro-entity |
| current_assets | 11609 | GBP | 2024-10-31 | 2026-07-27 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| equity | 2935 | GBP | 2024-10-31 | 2025-07-29 | filed | no | `frs-core:Equity` | micro-entity |
| equity | 2935 | GBP | 2024-10-31 | 2026-07-27 | filed | yes | `frs-core:Equity` | micro-entity |
| fixed_assets | 251 | GBP | 2024-10-31 | 2026-07-27 | filed | yes | `frs-core:FixedAssets` | micro-entity |
| fixed_assets | 251 | GBP | 2024-10-31 | 2025-07-29 | filed | no | `frs-core:FixedAssets` | micro-entity |
| net_assets | 2935 | GBP | 2024-10-31 | 2025-07-29 | filed | no | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 2935 | GBP | 2024-10-31 | 2026-07-27 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 3416 | GBP | 2024-10-31 | 2026-07-27 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 3416 | GBP | 2024-10-31 | 2025-07-29 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 3667 | GBP | 2024-10-31 | 2025-07-29 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 3667 | GBP | 2024-10-31 | 2026-07-27 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-10-31 | 2025-07-29 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-10-31 | 2024-08-01 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 5692 | GBP | 2023-10-31 | 2024-08-01 | filed | no | `frs-core:CurrentAssets` | micro-entity |
| current_assets | 5692 | GBP | 2023-10-31 | 2025-07-29 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| equity | 736 | GBP | 2023-10-31 | 2025-07-29 | filed | yes | `frs-core:Equity` | micro-entity |
| equity | 736 | GBP | 2023-10-31 | 2024-08-01 | filed | no | `frs-core:Equity` | micro-entity |
| fixed_assets | 295 | GBP | 2023-10-31 | 2024-08-01 | filed | no | `frs-core:FixedAssets` | micro-entity |
| fixed_assets | 295 | GBP | 2023-10-31 | 2025-07-29 | filed | yes | `frs-core:FixedAssets` | micro-entity |
| net_assets | 736 | GBP | 2023-10-31 | 2024-08-01 | filed | no | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 736 | GBP | 2023-10-31 | 2025-07-29 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 1137 | GBP | 2023-10-31 | 2024-08-01 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 1137 | GBP | 2023-10-31 | 2025-07-29 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 1432 | GBP | 2023-10-31 | 2025-07-29 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 1432 | GBP | 2023-10-31 | 2024-08-01 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2022-10-31 | 2024-08-01 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 3735 | GBP | 2022-10-31 | 2024-08-01 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| equity | 616 | GBP | 2022-10-31 | 2024-08-01 | filed | yes | `frs-core:Equity` | micro-entity |
| fixed_assets | 347 | GBP | 2022-10-31 | 2024-08-01 | filed | yes | `frs-core:FixedAssets` | micro-entity |
| net_assets | 616 | GBP | 2022-10-31 | 2024-08-01 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 905 | GBP | 2022-10-31 | 2024-08-01 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 1252 | GBP | 2022-10-31 | 2024-08-01 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## TOUCH SCREEN DEVELOPERS LIMITED (`gb:06389765`)

- registration: `06389765` (GB), status active, incorporated 2007-10-04
- classification: ['62012'] (sic_2007)
- records: 2 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 41 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-10-31 | 2026-03-20 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 1923 | GBP | 2025-10-31 | 2026-03-20 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 6957 | GBP | 2025-10-31 | 2026-03-20 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 5034 | GBP | 2025-10-31 | 2026-03-20 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 5034 | GBP | 2025-10-31 | 2026-03-20 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 252 | GBP | 2025-10-31 | 2026-03-20 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 152 | GBP | 2025-10-31 | 2026-03-20 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-10-31 | 2026-03-20 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 252 | GBP | 2025-10-31 | 2026-03-20 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -656 | GBP | 2025-10-31 | 2026-03-20 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 465 | GBP | 2025-10-31 | 2026-03-20 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-10-31 | 2026-03-20 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-10-31 | 2025-01-28 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 6036 | GBP | 2024-10-31 | 2025-01-28 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 6036 | GBP | 2024-10-31 | 2026-03-20 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 8669 | GBP | 2024-10-31 | 2025-01-28 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 8669 | GBP | 2024-10-31 | 2026-03-20 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 2633 | GBP | 2024-10-31 | 2025-01-28 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 2633 | GBP | 2024-10-31 | 2025-01-28 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 2633 | GBP | 2024-10-31 | 2026-03-20 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 2633 | GBP | 2024-10-31 | 2026-03-20 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 382 | GBP | 2024-10-31 | 2026-03-20 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 282 | GBP | 2024-10-31 | 2026-03-20 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-10-31 | 2025-01-28 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 382 | GBP | 2024-10-31 | 2025-01-28 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 282 | GBP | 2024-10-31 | 2025-01-28 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-10-31 | 2026-03-20 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 382 | GBP | 2024-10-31 | 2026-03-20 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 382 | GBP | 2024-10-31 | 2025-01-28 | filed | no | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -686 | GBP | 2024-10-31 | 2026-03-20 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -686 | GBP | 2024-10-31 | 2025-01-28 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 633 | GBP | 2024-10-31 | 2025-01-28 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 633 | GBP | 2024-10-31 | 2026-03-20 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-10-31 | 2025-01-28 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 1 | xbrli:pure | 2023-10-31 | 2024-02-20 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 6859 | GBP | 2023-10-31 | 2025-01-28 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 6859 | GBP | 2023-10-31 | 2024-02-20 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 11029 | GBP | 2023-10-31 | 2025-01-28 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 11029 | GBP | 2023-10-31 | 2024-02-20 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original'}` | 4170 | GBP | 2023-10-31 | 2024-02-20 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 4170 | GBP | 2023-10-31 | 2024-02-20 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 4170 | GBP | 2023-10-31 | 2025-01-28 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 4170 | GBP | 2023-10-31 | 2025-01-28 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 6972 | GBP | 2023-10-31 | 2025-01-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 100 | GBP | 2023-10-31 | 2024-02-20 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 6872 | GBP | 2023-10-31 | 2025-01-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 6872 | GBP | 2023-10-31 | 2024-02-20 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 6972 | GBP | 2023-10-31 | 2024-02-20 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-10-31 | 2025-01-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets `{'OriginalRevisedDataDimension': 'Original'}` | 6972 | GBP | 2023-10-31 | 2024-02-20 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 6972 | GBP | 2023-10-31 | 2025-01-28 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 6507 | GBP | 2023-10-31 | 2025-01-28 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 6507 | GBP | 2023-10-31 | 2024-02-20 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 7081 | GBP | 2023-10-31 | 2025-01-28 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 7081 | GBP | 2023-10-31 | 2024-02-20 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 1 | xbrli:pure | 2022-10-31 | 2024-02-20 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 5119 | GBP | 2022-10-31 | 2024-02-20 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 15902 | GBP | 2022-10-31 | 2024-02-20 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original'}` | 10783 | GBP | 2022-10-31 | 2024-02-20 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 10783 | GBP | 2022-10-31 | 2024-02-20 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 100 | GBP | 2022-10-31 | 2024-02-20 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 10672 | GBP | 2022-10-31 | 2024-02-20 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 10772 | GBP | 2022-10-31 | 2024-02-20 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets `{'OriginalRevisedDataDimension': 'Original'}` | 10772 | GBP | 2022-10-31 | 2024-02-20 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 10224 | GBP | 2022-10-31 | 2024-02-20 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 10900 | GBP | 2022-10-31 | 2024-02-20 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._
