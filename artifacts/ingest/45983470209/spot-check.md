# Ingest spot-check

- database: `data/engine.db`
- latest run: `20261127T103654Z-de00a35a`
- companies in store: 61000; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## DIGITAL PEOPLE LIMITED (`gb:02961157`)

- registration: `02961157` (GB), status active, incorporated 1994-08-17
- classification: ['62020'] (sic_2007)
- records: 7 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 100 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | iso4217:GBP | 2025-12-31 | 2026-09-09 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2025-12-31 | 2026-09-09 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 1216 | GBP | 2025-12-31 | 2026-09-09 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 1216 | GBP | 2025-12-31 | 2026-09-09 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 1216 | GBP | 2025-12-31 | 2026-09-09 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 1216 | GBP | 2025-12-31 | 2026-09-09 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 1216 | GBP | 2025-12-31 | 2026-09-09 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-12-31 | 2026-09-09 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-12-31 | 2025-09-22 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1450 | GBP | 2024-12-31 | 2026-09-09 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1450 | GBP | 2024-12-31 | 2025-09-22 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 3947 | GBP | 2024-12-31 | 2026-09-09 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 3947 | GBP | 2024-12-31 | 2025-09-22 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | 2497 | GBP | 2024-12-31 | 2025-09-22 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 2497 | GBP | 2024-12-31 | 2026-09-09 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 2497 | GBP | 2024-12-31 | 2025-09-22 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 2497 | GBP | 2024-12-31 | 2026-09-09 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 2497 | GBP | 2024-12-31 | 2025-09-22 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 2497 | GBP | 2024-12-31 | 2026-09-09 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 2497 | GBP | 2024-12-31 | 2026-09-09 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 2497 | GBP | 2024-12-31 | 2025-09-22 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-12-31 | 2024-09-24 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-12-31 | 2025-09-22 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1450 | GBP | 2023-12-31 | 2025-09-22 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1450 | GBP | 2023-12-31 | 2024-09-24 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 5150 | GBP | 2023-12-31 | 2025-09-22 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 5150 | GBP | 2023-12-31 | 2024-09-24 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | 3700 | GBP | 2023-12-31 | 2025-09-22 | filed | yes | `uk-core:Equity` | micro-entity |
| equity | 3700 | GBP | 2023-12-31 | 2024-09-24 | filed | no | `uk-core:Equity` | micro-entity |
| net_assets | 3700 | GBP | 2023-12-31 | 2025-09-22 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 3700 | GBP | 2023-12-31 | 2024-09-24 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 3700 | GBP | 2023-12-31 | 2025-09-22 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 3700 | GBP | 2023-12-31 | 2024-09-24 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 3700 | GBP | 2023-12-31 | 2025-09-22 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 3700 | GBP | 2023-12-31 | 2024-09-24 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2022-12-31 | 2024-09-24 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 41817 | GBP | 2022-12-31 | 2024-09-24 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 71525 | GBP | 2022-12-31 | 2024-09-24 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 29708 | GBP | 2022-12-31 | 2024-09-24 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 29708 | GBP | 2022-12-31 | 2024-09-24 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 29708 | GBP | 2022-12-31 | 2024-09-24 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 29708 | GBP | 2022-12-31 | 2024-09-24 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## SIMUNIX LIMITED (`gb:03684982`)

- registration: `03684982` (GB), status active, incorporated 1998-12-17
- classification: ['62012', '63110'] (sic_2007)
- records: 16 officers, 4 beneficial owners, 0 ownership statements, 1 security interests, 148 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 9 | xbrli:pure | 2024-12-31 | 2025-09-25 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 3462875 | GBP | 2024-12-31 | 2025-09-25 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1134374 | GBP | 2024-12-31 | 2025-09-25 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 4086219 | GBP | 2024-12-31 | 2025-09-25 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 623344 | GBP | 2024-12-31 | 2025-09-25 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 623344 | GBP | 2024-12-31 | 2025-09-25 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 472104 | GBP | 2024-12-31 | 2025-09-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 3506948 | GBP | 2024-12-31 | 2025-09-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1813 | GBP | 2024-12-31 | 2025-09-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3032844 | GBP | 2024-12-31 | 2025-09-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 187 | GBP | 2024-12-31 | 2025-09-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 1813 | GBP | 2024-12-31 | 2025-09-25 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 607303 | GBP | 2024-12-31 | 2025-09-25 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | 3506948 | GBP | 2024-12-31 | 2025-09-25 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 2951845 | GBP | 2024-12-31 | 2025-09-25 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 3559148 | GBP | 2024-12-31 | 2025-09-25 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 10 | xbrli:pure | 2023-12-31 | 2025-09-25 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 10 | xbrli:pure | 2023-12-31 | 2024-09-30 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 2989035 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 2989035 | GBP | 2023-12-31 | 2025-09-25 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 983048 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 983048 | GBP | 2023-12-31 | 2025-09-25 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 3180273 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 3180273 | GBP | 2023-12-31 | 2025-09-25 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 191238 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 191238 | GBP | 2023-12-31 | 2025-09-25 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 191238 | GBP | 2023-12-31 | 2025-09-25 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 191238 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2000 | GBP | 2023-12-31 | 2025-09-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 2805177 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 472104 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 0 | GBP | 2023-12-31 | 2025-09-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2331073 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2000 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2331073 | GBP | 2023-12-31 | 2025-09-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 2000 | GBP | 2023-12-31 | 2025-09-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 2805177 | GBP | 2023-12-31 | 2025-09-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 472104 | GBP | 2023-12-31 | 2025-09-25 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 673352 | GBP | 2023-12-31 | 2025-09-25 | filed | yes | `core:FixedAssets` | total-exemption-full |
| fixed_assets | 673352 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:FixedAssets` | total-exemption-full |
| net_assets | 2805177 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 2805177 | GBP | 2023-12-31 | 2025-09-25 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 2197225 | GBP | 2023-12-31 | 2025-09-25 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 2197225 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 2870577 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 2870577 | GBP | 2023-12-31 | 2025-09-25 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 9 | xbrli:pure | 2022-12-31 | 2023-09-14 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 9 | xbrli:pure | 2022-12-31 | 2024-09-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 2491573 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 2491573 | GBP | 2022-12-31 | 2023-09-14 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2022-12-31 | 2023-09-14 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1052746 | GBP | 2022-12-31 | 2023-09-14 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1052746 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 2789338 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 2789338 | GBP | 2022-12-31 | 2023-09-14 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors | 297765 | GBP | 2022-12-31 | 2023-09-14 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 297765 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 297765 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 297765 | GBP | 2022-12-31 | 2023-09-14 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 472104 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 2313622 | GBP | 2022-12-31 | 2023-09-14 | filed | no | `core:Equity` | total-exemption-full |
| equity | 2313622 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1839518 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1839518 | GBP | 2022-12-31 | 2023-09-14 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 472104 | GBP | 2022-12-31 | 2023-09-14 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2000 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2000 | GBP | 2022-12-31 | 2023-09-14 | filed | no | `core:Equity` | total-exemption-full |
| fixed_assets | 627330 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:FixedAssets` | total-exemption-full |
| fixed_assets | 627330 | GBP | 2022-12-31 | 2023-09-14 | filed | no | `core:FixedAssets` | total-exemption-full |
| net_assets | 2313622 | GBP | 2022-12-31 | 2023-09-14 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 2313622 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1736592 | GBP | 2022-12-31 | 2023-09-14 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1736592 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 2363922 | GBP | 2022-12-31 | 2023-09-14 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 2363922 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 9 | xbrli:pure | 2021-12-31 | 2023-09-14 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 1639105 | GBP | 2021-12-31 | 2023-09-14 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 36399 | GBP | 2021-12-31 | 2023-09-14 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 768257 | GBP | 2021-12-31 | 2023-09-14 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 1950850 | GBP | 2021-12-31 | 2023-09-14 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 311745 | GBP | 2021-12-31 | 2023-09-14 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 311745 | GBP | 2021-12-31 | 2023-09-14 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 472104 | GBP | 2021-12-31 | 2023-09-14 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1186008 | GBP | 2021-12-31 | 2023-09-14 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2000 | GBP | 2021-12-31 | 2023-09-14 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 1660112 | GBP | 2021-12-31 | 2023-09-14 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 596518 | GBP | 2021-12-31 | 2023-09-14 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | 1660112 | GBP | 2021-12-31 | 2023-09-14 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1182593 | GBP | 2021-12-31 | 2023-09-14 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1779111 | GBP | 2021-12-31 | 2023-09-14 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## GROUP IT LTD (`gb:04360252`)

