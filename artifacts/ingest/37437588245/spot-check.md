# Ingest spot-check

- database: `data/engine.db`
- latest run: `20261006T084008Z-ff17bbee`
- companies in store: 20200; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## PETRAMODE LIMITED (`gb:02050819`)

- registration: `02050819` (GB), status active, incorporated 1986-08-29
- classification: ['62012', '62020', '63110', '74202'] (sic_2007)
- records: 2 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 101 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-04-30 | 2025-08-27 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 241751 | GBP | 2025-04-30 | 2025-08-27 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 65715 | GBP | 2025-04-30 | 2025-08-27 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 246821 | GBP | 2025-04-30 | 2025-08-27 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 5070 | GBP | 2025-04-30 | 2025-08-27 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 182149 | GBP | 2025-04-30 | 2025-08-27 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 182145 | GBP | 2025-04-30 | 2025-08-27 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 4 | GBP | 2025-04-30 | 2025-08-27 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 1043 | GBP | 2025-04-30 | 2025-08-27 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | 182149 | GBP | 2025-04-30 | 2025-08-27 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 181106 | GBP | 2025-04-30 | 2025-08-27 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 182149 | GBP | 2025-04-30 | 2025-08-27 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-04-30 | 2025-08-27 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-04-30 | 2025-01-15 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 257902 | GBP | 2024-04-30 | 2025-01-15 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 257902 | GBP | 2024-04-30 | 2025-08-27 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 104404 | GBP | 2024-04-30 | 2025-01-15 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 104404 | GBP | 2024-04-30 | 2025-08-27 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 289223 | GBP | 2024-04-30 | 2025-08-27 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 289223 | GBP | 2024-04-30 | 2025-01-15 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors | 31321 | GBP | 2024-04-30 | 2025-08-27 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 31321 | GBP | 2024-04-30 | 2025-01-15 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 186374 | GBP | 2024-04-30 | 2025-08-27 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 4 | GBP | 2024-04-30 | 2025-01-15 | filed | no | `core:Equity` | total-exemption-full |
| equity | 186378 | GBP | 2024-04-30 | 2025-01-15 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 4 | GBP | 2024-04-30 | 2025-08-27 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 186378 | GBP | 2024-04-30 | 2025-08-27 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 186374 | GBP | 2024-04-30 | 2025-01-15 | filed | no | `core:Equity` | total-exemption-full |
| fixed_assets | 1559 | GBP | 2024-04-30 | 2025-01-15 | filed | no | `core:FixedAssets` | total-exemption-full |
| fixed_assets | 1559 | GBP | 2024-04-30 | 2025-08-27 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | 186378 | GBP | 2024-04-30 | 2025-01-15 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 186378 | GBP | 2024-04-30 | 2025-08-27 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 184819 | GBP | 2024-04-30 | 2025-01-15 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 184819 | GBP | 2024-04-30 | 2025-08-27 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 186378 | GBP | 2024-04-30 | 2025-08-27 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 186378 | GBP | 2024-04-30 | 2025-01-15 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-04-30 | 2023-10-25 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-04-30 | 2025-01-15 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 270801 | GBP | 2023-04-30 | 2023-10-25 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 270801 | GBP | 2023-04-30 | 2025-01-15 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 90892 | GBP | 2023-04-30 | 2025-01-15 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 90892 | GBP | 2023-04-30 | 2023-10-25 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 311919 | GBP | 2023-04-30 | 2025-01-15 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 311919 | GBP | 2023-04-30 | 2023-10-25 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors | 41118 | GBP | 2023-04-30 | 2023-10-25 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 41118 | GBP | 2023-04-30 | 2025-01-15 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 4 | GBP | 2023-04-30 | 2023-10-25 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 4 | GBP | 2023-04-30 | 2025-01-15 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 229427 | GBP | 2023-04-30 | 2025-01-15 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 229427 | GBP | 2023-04-30 | 2023-10-25 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 229423 | GBP | 2023-04-30 | 2025-01-15 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 229423 | GBP | 2023-04-30 | 2023-10-25 | filed | no | `core:Equity` | total-exemption-full |
| fixed_assets | 8400 | GBP | 2023-04-30 | 2025-01-15 | filed | yes | `core:FixedAssets` | total-exemption-full |
| fixed_assets | 8400 | GBP | 2023-04-30 | 2023-10-25 | filed | no | `core:FixedAssets` | total-exemption-full |
| net_assets | 229427 | GBP | 2023-04-30 | 2023-10-25 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 229427 | GBP | 2023-04-30 | 2025-01-15 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 221027 | GBP | 2023-04-30 | 2025-01-15 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 221027 | GBP | 2023-04-30 | 2023-10-25 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 229427 | GBP | 2023-04-30 | 2023-10-25 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 229427 | GBP | 2023-04-30 | 2025-01-15 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2022-04-30 | 2023-10-25 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 223347 | GBP | 2022-04-30 | 2023-10-25 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 184055 | GBP | 2022-04-30 | 2023-10-25 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 373562 | GBP | 2022-04-30 | 2023-10-25 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 150215 | GBP | 2022-04-30 | 2023-10-25 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 4 | GBP | 2022-04-30 | 2023-10-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 207521 | GBP | 2022-04-30 | 2023-10-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 207525 | GBP | 2022-04-30 | 2023-10-25 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 18018 | GBP | 2022-04-30 | 2023-10-25 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | 207525 | GBP | 2022-04-30 | 2023-10-25 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 189507 | GBP | 2022-04-30 | 2023-10-25 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 207525 | GBP | 2022-04-30 | 2023-10-25 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## SAI360 LIMITED (`gb:02583952`)

