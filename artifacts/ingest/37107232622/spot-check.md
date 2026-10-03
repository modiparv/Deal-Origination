# Ingest spot-check

- database: `data/engine.db`
- latest run: `20261003T074253Z-67b36376`
- companies in store: 17800; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## COMPATIBILITY LIMITED (`gb:01964830`)

- registration: `01964830` (GB), status active, incorporated 1985-11-26
- classification: ['47410', '62090', '77330', '95110'] (sic_2007)
- records: 8 officers, 2 beneficial owners, 0 ownership statements, 3 security interests, 131 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 13 | xbrli:pure | 2025-06-30 | 2026-03-31 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 96057 | GBP | 2025-06-30 | 2026-03-31 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 304656 | GBP | 2025-06-30 | 2026-03-31 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 185755 | GBP | 2025-06-30 | 2026-03-31 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 185755 | GBP | 2025-06-30 | 2026-03-31 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 219820 | GBP | 2025-06-30 | 2026-03-31 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 5129 | GBP | 2025-06-30 | 2026-03-31 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 212361 | GBP | 2025-06-30 | 2026-03-31 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2328 | GBP | 2025-06-30 | 2026-03-31 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 2 | GBP | 2025-06-30 | 2026-03-31 | filed | yes | `ns5:Equity` | total-exemption-full |
| fixed_assets | 400992 | GBP | 2025-06-30 | 2026-03-31 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| net_assets | 219820 | GBP | 2025-06-30 | 2026-03-31 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 38708 | GBP | 2025-06-30 | 2026-03-31 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 88025 | GBP | 2025-06-30 | 2026-03-31 | filed | yes | `ns5:ProfitLoss` | total-exemption-full |
| profit_for_period | 88025 | GBP | 2025-06-30 | 2026-03-31 | filed | yes | `ns5:ProfitLoss` | total-exemption-full |
| total_assets_less_current_liabilities | 439700 | GBP | 2025-06-30 | 2026-03-31 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 14 | xbrli:pure | 2024-06-30 | 2026-03-31 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 14 | xbrli:pure | 2024-06-30 | 2025-03-31 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 81949 | GBP | 2024-06-30 | 2025-03-31 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 81949 | GBP | 2024-06-30 | 2026-03-31 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 296709 | GBP | 2024-06-30 | 2025-03-31 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 296709 | GBP | 2024-06-30 | 2026-03-31 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 190236 | GBP | 2024-06-30 | 2026-03-31 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 190236 | GBP | 2024-06-30 | 2025-03-31 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 190236 | GBP | 2024-06-30 | 2025-03-31 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 190236 | GBP | 2024-06-30 | 2026-03-31 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 5129 | GBP | 2024-06-30 | 2025-03-31 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 248160 | GBP | 2024-06-30 | 2026-03-31 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 240701 | GBP | 2024-06-30 | 2026-03-31 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 2 | GBP | 2024-06-30 | 2025-03-31 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 2 | GBP | 2024-06-30 | 2026-03-31 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 5129 | GBP | 2024-06-30 | 2026-03-31 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 248160 | GBP | 2024-06-30 | 2025-03-31 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 240701 | GBP | 2024-06-30 | 2025-03-31 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2328 | GBP | 2024-06-30 | 2026-03-31 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2328 | GBP | 2024-06-30 | 2025-03-31 | filed | no | `ns5:Equity` | total-exemption-full |
| fixed_assets | 412739 | GBP | 2024-06-30 | 2026-03-31 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| fixed_assets | 412739 | GBP | 2024-06-30 | 2025-03-31 | filed | no | `ns5:FixedAssets` | total-exemption-full |
| net_assets | 248160 | GBP | 2024-06-30 | 2025-03-31 | filed | no | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 248160 | GBP | 2024-06-30 | 2026-03-31 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 64016 | GBP | 2024-06-30 | 2025-03-31 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 64016 | GBP | 2024-06-30 | 2026-03-31 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_for_period | 42772 | GBP | 2024-06-30 | 2025-03-31 | filed | yes | `ns5:ProfitLoss` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 42772 | GBP | 2024-06-30 | 2025-03-31 | filed | yes | `ns5:ProfitLoss` | total-exemption-full |
| total_assets_less_current_liabilities | 476755 | GBP | 2024-06-30 | 2026-03-31 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 476755 | GBP | 2024-06-30 | 2025-03-31 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 13 | xbrli:pure | 2023-06-30 | 2024-03-28 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 13 | xbrli:pure | 2023-06-30 | 2025-03-31 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 149132 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 149132 | GBP | 2023-06-30 | 2025-03-31 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 394802 | GBP | 2023-06-30 | 2025-03-31 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 394802 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 222062 | GBP | 2023-06-30 | 2025-03-31 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 222062 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 222062 | GBP | 2023-06-30 | 2025-03-31 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 222062 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2328 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 311935 | GBP | 2023-06-30 | 2025-03-31 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 2 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 304476 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 2 | GBP | 2023-06-30 | 2025-03-31 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 311935 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 5129 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 5129 | GBP | 2023-06-30 | 2025-03-31 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2328 | GBP | 2023-06-30 | 2025-03-31 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 304476 | GBP | 2023-06-30 | 2025-03-31 | filed | yes | `ns5:Equity` | total-exemption-full |
| fixed_assets | 412646 | GBP | 2023-06-30 | 2025-03-31 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| fixed_assets | 412646 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `ns5:FixedAssets` | total-exemption-full |
| net_assets | 311935 | GBP | 2023-06-30 | 2025-03-31 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 311935 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 110404 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 110404 | GBP | 2023-06-30 | 2025-03-31 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_for_period | 96168 | GBP | 2023-06-30 | 2024-03-28 | filed | yes | `ns5:ProfitLoss` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 96168 | GBP | 2023-06-30 | 2024-03-28 | filed | yes | `ns5:ProfitLoss` | total-exemption-full |
| total_assets_less_current_liabilities | 523050 | GBP | 2023-06-30 | 2025-03-31 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 523050 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 14 | xbrli:pure | 2022-06-30 | 2024-03-28 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 154723 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 384207 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 203469 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 203469 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 337228 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 329769 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 5129 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 2 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2328 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| fixed_assets | 413617 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| net_assets | 337228 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 146678 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 560295 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## INTERACTIVE TRANSACTION SOLUTIONS LIMITED (`gb:02473364`)