- registration: `04360252` (GB), status active, incorporated 2002-01-25
- classification: ['62090'] (sic_2007)
- records: 2 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 56 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | xbrli:pure | 2026-01-31 | 2026-07-06 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 11357 | GBP | 2026-01-31 | 2026-07-06 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 11357 | GBP | 2026-01-31 | 2026-07-06 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -14362 | GBP | 2026-01-31 | 2026-07-06 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2026-01-31 | 2026-07-06 | filed | yes | `frs-core:Equity` | total-exemption-full |
| net_assets | -14262 | GBP | 2026-01-31 | 2026-07-06 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -14262 | GBP | 2026-01-31 | 2026-07-06 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -14262 | GBP | 2026-01-31 | 2026-07-06 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0 | xbrli:pure | 2025-01-31 | 2026-07-06 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 0 | xbrli:pure | 2025-01-31 | 2025-06-10 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 12425 | GBP | 2025-01-31 | 2025-06-10 | filed | no | `frs-core:CashBankOnHand` | total-exemption-full |
| cash | 12425 | GBP | 2025-01-31 | 2026-07-06 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 12425 | GBP | 2025-01-31 | 2025-06-10 | filed | no | `frs-core:CurrentAssets` | total-exemption-full |
| current_assets | 12425 | GBP | 2025-01-31 | 2026-07-06 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-01-31 | 2025-06-10 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -12332 | GBP | 2025-01-31 | 2026-07-06 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-01-31 | 2026-07-06 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -12332 | GBP | 2025-01-31 | 2025-06-10 | filed | no | `frs-core:Equity` | total-exemption-full |
| net_assets | -12232 | GBP | 2025-01-31 | 2026-07-06 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | -12232 | GBP | 2025-01-31 | 2025-06-10 | filed | no | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -12232 | GBP | 2025-01-31 | 2026-07-06 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -12232 | GBP | 2025-01-31 | 2025-06-10 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -12232 | GBP | 2025-01-31 | 2026-07-06 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -12232 | GBP | 2025-01-31 | 2025-06-10 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0 | xbrli:pure | 2024-01-31 | 2025-06-10 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 0 | xbrli:pure | 2024-01-31 | 2024-09-03 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 11560 | GBP | 2024-01-31 | 2024-09-03 | filed | no | `frs-core:CashBankOnHand` | total-exemption-full |
| cash | 11560 | GBP | 2024-01-31 | 2025-06-10 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 11560 | GBP | 2024-01-31 | 2024-09-03 | filed | no | `frs-core:CurrentAssets` | total-exemption-full |
| current_assets | 11560 | GBP | 2024-01-31 | 2025-06-10 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-01-31 | 2024-09-03 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -10794 | GBP | 2024-01-31 | 2025-06-10 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -10794 | GBP | 2024-01-31 | 2024-09-03 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-01-31 | 2025-06-10 | filed | yes | `frs-core:Equity` | total-exemption-full |
| net_assets | -10694 | GBP | 2024-01-31 | 2025-06-10 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | -10694 | GBP | 2024-01-31 | 2024-09-03 | filed | no | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -10694 | GBP | 2024-01-31 | 2025-06-10 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -10694 | GBP | 2024-01-31 | 2024-09-03 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -10694 | GBP | 2024-01-31 | 2024-09-03 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -10694 | GBP | 2024-01-31 | 2025-06-10 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0 | xbrli:pure | 2023-01-31 | 2024-09-03 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 10763 | GBP | 2023-01-31 | 2024-09-03 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 10763 | GBP | 2023-01-31 | 2024-09-03 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -9004 | GBP | 2023-01-31 | 2024-09-03 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-01-31 | 2024-09-03 | filed | yes | `frs-core:Equity` | total-exemption-full |
| net_assets | -8904 | GBP | 2023-01-31 | 2024-09-03 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -8904 | GBP | 2023-01-31 | 2024-09-03 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -8904 | GBP | 2023-01-31 | 2024-09-03 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## URBANR LIMITED (`gb:05065265`)

