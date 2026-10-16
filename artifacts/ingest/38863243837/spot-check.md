# Ingest spot-check

- database: `data/engine.db`
- latest run: `20261016T064823Z-3c89ef68`
- companies in store: 28200; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## DDC PRECISION LIMITED (`gb:02286557`)

- registration: `02286557` (GB), status active, incorporated 1988-08-12
- classification: ['71129'] (sic_2007)
- records: 3 officers, 2 beneficial owners, 0 ownership statements, 3 security interests, 101 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.18 | xbrli:pure | 2025-10-31 | 2026-07-28 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 419 | GBP | 2025-10-31 | 2026-07-28 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 65250 | GBP | 2025-10-31 | 2026-07-28 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1687004 | GBP | 2025-10-31 | 2026-07-28 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 2607423 | GBP | 2025-10-31 | 2026-07-28 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 2607004 | GBP | 2025-10-31 | 2026-07-28 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2607004 | GBP | 2025-10-31 | 2026-07-28 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 1082319 | GBP | 2025-10-31 | 2026-07-28 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2025-10-31 | 2026-07-28 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 2 | GBP | 2025-10-31 | 2026-07-28 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1082317 | GBP | 2025-10-31 | 2026-07-28 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 1082319 | GBP | 2025-10-31 | 2026-07-28 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 920419 | GBP | 2025-10-31 | 2026-07-28 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1213168 | GBP | 2025-10-31 | 2026-07-28 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 21 | xbrli:pure | 2024-10-31 | 2025-07-30 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 0.21 | xbrli:pure | 2024-10-31 | 2026-07-28 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 350902 | GBP | 2024-10-31 | 2025-07-30 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 350902 | GBP | 2024-10-31 | 2026-07-28 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 127232 | GBP | 2024-10-31 | 2026-07-28 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 127232 | GBP | 2024-10-31 | 2025-07-30 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1923250 | GBP | 2024-10-31 | 2025-07-30 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1923250 | GBP | 2024-10-31 | 2026-07-28 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 3179758 | GBP | 2024-10-31 | 2026-07-28 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 3179758 | GBP | 2024-10-31 | 2025-07-30 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2828856 | GBP | 2024-10-31 | 2025-07-30 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 2828856 | GBP | 2024-10-31 | 2026-07-28 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 2828856 | GBP | 2024-10-31 | 2025-07-30 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2828856 | GBP | 2024-10-31 | 2026-07-28 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 1407938 | GBP | 2024-10-31 | 2026-07-28 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 2 | GBP | 2024-10-31 | 2026-07-28 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-10-31 | 2026-07-28 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1407936 | GBP | 2024-10-31 | 2026-07-28 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 2 | GBP | 2024-10-31 | 2025-07-30 | filed | no | `core:Equity` | total-exemption-full |
| equity | 1407938 | GBP | 2024-10-31 | 2025-07-30 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-10-31 | 2025-07-30 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1407936 | GBP | 2024-10-31 | 2025-07-30 | filed | no | `core:Equity` | total-exemption-full |
| net_assets | 1407938 | GBP | 2024-10-31 | 2025-07-30 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 1407938 | GBP | 2024-10-31 | 2026-07-28 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1256508 | GBP | 2024-10-31 | 2025-07-30 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1256508 | GBP | 2024-10-31 | 2026-07-28 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1616817 | GBP | 2024-10-31 | 2026-07-28 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1616817 | GBP | 2024-10-31 | 2025-07-30 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 45 | xbrli:pure | 2023-10-31 | 2025-07-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 45 | xbrli:pure | 2023-10-31 | 2024-07-25 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 3177 | GBP | 2023-10-31 | 2025-07-30 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 3177 | GBP | 2023-10-31 | 2024-07-25 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 60454 | GBP | 2023-10-31 | 2025-07-30 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 60454 | GBP | 2023-10-31 | 2024-07-25 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1606208 | GBP | 2023-10-31 | 2025-07-30 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1606208 | GBP | 2023-10-31 | 2024-07-25 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 2893752 | GBP | 2023-10-31 | 2025-07-30 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 2893752 | GBP | 2023-10-31 | 2024-07-25 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2890575 | GBP | 2023-10-31 | 2025-07-30 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2890575 | GBP | 2023-10-31 | 2024-07-25 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 2890575 | GBP | 2023-10-31 | 2025-07-30 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 2890575 | GBP | 2023-10-31 | 2024-07-25 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-10-31 | 2024-07-25 | filed | no | `core:Equity` | total-exemption-full |
| equity | 1430536 | GBP | 2023-10-31 | 2025-07-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 1430536 | GBP | 2023-10-31 | 2024-07-25 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 2 | GBP | 2023-10-31 | 2025-07-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1430534 | GBP | 2023-10-31 | 2024-07-25 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-10-31 | 2025-07-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1430534 | GBP | 2023-10-31 | 2025-07-30 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 1430536 | GBP | 2023-10-31 | 2024-07-25 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 1430536 | GBP | 2023-10-31 | 2025-07-30 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1287544 | GBP | 2023-10-31 | 2024-07-25 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1287544 | GBP | 2023-10-31 | 2025-07-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1546266 | GBP | 2023-10-31 | 2024-07-25 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1546266 | GBP | 2023-10-31 | 2025-07-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 47 | xbrli:pure | 2022-10-31 | 2024-07-25 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 12537 | GBP | 2022-10-31 | 2024-07-25 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 80209 | GBP | 2022-10-31 | 2024-07-25 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1395787 | GBP | 2022-10-31 | 2024-07-25 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 2496060 | GBP | 2022-10-31 | 2024-07-25 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 2483523 | GBP | 2022-10-31 | 2024-07-25 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2483523 | GBP | 2022-10-31 | 2024-07-25 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1141593 | GBP | 2022-10-31 | 2024-07-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 1141595 | GBP | 2022-10-31 | 2024-07-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2022-10-31 | 2024-07-25 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 1141595 | GBP | 2022-10-31 | 2024-07-25 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1100273 | GBP | 2022-10-31 | 2024-07-25 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1253443 | GBP | 2022-10-31 | 2024-07-25 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2026-07-28: `{"superseded_document_id": "gb:02286557:doc:Ks_ESBSGSvh_QQDJilhwlftdBILPJ7jr8oRUzpgOpwk", "restatements": [{"concept": "average_employees", "period_end": "2024-10-31", "old_value": "21.0000", "new_val`

