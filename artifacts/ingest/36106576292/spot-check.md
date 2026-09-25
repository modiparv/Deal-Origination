# Ingest spot-check

- database: `data/engine.db`
- latest run: `20260925T071413Z-161dbcab`
- companies in store: 12200; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## EMOS INFORMATION SYSTEMS LIMITED (`gb:01743307`)

- registration: `01743307` (GB), status active, incorporated 1983-07-29
- classification: ['18129', '46660', '62090'] (sic_2007)
- records: 15 officers, 2 beneficial owners, 0 ownership statements, 6 security interests, 164 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.12 | xbrli:pure | 2025-03-31 | 2025-11-25 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 52865 | GBP | 2025-03-31 | 2025-11-25 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| current_assets | 2691221 | GBP | 2025-03-31 | 2025-11-25 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 2549530 | GBP | 2025-03-31 | 2025-11-25 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2549530 | GBP | 2025-03-31 | 2025-11-25 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 2141934 | GBP | 2025-03-31 | 2025-11-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 105185 | GBP | 2025-03-31 | 2025-11-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 9786 | GBP | 2025-03-31 | 2025-11-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1981933 | GBP | 2025-03-31 | 2025-11-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 45030 | GBP | 2025-03-31 | 2025-11-25 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 1067522 | GBP | 2025-03-31 | 2025-11-25 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_current_assets | 1074412 | GBP | 2025-03-31 | 2025-11-25 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 2141934 | GBP | 2025-03-31 | 2025-11-25 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0.11 | xbrli:pure | 2024-03-31 | 2025-11-25 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 11 | xbrli:pure | 2024-03-31 | 2024-08-13 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 393997 | GBP | 2024-03-31 | 2024-08-13 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 393998 | GBP | 2024-03-31 | 2025-11-25 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1684252 | GBP | 2024-03-31 | 2024-08-13 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 3548114 | GBP | 2024-03-31 | 2024-08-13 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 3548114 | GBP | 2024-03-31 | 2025-11-25 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 3079643 | GBP | 2024-03-31 | 2025-11-25 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 3079644 | GBP | 2024-03-31 | 2024-08-13 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 3079643 | GBP | 2024-03-31 | 2025-11-25 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 3079644 | GBP | 2024-03-31 | 2024-08-13 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 45030 | GBP | 2024-03-31 | 2025-11-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 9786 | GBP | 2024-03-31 | 2024-08-13 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 45029 | GBP | 2024-03-31 | 2024-08-13 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 9786 | GBP | 2024-03-31 | 2025-11-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 2935151 | GBP | 2024-03-31 | 2024-08-13 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 105185 | GBP | 2024-03-31 | 2024-08-13 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 105185 | GBP | 2024-03-31 | 2025-11-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 2935148 | GBP | 2024-03-31 | 2025-11-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2775147 | GBP | 2024-03-31 | 2025-11-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2775151 | GBP | 2024-03-31 | 2024-08-13 | filed | no | `core:Equity` | total-exemption-full |
| fixed_assets | 1071288 | GBP | 2024-03-31 | 2025-11-25 | filed | yes | `core:FixedAssets` | total-exemption-full |
| fixed_assets | 1071289 | GBP | 2024-03-31 | 2024-08-13 | filed | no | `core:FixedAssets` | total-exemption-full |
| net_current_assets | 1863860 | GBP | 2024-03-31 | 2025-11-25 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1863862 | GBP | 2024-03-31 | 2024-08-13 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 2935148 | GBP | 2024-03-31 | 2025-11-25 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 2935151 | GBP | 2024-03-31 | 2024-08-13 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 11 | xbrli:pure | 2023-03-31 | 2024-08-13 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 11 | xbrli:pure | 2023-03-31 | 2023-11-15 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | small |
| cash | 220602 | GBP | 2023-03-31 | 2024-08-13 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 220602 | GBP | 2023-03-31 | 2023-11-15 | filed | no | `core:CashBankOnHand` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1715148 | GBP | 2023-03-31 | 2024-08-13 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1715148 | GBP | 2023-03-31 | 2023-11-15 | filed | no | `core:Creditors` | small |
| current_assets | 3574766 | GBP | 2023-03-31 | 2023-11-15 | filed | no | `core:CurrentAssets` | small |
| current_assets | 3574766 | GBP | 2023-03-31 | 2024-08-13 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 3273535 | GBP | 2023-03-31 | 2023-11-15 | filed | no | `core:Debtors` | small |
| debtors | 3273535 | GBP | 2023-03-31 | 2023-11-15 | filed | no | `core:Debtors` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 3273535 | GBP | 2023-03-31 | 2024-08-13 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 3273535 | GBP | 2023-03-31 | 2024-08-13 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2766774 | GBP | 2023-03-31 | 2024-08-13 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 9786 | GBP | 2023-03-31 | 2023-11-15 | filed | no | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 45029 | GBP | 2023-03-31 | 2023-11-15 | filed | no | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 105185 | GBP | 2023-03-31 | 2023-11-15 | filed | no | `core:Equity` | small |
| equity | 2926774 | GBP | 2023-03-31 | 2023-11-15 | filed | no | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 105185 | GBP | 2023-03-31 | 2024-08-13 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 2926774 | GBP | 2023-03-31 | 2024-08-13 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 45029 | GBP | 2023-03-31 | 2024-08-13 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2766774 | GBP | 2023-03-31 | 2023-11-15 | filed | no | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 9786 | GBP | 2023-03-31 | 2024-08-13 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 1067156 | GBP | 2023-03-31 | 2023-11-15 | filed | no | `core:FixedAssets` | small |
| fixed_assets | 1067156 | GBP | 2023-03-31 | 2024-08-13 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_current_assets | 1859618 | GBP | 2023-03-31 | 2023-11-15 | filed | no | `core:NetCurrentAssetsLiabilities` | small |
| net_current_assets | 1859618 | GBP | 2023-03-31 | 2024-08-13 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 172191 | GBP | 2023-03-31 | 2023-11-15 | filed | yes | `core:ProfitLoss` | small |
| profit_for_period | 172191 | GBP | 2023-03-31 | 2023-11-15 | filed | yes | `core:ProfitLoss` | small |
| total_assets_less_current_liabilities | 2926774 | GBP | 2023-03-31 | 2024-08-13 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 2926774 | GBP | 2023-03-31 | 2023-11-15 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | small |
| average_employees | 13 | xbrli:pure | 2022-03-31 | 2023-11-15 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | small |
| cash | 167908 | GBP | 2022-03-31 | 2023-11-15 | filed | yes | `core:CashBankOnHand` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1660281 | GBP | 2022-03-31 | 2023-11-15 | filed | yes | `core:Creditors` | small |
| current_assets | 3485866 | GBP | 2022-03-31 | 2023-11-15 | filed | yes | `core:CurrentAssets` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 3253041 | GBP | 2022-03-31 | 2023-11-15 | filed | yes | `core:Debtors` | small |
| debtors | 3253041 | GBP | 2022-03-31 | 2023-11-15 | filed | yes | `core:Debtors` | small |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 9786 | GBP | 2022-03-31 | 2023-11-15 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 105185 | GBP | 2022-03-31 | 2023-11-15 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2734173 | GBP | 2022-03-31 | 2023-11-15 | filed | yes | `core:Equity` | small |
| equity | 2894173 | GBP | 2022-03-31 | 2023-11-15 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 45029 | GBP | 2022-03-31 | 2023-11-15 | filed | yes | `core:Equity` | small |
| fixed_assets | 1068588 | GBP | 2022-03-31 | 2023-11-15 | filed | yes | `core:FixedAssets` | small |
| net_current_assets | 1825585 | GBP | 2022-03-31 | 2023-11-15 | filed | yes | `core:NetCurrentAssetsLiabilities` | small |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 132623 | GBP | 2022-03-31 | 2023-11-15 | filed | yes | `core:ProfitLoss` | small |
| profit_for_period | 132623 | GBP | 2022-03-31 | 2023-11-15 | filed | yes | `core:ProfitLoss` | small |
| total_assets_less_current_liabilities | 2894173 | GBP | 2022-03-31 | 2023-11-15 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 45029 | GBP | 2021-03-31 | 2023-11-15 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2741590 | GBP | 2021-03-31 | 2023-11-15 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 9786 | GBP | 2021-03-31 | 2023-11-15 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 105185 | GBP | 2021-03-31 | 2023-11-15 | filed | yes | `core:Equity` | small |

