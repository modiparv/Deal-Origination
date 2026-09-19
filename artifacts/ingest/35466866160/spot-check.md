# Ingest spot-check

- database: `data/engine.db`
- latest run: `20260919T201635Z-69c2aa4a`
- companies in store: 7400; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## MICROSEC LIMITED (`gb:01462783`)

- registration: `01462783` (GB), status active, incorporated 1979-11-23
- classification: ['62012', '62020', '62090'] (sic_2007)
- records: 5 officers, 3 beneficial owners, 0 ownership statements, 2 security interests, 113 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 4 | xbrli:pure | 2025-03-31 | 2025-12-18 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 293989 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 608365 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 314376 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 314376 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 451758 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 49 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 1703 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 453611 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 101 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `ns5:Equity` | total-exemption-full |
| fixed_assets | 99065 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| net_assets | 453611 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 409237 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 508302 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 3 | xbrli:pure | 2024-03-31 | 2025-12-18 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 3 | xbrli:pure | 2024-03-31 | 2024-12-20 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 276263 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 276263 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 515770 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 515770 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 239507 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 239507 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 239507 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 239507 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 49 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 334369 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 101 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 1703 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 101 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 1703 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 334369 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 332516 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 332516 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 49 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `ns5:Equity` | total-exemption-full |
| fixed_assets | 25423 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| fixed_assets | 25423 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `ns5:FixedAssets` | total-exemption-full |
| net_assets | 334369 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 334369 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 325214 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 325214 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 350637 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 350637 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 3 | xbrli:pure | 2023-03-31 | 2023-12-22 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 3 | xbrli:pure | 2023-03-31 | 2024-12-20 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 60490 | GBP | 2023-03-31 | 2023-12-22 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 60490 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 154353 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 154353 | GBP | 2023-03-31 | 2023-12-22 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 93863 | GBP | 2023-03-31 | 2023-12-22 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 93863 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original'}` | 93863 | GBP | 2023-03-31 | 2023-12-22 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 93863 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 65931 | GBP | 2023-03-31 | 2023-12-22 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 101 | GBP | 2023-03-31 | 2023-12-22 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 65931 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 49 | GBP | 2023-03-31 | 2023-12-22 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'SharePremium'}` | 1703 | GBP | 2023-03-31 | 2023-12-22 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 49 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 1703 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 67784 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 101 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 67784 | GBP | 2023-03-31 | 2023-12-22 | filed | yes | `ns5:Equity` | total-exemption-full |
| fixed_assets `{'OriginalRevisedDataDimension': 'Original'}` | 35269 | GBP | 2023-03-31 | 2023-12-22 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| fixed_assets | 35269 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| net_assets `{'OriginalRevisedDataDimension': 'Original'}` | 67784 | GBP | 2023-03-31 | 2023-12-22 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 67784 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 57683 | GBP | 2023-03-31 | 2023-12-22 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 57683 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 92952 | GBP | 2023-03-31 | 2023-12-22 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 92952 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 5 | xbrli:pure | 2022-03-31 | 2023-12-22 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 84096 | GBP | 2022-03-31 | 2023-12-22 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 416885 | GBP | 2022-03-31 | 2023-12-22 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original'}` | 332789 | GBP | 2022-03-31 | 2023-12-22 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 332789 | GBP | 2022-03-31 | 2023-12-22 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 293916 | GBP | 2022-03-31 | 2023-12-22 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'SharePremium'}` | 1703 | GBP | 2022-03-31 | 2023-12-22 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 101 | GBP | 2022-03-31 | 2023-12-22 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 295769 | GBP | 2022-03-31 | 2023-12-22 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 49 | GBP | 2022-03-31 | 2023-12-22 | filed | yes | `ns5:Equity` | total-exemption-full |
| fixed_assets `{'OriginalRevisedDataDimension': 'Original'}` | 46908 | GBP | 2022-03-31 | 2023-12-22 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| net_assets `{'OriginalRevisedDataDimension': 'Original'}` | 295769 | GBP | 2022-03-31 | 2023-12-22 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 284340 | GBP | 2022-03-31 | 2023-12-22 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 331248 | GBP | 2022-03-31 | 2023-12-22 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## NOLANHEATH LIMITED (`gb:01857757`)