## COLUMBUS GLOBAL UK LTD (`gb:02890010`)

- registration: `02890010` (GB), status active, incorporated 1994-01-21
- classification: ['62012'] (sic_2007)
- records: 31 officers, 1 beneficial owners, 1 ownership statements, 2 security interests, 182 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 216 | xbrli:pure | 2024-12-31 | 2025-08-25 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 4991901 | GBP | 2024-12-31 | 2025-08-25 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5896396 | GBP | 2024-12-31 | 2025-08-25 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 12985862 | GBP | 2024-12-31 | 2025-08-25 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 7993961 | GBP | 2024-12-31 | 2025-08-25 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 14008538 | GBP | 2024-12-31 | 2025-08-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 14008537 | GBP | 2024-12-31 | 2025-08-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2024-12-31 | 2025-08-25 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 9371900 | GBP | 2024-12-31 | 2025-08-25 | filed | yes | `core:FixedAssets` | total-exemption-full |
| gross_profit | 31382593 | GBP | 2024-12-31 | 2025-08-25 | filed | yes | `core:GrossProfitLoss` | total-exemption-full |
| net_assets | 14008538 | GBP | 2024-12-31 | 2025-08-25 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 7089466 | GBP | 2024-12-31 | 2025-08-25 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| operating_profit | 6196308 | GBP | 2024-12-31 | 2025-08-25 | filed | yes | `core:OperatingProfitLoss` | total-exemption-full |
| profit_before_tax | 6242536 | GBP | 2024-12-31 | 2025-08-25 | filed | yes | `core:ProfitLossOnOrdinaryActivitiesBeforeTax` | total-exemption-full |
| revenue | 41720014 | GBP | 2024-12-31 | 2025-08-25 | filed | yes | `core:TurnoverRevenue` | total-exemption-full |
| tax_charge | 1586301 | GBP | 2024-12-31 | 2025-08-25 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | total-exemption-full |
| total_assets_less_current_liabilities | 16461367 | GBP | 2024-12-31 | 2025-08-25 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 208 | xbrli:pure | 2023-12-31 | 2025-08-25 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 3191753 | GBP | 2023-12-31 | 2025-08-25 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 4860950 | GBP | 2023-12-31 | 2025-08-25 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 7941164 | GBP | 2023-12-31 | 2025-08-25 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 4749411 | GBP | 2023-12-31 | 2025-08-25 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2023-12-31 | 2025-08-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 9352301 | GBP | 2023-12-31 | 2025-08-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 9352302 | GBP | 2023-12-31 | 2025-08-25 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 6688627 | GBP | 2023-12-31 | 2025-08-25 | filed | yes | `core:FixedAssets` | total-exemption-full |
| gross_profit | 24475546 | GBP | 2023-12-31 | 2025-08-25 | filed | yes | `core:GrossProfitLoss` | total-exemption-full |
| net_assets | 9352302 | GBP | 2023-12-31 | 2025-08-25 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 3080214 | GBP | 2023-12-31 | 2025-08-25 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| operating_profit | 2020309 | GBP | 2023-12-31 | 2025-08-25 | filed | yes | `core:OperatingProfitLoss` | total-exemption-full |
| profit_before_tax | 2159136 | GBP | 2023-12-31 | 2025-08-25 | filed | yes | `core:ProfitLossOnOrdinaryActivitiesBeforeTax` | total-exemption-full |
| revenue | 32404794 | GBP | 2023-12-31 | 2025-08-25 | filed | yes | `core:TurnoverRevenue` | total-exemption-full |
| tax_charge | 513156 | GBP | 2023-12-31 | 2025-08-25 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | total-exemption-full |
| total_assets_less_current_liabilities | 9768842 | GBP | 2023-12-31 | 2025-08-25 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## QUAY DOCUMENTATION SERVICES LIMITED (`gb:03266488`)