_No coverage facts for the latest run._

- event restatement @ 2025-11-25: `{"superseded_document_id": "gb:01743307:doc:qX6eeTuYG1g-kkGp99C-tLPbyugGbU2L5KoEJVccv7I", "restatements": [{"concept": "fixed_assets", "period_end": "2024-03-31", "old_value": "1071289.0000", "new_val`

## PAUL A.FRIEZE & ASSOCIATES LTD (`gb:02178817`)

- registration: `02178817` (GB), status active, incorporated 1987-10-15
- classification: ['71122'] (sic_2007)
- records: 7 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 105 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | iso4217:GBP | 2025-03-31 | 2026-03-27 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5419 | GBP | 2025-03-31 | 2026-03-27 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 14864 | GBP | 2025-03-31 | 2026-03-27 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 9445 | GBP | 2025-03-31 | 2026-03-27 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2025-03-31 | 2026-03-27 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 9445 | GBP | 2025-03-31 | 2026-03-27 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 9445 | GBP | 2025-03-31 | 2026-03-27 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 9445 | GBP | 2025-03-31 | 2026-03-27 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-03-31 | 2024-12-20 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-03-31 | 2026-03-27 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 518 | GBP | 2024-03-31 | 2026-03-27 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 518 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 14351 | GBP | 2024-03-31 | 2026-03-27 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 14351 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | 14627 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 14627 | GBP | 2024-03-31 | 2026-03-27 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 794 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 794 | GBP | 2024-03-31 | 2026-03-27 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 14627 | GBP | 2024-03-31 | 2026-03-27 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 14627 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 13833 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 13833 | GBP | 2024-03-31 | 2026-03-27 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 14627 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 14627 | GBP | 2024-03-31 | 2026-03-27 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-03-31 | 2024-12-20 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-03-31 | 2023-09-27 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 7016 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 6627 | GBP | 2023-03-31 | 2023-09-27 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 22555 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 21960 | GBP | 2023-03-31 | 2023-09-27 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 16899 | GBP | 2023-03-31 | 2023-09-27 | filed | no | `core:Equity` | micro-entity |
| equity | 16899 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 1360 | GBP | 2023-03-31 | 2023-09-27 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 1360 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 16899 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 16899 | GBP | 2023-03-31 | 2023-09-27 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 15539 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 16072 | GBP | 2023-03-31 | 2023-09-27 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 16899 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 17432 | GBP | 2023-03-31 | 2023-09-27 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2022-03-31 | 2023-09-27 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 16187 | GBP | 2022-03-31 | 2023-09-27 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 26522 | GBP | 2022-03-31 | 2023-09-27 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 12203 | GBP | 2022-03-31 | 2023-09-27 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 1926 | GBP | 2022-03-31 | 2023-09-27 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 12203 | GBP | 2022-03-31 | 2023-09-27 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 10871 | GBP | 2022-03-31 | 2023-09-27 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 12797 | GBP | 2022-03-31 | 2023-09-27 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2024-12-20: `{"superseded_document_id": "gb:02178817:doc:WLyxpJnNryVMmXV_MQGFCqEGZKvkEWvz9VLgirJHI64", "restatements": [{"concept": "current_assets", "period_end": "2023-03-31", "old_value": "21960.0000", "new_val`