- registration: `01857757` (GB), status active, incorporated 1984-10-23
- classification: ['62020'] (sic_2007)
- records: 3 officers, 1 beneficial owners, 0 ownership statements, 1 security interests, 92 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-10-31 | 2026-04-01 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 115745 | GBP | 2025-10-31 | 2026-04-01 | filed | yes | `ns5:CashBankOnHand` | unaudited-abridged |
| equity | 570572 | GBP | 2025-10-31 | 2026-04-01 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-10-31 | 2026-04-01 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 165439 | GBP | 2025-10-31 | 2026-04-01 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'FurtherSpecificReserve3ComponentTotalEquity'}` | 405033 | GBP | 2025-10-31 | 2026-04-01 | filed | yes | `ns5:Equity` | unaudited-abridged |
| fixed_assets | 896000 | GBP | 2025-10-31 | 2026-04-01 | filed | yes | `ns5:FixedAssets` | unaudited-abridged |
| net_assets | 570572 | GBP | 2025-10-31 | 2026-04-01 | filed | yes | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | -229119 | GBP | 2025-10-31 | 2026-04-01 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 666881 | GBP | 2025-10-31 | 2026-04-01 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 1 | xbrli:pure | 2024-10-31 | 2025-04-12 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| average_employees | 1 | xbrli:pure | 2024-10-31 | 2026-04-01 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 128536 | GBP | 2024-10-31 | 2025-04-12 | filed | no | `ns5:CashBankOnHand` | unaudited-abridged |
| cash | 128536 | GBP | 2024-10-31 | 2026-04-01 | filed | yes | `ns5:CashBankOnHand` | unaudited-abridged |
| current_assets | 128536 | GBP | 2024-10-31 | 2025-04-12 | filed | yes | `ns5:CurrentAssets` | unaudited-abridged |
| debtors | 0 | GBP | 2024-10-31 | 2025-04-12 | filed | yes | `ns5:Debtors` | unaudited-abridged |
| equity | 570191 | GBP | 2024-10-31 | 2025-04-12 | filed | no | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'FurtherSpecificReserve3ComponentTotalEquity'}` | 392463 | GBP | 2024-10-31 | 2026-04-01 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity | 570191 | GBP | 2024-10-31 | 2026-04-01 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 177628 | GBP | 2024-10-31 | 2025-04-12 | filed | no | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'FurtherSpecificReserve3ComponentTotalEquity'}` | 392463 | GBP | 2024-10-31 | 2025-04-12 | filed | no | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-10-31 | 2025-04-12 | filed | no | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 177628 | GBP | 2024-10-31 | 2026-04-01 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-10-31 | 2026-04-01 | filed | yes | `ns5:Equity` | unaudited-abridged |
| fixed_assets | 873000 | GBP | 2024-10-31 | 2025-04-12 | filed | no | `ns5:FixedAssets` | unaudited-abridged |
| fixed_assets | 873000 | GBP | 2024-10-31 | 2026-04-01 | filed | yes | `ns5:FixedAssets` | unaudited-abridged |
| net_assets | 570191 | GBP | 2024-10-31 | 2026-04-01 | filed | yes | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_assets | 570191 | GBP | 2024-10-31 | 2025-04-12 | filed | no | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | -210750 | GBP | 2024-10-31 | 2025-04-12 | filed | no | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| net_current_assets | -210750 | GBP | 2024-10-31 | 2026-04-01 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 662250 | GBP | 2024-10-31 | 2025-04-12 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 662250 | GBP | 2024-10-31 | 2026-04-01 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 1 | xbrli:pure | 2023-10-31 | 2025-04-12 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| average_employees | 1 | xbrli:pure | 2023-10-31 | 2024-05-08 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 132679 | GBP | 2023-10-31 | 2024-05-08 | filed | no | `ns5:CashBankOnHand` | unaudited-abridged |
| cash | 132679 | GBP | 2023-10-31 | 2025-04-12 | filed | yes | `ns5:CashBankOnHand` | unaudited-abridged |
| current_assets | 140101 | GBP | 2023-10-31 | 2025-04-12 | filed | yes | `ns5:CurrentAssets` | unaudited-abridged |
| current_assets | 140101 | GBP | 2023-10-31 | 2024-05-08 | filed | no | `ns5:CurrentAssets` | unaudited-abridged |
| debtors | 7422 | GBP | 2023-10-31 | 2024-05-08 | filed | no | `ns5:Debtors` | unaudited-abridged |
| debtors | 7422 | GBP | 2023-10-31 | 2025-04-12 | filed | yes | `ns5:Debtors` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 172942 | GBP | 2023-10-31 | 2024-05-08 | filed | no | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 172942 | GBP | 2023-10-31 | 2025-04-12 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity | 537965 | GBP | 2023-10-31 | 2025-04-12 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-10-31 | 2024-05-08 | filed | no | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'FurtherSpecificReserve3ComponentTotalEquity'}` | 364923 | GBP | 2023-10-31 | 2025-04-12 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'FurtherSpecificReserve3ComponentTotalEquity'}` | 364923 | GBP | 2023-10-31 | 2024-05-08 | filed | no | `ns5:Equity` | unaudited-abridged |
| equity | 537965 | GBP | 2023-10-31 | 2024-05-08 | filed | no | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-10-31 | 2025-04-12 | filed | yes | `ns5:Equity` | unaudited-abridged |
| fixed_assets | 839000 | GBP | 2023-10-31 | 2025-04-12 | filed | yes | `ns5:FixedAssets` | unaudited-abridged |
| fixed_assets | 839000 | GBP | 2023-10-31 | 2024-05-08 | filed | no | `ns5:FixedAssets` | unaudited-abridged |
| net_assets | 537965 | GBP | 2023-10-31 | 2024-05-08 | filed | no | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_assets | 537965 | GBP | 2023-10-31 | 2025-04-12 | filed | yes | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | -215436 | GBP | 2023-10-31 | 2025-04-12 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| net_current_assets | -215436 | GBP | 2023-10-31 | 2024-05-08 | filed | no | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 623564 | GBP | 2023-10-31 | 2025-04-12 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 623564 | GBP | 2023-10-31 | 2024-05-08 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 1 | xbrli:pure | 2022-10-31 | 2024-05-08 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 92130 | GBP | 2022-10-31 | 2024-05-08 | filed | yes | `ns5:CashBankOnHand` | unaudited-abridged |
| current_assets | 92507 | GBP | 2022-10-31 | 2024-05-08 | filed | yes | `ns5:CurrentAssets` | unaudited-abridged |
| debtors | 377 | GBP | 2022-10-31 | 2024-05-08 | filed | yes | `ns5:Debtors` | unaudited-abridged |
| equity | 455902 | GBP | 2022-10-31 | 2024-05-08 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 143529 | GBP | 2022-10-31 | 2024-05-08 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'FurtherSpecificReserve3ComponentTotalEquity'}` | 312273 | GBP | 2022-10-31 | 2024-05-08 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2022-10-31 | 2024-05-08 | filed | yes | `ns5:Equity` | unaudited-abridged |
| fixed_assets | 774000 | GBP | 2022-10-31 | 2024-05-08 | filed | yes | `ns5:FixedAssets` | unaudited-abridged |
| net_assets | 455902 | GBP | 2022-10-31 | 2024-05-08 | filed | yes | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | -244849 | GBP | 2022-10-31 | 2024-05-08 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 529151 | GBP | 2022-10-31 | 2024-05-08 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |

_No coverage facts for the latest run._

## CAMBRIDGE DATABASE TECHNOLOGIES LIMITED (`gb:02118916`)

- registration: `02118916` (GB), status active, incorporated 1987-04-02
- classification: ['62012'] (sic_2007)
- records: 3 officers, 1 beneficial owners, 0 ownership statements, 1 security interests, 101 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | iso4217:GBP | 2025-05-31 | 2026-02-26 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 11311 | GBP | 2025-05-31 | 2026-02-26 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 59690 | GBP | 2025-05-31 | 2026-02-26 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 51298 | GBP | 2025-05-31 | 2026-02-26 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 2919 | GBP | 2025-05-31 | 2026-02-26 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 51298 | GBP | 2025-05-31 | 2026-02-26 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 48379 | GBP | 2025-05-31 | 2026-02-26 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| profit_for_period | 48019 | GBP | 2025-05-31 | 2026-02-26 | filed | yes | `core:ProfitLoss` | micro-entity |
| revenue | 94866 | GBP | 2025-05-31 | 2026-02-26 | filed | yes | `core:TurnoverRevenue` | micro-entity |
| staff_costs | 25140 | GBP | 2025-05-31 | 2026-02-26 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | micro-entity |
| tax_charge | 11311 | GBP | 2025-05-31 | 2026-02-26 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | micro-entity |
| total_assets_less_current_liabilities | 51298 | GBP | 2025-05-31 | 2026-02-26 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2024-05-31 | 2025-02-26 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2024-05-31 | 2025-02-26 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 7221 | GBP | 2024-05-31 | 2026-02-26 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 7221 | GBP | 2024-05-31 | 2025-02-26 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 7375 | GBP | 2024-05-31 | 2025-02-26 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 7375 | GBP | 2024-05-31 | 2026-02-26 | filed | yes | `core:CurrentAssets` | micro-entity |
| depreciation_amortisation | 0 | GBP | 2024-05-31 | 2025-02-26 | filed | yes | `core:DepreciationAmortisationImpairmentExpense` | micro-entity |
| equity | 3073 | GBP | 2024-05-31 | 2026-02-26 | filed | yes | `core:Equity` | micro-entity |
| equity | 3073 | GBP | 2024-05-31 | 2025-02-26 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 2919 | GBP | 2024-05-31 | 2026-02-26 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 2919 | GBP | 2024-05-31 | 2025-02-26 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | 3073 | GBP | 2024-05-31 | 2025-02-26 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 3073 | GBP | 2024-05-31 | 2026-02-26 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 154 | GBP | 2024-05-31 | 2025-02-26 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 154 | GBP | 2024-05-31 | 2026-02-26 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| profit_for_period | 30788 | GBP | 2024-05-31 | 2025-02-26 | filed | no | `core:ProfitLoss` | micro-entity |
| profit_for_period | 30788 | GBP | 2024-05-31 | 2026-02-26 | filed | yes | `core:ProfitLoss` | micro-entity |
| revenue | 73339 | GBP | 2024-05-31 | 2025-02-26 | filed | no | `core:TurnoverRevenue` | micro-entity |
| revenue | 73339 | GBP | 2024-05-31 | 2026-02-26 | filed | yes | `core:TurnoverRevenue` | micro-entity |
| staff_costs | 25140 | GBP | 2024-05-31 | 2026-02-26 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | micro-entity |
| staff_costs | 25140 | GBP | 2024-05-31 | 2025-02-26 | filed | no | `core:StaffCostsEmployeeBenefitsExpense` | micro-entity |
| tax_charge | 7221 | GBP | 2024-05-31 | 2026-02-26 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | micro-entity |
| tax_charge | 7222 | GBP | 2024-05-31 | 2025-02-26 | filed | no | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | micro-entity |
| total_assets_less_current_liabilities | 3073 | GBP | 2024-05-31 | 2025-02-26 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 3073 | GBP | 2024-05-31 | 2026-02-26 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2023-05-31 | 2024-02-29 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2023-05-31 | 2025-02-26 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 4093 | GBP | 2023-05-31 | 2024-02-29 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 4093 | GBP | 2023-05-31 | 2025-02-26 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 3459 | GBP | 2023-05-31 | 2024-02-29 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 3459 | GBP | 2023-05-31 | 2025-02-26 | filed | yes | `core:CurrentAssets` | micro-entity |
| depreciation_amortisation | 0 | GBP | 2023-05-31 | 2025-02-26 | filed | yes | `core:DepreciationAmortisationImpairmentExpense` | micro-entity |
| equity | 2285 | GBP | 2023-05-31 | 2024-02-29 | filed | no | `core:Equity` | micro-entity |
| equity | 2285 | GBP | 2023-05-31 | 2025-02-26 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 2919 | GBP | 2023-05-31 | 2025-02-26 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 2919 | GBP | 2023-05-31 | 2024-02-29 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | 2285 | GBP | 2023-05-31 | 2024-02-29 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 2285 | GBP | 2023-05-31 | 2025-02-26 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -634 | GBP | 2023-05-31 | 2025-02-26 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -634 | GBP | 2023-05-31 | 2024-02-29 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| profit_for_period | 17448 | GBP | 2023-05-31 | 2025-02-26 | filed | yes | `core:ProfitLoss` | micro-entity |
| profit_for_period | 17448 | GBP | 2023-05-31 | 2024-02-29 | filed | no | `core:ProfitLoss` | micro-entity |
| revenue | 57220 | GBP | 2023-05-31 | 2025-02-26 | filed | yes | `core:TurnoverRevenue` | micro-entity |
| revenue | 57220 | GBP | 2023-05-31 | 2024-02-29 | filed | no | `core:TurnoverRevenue` | micro-entity |
| staff_costs | 25140 | GBP | 2023-05-31 | 2025-02-26 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | micro-entity |
| staff_costs | 25140 | GBP | 2023-05-31 | 2024-02-29 | filed | no | `core:StaffCostsEmployeeBenefitsExpense` | micro-entity |
| tax_charge | 4092 | GBP | 2023-05-31 | 2025-02-26 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | micro-entity |
| tax_charge | 4092 | GBP | 2023-05-31 | 2024-02-29 | filed | no | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | micro-entity |
| total_assets_less_current_liabilities | 2285 | GBP | 2023-05-31 | 2025-02-26 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 2285 | GBP | 2023-05-31 | 2024-02-29 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1455 | GBP | 2022-05-31 | 2024-02-29 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 9374 | GBP | 2022-05-31 | 2024-02-29 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 838 | GBP | 2022-05-31 | 2024-02-29 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 2919 | GBP | 2022-05-31 | 2024-02-29 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 838 | GBP | 2022-05-31 | 2024-02-29 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 7919 | GBP | 2022-05-31 | 2024-02-29 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| profit_for_period | 6202 | GBP | 2022-05-31 | 2024-02-29 | filed | yes | `core:ProfitLoss` | micro-entity |
| revenue | 43730 | GBP | 2022-05-31 | 2024-02-29 | filed | yes | `core:TurnoverRevenue` | micro-entity |
| staff_costs | 23816 | GBP | 2022-05-31 | 2024-02-29 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | micro-entity |
| tax_charge | 1454 | GBP | 2022-05-31 | 2024-02-29 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | micro-entity |
| total_assets_less_current_liabilities | 10838 | GBP | 2022-05-31 | 2024-02-29 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2026-02-26: `{"superseded_document_id": "gb:02118916:doc:r6qt4Isg013YDKi4hHjPYvVwBixG69teD4yAY_ODtL8", "restatements": [{"concept": "tax_charge", "period_end": "2024-05-31", "old_value": "7222.0000", "new_value": `

