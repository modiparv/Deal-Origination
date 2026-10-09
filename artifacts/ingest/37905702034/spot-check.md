# Ingest spot-check

- database: `data/engine.db`
- latest run: `20261009T083421Z-67b59a7e`
- companies in store: 22600; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## FERRET INFORMATION SYSTEMS LIMITED (`gb:02126033`)

- registration: `02126033` (GB), status active, incorporated 1987-04-24
- classification: ['62012', '62090'] (sic_2007)
- records: 5 officers, 1 beneficial owners, 0 ownership statements, 2 security interests, 100 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 7 | xbrli:pure | 2025-03-31 | 2025-11-14 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 70496 | GBP | 2025-03-31 | 2025-11-14 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 238298 | GBP | 2025-03-31 | 2025-11-14 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 167802 | GBP | 2025-03-31 | 2025-11-14 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 167802 | GBP | 2025-03-31 | 2025-11-14 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-03-31 | 2025-11-14 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 178586 | GBP | 2025-03-31 | 2025-11-14 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 207186 | GBP | 2025-03-31 | 2025-11-14 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 28500 | GBP | 2025-03-31 | 2025-11-14 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | 85674 | GBP | 2025-03-31 | 2025-11-14 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1538 | GBP | 2025-03-31 | 2025-11-14 | filed | yes | `ns5:ProfitLoss` | total-exemption-full |
| profit_for_period | 1538 | GBP | 2025-03-31 | 2025-11-14 | filed | yes | `ns5:ProfitLoss` | total-exemption-full |
| total_assets_less_current_liabilities | 207186 | GBP | 2025-03-31 | 2025-11-14 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 8 | xbrli:pure | 2024-03-31 | 2024-12-20 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 8 | xbrli:pure | 2024-03-31 | 2025-11-14 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 131923 | GBP | 2024-03-31 | 2025-11-14 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 131923 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 191864 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 191864 | GBP | 2024-03-31 | 2025-11-14 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 59941 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 59941 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 59941 | GBP | 2024-03-31 | 2025-11-14 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 59941 | GBP | 2024-03-31 | 2025-11-14 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 28500 | GBP | 2024-03-31 | 2025-11-14 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 192048 | GBP | 2024-03-31 | 2025-11-14 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 192048 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 28500 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 220648 | GBP | 2024-03-31 | 2025-11-14 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 220648 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-03-31 | 2025-11-14 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | 93315 | GBP | 2024-03-31 | 2025-11-14 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 93315 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -13684 | GBP | 2024-03-31 | 2024-12-20 | filed | yes | `ns5:ProfitLoss` | total-exemption-full |
| profit_for_period | -13684 | GBP | 2024-03-31 | 2024-12-20 | filed | yes | `ns5:ProfitLoss` | total-exemption-full |
| total_assets_less_current_liabilities | 220648 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 220648 | GBP | 2024-03-31 | 2025-11-14 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 8 | xbrli:pure | 2023-03-31 | 2023-11-07 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 8 | xbrli:pure | 2023-03-31 | 2024-12-20 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 109328 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 109328 | GBP | 2023-03-31 | 2023-11-07 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 175273 | GBP | 2023-03-31 | 2023-11-07 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 175273 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 65945 | GBP | 2023-03-31 | 2023-11-07 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 65945 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 65945 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 65945 | GBP | 2023-03-31 | 2023-11-07 | filed | no | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 242332 | GBP | 2023-03-31 | 2023-11-07 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 242332 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 28500 | GBP | 2023-03-31 | 2023-11-07 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 213732 | GBP | 2023-03-31 | 2023-11-07 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 213732 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-03-31 | 2023-11-07 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 28500 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | 108060 | GBP | 2023-03-31 | 2023-11-07 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 108060 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_for_period | 16951 | GBP | 2023-03-31 | 2023-11-07 | filed | yes | `ns5:ProfitLoss` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 16951 | GBP | 2023-03-31 | 2023-11-07 | filed | yes | `ns5:ProfitLoss` | total-exemption-full |
| total_assets_less_current_liabilities | 242332 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 242332 | GBP | 2023-03-31 | 2023-11-07 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 8 | xbrli:pure | 2022-03-31 | 2023-11-07 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 97314 | GBP | 2022-03-31 | 2023-11-07 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 156275 | GBP | 2022-03-31 | 2023-11-07 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 58961 | GBP | 2022-03-31 | 2023-11-07 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 58961 | GBP | 2022-03-31 | 2023-11-07 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 212781 | GBP | 2022-03-31 | 2023-11-07 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2022-03-31 | 2023-11-07 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 28500 | GBP | 2022-03-31 | 2023-11-07 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 241381 | GBP | 2022-03-31 | 2023-11-07 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | 100228 | GBP | 2022-03-31 | 2023-11-07 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 241381 | GBP | 2022-03-31 | 2023-11-07 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## TQS SE LIMITED (`gb:02689256`)