- registration: `02473364` (GB), status active, incorporated 1990-02-22
- classification: ['62020', '63110'] (sic_2007)
- records: 24 officers, 2 beneficial owners, 0 ownership statements, 3 security interests, 163 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.16 | xbrli:pure | 2025-03-31 | 2025-12-16 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 1184618 | GBP | 2025-03-31 | 2025-12-16 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2414371 | GBP | 2025-03-31 | 2025-12-16 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 2950885 | GBP | 2025-03-31 | 2025-12-16 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 1455952 | GBP | 2025-03-31 | 2025-12-16 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1455952 | GBP | 2025-03-31 | 2025-12-16 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 977538 | GBP | 2025-03-31 | 2025-12-16 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2025-03-31 | 2025-12-16 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 976538 | GBP | 2025-03-31 | 2025-12-16 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 977538 | GBP | 2025-03-31 | 2025-12-16 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 536514 | GBP | 2025-03-31 | 2025-12-16 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1070046 | GBP | 2025-03-31 | 2025-12-16 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0.19 | xbrli:pure | 2024-03-31 | 2025-12-16 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 19 | xbrli:pure | 2024-03-31 | 2024-12-13 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 1259185 | GBP | 2024-03-31 | 2024-12-13 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 1259185 | GBP | 2024-03-31 | 2025-12-16 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 893922 | GBP | 2024-03-31 | 2025-12-16 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 893922 | GBP | 2024-03-31 | 2024-12-13 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 1782602 | GBP | 2024-03-31 | 2025-12-16 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 1782602 | GBP | 2024-03-31 | 2024-12-13 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors | 523417 | GBP | 2024-03-31 | 2024-12-13 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 523417 | GBP | 2024-03-31 | 2025-12-16 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 523417 | GBP | 2024-03-31 | 2024-12-13 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 523417 | GBP | 2024-03-31 | 2025-12-16 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 1017303 | GBP | 2024-03-31 | 2024-12-13 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1016303 | GBP | 2024-03-31 | 2024-12-13 | filed | no | `core:Equity` | total-exemption-full |
| equity | 1017303 | GBP | 2024-03-31 | 2025-12-16 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1016303 | GBP | 2024-03-31 | 2025-12-16 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2024-03-31 | 2025-12-16 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2024-03-31 | 2024-12-13 | filed | no | `core:Equity` | total-exemption-full |
| net_assets | 1017303 | GBP | 2024-03-31 | 2025-12-16 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 1017303 | GBP | 2024-03-31 | 2024-12-13 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 888680 | GBP | 2024-03-31 | 2024-12-13 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 888680 | GBP | 2024-03-31 | 2025-12-16 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1017303 | GBP | 2024-03-31 | 2025-12-16 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1017303 | GBP | 2024-03-31 | 2024-12-13 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 26 | xbrli:pure | 2023-03-31 | 2023-12-12 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 26 | xbrli:pure | 2023-03-31 | 2024-12-13 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 1029909 | GBP | 2023-03-31 | 2023-12-12 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 1029909 | GBP | 2023-03-31 | 2024-12-13 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 778987 | GBP | 2023-03-31 | 2024-12-13 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 778987 | GBP | 2023-03-31 | 2023-12-12 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 1511240 | GBP | 2023-03-31 | 2024-12-13 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 1511240 | GBP | 2023-03-31 | 2023-12-12 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors | 481331 | GBP | 2023-03-31 | 2024-12-13 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 481331 | GBP | 2023-03-31 | 2024-12-13 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 481331 | GBP | 2023-03-31 | 2023-12-12 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 481331 | GBP | 2023-03-31 | 2023-12-12 | filed | no | `core:Debtors` | total-exemption-full |
| equity | 908173 | GBP | 2023-03-31 | 2024-12-13 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2023-03-31 | 2024-12-13 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2023-03-31 | 2023-12-12 | filed | no | `core:Equity` | total-exemption-full |
| equity | 908173 | GBP | 2023-03-31 | 2023-12-12 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 907173 | GBP | 2023-03-31 | 2023-12-12 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 907173 | GBP | 2023-03-31 | 2024-12-13 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 908173 | GBP | 2023-03-31 | 2024-12-13 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 908173 | GBP | 2023-03-31 | 2023-12-12 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 732253 | GBP | 2023-03-31 | 2024-12-13 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 732253 | GBP | 2023-03-31 | 2023-12-12 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 949002 | GBP | 2023-03-31 | 2024-12-13 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 949002 | GBP | 2023-03-31 | 2023-12-12 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 26 | xbrli:pure | 2021-12-31 | 2023-12-12 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 1481211 | GBP | 2021-12-31 | 2023-12-12 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 547645 | GBP | 2021-12-31 | 2023-12-12 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 1974063 | GBP | 2021-12-31 | 2023-12-12 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 492852 | GBP | 2021-12-31 | 2023-12-12 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 492852 | GBP | 2021-12-31 | 2023-12-12 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 1756792 | GBP | 2021-12-31 | 2023-12-12 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1755792 | GBP | 2021-12-31 | 2023-12-12 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2021-12-31 | 2023-12-12 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 1756792 | GBP | 2021-12-31 | 2023-12-12 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1426418 | GBP | 2021-12-31 | 2023-12-12 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1797621 | GBP | 2021-12-31 | 2023-12-12 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2025-12-16: `{"superseded_document_id": "gb:02473364:doc:rX-cXLDLacmjFrHNU4IePv7rLjQ5JyIIAlPpBH9RmSQ", "restatements": [{"concept": "average_employees", "period_end": "2024-03-31", "old_value": "19.0000", "new_val`

