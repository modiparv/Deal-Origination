# Ingest spot-check

- database: `data/engine.db`
- latest run: `20260813T041321Z-a59172cb`
- companies in store: 2600; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## SCANTRON INDUSTRIAL PRODUCTS LIMITED (`gb:01036910`)

- registration: `01036910` (GB), status active, incorporated 1972-01-04
- classification: ['71129'] (sic_2007)
- records: 3 officers, 1 beneficial owners, 0 ownership statements, 3 security interests, 120 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 9 | xbrli:pure | 2025-05-31 | 2025-12-04 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 730972 | GBP | 2025-05-31 | 2025-12-04 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 239347 | GBP | 2025-05-31 | 2025-12-04 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 10 | GBP | 2025-05-31 | 2025-12-04 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 1176446 | GBP | 2025-05-31 | 2025-12-04 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1176346 | GBP | 2025-05-31 | 2025-12-04 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 90 | GBP | 2025-05-31 | 2025-12-04 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 1176446 | GBP | 2025-05-31 | 2025-12-04 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| average_employees | 8 | xbrli:pure | 2024-05-31 | 2025-12-04 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 8 | xbrli:pure | 2024-05-31 | 2025-02-17 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 409768 | GBP | 2024-05-31 | 2025-12-04 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 409768 | GBP | 2024-05-31 | 2025-02-17 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 993464 | GBP | 2024-05-31 | 2025-02-17 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 171100 | GBP | 2024-05-31 | 2025-12-04 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 171100 | GBP | 2024-05-31 | 2025-02-17 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 171100 | GBP | 2024-05-31 | 2025-02-17 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-05-31 | 2025-02-17 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-05-31 | 2025-12-04 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 897845 | GBP | 2024-05-31 | 2025-12-04 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 897845 | GBP | 2024-05-31 | 2025-02-17 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 0 | GBP | 2024-05-31 | 2025-12-04 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 897945 | GBP | 2024-05-31 | 2025-02-17 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 897945 | GBP | 2024-05-31 | 2025-12-04 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 897945 | GBP | 2024-05-31 | 2025-12-04 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 897945 | GBP | 2024-05-31 | 2025-02-17 | filed | no | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 898540 | GBP | 2024-05-31 | 2025-02-17 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 926319 | GBP | 2024-05-31 | 2025-02-17 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 8 | xbrli:pure | 2023-05-31 | 2025-02-17 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 8 | xbrli:pure | 2023-05-31 | 2024-01-24 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 454088 | GBP | 2023-05-31 | 2024-01-24 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 454088 | GBP | 2023-05-31 | 2025-02-17 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 1343697 | GBP | 2023-05-31 | 2024-01-24 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 1343697 | GBP | 2023-05-31 | 2025-02-17 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 425181 | GBP | 2023-05-31 | 2025-02-17 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 425181 | GBP | 2023-05-31 | 2025-02-17 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 425181 | GBP | 2023-05-31 | 2024-01-24 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original'}` | 425181 | GBP | 2023-05-31 | 2024-01-24 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 1006256 | GBP | 2023-05-31 | 2025-02-17 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1006156 | GBP | 2023-05-31 | 2024-01-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 100 | GBP | 2023-05-31 | 2024-01-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-05-31 | 2025-02-17 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 1006256 | GBP | 2023-05-31 | 2024-01-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-05-31 | 2025-12-04 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 0 | GBP | 2023-05-31 | 2025-12-04 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1006156 | GBP | 2023-05-31 | 2025-02-17 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 1006256 | GBP | 2023-05-31 | 2025-02-17 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets `{'OriginalRevisedDataDimension': 'Original'}` | 1006256 | GBP | 2023-05-31 | 2024-01-24 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1068918 | GBP | 2023-05-31 | 2025-02-17 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 1068918 | GBP | 2023-05-31 | 2024-01-24 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 1104092 | GBP | 2023-05-31 | 2024-01-24 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1104092 | GBP | 2023-05-31 | 2025-02-17 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 8 | xbrli:pure | 2022-05-31 | 2024-01-24 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 243234 | GBP | 2022-05-31 | 2024-01-24 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 1052255 | GBP | 2022-05-31 | 2024-01-24 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original'}` | 426049 | GBP | 2022-05-31 | 2024-01-24 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 426049 | GBP | 2022-05-31 | 2024-01-24 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 100 | GBP | 2022-05-31 | 2024-01-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 788850 | GBP | 2022-05-31 | 2024-01-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 788950 | GBP | 2022-05-31 | 2024-01-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets `{'OriginalRevisedDataDimension': 'Original'}` | 788950 | GBP | 2022-05-31 | 2024-01-24 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 918508 | GBP | 2022-05-31 | 2024-01-24 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 940264 | GBP | 2022-05-31 | 2024-01-24 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## PLANMASTER SYSTEMS LIMITED (`gb:01332822`)

- registration: `01332822` (GB), status active, incorporated 1977-10-05
- classification: ['62012'] (sic_2007)
- records: 6 officers, 1 beneficial owners, 0 ownership statements, 1 security interests, 103 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.05 | xbrli:pure | 2025-12-31 | 2026-04-14 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 20345 | GBP | 2025-12-31 | 2026-04-14 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 31266 | GBP | 2025-12-31 | 2026-04-14 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 21187 | GBP | 2025-12-31 | 2026-04-14 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 842 | GBP | 2025-12-31 | 2026-04-14 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 842 | GBP | 2025-12-31 | 2026-04-14 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -10355 | GBP | 2025-12-31 | 2026-04-14 | filed | yes | `core:Equity` | total-exemption-full |
| equity | -10255 | GBP | 2025-12-31 | 2026-04-14 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-12-31 | 2026-04-14 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | -10255 | GBP | 2025-12-31 | 2026-04-14 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -10079 | GBP | 2025-12-31 | 2026-04-14 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -9921 | GBP | 2025-12-31 | 2026-04-14 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0.05 | xbrli:pure | 2024-12-31 | 2026-04-14 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 0.05 | xbrli:pure | 2024-12-31 | 2025-10-24 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 31174 | GBP | 2024-12-31 | 2026-04-14 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 31174 | GBP | 2024-12-31 | 2025-10-24 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 37503 | GBP | 2024-12-31 | 2026-04-14 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 37503 | GBP | 2024-12-31 | 2025-10-24 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 32374 | GBP | 2024-12-31 | 2025-10-24 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 32374 | GBP | 2024-12-31 | 2026-04-14 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1200 | GBP | 2024-12-31 | 2026-04-14 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 1200 | GBP | 2024-12-31 | 2026-04-14 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 1200 | GBP | 2024-12-31 | 2025-10-24 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-12-31 | 2026-04-14 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -5326 | GBP | 2024-12-31 | 2026-04-14 | filed | yes | `core:Equity` | total-exemption-full |
| equity | -5226 | GBP | 2024-12-31 | 2026-04-14 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-12-31 | 2025-10-24 | filed | no | `core:Equity` | total-exemption-full |
| equity | -5226 | GBP | 2024-12-31 | 2025-10-24 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -5326 | GBP | 2024-12-31 | 2025-10-24 | filed | no | `core:Equity` | total-exemption-full |
| net_assets | -5226 | GBP | 2024-12-31 | 2025-10-24 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | -5226 | GBP | 2024-12-31 | 2026-04-14 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -5129 | GBP | 2024-12-31 | 2026-04-14 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -5129 | GBP | 2024-12-31 | 2025-10-24 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -4892 | GBP | 2024-12-31 | 2025-10-24 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -4892 | GBP | 2024-12-31 | 2026-04-14 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 4 | xbrli:pure | 2023-12-31 | 2024-04-05 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 0.04 | xbrli:pure | 2023-12-31 | 2025-10-24 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 38268 | GBP | 2023-12-31 | 2025-10-24 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 38268 | GBP | 2023-12-31 | 2024-04-05 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 41387 | GBP | 2023-12-31 | 2024-04-05 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 41387 | GBP | 2023-12-31 | 2025-10-24 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 38268 | GBP | 2023-12-31 | 2025-10-24 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 38268 | GBP | 2023-12-31 | 2024-04-05 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors | 0 | GBP | 2023-12-31 | 2025-10-24 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 0 | GBP | 2023-12-31 | 2024-04-05 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -2952 | GBP | 2023-12-31 | 2024-04-05 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-12-31 | 2024-04-05 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-12-31 | 2025-10-24 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -2952 | GBP | 2023-12-31 | 2025-10-24 | filed | yes | `core:Equity` | total-exemption-full |
| equity | -2852 | GBP | 2023-12-31 | 2025-10-24 | filed | yes | `core:Equity` | total-exemption-full |
| equity | -2852 | GBP | 2023-12-31 | 2024-04-05 | filed | no | `core:Equity` | total-exemption-full |
| net_assets | -2852 | GBP | 2023-12-31 | 2025-10-24 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | -2852 | GBP | 2023-12-31 | 2024-04-05 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -3119 | GBP | 2023-12-31 | 2025-10-24 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -3119 | GBP | 2023-12-31 | 2024-04-05 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -2763 | GBP | 2023-12-31 | 2025-10-24 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -2763 | GBP | 2023-12-31 | 2024-04-05 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 4 | xbrli:pure | 2022-12-31 | 2024-04-05 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 56132 | GBP | 2022-12-31 | 2024-04-05 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 48265 | GBP | 2022-12-31 | 2024-04-05 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 56271 | GBP | 2022-12-31 | 2024-04-05 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 139 | GBP | 2022-12-31 | 2024-04-05 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2022-12-31 | 2024-04-05 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 8306 | GBP | 2022-12-31 | 2024-04-05 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 8406 | GBP | 2022-12-31 | 2024-04-05 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 8406 | GBP | 2022-12-31 | 2024-04-05 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 8006 | GBP | 2022-12-31 | 2024-04-05 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 8540 | GBP | 2022-12-31 | 2024-04-05 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2025-10-24: `{"superseded_document_id": "gb:01332822:doc:bKeq7std6GpX-ZqY75uW3J0WE0tJDwuA1QlvqJLjADQ", "restatements": [{"concept": "average_employees", "period_end": "2023-12-31", "old_value": "4.0000", "new_valu`

## PDSVISION UK LIMITED (`gb:01494005`)

- registration: `01494005` (GB), status active, incorporated 1980-04-28
- classification: ['71122'] (sic_2007)
- records: 13 officers, 2 beneficial owners, 1 ownership statements, 2 security interests, 140 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 82 | xbrli:pure | 2024-12-31 | 2025-07-02 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | medium |
| cash | 742877 | GBP | 2024-12-31 | 2025-07-02 | filed | yes | `ns5:CashBankOnHand` | medium |
| current_assets | 8365230 | GBP | 2024-12-31 | 2025-07-02 | filed | yes | `ns5:CurrentAssets` | medium |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 7622353 | GBP | 2024-12-31 | 2025-07-02 | filed | yes | `ns5:Debtors` | medium |
| debtors | 7622353 | GBP | 2024-12-31 | 2025-07-02 | filed | yes | `ns5:Debtors` | medium |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-12-31 | 2025-07-02 | filed | yes | `ns5:Equity` | medium |
| equity | 1389718 | GBP | 2024-12-31 | 2025-07-02 | filed | yes | `ns5:Equity` | medium |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1389618 | GBP | 2024-12-31 | 2025-07-02 | filed | yes | `ns5:Equity` | medium |
| fixed_assets | 157851 | GBP | 2024-12-31 | 2025-07-02 | filed | yes | `ns5:FixedAssets` | medium |
| gross_profit | 6984748 | GBP | 2024-12-31 | 2025-07-02 | filed | yes | `ns5:GrossProfitLoss` | medium |
| net_assets | 1389718 | GBP | 2024-12-31 | 2025-07-02 | filed | yes | `ns5:NetAssetsLiabilities` | medium |
| net_current_assets | 1242943 | GBP | 2024-12-31 | 2025-07-02 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | medium |
| operating_profit | 1883692 | GBP | 2024-12-31 | 2025-07-02 | filed | yes | `ns5:OperatingProfitLoss` | medium |
| profit_before_tax | 1884516 | GBP | 2024-12-31 | 2025-07-02 | filed | yes | `ns5:ProfitLossOnOrdinaryActivitiesBeforeTax` | medium |
| profit_for_period | 1366087 | GBP | 2024-12-31 | 2025-07-02 | filed | yes | `ns5:ProfitLoss` | medium |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1366087 | GBP | 2024-12-31 | 2025-07-02 | filed | yes | `ns5:ProfitLoss` | medium |
| revenue | 13489871 | GBP | 2024-12-31 | 2025-07-02 | filed | yes | `ns5:TurnoverRevenue` | medium |
| tax_charge | 518429 | GBP | 2024-12-31 | 2025-07-02 | filed | yes | `ns5:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | medium |
| total_assets_less_current_liabilities | 1400794 | GBP | 2024-12-31 | 2025-07-02 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | medium |
| average_employees | 51 | xbrli:pure | 2023-12-31 | 2025-07-02 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | medium |
| average_employees | 51 | xbrli:pure | 2023-12-31 | 2024-05-31 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | small |
| cash | 455292 | GBP | 2023-12-31 | 2025-07-02 | filed | yes | `ns5:CashBankOnHand` | medium |
| cash | 455292 | GBP | 2023-12-31 | 2024-05-31 | filed | no | `ns5:CashBankOnHand` | small |
| current_assets | 2156569 | GBP | 2023-12-31 | 2024-05-31 | filed | no | `ns5:CurrentAssets` | small |
| current_assets | 2156569 | GBP | 2023-12-31 | 2025-07-02 | filed | yes | `ns5:CurrentAssets` | medium |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1701277 | GBP | 2023-12-31 | 2024-05-31 | filed | no | `ns5:Debtors` | small |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 1701277 | GBP | 2023-12-31 | 2025-07-02 | filed | yes | `ns5:Debtors` | medium |
| debtors | 1701277 | GBP | 2023-12-31 | 2024-05-31 | filed | no | `ns5:Debtors` | small |
| debtors | 1701277 | GBP | 2023-12-31 | 2025-07-02 | filed | yes | `ns5:Debtors` | medium |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-12-31 | 2024-05-31 | filed | no | `ns5:Equity` | small |
| equity | 393631 | GBP | 2023-12-31 | 2024-05-31 | filed | no | `ns5:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 393531 | GBP | 2023-12-31 | 2025-07-02 | filed | yes | `ns5:Equity` | medium |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-12-31 | 2025-07-02 | filed | yes | `ns5:Equity` | medium |
| equity | 393631 | GBP | 2023-12-31 | 2025-07-02 | filed | yes | `ns5:Equity` | medium |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 393531 | GBP | 2023-12-31 | 2024-05-31 | filed | no | `ns5:Equity` | small |
| fixed_assets | 50793 | GBP | 2023-12-31 | 2025-07-02 | filed | yes | `ns5:FixedAssets` | medium |
| fixed_assets | 50793 | GBP | 2023-12-31 | 2024-05-31 | filed | no | `ns5:FixedAssets` | small |
| gross_profit | 3718965 | GBP | 2023-12-31 | 2025-07-02 | filed | yes | `ns5:GrossProfitLoss` | medium |
| net_assets | 393631 | GBP | 2023-12-31 | 2024-05-31 | filed | no | `ns5:NetAssetsLiabilities` | small |
| net_assets | 393631 | GBP | 2023-12-31 | 2025-07-02 | filed | yes | `ns5:NetAssetsLiabilities` | medium |
| net_current_assets | 342838 | GBP | 2023-12-31 | 2024-05-31 | filed | no | `ns5:NetCurrentAssetsLiabilities` | small |
| net_current_assets | 342838 | GBP | 2023-12-31 | 2025-07-02 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | medium |
| operating_profit | 547746 | GBP | 2023-12-31 | 2025-07-02 | filed | yes | `ns5:OperatingProfitLoss` | medium |
| profit_before_tax | 547746 | GBP | 2023-12-31 | 2025-07-02 | filed | yes | `ns5:ProfitLossOnOrdinaryActivitiesBeforeTax` | medium |
| profit_for_period | 390443 | GBP | 2023-12-31 | 2025-07-02 | filed | yes | `ns5:ProfitLoss` | medium |
| revenue | 6363919 | GBP | 2023-12-31 | 2025-07-02 | filed | yes | `ns5:TurnoverRevenue` | medium |
| tax_charge | 157303 | GBP | 2023-12-31 | 2025-07-02 | filed | yes | `ns5:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | medium |
| total_assets_less_current_liabilities | 393631 | GBP | 2023-12-31 | 2025-07-02 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | medium |
| total_assets_less_current_liabilities | 393631 | GBP | 2023-12-31 | 2024-05-31 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | small |
| average_employees | 41 | xbrli:pure | 2022-12-31 | 2023-08-08 | filed | no | `ns6:AverageNumberEmployeesDuringPeriod` | small |
| average_employees | 41 | xbrli:pure | 2022-12-31 | 2024-05-31 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | small |
| cash | 489894 | GBP | 2022-12-31 | 2024-05-31 | filed | yes | `ns5:CashBankOnHand` | small |
| cash | 489894 | GBP | 2022-12-31 | 2023-08-08 | filed | no | `ns6:CashBankOnHand` | small |
| current_assets | 3026193 | GBP | 2022-12-31 | 2024-05-31 | filed | yes | `ns5:CurrentAssets` | small |
| current_assets | 3026193 | GBP | 2022-12-31 | 2023-08-08 | filed | no | `ns6:CurrentAssets` | small |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 2536299 | GBP | 2022-12-31 | 2023-08-08 | filed | no | `ns6:Debtors` | small |
| debtors | 2536299 | GBP | 2022-12-31 | 2024-05-31 | filed | yes | `ns5:Debtors` | small |
| debtors | 2536299 | GBP | 2022-12-31 | 2023-08-08 | filed | no | `ns6:Debtors` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2536299 | GBP | 2022-12-31 | 2024-05-31 | filed | yes | `ns5:Debtors` | small |
| equity | 333188 | GBP | 2022-12-31 | 2024-05-31 | filed | yes | `ns5:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2022-12-31 | 2024-05-31 | filed | yes | `ns5:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2022-12-31 | 2023-08-08 | filed | no | `ns6:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 333088 | GBP | 2022-12-31 | 2024-05-31 | filed | no | `ns5:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 333088 | GBP | 2022-12-31 | 2023-08-08 | filed | no | `ns6:Equity` | small |
| equity | 333188 | GBP | 2022-12-31 | 2023-08-08 | filed | no | `ns6:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 333088 | GBP | 2022-12-31 | 2025-07-02 | filed | yes | `ns5:Equity` | medium |
| fixed_assets | 118913 | GBP | 2022-12-31 | 2024-05-31 | filed | yes | `ns5:FixedAssets` | small |
| fixed_assets | 118913 | GBP | 2022-12-31 | 2023-08-08 | filed | no | `ns6:FixedAssets` | small |
| net_assets | 333188 | GBP | 2022-12-31 | 2024-05-31 | filed | yes | `ns5:NetAssetsLiabilities` | small |
| net_assets | 333188 | GBP | 2022-12-31 | 2023-08-08 | filed | no | `ns6:NetAssetsLiabilities` | small |
| net_current_assets | 223991 | GBP | 2022-12-31 | 2023-08-08 | filed | no | `ns6:NetCurrentAssetsLiabilities` | small |
| net_current_assets | 223991 | GBP | 2022-12-31 | 2024-05-31 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | small |
| total_assets_less_current_liabilities | 342904 | GBP | 2022-12-31 | 2023-08-08 | filed | no | `ns6:TotalAssetsLessCurrentLiabilities` | small |
| total_assets_less_current_liabilities | 342904 | GBP | 2022-12-31 | 2024-05-31 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | small |
| average_employees | 39 | xbrli:pure | 2021-12-31 | 2023-08-08 | filed | yes | `ns6:AverageNumberEmployeesDuringPeriod` | small |
| cash | 164895 | GBP | 2021-12-31 | 2023-08-08 | filed | yes | `ns6:CashBankOnHand` | small |
| current_assets | 2124917 | GBP | 2021-12-31 | 2023-08-08 | filed | yes | `ns6:CurrentAssets` | small |
| debtors | 1960022 | GBP | 2021-12-31 | 2023-08-08 | filed | yes | `ns6:Debtors` | small |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 1960022 | GBP | 2021-12-31 | 2023-08-08 | filed | yes | `ns6:Debtors` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2021-12-31 | 2023-08-08 | filed | yes | `ns6:Equity` | small |
| equity | 49885 | GBP | 2021-12-31 | 2023-08-08 | filed | yes | `ns6:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 49785 | GBP | 2021-12-31 | 2023-08-08 | filed | yes | `ns6:Equity` | small |
| fixed_assets | 157843 | GBP | 2021-12-31 | 2023-08-08 | filed | yes | `ns6:FixedAssets` | small |
| net_assets | 49885 | GBP | 2021-12-31 | 2023-08-08 | filed | yes | `ns6:NetAssetsLiabilities` | small |
| net_current_assets | -107958 | GBP | 2021-12-31 | 2023-08-08 | filed | yes | `ns6:NetCurrentAssetsLiabilities` | small |
| total_assets_less_current_liabilities | 49885 | GBP | 2021-12-31 | 2023-08-08 | filed | yes | `ns6:TotalAssetsLessCurrentLiabilities` | small |

_No coverage facts for the latest run._

## ESTEEM SYSTEMS LIMITED (`gb:01806531`)

- registration: `01806531` (GB), status active, incorporated 1984-04-06
- classification: ['62020'] (sic_2007)
- records: 30 officers, 1 beneficial owners, 0 ownership statements, 25 security interests, 245 filings, 0 events, 3 source documents

_No figures persisted for this company._

Coverage @ 2025-03-31: 0/21 concepts available
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

## WOODS BAGOT EUROPE LIMITED (`gb:02031503`)

- registration: `02031503` (GB), status active, incorporated 1986-06-26
- classification: ['71111', '71129'] (sic_2007)
- records: 41 officers, 0 beneficial owners, 1 ownership statements, 9 security interests, 219 filings, 0 events, 3 source documents

_No figures persisted for this company._

Coverage @ 2025-06-30: 0/21 concepts available
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

## VIRTUAL SCIENCE LTD (`gb:02228420`)

- registration: `02228420` (GB), status active, incorporated 1988-03-09
- classification: ['62090'] (sic_2007)
- records: 3 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 92 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | xbrli:pure | 2026-03-31 | 2026-07-23 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 27535 | GBP | 2026-03-31 | 2026-07-23 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 27535 | GBP | 2026-03-31 | 2026-07-23 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 0 | GBP | 2026-03-31 | 2026-07-23 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 20700 | GBP | 2026-03-31 | 2026-07-23 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 20600 | GBP | 2026-03-31 | 2026-07-23 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2026-03-31 | 2026-07-23 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | 20154 | GBP | 2026-03-31 | 2026-07-23 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 20700 | GBP | 2026-03-31 | 2026-07-23 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0 | xbrli:pure | 2025-03-31 | 2025-10-01 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 0 | xbrli:pure | 2025-03-31 | 2026-07-23 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 222 | GBP | 2025-03-31 | 2026-07-23 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 222 | GBP | 2025-03-31 | 2025-10-01 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 1034 | GBP | 2025-03-31 | 2026-07-23 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 1034 | GBP | 2025-03-31 | 2025-10-01 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 812 | GBP | 2025-03-31 | 2025-10-01 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 812 | GBP | 2025-03-31 | 2026-07-23 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 812 | GBP | 2025-03-31 | 2025-10-01 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 14011 | GBP | 2025-03-31 | 2025-10-01 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 14011 | GBP | 2025-03-31 | 2026-07-23 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-03-31 | 2026-07-23 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 13911 | GBP | 2025-03-31 | 2026-07-23 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 13911 | GBP | 2025-03-31 | 2025-10-01 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-03-31 | 2025-10-01 | filed | no | `ns5:Equity` | total-exemption-full |
| net_current_assets | -59623 | GBP | 2025-03-31 | 2025-10-01 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -59623 | GBP | 2025-03-31 | 2026-07-23 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 14011 | GBP | 2025-03-31 | 2026-07-23 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 14011 | GBP | 2025-03-31 | 2025-10-01 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-03-31 | 2024-08-21 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-03-31 | 2025-10-01 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 222 | GBP | 2024-03-31 | 2024-08-21 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 222 | GBP | 2024-03-31 | 2025-10-01 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 436 | GBP | 2024-03-31 | 2025-10-01 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 436 | GBP | 2024-03-31 | 2024-08-21 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 214 | GBP | 2024-03-31 | 2024-08-21 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 214 | GBP | 2024-03-31 | 2025-10-01 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 214 | GBP | 2024-03-31 | 2025-10-01 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 24389 | GBP | 2024-03-31 | 2025-10-01 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 24489 | GBP | 2024-03-31 | 2024-08-21 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 24489 | GBP | 2024-03-31 | 2025-10-01 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 24389 | GBP | 2024-03-31 | 2024-08-21 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-03-31 | 2024-08-21 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-03-31 | 2025-10-01 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | -49199 | GBP | 2024-03-31 | 2025-10-01 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -49199 | GBP | 2024-03-31 | 2024-08-21 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 24489 | GBP | 2024-03-31 | 2025-10-01 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 24489 | GBP | 2024-03-31 | 2024-08-21 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-03-31 | 2024-08-21 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 223 | GBP | 2023-03-31 | 2024-08-21 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 223 | GBP | 2023-03-31 | 2024-08-21 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 0 | GBP | 2023-03-31 | 2024-08-21 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 31076 | GBP | 2023-03-31 | 2024-08-21 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-03-31 | 2024-08-21 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 31176 | GBP | 2023-03-31 | 2024-08-21 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | -42685 | GBP | 2023-03-31 | 2024-08-21 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 31176 | GBP | 2023-03-31 | 2024-08-21 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## JACOBSGIBB LTD (`gb:02387707`)

- registration: `02387707` (GB), status active, incorporated 1989-05-22
- classification: ['71129'] (sic_2007)
- records: 74 officers, 3 beneficial owners, 0 ownership statements, 9 security interests, 321 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## DELTAXML LIMITED (`gb:02528681`)

- registration: `02528681` (GB), status active, incorporated 1990-08-07
- classification: ['58290', '62020', '62090'] (sic_2007)
- records: 7 officers, 5 beneficial owners, 0 ownership statements, 2 security interests, 111 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.26 | xbrli:pure | 2025-08-31 | 2026-03-25 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 719601 | GBP | 2025-08-31 | 2026-03-25 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| current_assets | 1044237 | GBP | 2025-08-31 | 2026-03-25 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 324636 | GBP | 2025-08-31 | 2026-03-25 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 322942 | GBP | 2025-08-31 | 2026-03-25 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShares'}` | 960 | GBP | 2025-08-31 | 2026-03-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 925 | GBP | 2025-08-31 | 2026-03-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass2'}` | 35 | GBP | 2025-08-31 | 2026-03-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 960 | GBP | 2025-08-31 | 2026-03-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 262738 | GBP | 2025-08-31 | 2026-03-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 263698 | GBP | 2025-08-31 | 2026-03-25 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 263698 | GBP | 2025-08-31 | 2026-03-25 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 251600 | GBP | 2025-08-31 | 2026-03-25 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 264662 | GBP | 2025-08-31 | 2026-03-25 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0.26 | xbrli:pure | 2024-08-31 | 2026-03-25 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 26 | xbrli:pure | 2024-08-31 | 2025-03-21 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 1003503 | GBP | 2024-08-31 | 2026-03-25 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 1003503 | GBP | 2024-08-31 | 2025-03-21 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1008369 | GBP | 2024-08-31 | 2025-03-21 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 1245265 | GBP | 2024-08-31 | 2026-03-25 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 1245265 | GBP | 2024-08-31 | 2025-03-21 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 241762 | GBP | 2024-08-31 | 2026-03-25 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 241762 | GBP | 2024-08-31 | 2026-03-25 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 241762 | GBP | 2024-08-31 | 2025-03-21 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 241762 | GBP | 2024-08-31 | 2025-03-21 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 960 | GBP | 2024-08-31 | 2025-03-21 | filed | no | `core:Equity` | total-exemption-full |
| equity | 249893 | GBP | 2024-08-31 | 2026-03-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShares'}` | 960 | GBP | 2024-08-31 | 2025-03-21 | filed | no | `core:Equity` | total-exemption-full |
| equity | 249893 | GBP | 2024-08-31 | 2025-03-21 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 248933 | GBP | 2024-08-31 | 2025-03-21 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShares'}` | 960 | GBP | 2024-08-31 | 2026-03-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 925 | GBP | 2024-08-31 | 2026-03-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 960 | GBP | 2024-08-31 | 2026-03-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass2'}` | 35 | GBP | 2024-08-31 | 2026-03-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 248933 | GBP | 2024-08-31 | 2026-03-25 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 249893 | GBP | 2024-08-31 | 2025-03-21 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 249893 | GBP | 2024-08-31 | 2026-03-25 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 236896 | GBP | 2024-08-31 | 2025-03-21 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 236896 | GBP | 2024-08-31 | 2026-03-25 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 254226 | GBP | 2024-08-31 | 2026-03-25 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 254226 | GBP | 2024-08-31 | 2025-03-21 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 28 | xbrli:pure | 2023-08-31 | 2025-03-21 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 28 | xbrli:pure | 2023-08-31 | 2024-03-04 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 1104472 | GBP | 2023-08-31 | 2024-03-04 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 1104472 | GBP | 2023-08-31 | 2025-03-21 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 842929 | GBP | 2023-08-31 | 2025-03-21 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 842929 | GBP | 2023-08-31 | 2024-03-04 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 1370900 | GBP | 2023-08-31 | 2025-03-21 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 1370900 | GBP | 2023-08-31 | 2024-03-04 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors | 266428 | GBP | 2023-08-31 | 2025-03-21 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 266428 | GBP | 2023-08-31 | 2024-03-04 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 266428 | GBP | 2023-08-31 | 2025-03-21 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 266428 | GBP | 2023-08-31 | 2024-03-04 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 546200 | GBP | 2023-08-31 | 2025-03-21 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 547160 | GBP | 2023-08-31 | 2024-03-04 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 960 | GBP | 2023-08-31 | 2025-03-21 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShares'}` | 960 | GBP | 2023-08-31 | 2024-03-04 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 546200 | GBP | 2023-08-31 | 2024-03-04 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 960 | GBP | 2023-08-31 | 2024-03-04 | filed | no | `core:Equity` | total-exemption-full |
| equity | 547160 | GBP | 2023-08-31 | 2025-03-21 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShares'}` | 960 | GBP | 2023-08-31 | 2025-03-21 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 547160 | GBP | 2023-08-31 | 2025-03-21 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 547160 | GBP | 2023-08-31 | 2024-03-04 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 527971 | GBP | 2023-08-31 | 2024-03-04 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 527971 | GBP | 2023-08-31 | 2025-03-21 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 553557 | GBP | 2023-08-31 | 2024-03-04 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 553557 | GBP | 2023-08-31 | 2025-03-21 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 25 | xbrli:pure | 2022-08-31 | 2024-03-04 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 1347359 | GBP | 2022-08-31 | 2024-03-04 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1532758 | GBP | 2022-08-31 | 2024-03-04 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 1715388 | GBP | 2022-08-31 | 2024-03-04 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 368029 | GBP | 2022-08-31 | 2024-03-04 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 368029 | GBP | 2022-08-31 | 2024-03-04 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 205955 | GBP | 2022-08-31 | 2024-03-04 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 206915 | GBP | 2022-08-31 | 2024-03-04 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 960 | GBP | 2022-08-31 | 2024-03-04 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShares'}` | 960 | GBP | 2022-08-31 | 2024-03-04 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 206915 | GBP | 2022-08-31 | 2024-03-04 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 182630 | GBP | 2022-08-31 | 2024-03-04 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 212612 | GBP | 2022-08-31 | 2024-03-04 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2026-03-25: `{"superseded_document_id": "gb:02528681:doc:h4gBZxgSvqDO_OFNyzU-QDpo6eBXLTtZdFHmvdKEnh8", "restatements": [{"concept": "average_employees", "period_end": "2024-08-31", "old_value": "26.0000", "new_val`

## INVENIAM CONSORTIUM LTD (`gb:02671140`)

- registration: `02671140` (GB), status active, incorporated 1991-12-13
- classification: ['62020'] (sic_2007)
- records: 6 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 103 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-06-30 | 2026-01-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 4287 | GBP | 2025-06-30 | 2026-01-30 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 12131 | GBP | 2025-06-30 | 2026-01-30 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 31306 | GBP | 2025-06-30 | 2026-01-30 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 27019 | GBP | 2025-06-30 | 2026-01-30 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2025-06-30 | 2026-01-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 22659 | GBP | 2025-06-30 | 2026-01-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 22658 | GBP | 2025-06-30 | 2026-01-30 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 22659 | GBP | 2025-06-30 | 2026-01-30 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 19175 | GBP | 2025-06-30 | 2026-01-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-06-30 | 2026-01-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-06-30 | 2025-03-05 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 3787 | GBP | 2024-06-30 | 2026-01-30 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 3787 | GBP | 2024-06-30 | 2025-03-05 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 18614 | GBP | 2024-06-30 | 2025-03-05 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 18614 | GBP | 2024-06-30 | 2026-01-30 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 24484 | GBP | 2024-06-30 | 2025-03-05 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 24484 | GBP | 2024-06-30 | 2026-01-30 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 20697 | GBP | 2024-06-30 | 2025-03-05 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 385 | GBP | 2024-06-30 | 2025-03-05 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 20697 | GBP | 2024-06-30 | 2026-01-30 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 6784 | GBP | 2024-06-30 | 2025-03-05 | filed | no | `core:Equity` | total-exemption-full |
| equity | 6785 | GBP | 2024-06-30 | 2025-03-05 | filed | no | `core:Equity` | total-exemption-full |
| equity | 6785 | GBP | 2024-06-30 | 2026-01-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2024-06-30 | 2026-01-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2024-06-30 | 2025-03-05 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 6784 | GBP | 2024-06-30 | 2026-01-30 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 6785 | GBP | 2024-06-30 | 2026-01-30 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 6785 | GBP | 2024-06-30 | 2025-03-05 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 5870 | GBP | 2024-06-30 | 2025-03-05 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 5870 | GBP | 2024-06-30 | 2026-01-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-06-30 | 2025-03-05 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-06-30 | 2024-03-28 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 17765 | GBP | 2023-06-30 | 2025-03-05 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 17765 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 15125 | GBP | 2023-06-30 | 2025-03-05 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 15125 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 23099 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 23099 | GBP | 2023-06-30 | 2025-03-05 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 580 | GBP | 2023-06-30 | 2025-03-05 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 580 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 5334 | GBP | 2023-06-30 | 2025-03-05 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 5334 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `core:Equity` | total-exemption-full |
| equity | 9635 | GBP | 2023-06-30 | 2025-03-05 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2023-06-30 | 2025-03-05 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 9635 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 9634 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 9634 | GBP | 2023-06-30 | 2025-03-05 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 9635 | GBP | 2023-06-30 | 2025-03-05 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 9635 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 7974 | GBP | 2023-06-30 | 2025-03-05 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 7974 | GBP | 2023-06-30 | 2024-03-28 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2022-06-30 | 2024-03-28 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 6625 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 10606 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 14462 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 6222 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 7837 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 4965 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 4966 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 4966 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 3856 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |

Coverage @ 2025-06-30: 8/21 concepts available (average_employees, cash, creditors_within_one_year, current_assets, debtors, equity, net_assets, net_current_assets)
- `creditors_after_one_year`: filed_without_concept — absent though regime 'total-exemption-full' typically includes it
- `depreciation_amortisation`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `fixed_assets`: filed_without_concept — absent though regime 'total-exemption-full' typically includes it
- `gross_profit`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `operating_profit`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `profit_before_tax`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `profit_for_period`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `retained_earnings`: filed_without_concept — absent though regime 'total-exemption-full' typically includes it
- `revenue`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `share_capital`: filed_without_concept — absent though regime 'total-exemption-full' typically includes it
- `staff_costs`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `tax_charge`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `total_assets_less_current_liabilities`: filed_without_concept — absent though regime 'total-exemption-full' typically includes it