- registration: `02689256` (GB), status active, incorporated 1992-02-19
- classification: ['62090'] (sic_2007)
- records: 5 officers, 3 beneficial owners, 0 ownership statements, 2 security interests, 98 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 12 | xbrli:pure | 2025-03-31 | 2025-12-22 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 508021 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 552208 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 643168 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 115147 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:Debtors` | total-exemption-full |
| net_assets | 146249 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 90960 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 161358 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 12 | xbrli:pure | 2024-03-31 | 2024-10-02 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 12 | xbrli:pure | 2024-03-31 | 2025-12-22 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 697958 | GBP | 2024-03-31 | 2024-10-02 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 697958 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 549616 | GBP | 2024-03-31 | 2024-10-02 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 549616 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 891810 | GBP | 2024-03-31 | 2024-10-02 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 891810 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 173852 | GBP | 2024-03-31 | 2024-10-02 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 173852 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 173852 | GBP | 2024-03-31 | 2024-10-02 | filed | no | `core:Debtors` | total-exemption-full |
| net_assets | 424039 | GBP | 2024-03-31 | 2024-10-02 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 424039 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 342194 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 342194 | GBP | 2024-03-31 | 2024-10-02 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 447619 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 447619 | GBP | 2024-03-31 | 2024-10-02 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 12 | xbrli:pure | 2023-03-31 | 2023-10-12 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 12 | xbrli:pure | 2023-03-31 | 2024-10-02 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 682609 | GBP | 2023-03-31 | 2023-10-12 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 682609 | GBP | 2023-03-31 | 2024-10-02 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 409632 | GBP | 2023-03-31 | 2024-10-02 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 409632 | GBP | 2023-03-31 | 2023-10-12 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 938612 | GBP | 2023-03-31 | 2023-10-12 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 938612 | GBP | 2023-03-31 | 2024-10-02 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 243003 | GBP | 2023-03-31 | 2023-10-12 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 243003 | GBP | 2023-03-31 | 2024-10-02 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 243003 | GBP | 2023-03-31 | 2024-10-02 | filed | yes | `core:Debtors` | total-exemption-full |
| net_assets | 633007 | GBP | 2023-03-31 | 2024-10-02 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 633007 | GBP | 2023-03-31 | 2023-10-12 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 528980 | GBP | 2023-03-31 | 2023-10-12 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 528980 | GBP | 2023-03-31 | 2024-10-02 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 667683 | GBP | 2023-03-31 | 2024-10-02 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 667683 | GBP | 2023-03-31 | 2023-10-12 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 5 | xbrli:pure | 2022-03-31 | 2023-10-12 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 525934 | GBP | 2022-03-31 | 2023-10-12 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 246217 | GBP | 2022-03-31 | 2023-10-12 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 679738 | GBP | 2022-03-31 | 2023-10-12 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 149804 | GBP | 2022-03-31 | 2023-10-12 | filed | yes | `core:Debtors` | total-exemption-full |
| net_assets | 506824 | GBP | 2022-03-31 | 2023-10-12 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 433521 | GBP | 2022-03-31 | 2023-10-12 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 506824 | GBP | 2022-03-31 | 2023-10-12 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## WHEELER TREVITT CONSULTANTS LIMITED (`gb:03054720`)

- registration: `03054720` (GB), status active, incorporated 1995-05-10
- classification: ['71129'] (sic_2007)
- records: 6 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 80 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-10-31 | 2026-07-30 | filed | yes | `d:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 33066 | GBP | 2025-10-31 | 2026-07-30 | filed | yes | `d:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 129831 | GBP | 2025-10-31 | 2026-07-30 | filed | yes | `d:Creditors` | total-exemption-full |
| current_assets | 34610 | GBP | 2025-10-31 | 2026-07-30 | filed | yes | `d:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 1544 | GBP | 2025-10-31 | 2026-07-30 | filed | yes | `d:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2025-10-31 | 2026-07-30 | filed | yes | `d:Equity` | total-exemption-full |
| equity | -94912 | GBP | 2025-10-31 | 2026-07-30 | filed | yes | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -94914 | GBP | 2025-10-31 | 2026-07-30 | filed | yes | `d:Equity` | total-exemption-full |
| fixed_assets | 309 | GBP | 2025-10-31 | 2026-07-30 | filed | yes | `d:FixedAssets` | total-exemption-full |
| net_assets | -94912 | GBP | 2025-10-31 | 2026-07-30 | filed | yes | `d:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -95221 | GBP | 2025-10-31 | 2026-07-30 | filed | yes | `d:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -94912 | GBP | 2025-10-31 | 2026-07-30 | filed | yes | `d:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-10-31 | 2026-07-30 | filed | yes | `d:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-10-31 | 2026-01-30 | filed | no | `d:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 44129 | GBP | 2024-10-31 | 2026-01-30 | filed | no | `d:CashBankOnHand` | total-exemption-full |
| cash | 44129 | GBP | 2024-10-31 | 2026-07-30 | filed | yes | `d:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 132803 | GBP | 2024-10-31 | 2026-01-30 | filed | no | `d:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 132803 | GBP | 2024-10-31 | 2026-07-30 | filed | yes | `d:Creditors` | total-exemption-full |
| current_assets | 44919 | GBP | 2024-10-31 | 2026-07-30 | filed | yes | `d:CurrentAssets` | total-exemption-full |
| current_assets | 44919 | GBP | 2024-10-31 | 2026-01-30 | filed | no | `d:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 790 | GBP | 2024-10-31 | 2026-01-30 | filed | no | `d:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 790 | GBP | 2024-10-31 | 2026-07-30 | filed | yes | `d:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -87520 | GBP | 2024-10-31 | 2026-01-30 | filed | no | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-10-31 | 2026-07-30 | filed | yes | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-10-31 | 2026-01-30 | filed | no | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -87520 | GBP | 2024-10-31 | 2026-07-30 | filed | yes | `d:Equity` | total-exemption-full |
| equity | -87518 | GBP | 2024-10-31 | 2026-01-30 | filed | no | `d:Equity` | total-exemption-full |
| equity | -87518 | GBP | 2024-10-31 | 2026-07-30 | filed | yes | `d:Equity` | total-exemption-full |
| fixed_assets | 366 | GBP | 2024-10-31 | 2026-01-30 | filed | no | `d:FixedAssets` | total-exemption-full |
| fixed_assets | 366 | GBP | 2024-10-31 | 2026-07-30 | filed | yes | `d:FixedAssets` | total-exemption-full |
| net_assets | -87518 | GBP | 2024-10-31 | 2026-07-30 | filed | yes | `d:NetAssetsLiabilities` | total-exemption-full |
| net_assets | -87518 | GBP | 2024-10-31 | 2026-01-30 | filed | no | `d:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -87884 | GBP | 2024-10-31 | 2026-01-30 | filed | no | `d:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -87884 | GBP | 2024-10-31 | 2026-07-30 | filed | yes | `d:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -87518 | GBP | 2024-10-31 | 2026-01-30 | filed | no | `d:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -87518 | GBP | 2024-10-31 | 2026-07-30 | filed | yes | `d:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-10-31 | 2024-09-19 | filed | no | `d:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-10-31 | 2026-01-30 | filed | yes | `d:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 52950 | GBP | 2023-10-31 | 2024-09-19 | filed | no | `d:CashBankOnHand` | total-exemption-full |
| cash | 52950 | GBP | 2023-10-31 | 2026-01-30 | filed | yes | `d:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 130972 | GBP | 2023-10-31 | 2026-01-30 | filed | yes | `d:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 130972 | GBP | 2023-10-31 | 2024-09-19 | filed | no | `d:Creditors` | total-exemption-full |
| current_assets | 55707 | GBP | 2023-10-31 | 2026-01-30 | filed | yes | `d:CurrentAssets` | total-exemption-full |
| current_assets | 55707 | GBP | 2023-10-31 | 2024-09-19 | filed | no | `d:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 2757 | GBP | 2023-10-31 | 2026-01-30 | filed | yes | `d:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 2757 | GBP | 2023-10-31 | 2024-09-19 | filed | no | `d:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -74808 | GBP | 2023-10-31 | 2024-09-19 | filed | no | `d:Equity` | total-exemption-full |
| equity | -74806 | GBP | 2023-10-31 | 2024-09-19 | filed | no | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -74808 | GBP | 2023-10-31 | 2026-01-30 | filed | yes | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-10-31 | 2024-09-19 | filed | no | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-10-31 | 2026-01-30 | filed | yes | `d:Equity` | total-exemption-full |
| equity | -74806 | GBP | 2023-10-31 | 2026-01-30 | filed | yes | `d:Equity` | total-exemption-full |
| fixed_assets | 459 | GBP | 2023-10-31 | 2024-09-19 | filed | no | `d:FixedAssets` | total-exemption-full |
| fixed_assets | 459 | GBP | 2023-10-31 | 2026-01-30 | filed | yes | `d:FixedAssets` | total-exemption-full |
| net_assets | -74806 | GBP | 2023-10-31 | 2024-09-19 | filed | no | `d:NetAssetsLiabilities` | total-exemption-full |
| net_assets | -74806 | GBP | 2023-10-31 | 2026-01-30 | filed | yes | `d:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -75265 | GBP | 2023-10-31 | 2024-09-19 | filed | no | `d:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -75265 | GBP | 2023-10-31 | 2026-01-30 | filed | yes | `d:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -74806 | GBP | 2023-10-31 | 2024-09-19 | filed | no | `d:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -74806 | GBP | 2023-10-31 | 2026-01-30 | filed | yes | `d:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2022-10-31 | 2024-09-19 | filed | yes | `d:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 65011 | GBP | 2022-10-31 | 2024-09-19 | filed | yes | `d:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 129352 | GBP | 2022-10-31 | 2024-09-19 | filed | yes | `d:Creditors` | total-exemption-full |
| current_assets | 137021 | GBP | 2022-10-31 | 2024-09-19 | filed | yes | `d:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 72010 | GBP | 2022-10-31 | 2024-09-19 | filed | yes | `d:Debtors` | total-exemption-full |
| equity | 8647 | GBP | 2022-10-31 | 2024-09-19 | filed | yes | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 8645 | GBP | 2022-10-31 | 2024-09-19 | filed | yes | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2022-10-31 | 2024-09-19 | filed | yes | `d:Equity` | total-exemption-full |
| fixed_assets | 978 | GBP | 2022-10-31 | 2024-09-19 | filed | yes | `d:FixedAssets` | total-exemption-full |
| net_assets | 8647 | GBP | 2022-10-31 | 2024-09-19 | filed | yes | `d:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 7669 | GBP | 2022-10-31 | 2024-09-19 | filed | yes | `d:NetCurrentAssetsLiabilities` | total-exemption-full |
| staff_costs | 3683 | GBP | 2022-10-31 | 2024-09-19 | filed | yes | `d:StaffCostsEmployeeBenefitsExpense` | total-exemption-full |
| total_assets_less_current_liabilities | 8647 | GBP | 2022-10-31 | 2024-09-19 | filed | yes | `d:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## NIMBUS DIGITAL & TECHNOLOGY INNOVATIONS LTD (`gb:03337471`)

- registration: `03337471` (GB), status active, incorporated 1997-03-21
- classification: ['62020'] (sic_2007)
- records: 5 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 100 filings, 2 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.3 | xbrli:pure | 2025-06-30 | 2026-03-25 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 594580 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| current_assets | 1679451 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 1084704 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1084704 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 770411 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 770311 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 770411 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 757436 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 773454 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0.29 | xbrli:pure | 2024-06-30 | 2026-03-25 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 29 | xbrli:pure | 2024-06-30 | 2024-11-18 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 466604 | GBP | 2024-06-30 | 2024-11-18 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 466604 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1038750 | GBP | 2024-06-30 | 2024-11-18 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 1864117 | GBP | 2024-06-30 | 2024-11-18 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 1864117 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1396822 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 1396822 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 1396822 | GBP | 2024-06-30 | 2024-11-18 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1396822 | GBP | 2024-06-30 | 2024-11-18 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 854145 | GBP | 2024-06-30 | 2024-11-18 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-06-30 | 2024-11-18 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 854245 | GBP | 2024-06-30 | 2024-11-18 | filed | no | `core:Equity` | total-exemption-full |
| equity | 854245 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 854145 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 854245 | GBP | 2024-06-30 | 2024-11-18 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 854245 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 825367 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 825367 | GBP | 2024-06-30 | 2024-11-18 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 863871 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 863871 | GBP | 2024-06-30 | 2024-11-18 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 28 | xbrli:pure | 2023-06-30 | 2024-11-18 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 28 | xbrli:pure | 2023-06-30 | 2023-10-12 | filed | no | `ns6:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 300812 | GBP | 2023-06-30 | 2024-11-18 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 300812 | GBP | 2023-06-30 | 2023-10-12 | filed | no | `ns6:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 770869 | GBP | 2023-06-30 | 2024-11-18 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 1672764 | GBP | 2023-06-30 | 2023-10-12 | filed | no | `ns6:CurrentAssets` | total-exemption-full |
| current_assets | 1672762 | GBP | 2023-06-30 | 2024-11-18 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 1369429 | GBP | 2023-06-30 | 2023-10-12 | filed | no | `ns6:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1369427 | GBP | 2023-06-30 | 2024-11-18 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 1369427 | GBP | 2023-06-30 | 2024-11-18 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 1369429 | GBP | 2023-06-30 | 2023-10-12 | filed | no | `ns6:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 950610 | GBP | 2023-06-30 | 2024-11-18 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-06-30 | 2023-10-12 | filed | no | `ns6:Equity` | total-exemption-full |
| equity | 950710 | GBP | 2023-06-30 | 2023-10-12 | filed | no | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 950610 | GBP | 2023-06-30 | 2023-10-12 | filed | no | `ns6:Equity` | total-exemption-full |
| equity | 950710 | GBP | 2023-06-30 | 2024-11-18 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-06-30 | 2024-11-18 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 950710 | GBP | 2023-06-30 | 2024-11-18 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 950710 | GBP | 2023-06-30 | 2023-10-12 | filed | no | `ns6:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 901894 | GBP | 2023-06-30 | 2023-10-12 | filed | no | `ns6:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 901893 | GBP | 2023-06-30 | 2024-11-18 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 962161 | GBP | 2023-06-30 | 2024-11-18 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 962161 | GBP | 2023-06-30 | 2023-10-12 | filed | no | `ns6:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 21 | xbrli:pure | 2022-06-30 | 2023-10-12 | filed | yes | `ns6:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 204487 | GBP | 2022-06-30 | 2023-10-12 | filed | yes | `ns6:CashBankOnHand` | total-exemption-full |
| current_assets | 2119608 | GBP | 2022-06-30 | 2023-10-12 | filed | yes | `ns6:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 1915121 | GBP | 2022-06-30 | 2023-10-12 | filed | yes | `ns6:Debtors` | total-exemption-full |
| debtors | 1915121 | GBP | 2022-06-30 | 2023-10-12 | filed | yes | `ns6:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 868773 | GBP | 2022-06-30 | 2023-10-12 | filed | yes | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2022-06-30 | 2023-10-12 | filed | yes | `ns6:Equity` | total-exemption-full |
| equity | 868873 | GBP | 2022-06-30 | 2023-10-12 | filed | yes | `ns6:Equity` | total-exemption-full |
| net_assets | 868873 | GBP | 2022-06-30 | 2023-10-12 | filed | yes | `ns6:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 838583 | GBP | 2022-06-30 | 2023-10-12 | filed | yes | `ns6:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 875981 | GBP | 2022-06-30 | 2023-10-12 | filed | yes | `ns6:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2024-11-18: `{"superseded_document_id": "gb:03337471:doc:rUDQQ1Pz4PzYx-IHktDnOyEcV6oYHDJH-tCGBj5e5a0", "restatements": [{"concept": "debtors", "period_end": "2023-06-30", "old_value": "1369429.0000", "new_value": `
- event restatement @ 2026-03-25: `{"superseded_document_id": "gb:03337471:doc:JaL6JVJGyoaHY4qsHitXI764e5eJV5QvuLeWC24PVLs", "restatements": [{"concept": "average_employees", "period_end": "2024-06-30", "old_value": "29.0000", "new_val`