- registration: `02583952` (GB), status active, incorporated 1991-02-20
- classification: ['62090'] (sic_2007)
- records: 33 officers, 2 beneficial owners, 1 ownership statements, 6 security interests, 185 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## CHARLES KANGAI ASSOCIATES LIMITED (`gb:02956476`)

- registration: `02956476` (GB), status active, incorporated 1994-08-08
- classification: ['62020'] (sic_2007)
- records: 4 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 87 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | xbrli:pure | 2025-03-31 | 2026-04-30 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 4 | GBP | 2025-03-31 | 2026-04-30 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 171175 | GBP | 2025-03-31 | 2026-04-30 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 171171 | GBP | 2025-03-31 | 2026-04-30 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 171171 | GBP | 2025-03-31 | 2026-04-30 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 1876 | GBP | 2025-03-31 | 2026-04-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2025-03-31 | 2026-04-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 876 | GBP | 2025-03-31 | 2026-04-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 1876 | GBP | 2025-03-31 | 2026-04-30 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 34325 | GBP | 2025-03-31 | 2026-04-30 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 65250 | GBP | 2025-03-31 | 2026-04-30 | filed | yes | `ns5:ProfitLoss` | total-exemption-full |
| total_assets_less_current_liabilities | 36165 | GBP | 2025-03-31 | 2026-04-30 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-03-31 | 2025-09-01 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-03-31 | 2026-04-30 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 4 | GBP | 2024-03-31 | 2026-04-30 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 4 | GBP | 2024-03-31 | 2025-09-01 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 153280 | GBP | 2024-03-31 | 2025-09-01 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 153280 | GBP | 2024-03-31 | 2026-04-30 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 153276 | GBP | 2024-03-31 | 2025-09-01 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 153276 | GBP | 2024-03-31 | 2026-04-30 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 153276 | GBP | 2024-03-31 | 2026-04-30 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 153276 | GBP | 2024-03-31 | 2025-09-01 | filed | no | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 365 | GBP | 2024-03-31 | 2025-09-01 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2024-03-31 | 2025-09-01 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 365 | GBP | 2024-03-31 | 2026-04-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2024-03-31 | 2026-04-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 1365 | GBP | 2024-03-31 | 2025-09-01 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 1365 | GBP | 2024-03-31 | 2026-04-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 1365 | GBP | 2024-03-31 | 2026-04-30 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 1365 | GBP | 2024-03-31 | 2025-09-01 | filed | no | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 40171 | GBP | 2024-03-31 | 2025-09-01 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 40171 | GBP | 2024-03-31 | 2026-04-30 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 44141 | GBP | 2024-03-31 | 2025-09-01 | filed | yes | `ns5:ProfitLoss` | total-exemption-full |
| total_assets_less_current_liabilities | 42903 | GBP | 2024-03-31 | 2025-09-01 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 42903 | GBP | 2024-03-31 | 2026-04-30 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 1 | xbrli:pure | 2023-03-31 | 2023-12-30 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-03-31 | 2025-09-01 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 11406 | GBP | 2023-03-31 | 2023-12-30 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 11406 | GBP | 2023-03-31 | 2025-09-01 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 39063 | GBP | 2023-03-31 | 2025-09-01 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 39063 | GBP | 2023-03-31 | 2023-12-30 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original'}` | 27657 | GBP | 2023-03-31 | 2023-12-30 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 27657 | GBP | 2023-03-31 | 2023-12-30 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 27657 | GBP | 2023-03-31 | 2025-09-01 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 27657 | GBP | 2023-03-31 | 2025-09-01 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 1000 | GBP | 2023-03-31 | 2023-12-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 1626 | GBP | 2023-03-31 | 2023-12-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 626 | GBP | 2023-03-31 | 2025-09-01 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 1626 | GBP | 2023-03-31 | 2025-09-01 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2023-03-31 | 2025-09-01 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 626 | GBP | 2023-03-31 | 2023-12-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 1626 | GBP | 2023-03-31 | 2025-09-01 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets `{'OriginalRevisedDataDimension': 'Original'}` | 1626 | GBP | 2023-03-31 | 2023-12-30 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 5270 | GBP | 2023-03-31 | 2023-12-30 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 5270 | GBP | 2023-03-31 | 2025-09-01 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_for_period `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 89797 | GBP | 2023-03-31 | 2023-12-30 | filed | yes | `ns5:ProfitLoss` | total-exemption-full |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 10376 | GBP | 2023-03-31 | 2023-12-30 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 10376 | GBP | 2023-03-31 | 2025-09-01 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 1 | xbrli:pure | 2022-03-31 | 2023-12-30 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 3622 | GBP | 2022-03-31 | 2023-12-30 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 38177 | GBP | 2022-03-31 | 2023-12-30 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original'}` | 34555 | GBP | 2022-03-31 | 2023-12-30 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 34555 | GBP | 2022-03-31 | 2023-12-30 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 1000 | GBP | 2022-03-31 | 2023-12-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 1129 | GBP | 2022-03-31 | 2023-12-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 129 | GBP | 2022-03-31 | 2023-12-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets `{'OriginalRevisedDataDimension': 'Original'}` | 1129 | GBP | 2022-03-31 | 2023-12-30 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 9134 | GBP | 2022-03-31 | 2023-12-30 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 12879 | GBP | 2022-03-31 | 2023-12-30 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## SAFENET LIMITED (`gb:03221595`)

- registration: `03221595` (GB), status active, incorporated 1996-07-08
- classification: ['71122', '71200'] (sic_2007)
- records: 7 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 93 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.03 | xbrli:pure | 2025-07-31 | 2026-02-04 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 68425 | GBP | 2025-07-31 | 2026-02-04 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 21903 | GBP | 2025-07-31 | 2026-02-04 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 165784 | GBP | 2025-07-31 | 2026-02-04 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 97359 | GBP | 2025-07-31 | 2026-02-04 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 97359 | GBP | 2025-07-31 | 2026-02-04 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 179578 | GBP | 2025-07-31 | 2026-02-04 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-07-31 | 2026-02-04 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 179478 | GBP | 2025-07-31 | 2026-02-04 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 179578 | GBP | 2025-07-31 | 2026-02-04 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 143881 | GBP | 2025-07-31 | 2026-02-04 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 185384 | GBP | 2025-07-31 | 2026-02-04 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0.03 | xbrli:pure | 2024-07-31 | 2026-02-04 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 3 | xbrli:pure | 2024-07-31 | 2025-03-10 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 48739 | GBP | 2024-07-31 | 2025-03-10 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 48739 | GBP | 2024-07-31 | 2026-02-04 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 38012 | GBP | 2024-07-31 | 2026-02-04 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 38012 | GBP | 2024-07-31 | 2025-03-10 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 220660 | GBP | 2024-07-31 | 2026-02-04 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 220660 | GBP | 2024-07-31 | 2025-03-10 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 171921 | GBP | 2024-07-31 | 2026-02-04 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 171921 | GBP | 2024-07-31 | 2025-03-10 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 171921 | GBP | 2024-07-31 | 2026-02-04 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 171921 | GBP | 2024-07-31 | 2025-03-10 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 225257 | GBP | 2024-07-31 | 2025-03-10 | filed | no | `core:Equity` | total-exemption-full |
| equity | 225357 | GBP | 2024-07-31 | 2025-03-10 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-07-31 | 2025-03-10 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-07-31 | 2026-02-04 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 225257 | GBP | 2024-07-31 | 2026-02-04 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 225357 | GBP | 2024-07-31 | 2026-02-04 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 225357 | GBP | 2024-07-31 | 2026-02-04 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 225357 | GBP | 2024-07-31 | 2025-03-10 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 182648 | GBP | 2024-07-31 | 2025-03-10 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 182648 | GBP | 2024-07-31 | 2026-02-04 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 232643 | GBP | 2024-07-31 | 2025-03-10 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 232643 | GBP | 2024-07-31 | 2026-02-04 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 3 | xbrli:pure | 2023-07-31 | 2024-01-02 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 3 | xbrli:pure | 2023-07-31 | 2025-03-10 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 103962 | GBP | 2023-07-31 | 2024-01-02 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 103962 | GBP | 2023-07-31 | 2025-03-10 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 21276 | GBP | 2023-07-31 | 2025-03-10 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 21276 | GBP | 2023-07-31 | 2024-01-02 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 167716 | GBP | 2023-07-31 | 2025-03-10 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 167716 | GBP | 2023-07-31 | 2024-01-02 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 63754 | GBP | 2023-07-31 | 2025-03-10 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 63754 | GBP | 2023-07-31 | 2024-01-02 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 63754 | GBP | 2023-07-31 | 2025-03-10 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 63754 | GBP | 2023-07-31 | 2024-01-02 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 185976 | GBP | 2023-07-31 | 2025-03-10 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 186076 | GBP | 2023-07-31 | 2025-03-10 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-07-31 | 2024-01-02 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 185976 | GBP | 2023-07-31 | 2024-01-02 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-07-31 | 2025-03-10 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 186076 | GBP | 2023-07-31 | 2024-01-02 | filed | no | `core:Equity` | total-exemption-full |
| net_assets | 186076 | GBP | 2023-07-31 | 2024-01-02 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 186076 | GBP | 2023-07-31 | 2025-03-10 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 146440 | GBP | 2023-07-31 | 2025-03-10 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 146440 | GBP | 2023-07-31 | 2024-01-02 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 195159 | GBP | 2023-07-31 | 2024-01-02 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 195159 | GBP | 2023-07-31 | 2025-03-10 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 3 | xbrli:pure | 2022-07-31 | 2024-01-02 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 51677 | GBP | 2022-07-31 | 2024-01-02 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 23972 | GBP | 2022-07-31 | 2024-01-02 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 175003 | GBP | 2022-07-31 | 2024-01-02 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 123326 | GBP | 2022-07-31 | 2024-01-02 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 123326 | GBP | 2022-07-31 | 2024-01-02 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 202813 | GBP | 2022-07-31 | 2024-01-02 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 202913 | GBP | 2022-07-31 | 2024-01-02 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2022-07-31 | 2024-01-02 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 202913 | GBP | 2022-07-31 | 2024-01-02 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 151031 | GBP | 2022-07-31 | 2024-01-02 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 211913 | GBP | 2022-07-31 | 2024-01-02 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2026-02-04: `{"superseded_document_id": "gb:03221595:doc:viVdiSi-PvQDxfj32MAME9mvkbik_57y6WiTQW225pY", "restatements": [{"concept": "average_employees", "period_end": "2024-07-31", "old_value": "3.0000", "new_valu`

## BEART & GIBSON LIMITED (`gb:03465344`)

- registration: `03465344` (GB), status active, incorporated 1997-11-13
- classification: ['41100', '62012', '64999', '66120'] (sic_2007)
- records: 10 officers, 1 beneficial owners, 0 ownership statements, 2 security interests, 105 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | xbrli:pure | 2026-03-31 | 2026-09-02 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 7583 | GBP | 2026-03-31 | 2026-09-02 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 66706 | GBP | 2026-03-31 | 2026-09-02 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 84857 | GBP | 2026-03-31 | 2026-09-02 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 49893 | GBP | 2026-03-31 | 2026-09-02 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 43625 | GBP | 2026-03-31 | 2026-09-02 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 49893 | GBP | 2026-03-31 | 2026-09-02 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 18151 | GBP | 2026-03-31 | 2026-09-02 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 61776 | GBP | 2026-03-31 | 2026-09-02 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2025-03-31 | 2026-09-02 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | xbrli:pure | 2025-03-31 | 2026-01-21 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 10558 | GBP | 2025-03-31 | 2026-09-02 | filed | yes | `core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 10558 | GBP | 2025-03-31 | 2026-01-21 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 65580 | GBP | 2025-03-31 | 2026-09-02 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 65580 | GBP | 2025-03-31 | 2026-01-21 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 84831 | GBP | 2025-03-31 | 2026-09-02 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 84831 | GBP | 2025-03-31 | 2026-01-21 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 48839 | GBP | 2025-03-31 | 2026-01-21 | filed | no | `core:Equity` | micro-entity |
| equity | 48839 | GBP | 2025-03-31 | 2026-09-02 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 43696 | GBP | 2025-03-31 | 2026-09-02 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 43696 | GBP | 2025-03-31 | 2026-01-21 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | 48839 | GBP | 2025-03-31 | 2026-09-02 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 48839 | GBP | 2025-03-31 | 2026-01-21 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 19251 | GBP | 2025-03-31 | 2026-01-21 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 19251 | GBP | 2025-03-31 | 2026-09-02 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 62947 | GBP | 2025-03-31 | 2026-01-21 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 62947 | GBP | 2025-03-31 | 2026-09-02 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2024-03-31 | 2024-12-20 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | xbrli:pure | 2024-03-31 | 2026-01-21 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 13545 | GBP | 2024-03-31 | 2026-01-21 | filed | yes | `core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 13545 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 65534 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 65534 | GBP | 2024-03-31 | 2026-01-21 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 84982 | GBP | 2024-03-31 | 2026-01-21 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 84982 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 46888 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:Equity` | micro-entity |
| equity | 46888 | GBP | 2024-03-31 | 2026-01-21 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 43785 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 43785 | GBP | 2024-03-31 | 2026-01-21 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 46888 | GBP | 2024-03-31 | 2026-01-21 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 46888 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 19448 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 19448 | GBP | 2024-03-31 | 2026-01-21 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 63233 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 63233 | GBP | 2024-03-31 | 2026-01-21 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2023-03-31 | 2024-12-20 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 19519 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 62758 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 87911 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 46516 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 43932 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 46516 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 25153 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 69085 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## SQUARE ENIX (2009) LIMITED (`gb:03679704`)

- registration: `03679704` (GB), status active, incorporated 1998-12-01
- classification: ['58210', '62011'] (sic_2007)
- records: 26 officers, 1 beneficial owners, 0 ownership statements, 1 security interests, 127 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## NEW MEDIA AID LIMITED (`gb:03903923`)

- registration: `03903923` (GB), status active, incorporated 2000-01-10
- classification: ['62012'] (sic_2007)
- records: 3 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 59 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2026-01-31 | 2026-06-03 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 45776 | GBP | 2026-01-31 | 2026-06-03 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 55476 | GBP | 2026-01-31 | 2026-06-03 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 9700 | GBP | 2026-01-31 | 2026-06-03 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2026-01-31 | 2026-06-03 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 22560 | GBP | 2026-01-31 | 2026-06-03 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 278 | GBP | 2026-01-31 | 2026-06-03 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 22660 | GBP | 2026-01-31 | 2026-06-03 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 22382 | GBP | 2026-01-31 | 2026-06-03 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 22660 | GBP | 2026-01-31 | 2026-06-03 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2025-01-31 | 2026-06-03 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2025-01-31 | 2025-04-15 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 54379 | GBP | 2025-01-31 | 2026-06-03 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| cash | 54379 | GBP | 2025-01-31 | 2025-04-15 | filed | no | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 57603 | GBP | 2025-01-31 | 2026-06-03 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| current_assets | 57603 | GBP | 2025-01-31 | 2025-04-15 | filed | no | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 3224 | GBP | 2025-01-31 | 2026-06-03 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| debtors | 3224 | GBP | 2025-01-31 | 2025-04-15 | filed | no | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 20044 | GBP | 2025-01-31 | 2026-06-03 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 20044 | GBP | 2025-01-31 | 2025-04-15 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-01-31 | 2026-06-03 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-01-31 | 2025-04-15 | filed | no | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 556 | GBP | 2025-01-31 | 2026-06-03 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| fixed_assets | 556 | GBP | 2025-01-31 | 2025-04-15 | filed | no | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 20144 | GBP | 2025-01-31 | 2026-06-03 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 20144 | GBP | 2025-01-31 | 2025-04-15 | filed | no | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 19588 | GBP | 2025-01-31 | 2026-06-03 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 19588 | GBP | 2025-01-31 | 2025-04-15 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 20144 | GBP | 2025-01-31 | 2026-06-03 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 20144 | GBP | 2025-01-31 | 2025-04-15 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-01-31 | 2024-06-10 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-01-31 | 2025-04-15 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 43675 | GBP | 2024-01-31 | 2024-06-10 | filed | no | `frs-core:CashBankOnHand` | total-exemption-full |
| cash | 43675 | GBP | 2024-01-31 | 2025-04-15 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 44933 | GBP | 2024-01-31 | 2024-06-10 | filed | no | `frs-core:CurrentAssets` | total-exemption-full |
| current_assets | 44933 | GBP | 2024-01-31 | 2025-04-15 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 1258 | GBP | 2024-01-31 | 2025-04-15 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| debtors | 1258 | GBP | 2024-01-31 | 2024-06-10 | filed | no | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-01-31 | 2024-06-10 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 9786 | GBP | 2024-01-31 | 2025-04-15 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 9786 | GBP | 2024-01-31 | 2024-06-10 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-01-31 | 2025-04-15 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 187 | GBP | 2024-01-31 | 2024-06-10 | filed | no | `frs-core:FixedAssets` | total-exemption-full |
| fixed_assets | 187 | GBP | 2024-01-31 | 2025-04-15 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 9886 | GBP | 2024-01-31 | 2024-06-10 | filed | no | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 9886 | GBP | 2024-01-31 | 2025-04-15 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 9699 | GBP | 2024-01-31 | 2024-06-10 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 9699 | GBP | 2024-01-31 | 2025-04-15 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 9886 | GBP | 2024-01-31 | 2025-04-15 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 9886 | GBP | 2024-01-31 | 2024-06-10 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-01-31 | 2024-06-10 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 36982 | GBP | 2023-01-31 | 2024-06-10 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 47265 | GBP | 2023-01-31 | 2024-06-10 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 10283 | GBP | 2023-01-31 | 2024-06-10 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 13821 | GBP | 2023-01-31 | 2024-06-10 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-01-31 | 2024-06-10 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 508 | GBP | 2023-01-31 | 2024-06-10 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 13921 | GBP | 2023-01-31 | 2024-06-10 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 13413 | GBP | 2023-01-31 | 2024-06-10 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 13921 | GBP | 2023-01-31 | 2024-06-10 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## TAILOR MADE TECHNOLOGIES LIMITED (`gb:04125178`)

- registration: `04125178` (GB), status active, incorporated 2000-12-13
- classification: ['62012', '62020', '62090', '63110'] (sic_2007)
- records: 28 officers, 3 beneficial owners, 0 ownership statements, 8 security interests, 180 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 110 | xbrli:pure | 2024-12-31 | 2026-03-05 | filed | yes | `c:AverageNumberEmployeesDuringPeriod` | full |
| cash | 38637 | GBP | 2024-12-31 | 2026-03-05 | filed | yes | `c:CashBankOnHand` | full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 70834 | GBP | 2024-12-31 | 2026-03-05 | filed | yes | `c:Creditors` | full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2293680 | GBP | 2024-12-31 | 2026-03-05 | filed | yes | `c:Creditors` | full |
| current_assets | 5515070 | GBP | 2024-12-31 | 2026-03-05 | filed | yes | `c:CurrentAssets` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 5410996 | GBP | 2024-12-31 | 2026-03-05 | filed | yes | `c:Debtors` | full |
| equity | 3297866 | GBP | 2024-12-31 | 2026-03-05 | filed | yes | `c:Equity` | full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 1198 | GBP | 2024-12-31 | 2026-03-05 | filed | yes | `c:Equity` | full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 560 | GBP | 2024-12-31 | 2026-03-05 | filed | yes | `c:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 9886 | GBP | 2024-12-31 | 2026-03-05 | filed | yes | `c:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3286222 | GBP | 2024-12-31 | 2026-03-05 | filed | yes | `c:Equity` | full |
| fixed_assets | 147310 | GBP | 2024-12-31 | 2026-03-05 | filed | yes | `c:FixedAssets` | full |
| gross_profit | 5323347 | GBP | 2024-12-31 | 2026-03-05 | filed | yes | `c:GrossProfitLoss` | full |
| net_assets | 3297866 | GBP | 2024-12-31 | 2026-03-05 | filed | yes | `c:NetAssetsLiabilities` | full |
| net_current_assets | 3221390 | GBP | 2024-12-31 | 2026-03-05 | filed | yes | `c:NetCurrentAssetsLiabilities` | full |
| operating_profit | 1027175 | GBP | 2024-12-31 | 2026-03-05 | filed | yes | `c:OperatingProfitLoss` | full |
| profit_before_tax | 1021705 | GBP | 2024-12-31 | 2026-03-05 | filed | yes | `c:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 900822 | GBP | 2024-12-31 | 2026-03-05 | filed | yes | `c:ProfitLoss` | full |
| profit_for_period | 900822 | GBP | 2024-12-31 | 2026-03-05 | filed | yes | `c:ProfitLoss` | full |
| revenue | 15663157 | GBP | 2024-12-31 | 2026-03-05 | filed | yes | `c:TurnoverRevenue` | full |
| tax_charge | 120883 | GBP | 2024-12-31 | 2026-03-05 | filed | yes | `c:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| total_assets_less_current_liabilities | 3368700 | GBP | 2024-12-31 | 2026-03-05 | filed | yes | `c:TotalAssetsLessCurrentLiabilities` | full |
| average_employees | 112 | xbrli:pure | 2023-12-31 | 2026-03-05 | filed | yes | `c:AverageNumberEmployeesDuringPeriod` | full |
| cash | 396369 | GBP | 2023-12-31 | 2026-03-05 | filed | yes | `c:CashBankOnHand` | full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 84762 | GBP | 2023-12-31 | 2026-03-05 | filed | yes | `c:Creditors` | full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2637962 | GBP | 2023-12-31 | 2026-03-05 | filed | yes | `c:Creditors` | full |
| current_assets | 5535757 | GBP | 2023-12-31 | 2026-03-05 | filed | yes | `c:CurrentAssets` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 5035786 | GBP | 2023-12-31 | 2026-03-05 | filed | yes | `c:Debtors` | full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 1198 | GBP | 2023-12-31 | 2026-03-05 | filed | yes | `c:Equity` | full |
| equity | 3047044 | GBP | 2023-12-31 | 2026-03-05 | filed | yes | `c:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 9886 | GBP | 2023-12-31 | 2026-03-05 | filed | yes | `c:Equity` | full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 560 | GBP | 2023-12-31 | 2026-03-05 | filed | yes | `c:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3035400 | GBP | 2023-12-31 | 2026-03-05 | filed | yes | `c:Equity` | full |
| fixed_assets | 234011 | GBP | 2023-12-31 | 2026-03-05 | filed | yes | `c:FixedAssets` | full |
| gross_profit | 5018708 | GBP | 2023-12-31 | 2026-03-05 | filed | yes | `c:GrossProfitLoss` | full |
| net_assets | 3047044 | GBP | 2023-12-31 | 2026-03-05 | filed | yes | `c:NetAssetsLiabilities` | full |
| net_current_assets | 2897795 | GBP | 2023-12-31 | 2026-03-05 | filed | yes | `c:NetCurrentAssetsLiabilities` | full |
| operating_profit | 835344 | GBP | 2023-12-31 | 2026-03-05 | filed | yes | `c:OperatingProfitLoss` | full |
| profit_before_tax | 825257 | GBP | 2023-12-31 | 2026-03-05 | filed | yes | `c:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 915936 | GBP | 2023-12-31 | 2026-03-05 | filed | yes | `c:ProfitLoss` | full |
| profit_for_period | 915936 | GBP | 2023-12-31 | 2026-03-05 | filed | yes | `c:ProfitLoss` | full |
| revenue | 15348743 | GBP | 2023-12-31 | 2026-03-05 | filed | yes | `c:TurnoverRevenue` | full |
| tax_charge | -90679 | GBP | 2023-12-31 | 2026-03-05 | filed | yes | `c:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| total_assets_less_current_liabilities | 3131806 | GBP | 2023-12-31 | 2026-03-05 | filed | yes | `c:TotalAssetsLessCurrentLiabilities` | full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 560 | GBP | 2023-01-01 | 2026-03-05 | filed | yes | `c:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 9886 | GBP | 2023-01-01 | 2026-03-05 | filed | yes | `c:Equity` | full |
| equity | 2131108 | GBP | 2023-01-01 | 2026-03-05 | filed | yes | `c:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2119464 | GBP | 2023-01-01 | 2026-03-05 | filed | yes | `c:Equity` | full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 1198 | GBP | 2023-01-01 | 2026-03-05 | filed | yes | `c:Equity` | full |

_No coverage facts for the latest run._

## FACETIME LIMITED (`gb:04714174`)

- registration: `04714174` (GB), status active, incorporated 2003-03-27
- classification: ['62090'] (sic_2007)
- records: 5 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 80 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | xbrli:pure | 2025-04-30 | 2025-08-06 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 35791 | GBP | 2025-04-30 | 2025-08-06 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 59220 | GBP | 2025-04-30 | 2025-08-06 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 24613 | GBP | 2025-04-30 | 2025-08-06 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 1184 | GBP | 2025-04-30 | 2025-08-06 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 24613 | GBP | 2025-04-30 | 2025-08-06 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 23429 | GBP | 2025-04-30 | 2025-08-06 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 24613 | GBP | 2025-04-30 | 2025-08-06 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2024-04-30 | 2025-08-06 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-04-30 | 2024-07-10 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 28491 | GBP | 2024-04-30 | 2024-07-10 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 8636 | GBP | 2024-04-30 | 2025-08-06 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 42029 | GBP | 2024-04-30 | 2025-08-06 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 73879 | GBP | 2024-04-30 | 2025-08-06 | filed | yes | `core:CurrentAssets` | micro-entity |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 40138 | GBP | 2024-04-30 | 2024-07-10 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 4 | GBP | 2024-04-30 | 2024-07-10 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 24793 | GBP | 2024-04-30 | 2024-07-10 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 24789 | GBP | 2024-04-30 | 2024-07-10 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 24793 | GBP | 2024-04-30 | 2025-08-06 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 1579 | GBP | 2024-04-30 | 2025-08-06 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 24793 | GBP | 2024-04-30 | 2024-07-10 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 24793 | GBP | 2024-04-30 | 2025-08-06 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 31850 | GBP | 2024-04-30 | 2025-08-06 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 33429 | GBP | 2024-04-30 | 2025-08-06 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-04-30 | 2023-10-10 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-04-30 | 2024-07-10 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 45489 | GBP | 2023-04-30 | 2023-10-10 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 45489 | GBP | 2023-04-30 | 2024-07-10 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 35046 | GBP | 2023-04-30 | 2024-07-10 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 35046 | GBP | 2023-04-30 | 2023-10-10 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 4 | GBP | 2023-04-30 | 2024-07-10 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 21975 | GBP | 2023-04-30 | 2024-07-10 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 21971 | GBP | 2023-04-30 | 2023-10-10 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 4 | GBP | 2023-04-30 | 2023-10-10 | filed | no | `core:Equity` | total-exemption-full |
| equity | 21975 | GBP | 2023-04-30 | 2023-10-10 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 21971 | GBP | 2023-04-30 | 2024-07-10 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 21975 | GBP | 2023-04-30 | 2024-07-10 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 21975 | GBP | 2023-04-30 | 2023-10-10 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2022-04-30 | 2023-10-10 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 25468 | GBP | 2022-04-30 | 2023-10-10 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 37323 | GBP | 2022-04-30 | 2023-10-10 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 4 | GBP | 2022-04-30 | 2023-10-10 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 3910 | GBP | 2022-04-30 | 2023-10-10 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3906 | GBP | 2022-04-30 | 2023-10-10 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 3910 | GBP | 2022-04-30 | 2023-10-10 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2025-08-06: `{"superseded_document_id": "gb:04714174:doc:_OIrmWM-bToZo3PJeZDovjwqbMdVx_-vPW9dc4iF9PA", "restatements": [{"concept": "average_employees", "period_end": "2024-04-30", "old_value": "2.0000", "new_valu`