## NORPRESS LIMITED (`gb:02326597`)

- registration: `02326597` (GB), status active, incorporated 1988-12-08
- classification: ['62020'] (sic_2007)
- records: 4 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 88 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2026-03-31 | 2026-06-09 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 96410 | GBP | 2026-03-31 | 2026-06-09 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 96670 | GBP | 2026-03-31 | 2026-06-09 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 260 | GBP | 2026-03-31 | 2026-06-09 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 94952 | GBP | 2026-03-31 | 2026-06-09 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2026-03-31 | 2026-06-09 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 9592 | GBP | 2026-03-31 | 2026-06-09 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 94954 | GBP | 2026-03-31 | 2026-06-09 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 85362 | GBP | 2026-03-31 | 2026-06-09 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 94954 | GBP | 2026-03-31 | 2026-06-09 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2025-03-31 | 2025-07-01 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2025-03-31 | 2026-06-09 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 100468 | GBP | 2025-03-31 | 2025-07-01 | filed | no | `frs-core:CashBankOnHand` | total-exemption-full |
| cash | 100468 | GBP | 2025-03-31 | 2026-06-09 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 100669 | GBP | 2025-03-31 | 2025-07-01 | filed | no | `frs-core:CurrentAssets` | total-exemption-full |
| current_assets | 100669 | GBP | 2025-03-31 | 2026-06-09 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 201 | GBP | 2025-03-31 | 2025-07-01 | filed | no | `frs-core:Debtors` | total-exemption-full |
| debtors | 201 | GBP | 2025-03-31 | 2026-06-09 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2025-03-31 | 2025-07-01 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 109984 | GBP | 2025-03-31 | 2026-06-09 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 109984 | GBP | 2025-03-31 | 2025-07-01 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2025-03-31 | 2026-06-09 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 12615 | GBP | 2025-03-31 | 2026-06-09 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| fixed_assets | 12615 | GBP | 2025-03-31 | 2025-07-01 | filed | no | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 109986 | GBP | 2025-03-31 | 2025-07-01 | filed | no | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 109986 | GBP | 2025-03-31 | 2026-06-09 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 97371 | GBP | 2025-03-31 | 2026-06-09 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 97371 | GBP | 2025-03-31 | 2025-07-01 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 109986 | GBP | 2025-03-31 | 2026-06-09 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 109986 | GBP | 2025-03-31 | 2025-07-01 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-03-31 | 2025-07-01 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-03-31 | 2024-06-17 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 117411 | GBP | 2024-03-31 | 2024-06-17 | filed | no | `frs-core:CashBankOnHand` | total-exemption-full |
| cash | 117411 | GBP | 2024-03-31 | 2025-07-01 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 117494 | GBP | 2024-03-31 | 2024-06-17 | filed | no | `frs-core:CurrentAssets` | total-exemption-full |
| current_assets | 117494 | GBP | 2024-03-31 | 2025-07-01 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 83 | GBP | 2024-03-31 | 2024-06-17 | filed | no | `frs-core:Debtors` | total-exemption-full |
| debtors | 83 | GBP | 2024-03-31 | 2025-07-01 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-03-31 | 2024-06-17 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-03-31 | 2025-07-01 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 107568 | GBP | 2024-03-31 | 2025-07-01 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 107568 | GBP | 2024-03-31 | 2024-06-17 | filed | no | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 0 | GBP | 2024-03-31 | 2025-07-01 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 107570 | GBP | 2024-03-31 | 2024-06-17 | filed | no | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 107570 | GBP | 2024-03-31 | 2025-07-01 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 107570 | GBP | 2024-03-31 | 2025-07-01 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 107570 | GBP | 2024-03-31 | 2024-06-17 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 107570 | GBP | 2024-03-31 | 2025-07-01 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 107570 | GBP | 2024-03-31 | 2024-06-17 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-03-31 | 2024-06-17 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 118415 | GBP | 2023-03-31 | 2024-06-17 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 118825 | GBP | 2023-03-31 | 2024-06-17 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 410 | GBP | 2023-03-31 | 2024-06-17 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 99024 | GBP | 2023-03-31 | 2024-06-17 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-03-31 | 2024-06-17 | filed | yes | `frs-core:Equity` | total-exemption-full |
| net_assets | 99026 | GBP | 2023-03-31 | 2024-06-17 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 99026 | GBP | 2023-03-31 | 2024-06-17 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 99026 | GBP | 2023-03-31 | 2024-06-17 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## COMTECK CONSULTANTS LIMITED (`gb:02508256`)