## HNW ARCHITECTS LIMITED (`gb:03589904`)

- registration: `03589904` (GB), status active, incorporated 1998-06-30
- classification: ['71111', '82990'] (sic_2007)
- records: 14 officers, 6 beneficial owners, 0 ownership statements, 4 security interests, 134 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.37 | xbrli:pure | 2025-03-31 | 2025-12-11 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 165511 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 90016 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 532194 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 532194 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 884389 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 651214 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 651214 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 306218 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 638 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 50 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShares'}` | 987 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 987 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass2'}` | 607 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass5'}` | 115 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass4'}` | 115 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 304593 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 47039 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | 306218 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 352195 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| tax_charge | 106178 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | total-exemption-full |
| total_assets_less_current_liabilities | 399234 | GBP | 2025-03-31 | 2025-12-11 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 38 | xbrli:pure | 2024-03-31 | 2024-11-18 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 0.38 | xbrli:pure | 2024-03-31 | 2025-12-11 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 150897 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 150897 | GBP | 2024-03-31 | 2024-11-18 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 161216 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 161216 | GBP | 2024-03-31 | 2024-11-18 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 493164 | GBP | 2024-03-31 | 2024-11-18 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 493164 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 493164 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 828648 | GBP | 2024-03-31 | 2024-11-18 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 828648 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 654995 | GBP | 2024-03-31 | 2024-11-18 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 654995 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 654995 | GBP | 2024-03-31 | 2024-11-18 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 654995 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShares'}` | 986 | GBP | 2024-03-31 | 2024-11-18 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 240193 | GBP | 2024-03-31 | 2024-11-18 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass5'}` | 115 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 240193 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShares'}` | 987 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 50 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 986 | GBP | 2024-03-31 | 2024-11-18 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 639 | GBP | 2024-03-31 | 2024-11-18 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass2'}` | 607 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 241818 | GBP | 2024-03-31 | 2024-11-18 | filed | no | `core:Equity` | total-exemption-full |
| equity | 241818 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 987 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 638 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass4'}` | 115 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 74350 | GBP | 2024-03-31 | 2024-11-18 | filed | no | `core:FixedAssets` | total-exemption-full |
| fixed_assets | 74350 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | 241818 | GBP | 2024-03-31 | 2024-11-18 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 241818 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 335484 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 335484 | GBP | 2024-03-31 | 2024-11-18 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_for_period | 428816 | GBP | 2024-03-31 | 2024-11-18 | filed | yes | `core:ProfitLoss` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 428816 | GBP | 2024-03-31 | 2024-11-18 | filed | yes | `core:ProfitLoss` | total-exemption-full |
| tax_charge | 27797 | GBP | 2024-03-31 | 2024-11-18 | filed | no | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | total-exemption-full |
| tax_charge | 27797 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | total-exemption-full |
| total_assets_less_current_liabilities | 409834 | GBP | 2024-03-31 | 2024-11-18 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 409834 | GBP | 2024-03-31 | 2025-12-11 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 42 | xbrli:pure | 2023-03-31 | 2023-12-19 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 42 | xbrli:pure | 2023-03-31 | 2024-11-18 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 269894 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 269894 | GBP | 2023-03-31 | 2024-11-18 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 274338 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 274338 | GBP | 2023-03-31 | 2024-11-18 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 541637 | GBP | 2023-03-31 | 2024-11-18 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 541637 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 908144 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 908144 | GBP | 2023-03-31 | 2024-11-18 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 594508 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 594508 | GBP | 2023-03-31 | 2024-11-18 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 594508 | GBP | 2023-03-31 | 2024-11-18 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 594508 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 639 | GBP | 2023-03-31 | 2024-11-18 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShares'}` | 986 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:Equity` | total-exemption-full |
| equity | 131602 | GBP | 2023-03-31 | 2024-11-18 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 129977 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 986 | GBP | 2023-03-31 | 2024-11-18 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 639 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShares'}` | 986 | GBP | 2023-03-31 | 2024-11-18 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 131602 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 129977 | GBP | 2023-03-31 | 2024-11-18 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 986 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:Equity` | total-exemption-full |
| fixed_assets | 47433 | GBP | 2023-03-31 | 2024-11-18 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | 131602 | GBP | 2023-03-31 | 2024-11-18 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 131602 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 366507 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 366507 | GBP | 2023-03-31 | 2024-11-18 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_for_period | -118717 | GBP | 2023-03-31 | 2024-11-18 | filed | yes | `core:ProfitLoss` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -118717 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:ProfitLoss` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -118717 | GBP | 2023-03-31 | 2024-11-18 | filed | yes | `core:ProfitLoss` | total-exemption-full |
| profit_for_period | -118717 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:ProfitLoss` | total-exemption-full |
| tax_charge | -5877 | GBP | 2023-03-31 | 2024-11-18 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | total-exemption-full |
| tax_charge | -5877 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | total-exemption-full |
| total_assets_less_current_liabilities | 413940 | GBP | 2023-03-31 | 2024-11-18 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 413940 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 45 | xbrli:pure | 2022-03-31 | 2023-12-19 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 271950 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 204167 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 382681 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 1177445 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 817081 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 817081 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 655124 | GBP | 2022-03-31 | 2023-12-19 | filed | no | `core:Equity` | total-exemption-full |
| equity | 656424 | GBP | 2022-03-31 | 2023-12-19 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1300 | GBP | 2022-03-31 | 2023-12-19 | filed | no | `core:Equity` | total-exemption-full |
| equity | 656424 | GBP | 2022-03-31 | 2024-11-18 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1300 | GBP | 2022-03-31 | 2024-11-18 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 655124 | GBP | 2022-03-31 | 2024-11-18 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 0 | GBP | 2022-03-31 | 2023-12-19 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 0 | GBP | 2022-03-31 | 2024-11-18 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShares'}` | 1300 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 656424 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 794764 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 267537 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `core:ProfitLoss` | total-exemption-full |
| profit_for_period | 267537 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `core:ProfitLoss` | total-exemption-full |
| tax_charge | -109365 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | total-exemption-full |
| total_assets_less_current_liabilities | 874491 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 0 | GBP | 2021-03-31 | 2023-12-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1300 | GBP | 2021-03-31 | 2023-12-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 772587 | GBP | 2021-03-31 | 2023-12-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 773887 | GBP | 2021-03-31 | 2023-12-19 | filed | yes | `core:Equity` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2025-12-11: `{"superseded_document_id": "gb:03589904:doc:33Ia0IRiT11swvi42rFZClGPCS_mpxpuE8RQ9NOAsB4", "restatements": [{"concept": "equity", "period_end": "2024-03-31", "old_value": "986.0000", "new_value": "987.`

