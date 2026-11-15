# Ingest spot-check

- database: `data/engine.db`
- latest run: `20261115T085427Z-3404808d`
- companies in store: 52200; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## NETWORK MAINTENANCE LIMITED (`gb:02814298`)

- registration: `02814298` (GB), status active, incorporated 1993-04-30
- classification: ['58290', '62090'] (sic_2007)
- records: 20 officers, 2 beneficial owners, 0 ownership statements, 3 security interests, 143 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 5 | xbrli:pure | 2025-11-30 | 2026-04-01 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 131063 | GBP | 2025-11-30 | 2026-04-01 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 228742 | GBP | 2025-11-30 | 2026-04-01 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 93097 | GBP | 2025-11-30 | 2026-04-01 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 170569 | GBP | 2025-11-30 | 2026-04-01 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 52 | GBP | 2025-11-30 | 2026-04-01 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 78 | GBP | 2025-11-30 | 2026-04-01 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 29288 | GBP | 2025-11-30 | 2026-04-01 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 170699 | GBP | 2025-11-30 | 2026-04-01 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 141411 | GBP | 2025-11-30 | 2026-04-01 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 170699 | GBP | 2025-11-30 | 2026-04-01 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 5 | xbrli:pure | 2024-11-30 | 2025-03-17 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 5 | xbrli:pure | 2024-11-30 | 2026-04-01 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 100854 | GBP | 2024-11-30 | 2025-03-17 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 100854 | GBP | 2024-11-30 | 2026-04-01 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 222054 | GBP | 2024-11-30 | 2025-03-17 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 222054 | GBP | 2024-11-30 | 2026-04-01 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 118734 | GBP | 2024-11-30 | 2025-03-17 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 118734 | GBP | 2024-11-30 | 2026-04-01 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 118734 | GBP | 2024-11-30 | 2025-03-17 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 64 | GBP | 2024-11-30 | 2026-04-01 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 149705 | GBP | 2024-11-30 | 2025-03-17 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 149835 | GBP | 2024-11-30 | 2025-03-17 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 66 | GBP | 2024-11-30 | 2025-03-17 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 149705 | GBP | 2024-11-30 | 2026-04-01 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 149705 | GBP | 2024-11-30 | 2026-04-01 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 64 | GBP | 2024-11-30 | 2025-03-17 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 66 | GBP | 2024-11-30 | 2026-04-01 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 32927 | GBP | 2024-11-30 | 2026-04-01 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 149835 | GBP | 2024-11-30 | 2026-04-01 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 116908 | GBP | 2024-11-30 | 2026-04-01 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 116908 | GBP | 2024-11-30 | 2025-03-17 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_for_period | 51916 | GBP | 2024-11-30 | 2025-03-17 | filed | yes | `ns5:ProfitLoss` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 51916 | GBP | 2024-11-30 | 2025-03-17 | filed | yes | `ns5:ProfitLoss` | total-exemption-full |
| total_assets_less_current_liabilities | 149835 | GBP | 2024-11-30 | 2026-04-01 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 149835 | GBP | 2024-11-30 | 2025-03-17 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 5 | xbrli:pure | 2023-11-30 | 2025-03-17 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 5 | xbrli:pure | 2023-11-30 | 2024-03-05 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 125059 | GBP | 2023-11-30 | 2025-03-17 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 125059 | GBP | 2023-11-30 | 2024-03-05 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 211423 | GBP | 2023-11-30 | 2024-03-05 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 211423 | GBP | 2023-11-30 | 2025-03-17 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original'}` | 83341 | GBP | 2023-11-30 | 2024-03-05 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 83341 | GBP | 2023-11-30 | 2025-03-17 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 83341 | GBP | 2023-11-30 | 2024-03-05 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 83341 | GBP | 2023-11-30 | 2025-03-17 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 128874 | GBP | 2023-11-30 | 2025-03-17 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 76 | GBP | 2023-11-30 | 2025-03-17 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 54 | GBP | 2023-11-30 | 2024-03-05 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 129004 | GBP | 2023-11-30 | 2024-03-05 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 54 | GBP | 2023-11-30 | 2025-03-17 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 128874 | GBP | 2023-11-30 | 2024-03-05 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 129004 | GBP | 2023-11-30 | 2025-03-17 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 76 | GBP | 2023-11-30 | 2024-03-05 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | 104876 | GBP | 2023-11-30 | 2025-03-17 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 104876 | GBP | 2023-11-30 | 2024-03-05 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_for_period `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 39581 | GBP | 2023-11-30 | 2024-03-05 | filed | yes | `ns5:ProfitLoss` | total-exemption-full |
| profit_for_period `{'OriginalRevisedDataDimension': 'Original'}` | 39581 | GBP | 2023-11-30 | 2024-03-05 | filed | yes | `ns5:ProfitLoss` | total-exemption-full |
| total_assets_less_current_liabilities | 129004 | GBP | 2023-11-30 | 2025-03-17 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 129004 | GBP | 2023-11-30 | 2024-03-05 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 5 | xbrli:pure | 2022-11-30 | 2024-03-05 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 124340 | GBP | 2022-11-30 | 2024-03-05 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 176215 | GBP | 2022-11-30 | 2024-03-05 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 40025 | GBP | 2022-11-30 | 2024-03-05 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original'}` | 40025 | GBP | 2022-11-30 | 2024-03-05 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 121795 | GBP | 2022-11-30 | 2024-03-05 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 100 | GBP | 2022-11-30 | 2024-03-05 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 121925 | GBP | 2022-11-30 | 2024-03-05 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 30 | GBP | 2022-11-30 | 2024-03-05 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 105399 | GBP | 2022-11-30 | 2024-03-05 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 121925 | GBP | 2022-11-30 | 2024-03-05 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## OBERON IT & PHOTOGRAPHICS LTD (`gb:03498685`)