- registration: `02508256` (GB), status active, incorporated 1990-06-04
- classification: ['62020'] (sic_2007)
- records: 3 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 88 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | iso4217:GBP | 2025-08-31 | 2026-03-12 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 32441 | GBP | 2025-08-31 | 2026-03-12 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 572313 | GBP | 2025-08-31 | 2026-03-12 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 539872 | GBP | 2025-08-31 | 2026-03-12 | filed | yes | `core:Equity` | micro-entity |
| net_assets | 539872 | GBP | 2025-08-31 | 2026-03-12 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 539872 | GBP | 2025-08-31 | 2026-03-12 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 539872 | GBP | 2025-08-31 | 2026-03-12 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2024-08-31 | 2025-05-29 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 36070 | GBP | 2024-08-31 | 2025-05-29 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 36069 | GBP | 2024-08-31 | 2026-03-12 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 554775 | GBP | 2024-08-31 | 2026-03-12 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 554775 | GBP | 2024-08-31 | 2025-05-29 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 518705 | GBP | 2024-08-31 | 2025-05-29 | filed | no | `core:Equity` | micro-entity |
| equity | 518706 | GBP | 2024-08-31 | 2026-03-12 | filed | yes | `core:Equity` | micro-entity |
| net_assets | 518706 | GBP | 2024-08-31 | 2026-03-12 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 518705 | GBP | 2024-08-31 | 2025-05-29 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 518705 | GBP | 2024-08-31 | 2025-05-29 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 518706 | GBP | 2024-08-31 | 2026-03-12 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 518705 | GBP | 2024-08-31 | 2025-05-29 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 518706 | GBP | 2024-08-31 | 2026-03-12 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2023-08-31 | 2024-05-23 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 34794 | GBP | 2023-08-31 | 2024-05-23 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 34794 | GBP | 2023-08-31 | 2025-05-29 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 565302 | GBP | 2023-08-31 | 2025-05-29 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 565302 | GBP | 2023-08-31 | 2024-05-23 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 530508 | GBP | 2023-08-31 | 2025-05-29 | filed | yes | `core:Equity` | micro-entity |
| equity | 530508 | GBP | 2023-08-31 | 2024-05-23 | filed | no | `core:Equity` | micro-entity |
| net_assets | 530508 | GBP | 2023-08-31 | 2024-05-23 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 530508 | GBP | 2023-08-31 | 2025-05-29 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 530508 | GBP | 2023-08-31 | 2025-05-29 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 530508 | GBP | 2023-08-31 | 2024-05-23 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 530508 | GBP | 2023-08-31 | 2024-05-23 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 530508 | GBP | 2023-08-31 | 2025-05-29 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 65240 | GBP | 2022-08-31 | 2024-05-23 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 616712 | GBP | 2022-08-31 | 2024-05-23 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 551232 | GBP | 2022-08-31 | 2024-05-23 | filed | yes | `core:Equity` | micro-entity |
| net_assets | 551232 | GBP | 2022-08-31 | 2024-05-23 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 551472 | GBP | 2022-08-31 | 2024-05-23 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 551472 | GBP | 2022-08-31 | 2024-05-23 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2026-03-12: `{"superseded_document_id": "gb:02508256:doc:RdPEre8Fj60LiNuPlPUeRn-Ydh4y5CJAf2bUsVy9xj4", "restatements": [{"concept": "creditors_within_one_year", "period_end": "2024-08-31", "old_value": "36070.0000`