## DIEBOLD NIXDORF (UK) LIMITED (`gb:03841833`)

- registration: `03841833` (GB), status active, incorporated 1999-09-15
- classification: ['27900', '62090'] (sic_2007)
- records: 21 officers, 2 beneficial owners, 0 ownership statements, 7 security interests, 128 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## METAFOUR INTERNATIONAL LIMITED (`gb:04088822`)

- registration: `04088822` (GB), status active, incorporated 2000-10-12
- classification: ['62012'] (sic_2007)
- records: 11 officers, 3 beneficial owners, 0 ownership statements, 2 security interests, 99 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.04 | xbrli:pure | 2025-06-30 | 2026-03-25 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | group |
| average_employees `{'GroupCompanyDataDimension': 'Consolidated'}` | 0.52 | xbrli:pure | 2025-06-30 | 2026-03-25 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | group |
| cash `{'GroupCompanyDataDimension': 'Consolidated'}` | 365302 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:CashBankOnHand` | group |
| cash | 70045 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:CashBankOnHand` | group |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'GroupCompanyDataDimension': 'Consolidated'}` | 677684 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:Creditors` | group |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 276454 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:Creditors` | group |
| current_assets | 71423 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:CurrentAssets` | group |
| debtors | 1378 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:Debtors` | group |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'GroupCompanyDataDimension': 'Consolidated'}` | 640552 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:Debtors` | group |
| equity `{'EquityClassesDimension': 'OtherMiscellaneousReserve', 'GroupCompanyDataDimension': 'Consolidated'}` | -48789 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:Equity` | group |
| equity `{'GroupCompanyDataDimension': 'Consolidated'}` | 996582 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:Equity` | group |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses', 'GroupCompanyDataDimension': 'Consolidated'}` | 985871 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:Equity` | group |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 574439 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:Equity` | group |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 4300 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:Equity` | group |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 28507 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:Equity` | group |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve', 'GroupCompanyDataDimension': 'Consolidated'}` | 4300 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:Equity` | group |
| equity `{'EquityClassesDimension': 'ShareCapital', 'GroupCompanyDataDimension': 'Consolidated'}` | 26693 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:Equity` | group |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 26693 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:Equity` | group |
| equity `{'EquityClassesDimension': 'SharePremium', 'GroupCompanyDataDimension': 'Consolidated'}` | 28507 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:Equity` | group |
| equity | 633939 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:Equity` | group |
| equity `{'EquityClassesDimension': 'ForeignCurrencyTranslationReserve', 'GroupCompanyDataDimension': 'Consolidated'}` | -48789 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:Equity` | group |
| fixed_assets | 984524 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:FixedAssets` | group |
| net_assets | 633939 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:NetAssetsLiabilities` | group |
| net_assets `{'GroupCompanyDataDimension': 'Consolidated'}` | 996582 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:NetAssetsLiabilities` | group |
| net_current_assets `{'GroupCompanyDataDimension': 'Consolidated'}` | 328170 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:NetCurrentAssetsLiabilities` | group |
| net_current_assets | -205031 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:NetCurrentAssetsLiabilities` | group |
| profit_for_period `{'GroupCompanyDataDimension': 'Consolidated'}` | 806599 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:ProfitLoss` | group |
| profit_for_period | 846641 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:ProfitLoss` | group |
| tax_charge `{'GroupCompanyDataDimension': 'Consolidated'}` | 245347 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | group |
| total_assets_less_current_liabilities `{'GroupCompanyDataDimension': 'Consolidated'}` | 1166837 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | group |
| total_assets_less_current_liabilities | 779493 | GBP | 2025-06-30 | 2026-03-25 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | group |
| average_employees | 5 | xbrli:pure | 2024-06-30 | 2025-03-27 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | group |
| average_employees `{'GroupCompanyDataDimension': 'Consolidated'}` | 0.52 | xbrli:pure | 2024-06-30 | 2026-03-25 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | group |
| average_employees | 0.05 | xbrli:pure | 2024-06-30 | 2026-03-25 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | group |
| cash | 25393 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:CashBankOnHand` | group |
| cash | 25393 | GBP | 2024-06-30 | 2025-03-27 | filed | no | `core:CashBankOnHand` | group |
| cash `{'GroupCompanyDataDimension': 'Consolidated'}` | 471775 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:CashBankOnHand` | group |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 72995 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:Creditors` | group |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'GroupCompanyDataDimension': 'Consolidated'}` | 540730 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:Creditors` | group |
| current_assets | 26731 | GBP | 2024-06-30 | 2025-03-27 | filed | no | `core:CurrentAssets` | group |
| current_assets | 26731 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:CurrentAssets` | group |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'GroupCompanyDataDimension': 'Consolidated'}` | 642450 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:Debtors` | group |
| debtors | 1338 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:Debtors` | group |
| debtors | 1338 | GBP | 2024-06-30 | 2025-03-27 | filed | no | `core:Debtors` | group |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 4300 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:Equity` | group |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 595831 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:Equity` | group |
| equity `{'EquityClassesDimension': 'ShareCapital', 'GroupCompanyDataDimension': 'Consolidated'}` | 26693 | GBP | 2024-06-30 | 2025-03-27 | filed | no | `core:Equity` | group |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 28507 | GBP | 2024-06-30 | 2025-03-27 | filed | no | `core:Equity` | group |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve', 'GroupCompanyDataDimension': 'Consolidated'}` | 4300 | GBP | 2024-06-30 | 2025-03-27 | filed | no | `core:Equity` | group |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 26693 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:Equity` | group |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve', 'GroupCompanyDataDimension': 'Consolidated'}` | 4300 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:Equity` | group |
| equity `{'EquityClassesDimension': 'SharePremium', 'GroupCompanyDataDimension': 'Consolidated'}` | 28507 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:Equity` | group |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses', 'GroupCompanyDataDimension': 'Consolidated'}` | 1047305 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:Equity` | group |
| equity `{'GroupCompanyDataDimension': 'Consolidated'}` | 1108258 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:Equity` | group |
| equity `{'EquityClassesDimension': 'SharePremium', 'GroupCompanyDataDimension': 'Consolidated'}` | 28507 | GBP | 2024-06-30 | 2025-03-27 | filed | no | `core:Equity` | group |
| equity | 655331 | GBP | 2024-06-30 | 2025-03-27 | filed | no | `core:Equity` | group |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 26693 | GBP | 2024-06-30 | 2025-03-27 | filed | no | `core:Equity` | group |
| equity | 655331 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:Equity` | group |
| equity `{'EquityClassesDimension': 'ShareCapital', 'GroupCompanyDataDimension': 'Consolidated'}` | 26693 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:Equity` | group |
| equity `{'EquityClassesDimension': 'OtherMiscellaneousReserve', 'GroupCompanyDataDimension': 'Consolidated'}` | 1453 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:Equity` | group |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 28507 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:Equity` | group |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 4300 | GBP | 2024-06-30 | 2025-03-27 | filed | no | `core:Equity` | group |
| equity `{'EquityClassesDimension': 'ForeignCurrencyTranslationReserve', 'GroupCompanyDataDimension': 'Consolidated'}` | 1453 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:Equity` | group |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 595831 | GBP | 2024-06-30 | 2025-03-27 | filed | no | `core:Equity` | group |
| fixed_assets | 855097 | GBP | 2024-06-30 | 2025-03-27 | filed | no | `core:FixedAssets` | group |
| fixed_assets | 855097 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:FixedAssets` | group |
| net_assets `{'GroupCompanyDataDimension': 'Consolidated'}` | 1108258 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:NetAssetsLiabilities` | group |
| net_assets | 655331 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:NetAssetsLiabilities` | group |
| net_assets | 655331 | GBP | 2024-06-30 | 2025-03-27 | filed | no | `core:NetAssetsLiabilities` | group |
| net_current_assets | -46264 | GBP | 2024-06-30 | 2025-03-27 | filed | no | `core:NetCurrentAssetsLiabilities` | group |
| net_current_assets `{'GroupCompanyDataDimension': 'Consolidated'}` | 573495 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:NetCurrentAssetsLiabilities` | group |
| net_current_assets | -46264 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:NetCurrentAssetsLiabilities` | group |
| profit_for_period `{'GroupCompanyDataDimension': 'Consolidated'}` | 587838 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:ProfitLoss` | group |
| profit_for_period `{'GroupCompanyDataDimension': 'Consolidated'}` | 587838 | GBP | 2024-06-30 | 2025-03-27 | filed | no | `core:ProfitLoss` | group |
| profit_for_period | 664853 | GBP | 2024-06-30 | 2025-03-27 | filed | no | `core:ProfitLoss` | group |
| profit_for_period | 664853 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:ProfitLoss` | group |
| tax_charge `{'GroupCompanyDataDimension': 'Consolidated'}` | 107897 | GBP | 2024-06-30 | 2025-03-27 | filed | no | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | group |
| tax_charge `{'GroupCompanyDataDimension': 'Consolidated'}` | 107897 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | group |
| total_assets_less_current_liabilities | 808833 | GBP | 2024-06-30 | 2025-03-27 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | group |
| total_assets_less_current_liabilities `{'GroupCompanyDataDimension': 'Consolidated'}` | 1281065 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | group |
| total_assets_less_current_liabilities | 808833 | GBP | 2024-06-30 | 2026-03-25 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | group |
| average_employees | 5 | xbrli:pure | 2023-06-30 | 2025-03-27 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | group |
| cash | 296821 | GBP | 2023-06-30 | 2025-03-27 | filed | yes | `core:CashBankOnHand` | group |
| current_assets | 298284 | GBP | 2023-06-30 | 2025-03-27 | filed | yes | `core:CurrentAssets` | group |
| debtors | 1463 | GBP | 2023-06-30 | 2025-03-27 | filed | yes | `core:Debtors` | group |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 28507 | GBP | 2023-06-30 | 2026-03-25 | filed | yes | `core:Equity` | group |
| equity `{'EquityClassesDimension': 'SharePremium', 'GroupCompanyDataDimension': 'Consolidated'}` | 28507 | GBP | 2023-06-30 | 2025-03-27 | filed | no | `core:Equity` | group |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 4300 | GBP | 2023-06-30 | 2025-03-27 | filed | no | `core:Equity` | group |
| equity | 966539 | GBP | 2023-06-30 | 2025-03-27 | filed | no | `core:Equity` | group |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve', 'GroupCompanyDataDimension': 'Consolidated'}` | 4300 | GBP | 2023-06-30 | 2026-03-25 | filed | yes | `core:Equity` | group |
| equity | 1435528 | GBP | 2023-06-30 | 2026-03-25 | filed | yes | `core:Equity` | group |
| equity `{'EquityClassesDimension': 'ForeignCurrencyTranslationReserve', 'GroupCompanyDataDimension': 'Consolidated'}` | -20014 | GBP | 2023-06-30 | 2026-03-25 | filed | yes | `core:Equity` | group |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 28507 | GBP | 2023-06-30 | 2025-03-27 | filed | no | `core:Equity` | group |
| equity `{'EquityClassesDimension': 'SharePremium', 'GroupCompanyDataDimension': 'Consolidated'}` | 28507 | GBP | 2023-06-30 | 2026-03-25 | filed | yes | `core:Equity` | group |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 907039 | GBP | 2023-06-30 | 2026-03-25 | filed | yes | `core:Equity` | group |
| equity `{'EquityClassesDimension': 'ShareCapital', 'GroupCompanyDataDimension': 'Consolidated'}` | 26693 | GBP | 2023-06-30 | 2026-03-25 | filed | yes | `core:Equity` | group |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 4300 | GBP | 2023-06-30 | 2026-03-25 | filed | yes | `core:Equity` | group |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 907039 | GBP | 2023-06-30 | 2025-03-27 | filed | no | `core:Equity` | group |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 26693 | GBP | 2023-06-30 | 2025-03-27 | filed | no | `core:Equity` | group |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 26693 | GBP | 2023-06-30 | 2026-03-25 | filed | yes | `core:Equity` | group |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve', 'GroupCompanyDataDimension': 'Consolidated'}` | 4300 | GBP | 2023-06-30 | 2025-03-27 | filed | no | `core:Equity` | group |
| equity `{'EquityClassesDimension': 'ShareCapital', 'GroupCompanyDataDimension': 'Consolidated'}` | 26693 | GBP | 2023-06-30 | 2025-03-27 | filed | no | `core:Equity` | group |
| fixed_assets | 879180 | GBP | 2023-06-30 | 2025-03-27 | filed | yes | `core:FixedAssets` | group |
| net_assets | 966539 | GBP | 2023-06-30 | 2025-03-27 | filed | yes | `core:NetAssetsLiabilities` | group |
| net_current_assets | 205303 | GBP | 2023-06-30 | 2025-03-27 | filed | yes | `core:NetCurrentAssetsLiabilities` | group |
| profit_for_period | 828240 | GBP | 2023-06-30 | 2025-03-27 | filed | yes | `core:ProfitLoss` | group |
| profit_for_period `{'GroupCompanyDataDimension': 'Consolidated'}` | 444232 | GBP | 2023-06-30 | 2025-03-27 | filed | yes | `core:ProfitLoss` | group |
| tax_charge `{'GroupCompanyDataDimension': 'Consolidated'}` | 151168 | GBP | 2023-06-30 | 2025-03-27 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | group |
| total_assets_less_current_liabilities | 1084483 | GBP | 2023-06-30 | 2025-03-27 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | group |
| equity | 1353010 | GBP | 2022-06-30 | 2025-03-27 | filed | yes | `core:Equity` | group |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 0 | GBP | 2022-06-30 | 2025-03-27 | filed | yes | `core:Equity` | group |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1323000 | GBP | 2022-06-30 | 2025-03-27 | filed | yes | `core:Equity` | group |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 4300 | GBP | 2022-06-30 | 2025-03-27 | filed | yes | `core:Equity` | group |