## QUADGEM LIMITED (`gb:02836580`)

- registration: `02836580` (GB), status active, incorporated 1993-07-15
- classification: ['62020'] (sic_2007)
- records: 5 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 79 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-07-31 | 2026-04-22 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 51584 | GBP | 2025-07-31 | 2026-04-22 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 12087 | GBP | 2025-07-31 | 2026-04-22 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 1774 | GBP | 2025-07-31 | 2026-04-22 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -56472 | GBP | 2025-07-31 | 2026-04-22 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 6475 | GBP | 2025-07-31 | 2026-04-22 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | -56472 | GBP | 2025-07-31 | 2026-04-22 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -10313 | GBP | 2025-07-31 | 2026-04-22 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -3838 | GBP | 2025-07-31 | 2026-04-22 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-07-31 | 2026-04-22 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-07-31 | 2025-03-06 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 47107 | GBP | 2024-07-31 | 2026-04-22 | filed | yes | `core:Creditors` | micro-entity |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 47107 | GBP | 2024-07-31 | 2025-03-06 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 12320 | GBP | 2024-07-31 | 2025-03-06 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 12320 | GBP | 2024-07-31 | 2026-04-22 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 3584 | GBP | 2024-07-31 | 2025-03-06 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 3584 | GBP | 2024-07-31 | 2026-04-22 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -48649 | GBP | 2024-07-31 | 2026-04-22 | filed | yes | `core:Equity` | micro-entity |
| equity | -48649 | GBP | 2024-07-31 | 2025-03-06 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 8094 | GBP | 2024-07-31 | 2025-03-06 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 8094 | GBP | 2024-07-31 | 2026-04-22 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | -48649 | GBP | 2024-07-31 | 2025-03-06 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | -48649 | GBP | 2024-07-31 | 2026-04-22 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -8736 | GBP | 2024-07-31 | 2025-03-06 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -8736 | GBP | 2024-07-31 | 2026-04-22 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -642 | GBP | 2024-07-31 | 2025-03-06 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -642 | GBP | 2024-07-31 | 2026-04-22 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-07-31 | 2025-03-06 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-07-31 | 2024-04-26 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 34110 | GBP | 2023-07-31 | 2025-03-06 | filed | yes | `core:Creditors` | micro-entity |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 4435 | GBP | 2023-07-31 | 2024-04-26 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 42007 | GBP | 2023-07-31 | 2024-04-26 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 12332 | GBP | 2023-07-31 | 2025-03-06 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 6733 | GBP | 2023-07-31 | 2024-04-26 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 6733 | GBP | 2023-07-31 | 2025-03-06 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -34626 | GBP | 2023-07-31 | 2024-04-26 | filed | no | `core:Equity` | micro-entity |
| equity | -34626 | GBP | 2023-07-31 | 2025-03-06 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 5983 | GBP | 2023-07-31 | 2025-03-06 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 5983 | GBP | 2023-07-31 | 2024-04-26 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | -34626 | GBP | 2023-07-31 | 2024-04-26 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | -34626 | GBP | 2023-07-31 | 2025-03-06 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -5599 | GBP | 2023-07-31 | 2025-03-06 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -35274 | GBP | 2023-07-31 | 2024-04-26 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -29291 | GBP | 2023-07-31 | 2024-04-26 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 384 | GBP | 2023-07-31 | 2025-03-06 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2022-07-31 | 2024-04-26 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 6767 | GBP | 2022-07-31 | 2024-04-26 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 28039 | GBP | 2022-07-31 | 2024-04-26 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 6680 | GBP | 2022-07-31 | 2024-04-26 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -25558 | GBP | 2022-07-31 | 2024-04-26 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 2568 | GBP | 2022-07-31 | 2024-04-26 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | -25558 | GBP | 2022-07-31 | 2024-04-26 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -21359 | GBP | 2022-07-31 | 2024-04-26 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -18791 | GBP | 2022-07-31 | 2024-04-26 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2025-03-06: `{"superseded_document_id": "gb:02836580:doc:UJeTsXO-1CDsyHNazhowykokb_yc71ak3mcPrAZm7Q4", "restatements": [{"concept": "creditors_within_one_year", "period_end": "2023-07-31", "old_value": "42007.0000`

## FIELD INTERNATIONAL LIMITED (`gb:03102815`)