- registration: `03498685` (GB), status active, incorporated 1998-01-26
- classification: ['62020', '90030'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 70 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-04-05 | 2026-01-01 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 262 | GBP | 2025-04-05 | 2026-01-01 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity | -2534 | GBP | 2025-04-05 | 2026-01-01 | filed | yes | `ns5:Equity` | micro-entity |
| net_current_assets | -2534 | GBP | 2025-04-05 | 2026-01-01 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -2534 | GBP | 2025-04-05 | 2026-01-01 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-04-05 | 2025-01-02 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-04-05 | 2026-01-01 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 492 | GBP | 2024-04-05 | 2026-01-01 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| current_assets | 492 | GBP | 2024-04-05 | 2025-01-02 | filed | no | `ns5:CurrentAssets` | micro-entity |
| equity | -2050 | GBP | 2024-04-05 | 2026-01-01 | filed | yes | `ns5:Equity` | micro-entity |
| equity | -2050 | GBP | 2024-04-05 | 2025-01-02 | filed | no | `ns5:Equity` | micro-entity |
| net_current_assets | -2050 | GBP | 2024-04-05 | 2025-01-02 | filed | no | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -2050 | GBP | 2024-04-05 | 2026-01-01 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -2050 | GBP | 2024-04-05 | 2026-01-01 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -2050 | GBP | 2024-04-05 | 2025-01-02 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 1 | xbrli:pure | 2023-04-05 | 2023-12-30 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-04-05 | 2025-01-02 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 718 | GBP | 2023-04-05 | 2023-12-30 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 844 | GBP | 2023-04-05 | 2023-12-30 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 844 | GBP | 2023-04-05 | 2025-01-02 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| debtors `{'OriginalRevisedDataDimension': 'Original'}` | 126 | GBP | 2023-04-05 | 2023-12-30 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | -1703 | GBP | 2023-04-05 | 2023-12-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 1000 | GBP | 2023-04-05 | 2023-12-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | -1703 | GBP | 2023-04-05 | 2025-01-02 | filed | yes | `ns5:Equity` | micro-entity |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -2703 | GBP | 2023-04-05 | 2023-12-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | -1703 | GBP | 2023-04-05 | 2023-12-30 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -1703 | GBP | 2023-04-05 | 2025-01-02 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| profit_for_period `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -520 | GBP | 2023-04-05 | 2023-12-30 | filed | yes | `ns5:ProfitLoss` | total-exemption-full |
| total_assets_less_current_liabilities | -1703 | GBP | 2023-04-05 | 2025-01-02 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | -1703 | GBP | 2023-04-05 | 2023-12-30 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 1 | xbrli:pure | 2022-04-05 | 2023-12-30 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 1032 | GBP | 2022-04-05 | 2023-12-30 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 1123 | GBP | 2022-04-05 | 2023-12-30 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original'}` | 91 | GBP | 2022-04-05 | 2023-12-30 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | -1183 | GBP | 2022-04-05 | 2023-12-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -2183 | GBP | 2022-04-05 | 2023-12-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 1000 | GBP | 2022-04-05 | 2023-12-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | -1183 | GBP | 2022-04-05 | 2023-12-30 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | -1183 | GBP | 2022-04-05 | 2023-12-30 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## ONE-IP.NET LIMITED (`gb:04068652`)

- registration: `04068652` (GB), status active, incorporated 2000-09-08
- classification: ['62090'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 64 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | xbrli:pure | 2025-03-31 | 2025-12-08 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 5484 | GBP | 2025-03-31 | 2025-12-08 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 164439 | GBP | 2025-03-31 | 2025-12-08 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 158955 | GBP | 2025-03-31 | 2025-12-08 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 152869 | GBP | 2025-03-31 | 2025-12-08 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2025-03-31 | 2025-12-08 | filed | yes | `frs-core:Equity` | total-exemption-full |
| net_assets | 152871 | GBP | 2025-03-31 | 2025-12-08 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 152871 | GBP | 2025-03-31 | 2025-12-08 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 152871 | GBP | 2025-03-31 | 2025-12-08 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0 | xbrli:pure | 2024-03-31 | 2024-11-12 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 0 | xbrli:pure | 2024-03-31 | 2025-12-08 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 6602 | GBP | 2024-03-31 | 2024-11-12 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 6602 | GBP | 2024-03-31 | 2025-12-08 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 164011 | GBP | 2024-03-31 | 2024-11-12 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 164011 | GBP | 2024-03-31 | 2025-12-08 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 157409 | GBP | 2024-03-31 | 2025-12-08 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| debtors | 157409 | GBP | 2024-03-31 | 2024-11-12 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 157409 | GBP | 2024-03-31 | 2024-11-12 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-03-31 | 2025-12-08 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 153368 | GBP | 2024-03-31 | 2024-11-12 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 153370 | GBP | 2024-03-31 | 2024-11-12 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 153368 | GBP | 2024-03-31 | 2025-12-08 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-03-31 | 2024-11-12 | filed | no | `ns5:Equity` | total-exemption-full |
| net_assets | 153370 | GBP | 2024-03-31 | 2025-12-08 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 153370 | GBP | 2024-03-31 | 2025-12-08 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 153370 | GBP | 2024-03-31 | 2024-11-12 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 153370 | GBP | 2024-03-31 | 2024-11-12 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 153370 | GBP | 2024-03-31 | 2025-12-08 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0 | xbrli:pure | 2023-03-31 | 2024-11-12 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 0 | xbrli:pure | 2023-03-31 | 2023-11-10 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 7577 | GBP | 2023-03-31 | 2024-11-12 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 7577 | GBP | 2023-03-31 | 2023-11-10 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 163883 | GBP | 2023-03-31 | 2024-11-12 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 163883 | GBP | 2023-03-31 | 2023-11-10 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 156306 | GBP | 2023-03-31 | 2024-11-12 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 156306 | GBP | 2023-03-31 | 2024-11-12 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 156306 | GBP | 2023-03-31 | 2023-11-10 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original'}` | 156306 | GBP | 2023-03-31 | 2023-11-10 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 153774 | GBP | 2023-03-31 | 2024-11-12 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-03-31 | 2024-11-12 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 153774 | GBP | 2023-03-31 | 2023-11-10 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 153772 | GBP | 2023-03-31 | 2024-11-12 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 153772 | GBP | 2023-03-31 | 2023-11-10 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 2 | GBP | 2023-03-31 | 2023-11-10 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | 153774 | GBP | 2023-03-31 | 2024-11-12 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 153774 | GBP | 2023-03-31 | 2023-11-10 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 153774 | GBP | 2023-03-31 | 2024-11-12 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 153774 | GBP | 2023-03-31 | 2023-11-10 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 1 | xbrli:pure | 2022-03-31 | 2023-11-10 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 9104 | GBP | 2022-03-31 | 2023-11-10 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 164413 | GBP | 2022-03-31 | 2023-11-10 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original'}` | 155309 | GBP | 2022-03-31 | 2023-11-10 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 155309 | GBP | 2022-03-31 | 2023-11-10 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 154630 | GBP | 2022-03-31 | 2023-11-10 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 2 | GBP | 2022-03-31 | 2023-11-10 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 154632 | GBP | 2022-03-31 | 2023-11-10 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 154632 | GBP | 2022-03-31 | 2023-11-10 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 154632 | GBP | 2022-03-31 | 2023-11-10 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## FORESTER BUSINESS CONSULTING LIMITED (`gb:04647386`)

- registration: `04647386` (GB), status active, incorporated 2003-01-24
- classification: ['62090', '70229', '74300'] (sic_2007)
- records: 8 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 77 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-03-31 | 2025-12-18 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 29667 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 29667 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 0 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 26019 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 26021 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | 20150 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 26021 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-03-31 | 2024-10-28 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-03-31 | 2025-12-18 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 52835 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 52835 | GBP | 2024-03-31 | 2024-10-28 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 53058 | GBP | 2024-03-31 | 2024-10-28 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 53058 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 223 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 223 | GBP | 2024-03-31 | 2024-10-28 | filed | no | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 37561 | GBP | 2024-03-31 | 2024-10-28 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 37561 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 37563 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 37563 | GBP | 2024-03-31 | 2024-10-28 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-03-31 | 2024-10-28 | filed | no | `ns5:Equity` | total-exemption-full |
| net_current_assets | 37563 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 37563 | GBP | 2024-03-31 | 2024-10-28 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 37563 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 37563 | GBP | 2024-03-31 | 2024-10-28 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-03-31 | 2023-07-25 | filed | no | `ns6:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-03-31 | 2024-10-28 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 41475 | GBP | 2023-03-31 | 2024-10-28 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 41475 | GBP | 2023-03-31 | 2023-07-25 | filed | no | `ns6:CashBankOnHand` | total-exemption-full |
| current_assets | 41475 | GBP | 2023-03-31 | 2024-10-28 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 0 | GBP | 2023-03-31 | 2024-10-28 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 33568 | GBP | 2023-03-31 | 2024-10-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-03-31 | 2024-10-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-03-31 | 2023-07-25 | filed | no | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 33568 | GBP | 2023-03-31 | 2023-07-25 | filed | no | `ns6:Equity` | total-exemption-full |
| equity | 33570 | GBP | 2023-03-31 | 2023-07-25 | filed | no | `ns6:Equity` | total-exemption-full |
| equity | 33570 | GBP | 2023-03-31 | 2024-10-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | 33570 | GBP | 2023-03-31 | 2024-10-28 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 33570 | GBP | 2023-03-31 | 2023-07-25 | filed | no | `ns6:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 33570 | GBP | 2023-03-31 | 2024-10-28 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 33570 | GBP | 2023-03-31 | 2023-07-25 | filed | no | `ns6:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2022-03-31 | 2023-07-25 | filed | yes | `ns6:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 64425 | GBP | 2022-03-31 | 2023-07-25 | filed | yes | `ns6:CashBankOnHand` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2022-03-31 | 2023-07-25 | filed | yes | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 49978 | GBP | 2022-03-31 | 2023-07-25 | filed | yes | `ns6:Equity` | total-exemption-full |
| equity | 49980 | GBP | 2022-03-31 | 2023-07-25 | filed | yes | `ns6:Equity` | total-exemption-full |
| net_current_assets | 49980 | GBP | 2022-03-31 | 2023-07-25 | filed | yes | `ns6:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 49980 | GBP | 2022-03-31 | 2023-07-25 | filed | yes | `ns6:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## QUARM SOLUTIONS LIMITED (`gb:05247629`)

- registration: `05247629` (GB), status active, incorporated 2004-10-01
- classification: ['62020'] (sic_2007)
- records: 4 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 57 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | iso4217:GBP | 2025-10-31 | 2026-07-24 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 95776 | GBP | 2025-10-31 | 2026-07-24 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 114785 | GBP | 2025-10-31 | 2026-07-24 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 53841 | GBP | 2025-10-31 | 2026-07-24 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 35232 | GBP | 2025-10-31 | 2026-07-24 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 53841 | GBP | 2025-10-31 | 2026-07-24 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 20009 | GBP | 2025-10-31 | 2026-07-24 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 55241 | GBP | 2025-10-31 | 2026-07-24 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2024-10-31 | 2026-07-24 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2024-10-31 | 2025-07-28 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 86662 | GBP | 2024-10-31 | 2026-07-24 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 86662 | GBP | 2024-10-31 | 2025-07-28 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 115016 | GBP | 2024-10-31 | 2025-07-28 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 115016 | GBP | 2024-10-31 | 2026-07-24 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 74147 | GBP | 2024-10-31 | 2025-07-28 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 74147 | GBP | 2024-10-31 | 2026-07-24 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 46043 | GBP | 2024-10-31 | 2025-07-28 | filed | no | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 46043 | GBP | 2024-10-31 | 2026-07-24 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 74147 | GBP | 2024-10-31 | 2026-07-24 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 74147 | GBP | 2024-10-31 | 2025-07-28 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 29354 | GBP | 2024-10-31 | 2025-07-28 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 29354 | GBP | 2024-10-31 | 2026-07-24 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 75397 | GBP | 2024-10-31 | 2025-07-28 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 75397 | GBP | 2024-10-31 | 2026-07-24 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2023-10-31 | 2025-07-28 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2023-10-31 | 2024-05-22 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 37394 | GBP | 2023-10-31 | 2024-05-22 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 37394 | GBP | 2023-10-31 | 2025-07-28 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 100256 | GBP | 2023-10-31 | 2024-05-22 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 100256 | GBP | 2023-10-31 | 2025-07-28 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 66037 | GBP | 2023-10-31 | 2024-05-22 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 66037 | GBP | 2023-10-31 | 2025-07-28 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 3275 | GBP | 2023-10-31 | 2025-07-28 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 3275 | GBP | 2023-10-31 | 2024-05-22 | filed | no | `uk-core:FixedAssets` | micro-entity |
| net_assets | 66037 | GBP | 2023-10-31 | 2024-05-22 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 66037 | GBP | 2023-10-31 | 2025-07-28 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 63862 | GBP | 2023-10-31 | 2025-07-28 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 63862 | GBP | 2023-10-31 | 2024-05-22 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 67137 | GBP | 2023-10-31 | 2024-05-22 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 67137 | GBP | 2023-10-31 | 2025-07-28 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2022-10-31 | 2024-05-22 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 53614 | GBP | 2022-10-31 | 2024-05-22 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 127030 | GBP | 2022-10-31 | 2024-05-22 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 76733 | GBP | 2022-10-31 | 2024-05-22 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 4367 | GBP | 2022-10-31 | 2024-05-22 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 76733 | GBP | 2022-10-31 | 2024-05-22 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 73416 | GBP | 2022-10-31 | 2024-05-22 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 77783 | GBP | 2022-10-31 | 2024-05-22 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## K M C DESIGN LIMITED (`gb:05821677`)

- registration: `05821677` (GB), status active, incorporated 2006-05-18
- classification: ['71121', '74100'] (sic_2007)
- records: 5 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 52 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.02 | xbrli:pure | 2025-05-31 | 2025-10-13 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 34293 | GBP | 2025-05-31 | 2025-10-13 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 119544 | GBP | 2025-05-31 | 2025-10-13 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 85691 | GBP | 2025-05-31 | 2025-10-13 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 203 | GBP | 2025-05-31 | 2025-10-13 | filed | yes | `core:FixedAssets` | micro-entity |
| average_employees | 0.02 | xbrli:pure | 2024-05-31 | 2025-10-13 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-05-31 | 2024-11-21 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 94441 | GBP | 2024-05-31 | 2024-11-21 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 14004 | GBP | 2024-05-31 | 2025-10-13 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 94465 | GBP | 2024-05-31 | 2025-10-13 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 94702 | GBP | 2024-05-31 | 2024-11-21 | filed | no | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 261 | GBP | 2024-05-31 | 2024-11-21 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2024-05-31 | 2024-11-21 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity | 80970 | GBP | 2024-05-31 | 2025-10-13 | filed | yes | `core:Equity` | micro-entity |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 79970 | GBP | 2024-05-31 | 2024-11-21 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 272 | GBP | 2024-05-31 | 2025-10-13 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 272 | GBP | 2024-05-31 | 2024-11-21 | filed | no | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 80970 | GBP | 2024-05-31 | 2024-11-21 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 80698 | GBP | 2024-05-31 | 2024-11-21 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 80970 | GBP | 2024-05-31 | 2024-11-21 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-05-31 | 2024-01-12 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-05-31 | 2024-11-21 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 110329 | GBP | 2023-05-31 | 2024-01-12 | filed | no | `frs-core:CashBankOnHand` | total-exemption-full |
| cash | 110329 | GBP | 2023-05-31 | 2024-11-21 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 116190 | GBP | 2023-05-31 | 2024-01-12 | filed | no | `frs-core:CurrentAssets` | total-exemption-full |
| current_assets | 116190 | GBP | 2023-05-31 | 2024-11-21 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 5861 | GBP | 2023-05-31 | 2024-01-12 | filed | no | `frs-core:Debtors` | total-exemption-full |
| debtors | 5861 | GBP | 2023-05-31 | 2024-11-21 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 98014 | GBP | 2023-05-31 | 2024-01-12 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2023-05-31 | 2024-11-21 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 98014 | GBP | 2023-05-31 | 2024-11-21 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2023-05-31 | 2024-01-12 | filed | no | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 363 | GBP | 2023-05-31 | 2024-01-12 | filed | no | `frs-core:FixedAssets` | total-exemption-full |
| fixed_assets | 363 | GBP | 2023-05-31 | 2024-11-21 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 99014 | GBP | 2023-05-31 | 2024-11-21 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 99014 | GBP | 2023-05-31 | 2024-01-12 | filed | no | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 98651 | GBP | 2023-05-31 | 2024-01-12 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 98651 | GBP | 2023-05-31 | 2024-11-21 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 99014 | GBP | 2023-05-31 | 2024-11-21 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 99014 | GBP | 2023-05-31 | 2024-01-12 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2022-05-31 | 2024-01-12 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 115471 | GBP | 2022-05-31 | 2024-01-12 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 120910 | GBP | 2022-05-31 | 2024-01-12 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 5439 | GBP | 2022-05-31 | 2024-01-12 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2022-05-31 | 2024-01-12 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 102876 | GBP | 2022-05-31 | 2024-01-12 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 509 | GBP | 2022-05-31 | 2024-01-12 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 103876 | GBP | 2022-05-31 | 2024-01-12 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 103367 | GBP | 2022-05-31 | 2024-01-12 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 103876 | GBP | 2022-05-31 | 2024-01-12 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2025-10-13: `{"superseded_document_id": "gb:05821677:doc:b0Gz8BAPs11QVT1rn9k1xEKnV7plGO41SzFxm6tkTHA", "restatements": [{"concept": "current_assets", "period_end": "2024-05-31", "old_value": "94702.0000", "new_val`

## ERUDUS LIMITED (`gb:06315071`)

- registration: `06315071` (GB), status active, incorporated 2007-07-17
- classification: ['62030'] (sic_2007)
- records: 17 officers, 2 beneficial owners, 1 ownership statements, 0 security interests, 98 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.23 | xbrli:pure | 2025-12-31 | 2026-06-22 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | small |
| cash | 706098 | GBP | 2025-12-31 | 2026-06-22 | filed | yes | `core:CashBankOnHand` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1109690 | GBP | 2025-12-31 | 2026-06-22 | filed | yes | `core:Creditors` | small |
| current_assets | 1090714 | GBP | 2025-12-31 | 2026-06-22 | filed | yes | `core:CurrentAssets` | small |
| debtors | 384616 | GBP | 2025-12-31 | 2026-06-22 | filed | yes | `core:Debtors` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 330423 | GBP | 2025-12-31 | 2026-06-22 | filed | yes | `core:Debtors` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 326 | GBP | 2025-12-31 | 2026-06-22 | filed | yes | `core:Equity` | small |
| equity | 86221 | GBP | 2025-12-31 | 2026-06-22 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 85895 | GBP | 2025-12-31 | 2026-06-22 | filed | yes | `core:Equity` | small |
| net_current_assets | -18976 | GBP | 2025-12-31 | 2026-06-22 | filed | yes | `core:NetCurrentAssetsLiabilities` | small |
| profit_for_period | 48738 | GBP | 2025-12-31 | 2026-06-22 | filed | yes | `core:ProfitLoss` | small |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 48738 | GBP | 2025-12-31 | 2026-06-22 | filed | yes | `core:ProfitLoss` | small |
| total_assets_less_current_liabilities | 86221 | GBP | 2025-12-31 | 2026-06-22 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | small |
| average_employees | 0.2 | xbrli:pure | 2025-03-31 | 2026-06-22 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | small |
| average_employees | 20 | xbrli:pure | 2025-03-31 | 2025-08-05 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 312646 | GBP | 2025-03-31 | 2025-08-05 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 312646 | GBP | 2025-03-31 | 2026-06-22 | filed | yes | `core:CashBankOnHand` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 890114 | GBP | 2025-03-31 | 2026-06-22 | filed | yes | `core:Creditors` | small |
| current_assets | 935898 | GBP | 2025-03-31 | 2025-08-05 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 935898 | GBP | 2025-03-31 | 2026-06-22 | filed | yes | `core:CurrentAssets` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 503218 | GBP | 2025-03-31 | 2025-08-05 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 623252 | GBP | 2025-03-31 | 2025-08-05 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 623252 | GBP | 2025-03-31 | 2026-06-22 | filed | yes | `core:Debtors` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 503218 | GBP | 2025-03-31 | 2026-06-22 | filed | yes | `core:Debtors` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 162437 | GBP | 2025-03-31 | 2026-06-22 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 326 | GBP | 2025-03-31 | 2025-08-05 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 211760 | GBP | 2025-03-31 | 2025-08-05 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 326 | GBP | 2025-03-31 | 2026-06-22 | filed | yes | `core:Equity` | small |
| equity | 212086 | GBP | 2025-03-31 | 2025-08-05 | filed | no | `core:Equity` | total-exemption-full |
| equity | 162763 | GBP | 2025-03-31 | 2026-06-22 | filed | yes | `core:Equity` | small |
| net_current_assets | 95107 | GBP | 2025-03-31 | 2025-08-05 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 45784 | GBP | 2025-03-31 | 2026-06-22 | filed | yes | `core:NetCurrentAssetsLiabilities` | small |
| profit_for_period | 241674 | GBP | 2025-03-31 | 2025-08-05 | filed | no | `core:ProfitLoss` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 231351 | GBP | 2025-03-31 | 2026-06-22 | filed | yes | `core:ProfitLoss` | small |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 241674 | GBP | 2025-03-31 | 2025-08-05 | filed | no | `core:ProfitLoss` | total-exemption-full |
| profit_for_period | 231351 | GBP | 2025-03-31 | 2026-06-22 | filed | yes | `core:ProfitLoss` | small |
| total_assets_less_current_liabilities | 162763 | GBP | 2025-03-31 | 2026-06-22 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | small |
| total_assets_less_current_liabilities | 212086 | GBP | 2025-03-31 | 2025-08-05 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 18 | xbrli:pure | 2024-03-31 | 2025-08-05 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 501857 | GBP | 2024-03-31 | 2025-08-05 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| current_assets | 828403 | GBP | 2024-03-31 | 2025-08-05 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 326546 | GBP | 2024-03-31 | 2025-08-05 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 326546 | GBP | 2024-03-31 | 2025-08-05 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 224491 | GBP | 2024-03-31 | 2025-08-05 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 185491 | GBP | 2024-03-31 | 2026-06-22 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 340 | GBP | 2024-03-31 | 2026-06-22 | filed | yes | `core:Equity` | small |
| equity | 224831 | GBP | 2024-03-31 | 2025-08-05 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 340 | GBP | 2024-03-31 | 2025-08-05 | filed | no | `core:Equity` | total-exemption-full |
| net_current_assets | 115062 | GBP | 2024-03-31 | 2025-08-05 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 71429 | GBP | 2024-03-31 | 2025-08-05 | filed | yes | `core:ProfitLoss` | total-exemption-full |
| profit_for_period | 71429 | GBP | 2024-03-31 | 2025-08-05 | filed | yes | `core:ProfitLoss` | total-exemption-full |
| total_assets_less_current_liabilities | 224831 | GBP | 2024-03-31 | 2025-08-05 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 340 | GBP | 2023-03-31 | 2025-08-05 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 203063 | GBP | 2023-03-31 | 2025-08-05 | filed | yes | `core:Equity` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2026-06-22: `{"superseded_document_id": "gb:06315071:doc:6hdmfuIKE4qfLiBeUDfTTjxohx3hehOpSoOLZOkhOnU", "restatements": [{"concept": "net_current_assets", "period_end": "2025-03-31", "old_value": "95107.0000", "new`

## CMETRIX LTD (`gb:06720930`)

- registration: `06720930` (GB), status active, incorporated 2008-10-10
- classification: ['62012', '73200'] (sic_2007)
- records: 1 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 41 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | iso4217:GBP | 2025-12-31 | 2026-09-30 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2025-12-31 | 2026-09-30 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 12179 | GBP | 2025-12-31 | 2026-09-30 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 18785 | GBP | 2025-12-31 | 2026-09-30 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 7591 | GBP | 2025-12-31 | 2026-09-30 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 1216 | GBP | 2025-12-31 | 2026-09-30 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 7591 | GBP | 2025-12-31 | 2026-09-30 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 6606 | GBP | 2025-12-31 | 2026-09-30 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 7822 | GBP | 2025-12-31 | 2026-09-30 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-12-31 | 2025-09-25 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | iso4217:GBP | 2024-12-31 | 2026-09-30 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| cash | 17792 | GBP | 2024-12-31 | 2025-09-25 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 1833 | GBP | 2024-12-31 | 2026-09-30 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 32833 | GBP | 2024-12-31 | 2026-09-30 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 49137 | GBP | 2024-12-31 | 2026-09-30 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 49137 | GBP | 2024-12-31 | 2025-09-25 | filed | no | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 31345 | GBP | 2024-12-31 | 2025-09-25 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-12-31 | 2025-09-25 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity | 18645 | GBP | 2024-12-31 | 2026-09-30 | filed | yes | `uk-core:Equity` | micro-entity |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 18545 | GBP | 2024-12-31 | 2025-09-25 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 5153 | GBP | 2024-12-31 | 2025-09-25 | filed | no | `frs-core:FixedAssets` | total-exemption-full |
| fixed_assets | 5153 | GBP | 2024-12-31 | 2026-09-30 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 18645 | GBP | 2024-12-31 | 2025-09-25 | filed | no | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 18645 | GBP | 2024-12-31 | 2026-09-30 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 16304 | GBP | 2024-12-31 | 2025-09-25 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 16304 | GBP | 2024-12-31 | 2026-09-30 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 21457 | GBP | 2024-12-31 | 2026-09-30 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 21457 | GBP | 2024-12-31 | 2025-09-25 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-12-31 | 2024-09-27 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-12-31 | 2025-09-25 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 26115 | GBP | 2023-12-31 | 2025-09-25 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| cash | 26115 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 54696 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 54697 | GBP | 2023-12-31 | 2025-09-25 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 28581 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 28582 | GBP | 2023-12-31 | 2025-09-25 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 28581 | GBP | 2023-12-31 | 2024-09-27 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 31301 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 31401 | GBP | 2023-12-31 | 2024-09-27 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-12-31 | 2025-09-25 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 31301 | GBP | 2023-12-31 | 2025-09-25 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 7324 | GBP | 2023-12-31 | 2025-09-25 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 31401 | GBP | 2023-12-31 | 2025-09-25 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 31401 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 31702 | GBP | 2023-12-31 | 2025-09-25 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 31702 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 21322 | GBP | 2023-12-31 | 2024-09-27 | filed | yes | `ns5:ProfitLoss` | total-exemption-full |
| total_assets_less_current_liabilities | 39026 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 39026 | GBP | 2023-12-31 | 2025-09-25 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2022-12-31 | 2024-09-27 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 39608 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 48998 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 3865 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 3865 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 25079 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 24979 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 25079 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 27223 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 37703 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2025-09-25: `{"superseded_document_id": "gb:06720930:doc:QoBjHzFLzuWfjQtiZ6CRyzAQultHwyFmuuipPexOjGc", "restatements": [{"concept": "debtors", "period_end": "2023-12-31", "old_value": "28581.0000", "new_value": "2`

## BURKES CAD SERVICES LIMITED (`gb:07208925`)

- registration: `07208925` (GB), status active, incorporated 2010-03-30
- classification: ['62020'] (sic_2007)
- records: 1 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 34 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2026-03-31 | 2026-10-28 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 14150 | GBP | 2026-03-31 | 2026-10-28 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 20070 | GBP | 2026-03-31 | 2026-10-28 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 5920 | GBP | 2026-03-31 | 2026-10-28 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2026-03-31 | 2026-10-28 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2 | GBP | 2026-03-31 | 2026-10-28 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 1716 | GBP | 2026-03-31 | 2026-10-28 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 102 | GBP | 2026-03-31 | 2026-10-28 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -1614 | GBP | 2026-03-31 | 2026-10-28 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 102 | GBP | 2026-03-31 | 2026-10-28 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2025-03-31 | 2025-11-26 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2025-03-31 | 2026-10-28 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 11695 | GBP | 2025-03-31 | 2025-11-26 | filed | no | `frs-core:CashBankOnHand` | total-exemption-full |
| cash | 11695 | GBP | 2025-03-31 | 2026-10-28 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 24455 | GBP | 2025-03-31 | 2025-11-26 | filed | no | `frs-core:CurrentAssets` | total-exemption-full |
| current_assets | 24455 | GBP | 2025-03-31 | 2026-10-28 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 12760 | GBP | 2025-03-31 | 2025-11-26 | filed | no | `frs-core:Debtors` | total-exemption-full |
| debtors | 12760 | GBP | 2025-03-31 | 2026-10-28 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2 | GBP | 2025-03-31 | 2025-11-26 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-03-31 | 2025-11-26 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2 | GBP | 2025-03-31 | 2026-10-28 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-03-31 | 2026-10-28 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 2288 | GBP | 2025-03-31 | 2025-11-26 | filed | no | `frs-core:FixedAssets` | total-exemption-full |
| fixed_assets | 2288 | GBP | 2025-03-31 | 2026-10-28 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 102 | GBP | 2025-03-31 | 2026-10-28 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 102 | GBP | 2025-03-31 | 2025-11-26 | filed | no | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -2186 | GBP | 2025-03-31 | 2025-11-26 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -2186 | GBP | 2025-03-31 | 2026-10-28 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 102 | GBP | 2025-03-31 | 2025-11-26 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 102 | GBP | 2025-03-31 | 2026-10-28 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-03-31 | 2025-11-26 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-03-31 | 2024-09-16 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 18834 | GBP | 2024-03-31 | 2025-11-26 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| cash | 18834 | GBP | 2024-03-31 | 2024-09-16 | filed | no | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 28314 | GBP | 2024-03-31 | 2025-11-26 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| current_assets | 28314 | GBP | 2024-03-31 | 2024-09-16 | filed | no | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 9480 | GBP | 2024-03-31 | 2025-11-26 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| debtors | 9480 | GBP | 2024-03-31 | 2024-09-16 | filed | no | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-03-31 | 2024-09-16 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3 | GBP | 2024-03-31 | 2025-11-26 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3 | GBP | 2024-03-31 | 2024-09-16 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-03-31 | 2025-11-26 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 2238 | GBP | 2024-03-31 | 2025-11-26 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| fixed_assets | 2238 | GBP | 2024-03-31 | 2024-09-16 | filed | no | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 103 | GBP | 2024-03-31 | 2025-11-26 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 103 | GBP | 2024-03-31 | 2024-09-16 | filed | no | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -2135 | GBP | 2024-03-31 | 2024-09-16 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -2135 | GBP | 2024-03-31 | 2025-11-26 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 103 | GBP | 2024-03-31 | 2024-09-16 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 103 | GBP | 2024-03-31 | 2025-11-26 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-03-31 | 2024-09-16 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 11922 | GBP | 2023-03-31 | 2024-09-16 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 16162 | GBP | 2023-03-31 | 2024-09-16 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 4240 | GBP | 2023-03-31 | 2024-09-16 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-03-31 | 2024-09-16 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1 | GBP | 2023-03-31 | 2024-09-16 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 2155 | GBP | 2023-03-31 | 2024-09-16 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 101 | GBP | 2023-03-31 | 2024-09-16 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -2054 | GBP | 2023-03-31 | 2024-09-16 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 101 | GBP | 2023-03-31 | 2024-09-16 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._