## BURNET WARE & GRAVES LIMITED (`gb:02498513`)

- registration: `02498513` (GB), status active, incorporated 1990-05-03
- classification: ['68310', '68320', '71129'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 1 security interests, 107 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 7 | xbrli:pure | 2025-03-31 | 2025-08-26 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 92776 | GBP | 2025-03-31 | 2025-08-26 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 16800 | GBP | 2025-03-31 | 2025-08-26 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 54549 | GBP | 2025-03-31 | 2025-08-26 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 114240 | GBP | 2025-03-31 | 2025-08-26 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 21464 | GBP | 2025-03-31 | 2025-08-26 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 15290 | GBP | 2025-03-31 | 2025-08-26 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 57290 | GBP | 2025-03-31 | 2025-08-26 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 28000 | GBP | 2025-03-31 | 2025-08-26 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 14000 | GBP | 2025-03-31 | 2025-08-26 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 57290 | GBP | 2025-03-31 | 2025-08-26 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 59691 | GBP | 2025-03-31 | 2025-08-26 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 74090 | GBP | 2025-03-31 | 2025-08-26 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0 | xbrli:pure | 2024-03-31 | 2024-08-23 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 86429 | GBP | 2024-03-31 | 2025-08-26 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 86429 | GBP | 2024-03-31 | 2024-08-23 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 19967 | GBP | 2024-03-31 | 2024-08-23 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 19967 | GBP | 2024-03-31 | 2025-08-26 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 63994 | GBP | 2024-03-31 | 2024-08-23 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 63994 | GBP | 2024-03-31 | 2025-08-26 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 111379 | GBP | 2024-03-31 | 2024-08-23 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 111379 | GBP | 2024-03-31 | 2025-08-26 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 24950 | GBP | 2024-03-31 | 2025-08-26 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 24950 | GBP | 2024-03-31 | 2024-08-23 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 14000 | GBP | 2024-03-31 | 2025-08-26 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 9686 | GBP | 2024-03-31 | 2024-08-23 | filed | no | `core:Equity` | total-exemption-full |
| equity | 51686 | GBP | 2024-03-31 | 2024-08-23 | filed | no | `core:Equity` | total-exemption-full |
| equity | 51686 | GBP | 2024-03-31 | 2025-08-26 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 28000 | GBP | 2024-03-31 | 2025-08-26 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 28000 | GBP | 2024-03-31 | 2024-08-23 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 9686 | GBP | 2024-03-31 | 2025-08-26 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 14000 | GBP | 2024-03-31 | 2024-08-23 | filed | no | `core:Equity` | total-exemption-full |
| net_assets | 51686 | GBP | 2024-03-31 | 2025-08-26 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 51686 | GBP | 2024-03-31 | 2024-08-23 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 47385 | GBP | 2024-03-31 | 2024-08-23 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 47385 | GBP | 2024-03-31 | 2025-08-26 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 71653 | GBP | 2024-03-31 | 2025-08-26 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 71653 | GBP | 2024-03-31 | 2024-08-23 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 6 | xbrli:pure | 2023-03-31 | 2024-08-23 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 6 | xbrli:pure | 2023-03-31 | 2023-09-22 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 39635 | GBP | 2023-03-31 | 2023-09-22 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 39635 | GBP | 2023-03-31 | 2024-08-23 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 23133 | GBP | 2023-03-31 | 2024-08-23 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 23133 | GBP | 2023-03-31 | 2023-09-22 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 66709 | GBP | 2023-03-31 | 2023-09-22 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 66709 | GBP | 2023-03-31 | 2024-08-23 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 99013 | GBP | 2023-03-31 | 2023-09-22 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 99013 | GBP | 2023-03-31 | 2024-08-23 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 59378 | GBP | 2023-03-31 | 2023-09-22 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 59378 | GBP | 2023-03-31 | 2024-08-23 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 14000 | GBP | 2023-03-31 | 2024-08-23 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 28000 | GBP | 2023-03-31 | 2024-08-23 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 28000 | GBP | 2023-03-31 | 2023-09-22 | filed | no | `core:Equity` | total-exemption-full |
| equity | 45158 | GBP | 2023-03-31 | 2023-09-22 | filed | no | `core:Equity` | total-exemption-full |
| equity | 45158 | GBP | 2023-03-31 | 2024-08-23 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 14000 | GBP | 2023-03-31 | 2023-09-22 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3158 | GBP | 2023-03-31 | 2023-09-22 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3158 | GBP | 2023-03-31 | 2024-08-23 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 45158 | GBP | 2023-03-31 | 2023-09-22 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 45158 | GBP | 2023-03-31 | 2024-08-23 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 32304 | GBP | 2023-03-31 | 2023-09-22 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 32304 | GBP | 2023-03-31 | 2024-08-23 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 68291 | GBP | 2023-03-31 | 2023-09-22 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 68291 | GBP | 2023-03-31 | 2024-08-23 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 6 | xbrli:pure | 2022-03-31 | 2023-09-22 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 73367 | GBP | 2022-03-31 | 2023-09-22 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 26300 | GBP | 2022-03-31 | 2023-09-22 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 76458 | GBP | 2022-03-31 | 2023-09-22 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 94420 | GBP | 2022-03-31 | 2023-09-22 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 21053 | GBP | 2022-03-31 | 2023-09-22 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 14000 | GBP | 2022-03-31 | 2023-09-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 18962 | GBP | 2022-03-31 | 2023-09-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -23038 | GBP | 2022-03-31 | 2023-09-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 28000 | GBP | 2022-03-31 | 2023-09-22 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 18962 | GBP | 2022-03-31 | 2023-09-22 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 17962 | GBP | 2022-03-31 | 2023-09-22 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 45262 | GBP | 2022-03-31 | 2023-09-22 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## COMPUTER COMMUNICATIONS U.K. LTD. (`gb:02750333`)

- registration: `02750333` (GB), status active, incorporated 1992-09-24
- classification: ['61900', '62020'] (sic_2007)
- records: 7 officers, 1 beneficial owners, 0 ownership statements, 1 security interests, 94 filings, 2 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-08-31 | 2026-05-07 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 76788 | GBP | 2025-08-31 | 2026-05-07 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 5458 | GBP | 2025-08-31 | 2026-05-07 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 33921 | GBP | 2025-08-31 | 2026-05-07 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 94763 | GBP | 2025-08-31 | 2026-05-07 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 17273 | GBP | 2025-08-31 | 2026-05-07 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 41018 | GBP | 2025-08-31 | 2026-05-07 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 20100 | GBP | 2025-08-31 | 2026-05-07 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 61118 | GBP | 2025-08-31 | 2026-05-07 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 61118 | GBP | 2025-08-31 | 2026-05-07 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 60842 | GBP | 2025-08-31 | 2026-05-07 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 66576 | GBP | 2025-08-31 | 2026-05-07 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-08-31 | 2025-01-30 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 3 | xbrli:pure | 2024-08-31 | 2026-05-07 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 51450 | GBP | 2024-08-31 | 2026-05-07 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 51450 | GBP | 2024-08-31 | 2025-01-30 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 409 | GBP | 2024-08-31 | 2025-01-30 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 409 | GBP | 2024-08-31 | 2026-05-07 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 26436 | GBP | 2024-08-31 | 2026-05-07 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 26436 | GBP | 2024-08-31 | 2025-01-30 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 69789 | GBP | 2024-08-31 | 2025-01-30 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 69789 | GBP | 2024-08-31 | 2026-05-07 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 16454 | GBP | 2024-08-31 | 2026-05-07 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 16454 | GBP | 2024-08-31 | 2025-01-30 | filed | no | `core:Debtors` | total-exemption-full |
| equity | 47329 | GBP | 2024-08-31 | 2025-01-30 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 27229 | GBP | 2024-08-31 | 2025-01-30 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 20100 | GBP | 2024-08-31 | 2025-01-30 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 20100 | GBP | 2024-08-31 | 2026-05-07 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 27229 | GBP | 2024-08-31 | 2026-05-07 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 47329 | GBP | 2024-08-31 | 2026-05-07 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 47329 | GBP | 2024-08-31 | 2026-05-07 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 47329 | GBP | 2024-08-31 | 2025-01-30 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 43353 | GBP | 2024-08-31 | 2025-01-30 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 43353 | GBP | 2024-08-31 | 2026-05-07 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 47738 | GBP | 2024-08-31 | 2026-05-07 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 47738 | GBP | 2024-08-31 | 2025-01-30 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 3 | xbrli:pure | 2023-08-31 | 2025-01-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-08-31 | 2024-03-08 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 67401 | GBP | 2023-08-31 | 2024-03-08 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 67401 | GBP | 2023-08-31 | 2025-01-30 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 18 | GBP | 2023-08-31 | 2024-03-08 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 18 | GBP | 2023-08-31 | 2025-01-30 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 45320 | GBP | 2023-08-31 | 2024-03-08 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 45320 | GBP | 2023-08-31 | 2025-01-30 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 84577 | GBP | 2023-08-31 | 2025-01-30 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 84577 | GBP | 2023-08-31 | 2024-03-08 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors | 15556 | GBP | 2023-08-31 | 2025-01-30 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 15556 | GBP | 2023-08-31 | 2024-03-08 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 27282 | GBP | 2023-08-31 | 2025-01-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 47382 | GBP | 2023-08-31 | 2024-03-08 | filed | no | `core:Equity` | total-exemption-full |
| equity | 47382 | GBP | 2023-08-31 | 2025-01-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 20100 | GBP | 2023-08-31 | 2024-03-08 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 27282 | GBP | 2023-08-31 | 2024-03-08 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 20100 | GBP | 2023-08-31 | 2025-01-30 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 47382 | GBP | 2023-08-31 | 2025-01-30 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 47382 | GBP | 2023-08-31 | 2024-03-08 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 39257 | GBP | 2023-08-31 | 2025-01-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 39257 | GBP | 2023-08-31 | 2024-03-08 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 47400 | GBP | 2023-08-31 | 2025-01-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 47400 | GBP | 2023-08-31 | 2024-03-08 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 3 | xbrli:pure | 2022-08-31 | 2024-03-08 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 64349 | GBP | 2022-08-31 | 2024-03-08 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 231 | GBP | 2022-08-31 | 2024-03-08 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 39259 | GBP | 2022-08-31 | 2024-03-08 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 80897 | GBP | 2022-08-31 | 2024-03-08 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 14928 | GBP | 2022-08-31 | 2024-03-08 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 27278 | GBP | 2022-08-31 | 2024-03-08 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 47378 | GBP | 2022-08-31 | 2024-03-08 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 20100 | GBP | 2022-08-31 | 2024-03-08 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 47378 | GBP | 2022-08-31 | 2024-03-08 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 41638 | GBP | 2022-08-31 | 2024-03-08 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 47609 | GBP | 2022-08-31 | 2024-03-08 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2025-01-30: `{"superseded_document_id": "gb:02750333:doc:39pDXmeqfvvLFTs-5Vs8NQztuYPvd-zJSQBd1ECVnsM", "restatements": [{"concept": "average_employees", "period_end": "2023-08-31", "old_value": "2.0000", "new_valu`
- event restatement @ 2026-05-07: `{"superseded_document_id": "gb:02750333:doc:Fi5oEsOc2nxYAYLoWCi8Gh8tMUglkFb7rgokgGDhWy0", "restatements": [{"concept": "average_employees", "period_end": "2024-08-31", "old_value": "2.0000", "new_valu`

## BRIDGEHEAD SOFTWARE LIMITED (`gb:02962777`)

- registration: `02962777` (GB), status active, incorporated 1994-08-26
- classification: ['62090'] (sic_2007)
- records: 15 officers, 1 beneficial owners, 0 ownership statements, 9 security interests, 161 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## BIGHAND LIMITED (`gb:03128724`)

- registration: `03128724` (GB), status active, incorporated 1995-11-21
- classification: ['62012'] (sic_2007)
- records: 20 officers, 2 beneficial owners, 0 ownership statements, 19 security interests, 205 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## GARRATT CONSULTANTS LIMITED (`gb:03276296`)

- registration: `03276296` (GB), status active, incorporated 1996-11-11
- classification: ['62020', '62090', '71129', '82990'] (sic_2007)
- records: 5 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 74 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | xbrli:pure | 2025-10-31 | 2026-07-23 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 12632 | GBP | 2025-10-31 | 2026-07-23 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 12786 | GBP | 2025-10-31 | 2026-07-23 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 154 | GBP | 2025-10-31 | 2026-07-23 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 7403 | GBP | 2025-10-31 | 2026-07-23 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2025-10-31 | 2026-07-23 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 7401 | GBP | 2025-10-31 | 2026-07-23 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | 6937 | GBP | 2025-10-31 | 2026-07-23 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 7403 | GBP | 2025-10-31 | 2026-07-23 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0 | xbrli:pure | 2024-10-31 | 2025-07-17 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 0 | xbrli:pure | 2024-10-31 | 2026-07-23 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 12306 | GBP | 2024-10-31 | 2026-07-23 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 12306 | GBP | 2024-10-31 | 2025-07-17 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 12596 | GBP | 2024-10-31 | 2026-07-23 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 12596 | GBP | 2024-10-31 | 2025-07-17 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 290 | GBP | 2024-10-31 | 2026-07-23 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 290 | GBP | 2024-10-31 | 2025-07-17 | filed | no | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 7437 | GBP | 2024-10-31 | 2025-07-17 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 7439 | GBP | 2024-10-31 | 2025-07-17 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-10-31 | 2026-07-23 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-10-31 | 2025-07-17 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 7439 | GBP | 2024-10-31 | 2026-07-23 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 7437 | GBP | 2024-10-31 | 2026-07-23 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | 6651 | GBP | 2024-10-31 | 2026-07-23 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 6651 | GBP | 2024-10-31 | 2025-07-17 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 7439 | GBP | 2024-10-31 | 2026-07-23 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 7439 | GBP | 2024-10-31 | 2025-07-17 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0 | xbrli:pure | 2023-10-31 | 2024-07-18 | filed | no | `ns6:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 0 | xbrli:pure | 2023-10-31 | 2025-07-17 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 20510 | GBP | 2023-10-31 | 2024-07-18 | filed | no | `ns6:CashBankOnHand` | total-exemption-full |
| cash | 20510 | GBP | 2023-10-31 | 2025-07-17 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 20608 | GBP | 2023-10-31 | 2025-07-17 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 20608 | GBP | 2023-10-31 | 2024-07-18 | filed | no | `ns6:CurrentAssets` | total-exemption-full |
| debtors | 98 | GBP | 2023-10-31 | 2025-07-17 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 98 | GBP | 2023-10-31 | 2024-07-18 | filed | no | `ns6:Debtors` | total-exemption-full |
| equity | 14851 | GBP | 2023-10-31 | 2025-07-17 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 14849 | GBP | 2023-10-31 | 2024-07-18 | filed | no | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-10-31 | 2024-07-18 | filed | no | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 14849 | GBP | 2023-10-31 | 2025-07-17 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-10-31 | 2025-07-17 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 14851 | GBP | 2023-10-31 | 2024-07-18 | filed | no | `ns6:Equity` | total-exemption-full |
| net_current_assets | 13506 | GBP | 2023-10-31 | 2025-07-17 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 13506 | GBP | 2023-10-31 | 2024-07-18 | filed | no | `ns6:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 14851 | GBP | 2023-10-31 | 2025-07-17 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 14851 | GBP | 2023-10-31 | 2024-07-18 | filed | no | `ns6:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0 | xbrli:pure | 2022-10-31 | 2024-07-18 | filed | yes | `ns6:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 11985 | GBP | 2022-10-31 | 2024-07-18 | filed | yes | `ns6:CashBankOnHand` | total-exemption-full |
| current_assets | 12092 | GBP | 2022-10-31 | 2024-07-18 | filed | yes | `ns6:CurrentAssets` | total-exemption-full |
| debtors | 107 | GBP | 2022-10-31 | 2024-07-18 | filed | yes | `ns6:Debtors` | total-exemption-full |
| equity | 7307 | GBP | 2022-10-31 | 2024-07-18 | filed | yes | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2022-10-31 | 2024-07-18 | filed | yes | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 7305 | GBP | 2022-10-31 | 2024-07-18 | filed | yes | `ns6:Equity` | total-exemption-full |
| net_current_assets | 6225 | GBP | 2022-10-31 | 2024-07-18 | filed | yes | `ns6:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 7307 | GBP | 2022-10-31 | 2024-07-18 | filed | yes | `ns6:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## ICODE SYSTEMS LIMITED (`gb:03428325`)

- registration: `03428325` (GB), status active, incorporated 1997-09-03
- classification: ['62090'] (sic_2007)
- records: 8 officers, 3 beneficial owners, 0 ownership statements, 0 security interests, 77 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 7 | iso4217:GBP | 2025-02-28 | 2025-11-28 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 2500 | GBP | 2025-02-28 | 2025-11-28 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 110194 | GBP | 2025-02-28 | 2025-11-28 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 325840 | GBP | 2025-02-28 | 2025-11-28 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 223838 | GBP | 2025-02-28 | 2025-11-28 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 12460 | GBP | 2025-02-28 | 2025-11-28 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 223838 | GBP | 2025-02-28 | 2025-11-28 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 215646 | GBP | 2025-02-28 | 2025-11-28 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 228106 | GBP | 2025-02-28 | 2025-11-28 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 8 | iso4217:GBP | 2024-02-28 | 2025-11-28 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 8 | xbrli:pure | 2024-02-28 | 2024-11-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 69552 | GBP | 2024-02-28 | 2024-11-30 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 12500 | GBP | 2024-02-28 | 2025-11-28 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 12500 | GBP | 2024-02-28 | 2024-11-30 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 93786 | GBP | 2024-02-28 | 2024-11-30 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 93786 | GBP | 2024-02-28 | 2025-11-28 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 245893 | GBP | 2024-02-28 | 2025-11-28 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 245893 | GBP | 2024-02-28 | 2024-11-30 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 161126 | GBP | 2024-02-28 | 2024-11-30 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 161126 | GBP | 2024-02-28 | 2024-11-30 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 144810 | GBP | 2024-02-28 | 2024-11-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 144910 | GBP | 2024-02-28 | 2025-11-28 | filed | yes | `uk-core:Equity` | micro-entity |
| equity | 144910 | GBP | 2024-02-28 | 2024-11-30 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-02-28 | 2024-11-30 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 7071 | GBP | 2024-02-28 | 2025-11-28 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 144910 | GBP | 2024-02-28 | 2025-11-28 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 144910 | GBP | 2024-02-28 | 2024-11-30 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 152107 | GBP | 2024-02-28 | 2024-11-30 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 152107 | GBP | 2024-02-28 | 2025-11-28 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 159178 | GBP | 2024-02-28 | 2025-11-28 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 159178 | GBP | 2024-02-28 | 2024-11-30 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 8 | iso4217:GBP | 2023-02-28 | 2023-11-27 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 8 | xbrli:pure | 2023-02-28 | 2024-11-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 68389 | GBP | 2023-02-28 | 2024-11-30 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 23742 | GBP | 2023-02-28 | 2024-11-30 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 98911 | GBP | 2023-02-28 | 2023-11-27 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 98911 | GBP | 2023-02-28 | 2024-11-30 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 225209 | GBP | 2023-02-28 | 2024-11-30 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 225209 | GBP | 2023-02-28 | 2023-11-27 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| debtors | 152190 | GBP | 2023-02-28 | 2024-11-30 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 152190 | GBP | 2023-02-28 | 2024-11-30 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-02-28 | 2024-11-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 106108 | GBP | 2023-02-28 | 2024-11-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 106108 | GBP | 2023-02-28 | 2023-11-27 | filed | no | `uk-core:Equity` | micro-entity |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 106008 | GBP | 2023-02-28 | 2024-11-30 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 4386 | GBP | 2023-02-28 | 2023-11-27 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 106108 | GBP | 2023-02-28 | 2024-11-30 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 106108 | GBP | 2023-02-28 | 2023-11-27 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 126298 | GBP | 2023-02-28 | 2024-11-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 126298 | GBP | 2023-02-28 | 2023-11-27 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 130684 | GBP | 2023-02-28 | 2024-11-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 130684 | GBP | 2023-02-28 | 2023-11-27 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 6 | iso4217:GBP | 2022-02-28 | 2023-11-27 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 92821 | GBP | 2022-02-28 | 2023-11-27 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 271997 | GBP | 2022-02-28 | 2023-11-27 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 146135 | GBP | 2022-02-28 | 2023-11-27 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 5225 | GBP | 2022-02-28 | 2023-11-27 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 146135 | GBP | 2022-02-28 | 2023-11-27 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 179176 | GBP | 2022-02-28 | 2023-11-27 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 184401 | GBP | 2022-02-28 | 2023-11-27 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## MICHAEL LYONS ARCHITECTURE LIMITED (`gb:03768963`)

- registration: `03768963` (GB), status active, incorporated 1999-05-12
- classification: ['71129'] (sic_2007)
- records: 10 officers, 3 beneficial owners, 0 ownership statements, 0 security interests, 98 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 10 | xbrli:pure | 2025-03-31 | 2025-12-17 | filed | yes | `d:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 439115 | GBP | 2025-03-31 | 2025-12-17 | filed | yes | `d:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 150418 | GBP | 2025-03-31 | 2025-12-17 | filed | yes | `d:Creditors` | total-exemption-full |
| current_assets | 549473 | GBP | 2025-03-31 | 2025-12-17 | filed | yes | `d:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 88608 | GBP | 2025-03-31 | 2025-12-17 | filed | yes | `d:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1183 | GBP | 2025-03-31 | 2025-12-17 | filed | yes | `d:Equity` | total-exemption-full |
| equity | 407589 | GBP | 2025-03-31 | 2025-12-17 | filed | yes | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 406295 | GBP | 2025-03-31 | 2025-12-17 | filed | yes | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 111 | GBP | 2025-03-31 | 2025-12-17 | filed | yes | `d:Equity` | total-exemption-full |
| fixed_assets | 8534 | GBP | 2025-03-31 | 2025-12-17 | filed | yes | `d:FixedAssets` | total-exemption-full |
| net_assets | 407589 | GBP | 2025-03-31 | 2025-12-17 | filed | yes | `d:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 399055 | GBP | 2025-03-31 | 2025-12-17 | filed | yes | `d:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 407589 | GBP | 2025-03-31 | 2025-12-17 | filed | yes | `d:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 11 | xbrli:pure | 2024-03-31 | 2024-12-10 | filed | no | `d:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 11 | xbrli:pure | 2024-03-31 | 2025-12-17 | filed | yes | `d:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 372249 | GBP | 2024-03-31 | 2025-12-17 | filed | yes | `d:CashBankOnHand` | total-exemption-full |
| cash | 372249 | GBP | 2024-03-31 | 2024-12-10 | filed | no | `d:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 170229 | GBP | 2024-03-31 | 2025-12-17 | filed | yes | `d:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 170229 | GBP | 2024-03-31 | 2024-12-10 | filed | no | `d:Creditors` | total-exemption-full |
| current_assets | 527161 | GBP | 2024-03-31 | 2025-12-17 | filed | yes | `d:CurrentAssets` | total-exemption-full |
| current_assets | 527161 | GBP | 2024-03-31 | 2024-12-10 | filed | no | `d:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 134812 | GBP | 2024-03-31 | 2025-12-17 | filed | yes | `d:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 134812 | GBP | 2024-03-31 | 2024-12-10 | filed | no | `d:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1183 | GBP | 2024-03-31 | 2025-12-17 | filed | yes | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 359340 | GBP | 2024-03-31 | 2024-12-10 | filed | no | `d:Equity` | total-exemption-full |
| equity | 360634 | GBP | 2024-03-31 | 2024-12-10 | filed | no | `d:Equity` | total-exemption-full |
| equity | 360634 | GBP | 2024-03-31 | 2025-12-17 | filed | yes | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1183 | GBP | 2024-03-31 | 2024-12-10 | filed | no | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 359340 | GBP | 2024-03-31 | 2025-12-17 | filed | yes | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 111 | GBP | 2024-03-31 | 2024-12-10 | filed | no | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 111 | GBP | 2024-03-31 | 2025-12-17 | filed | yes | `d:Equity` | total-exemption-full |
| fixed_assets | 3702 | GBP | 2024-03-31 | 2024-12-10 | filed | no | `d:FixedAssets` | total-exemption-full |
| fixed_assets | 3702 | GBP | 2024-03-31 | 2025-12-17 | filed | yes | `d:FixedAssets` | total-exemption-full |
| net_assets | 360634 | GBP | 2024-03-31 | 2024-12-10 | filed | no | `d:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 360634 | GBP | 2024-03-31 | 2025-12-17 | filed | yes | `d:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 356932 | GBP | 2024-03-31 | 2025-12-17 | filed | yes | `d:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 356932 | GBP | 2024-03-31 | 2024-12-10 | filed | no | `d:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 360634 | GBP | 2024-03-31 | 2024-12-10 | filed | no | `d:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 360634 | GBP | 2024-03-31 | 2025-12-17 | filed | yes | `d:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 10 | xbrli:pure | 2023-03-31 | 2024-12-10 | filed | yes | `d:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 10 | xbrli:pure | 2023-03-31 | 2023-12-01 | filed | no | `d:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 331284 | GBP | 2023-03-31 | 2024-12-10 | filed | yes | `d:CashBankOnHand` | total-exemption-full |
| cash | 331284 | GBP | 2023-03-31 | 2023-12-01 | filed | no | `d:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 112101 | GBP | 2023-03-31 | 2023-12-01 | filed | no | `d:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 112101 | GBP | 2023-03-31 | 2024-12-10 | filed | yes | `d:Creditors` | total-exemption-full |
| current_assets | 387842 | GBP | 2023-03-31 | 2024-12-10 | filed | yes | `d:CurrentAssets` | total-exemption-full |
| current_assets | 387842 | GBP | 2023-03-31 | 2023-12-01 | filed | no | `d:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 36458 | GBP | 2023-03-31 | 2024-12-10 | filed | yes | `d:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 36458 | GBP | 2023-03-31 | 2023-12-01 | filed | no | `d:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 111 | GBP | 2023-03-31 | 2023-12-01 | filed | no | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1006 | GBP | 2023-03-31 | 2023-12-01 | filed | no | `d:Equity` | total-exemption-full |
| equity | 279630 | GBP | 2023-03-31 | 2024-12-10 | filed | yes | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1006 | GBP | 2023-03-31 | 2024-12-10 | filed | yes | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 278513 | GBP | 2023-03-31 | 2023-12-01 | filed | no | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 278513 | GBP | 2023-03-31 | 2024-12-10 | filed | yes | `d:Equity` | total-exemption-full |
| equity | 279630 | GBP | 2023-03-31 | 2023-12-01 | filed | no | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 111 | GBP | 2023-03-31 | 2024-12-10 | filed | yes | `d:Equity` | total-exemption-full |
| fixed_assets | 3889 | GBP | 2023-03-31 | 2023-12-01 | filed | no | `d:FixedAssets` | total-exemption-full |
| fixed_assets | 3889 | GBP | 2023-03-31 | 2024-12-10 | filed | yes | `d:FixedAssets` | total-exemption-full |
| net_assets | 279630 | GBP | 2023-03-31 | 2024-12-10 | filed | yes | `d:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 279630 | GBP | 2023-03-31 | 2023-12-01 | filed | no | `d:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 275741 | GBP | 2023-03-31 | 2023-12-01 | filed | no | `d:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 275741 | GBP | 2023-03-31 | 2024-12-10 | filed | yes | `d:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 279630 | GBP | 2023-03-31 | 2023-12-01 | filed | no | `d:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 279630 | GBP | 2023-03-31 | 2024-12-10 | filed | yes | `d:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 12 | xbrli:pure | 2022-03-31 | 2023-12-01 | filed | yes | `d:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 375619 | GBP | 2022-03-31 | 2023-12-01 | filed | yes | `d:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 112660 | GBP | 2022-03-31 | 2023-12-01 | filed | yes | `d:Creditors` | total-exemption-full |
| current_assets | 410746 | GBP | 2022-03-31 | 2023-12-01 | filed | yes | `d:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 26487 | GBP | 2022-03-31 | 2023-12-01 | filed | yes | `d:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1006 | GBP | 2022-03-31 | 2023-12-01 | filed | yes | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 301669 | GBP | 2022-03-31 | 2023-12-01 | filed | yes | `d:Equity` | total-exemption-full |
| equity | 302786 | GBP | 2022-03-31 | 2023-12-01 | filed | yes | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 111 | GBP | 2022-03-31 | 2023-12-01 | filed | yes | `d:Equity` | total-exemption-full |
| fixed_assets | 4700 | GBP | 2022-03-31 | 2023-12-01 | filed | yes | `d:FixedAssets` | total-exemption-full |
| net_assets | 302786 | GBP | 2022-03-31 | 2023-12-01 | filed | yes | `d:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 298086 | GBP | 2022-03-31 | 2023-12-01 | filed | yes | `d:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 302786 | GBP | 2022-03-31 | 2023-12-01 | filed | yes | `d:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

Coverage @ 2025-03-31: 10/21 concepts available (average_employees, cash, creditors_within_one_year, current_assets, debtors, equity, fixed_assets, net_assets, net_current_assets, total_assets_less_current_liabilities)
- `creditors_after_one_year`: filed_without_concept — absent though regime 'total-exemption-full' typically includes it
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