- registration: `03102815` (GB), status active, incorporated 1995-09-15
- classification: ['71129'] (sic_2007)
- records: 19 officers, 1 beneficial owners, 0 ownership statements, 15 security interests, 141 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 40 | xbrli:pure | 2024-12-31 | 2025-06-19 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | full |
| cash | 624936 | GBP | 2024-12-31 | 2025-06-19 | filed | yes | `core:CashBankOnHand` | full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 931055 | GBP | 2024-12-31 | 2025-06-19 | filed | yes | `core:Creditors` | full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 3824272 | GBP | 2024-12-31 | 2025-06-19 | filed | yes | `core:Creditors` | full |
| current_assets | 4771648 | GBP | 2024-12-31 | 2025-06-19 | filed | yes | `core:CurrentAssets` | full |
| debtors | 2894028 | GBP | 2024-12-31 | 2025-06-19 | filed | yes | `core:Debtors` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2894028 | GBP | 2024-12-31 | 2025-06-19 | filed | yes | `core:Debtors` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1759629 | GBP | 2024-12-31 | 2025-06-19 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 3 | GBP | 2024-12-31 | 2025-06-19 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 625940 | GBP | 2024-12-31 | 2025-06-19 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 3 | GBP | 2024-12-31 | 2025-06-19 | filed | yes | `core:Equity` | full |
| equity | 2385572 | GBP | 2024-12-31 | 2025-06-19 | filed | yes | `core:Equity` | full |
| fixed_assets | 2369251 | GBP | 2024-12-31 | 2025-06-19 | filed | yes | `core:FixedAssets` | full |
| net_assets | 2385572 | GBP | 2024-12-31 | 2025-06-19 | filed | yes | `core:NetAssetsLiabilities` | full |
| net_current_assets | 947376 | GBP | 2024-12-31 | 2025-06-19 | filed | yes | `core:NetCurrentAssetsLiabilities` | full |
| profit_before_tax | 2373552 | GBP | 2024-12-31 | 2025-06-19 | filed | yes | `core:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period | 2284765 | GBP | 2024-12-31 | 2025-06-19 | filed | yes | `core:ProfitLoss` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2284765 | GBP | 2024-12-31 | 2025-06-19 | filed | yes | `core:ProfitLoss` | full |
| staff_costs | 1854546 | GBP | 2024-12-31 | 2025-06-19 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | full |
| tax_charge | 88787 | GBP | 2024-12-31 | 2025-06-19 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| total_assets_less_current_liabilities | 3316627 | GBP | 2024-12-31 | 2025-06-19 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | full |
| average_employees | 48 | xbrli:pure | 2023-12-31 | 2024-12-11 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | full |
| average_employees | 48 | xbrli:pure | 2023-12-31 | 2025-06-19 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | full |
| cash | 77036 | GBP | 2023-12-31 | 2024-12-11 | filed | no | `core:CashBankOnHand` | full |
| cash | 77036 | GBP | 2023-12-31 | 2025-06-19 | filed | yes | `core:CashBankOnHand` | full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 1053871 | GBP | 2023-12-31 | 2024-12-11 | filed | no | `core:Creditors` | full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 1053871 | GBP | 2023-12-31 | 2025-06-19 | filed | yes | `core:Creditors` | full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5070036 | GBP | 2023-12-31 | 2025-06-19 | filed | yes | `core:Creditors` | full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5070036 | GBP | 2023-12-31 | 2024-12-11 | filed | no | `core:Creditors` | full |
| current_assets | 3950165 | GBP | 2023-12-31 | 2024-12-11 | filed | no | `core:CurrentAssets` | full |
| current_assets | 3950165 | GBP | 2023-12-31 | 2025-06-19 | filed | yes | `core:CurrentAssets` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2555938 | GBP | 2023-12-31 | 2024-12-11 | filed | no | `core:Debtors` | full |
| debtors | 2555938 | GBP | 2023-12-31 | 2025-06-19 | filed | yes | `core:Debtors` | full |
| debtors | 2555938 | GBP | 2023-12-31 | 2024-12-11 | filed | no | `core:Debtors` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2555938 | GBP | 2023-12-31 | 2025-06-19 | filed | yes | `core:Debtors` | full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 295940 | GBP | 2023-12-31 | 2025-06-19 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -525136 | GBP | 2023-12-31 | 2025-06-19 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 3 | GBP | 2023-12-31 | 2024-12-11 | filed | no | `core:Equity` | full |
| equity | -229193 | GBP | 2023-12-31 | 2025-06-19 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 3 | GBP | 2023-12-31 | 2025-06-19 | filed | yes | `core:Equity` | full |
| equity | -229193 | GBP | 2023-12-31 | 2024-12-11 | filed | no | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -525136 | GBP | 2023-12-31 | 2024-12-11 | filed | no | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 295940 | GBP | 2023-12-31 | 2024-12-11 | filed | no | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 3 | GBP | 2023-12-31 | 2025-06-19 | filed | yes | `core:Equity` | full |
| fixed_assets | 1944549 | GBP | 2023-12-31 | 2024-12-11 | filed | no | `core:FixedAssets` | full |
| fixed_assets | 1944549 | GBP | 2023-12-31 | 2025-06-19 | filed | yes | `core:FixedAssets` | full |
| net_assets | -229193 | GBP | 2023-12-31 | 2024-12-11 | filed | no | `core:NetAssetsLiabilities` | full |
| net_assets | -229193 | GBP | 2023-12-31 | 2025-06-19 | filed | yes | `core:NetAssetsLiabilities` | full |
| net_current_assets | -1119871 | GBP | 2023-12-31 | 2024-12-11 | filed | no | `core:NetCurrentAssetsLiabilities` | full |
| net_current_assets | -1119871 | GBP | 2023-12-31 | 2025-06-19 | filed | yes | `core:NetCurrentAssetsLiabilities` | full |
| profit_before_tax | 93637 | GBP | 2023-12-31 | 2024-12-11 | filed | no | `core:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_before_tax | 93637 | GBP | 2023-12-31 | 2025-06-19 | filed | yes | `core:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period | 92748 | GBP | 2023-12-31 | 2024-12-11 | filed | no | `core:ProfitLoss` | full |
| profit_for_period | 92748 | GBP | 2023-12-31 | 2025-06-19 | filed | yes | `core:ProfitLoss` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 92748 | GBP | 2023-12-31 | 2024-12-11 | filed | no | `core:ProfitLoss` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 92748 | GBP | 2023-12-31 | 2025-06-19 | filed | yes | `core:ProfitLoss` | full |
| staff_costs | 1965294 | GBP | 2023-12-31 | 2024-12-11 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | full |
| tax_charge | 889 | GBP | 2023-12-31 | 2025-06-19 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| tax_charge | 889 | GBP | 2023-12-31 | 2024-12-11 | filed | no | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| total_assets_less_current_liabilities | 824678 | GBP | 2023-12-31 | 2024-12-11 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | full |
| total_assets_less_current_liabilities | 824678 | GBP | 2023-12-31 | 2025-06-19 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | full |
| average_employees | 38 | xbrli:pure | 2022-12-31 | 2023-12-20 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | full |
| average_employees | 38 | xbrli:pure | 2022-12-31 | 2024-12-11 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | full |
| cash | 50941 | GBP | 2022-12-31 | 2024-12-11 | filed | yes | `core:CashBankOnHand` | full |
| cash | 50941 | GBP | 2022-12-31 | 2023-12-20 | filed | no | `core:CashBankOnHand` | full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 710423 | GBP | 2022-12-31 | 2024-12-11 | filed | yes | `core:Creditors` | full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 710423 | GBP | 2022-12-31 | 2023-12-20 | filed | no | `core:Creditors` | full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5616916 | GBP | 2022-12-31 | 2023-12-20 | filed | no | `core:Creditors` | full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5616916 | GBP | 2022-12-31 | 2024-12-11 | filed | yes | `core:Creditors` | full |
| current_assets | 4281876 | GBP | 2022-12-31 | 2024-12-11 | filed | yes | `core:CurrentAssets` | full |
| current_assets | 4491372 | GBP | 2022-12-31 | 2023-12-20 | filed | no | `core:CurrentAssets` | full |
| debtors | 2894244 | GBP | 2022-12-31 | 2024-12-11 | filed | yes | `core:Debtors` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2894244 | GBP | 2022-12-31 | 2024-12-11 | filed | yes | `core:Debtors` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2894244 | GBP | 2022-12-31 | 2023-12-20 | filed | no | `core:Debtors` | full |
| debtors | 2894244 | GBP | 2022-12-31 | 2023-12-20 | filed | no | `core:Debtors` | full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 295940 | GBP | 2022-12-31 | 2024-12-11 | filed | no | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 295940 | GBP | 2022-12-31 | 2025-06-19 | filed | yes | `core:Equity` | full |
| equity | -112445 | GBP | 2022-12-31 | 2023-12-20 | filed | no | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 3 | GBP | 2022-12-31 | 2024-12-11 | filed | no | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -408388 | GBP | 2022-12-31 | 2023-12-20 | filed | no | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 3 | GBP | 2022-12-31 | 2023-12-20 | filed | no | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -617884 | GBP | 2022-12-31 | 2025-06-19 | filed | yes | `core:Equity` | full |
| equity | -321941 | GBP | 2022-12-31 | 2024-12-11 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 3 | GBP | 2022-12-31 | 2025-06-19 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 295940 | GBP | 2022-12-31 | 2023-12-20 | filed | no | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -617884 | GBP | 2022-12-31 | 2024-12-11 | filed | no | `core:Equity` | full |
| fixed_assets | 1723522 | GBP | 2022-12-31 | 2023-12-20 | filed | no | `core:FixedAssets` | full |
| fixed_assets | 1723522 | GBP | 2022-12-31 | 2024-12-11 | filed | yes | `core:FixedAssets` | full |
| net_assets | -321941 | GBP | 2022-12-31 | 2024-12-11 | filed | yes | `core:NetAssetsLiabilities` | full |
| net_assets | -112445 | GBP | 2022-12-31 | 2023-12-20 | filed | no | `core:NetAssetsLiabilities` | full |
| net_current_assets | -1125544 | GBP | 2022-12-31 | 2023-12-20 | filed | no | `core:NetCurrentAssetsLiabilities` | full |
| net_current_assets | -1335040 | GBP | 2022-12-31 | 2024-12-11 | filed | yes | `core:NetCurrentAssetsLiabilities` | full |
| profit_before_tax | -778807 | GBP | 2022-12-31 | 2024-12-11 | filed | yes | `core:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_before_tax | -569311 | GBP | 2022-12-31 | 2023-12-20 | filed | no | `core:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period | -335050 | GBP | 2022-12-31 | 2023-12-20 | filed | no | `core:ProfitLoss` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -544546 | GBP | 2022-12-31 | 2024-12-11 | filed | yes | `core:ProfitLoss` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -335050 | GBP | 2022-12-31 | 2023-12-20 | filed | no | `core:ProfitLoss` | full |
| profit_for_period | -544546 | GBP | 2022-12-31 | 2024-12-11 | filed | yes | `core:ProfitLoss` | full |
| staff_costs | 1317700 | GBP | 2022-12-31 | 2023-12-20 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | full |
| tax_charge | -234261 | GBP | 2022-12-31 | 2024-12-11 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| tax_charge | -234261 | GBP | 2022-12-31 | 2023-12-20 | filed | no | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| total_assets_less_current_liabilities | 597978 | GBP | 2022-12-31 | 2023-12-20 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | full |
| total_assets_less_current_liabilities | 388482 | GBP | 2022-12-31 | 2024-12-11 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | full |
| average_employees | 24 | xbrli:pure | 2021-12-31 | 2023-12-20 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | full |
| cash | 207470 | GBP | 2021-12-31 | 2023-12-20 | filed | yes | `core:CashBankOnHand` | full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 745844 | GBP | 2021-12-31 | 2023-12-20 | filed | yes | `core:Creditors` | full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 3305125 | GBP | 2021-12-31 | 2023-12-20 | filed | yes | `core:Creditors` | full |
| current_assets | 2829298 | GBP | 2021-12-31 | 2023-12-20 | filed | yes | `core:CurrentAssets` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1907883 | GBP | 2021-12-31 | 2023-12-20 | filed | yes | `core:Debtors` | full |
| debtors | 1907883 | GBP | 2021-12-31 | 2023-12-20 | filed | yes | `core:Debtors` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 3 | GBP | 2021-12-31 | 2023-12-20 | filed | no | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 295940 | GBP | 2021-12-31 | 2024-12-11 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 295940 | GBP | 2021-12-31 | 2023-12-20 | filed | no | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 3 | GBP | 2021-12-31 | 2024-12-11 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -73338 | GBP | 2021-12-31 | 2024-12-11 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -73338 | GBP | 2021-12-31 | 2023-12-20 | filed | no | `core:Equity` | full |
| equity | 222605 | GBP | 2021-12-31 | 2023-12-20 | filed | yes | `core:Equity` | full |
| fixed_assets | 1444276 | GBP | 2021-12-31 | 2023-12-20 | filed | yes | `core:FixedAssets` | full |
| net_assets | 222605 | GBP | 2021-12-31 | 2023-12-20 | filed | yes | `core:NetAssetsLiabilities` | full |
| net_current_assets | -475827 | GBP | 2021-12-31 | 2023-12-20 | filed | yes | `core:NetCurrentAssetsLiabilities` | full |
| profit_before_tax | -152976 | GBP | 2021-12-31 | 2023-12-20 | filed | yes | `core:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -177675 | GBP | 2021-12-31 | 2023-12-20 | filed | yes | `core:ProfitLoss` | full |
| profit_for_period | -177675 | GBP | 2021-12-31 | 2023-12-20 | filed | yes | `core:ProfitLoss` | full |
| tax_charge | 24699 | GBP | 2021-12-31 | 2023-12-20 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| total_assets_less_current_liabilities | 968449 | GBP | 2021-12-31 | 2023-12-20 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 150000 | GBP | 2020-12-31 | 2023-12-20 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 354337 | GBP | 2020-12-31 | 2023-12-20 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 3 | GBP | 2020-12-31 | 2023-12-20 | filed | yes | `core:Equity` | full |