_No coverage facts for the latest run._

- event restatement @ 2026-03-25: `{"superseded_document_id": "gb:04088822:doc:efNJsF8GKYD06PK81kTXgVTJS72iH83wX5mbyuUTkQc", "restatements": [{"concept": "equity", "period_end": "2023-06-30", "old_value": "966539.0000", "new_value": "1`

## BEDROCK SOFTWARE LIMITED (`gb:04435779`)

- registration: `04435779` (GB), status active, incorporated 2002-05-10
- classification: ['47910', '62012', '62020', '62090'] (sic_2007)
- records: 4 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 56 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-09-30 | 2026-01-19 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 8901 | GBP | 2025-09-30 | 2026-01-19 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 7512 | GBP | 2025-09-30 | 2026-01-19 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 9505 | GBP | 2025-09-30 | 2026-01-19 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 604 | GBP | 2025-09-30 | 2026-01-19 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 604 | GBP | 2025-09-30 | 2026-01-19 | filed | yes | `core:Debtors` | total-exemption-full |
| net_assets | 5417 | GBP | 2025-09-30 | 2026-01-19 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1993 | GBP | 2025-09-30 | 2026-01-19 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 5417 | GBP | 2025-09-30 | 2026-01-19 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-09-30 | 2026-01-19 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-09-30 | 2025-02-10 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 14014 | GBP | 2024-09-30 | 2026-01-19 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 14014 | GBP | 2024-09-30 | 2025-02-10 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 8000 | GBP | 2024-09-30 | 2026-01-19 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 8000 | GBP | 2024-09-30 | 2025-02-10 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 13737 | GBP | 2024-09-30 | 2025-02-10 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 13737 | GBP | 2024-09-30 | 2026-01-19 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 16029 | GBP | 2024-09-30 | 2026-01-19 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 16029 | GBP | 2024-09-30 | 2025-02-10 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 2015 | GBP | 2024-09-30 | 2025-02-10 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2015 | GBP | 2024-09-30 | 2025-02-10 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 2015 | GBP | 2024-09-30 | 2026-01-19 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2015 | GBP | 2024-09-30 | 2026-01-19 | filed | yes | `core:Debtors` | total-exemption-full |
| net_assets | -1398 | GBP | 2024-09-30 | 2026-01-19 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | -1398 | GBP | 2024-09-30 | 2025-02-10 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 2292 | GBP | 2024-09-30 | 2025-02-10 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 2292 | GBP | 2024-09-30 | 2026-01-19 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 6602 | GBP | 2024-09-30 | 2026-01-19 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 6602 | GBP | 2024-09-30 | 2025-02-10 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | iso4217:GBP | 2023-09-30 | 2024-01-22 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-09-30 | 2025-02-10 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 3327 | GBP | 2023-09-30 | 2025-02-10 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 8000 | GBP | 2023-09-30 | 2024-01-22 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 8000 | GBP | 2023-09-30 | 2025-02-10 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 11843 | GBP | 2023-09-30 | 2024-01-22 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 12206 | GBP | 2023-09-30 | 2025-02-10 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 13822 | GBP | 2023-09-30 | 2025-02-10 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 13739 | GBP | 2023-09-30 | 2024-01-22 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 10495 | GBP | 2023-09-30 | 2025-02-10 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 10495 | GBP | 2023-09-30 | 2025-02-10 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 963 | GBP | 2023-09-30 | 2024-01-22 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 5421 | GBP | 2023-09-30 | 2024-01-22 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | -963 | GBP | 2023-09-30 | 2025-02-10 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 963 | GBP | 2023-09-30 | 2024-01-22 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 1616 | GBP | 2023-09-30 | 2025-02-10 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1979 | GBP | 2023-09-30 | 2024-01-22 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 7037 | GBP | 2023-09-30 | 2025-02-10 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 7400 | GBP | 2023-09-30 | 2024-01-22 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2022-09-30 | 2024-01-22 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 10000 | GBP | 2022-09-30 | 2024-01-22 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 13607 | GBP | 2022-09-30 | 2024-01-22 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 2535 | GBP | 2022-09-30 | 2024-01-22 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 18326 | GBP | 2022-09-30 | 2024-01-22 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 3062 | GBP | 2022-09-30 | 2024-01-22 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 18326 | GBP | 2022-09-30 | 2024-01-22 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 11072 | GBP | 2022-09-30 | 2024-01-22 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 8010 | GBP | 2022-09-30 | 2024-01-22 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2025-02-10: `{"superseded_document_id": "gb:04435779:doc:1pOBZIhCMWVN_jIlb3cfaKesyuA5QnHC_PolFDdz4ME", "restatements": [{"concept": "current_assets", "period_end": "2023-09-30", "old_value": "13739.0000", "new_val`