- registration: `05065265` (GB), status active, incorporated 2004-03-05
- classification: ['71111'] (sic_2007)
- records: 9 officers, 3 beneficial owners, 0 ownership statements, 1 security interests, 79 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 11 | xbrli:pure | 2025-03-31 | 2025-12-29 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | small |
| cash | 21320 | GBP | 2025-03-31 | 2025-12-29 | filed | yes | `ns5:CashBankOnHand` | small |
| current_assets | 1454149 | GBP | 2025-03-31 | 2025-12-29 | filed | yes | `ns5:CurrentAssets` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1432829 | GBP | 2025-03-31 | 2025-12-29 | filed | yes | `ns5:Debtors` | small |
| debtors | 1432829 | GBP | 2025-03-31 | 2025-12-29 | filed | yes | `ns5:Debtors` | small |
| equity | 1262238 | GBP | 2025-03-31 | 2025-12-29 | filed | yes | `ns5:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2025-03-31 | 2025-12-29 | filed | yes | `ns5:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1261238 | GBP | 2025-03-31 | 2025-12-29 | filed | yes | `ns5:Equity` | small |
| net_current_assets | 1261888 | GBP | 2025-03-31 | 2025-12-29 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | small |
| total_assets_less_current_liabilities | 1262238 | GBP | 2025-03-31 | 2025-12-29 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | small |
| average_employees | 11 | xbrli:pure | 2024-03-31 | 2025-12-29 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | small |
| average_employees | 11 | xbrli:pure | 2024-03-31 | 2024-12-31 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | small |
| cash | 573129 | GBP | 2024-03-31 | 2025-12-29 | filed | yes | `ns5:CashBankOnHand` | small |
| cash | 573129 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `ns5:CashBankOnHand` | small |
| current_assets | 2497228 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `ns5:CurrentAssets` | small |
| current_assets | 2497228 | GBP | 2024-03-31 | 2025-12-29 | filed | yes | `ns5:CurrentAssets` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1924099 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `ns5:Debtors` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1924099 | GBP | 2024-03-31 | 2025-12-29 | filed | yes | `ns5:Debtors` | small |
| debtors | 1924099 | GBP | 2024-03-31 | 2025-12-29 | filed | yes | `ns5:Debtors` | small |
| debtors | 1924099 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `ns5:Debtors` | small |
| equity | 1676704 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `ns5:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `ns5:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2024-03-31 | 2025-12-29 | filed | yes | `ns5:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1675704 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `ns5:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1675704 | GBP | 2024-03-31 | 2025-12-29 | filed | yes | `ns5:Equity` | small |
| equity | 1676704 | GBP | 2024-03-31 | 2025-12-29 | filed | yes | `ns5:Equity` | small |
| net_current_assets | 1676004 | GBP | 2024-03-31 | 2025-12-29 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | small |
| net_current_assets | 1676004 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `ns5:NetCurrentAssetsLiabilities` | small |
| total_assets_less_current_liabilities | 1676704 | GBP | 2024-03-31 | 2025-12-29 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | small |
| total_assets_less_current_liabilities | 1676704 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | small |
| average_employees | 11 | xbrli:pure | 2023-03-31 | 2024-12-31 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | small |
| average_employees | 11 | xbrli:pure | 2023-03-31 | 2023-12-22 | filed | no | `ns6:AverageNumberEmployeesDuringPeriod` | small |
| cash | 666355 | GBP | 2023-03-31 | 2023-12-22 | filed | no | `ns6:CashBankOnHand` | small |
| cash | 666355 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `ns5:CashBankOnHand` | small |
| current_assets | 3244114 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `ns5:CurrentAssets` | small |
| current_assets | 3244114 | GBP | 2023-03-31 | 2023-12-22 | filed | no | `ns6:CurrentAssets` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2577759 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `ns5:Debtors` | small |
| debtors | 2577759 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `ns5:Debtors` | small |
| debtors | 2577759 | GBP | 2023-03-31 | 2023-12-22 | filed | no | `ns6:Debtors` | small |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 2577759 | GBP | 2023-03-31 | 2023-12-22 | filed | no | `ns6:Debtors` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `ns5:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2023-03-31 | 2023-12-22 | filed | no | `ns6:Equity` | small |
| equity | 1197072 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `ns5:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1196072 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `ns5:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1196072 | GBP | 2023-03-31 | 2023-12-22 | filed | no | `ns6:Equity` | small |
| equity | 1197072 | GBP | 2023-03-31 | 2023-12-22 | filed | no | `ns6:Equity` | small |
| net_current_assets | 1196022 | GBP | 2023-03-31 | 2023-12-22 | filed | no | `ns6:NetCurrentAssetsLiabilities` | small |
| net_current_assets | 1196022 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | small |
| total_assets_less_current_liabilities | 1197072 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | small |
| total_assets_less_current_liabilities | 1197072 | GBP | 2023-03-31 | 2023-12-22 | filed | no | `ns6:TotalAssetsLessCurrentLiabilities` | small |
| average_employees | 11 | xbrli:pure | 2022-03-31 | 2023-12-22 | filed | yes | `ns6:AverageNumberEmployeesDuringPeriod` | small |
| cash | 323661 | GBP | 2022-03-31 | 2023-12-22 | filed | yes | `ns6:CashBankOnHand` | small |
| current_assets | 1442499 | GBP | 2022-03-31 | 2023-12-22 | filed | yes | `ns6:CurrentAssets` | small |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 1118838 | GBP | 2022-03-31 | 2023-12-22 | filed | yes | `ns6:Debtors` | small |
| debtors | 1118838 | GBP | 2022-03-31 | 2023-12-22 | filed | yes | `ns6:Debtors` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2022-03-31 | 2023-12-22 | filed | yes | `ns6:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 569739 | GBP | 2022-03-31 | 2023-12-22 | filed | yes | `ns6:Equity` | small |
| equity | 570739 | GBP | 2022-03-31 | 2023-12-22 | filed | yes | `ns6:Equity` | small |
| net_current_assets | 569339 | GBP | 2022-03-31 | 2023-12-22 | filed | yes | `ns6:NetCurrentAssetsLiabilities` | small |
| total_assets_less_current_liabilities | 570739 | GBP | 2022-03-31 | 2023-12-22 | filed | yes | `ns6:TotalAssetsLessCurrentLiabilities` | small |