_No coverage facts for the latest run._

- event restatement @ 2024-12-11: `{"superseded_document_id": "gb:03102815:doc:mjaB592PRoZaiyA5lkpXMancGdmUepNjNRdkuZZVm3M", "restatements": [{"concept": "equity", "period_end": "2022-12-31", "old_value": "-408388.0000", "new_value": "`

## APPLIED BUSINESS COMPUTERS LIMITED (`gb:03319135`)

- registration: `03319135` (GB), status active, incorporated 1997-02-17
- classification: ['62090'] (sic_2007)
- records: 8 officers, 3 beneficial owners, 0 ownership statements, 1 security interests, 83 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 10 | xbrli:pure | 2025-03-31 | 2025-12-22 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 49563 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 1769 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 370543 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 393612 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 344049 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 21300 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 21150 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 150 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 21300 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 23069 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 23069 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 9 | xbrli:pure | 2024-03-31 | 2025-12-22 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 9 | xbrli:pure | 2024-03-31 | 2024-12-12 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 31194 | GBP | 2024-03-31 | 2024-12-12 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 31194 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 12237 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 12237 | GBP | 2024-03-31 | 2024-12-12 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 358482 | GBP | 2024-03-31 | 2024-12-12 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 358482 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 333081 | GBP | 2024-03-31 | 2024-12-12 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 333081 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 301887 | GBP | 2024-03-31 | 2024-12-12 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 301887 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | -37638 | GBP | 2024-03-31 | 2024-12-12 | filed | no | `core:Equity` | total-exemption-full |
| equity | -37638 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -37788 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -37788 | GBP | 2024-03-31 | 2024-12-12 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 150 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 150 | GBP | 2024-03-31 | 2024-12-12 | filed | no | `core:Equity` | total-exemption-full |
| net_assets | -37638 | GBP | 2024-03-31 | 2024-12-12 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | -37638 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -25401 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -25401 | GBP | 2024-03-31 | 2024-12-12 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -25401 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -25401 | GBP | 2024-03-31 | 2024-12-12 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 9 | xbrli:pure | 2023-03-31 | 2023-12-27 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 9 | xbrli:pure | 2023-03-31 | 2024-12-12 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 17644 | GBP | 2023-03-31 | 2023-12-27 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 17644 | GBP | 2023-03-31 | 2024-12-12 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 22450 | GBP | 2023-03-31 | 2024-12-12 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 22450 | GBP | 2023-03-31 | 2023-12-27 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 299374 | GBP | 2023-03-31 | 2023-12-27 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 299374 | GBP | 2023-03-31 | 2024-12-12 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 293054 | GBP | 2023-03-31 | 2023-12-27 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 293054 | GBP | 2023-03-31 | 2024-12-12 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 275410 | GBP | 2023-03-31 | 2023-12-27 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 275410 | GBP | 2023-03-31 | 2024-12-12 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | -28770 | GBP | 2023-03-31 | 2024-12-12 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 150 | GBP | 2023-03-31 | 2024-12-12 | filed | yes | `core:Equity` | total-exemption-full |
| equity | -28770 | GBP | 2023-03-31 | 2023-12-27 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -28920 | GBP | 2023-03-31 | 2024-12-12 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -28920 | GBP | 2023-03-31 | 2023-12-27 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 150 | GBP | 2023-03-31 | 2023-12-27 | filed | no | `core:Equity` | total-exemption-full |
| net_assets | -28770 | GBP | 2023-03-31 | 2023-12-27 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | -28770 | GBP | 2023-03-31 | 2024-12-12 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -6320 | GBP | 2023-03-31 | 2024-12-12 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -6320 | GBP | 2023-03-31 | 2023-12-27 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -6320 | GBP | 2023-03-31 | 2024-12-12 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -6320 | GBP | 2023-03-31 | 2023-12-27 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 9 | xbrli:pure | 2022-03-31 | 2023-12-27 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 33760 | GBP | 2022-03-31 | 2023-12-27 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 32408 | GBP | 2022-03-31 | 2023-12-27 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 226805 | GBP | 2022-03-31 | 2023-12-27 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 247835 | GBP | 2022-03-31 | 2023-12-27 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 214075 | GBP | 2022-03-31 | 2023-12-27 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | -11378 | GBP | 2022-03-31 | 2023-12-27 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -11528 | GBP | 2022-03-31 | 2023-12-27 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 150 | GBP | 2022-03-31 | 2023-12-27 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | -11378 | GBP | 2022-03-31 | 2023-12-27 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 21030 | GBP | 2022-03-31 | 2023-12-27 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 21030 | GBP | 2022-03-31 | 2023-12-27 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## GLOBAL 4 COMMUNICATIONS LIMITED (`gb:03526932`)