## SCREENSAVERS PC'S LIMITED (`gb:04815864`)

- registration: `04815864` (GB), status active, incorporated 2003-06-30
- classification: ['62090'] (sic_2007)
- records: 8 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 75 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 5 | xbrli:pure | 2025-03-31 | 2025-12-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 373484 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 183844 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 484096 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 109862 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'OtherReservesSubtotal'}` | 60 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 310284 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 40 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 310184 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 60 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 310284 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 300252 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| average_employees | 5 | xbrli:pure | 2024-03-31 | 2024-12-31 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 6 | xbrli:pure | 2024-03-31 | 2025-12-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 329148 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 329148 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 170056 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 170056 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 421706 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 421706 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 91808 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 91808 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 40 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 256811 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 60 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 40 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'OtherReservesSubtotal'}` | 60 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 256811 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 256711 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'OtherReservesSubtotal'}` | 60 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 256711 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 60 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 256811 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 256811 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 251650 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 251650 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| average_employees | 6 | xbrli:pure | 2023-03-31 | 2024-02-27 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 6 | xbrli:pure | 2023-03-31 | 2024-12-31 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 307246 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 307246 | GBP | 2023-03-31 | 2024-02-27 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 155518 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 155518 | GBP | 2023-03-31 | 2024-02-27 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 376812 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 376812 | GBP | 2023-03-31 | 2024-02-27 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors | 69316 | GBP | 2023-03-31 | 2024-02-27 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 69316 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 224548 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 224448 | GBP | 2023-03-31 | 2024-02-27 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'OtherReservesSubtotal'}` | 60 | GBP | 2023-03-31 | 2024-02-27 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 224448 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 40 | GBP | 2023-03-31 | 2024-02-27 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'OtherReservesSubtotal'}` | 60 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 60 | GBP | 2023-03-31 | 2025-12-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 60 | GBP | 2023-03-31 | 2024-12-31 | filed | no | `core:Equity` | total-exemption-full |
| equity | 224548 | GBP | 2023-03-31 | 2024-02-27 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 60 | GBP | 2023-03-31 | 2024-02-27 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 40 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 224548 | GBP | 2023-03-31 | 2024-02-27 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 224548 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 221294 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 221294 | GBP | 2023-03-31 | 2024-02-27 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| average_employees | 6 | xbrli:pure | 2022-03-31 | 2024-02-27 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 282811 | GBP | 2022-03-31 | 2024-02-27 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 191341 | GBP | 2022-03-31 | 2024-02-27 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 378580 | GBP | 2022-03-31 | 2024-02-27 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 95519 | GBP | 2022-03-31 | 2024-02-27 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 40 | GBP | 2022-03-31 | 2024-02-27 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 60 | GBP | 2022-03-31 | 2024-12-31 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 188898 | GBP | 2022-03-31 | 2024-02-27 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 60 | GBP | 2022-03-31 | 2024-02-27 | filed | no | `core:Equity` | total-exemption-full |
| equity | 188998 | GBP | 2022-03-31 | 2024-02-27 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'OtherReservesSubtotal'}` | 60 | GBP | 2022-03-31 | 2024-02-27 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 188998 | GBP | 2022-03-31 | 2024-02-27 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 187239 | GBP | 2022-03-31 | 2024-02-27 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 60 | GBP | 2021-03-31 | 2024-02-27 | filed | yes | `core:Equity` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2025-12-30: `{"superseded_document_id": "gb:04815864:doc:R8Rv3HnAgxZUn6anTv1CVG3wgF2JQbeCHW3fsVAQL70", "restatements": [{"concept": "average_employees", "period_end": "2024-03-31", "old_value": "5.0000", "new_valu`