_No coverage facts for the latest run._

## LIGHTPATH IT LTD (`gb:05733082`)

- registration: `05733082` (GB), status active, incorporated 2006-03-07
- classification: ['62020'] (sic_2007)
- records: 5 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 57 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 6 | xbrli:pure | 2025-03-31 | 2025-12-23 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 361341 | GBP | 2025-03-31 | 2025-12-23 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 113259 | GBP | 2025-03-31 | 2025-12-23 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 470586 | GBP | 2025-03-31 | 2025-12-23 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 109245 | GBP | 2025-03-31 | 2025-12-23 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 100 | GBP | 2025-03-31 | 2025-12-23 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 408122 | GBP | 2025-03-31 | 2025-12-23 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 408222 | GBP | 2025-03-31 | 2025-12-23 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 408222 | GBP | 2025-03-31 | 2025-12-23 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 357327 | GBP | 2025-03-31 | 2025-12-23 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| average_employees | 6 | xbrli:pure | 2024-03-31 | 2024-12-09 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 6 | xbrli:pure | 2024-03-31 | 2025-12-23 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 326249 | GBP | 2024-03-31 | 2025-12-23 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 326249 | GBP | 2024-03-31 | 2024-12-09 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 108212 | GBP | 2024-03-31 | 2025-12-23 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 108212 | GBP | 2024-03-31 | 2024-12-09 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 421903 | GBP | 2024-03-31 | 2025-12-23 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 421903 | GBP | 2024-03-31 | 2024-12-09 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors | 95654 | GBP | 2024-03-31 | 2025-12-23 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 95654 | GBP | 2024-03-31 | 2024-12-09 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 95654 | GBP | 2024-03-31 | 2024-12-09 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 100 | GBP | 2024-03-31 | 2025-12-23 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 358017 | GBP | 2024-03-31 | 2024-12-09 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 100 | GBP | 2024-03-31 | 2024-12-09 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 357917 | GBP | 2024-03-31 | 2025-12-23 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 357917 | GBP | 2024-03-31 | 2024-12-09 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 358017 | GBP | 2024-03-31 | 2025-12-23 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 358017 | GBP | 2024-03-31 | 2025-12-23 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 358017 | GBP | 2024-03-31 | 2024-12-09 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 313691 | GBP | 2024-03-31 | 2025-12-23 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 313691 | GBP | 2024-03-31 | 2024-12-09 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| average_employees | 4 | xbrli:pure | 2023-03-31 | 2023-12-15 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 4 | xbrli:pure | 2023-03-31 | 2024-12-09 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 260818 | GBP | 2023-03-31 | 2024-12-09 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 260818 | GBP | 2023-03-31 | 2023-12-15 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 69610 | GBP | 2023-03-31 | 2023-12-15 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 69610 | GBP | 2023-03-31 | 2024-12-09 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 340354 | GBP | 2023-03-31 | 2024-12-09 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 340354 | GBP | 2023-03-31 | 2023-12-15 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors | 79536 | GBP | 2023-03-31 | 2024-12-09 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 79536 | GBP | 2023-03-31 | 2024-12-09 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 79536 | GBP | 2023-03-31 | 2023-12-15 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 79536 | GBP | 2023-03-31 | 2023-12-15 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 307701 | GBP | 2023-03-31 | 2023-12-15 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 100 | GBP | 2023-03-31 | 2023-12-15 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 307801 | GBP | 2023-03-31 | 2023-12-15 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 307701 | GBP | 2023-03-31 | 2024-12-09 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 307801 | GBP | 2023-03-31 | 2024-12-09 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 100 | GBP | 2023-03-31 | 2024-12-09 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 307801 | GBP | 2023-03-31 | 2023-12-15 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 307801 | GBP | 2023-03-31 | 2024-12-09 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 270744 | GBP | 2023-03-31 | 2024-12-09 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 270744 | GBP | 2023-03-31 | 2023-12-15 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| average_employees | 5 | xbrli:pure | 2022-03-31 | 2023-12-15 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 238504 | GBP | 2022-03-31 | 2023-12-15 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 55625 | GBP | 2022-03-31 | 2023-12-15 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 299063 | GBP | 2022-03-31 | 2023-12-15 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 60559 | GBP | 2022-03-31 | 2023-12-15 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 60559 | GBP | 2022-03-31 | 2023-12-15 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 100 | GBP | 2022-03-31 | 2023-12-15 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 254898 | GBP | 2022-03-31 | 2023-12-15 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 254798 | GBP | 2022-03-31 | 2023-12-15 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 254898 | GBP | 2022-03-31 | 2023-12-15 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 243438 | GBP | 2022-03-31 | 2023-12-15 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## VASS IT SERVICES LIMITED (`gb:06319930`)