## MJC ENGINEERING LIMITED (`gb:02673377`)

- registration: `02673377` (GB), status active, incorporated 1991-12-20
- classification: ['71129'] (sic_2007)
- records: 5 officers, 3 beneficial owners, 0 ownership statements, 0 security interests, 83 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 6 | xbrli:pure | 2025-05-31 | 2025-10-13 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 148236 | GBP | 2025-05-31 | 2025-10-13 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity | 101929 | GBP | 2025-05-31 | 2025-10-13 | filed | yes | `ns5:Equity` | micro-entity |
| fixed_assets | 323 | GBP | 2025-05-31 | 2025-10-13 | filed | yes | `ns5:FixedAssets` | micro-entity |
| net_current_assets | 101606 | GBP | 2025-05-31 | 2025-10-13 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 101929 | GBP | 2025-05-31 | 2025-10-13 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 5 | xbrli:pure | 2024-05-31 | 2024-11-15 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 5 | xbrli:pure | 2024-05-31 | 2025-10-13 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| cash | 74778 | GBP | 2024-05-31 | 2024-11-15 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 129668 | GBP | 2024-05-31 | 2025-10-13 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| current_assets | 129668 | GBP | 2024-05-31 | 2024-11-15 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 49790 | GBP | 2024-05-31 | 2024-11-15 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 49790 | GBP | 2024-05-31 | 2024-11-15 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 88293 | GBP | 2024-05-31 | 2024-11-15 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 88193 | GBP | 2024-05-31 | 2024-11-15 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 100 | GBP | 2024-05-31 | 2024-11-15 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 88396 | GBP | 2024-05-31 | 2025-10-13 | filed | yes | `ns5:Equity` | micro-entity |
| fixed_assets | 544 | GBP | 2024-05-31 | 2025-10-13 | filed | yes | `ns5:FixedAssets` | micro-entity |
| net_assets | 88293 | GBP | 2024-05-31 | 2024-11-15 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 87852 | GBP | 2024-05-31 | 2025-10-13 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 87852 | GBP | 2024-05-31 | 2024-11-15 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 88396 | GBP | 2024-05-31 | 2024-11-15 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 88396 | GBP | 2024-05-31 | 2025-10-13 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 4 | xbrli:pure | 2023-05-31 | 2024-11-15 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 4 | xbrli:pure | 2023-05-31 | 2023-09-13 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 77166 | GBP | 2023-05-31 | 2023-09-13 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 77166 | GBP | 2023-05-31 | 2024-11-15 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 133905 | GBP | 2023-05-31 | 2023-09-13 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 133905 | GBP | 2023-05-31 | 2024-11-15 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 51239 | GBP | 2023-05-31 | 2023-09-13 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 51239 | GBP | 2023-05-31 | 2024-11-15 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 51239 | GBP | 2023-05-31 | 2023-09-13 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 51239 | GBP | 2023-05-31 | 2024-11-15 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 100 | GBP | 2023-05-31 | 2023-09-13 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 100 | GBP | 2023-05-31 | 2024-11-15 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 89405 | GBP | 2023-05-31 | 2023-09-13 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 89505 | GBP | 2023-05-31 | 2024-11-15 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 89505 | GBP | 2023-05-31 | 2023-09-13 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 89405 | GBP | 2023-05-31 | 2024-11-15 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 89505 | GBP | 2023-05-31 | 2024-11-15 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 89505 | GBP | 2023-05-31 | 2023-09-13 | filed | no | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 88846 | GBP | 2023-05-31 | 2023-09-13 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 88846 | GBP | 2023-05-31 | 2024-11-15 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 89660 | GBP | 2023-05-31 | 2024-11-15 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 89660 | GBP | 2023-05-31 | 2023-09-13 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 5 | xbrli:pure | 2022-05-31 | 2023-09-13 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 65533 | GBP | 2022-05-31 | 2023-09-13 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 140862 | GBP | 2022-05-31 | 2023-09-13 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 69529 | GBP | 2022-05-31 | 2023-09-13 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 69529 | GBP | 2022-05-31 | 2023-09-13 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 85064 | GBP | 2022-05-31 | 2023-09-13 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 100 | GBP | 2022-05-31 | 2023-09-13 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 85164 | GBP | 2022-05-31 | 2023-09-13 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 85164 | GBP | 2022-05-31 | 2023-09-13 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 84130 | GBP | 2022-05-31 | 2023-09-13 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 85407 | GBP | 2022-05-31 | 2023-09-13 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2025-10-13: `{"superseded_document_id": "gb:02673377:doc:Bb18BqL22R63aVfgZ_Qdr5_7q1cembQFcDTRywr52Tw", "restatements": [{"concept": "equity", "period_end": "2024-05-31", "old_value": "88293.0000", "new_value": "88`

## GLASS COMPUTERS LIMITED (`gb:02930948`)