- registration: `03266488` (GB), status active, incorporated 1996-10-21
- classification: ['62090'] (sic_2007)
- records: 6 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 82 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | iso4217:GBP | 2025-12-31 | 2026-09-09 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2025-12-31 | 2026-09-09 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 143110 | GBP | 2025-12-31 | 2026-09-09 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 143110 | GBP | 2025-12-31 | 2026-09-09 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 143110 | GBP | 2025-12-31 | 2026-09-09 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 143110 | GBP | 2025-12-31 | 2026-09-09 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 143110 | GBP | 2025-12-31 | 2026-09-09 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-12-31 | 2025-09-28 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-12-31 | 2026-09-09 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1066 | GBP | 2024-12-31 | 2026-09-09 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1066 | GBP | 2024-12-31 | 2025-09-28 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 145922 | GBP | 2024-12-31 | 2026-09-09 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 145922 | GBP | 2024-12-31 | 2025-09-28 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | 144856 | GBP | 2024-12-31 | 2026-09-09 | filed | yes | `uk-core:Equity` | micro-entity |
| equity | 144856 | GBP | 2024-12-31 | 2025-09-28 | filed | no | `uk-core:Equity` | micro-entity |
| net_assets | 144856 | GBP | 2024-12-31 | 2025-09-28 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 144856 | GBP | 2024-12-31 | 2026-09-09 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 144856 | GBP | 2024-12-31 | 2026-09-09 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 144856 | GBP | 2024-12-31 | 2025-09-28 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 144856 | GBP | 2024-12-31 | 2025-09-28 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 144856 | GBP | 2024-12-31 | 2026-09-09 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-12-31 | 2024-09-27 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-12-31 | 2025-09-28 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2023-12-31 | 2024-09-27 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 3501 | GBP | 2023-12-31 | 2025-09-28 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 3501 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 145879 | GBP | 2023-12-31 | 2025-09-28 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 145879 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | 142378 | GBP | 2023-12-31 | 2025-09-28 | filed | yes | `uk-core:Equity` | micro-entity |
| equity | 142378 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `uk-core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2023-12-31 | 2024-09-27 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 142378 | GBP | 2023-12-31 | 2025-09-28 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 142378 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 142378 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 142378 | GBP | 2023-12-31 | 2025-09-28 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 142378 | GBP | 2023-12-31 | 2025-09-28 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 142378 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2022-12-31 | 2024-09-27 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 3533 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 146064 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 163692 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 21161 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 163692 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 142531 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 163692 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## SOPEL SYSTEMS & TRAINING LIMITED (`gb:03588476`)

- registration: `03588476` (GB), status active, incorporated 1998-06-23
- classification: ['59112', '59120', '59200', '62020'] (sic_2007)
- records: 6 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 69 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-03-31 | 2025-12-15 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 43378 | GBP | 2025-03-31 | 2025-12-15 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity | 19497 | GBP | 2025-03-31 | 2025-12-15 | filed | yes | `ns5:Equity` | micro-entity |
| fixed_assets | 498 | GBP | 2025-03-31 | 2025-12-15 | filed | yes | `ns5:FixedAssets` | micro-entity |
| net_assets | 19497 | GBP | 2025-03-31 | 2025-12-15 | filed | yes | `ns5:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 22637 | GBP | 2025-03-31 | 2025-12-15 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 23135 | GBP | 2025-03-31 | 2025-12-15 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-03-31 | 2025-12-15 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-03-31 | 2024-12-20 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 35866 | GBP | 2024-03-31 | 2025-12-15 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| current_assets | 35866 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `ns5:CurrentAssets` | micro-entity |
| equity | 15350 | GBP | 2024-03-31 | 2025-12-15 | filed | yes | `ns5:Equity` | micro-entity |
| equity | 15350 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `ns5:Equity` | micro-entity |
| fixed_assets | 698 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `ns5:FixedAssets` | micro-entity |
| fixed_assets | 698 | GBP | 2024-03-31 | 2025-12-15 | filed | yes | `ns5:FixedAssets` | micro-entity |
| net_assets | 15350 | GBP | 2024-03-31 | 2025-12-15 | filed | yes | `ns5:NetAssetsLiabilities` | micro-entity |
| net_assets | 15350 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `ns5:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 16203 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 16203 | GBP | 2024-03-31 | 2025-12-15 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 16901 | GBP | 2024-03-31 | 2025-12-15 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 16901 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-03-31 | 2023-12-27 | filed | no | `ns6:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-03-31 | 2024-12-20 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 40745 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| current_assets | 40745 | GBP | 2023-03-31 | 2023-12-27 | filed | no | `ns6:CurrentAssets` | micro-entity |
| equity | 20205 | GBP | 2023-03-31 | 2023-12-27 | filed | no | `ns6:Equity` | micro-entity |
| equity | 20205 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `ns5:Equity` | micro-entity |
| fixed_assets | 626 | GBP | 2023-03-31 | 2023-12-27 | filed | no | `ns6:FixedAssets` | micro-entity |
| fixed_assets | 626 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `ns5:FixedAssets` | micro-entity |
| net_assets | 20205 | GBP | 2023-03-31 | 2023-12-27 | filed | no | `ns6:NetAssetsLiabilities` | micro-entity |
| net_assets | 20205 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `ns5:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 21078 | GBP | 2023-03-31 | 2023-12-27 | filed | no | `ns6:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 21078 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 21704 | GBP | 2023-03-31 | 2023-12-27 | filed | no | `ns6:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 21704 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2022-03-31 | 2023-12-27 | filed | yes | `ns6:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 41976 | GBP | 2022-03-31 | 2023-12-27 | filed | yes | `ns6:CurrentAssets` | micro-entity |
| equity | 22402 | GBP | 2022-03-31 | 2023-12-27 | filed | yes | `ns6:Equity` | micro-entity |
| fixed_assets | 851 | GBP | 2022-03-31 | 2023-12-27 | filed | yes | `ns6:FixedAssets` | micro-entity |
| net_assets | 22402 | GBP | 2022-03-31 | 2023-12-27 | filed | yes | `ns6:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 22902 | GBP | 2022-03-31 | 2023-12-27 | filed | yes | `ns6:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 23753 | GBP | 2022-03-31 | 2023-12-27 | filed | yes | `ns6:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## FULLY DISTRIBUTED SYSTEMS LTD (`gb:03899842`)

- registration: `03899842` (GB), status active, incorporated 1999-12-24
- classification: ['26512', '62012'] (sic_2007)
- records: 7 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 68 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-12-31 | 2026-09-09 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 202050 | GBP | 2025-12-31 | 2026-09-09 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 208793 | GBP | 2025-12-31 | 2026-09-09 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 6743 | GBP | 2025-12-31 | 2026-09-09 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 117359 | GBP | 2025-12-31 | 2026-09-09 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2025-12-31 | 2026-09-09 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 273 | GBP | 2025-12-31 | 2026-09-09 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 117361 | GBP | 2025-12-31 | 2026-09-09 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 117088 | GBP | 2025-12-31 | 2026-09-09 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 117361 | GBP | 2025-12-31 | 2026-09-09 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-12-31 | 2026-09-09 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-12-31 | 2025-09-17 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 210583 | GBP | 2024-12-31 | 2025-09-17 | filed | no | `frs-core:CashBankOnHand` | total-exemption-full |
| cash | 210583 | GBP | 2024-12-31 | 2026-09-09 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 217374 | GBP | 2024-12-31 | 2025-09-17 | filed | no | `frs-core:CurrentAssets` | total-exemption-full |
| current_assets | 217374 | GBP | 2024-12-31 | 2026-09-09 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 6791 | GBP | 2024-12-31 | 2025-09-17 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| debtors | 6791 | GBP | 2024-12-31 | 2025-09-17 | filed | no | `frs-core:Debtors` | total-exemption-full |
| debtors | 6791 | GBP | 2024-12-31 | 2026-09-09 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-12-31 | 2025-09-17 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 126571 | GBP | 2024-12-31 | 2025-09-17 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 126571 | GBP | 2024-12-31 | 2026-09-09 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-12-31 | 2026-09-09 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 407 | GBP | 2024-12-31 | 2026-09-09 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| fixed_assets | 407 | GBP | 2024-12-31 | 2025-09-17 | filed | no | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 126573 | GBP | 2024-12-31 | 2026-09-09 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 126573 | GBP | 2024-12-31 | 2025-09-17 | filed | no | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 126166 | GBP | 2024-12-31 | 2025-09-17 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 126166 | GBP | 2024-12-31 | 2026-09-09 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 126573 | GBP | 2024-12-31 | 2025-09-17 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 126573 | GBP | 2024-12-31 | 2026-09-09 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 4 | xbrli:pure | 2023-12-31 | 2024-09-20 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 4 | xbrli:pure | 2023-12-31 | 2025-09-17 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 227621 | GBP | 2023-12-31 | 2024-09-20 | filed | no | `frs-core:CashBankOnHand` | total-exemption-full |
| cash | 227621 | GBP | 2023-12-31 | 2025-09-17 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 237121 | GBP | 2023-12-31 | 2025-09-17 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| current_assets | 237121 | GBP | 2023-12-31 | 2024-09-20 | filed | no | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 9500 | GBP | 2023-12-31 | 2025-09-17 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 6991 | GBP | 2023-12-31 | 2025-09-17 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 6991 | GBP | 2023-12-31 | 2024-09-20 | filed | no | `frs-core:Debtors` | total-exemption-full |
| debtors | 9500 | GBP | 2023-12-31 | 2024-09-20 | filed | no | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 139460 | GBP | 2023-12-31 | 2025-09-17 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 139460 | GBP | 2023-12-31 | 2024-09-20 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-12-31 | 2025-09-17 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-12-31 | 2024-09-20 | filed | no | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 607 | GBP | 2023-12-31 | 2024-09-20 | filed | no | `frs-core:FixedAssets` | total-exemption-full |
| fixed_assets | 607 | GBP | 2023-12-31 | 2025-09-17 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 139462 | GBP | 2023-12-31 | 2025-09-17 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 139462 | GBP | 2023-12-31 | 2024-09-20 | filed | no | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 138855 | GBP | 2023-12-31 | 2024-09-20 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 138855 | GBP | 2023-12-31 | 2025-09-17 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 139462 | GBP | 2023-12-31 | 2024-09-20 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 139462 | GBP | 2023-12-31 | 2025-09-17 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 6 | xbrli:pure | 2022-12-31 | 2024-09-20 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 203117 | GBP | 2022-12-31 | 2024-09-20 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 203749 | GBP | 2022-12-31 | 2024-09-20 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 632 | GBP | 2022-12-31 | 2024-09-20 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| debtors | 632 | GBP | 2022-12-31 | 2024-09-20 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2022-12-31 | 2024-09-20 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 107582 | GBP | 2022-12-31 | 2024-09-20 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 907 | GBP | 2022-12-31 | 2024-09-20 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 107584 | GBP | 2022-12-31 | 2024-09-20 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 106677 | GBP | 2022-12-31 | 2024-09-20 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 107584 | GBP | 2022-12-31 | 2024-09-20 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## VETERINARY SOLUTIONS LIMITED (`gb:04207571`)

- registration: `04207571` (GB), status active, incorporated 2001-04-27
- classification: ['62090'] (sic_2007)
- records: 24 officers, 3 beneficial owners, 1 ownership statements, 2 security interests, 129 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## CREASE COMMUNICATIONS LIMITED (`gb:04528747`)

- registration: `04528747` (GB), status active, incorporated 2002-09-06
- classification: ['62020'] (sic_2007)
- records: 3 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 63 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.02 | xbrli:pure | 2025-09-30 | 2026-04-27 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 6536 | GBP | 2025-09-30 | 2026-04-27 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2025-09-30 | 2026-04-27 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 25877 | GBP | 2025-09-30 | 2026-04-27 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 37355 | GBP | 2025-09-30 | 2026-04-27 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 30819 | GBP | 2025-09-30 | 2026-04-27 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 30819 | GBP | 2025-09-30 | 2026-04-27 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 19073 | GBP | 2025-09-30 | 2026-04-27 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 19173 | GBP | 2025-09-30 | 2026-04-27 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 100 | GBP | 2025-09-30 | 2026-04-27 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-09-30 | 2026-04-27 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 19173 | GBP | 2025-09-30 | 2026-04-27 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 11478 | GBP | 2025-09-30 | 2026-04-27 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 19878 | GBP | 2025-09-30 | 2026-04-27 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-09-30 | 2025-06-17 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 0.02 | xbrli:pure | 2024-09-30 | 2026-04-27 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 57812 | GBP | 2024-09-30 | 2025-06-17 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 57812 | GBP | 2024-09-30 | 2026-04-27 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 5100 | GBP | 2024-09-30 | 2026-04-27 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 57254 | GBP | 2024-09-30 | 2026-04-27 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 69198 | GBP | 2024-09-30 | 2025-06-17 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 69198 | GBP | 2024-09-30 | 2026-04-27 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 11386 | GBP | 2024-09-30 | 2026-04-27 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 11386 | GBP | 2024-09-30 | 2025-06-17 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 11386 | GBP | 2024-09-30 | 2026-04-27 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 11386 | GBP | 2024-09-30 | 2025-06-17 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-09-30 | 2025-06-17 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 14760 | GBP | 2024-09-30 | 2026-04-27 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 100 | GBP | 2024-09-30 | 2025-06-17 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 14760 | GBP | 2024-09-30 | 2025-06-17 | filed | no | `core:Equity` | total-exemption-full |
| equity | 14860 | GBP | 2024-09-30 | 2025-06-17 | filed | no | `core:Equity` | total-exemption-full |
| equity | 14860 | GBP | 2024-09-30 | 2026-04-27 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 100 | GBP | 2024-09-30 | 2026-04-27 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-09-30 | 2026-04-27 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 14860 | GBP | 2024-09-30 | 2025-06-17 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 14860 | GBP | 2024-09-30 | 2026-04-27 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 11944 | GBP | 2024-09-30 | 2026-04-27 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 11944 | GBP | 2024-09-30 | 2025-06-17 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 20653 | GBP | 2024-09-30 | 2025-06-17 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 20653 | GBP | 2024-09-30 | 2026-04-27 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-09-30 | 2024-03-21 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-09-30 | 2025-06-17 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 54156 | GBP | 2023-09-30 | 2024-03-21 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 54156 | GBP | 2023-09-30 | 2025-06-17 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 11900 | GBP | 2023-09-30 | 2024-03-21 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 43990 | GBP | 2023-09-30 | 2024-03-21 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 63866 | GBP | 2023-09-30 | 2025-06-17 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 63866 | GBP | 2023-09-30 | 2024-03-21 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors | 9710 | GBP | 2023-09-30 | 2025-06-17 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 9710 | GBP | 2023-09-30 | 2025-06-17 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 9710 | GBP | 2023-09-30 | 2024-03-21 | filed | no | `core:Debtors` | total-exemption-full |
| equity | 16182 | GBP | 2023-09-30 | 2025-06-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 100 | GBP | 2023-09-30 | 2025-06-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 16082 | GBP | 2023-09-30 | 2024-03-21 | filed | no | `core:Equity` | total-exemption-full |
| equity | 16182 | GBP | 2023-09-30 | 2024-03-21 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 16082 | GBP | 2023-09-30 | 2025-06-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-09-30 | 2025-06-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-09-30 | 2024-03-21 | filed | no | `core:Equity` | total-exemption-full |
| net_assets | 16182 | GBP | 2023-09-30 | 2025-06-17 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 16182 | GBP | 2023-09-30 | 2024-03-21 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 19876 | GBP | 2023-09-30 | 2024-03-21 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 19876 | GBP | 2023-09-30 | 2025-06-17 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 28712 | GBP | 2023-09-30 | 2024-03-21 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 28712 | GBP | 2023-09-30 | 2025-06-17 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2022-09-30 | 2024-03-21 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 67153 | GBP | 2022-09-30 | 2024-03-21 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 18700 | GBP | 2022-09-30 | 2024-03-21 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 40741 | GBP | 2022-09-30 | 2024-03-21 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 79890 | GBP | 2022-09-30 | 2024-03-21 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 12737 | GBP | 2022-09-30 | 2024-03-21 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2022-09-30 | 2024-03-21 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 22949 | GBP | 2022-09-30 | 2024-03-21 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 22849 | GBP | 2022-09-30 | 2024-03-21 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 22949 | GBP | 2022-09-30 | 2024-03-21 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 39149 | GBP | 2022-09-30 | 2024-03-21 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 41649 | GBP | 2022-09-30 | 2024-03-21 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2026-04-27: `{"superseded_document_id": "gb:04528747:doc:6AFzMSLr2J2gmRLAo-ToiUXDghNit-Z-ozVBBdTakYo", "restatements": [{"concept": "average_employees", "period_end": "2024-09-30", "old_value": "2.0000", "new_valu`

## HARDSTATE LIMITED (`gb:04845277`)

- registration: `04845277` (GB), status active, incorporated 2003-07-25
- classification: ['11050', '62020'] (sic_2007)
- records: 6 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 63 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-12-31 | 2026-08-25 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 7356 | GBP | 2025-12-31 | 2026-08-25 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| equity | -71568 | GBP | 2025-12-31 | 2026-08-25 | filed | yes | `frs-core:Equity` | micro-entity |
| fixed_assets | 11090 | GBP | 2025-12-31 | 2026-08-25 | filed | yes | `frs-core:FixedAssets` | micro-entity |
| net_assets | -71568 | GBP | 2025-12-31 | 2026-08-25 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -81574 | GBP | 2025-12-31 | 2026-08-25 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -70484 | GBP | 2025-12-31 | 2026-08-25 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-12-31 | 2026-08-25 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-12-31 | 2025-08-22 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 9165 | GBP | 2024-12-31 | 2025-08-22 | filed | no | `frs-core:CurrentAssets` | micro-entity |
| current_assets | 9165 | GBP | 2024-12-31 | 2026-08-25 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| equity | -66410 | GBP | 2024-12-31 | 2026-08-25 | filed | yes | `frs-core:Equity` | micro-entity |
| equity | -66410 | GBP | 2024-12-31 | 2025-08-22 | filed | no | `frs-core:Equity` | micro-entity |
| fixed_assets | 13863 | GBP | 2024-12-31 | 2026-08-25 | filed | yes | `frs-core:FixedAssets` | micro-entity |
| fixed_assets | 13863 | GBP | 2024-12-31 | 2025-08-22 | filed | no | `frs-core:FixedAssets` | micro-entity |
| net_assets | -66410 | GBP | 2024-12-31 | 2026-08-25 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_assets | -66410 | GBP | 2024-12-31 | 2025-08-22 | filed | no | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -78606 | GBP | 2024-12-31 | 2025-08-22 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -78606 | GBP | 2024-12-31 | 2026-08-25 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -64743 | GBP | 2024-12-31 | 2025-08-22 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -64743 | GBP | 2024-12-31 | 2026-08-25 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-12-31 | 2024-09-25 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-12-31 | 2025-08-22 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 94416 | GBP | 2023-12-31 | 2024-09-25 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 13762 | GBP | 2023-12-31 | 2025-08-22 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| current_assets | 13762 | GBP | 2023-12-31 | 2024-09-25 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | -59890 | GBP | 2023-12-31 | 2024-09-25 | filed | no | `core:Equity` | micro-entity |
| equity | -59891 | GBP | 2023-12-31 | 2025-08-22 | filed | yes | `frs-core:Equity` | micro-entity |
| fixed_assets | 22346 | GBP | 2023-12-31 | 2025-08-22 | filed | yes | `frs-core:FixedAssets` | micro-entity |
| fixed_assets | 22347 | GBP | 2023-12-31 | 2024-09-25 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | -59891 | GBP | 2023-12-31 | 2025-08-22 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -79741 | GBP | 2023-12-31 | 2025-08-22 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -57395 | GBP | 2023-12-31 | 2025-08-22 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2022-12-31 | 2024-09-25 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 94050 | GBP | 2022-12-31 | 2024-09-25 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 34194 | GBP | 2022-12-31 | 2024-09-25 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -36037 | GBP | 2022-12-31 | 2024-09-25 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 26402 | GBP | 2022-12-31 | 2024-09-25 | filed | yes | `core:FixedAssets` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2025-08-22: `{"superseded_document_id": "gb:04845277:doc:dkh9OrwkYo2OMBQz_wwiB-lN-5NfUTepP0qjlVmSuXs", "restatements": [{"concept": "fixed_assets", "period_end": "2023-12-31", "old_value": "22347.0000", "new_value`

## JAV SOLUTIONS LIMITED (`gb:05276409`)

- registration: `05276409` (GB), status active, incorporated 2004-11-03
- classification: ['62030'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 55 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | iso4217:GBP | 2025-03-31 | 2025-12-08 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2025-03-31 | 2025-12-08 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 567 | GBP | 2025-03-31 | 2025-12-08 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 1547 | GBP | 2025-03-31 | 2025-12-08 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 983 | GBP | 2025-03-31 | 2025-12-08 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2025-03-31 | 2025-12-08 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 983 | GBP | 2025-03-31 | 2025-12-08 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 980 | GBP | 2025-03-31 | 2025-12-08 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 983 | GBP | 2025-03-31 | 2025-12-08 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2024-03-31 | 2025-12-08 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2024-03-31 | 2024-12-09 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2024-03-31 | 2025-12-08 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 567 | GBP | 2024-03-31 | 2024-12-09 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 567 | GBP | 2024-03-31 | 2025-12-08 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 1547 | GBP | 2024-03-31 | 2025-12-08 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 1547 | GBP | 2024-03-31 | 2024-12-09 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | 983 | GBP | 2024-03-31 | 2024-12-09 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 983 | GBP | 2024-03-31 | 2025-12-08 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2024-03-31 | 2025-12-08 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 983 | GBP | 2024-03-31 | 2025-12-08 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 983 | GBP | 2024-03-31 | 2024-12-09 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 980 | GBP | 2024-03-31 | 2024-12-09 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 980 | GBP | 2024-03-31 | 2025-12-08 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 983 | GBP | 2024-03-31 | 2024-12-09 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 983 | GBP | 2024-03-31 | 2025-12-08 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2023-03-31 | 2023-12-12 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2023-03-31 | 2024-12-09 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 56947 | GBP | 2023-03-31 | 2024-12-09 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 56947 | GBP | 2023-03-31 | 2023-12-12 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 6441 | GBP | 2023-03-31 | 2023-12-12 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 6441 | GBP | 2023-03-31 | 2024-12-09 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 50503 | GBP | 2023-03-31 | 2023-12-12 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 50503 | GBP | 2023-03-31 | 2024-12-09 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 50503 | GBP | 2023-03-31 | 2023-12-12 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 50503 | GBP | 2023-03-31 | 2024-12-09 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 50506 | GBP | 2023-03-31 | 2024-12-09 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 50506 | GBP | 2023-03-31 | 2023-12-12 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 50503 | GBP | 2023-03-31 | 2024-12-09 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 50503 | GBP | 2023-03-31 | 2023-12-12 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2022-03-31 | 2023-12-12 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 56947 | GBP | 2022-03-31 | 2023-12-12 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 6441 | GBP | 2022-03-31 | 2023-12-12 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 50503 | GBP | 2022-03-31 | 2023-12-12 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 50503 | GBP | 2022-03-31 | 2023-12-12 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 50506 | GBP | 2022-03-31 | 2023-12-12 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 50503 | GBP | 2022-03-31 | 2023-12-12 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._