- registration: `06319930` (GB), status active, incorporated 2007-07-23
- classification: ['62020'] (sic_2007)
- records: 11 officers, 1 beneficial owners, 0 ownership statements, 3 security interests, 73 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 62 | xbrli:pure | 2025-12-31 | 2026-03-03 | filed | yes | `c:AverageNumberEmployeesDuringPeriod` | full |
| cash | 2201780 | GBP | 2025-12-31 | 2026-03-03 | filed | yes | `c:CashBankOnHand` | full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 10190390 | GBP | 2025-12-31 | 2026-03-03 | filed | yes | `c:Creditors` | full |
| current_assets | 6134506 | GBP | 2025-12-31 | 2026-03-03 | filed | yes | `c:CurrentAssets` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 3932726 | GBP | 2025-12-31 | 2026-03-03 | filed | yes | `c:Debtors` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -3923844 | GBP | 2025-12-31 | 2026-03-03 | filed | yes | `c:Equity` | full |
| equity | -3922844 | GBP | 2025-12-31 | 2026-03-03 | filed | yes | `c:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2025-12-31 | 2026-03-03 | filed | yes | `c:Equity` | full |
| fixed_assets | 133040 | GBP | 2025-12-31 | 2026-03-03 | filed | yes | `c:FixedAssets` | full |
| gross_profit | -21912 | GBP | 2025-12-31 | 2026-03-03 | filed | yes | `c:GrossProfitLoss` | full |
| net_assets | -3922844 | GBP | 2025-12-31 | 2026-03-03 | filed | yes | `c:NetAssetsLiabilities` | full |
| net_current_assets | -4055884 | GBP | 2025-12-31 | 2026-03-03 | filed | yes | `c:NetCurrentAssetsLiabilities` | full |
| operating_profit | -3418346 | GBP | 2025-12-31 | 2026-03-03 | filed | yes | `c:OperatingProfitLoss` | full |
| profit_before_tax | -3453140 | GBP | 2025-12-31 | 2026-03-03 | filed | yes | `c:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period | -3422283 | GBP | 2025-12-31 | 2026-03-03 | filed | yes | `c:ProfitLoss` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -3422283 | GBP | 2025-12-31 | 2026-03-03 | filed | yes | `c:ProfitLoss` | full |
| revenue | 13070278 | GBP | 2025-12-31 | 2026-03-03 | filed | yes | `c:TurnoverRevenue` | full |
| staff_costs | 5580039 | GBP | 2025-12-31 | 2026-03-03 | filed | yes | `c:StaffCostsEmployeeBenefitsExpense` | full |
| tax_charge | -30857 | GBP | 2025-12-31 | 2026-03-03 | filed | yes | `c:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| total_assets_less_current_liabilities | -3922844 | GBP | 2025-12-31 | 2026-03-03 | filed | yes | `c:TotalAssetsLessCurrentLiabilities` | full |
| average_employees | 75 | xbrli:pure | 2024-12-31 | 2025-03-19 | filed | no | `d:AverageNumberEmployeesDuringPeriod` | full |
| average_employees | 75 | xbrli:pure | 2024-12-31 | 2026-03-03 | filed | yes | `c:AverageNumberEmployeesDuringPeriod` | full |
| cash | 856816 | GBP | 2024-12-31 | 2026-03-03 | filed | yes | `c:CashBankOnHand` | full |
| cash | 856816 | GBP | 2024-12-31 | 2025-03-19 | filed | no | `d:CashBankOnHand` | full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 8293717 | GBP | 2024-12-31 | 2025-03-19 | filed | no | `d:Creditors` | full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 8511380 | GBP | 2024-12-31 | 2026-03-03 | filed | yes | `c:Creditors` | full |
| current_assets | 6860093 | GBP | 2024-12-31 | 2026-03-03 | filed | yes | `c:CurrentAssets` | full |
| current_assets | 7336616 | GBP | 2024-12-31 | 2025-03-19 | filed | no | `d:CurrentAssets` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 6003277 | GBP | 2024-12-31 | 2026-03-03 | filed | yes | `c:Debtors` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 6479800 | GBP | 2024-12-31 | 2025-03-19 | filed | no | `d:Debtors` | full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'RestatementsFirstTimeAdoptionDimension': 'PriorPeriodErrorIncreaseDecrease'}` | 0 | GBP | 2024-12-31 | 2026-03-03 | filed | yes | `c:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses', 'RestatementsFirstTimeAdoptionDimension': 'PriorPeriodErrorIncreaseDecrease'}` | -694186 | GBP | 2024-12-31 | 2026-03-03 | filed | yes | `c:Equity` | full |
| equity `{'RestatementsFirstTimeAdoptionDimension': 'PriorPeriodErrorIncreaseDecrease'}` | -694186 | GBP | 2024-12-31 | 2026-03-03 | filed | yes | `c:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 192625 | GBP | 2024-12-31 | 2026-03-03 | filed | yes | `c:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2024-12-31 | 2025-03-19 | filed | no | `d:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -501561 | GBP | 2024-12-31 | 2026-03-03 | filed | yes | `c:Equity` | full |
| equity | 193625 | GBP | 2024-12-31 | 2025-03-19 | filed | no | `d:Equity` | full |
| equity `{'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 193625 | GBP | 2024-12-31 | 2026-03-03 | filed | yes | `c:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 192625 | GBP | 2024-12-31 | 2025-03-19 | filed | no | `d:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2024-12-31 | 2026-03-03 | filed | yes | `c:Equity` | full |
| equity | -500561 | GBP | 2024-12-31 | 2026-03-03 | filed | yes | `c:Equity` | full |
| fixed_assets | 1150726 | GBP | 2024-12-31 | 2026-03-03 | filed | yes | `c:FixedAssets` | full |
| fixed_assets | 1150726 | GBP | 2024-12-31 | 2025-03-19 | filed | no | `d:FixedAssets` | full |
| gross_profit | 1373062 | GBP | 2024-12-31 | 2026-03-03 | filed | yes | `c:GrossProfitLoss` | full |
| gross_profit | 1449331 | GBP | 2024-12-31 | 2025-03-19 | filed | no | `d:GrossProfitLoss` | full |
| net_assets | 193625 | GBP | 2024-12-31 | 2025-03-19 | filed | no | `d:NetAssetsLiabilities` | full |
| net_assets | -500561 | GBP | 2024-12-31 | 2026-03-03 | filed | yes | `c:NetAssetsLiabilities` | full |
| net_current_assets | -957101 | GBP | 2024-12-31 | 2025-03-19 | filed | no | `d:NetCurrentAssetsLiabilities` | full |
| net_current_assets | -1651287 | GBP | 2024-12-31 | 2026-03-03 | filed | yes | `c:NetCurrentAssetsLiabilities` | full |
| operating_profit | -940601 | GBP | 2024-12-31 | 2026-03-03 | filed | yes | `c:OperatingProfitLoss` | full |
| operating_profit | -864332 | GBP | 2024-12-31 | 2025-03-19 | filed | no | `d:OperatingProfitLoss` | full |
| profit_before_tax | -892038 | GBP | 2024-12-31 | 2025-03-19 | filed | no | `d:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_before_tax | -968307 | GBP | 2024-12-31 | 2026-03-03 | filed | yes | `c:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period | -1399493 | GBP | 2024-12-31 | 2026-03-03 | filed | yes | `c:ProfitLoss` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -1399493 | GBP | 2024-12-31 | 2026-03-03 | filed | yes | `c:ProfitLoss` | full |
| profit_for_period | -1323224 | GBP | 2024-12-31 | 2025-03-19 | filed | no | `d:ProfitLoss` | full |
| revenue | 17756733 | GBP | 2024-12-31 | 2026-03-03 | filed | yes | `c:TurnoverRevenue` | full |
| revenue | 17833002 | GBP | 2024-12-31 | 2025-03-19 | filed | no | `d:TurnoverRevenue` | full |
| staff_costs | 6104089 | GBP | 2024-12-31 | 2025-03-19 | filed | no | `d:StaffCostsEmployeeBenefitsExpense` | full |
| staff_costs | 6104089 | GBP | 2024-12-31 | 2026-03-03 | filed | yes | `c:StaffCostsEmployeeBenefitsExpense` | full |
| tax_charge | 431186 | GBP | 2024-12-31 | 2025-03-19 | filed | no | `d:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| tax_charge | 431186 | GBP | 2024-12-31 | 2026-03-03 | filed | yes | `c:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| total_assets_less_current_liabilities | 193625 | GBP | 2024-12-31 | 2025-03-19 | filed | no | `d:TotalAssetsLessCurrentLiabilities` | full |
| total_assets_less_current_liabilities | -500561 | GBP | 2024-12-31 | 2026-03-03 | filed | yes | `c:TotalAssetsLessCurrentLiabilities` | full |
| equity `{'RestatementsFirstTimeAdoptionDimension': 'PriorPeriodErrorIncreaseDecrease'}` | -617917 | GBP | 2024-01-01 | 2026-03-03 | filed | yes | `c:Equity` | full |
| equity `{'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 1516849 | GBP | 2024-01-01 | 2026-03-03 | filed | yes | `c:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses', 'RestatementsFirstTimeAdoptionDimension': 'PriorPeriodErrorIncreaseDecrease'}` | -617917 | GBP | 2024-01-01 | 2026-03-03 | filed | yes | `c:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 897932 | GBP | 2024-01-01 | 2026-03-03 | filed | yes | `c:Equity` | full |
| equity | 898932 | GBP | 2024-01-01 | 2026-03-03 | filed | yes | `c:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'RestatementsFirstTimeAdoptionDimension': 'PriorPeriodErrorIncreaseDecrease'}` | 0 | GBP | 2024-01-01 | 2026-03-03 | filed | yes | `c:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 1515849 | GBP | 2024-01-01 | 2026-03-03 | filed | yes | `c:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2024-01-01 | 2026-03-03 | filed | yes | `c:Equity` | full |
| average_employees | 90 | xbrli:pure | 2023-12-31 | 2025-03-19 | filed | yes | `d:AverageNumberEmployeesDuringPeriod` | full |
| average_employees | 90 | xbrli:pure | 2023-12-31 | 2024-03-15 | filed | no | `d:AverageNumberEmployeesDuringPeriod` | full |
| cash | 2014414 | GBP | 2023-12-31 | 2024-03-15 | filed | no | `d:CashBankOnHand` | full |
| cash | 2014414 | GBP | 2023-12-31 | 2025-03-19 | filed | yes | `d:CashBankOnHand` | full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 9037717 | GBP | 2023-12-31 | 2025-03-19 | filed | yes | `d:Creditors` | full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 9037717 | GBP | 2023-12-31 | 2024-03-15 | filed | no | `d:Creditors` | full |
| current_assets | 9366856 | GBP | 2023-12-31 | 2024-03-15 | filed | no | `d:CurrentAssets` | full |
| current_assets | 9366856 | GBP | 2023-12-31 | 2025-03-19 | filed | yes | `d:CurrentAssets` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 7352442 | GBP | 2023-12-31 | 2025-03-19 | filed | yes | `d:Debtors` | full |
| debtors | 7352442 | GBP | 2023-12-31 | 2024-03-15 | filed | yes | `d:Debtors` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 7352442 | GBP | 2023-12-31 | 2024-03-15 | filed | no | `d:Debtors` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1658189 | GBP | 2023-12-31 | 2024-03-15 | filed | no | `d:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2023-12-31 | 2025-03-19 | filed | yes | `d:Equity` | full |
| equity | 1659189 | GBP | 2023-12-31 | 2024-03-15 | filed | no | `d:Equity` | full |
| equity | 1659189 | GBP | 2023-12-31 | 2025-03-19 | filed | yes | `d:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1658189 | GBP | 2023-12-31 | 2025-03-19 | filed | yes | `d:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2023-12-31 | 2024-03-15 | filed | no | `d:Equity` | full |
| fixed_assets | 1330050 | GBP | 2023-12-31 | 2024-03-15 | filed | no | `d:FixedAssets` | full |
| fixed_assets | 1330050 | GBP | 2023-12-31 | 2025-03-19 | filed | yes | `d:FixedAssets` | full |
| gross_profit | -588196 | GBP | 2023-12-31 | 2025-03-19 | filed | yes | `d:GrossProfitLoss` | full |
| gross_profit | -588196 | GBP | 2023-12-31 | 2024-03-15 | filed | no | `d:GrossProfitLoss` | full |
| net_assets | 1659189 | GBP | 2023-12-31 | 2025-03-19 | filed | yes | `d:NetAssetsLiabilities` | full |
| net_assets | 1659189 | GBP | 2023-12-31 | 2024-03-15 | filed | no | `d:NetAssetsLiabilities` | full |
| net_current_assets | 329139 | GBP | 2023-12-31 | 2025-03-19 | filed | yes | `d:NetCurrentAssetsLiabilities` | full |
| net_current_assets | 329139 | GBP | 2023-12-31 | 2024-03-15 | filed | no | `d:NetCurrentAssetsLiabilities` | full |
| operating_profit | -2414500 | GBP | 2023-12-31 | 2024-03-15 | filed | no | `d:OperatingProfitLoss` | full |
| operating_profit | -2414500 | GBP | 2023-12-31 | 2025-03-19 | filed | yes | `d:OperatingProfitLoss` | full |
| profit_before_tax | -2412915 | GBP | 2023-12-31 | 2024-03-15 | filed | no | `d:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_before_tax | -2412915 | GBP | 2023-12-31 | 2025-03-19 | filed | yes | `d:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period | -1906645 | GBP | 2023-12-31 | 2025-03-19 | filed | yes | `d:ProfitLoss` | full |
| profit_for_period | -1906645 | GBP | 2023-12-31 | 2024-03-15 | filed | no | `d:ProfitLoss` | full |
| revenue | 17971547 | GBP | 2023-12-31 | 2025-03-19 | filed | yes | `d:TurnoverRevenue` | full |
| revenue | 17971547 | GBP | 2023-12-31 | 2024-03-15 | filed | no | `d:TurnoverRevenue` | full |
| staff_costs | 7045738 | GBP | 2023-12-31 | 2025-03-19 | filed | yes | `d:StaffCostsEmployeeBenefitsExpense` | full |
| staff_costs | 7045738 | GBP | 2023-12-31 | 2024-03-15 | filed | no | `d:StaffCostsEmployeeBenefitsExpense` | full |
| tax_charge | -506270 | GBP | 2023-12-31 | 2024-03-15 | filed | no | `d:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| tax_charge | -506270 | GBP | 2023-12-31 | 2025-03-19 | filed | yes | `d:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| total_assets_less_current_liabilities | 1659189 | GBP | 2023-12-31 | 2024-03-15 | filed | no | `d:TotalAssetsLessCurrentLiabilities` | full |
| total_assets_less_current_liabilities | 1659189 | GBP | 2023-12-31 | 2025-03-19 | filed | yes | `d:TotalAssetsLessCurrentLiabilities` | full |
| average_employees | 40 | xbrli:pure | 2022-12-31 | 2024-03-15 | filed | yes | `d:AverageNumberEmployeesDuringPeriod` | full |
| cash | 3377152 | GBP | 2022-12-31 | 2024-03-15 | filed | yes | `d:CashBankOnHand` | full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5017503 | GBP | 2022-12-31 | 2024-03-15 | filed | yes | `d:Creditors` | full |
| current_assets | 8560955 | GBP | 2022-12-31 | 2024-03-15 | filed | yes | `d:CurrentAssets` | full |
| debtors | 5183803 | GBP | 2022-12-31 | 2024-03-15 | filed | yes | `d:Debtors` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 5183803 | GBP | 2022-12-31 | 2024-03-15 | filed | yes | `d:Debtors` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3566337 | GBP | 2022-12-31 | 2024-03-15 | filed | yes | `d:Equity` | full |
| equity | 3567337 | GBP | 2022-12-31 | 2024-03-15 | filed | yes | `d:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2022-12-31 | 2024-03-15 | filed | yes | `d:Equity` | full |
| fixed_assets | 24564 | GBP | 2022-12-31 | 2024-03-15 | filed | yes | `d:FixedAssets` | full |
| gross_profit | 2236159 | GBP | 2022-12-31 | 2024-03-15 | filed | yes | `d:GrossProfitLoss` | full |
| net_assets | 3567337 | GBP | 2022-12-31 | 2024-03-15 | filed | yes | `d:NetAssetsLiabilities` | full |
| net_current_assets | 3543452 | GBP | 2022-12-31 | 2024-03-15 | filed | yes | `d:NetCurrentAssetsLiabilities` | full |
| operating_profit | 1030408 | GBP | 2022-12-31 | 2024-03-15 | filed | yes | `d:OperatingProfitLoss` | full |
| profit_before_tax | 1030408 | GBP | 2022-12-31 | 2024-03-15 | filed | yes | `d:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period | 834416 | GBP | 2022-12-31 | 2024-03-15 | filed | yes | `d:ProfitLoss` | full |
| revenue | 13950996 | GBP | 2022-12-31 | 2024-03-15 | filed | yes | `d:TurnoverRevenue` | full |
| staff_costs | 3215895 | GBP | 2022-12-31 | 2024-03-15 | filed | yes | `d:StaffCostsEmployeeBenefitsExpense` | full |
| tax_charge | 195992 | GBP | 2022-12-31 | 2024-03-15 | filed | yes | `d:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| total_assets_less_current_liabilities | 3568016 | GBP | 2022-12-31 | 2024-03-15 | filed | yes | `d:TotalAssetsLessCurrentLiabilities` | full |

_No coverage facts for the latest run._

- event restatement @ 2026-03-03: `{"superseded_document_id": "gb:06319930:doc:stDlR6iLr8A6vH418jaims-WdJ8xhKRS-9dICiNPJmI", "restatements": [{"concept": "revenue", "period_end": "2024-12-31", "old_value": "17833002.0000", "new_value":`

## PROPERTY INVENTORY MANAGEMENT LTD (`gb:06787178`)

- registration: `06787178` (GB), status active, incorporated 2009-01-09
- classification: ['62012'] (sic_2007)
- records: 6 officers, 2 beneficial owners, 0 ownership statements, 1 security interests, 89 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | xbrli:pure | 2025-03-31 | 2025-12-22 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 9054 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 9433 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 53063 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 149084 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 140030 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 140030 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1001 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 88603 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 300 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 87302 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 2015 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | 88603 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 96021 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 98036 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0 | xbrli:pure | 2024-03-31 | 2025-03-24 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 0 | xbrli:pure | 2024-03-31 | 2025-12-22 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 15426 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 15426 | GBP | 2024-03-31 | 2025-03-24 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 12571 | GBP | 2024-03-31 | 2025-03-24 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 12571 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 46306 | GBP | 2024-03-31 | 2025-03-24 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 46306 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 144703 | GBP | 2024-03-31 | 2025-03-24 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 144703 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 129277 | GBP | 2024-03-31 | 2025-03-24 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 129277 | GBP | 2024-03-31 | 2025-03-24 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 129277 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 129277 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 300 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 85865 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 300 | GBP | 2024-03-31 | 2025-03-24 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1001 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 87166 | GBP | 2024-03-31 | 2025-03-24 | filed | no | `core:Equity` | total-exemption-full |
| equity | 87166 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1001 | GBP | 2024-03-31 | 2025-03-24 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 85865 | GBP | 2024-03-31 | 2025-03-24 | filed | no | `core:Equity` | total-exemption-full |
| fixed_assets | 1340 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:FixedAssets` | total-exemption-full |
| fixed_assets | 1340 | GBP | 2024-03-31 | 2025-03-24 | filed | no | `core:FixedAssets` | total-exemption-full |
| net_assets | 87166 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 87166 | GBP | 2024-03-31 | 2025-03-24 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 98397 | GBP | 2024-03-31 | 2025-03-24 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 98397 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 99737 | GBP | 2024-03-31 | 2025-03-24 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 99737 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-03-31 | 2025-03-24 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-03-31 | 2023-12-19 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 48562 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 48562 | GBP | 2023-03-31 | 2025-03-24 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 23166 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 23166 | GBP | 2023-03-31 | 2025-03-24 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 32073 | GBP | 2023-03-31 | 2025-03-24 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 32073 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 142666 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 142666 | GBP | 2023-03-31 | 2025-03-24 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 94104 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 94104 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 94104 | GBP | 2023-03-31 | 2025-03-24 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 94104 | GBP | 2023-03-31 | 2025-03-24 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1001 | GBP | 2023-03-31 | 2025-03-24 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 89060 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1001 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 300 | GBP | 2023-03-31 | 2025-03-24 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 300 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 87759 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:Equity` | total-exemption-full |
| equity | 89060 | GBP | 2023-03-31 | 2025-03-24 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 87759 | GBP | 2023-03-31 | 2025-03-24 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 1633 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:FixedAssets` | total-exemption-full |
| fixed_assets | 1633 | GBP | 2023-03-31 | 2025-03-24 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | 89060 | GBP | 2023-03-31 | 2025-03-24 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 89060 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 110593 | GBP | 2023-03-31 | 2025-03-24 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 110593 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 112226 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 112226 | GBP | 2023-03-31 | 2025-03-24 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 3 | xbrli:pure | 2022-03-31 | 2023-12-19 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 137477 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 31682 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 38729 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 203163 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 65686 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 65686 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 134060 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 135361 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 0 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1301 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 2609 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | 135361 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 164434 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 167043 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## ACE BIZ SOLUTION LIMITED (`gb:07206660`)

- registration: `07206660` (GB), status active, incorporated 2010-03-29
- classification: ['62020'] (sic_2007)
- records: 1 officers, 0 beneficial owners, 0 ownership statements, 0 security interests, 13 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## VARUNA ERP SOLUTIONS LIMITED (`gb:07583830`)

- registration: `07583830` (GB), status active, incorporated 2011-03-30
- classification: ['62012', '62020'] (sic_2007)
- records: 1 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 41 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2026-03-31 | 2026-09-23 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 399 | GBP | 2026-03-31 | 2026-09-23 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 65795 | GBP | 2026-03-31 | 2026-09-23 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 132 | GBP | 2026-03-31 | 2026-09-23 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -66062 | GBP | 2026-03-31 | 2026-09-23 | filed | yes | `core:Equity` | micro-entity |
| net_assets | -66062 | GBP | 2026-03-31 | 2026-09-23 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -65663 | GBP | 2026-03-31 | 2026-09-23 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -65663 | GBP | 2026-03-31 | 2026-09-23 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2025-03-31 | 2026-09-23 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2025-03-31 | 2025-07-08 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 2799 | GBP | 2025-03-31 | 2026-09-23 | filed | yes | `core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 2799 | GBP | 2025-03-31 | 2025-07-08 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 47497 | GBP | 2025-03-31 | 2026-09-23 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 47497 | GBP | 2025-03-31 | 2025-07-08 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 168 | GBP | 2025-03-31 | 2025-07-08 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 168 | GBP | 2025-03-31 | 2026-09-23 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -50128 | GBP | 2025-03-31 | 2025-07-08 | filed | no | `core:Equity` | micro-entity |
| equity | -50128 | GBP | 2025-03-31 | 2026-09-23 | filed | yes | `core:Equity` | micro-entity |
| net_assets | -50128 | GBP | 2025-03-31 | 2026-09-23 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | -50128 | GBP | 2025-03-31 | 2025-07-08 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -47329 | GBP | 2025-03-31 | 2025-07-08 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -47329 | GBP | 2025-03-31 | 2026-09-23 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -47329 | GBP | 2025-03-31 | 2026-09-23 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -47329 | GBP | 2025-03-31 | 2025-07-08 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-03-31 | 2025-07-08 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-03-31 | 2024-06-18 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 5199 | GBP | 2024-03-31 | 2024-06-18 | filed | no | `core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 5199 | GBP | 2024-03-31 | 2025-07-08 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 30363 | GBP | 2024-03-31 | 2024-06-18 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 30363 | GBP | 2024-03-31 | 2025-07-08 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 614 | GBP | 2024-03-31 | 2024-06-18 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 614 | GBP | 2024-03-31 | 2025-07-08 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -34948 | GBP | 2024-03-31 | 2025-07-08 | filed | yes | `core:Equity` | micro-entity |
| equity | -34948 | GBP | 2024-03-31 | 2024-06-18 | filed | no | `core:Equity` | micro-entity |
| net_assets | -34948 | GBP | 2024-03-31 | 2025-07-08 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | -34948 | GBP | 2024-03-31 | 2024-06-18 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -29749 | GBP | 2024-03-31 | 2025-07-08 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -29749 | GBP | 2024-03-31 | 2024-06-18 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -29749 | GBP | 2024-03-31 | 2024-06-18 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -29749 | GBP | 2024-03-31 | 2025-07-08 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-03-31 | 2024-06-18 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 7601 | GBP | 2023-03-31 | 2024-06-18 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 13692 | GBP | 2023-03-31 | 2024-06-18 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 489 | GBP | 2023-03-31 | 2024-06-18 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -20804 | GBP | 2023-03-31 | 2024-06-18 | filed | yes | `core:Equity` | micro-entity |
| net_assets | -20804 | GBP | 2023-03-31 | 2024-06-18 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -13203 | GBP | 2023-03-31 | 2024-06-18 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -13203 | GBP | 2023-03-31 | 2024-06-18 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._