- registration: `03526932` (GB), status active, incorporated 1998-03-13
- classification: ['61900', '62020'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 11 security interests, 153 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## ACORN LUXURY CARE LIMITED (`gb:03716938`)

- registration: `03716938` (GB), status active, incorporated 1999-02-22
- classification: ['86102', '87100'] (sic_2007)
- records: 5 officers, 2 beneficial owners, 0 ownership statements, 4 security interests, 89 filings, 2 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 26 | iso4217:GBP | 2025-03-31 | 2026-03-31 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 12181 | GBP | 2025-03-31 | 2026-03-31 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 43885 | GBP | 2025-03-31 | 2026-03-31 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 232484 | GBP | 2025-03-31 | 2026-03-31 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 548363 | GBP | 2025-03-31 | 2026-03-31 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 536182 | GBP | 2025-03-31 | 2026-03-31 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 492136 | GBP | 2025-03-31 | 2026-03-31 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 492138 | GBP | 2025-03-31 | 2026-03-31 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2025-03-31 | 2026-03-31 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 220144 | GBP | 2025-03-31 | 2026-03-31 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | 492138 | GBP | 2025-03-31 | 2026-03-31 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 315879 | GBP | 2025-03-31 | 2026-03-31 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 536023 | GBP | 2025-03-31 | 2026-03-31 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 33 | iso4217:GBP | 2024-03-31 | 2026-03-31 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 0 | iso4217:GBP | 2024-03-31 | 2025-03-31 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 33922 | GBP | 2024-03-31 | 2026-03-31 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 33922 | GBP | 2024-03-31 | 2025-03-31 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 36975 | GBP | 2024-03-31 | 2025-03-31 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 36975 | GBP | 2024-03-31 | 2026-03-31 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 270659 | GBP | 2024-03-31 | 2026-03-31 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 270659 | GBP | 2024-03-31 | 2025-03-31 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 550017 | GBP | 2024-03-31 | 2025-03-31 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 550017 | GBP | 2024-03-31 | 2026-03-31 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 516095 | GBP | 2024-03-31 | 2025-03-31 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 516095 | GBP | 2024-03-31 | 2026-03-31 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 470873 | GBP | 2024-03-31 | 2026-03-31 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 470875 | GBP | 2024-03-31 | 2026-03-31 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-03-31 | 2026-03-31 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 470873 | GBP | 2024-03-31 | 2025-03-31 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-03-31 | 2025-03-31 | filed | no | `core:Equity` | total-exemption-full |
| equity | 470875 | GBP | 2024-03-31 | 2025-03-31 | filed | no | `core:Equity` | total-exemption-full |
| fixed_assets | 228492 | GBP | 2024-03-31 | 2026-03-31 | filed | yes | `core:FixedAssets` | total-exemption-full |
| fixed_assets | 228492 | GBP | 2024-03-31 | 2025-03-31 | filed | no | `core:FixedAssets` | total-exemption-full |
| net_assets | 470875 | GBP | 2024-03-31 | 2026-03-31 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 470875 | GBP | 2024-03-31 | 2025-03-31 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 279358 | GBP | 2024-03-31 | 2025-03-31 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 279358 | GBP | 2024-03-31 | 2026-03-31 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 507850 | GBP | 2024-03-31 | 2026-03-31 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 507850 | GBP | 2024-03-31 | 2025-03-31 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 33 | iso4217:GBP | 2023-03-31 | 2025-03-31 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 33 | iso4217:GBP | 2023-03-31 | 2024-03-31 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 11247 | GBP | 2023-03-31 | 2025-03-31 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 11187 | GBP | 2023-03-31 | 2024-03-31 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 23451 | GBP | 2023-03-31 | 2025-03-31 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 23451 | GBP | 2023-03-31 | 2024-03-31 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 273297 | GBP | 2023-03-31 | 2024-03-31 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 273297 | GBP | 2023-03-31 | 2025-03-31 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 511795 | GBP | 2023-03-31 | 2025-03-31 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 511795 | GBP | 2023-03-31 | 2024-03-31 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors | 500548 | GBP | 2023-03-31 | 2025-03-31 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 500608 | GBP | 2023-03-31 | 2024-03-31 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 454667 | GBP | 2023-03-31 | 2024-03-31 | filed | no | `core:Equity` | total-exemption-full |
| equity | 454669 | GBP | 2023-03-31 | 2025-03-31 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 454667 | GBP | 2023-03-31 | 2025-03-31 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-03-31 | 2024-03-31 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-03-31 | 2025-03-31 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 454669 | GBP | 2023-03-31 | 2024-03-31 | filed | no | `core:Equity` | total-exemption-full |
| fixed_assets | 239622 | GBP | 2023-03-31 | 2025-03-31 | filed | yes | `core:FixedAssets` | total-exemption-full |
| fixed_assets | 239622 | GBP | 2023-03-31 | 2024-03-31 | filed | no | `core:FixedAssets` | total-exemption-full |
| net_assets | 454669 | GBP | 2023-03-31 | 2024-03-31 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 454669 | GBP | 2023-03-31 | 2025-03-31 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 238498 | GBP | 2023-03-31 | 2025-03-31 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 238498 | GBP | 2023-03-31 | 2024-03-31 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 478120 | GBP | 2023-03-31 | 2024-03-31 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 478120 | GBP | 2023-03-31 | 2025-03-31 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 32 | iso4217:GBP | 2022-03-31 | 2024-03-31 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 190 | GBP | 2022-03-31 | 2024-03-31 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 22991 | GBP | 2022-03-31 | 2024-03-31 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 284854 | GBP | 2022-03-31 | 2024-03-31 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 493484 | GBP | 2022-03-31 | 2024-03-31 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 493294 | GBP | 2022-03-31 | 2024-03-31 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2022-03-31 | 2024-03-31 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 432575 | GBP | 2022-03-31 | 2024-03-31 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 432577 | GBP | 2022-03-31 | 2024-03-31 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 246938 | GBP | 2022-03-31 | 2024-03-31 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | 432577 | GBP | 2022-03-31 | 2024-03-31 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 208630 | GBP | 2022-03-31 | 2024-03-31 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 455568 | GBP | 2022-03-31 | 2024-03-31 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2025-03-31: `{"superseded_document_id": "gb:03716938:doc:CPg8XLcbgjM_KT2YytXq87huRLToTsjmSSqpTgkyrBE", "restatements": [{"concept": "debtors", "period_end": "2023-03-31", "old_value": "500608.0000", "new_value": "`
- event restatement @ 2026-03-31: `{"superseded_document_id": "gb:03716938:doc:9MbDFKYp4JXxJT7tw1B-8fnq27AyxBHDusGMuGZEjcQ", "restatements": [{"concept": "average_employees", "period_end": "2024-03-31", "old_value": "0.0000", "new_valu`

## MATT HEMBER LIMITED (`gb:03915213`)

- registration: `03915213` (GB), status active, incorporated 2000-01-28
- classification: ['62020'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 59 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | iso4217:GBP | 2025-03-31 | 2025-12-29 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2025-03-31 | 2025-12-29 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2025-03-31 | 2025-12-29 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 33582 | GBP | 2025-03-31 | 2025-12-29 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 13833 | GBP | 2025-03-31 | 2025-12-29 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2025-03-31 | 2025-12-29 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 13833 | GBP | 2025-03-31 | 2025-12-29 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 33582 | GBP | 2025-03-31 | 2025-12-29 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 33582 | GBP | 2025-03-31 | 2025-12-29 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-03-31 | 2025-12-29 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2024-03-31 | 2025-12-29 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2024-03-31 | 2025-12-29 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 16120 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 23895 | GBP | 2024-03-31 | 2025-12-29 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 23896 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 7776 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:Equity` | micro-entity |
| equity | 7518 | GBP | 2024-03-31 | 2025-12-29 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2024-03-31 | 2025-12-29 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 7518 | GBP | 2024-03-31 | 2025-12-29 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 7776 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 7776 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 23895 | GBP | 2024-03-31 | 2025-12-29 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 7776 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 23895 | GBP | 2024-03-31 | 2025-12-29 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-03-31 | 2023-12-20 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 25169 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 25169 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 35322 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 35322 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 10153 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:Equity` | micro-entity |
| equity | 10153 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `core:Equity` | micro-entity |
| net_assets | 10153 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 10153 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 10153 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 10153 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 10153 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 10153 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 15131 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 23614 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 8483 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `core:Equity` | micro-entity |
| net_assets | 8483 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 8483 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 8483 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2025-12-29: `{"superseded_document_id": "gb:03915213:doc:98iU-d-Gw1N8PLwLcI_Ec_L-dePzZPPHdwTGHbceOcg", "restatements": [{"concept": "current_assets", "period_end": "2024-03-31", "old_value": "23896.0000", "new_val`

## AZENTA UK LTD (`gb:04109439`)

- registration: `04109439` (GB), status active, incorporated 2000-11-16
- classification: ['26511', '27900', '62090'] (sic_2007)
- records: 25 officers, 1 beneficial owners, 0 ownership statements, 6 security interests, 132 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._
