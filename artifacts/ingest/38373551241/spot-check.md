# Ingest spot-check

- database: `data/engine.db`
- latest run: `20261013T090342Z-caffcf54`
- companies in store: 25800; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## PAYHALL CONSULTING LIMITED (`gb:02219376`)

- registration: `02219376` (GB), status active, incorporated 1988-02-09
- classification: ['71111'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 95 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-03-31 | 2025-12-11 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 89846 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 104030 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 14184 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 14184 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 59925 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 58925 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 59925 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 56542 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 60382 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `ns5:ProfitLoss` | total-exemption-full |
| total_assets_less_current_liabilities | 60860 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-03-31 | 2024-09-11 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| average_employees | 1 | xbrli:pure | 2024-03-31 | 2025-12-11 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 45755 | GBP | 2024-03-31 | 2024-09-11 | filed | no | `ns5:CashBankOnHand` | unaudited-abridged |
| cash | 45755 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 59053 | GBP | 2024-03-31 | 2024-09-11 | filed | no | `ns5:CurrentAssets` | unaudited-abridged |
| current_assets | 59053 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 13298 | GBP | 2024-03-31 | 2024-09-11 | filed | no | `ns5:Debtors` | unaudited-abridged |
| debtors | 13298 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 13298 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 28543 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2024-03-31 | 2024-09-11 | filed | no | `ns5:Equity` | unaudited-abridged |
| equity | 29543 | GBP | 2024-03-31 | 2024-09-11 | filed | no | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 29543 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 28543 | GBP | 2024-03-31 | 2024-09-11 | filed | no | `ns5:Equity` | unaudited-abridged |
| net_assets | 29543 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 29543 | GBP | 2024-03-31 | 2024-09-11 | filed | no | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 26580 | GBP | 2024-03-31 | 2024-09-11 | filed | no | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 26580 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 30553 | GBP | 2024-03-31 | 2024-09-11 | filed | yes | `ns5:ProfitLoss` | unaudited-abridged |
| total_assets_less_current_liabilities | 30238 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 30238 | GBP | 2024-03-31 | 2024-09-11 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 1 | xbrli:pure | 2023-03-31 | 2024-09-11 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 1 | xbrli:pure | 2023-03-31 | 2023-09-26 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 29309 | GBP | 2023-03-31 | 2023-09-26 | filed | yes | `ns5:CashBankOnHand` | unaudited-abridged |
| cash | 29309 | GBP | 2023-03-31 | 2024-09-11 | filed | yes | `ns5:CashBankOnHand` | unaudited-abridged |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 41927 | GBP | 2023-03-31 | 2023-09-26 | filed | yes | `ns5:CurrentAssets` | unaudited-abridged |
| current_assets | 41927 | GBP | 2023-03-31 | 2024-09-11 | filed | yes | `ns5:CurrentAssets` | unaudited-abridged |
| debtors `{'OriginalRevisedDataDimension': 'Original'}` | 12618 | GBP | 2023-03-31 | 2023-09-26 | filed | yes | `ns5:Debtors` | unaudited-abridged |
| debtors | 12618 | GBP | 2023-03-31 | 2024-09-11 | filed | yes | `ns5:Debtors` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 27990 | GBP | 2023-03-31 | 2024-09-11 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity | 28990 | GBP | 2023-03-31 | 2024-09-11 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 1000 | GBP | 2023-03-31 | 2023-09-26 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2023-03-31 | 2024-09-11 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 28990 | GBP | 2023-03-31 | 2023-09-26 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 27990 | GBP | 2023-03-31 | 2023-09-26 | filed | yes | `ns5:Equity` | unaudited-abridged |
| net_assets | 28990 | GBP | 2023-03-31 | 2024-09-11 | filed | yes | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_assets `{'OriginalRevisedDataDimension': 'Original'}` | 28990 | GBP | 2023-03-31 | 2023-09-26 | filed | yes | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 26069 | GBP | 2023-03-31 | 2023-09-26 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 26069 | GBP | 2023-03-31 | 2024-09-11 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| profit_for_period `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 22644 | GBP | 2023-03-31 | 2023-09-26 | filed | yes | `ns5:ProfitLoss` | unaudited-abridged |
| total_assets_less_current_liabilities | 29963 | GBP | 2023-03-31 | 2024-09-11 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 29963 | GBP | 2023-03-31 | 2023-09-26 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 1 | xbrli:pure | 2022-03-31 | 2023-09-26 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 27427 | GBP | 2022-03-31 | 2023-09-26 | filed | yes | `ns5:CashBankOnHand` | unaudited-abridged |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 40064 | GBP | 2022-03-31 | 2023-09-26 | filed | yes | `ns5:CurrentAssets` | unaudited-abridged |
| debtors `{'OriginalRevisedDataDimension': 'Original'}` | 12637 | GBP | 2022-03-31 | 2023-09-26 | filed | yes | `ns5:Debtors` | unaudited-abridged |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 30346 | GBP | 2022-03-31 | 2023-09-26 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 31346 | GBP | 2022-03-31 | 2023-09-26 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 1000 | GBP | 2022-03-31 | 2023-09-26 | filed | yes | `ns5:Equity` | unaudited-abridged |
| net_assets `{'OriginalRevisedDataDimension': 'Original'}` | 31346 | GBP | 2022-03-31 | 2023-09-26 | filed | yes | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 30271 | GBP | 2022-03-31 | 2023-09-26 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 31598 | GBP | 2022-03-31 | 2023-09-26 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |

_No coverage facts for the latest run._

## ST BENEDICT'S HOSPICE, SUNDERLAND (`gb:02803974`)

- registration: `02803974` (GB), status active, incorporated 1993-03-26
- classification: ['86101'] (sic_2007)
- records: 55 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 185 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 26 | xbrli:pure | 2025-03-31 | 2025-12-22 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | full |
| average_employees | 24 | xbrli:pure | 2024-03-31 | 2025-12-22 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | full |

_No coverage facts for the latest run._

## STARFIRST LIMITED (`gb:03181002`)

- registration: `03181002` (GB), status active, incorporated 1996-04-01
- classification: ['62012', '62020', '62090', '70229'] (sic_2007)
- records: 8 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 84 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | xbrli:pure | 2025-04-30 | 2026-01-26 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 20567 | GBP | 2025-04-30 | 2026-01-26 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| equity | 16479 | GBP | 2025-04-30 | 2026-01-26 | filed | yes | `frs-core:Equity` | micro-entity |
| net_assets | 16479 | GBP | 2025-04-30 | 2026-01-26 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 16659 | GBP | 2025-04-30 | 2026-01-26 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 16659 | GBP | 2025-04-30 | 2026-01-26 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2024-04-30 | 2026-01-26 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | xbrli:pure | 2024-04-30 | 2025-01-28 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 20533 | GBP | 2024-04-30 | 2026-01-26 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| current_assets | 20533 | GBP | 2024-04-30 | 2025-01-28 | filed | no | `frs-core:CurrentAssets` | micro-entity |
| equity | 16479 | GBP | 2024-04-30 | 2026-01-26 | filed | yes | `frs-core:Equity` | micro-entity |
| equity | 16479 | GBP | 2024-04-30 | 2025-01-28 | filed | no | `frs-core:Equity` | micro-entity |
| net_assets | 16479 | GBP | 2024-04-30 | 2026-01-26 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 16479 | GBP | 2024-04-30 | 2025-01-28 | filed | no | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 16659 | GBP | 2024-04-30 | 2025-01-28 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 16659 | GBP | 2024-04-30 | 2026-01-26 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 16659 | GBP | 2024-04-30 | 2025-01-28 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 16659 | GBP | 2024-04-30 | 2026-01-26 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2023-04-30 | 2025-01-28 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | xbrli:pure | 2023-04-30 | 2024-01-29 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 20528 | GBP | 2023-04-30 | 2024-01-29 | filed | no | `frs-core:CurrentAssets` | micro-entity |
| current_assets | 20528 | GBP | 2023-04-30 | 2025-01-28 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| equity | 16474 | GBP | 2023-04-30 | 2024-01-29 | filed | no | `frs-core:Equity` | micro-entity |
| equity | 16474 | GBP | 2023-04-30 | 2025-01-28 | filed | yes | `frs-core:Equity` | micro-entity |
| net_assets | 16474 | GBP | 2023-04-30 | 2025-01-28 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 16474 | GBP | 2023-04-30 | 2024-01-29 | filed | no | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 16654 | GBP | 2023-04-30 | 2025-01-28 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 16654 | GBP | 2023-04-30 | 2024-01-29 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 16654 | GBP | 2023-04-30 | 2024-01-29 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 16654 | GBP | 2023-04-30 | 2025-01-28 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2022-04-30 | 2024-01-29 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 20665 | GBP | 2022-04-30 | 2024-01-29 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| equity | 16611 | GBP | 2022-04-30 | 2024-01-29 | filed | yes | `frs-core:Equity` | micro-entity |
| net_assets | 16611 | GBP | 2022-04-30 | 2024-01-29 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 16791 | GBP | 2022-04-30 | 2024-01-29 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 16791 | GBP | 2022-04-30 | 2024-01-29 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## THE SIDMOUTH DESIGN COMPANY LIMITED (`gb:03487793`)

- registration: `03487793` (GB), status active, incorporated 1998-01-02
- classification: ['47599', '71111', '74100'] (sic_2007)
- records: 6 officers, 1 beneficial owners, 0 ownership statements, 1 security interests, 85 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.04 | xbrli:pure | 2025-03-31 | 2025-12-24 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 222406 | GBP | 2025-03-31 | 2025-12-24 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| current_assets | 380070 | GBP | 2025-03-31 | 2025-12-24 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 96498 | GBP | 2025-03-31 | 2025-12-24 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 96498 | GBP | 2025-03-31 | 2025-12-24 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | -10987 | GBP | 2025-03-31 | 2025-12-24 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 8483 | GBP | 2025-03-31 | 2025-12-24 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 5050 | GBP | 2025-03-31 | 2025-12-24 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 338429 | GBP | 2025-03-31 | 2025-12-24 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 335883 | GBP | 2025-03-31 | 2025-12-24 | filed | yes | `core:Equity` | total-exemption-full |
| net_current_assets | 336018 | GBP | 2025-03-31 | 2025-12-24 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 338429 | GBP | 2025-03-31 | 2025-12-24 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 4 | xbrli:pure | 2024-03-31 | 2024-12-23 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 0.05 | xbrli:pure | 2024-03-31 | 2025-12-24 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 258249 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 258249 | GBP | 2024-03-31 | 2025-12-24 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 83885 | GBP | 2024-03-31 | 2024-12-23 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 451928 | GBP | 2024-03-31 | 2025-12-24 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 451928 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors | 121582 | GBP | 2024-03-31 | 2025-12-24 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 121582 | GBP | 2024-03-31 | 2025-12-24 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 121582 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 8483 | GBP | 2024-03-31 | 2025-12-24 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 0 | GBP | 2024-03-31 | 2025-12-24 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 357587 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:Equity` | total-exemption-full |
| equity | 371270 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 8483 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 5200 | GBP | 2024-03-31 | 2025-12-24 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 371270 | GBP | 2024-03-31 | 2025-12-24 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 357587 | GBP | 2024-03-31 | 2025-12-24 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 5200 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:Equity` | total-exemption-full |
| fixed_assets | 3227 | GBP | 2024-03-31 | 2024-12-23 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_current_assets | 368043 | GBP | 2024-03-31 | 2025-12-24 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 368043 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 371270 | GBP | 2024-03-31 | 2025-12-24 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 371270 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 5 | xbrli:pure | 2023-03-31 | 2024-12-23 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 5 | xbrli:pure | 2023-03-31 | 2023-12-21 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 260702 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 260702 | GBP | 2023-03-31 | 2023-12-21 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 114862 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 114862 | GBP | 2023-03-31 | 2023-12-21 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 458813 | GBP | 2023-03-31 | 2023-12-21 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 458813 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 129015 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 129015 | GBP | 2023-03-31 | 2023-12-21 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 129015 | GBP | 2023-03-31 | 2023-12-21 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 343231 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 356914 | GBP | 2023-03-31 | 2023-12-21 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 5200 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 5200 | GBP | 2023-03-31 | 2023-12-21 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 343231 | GBP | 2023-03-31 | 2023-12-21 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 8483 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 8483 | GBP | 2023-03-31 | 2023-12-21 | filed | no | `core:Equity` | total-exemption-full |
| equity | 356914 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 12963 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:FixedAssets` | total-exemption-full |
| fixed_assets | 12963 | GBP | 2023-03-31 | 2023-12-21 | filed | no | `core:FixedAssets` | total-exemption-full |
| net_current_assets | 343951 | GBP | 2023-03-31 | 2023-12-21 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 343951 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 356914 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 356914 | GBP | 2023-03-31 | 2023-12-21 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 5 | xbrli:pure | 2022-03-31 | 2023-12-21 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 174657 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 84378 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 377554 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 146502 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 146502 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 314248 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 5200 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 16971 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 292077 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 21072 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_current_assets | 293176 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 314248 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2025-12-24: `{"superseded_document_id": "gb:03487793:doc:k8J2r6Hnq63UO4Z5kG7djTOoXkRqerqk6GrioPpYxVE", "restatements": [{"concept": "average_employees", "period_end": "2024-03-31", "old_value": "4.0000", "new_valu`

## VIRTUAL DIMENSIONS LIMITED (`gb:03766586`)

- registration: `03766586` (GB), status active, incorporated 1999-05-07
- classification: ['62020'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 64 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | xbrli:pure | 2025-03-31 | 2025-11-17 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 8246 | GBP | 2025-03-31 | 2025-11-17 | filed | yes | `core:Creditors` | micro-entity |
| equity | -8194 | GBP | 2025-03-31 | 2025-11-17 | filed | yes | `core:Equity` | micro-entity |
| net_assets | -8194 | GBP | 2025-03-31 | 2025-11-17 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 52 | GBP | 2025-03-31 | 2025-11-17 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 52 | GBP | 2025-03-31 | 2025-11-17 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2024-03-31 | 2025-11-17 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | xbrli:pure | 2024-03-31 | 2024-12-12 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 7933 | GBP | 2024-03-31 | 2024-12-12 | filed | no | `core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 7933 | GBP | 2024-03-31 | 2025-11-17 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 3 | GBP | 2024-03-31 | 2025-11-17 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 3 | GBP | 2024-03-31 | 2024-12-12 | filed | no | `core:Creditors` | micro-entity |
| equity | -7936 | GBP | 2024-03-31 | 2024-12-12 | filed | no | `core:Equity` | micro-entity |
| equity | -7936 | GBP | 2024-03-31 | 2025-11-17 | filed | yes | `core:Equity` | micro-entity |
| net_assets | -7936 | GBP | 2024-03-31 | 2024-12-12 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | -7936 | GBP | 2024-03-31 | 2025-11-17 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -3 | GBP | 2024-03-31 | 2024-12-12 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -3 | GBP | 2024-03-31 | 2025-11-17 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -3 | GBP | 2024-03-31 | 2024-12-12 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -3 | GBP | 2024-03-31 | 2025-11-17 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2023-03-31 | 2024-12-12 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | xbrli:pure | 2023-03-31 | 2023-09-22 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 7619 | GBP | 2023-03-31 | 2023-09-22 | filed | no | `core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 7619 | GBP | 2023-03-31 | 2024-12-12 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 150 | GBP | 2023-03-31 | 2024-12-12 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 150 | GBP | 2023-03-31 | 2023-09-22 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 80 | GBP | 2023-03-31 | 2024-12-12 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 80 | GBP | 2023-03-31 | 2023-09-22 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | -7689 | GBP | 2023-03-31 | 2024-12-12 | filed | yes | `core:Equity` | micro-entity |
| equity | -7689 | GBP | 2023-03-31 | 2023-09-22 | filed | no | `core:Equity` | micro-entity |
| net_assets | -7689 | GBP | 2023-03-31 | 2024-12-12 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | -7689 | GBP | 2023-03-31 | 2023-09-22 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -70 | GBP | 2023-03-31 | 2024-12-12 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -70 | GBP | 2023-03-31 | 2023-09-22 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -70 | GBP | 2023-03-31 | 2023-09-22 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -70 | GBP | 2023-03-31 | 2024-12-12 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2022-03-31 | 2023-09-22 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 7356 | GBP | 2022-03-31 | 2023-09-22 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 150 | GBP | 2022-03-31 | 2023-09-22 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 64 | GBP | 2022-03-31 | 2023-09-22 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -7442 | GBP | 2022-03-31 | 2023-09-22 | filed | yes | `core:Equity` | micro-entity |
| net_assets | -7442 | GBP | 2022-03-31 | 2023-09-22 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -86 | GBP | 2022-03-31 | 2023-09-22 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -86 | GBP | 2022-03-31 | 2023-09-22 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## TEST COVERAGE LIMITED (`gb:04051019`)

- registration: `04051019` (GB), status active, incorporated 2000-08-10
- classification: ['62020'] (sic_2007)
- records: 5 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 63 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-08-31 | 2026-05-29 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 2369 | GBP | 2025-08-31 | 2026-05-29 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 3872 | GBP | 2025-08-31 | 2026-05-29 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 1503 | GBP | 2025-08-31 | 2026-05-29 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2025-08-31 | 2026-05-29 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -4561 | GBP | 2025-08-31 | 2026-05-29 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | -4560 | GBP | 2025-08-31 | 2026-05-29 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | -4560 | GBP | 2025-08-31 | 2026-05-29 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -4560 | GBP | 2025-08-31 | 2026-05-29 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-08-31 | 2025-05-29 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| average_employees | 1 | xbrli:pure | 2024-08-31 | 2026-05-29 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 9019 | GBP | 2024-08-31 | 2026-05-29 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 9019 | GBP | 2024-08-31 | 2025-05-29 | filed | no | `core:CashBankOnHand` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 8567 | GBP | 2024-08-31 | 2025-05-29 | filed | yes | `core:Creditors` | unaudited-abridged |
| current_assets | 9125 | GBP | 2024-08-31 | 2026-05-29 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 9125 | GBP | 2024-08-31 | 2025-05-29 | filed | no | `core:CurrentAssets` | unaudited-abridged |
| debtors | 106 | GBP | 2024-08-31 | 2026-05-29 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 106 | GBP | 2024-08-31 | 2025-05-29 | filed | no | `core:Debtors` | unaudited-abridged |
| equity | 558 | GBP | 2024-08-31 | 2025-05-29 | filed | no | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 557 | GBP | 2024-08-31 | 2025-05-29 | filed | no | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2024-08-31 | 2025-05-29 | filed | no | `core:Equity` | unaudited-abridged |
| equity | 558 | GBP | 2024-08-31 | 2026-05-29 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2024-08-31 | 2026-05-29 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 557 | GBP | 2024-08-31 | 2026-05-29 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 558 | GBP | 2024-08-31 | 2025-05-29 | filed | yes | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 558 | GBP | 2024-08-31 | 2025-05-29 | filed | no | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 558 | GBP | 2024-08-31 | 2026-05-29 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 558 | GBP | 2024-08-31 | 2025-05-29 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 558 | GBP | 2024-08-31 | 2026-05-29 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-08-31 | 2025-05-29 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| average_employees | 0 | xbrli:pure | 2023-08-31 | 2024-05-31 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 32285 | GBP | 2023-08-31 | 2024-05-31 | filed | no | `core:CashBankOnHand` | unaudited-abridged |
| cash | 32285 | GBP | 2023-08-31 | 2025-05-29 | filed | yes | `core:CashBankOnHand` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 19196 | GBP | 2023-08-31 | 2024-05-31 | filed | no | `core:Creditors` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 19196 | GBP | 2023-08-31 | 2025-05-29 | filed | yes | `core:Creditors` | unaudited-abridged |
| current_assets | 33025 | GBP | 2023-08-31 | 2024-05-31 | filed | no | `core:CurrentAssets` | unaudited-abridged |
| current_assets | 33025 | GBP | 2023-08-31 | 2025-05-29 | filed | yes | `core:CurrentAssets` | unaudited-abridged |
| debtors | 740 | GBP | 2023-08-31 | 2024-05-31 | filed | no | `core:Debtors` | unaudited-abridged |
| debtors | 740 | GBP | 2023-08-31 | 2025-05-29 | filed | yes | `core:Debtors` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 13828 | GBP | 2023-08-31 | 2024-05-31 | filed | no | `core:Equity` | unaudited-abridged |
| equity | 13829 | GBP | 2023-08-31 | 2024-05-31 | filed | no | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2023-08-31 | 2024-05-31 | filed | no | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2023-08-31 | 2025-05-29 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 13828 | GBP | 2023-08-31 | 2025-05-29 | filed | yes | `core:Equity` | unaudited-abridged |
| equity | 13829 | GBP | 2023-08-31 | 2025-05-29 | filed | yes | `core:Equity` | unaudited-abridged |
| net_assets | 13829 | GBP | 2023-08-31 | 2024-05-31 | filed | no | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_assets | 13829 | GBP | 2023-08-31 | 2025-05-29 | filed | yes | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 13829 | GBP | 2023-08-31 | 2025-05-29 | filed | yes | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 13829 | GBP | 2023-08-31 | 2024-05-31 | filed | no | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 13829 | GBP | 2023-08-31 | 2025-05-29 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 13829 | GBP | 2023-08-31 | 2024-05-31 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| cash | 6027 | GBP | 2022-08-31 | 2024-05-31 | filed | yes | `core:CashBankOnHand` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 16189 | GBP | 2022-08-31 | 2024-05-31 | filed | yes | `core:Creditors` | unaudited-abridged |
| current_assets | 31806 | GBP | 2022-08-31 | 2024-05-31 | filed | yes | `core:CurrentAssets` | unaudited-abridged |
| debtors | 25779 | GBP | 2022-08-31 | 2024-05-31 | filed | yes | `core:Debtors` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 15616 | GBP | 2022-08-31 | 2024-05-31 | filed | yes | `core:Equity` | unaudited-abridged |
| equity | 15617 | GBP | 2022-08-31 | 2024-05-31 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2022-08-31 | 2024-05-31 | filed | yes | `core:Equity` | unaudited-abridged |
| net_assets | 15617 | GBP | 2022-08-31 | 2024-05-31 | filed | yes | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 15617 | GBP | 2022-08-31 | 2024-05-31 | filed | yes | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 15617 | GBP | 2022-08-31 | 2024-05-31 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |

_No coverage facts for the latest run._

- event restatement @ 2025-05-29: `{"superseded_document_id": "gb:04051019:doc:OBdZ8lfawRteCo47FFMag9d_E-pyjCKcsBUjRZcVNlg", "restatements": [{"concept": "average_employees", "period_end": "2023-08-31", "old_value": "0.0000", "new_valu`

## I/N CONSULTANTS LTD (`gb:04336772`)

- registration: `04336772` (GB), status active, incorporated 2001-12-10
- classification: ['62020', '62090', '95110'] (sic_2007)
- records: 6 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 75 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-03-31 | 2025-12-01 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 19267 | GBP | 2025-03-31 | 2025-12-01 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 2165 | GBP | 2025-03-31 | 2025-12-01 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -7207 | GBP | 2025-03-31 | 2025-12-01 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 10995 | GBP | 2025-03-31 | 2025-12-01 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | -7207 | GBP | 2025-03-31 | 2025-12-01 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -17102 | GBP | 2025-03-31 | 2025-12-01 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -6107 | GBP | 2025-03-31 | 2025-12-01 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-03-31 | 2025-12-01 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-03-31 | 2024-10-10 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 18588 | GBP | 2024-03-31 | 2024-10-10 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 18588 | GBP | 2024-03-31 | 2025-12-01 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 15338 | GBP | 2024-03-31 | 2024-10-10 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 15338 | GBP | 2024-03-31 | 2025-12-01 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 16866 | GBP | 2024-03-31 | 2025-12-01 | filed | yes | `core:Equity` | micro-entity |
| equity | 16866 | GBP | 2024-03-31 | 2024-10-10 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 21216 | GBP | 2024-03-31 | 2025-12-01 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 21216 | GBP | 2024-03-31 | 2024-10-10 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | 16866 | GBP | 2024-03-31 | 2025-12-01 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 16866 | GBP | 2024-03-31 | 2024-10-10 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -3250 | GBP | 2024-03-31 | 2025-12-01 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -3250 | GBP | 2024-03-31 | 2024-10-10 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 17966 | GBP | 2024-03-31 | 2024-10-10 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 17966 | GBP | 2024-03-31 | 2025-12-01 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-03-31 | 2023-11-21 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-03-31 | 2024-10-10 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 6026 | GBP | 2023-03-31 | 2023-11-21 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 6026 | GBP | 2023-03-31 | 2024-10-10 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 7513 | GBP | 2023-03-31 | 2023-11-21 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 7513 | GBP | 2023-03-31 | 2024-10-10 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 31620 | GBP | 2023-03-31 | 2024-10-10 | filed | yes | `core:Equity` | micro-entity |
| equity | 31620 | GBP | 2023-03-31 | 2023-11-21 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 31233 | GBP | 2023-03-31 | 2024-10-10 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 31233 | GBP | 2023-03-31 | 2023-11-21 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | 31620 | GBP | 2023-03-31 | 2024-10-10 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 31620 | GBP | 2023-03-31 | 2023-11-21 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 1487 | GBP | 2023-03-31 | 2024-10-10 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 1487 | GBP | 2023-03-31 | 2023-11-21 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 32720 | GBP | 2023-03-31 | 2023-11-21 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 32720 | GBP | 2023-03-31 | 2024-10-10 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2022-03-31 | 2023-11-21 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 31438 | GBP | 2022-03-31 | 2023-11-21 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 53301 | GBP | 2022-03-31 | 2023-11-21 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 27109 | GBP | 2022-03-31 | 2023-11-21 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 6346 | GBP | 2022-03-31 | 2023-11-21 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 27109 | GBP | 2022-03-31 | 2023-11-21 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 21863 | GBP | 2022-03-31 | 2023-11-21 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 28209 | GBP | 2022-03-31 | 2023-11-21 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## THE OTHER PERSON CONSULTANCY LTD (`gb:04623850`)

- registration: `04623850` (GB), status active, incorporated 2002-12-23
- classification: ['62020'] (sic_2007)
- records: 5 officers, 3 beneficial owners, 0 ownership statements, 0 security interests, 79 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 6 | xbrli:pure | 2026-03-31 | 2026-05-27 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 265525 | GBP | 2026-03-31 | 2026-05-27 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 7140 | GBP | 2026-03-31 | 2026-05-27 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 596825 | GBP | 2026-03-31 | 2026-05-27 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 1108125 | GBP | 2026-03-31 | 2026-05-27 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 596825 | GBP | 2026-03-31 | 2026-05-27 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -258385 | GBP | 2026-03-31 | 2026-05-27 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 849740 | GBP | 2026-03-31 | 2026-05-27 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 5 | xbrli:pure | 2025-03-31 | 2026-05-27 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 5 | xbrli:pure | 2025-03-31 | 2025-06-05 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 236534 | GBP | 2025-03-31 | 2025-06-05 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 236534 | GBP | 2025-03-31 | 2026-05-27 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 4940 | GBP | 2025-03-31 | 2025-06-05 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 4940 | GBP | 2025-03-31 | 2026-05-27 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 513995 | GBP | 2025-03-31 | 2025-06-05 | filed | no | `core:Equity` | micro-entity |
| equity | 513995 | GBP | 2025-03-31 | 2026-05-27 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 960834 | GBP | 2025-03-31 | 2026-05-27 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 960834 | GBP | 2025-03-31 | 2025-06-05 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | 513995 | GBP | 2025-03-31 | 2025-06-05 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 513995 | GBP | 2025-03-31 | 2026-05-27 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -231373 | GBP | 2025-03-31 | 2026-05-27 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -231373 | GBP | 2025-03-31 | 2025-06-05 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 729461 | GBP | 2025-03-31 | 2025-06-05 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 729461 | GBP | 2025-03-31 | 2026-05-27 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 5 | xbrli:pure | 2024-03-31 | 2024-06-03 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 5 | xbrli:pure | 2024-03-31 | 2025-06-05 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 237187 | GBP | 2024-03-31 | 2025-06-05 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 237187 | GBP | 2024-03-31 | 2024-06-03 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 63660 | GBP | 2024-03-31 | 2025-06-05 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 63660 | GBP | 2024-03-31 | 2024-06-03 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 421960 | GBP | 2024-03-31 | 2024-06-03 | filed | no | `core:Equity` | micro-entity |
| equity | 421960 | GBP | 2024-03-31 | 2025-06-05 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 764446 | GBP | 2024-03-31 | 2025-06-05 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 764446 | GBP | 2024-03-31 | 2024-06-03 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | 421960 | GBP | 2024-03-31 | 2024-06-03 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 421960 | GBP | 2024-03-31 | 2025-06-05 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -173527 | GBP | 2024-03-31 | 2024-06-03 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -173527 | GBP | 2024-03-31 | 2025-06-05 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 590919 | GBP | 2024-03-31 | 2025-06-05 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 590919 | GBP | 2024-03-31 | 2024-06-03 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 5 | xbrli:pure | 2023-03-31 | 2024-06-03 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 184944 | GBP | 2023-03-31 | 2024-06-03 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 4556 | GBP | 2023-03-31 | 2024-06-03 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 231877 | GBP | 2023-03-31 | 2024-06-03 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 519261 | GBP | 2023-03-31 | 2024-06-03 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 231877 | GBP | 2023-03-31 | 2024-06-03 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -175054 | GBP | 2023-03-31 | 2024-06-03 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 344207 | GBP | 2023-03-31 | 2024-06-03 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## FLUENT INTERACTION LTD (`gb:04929439`)

- registration: `04929439` (GB), status active, incorporated 2003-10-10
- classification: ['62020', '63990', '74909'] (sic_2007)
- records: 7 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 84 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 10 | xbrli:pure | 2025-10-31 | 2026-07-29 | filed | yes | `d:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 415022 | GBP | 2025-10-31 | 2026-07-29 | filed | yes | `d:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 157433 | GBP | 2025-10-31 | 2026-07-29 | filed | yes | `d:Creditors` | total-exemption-full |
| current_assets | 540590 | GBP | 2025-10-31 | 2026-07-29 | filed | yes | `d:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 105568 | GBP | 2025-10-31 | 2026-07-29 | filed | yes | `d:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments'}` | 20000 | GBP | 2025-10-31 | 2026-07-29 | filed | yes | `d:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 220 | GBP | 2025-10-31 | 2026-07-29 | filed | yes | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 383176 | GBP | 2025-10-31 | 2026-07-29 | filed | yes | `d:Equity` | total-exemption-full |
| equity | 383396 | GBP | 2025-10-31 | 2026-07-29 | filed | yes | `d:Equity` | total-exemption-full |
| fixed_assets | 320 | GBP | 2025-10-31 | 2026-07-29 | filed | yes | `d:FixedAssets` | total-exemption-full |
| net_assets | 383396 | GBP | 2025-10-31 | 2026-07-29 | filed | yes | `d:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 383157 | GBP | 2025-10-31 | 2026-07-29 | filed | yes | `d:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 383477 | GBP | 2025-10-31 | 2026-07-29 | filed | yes | `d:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 12 | xbrli:pure | 2024-10-31 | 2026-07-29 | filed | yes | `d:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 10 | xbrli:pure | 2024-10-31 | 2025-07-31 | filed | no | `d:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 395862 | GBP | 2024-10-31 | 2025-07-31 | filed | no | `d:CashBankOnHand` | total-exemption-full |
| cash | 395862 | GBP | 2024-10-31 | 2026-07-29 | filed | yes | `d:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 130507 | GBP | 2024-10-31 | 2026-07-29 | filed | yes | `d:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 130506 | GBP | 2024-10-31 | 2025-07-31 | filed | no | `d:Creditors` | total-exemption-full |
| current_assets | 734058 | GBP | 2024-10-31 | 2026-07-29 | filed | yes | `d:CurrentAssets` | total-exemption-full |
| current_assets | 734058 | GBP | 2024-10-31 | 2025-07-31 | filed | no | `d:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments'}` | 20000 | GBP | 2024-10-31 | 2025-07-31 | filed | no | `d:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 318196 | GBP | 2024-10-31 | 2025-07-31 | filed | no | `d:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments'}` | 20000 | GBP | 2024-10-31 | 2026-07-29 | filed | yes | `d:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 318196 | GBP | 2024-10-31 | 2026-07-29 | filed | yes | `d:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 604443 | GBP | 2024-10-31 | 2025-07-31 | filed | no | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 604443 | GBP | 2024-10-31 | 2026-07-29 | filed | yes | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 220 | GBP | 2024-10-31 | 2025-07-31 | filed | no | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 220 | GBP | 2024-10-31 | 2026-07-29 | filed | yes | `d:Equity` | total-exemption-full |
| equity | 604663 | GBP | 2024-10-31 | 2026-07-29 | filed | yes | `d:Equity` | total-exemption-full |
| equity | 604663 | GBP | 2024-10-31 | 2025-07-31 | filed | no | `d:Equity` | total-exemption-full |
| fixed_assets | 1483 | GBP | 2024-10-31 | 2026-07-29 | filed | yes | `d:FixedAssets` | total-exemption-full |
| fixed_assets | 1482 | GBP | 2024-10-31 | 2025-07-31 | filed | no | `d:FixedAssets` | total-exemption-full |
| net_assets | 604663 | GBP | 2024-10-31 | 2026-07-29 | filed | yes | `d:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 604663 | GBP | 2024-10-31 | 2025-07-31 | filed | no | `d:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 603551 | GBP | 2024-10-31 | 2026-07-29 | filed | yes | `d:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 603552 | GBP | 2024-10-31 | 2025-07-31 | filed | no | `d:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 605034 | GBP | 2024-10-31 | 2025-07-31 | filed | no | `d:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 605034 | GBP | 2024-10-31 | 2026-07-29 | filed | yes | `d:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 12 | xbrli:pure | 2023-10-31 | 2025-07-31 | filed | yes | `d:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 12 | xbrli:pure | 2023-10-31 | 2024-07-31 | filed | no | `d:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 625573 | GBP | 2023-10-31 | 2024-07-31 | filed | no | `d:CashBankOnHand` | total-exemption-full |
| cash | 625573 | GBP | 2023-10-31 | 2025-07-31 | filed | yes | `d:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 201655 | GBP | 2023-10-31 | 2024-07-31 | filed | no | `d:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 201655 | GBP | 2023-10-31 | 2025-07-31 | filed | yes | `d:Creditors` | total-exemption-full |
| current_assets | 923373 | GBP | 2023-10-31 | 2025-07-31 | filed | yes | `d:CurrentAssets` | total-exemption-full |
| current_assets | 923373 | GBP | 2023-10-31 | 2024-07-31 | filed | no | `d:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments'}` | 20000 | GBP | 2023-10-31 | 2025-07-31 | filed | yes | `d:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 277800 | GBP | 2023-10-31 | 2025-07-31 | filed | yes | `d:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments'}` | 20000 | GBP | 2023-10-31 | 2024-07-31 | filed | no | `d:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 277800 | GBP | 2023-10-31 | 2024-07-31 | filed | no | `d:Debtors` | total-exemption-full |
| equity | 725504 | GBP | 2023-10-31 | 2025-07-31 | filed | yes | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 205 | GBP | 2023-10-31 | 2025-07-31 | filed | yes | `d:Equity` | total-exemption-full |
| equity | 725504 | GBP | 2023-10-31 | 2024-07-31 | filed | no | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 725299 | GBP | 2023-10-31 | 2025-07-31 | filed | yes | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 205 | GBP | 2023-10-31 | 2024-07-31 | filed | no | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 725299 | GBP | 2023-10-31 | 2024-07-31 | filed | no | `d:Equity` | total-exemption-full |
| fixed_assets | 5048 | GBP | 2023-10-31 | 2025-07-31 | filed | yes | `d:FixedAssets` | total-exemption-full |
| fixed_assets | 5048 | GBP | 2023-10-31 | 2024-07-31 | filed | no | `d:FixedAssets` | total-exemption-full |
| net_assets | 725504 | GBP | 2023-10-31 | 2024-07-31 | filed | no | `d:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 725504 | GBP | 2023-10-31 | 2025-07-31 | filed | yes | `d:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 721718 | GBP | 2023-10-31 | 2024-07-31 | filed | no | `d:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 721718 | GBP | 2023-10-31 | 2025-07-31 | filed | yes | `d:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 726766 | GBP | 2023-10-31 | 2024-07-31 | filed | no | `d:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 726766 | GBP | 2023-10-31 | 2025-07-31 | filed | yes | `d:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 12 | xbrli:pure | 2022-10-31 | 2024-07-31 | filed | yes | `d:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 784041 | GBP | 2022-10-31 | 2024-07-31 | filed | yes | `d:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 218904 | GBP | 2022-10-31 | 2024-07-31 | filed | yes | `d:Creditors` | total-exemption-full |
| current_assets | 1230974 | GBP | 2022-10-31 | 2024-07-31 | filed | yes | `d:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 426933 | GBP | 2022-10-31 | 2024-07-31 | filed | yes | `d:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments'}` | 20000 | GBP | 2022-10-31 | 2024-07-31 | filed | yes | `d:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 205 | GBP | 2022-10-31 | 2024-07-31 | filed | yes | `d:Equity` | total-exemption-full |
| equity | 1019333 | GBP | 2022-10-31 | 2024-07-31 | filed | yes | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1019128 | GBP | 2022-10-31 | 2024-07-31 | filed | yes | `d:Equity` | total-exemption-full |
| fixed_assets | 8966 | GBP | 2022-10-31 | 2024-07-31 | filed | yes | `d:FixedAssets` | total-exemption-full |
| net_assets | 1019333 | GBP | 2022-10-31 | 2024-07-31 | filed | yes | `d:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1012070 | GBP | 2022-10-31 | 2024-07-31 | filed | yes | `d:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1021036 | GBP | 2022-10-31 | 2024-07-31 | filed | yes | `d:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2026-07-29: `{"superseded_document_id": "gb:04929439:doc:-hA74YGU52L8YEIYYEzegO-90BYbX-JEpYQfUtoWU9E", "restatements": [{"concept": "average_employees", "period_end": "2024-10-31", "old_value": "10.0000", "new_val`