- registration: `02930948` (GB), status active, incorporated 1994-05-19
- classification: ['62020'] (sic_2007)
- records: 6 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 71 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | iso4217:GBP | 2025-03-31 | 2025-12-18 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 411 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 33695 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 33284 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 33284 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 33284 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 33284 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-03-31 | 2024-12-19 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-03-31 | 2025-12-18 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 411 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 411 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 34229 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 34229 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 33818 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `uk-core:Equity` | micro-entity |
| equity | 33818 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `uk-core:Equity` | micro-entity |
| net_assets | 33818 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 33818 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 33818 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 33818 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 33818 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 33818 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-03-31 | 2023-12-19 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-03-31 | 2024-12-19 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 411 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 411 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 35242 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 35242 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | 34831 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 34831 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 34831 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 34831 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 34831 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 34831 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 34831 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 34831 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2022-03-31 | 2023-12-19 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 411 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 37255 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 36844 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 36844 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 36844 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 36844 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## CYBER SALES LIMITED (`gb:03184917`)

- registration: `03184917` (GB), status active, incorporated 1996-04-12
- classification: ['62012', '62090'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 75 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | iso4217:GBP | 2025-04-30 | 2026-01-29 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2499 | GBP | 2025-04-30 | 2026-01-29 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 114 | GBP | 2025-04-30 | 2026-01-29 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 1688 | GBP | 2025-04-30 | 2026-01-29 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 697 | GBP | 2025-04-30 | 2026-01-29 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 1688 | GBP | 2025-04-30 | 2026-01-29 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 2385 | GBP | 2025-04-30 | 2026-01-29 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 1688 | GBP | 2025-04-30 | 2026-01-29 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2024-04-30 | 2026-01-29 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | xbrli:pure | 2024-04-30 | 2024-11-04 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 7688 | GBP | 2024-04-30 | 2026-01-29 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 7688 | GBP | 2024-04-30 | 2024-11-04 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 70 | GBP | 2024-04-30 | 2024-11-04 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 70 | GBP | 2024-04-30 | 2026-01-29 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 7101 | GBP | 2024-04-30 | 2026-01-29 | filed | yes | `uk-core:Equity` | micro-entity |
| equity | -7101 | GBP | 2024-04-30 | 2024-11-04 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 817 | GBP | 2024-04-30 | 2024-11-04 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 817 | GBP | 2024-04-30 | 2026-01-29 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | -7101 | GBP | 2024-04-30 | 2024-11-04 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 7101 | GBP | 2024-04-30 | 2026-01-29 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -7618 | GBP | 2024-04-30 | 2024-11-04 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 7618 | GBP | 2024-04-30 | 2026-01-29 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -6801 | GBP | 2024-04-30 | 2024-11-04 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 6801 | GBP | 2024-04-30 | 2026-01-29 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2023-04-30 | 2024-11-04 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | xbrli:pure | 2023-04-30 | 2024-01-23 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 11960 | GBP | 2023-04-30 | 2024-01-23 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 11960 | GBP | 2023-04-30 | 2024-11-04 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 1 | GBP | 2023-04-30 | 2024-11-04 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 1 | GBP | 2023-04-30 | 2024-01-23 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | -11200 | GBP | 2023-04-30 | 2024-11-04 | filed | yes | `core:Equity` | micro-entity |
| equity | -11200 | GBP | 2023-04-30 | 2024-01-23 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 1059 | GBP | 2023-04-30 | 2024-01-23 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 1059 | GBP | 2023-04-30 | 2024-11-04 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | -11200 | GBP | 2023-04-30 | 2024-11-04 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | -11200 | GBP | 2023-04-30 | 2024-01-23 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -11959 | GBP | 2023-04-30 | 2024-01-23 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -11959 | GBP | 2023-04-30 | 2024-11-04 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -10900 | GBP | 2023-04-30 | 2024-11-04 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -10900 | GBP | 2023-04-30 | 2024-01-23 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2022-04-30 | 2024-01-23 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 12445 | GBP | 2022-04-30 | 2024-01-23 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | -57 | GBP | 2022-04-30 | 2024-01-23 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -11116 | GBP | 2022-04-30 | 2024-01-23 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 1686 | GBP | 2022-04-30 | 2024-01-23 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | -11116 | GBP | 2022-04-30 | 2024-01-23 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -12502 | GBP | 2022-04-30 | 2024-01-23 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -10816 | GBP | 2022-04-30 | 2024-01-23 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

Coverage @ 2025-04-30: 8/21 concepts available (average_employees, creditors_within_one_year, current_assets, equity, fixed_assets, net_assets, net_current_assets, total_assets_less_current_liabilities)
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

- event restatement @ 2026-01-29: `{"superseded_document_id": "gb:03184917:doc:BGIgdzVjgnoDt9qxJuC2SVy-VQtQ9lBt-FC0bk87CY8", "restatements": [{"concept": "net_current_assets", "period_end": "2024-04-30", "old_value": "-7618.0000", "new`

## MORNINGSTAR INFORMATION SYSTEMS LIMITED (`gb:03430329`)

- registration: `03430329` (GB), status active, incorporated 1997-09-05
- classification: ['62020'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 68 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | iso4217:GBP | 2025-09-30 | 2025-11-28 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2025-09-30 | 2025-11-28 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 10030 | GBP | 2025-09-30 | 2025-11-28 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 0 | GBP | 2025-09-30 | 2025-11-28 | filed | yes | `core:CurrentAssets` | micro-entity |
| depreciation_amortisation | 0 | GBP | 2025-09-30 | 2025-11-28 | filed | yes | `core:DepreciationAmortisationImpairmentExpense` | micro-entity |
| equity | -9930 | GBP | 2025-09-30 | 2025-11-28 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 100 | GBP | 2025-09-30 | 2025-11-28 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | -9930 | GBP | 2025-09-30 | 2025-11-28 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -10030 | GBP | 2025-09-30 | 2025-11-28 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| profit_for_period | -270 | GBP | 2025-09-30 | 2025-11-28 | filed | yes | `core:ProfitLoss` | micro-entity |
| revenue | 4785 | GBP | 2025-09-30 | 2025-11-28 | filed | yes | `core:TurnoverRevenue` | micro-entity |
| staff_costs | 900 | GBP | 2025-09-30 | 2025-11-28 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | micro-entity |
| tax_charge | 0 | GBP | 2025-09-30 | 2025-11-28 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | micro-entity |
| total_assets_less_current_liabilities | -9930 | GBP | 2025-09-30 | 2025-11-28 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2024-09-30 | 2025-05-08 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2024-09-30 | 2025-11-28 | filed | yes | `core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2024-09-30 | 2025-05-08 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 9760 | GBP | 2024-09-30 | 2025-11-28 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 9760 | GBP | 2024-09-30 | 2025-05-08 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 0 | GBP | 2024-09-30 | 2025-05-08 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 0 | GBP | 2024-09-30 | 2025-11-28 | filed | yes | `core:CurrentAssets` | micro-entity |
| depreciation_amortisation | 0 | GBP | 2024-09-30 | 2025-11-28 | filed | yes | `core:DepreciationAmortisationImpairmentExpense` | micro-entity |
| equity | -9660 | GBP | 2024-09-30 | 2025-11-28 | filed | yes | `core:Equity` | micro-entity |
| equity | 9660 | GBP | 2024-09-30 | 2025-05-08 | filed | no | `uk-core:Equity` | micro-entity |
| fixed_assets | 100 | GBP | 2024-09-30 | 2025-11-28 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 100 | GBP | 2024-09-30 | 2025-05-08 | filed | no | `uk-core:FixedAssets` | micro-entity |
| net_assets | -9660 | GBP | 2024-09-30 | 2025-11-28 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 9660 | GBP | 2024-09-30 | 2025-05-08 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -9760 | GBP | 2024-09-30 | 2025-11-28 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 9760 | GBP | 2024-09-30 | 2025-05-08 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| profit_for_period | -565 | GBP | 2024-09-30 | 2025-11-28 | filed | yes | `core:ProfitLoss` | micro-entity |
| revenue | 5740 | GBP | 2024-09-30 | 2025-11-28 | filed | yes | `core:TurnoverRevenue` | micro-entity |
| staff_costs | 2630 | GBP | 2024-09-30 | 2025-11-28 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | micro-entity |
| tax_charge | 0 | GBP | 2024-09-30 | 2025-11-28 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | micro-entity |
| total_assets_less_current_liabilities | 9660 | GBP | 2024-09-30 | 2025-05-08 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -9660 | GBP | 2024-09-30 | 2025-11-28 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2023-09-30 | 2023-10-05 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2023-09-30 | 2025-05-08 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2023-09-30 | 2025-05-08 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2023-09-30 | 2023-10-05 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 9195 | GBP | 2023-09-30 | 2025-05-08 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 9195 | GBP | 2023-09-30 | 2023-10-05 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 0 | GBP | 2023-09-30 | 2025-05-08 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 0 | GBP | 2023-09-30 | 2023-10-05 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | 9095 | GBP | 2023-09-30 | 2025-05-08 | filed | yes | `uk-core:Equity` | micro-entity |
| equity | 9095 | GBP | 2023-09-30 | 2023-10-05 | filed | no | `uk-core:Equity` | micro-entity |
| fixed_assets | 100 | GBP | 2023-09-30 | 2023-10-05 | filed | no | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 100 | GBP | 2023-09-30 | 2025-05-08 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 9095 | GBP | 2023-09-30 | 2025-05-08 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 9095 | GBP | 2023-09-30 | 2023-10-05 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 9195 | GBP | 2023-09-30 | 2023-10-05 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 9195 | GBP | 2023-09-30 | 2025-05-08 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 9095 | GBP | 2023-09-30 | 2023-10-05 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 9095 | GBP | 2023-09-30 | 2025-05-08 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2022-09-30 | 2023-10-05 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2022-09-30 | 2023-10-05 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 8929 | GBP | 2022-09-30 | 2023-10-05 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 0 | GBP | 2022-09-30 | 2023-10-05 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 8829 | GBP | 2022-09-30 | 2023-10-05 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 100 | GBP | 2022-09-30 | 2023-10-05 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 8829 | GBP | 2022-09-30 | 2023-10-05 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 8929 | GBP | 2022-09-30 | 2023-10-05 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 8829 | GBP | 2022-09-30 | 2023-10-05 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2025-11-28: `{"superseded_document_id": "gb:03430329:doc:McRUqxhqb18pONNXHR6Xg3c0zLOZnmu0JNCpnMe9NkU", "restatements": [{"concept": "net_current_assets", "period_end": "2024-09-30", "old_value": "9760.0000", "new_`
