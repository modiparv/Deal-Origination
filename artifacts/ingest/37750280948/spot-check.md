# Ingest spot-check

- database: `data/engine.db`
- latest run: `20261008T083101Z-2063492c`
- companies in store: 21800; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## TIME SYSTEMS (UK) LIMITED (`gb:02110018`)

- registration: `02110018` (GB), status active, incorporated 1987-03-13
- classification: ['62012', '62020', '62030', '62090'] (sic_2007)
- records: 9 officers, 2 beneficial owners, 0 ownership statements, 1 security interests, 131 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 15 | xbrli:pure | 2025-03-31 | 2025-12-23 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 692561 | GBP | 2025-03-31 | 2025-12-23 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 278021 | GBP | 2025-03-31 | 2025-12-23 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 888006 | GBP | 2025-03-31 | 2025-12-23 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 102794 | GBP | 2025-03-31 | 2025-12-23 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 102794 | GBP | 2025-03-31 | 2025-12-23 | filed | yes | `core:Debtors` | total-exemption-full |
| fixed_assets | 591838 | GBP | 2025-03-31 | 2025-12-23 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | 1201823 | GBP | 2025-03-31 | 2025-12-23 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 609985 | GBP | 2025-03-31 | 2025-12-23 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1201823 | GBP | 2025-03-31 | 2025-12-23 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 17 | xbrli:pure | 2024-03-31 | 2024-11-05 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 17 | xbrli:pure | 2024-03-31 | 2025-12-23 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 723725 | GBP | 2024-03-31 | 2024-11-05 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 723725 | GBP | 2024-03-31 | 2025-12-23 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 305181 | GBP | 2024-03-31 | 2025-12-23 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 305181 | GBP | 2024-03-31 | 2024-11-05 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 931394 | GBP | 2024-03-31 | 2025-12-23 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 931394 | GBP | 2024-03-31 | 2024-11-05 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 131623 | GBP | 2024-03-31 | 2024-11-05 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 131623 | GBP | 2024-03-31 | 2025-12-23 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 131623 | GBP | 2024-03-31 | 2024-11-05 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 131623 | GBP | 2024-03-31 | 2025-12-23 | filed | yes | `core:Debtors` | total-exemption-full |
| fixed_assets | 597060 | GBP | 2024-03-31 | 2024-11-05 | filed | no | `core:FixedAssets` | total-exemption-full |
| fixed_assets | 597060 | GBP | 2024-03-31 | 2025-12-23 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | 1223197 | GBP | 2024-03-31 | 2025-12-23 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 1223197 | GBP | 2024-03-31 | 2024-11-05 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 626213 | GBP | 2024-03-31 | 2024-11-05 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 626213 | GBP | 2024-03-31 | 2025-12-23 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1223273 | GBP | 2024-03-31 | 2024-11-05 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1223273 | GBP | 2024-03-31 | 2025-12-23 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 16 | xbrli:pure | 2023-03-31 | 2024-11-05 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 16 | xbrli:pure | 2023-03-31 | 2023-10-26 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 790163 | GBP | 2023-03-31 | 2023-10-26 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 790163 | GBP | 2023-03-31 | 2024-11-05 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 316499 | GBP | 2023-03-31 | 2024-11-05 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 316499 | GBP | 2023-03-31 | 2023-10-26 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 1048654 | GBP | 2023-03-31 | 2024-11-05 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 1048654 | GBP | 2023-03-31 | 2023-10-26 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 156497 | GBP | 2023-03-31 | 2024-11-05 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 156497 | GBP | 2023-03-31 | 2023-10-26 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 156497 | GBP | 2023-03-31 | 2024-11-05 | filed | yes | `core:Debtors` | total-exemption-full |
| fixed_assets | 598895 | GBP | 2023-03-31 | 2024-11-05 | filed | yes | `core:FixedAssets` | total-exemption-full |
| fixed_assets | 598895 | GBP | 2023-03-31 | 2023-10-26 | filed | no | `core:FixedAssets` | total-exemption-full |
| net_assets | 1330371 | GBP | 2023-03-31 | 2023-10-26 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 1330371 | GBP | 2023-03-31 | 2024-11-05 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 732155 | GBP | 2023-03-31 | 2023-10-26 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 732155 | GBP | 2023-03-31 | 2024-11-05 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1331050 | GBP | 2023-03-31 | 2023-10-26 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1331050 | GBP | 2023-03-31 | 2024-11-05 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 15 | xbrli:pure | 2022-03-31 | 2023-10-26 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 587753 | GBP | 2022-03-31 | 2023-10-26 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 328429 | GBP | 2022-03-31 | 2023-10-26 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 807471 | GBP | 2022-03-31 | 2023-10-26 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 140822 | GBP | 2022-03-31 | 2023-10-26 | filed | yes | `core:Debtors` | total-exemption-full |
| fixed_assets | 824176 | GBP | 2022-03-31 | 2023-10-26 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | 1302786 | GBP | 2022-03-31 | 2023-10-26 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 479042 | GBP | 2022-03-31 | 2023-10-26 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1303218 | GBP | 2022-03-31 | 2023-10-26 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## HYDE DETAILS LIMITED (`gb:02652415`)

- registration: `02652415` (GB), status active, incorporated 1991-10-08
- classification: ['71129'] (sic_2007)
- records: 18 officers, 1 beneficial owners, 0 ownership statements, 4 security interests, 126 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 65 | xbrli:pure | 2025-09-30 | 2026-06-10 | filed | yes | `e:AverageNumberEmployeesDuringPeriod` | full |
| cash | 26503 | GBP | 2025-09-30 | 2026-06-10 | filed | yes | `e:CashBankOnHand` | full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1398810 | GBP | 2025-09-30 | 2026-06-10 | filed | yes | `e:Creditors` | full |
| current_assets | 12693020 | GBP | 2025-09-30 | 2026-06-10 | filed | yes | `e:CurrentAssets` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 11105349 | GBP | 2025-09-30 | 2026-06-10 | filed | yes | `e:Debtors` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-09-30 | 2026-06-10 | filed | yes | `e:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 12301934 | GBP | 2025-09-30 | 2026-06-10 | filed | yes | `e:Equity` | full |
| equity | 12302034 | GBP | 2025-09-30 | 2026-06-10 | filed | yes | `e:Equity` | full |
| gross_profit | 1201703 | GBP | 2025-09-30 | 2026-06-10 | filed | yes | `e:GrossProfitLoss` | full |
| net_assets | 12302034 | GBP | 2025-09-30 | 2026-06-10 | filed | yes | `e:NetAssetsLiabilities` | full |
| net_current_assets | 11294210 | GBP | 2025-09-30 | 2026-06-10 | filed | yes | `e:NetCurrentAssetsLiabilities` | full |
| operating_profit | 804338 | GBP | 2025-09-30 | 2026-06-10 | filed | yes | `e:OperatingProfitLoss` | full |
| profit_before_tax | 804338 | GBP | 2025-09-30 | 2026-06-10 | filed | yes | `e:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period | 450429 | GBP | 2025-09-30 | 2026-06-10 | filed | yes | `e:ProfitLoss` | full |
| revenue | 10165106 | GBP | 2025-09-30 | 2026-06-10 | filed | yes | `e:TurnoverRevenue` | full |
| staff_costs | 2834552 | GBP | 2025-09-30 | 2026-06-10 | filed | yes | `e:StaffCostsEmployeeBenefitsExpense` | full |
| tax_charge | 353909 | GBP | 2025-09-30 | 2026-06-10 | filed | yes | `e:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| total_assets_less_current_liabilities | 12403475 | GBP | 2025-09-30 | 2026-06-10 | filed | yes | `e:TotalAssetsLessCurrentLiabilities` | full |
| average_employees | 54 | xbrli:pure | 2024-09-30 | 2025-06-12 | filed | no | `d:AverageNumberEmployeesDuringPeriod` | small |
| average_employees | 54 | xbrli:pure | 2024-09-30 | 2026-06-10 | filed | yes | `e:AverageNumberEmployeesDuringPeriod` | full |
| cash | 0 | GBP | 2024-09-30 | 2026-06-10 | filed | yes | `e:CashBankOnHand` | full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1859681 | GBP | 2024-09-30 | 2025-06-12 | filed | no | `d:Creditors` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1859681 | GBP | 2024-09-30 | 2026-06-10 | filed | yes | `e:Creditors` | full |
| current_assets | 12963181 | GBP | 2024-09-30 | 2025-06-12 | filed | no | `d:CurrentAssets` | small |
| current_assets | 12963181 | GBP | 2024-09-30 | 2026-06-10 | filed | yes | `e:CurrentAssets` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 11931647 | GBP | 2024-09-30 | 2026-06-10 | filed | yes | `e:Debtors` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 11931647 | GBP | 2024-09-30 | 2025-06-12 | filed | no | `d:Debtors` | small |
| equity | 11851605 | GBP | 2024-09-30 | 2026-06-10 | filed | yes | `e:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 11851505 | GBP | 2024-09-30 | 2026-06-10 | filed | yes | `e:Equity` | full |
| equity | 11851605 | GBP | 2024-09-30 | 2025-06-12 | filed | no | `d:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-09-30 | 2026-06-10 | filed | yes | `e:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 11851505 | GBP | 2024-09-30 | 2025-06-12 | filed | no | `d:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-09-30 | 2025-06-12 | filed | no | `d:Equity` | small |
| gross_profit | 1138059 | GBP | 2024-09-30 | 2026-06-10 | filed | yes | `e:GrossProfitLoss` | full |
| net_assets | 11851605 | GBP | 2024-09-30 | 2025-06-12 | filed | no | `d:NetAssetsLiabilities` | small |
| net_assets | 11851605 | GBP | 2024-09-30 | 2026-06-10 | filed | yes | `e:NetAssetsLiabilities` | full |
| net_current_assets | 11103500 | GBP | 2024-09-30 | 2025-06-12 | filed | no | `d:NetCurrentAssetsLiabilities` | small |
| net_current_assets | 11103500 | GBP | 2024-09-30 | 2026-06-10 | filed | yes | `e:NetCurrentAssetsLiabilities` | full |
| operating_profit | 781139 | GBP | 2024-09-30 | 2026-06-10 | filed | yes | `e:OperatingProfitLoss` | full |
| profit_before_tax | 781139 | GBP | 2024-09-30 | 2026-06-10 | filed | yes | `e:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period | 731711 | GBP | 2024-09-30 | 2026-06-10 | filed | yes | `e:ProfitLoss` | full |
| revenue | 9821121 | GBP | 2024-09-30 | 2026-06-10 | filed | yes | `e:TurnoverRevenue` | full |
| staff_costs | 2325206 | GBP | 2024-09-30 | 2026-06-10 | filed | yes | `e:StaffCostsEmployeeBenefitsExpense` | full |
| tax_charge | 49428 | GBP | 2024-09-30 | 2026-06-10 | filed | yes | `e:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| total_assets_less_current_liabilities | 11884399 | GBP | 2024-09-30 | 2026-06-10 | filed | yes | `e:TotalAssetsLessCurrentLiabilities` | full |
| total_assets_less_current_liabilities | 11884399 | GBP | 2024-09-30 | 2025-06-12 | filed | no | `d:TotalAssetsLessCurrentLiabilities` | small |
| average_employees | 40 | xbrli:pure | 2023-09-30 | 2024-06-09 | filed | no | `d:AverageNumberEmployeesDuringPeriod` | small |
| average_employees | 40 | xbrli:pure | 2023-09-30 | 2025-06-12 | filed | yes | `d:AverageNumberEmployeesDuringPeriod` | small |
| cash | 0 | GBP | 2023-09-30 | 2024-06-09 | filed | yes | `d:CashBankOnHand` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1437514 | GBP | 2023-09-30 | 2024-06-09 | filed | no | `d:Creditors` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1437514 | GBP | 2023-09-30 | 2025-06-12 | filed | yes | `d:Creditors` | small |
| current_assets | 12111057 | GBP | 2023-09-30 | 2024-06-09 | filed | no | `d:CurrentAssets` | small |
| current_assets | 12111057 | GBP | 2023-09-30 | 2025-06-12 | filed | yes | `d:CurrentAssets` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 11396711 | GBP | 2023-09-30 | 2025-06-12 | filed | yes | `d:Debtors` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 11396711 | GBP | 2023-09-30 | 2024-06-09 | filed | no | `d:Debtors` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 11119794 | GBP | 2023-09-30 | 2025-06-12 | filed | yes | `d:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-09-30 | 2024-06-09 | filed | no | `d:Equity` | small |
| equity | 11119894 | GBP | 2023-09-30 | 2024-06-09 | filed | no | `d:Equity` | small |
| equity | 11119894 | GBP | 2023-09-30 | 2025-06-12 | filed | yes | `d:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-09-30 | 2025-06-12 | filed | yes | `d:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 11119794 | GBP | 2023-09-30 | 2024-06-09 | filed | no | `d:Equity` | small |
| net_assets | 11119894 | GBP | 2023-09-30 | 2025-06-12 | filed | yes | `d:NetAssetsLiabilities` | small |
| net_assets | 11119894 | GBP | 2023-09-30 | 2024-06-09 | filed | no | `d:NetAssetsLiabilities` | small |
| net_current_assets | 10673543 | GBP | 2023-09-30 | 2024-06-09 | filed | no | `d:NetCurrentAssetsLiabilities` | small |
| net_current_assets | 10673543 | GBP | 2023-09-30 | 2025-06-12 | filed | yes | `d:NetCurrentAssetsLiabilities` | small |
| total_assets_less_current_liabilities | 11119894 | GBP | 2023-09-30 | 2024-06-09 | filed | no | `d:TotalAssetsLessCurrentLiabilities` | small |
| total_assets_less_current_liabilities | 11119894 | GBP | 2023-09-30 | 2025-06-12 | filed | yes | `d:TotalAssetsLessCurrentLiabilities` | small |
| average_employees | 37 | xbrli:pure | 2022-09-30 | 2024-06-09 | filed | yes | `d:AverageNumberEmployeesDuringPeriod` | small |
| cash | 79376 | GBP | 2022-09-30 | 2024-06-09 | filed | yes | `d:CashBankOnHand` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 650634 | GBP | 2022-09-30 | 2024-06-09 | filed | yes | `d:Creditors` | small |
| current_assets | 10832761 | GBP | 2022-09-30 | 2024-06-09 | filed | yes | `d:CurrentAssets` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 10347101 | GBP | 2022-09-30 | 2024-06-09 | filed | yes | `d:Debtors` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2022-09-30 | 2024-06-09 | filed | yes | `d:Equity` | small |
| equity | 10716047 | GBP | 2022-09-30 | 2024-06-09 | filed | yes | `d:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 10715947 | GBP | 2022-09-30 | 2024-06-09 | filed | yes | `d:Equity` | small |
| net_assets | 10716047 | GBP | 2022-09-30 | 2024-06-09 | filed | yes | `d:NetAssetsLiabilities` | small |
| net_current_assets | 10182127 | GBP | 2022-09-30 | 2024-06-09 | filed | yes | `d:NetCurrentAssetsLiabilities` | small |
| total_assets_less_current_liabilities | 10716047 | GBP | 2022-09-30 | 2024-06-09 | filed | yes | `d:TotalAssetsLessCurrentLiabilities` | small |

_No coverage facts for the latest run._

## K S K ASSOCIATES LIMITED (`gb:03025252`)

- registration: `03025252` (GB), status active, incorporated 1995-02-22
- classification: ['71111'] (sic_2007)
- records: 5 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 82 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.01 | xbrli:pure | 2025-02-28 | 2025-11-27 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 29760 | GBP | 2025-02-28 | 2025-11-27 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2025-02-28 | 2025-11-27 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 40053 | GBP | 2025-02-28 | 2025-11-27 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 32107 | GBP | 2025-02-28 | 2025-11-27 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2347 | GBP | 2025-02-28 | 2025-11-27 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 2347 | GBP | 2025-02-28 | 2025-11-27 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | -4969 | GBP | 2025-02-28 | 2025-11-27 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 100 | GBP | 2025-02-28 | 2025-11-27 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -5069 | GBP | 2025-02-28 | 2025-11-27 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-02-28 | 2025-11-27 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | -4969 | GBP | 2025-02-28 | 2025-11-27 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -7946 | GBP | 2025-02-28 | 2025-11-27 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -4969 | GBP | 2025-02-28 | 2025-11-27 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-02-29 | 2024-12-11 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 0.01 | xbrli:pure | 2024-02-29 | 2025-11-27 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 32653 | GBP | 2024-02-29 | 2024-12-11 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 32653 | GBP | 2024-02-29 | 2025-11-27 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 18620 | GBP | 2024-02-29 | 2025-11-27 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 18620 | GBP | 2024-02-29 | 2024-12-11 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 54265 | GBP | 2024-02-29 | 2025-11-27 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 54265 | GBP | 2024-02-29 | 2024-12-11 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 41324 | GBP | 2024-02-29 | 2025-11-27 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 41324 | GBP | 2024-02-29 | 2024-12-11 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors | 8671 | GBP | 2024-02-29 | 2025-11-27 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 8671 | GBP | 2024-02-29 | 2024-12-11 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 8671 | GBP | 2024-02-29 | 2024-12-11 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 8671 | GBP | 2024-02-29 | 2025-11-27 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 100 | GBP | 2024-02-29 | 2025-11-27 | filed | yes | `core:Equity` | total-exemption-full |
| equity | -16679 | GBP | 2024-02-29 | 2024-12-11 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-02-29 | 2024-12-11 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -16779 | GBP | 2024-02-29 | 2024-12-11 | filed | no | `core:Equity` | total-exemption-full |
| equity | -16679 | GBP | 2024-02-29 | 2025-11-27 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -16779 | GBP | 2024-02-29 | 2025-11-27 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-02-29 | 2025-11-27 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | -16679 | GBP | 2024-02-29 | 2024-12-11 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | -16679 | GBP | 2024-02-29 | 2025-11-27 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -12941 | GBP | 2024-02-29 | 2024-12-11 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -12941 | GBP | 2024-02-29 | 2025-11-27 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1941 | GBP | 2024-02-29 | 2025-11-27 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1941 | GBP | 2024-02-29 | 2024-12-11 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-02-28 | 2024-12-11 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 98648 | GBP | 2023-02-28 | 2024-12-11 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 22105 | GBP | 2023-02-28 | 2024-12-11 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 130879 | GBP | 2023-02-28 | 2024-12-11 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 149448 | GBP | 2023-02-28 | 2024-12-11 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 50800 | GBP | 2023-02-28 | 2024-12-11 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 50800 | GBP | 2023-02-28 | 2024-12-11 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 21200 | GBP | 2023-02-28 | 2024-12-11 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 21300 | GBP | 2023-02-28 | 2024-12-11 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-02-28 | 2024-12-11 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 21300 | GBP | 2023-02-28 | 2024-12-11 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 18569 | GBP | 2023-02-28 | 2024-12-11 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 43405 | GBP | 2023-02-28 | 2024-12-11 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2025-11-27: `{"superseded_document_id": "gb:03025252:doc:YiydfNdMtFUjpy2hqu7paU8K93fbRET_8GVqb_NmwRY", "restatements": [{"concept": "average_employees", "period_end": "2024-02-29", "old_value": "1.0000", "new_valu`

## SEER SOLUTIONS LIMITED (`gb:03298022`)

- registration: `03298022` (GB), status active, incorporated 1996-12-31
- classification: ['62020'] (sic_2007)
- records: 5 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 71 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-12-31 | 2026-07-27 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 44991 | GBP | 2025-12-31 | 2026-07-27 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 84225 | GBP | 2025-12-31 | 2026-07-27 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 61091 | GBP | 2025-12-31 | 2026-07-27 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 2290 | GBP | 2025-12-31 | 2026-07-27 | filed | yes | `core:FixedAssets` | micro-entity |
| net_current_assets | 58801 | GBP | 2025-12-31 | 2026-07-27 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 61091 | GBP | 2025-12-31 | 2026-07-27 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-12-31 | 2026-07-27 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-12-31 | 2025-07-16 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 87312 | GBP | 2024-12-31 | 2025-07-16 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 87312 | GBP | 2024-12-31 | 2026-07-27 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 73374 | GBP | 2024-12-31 | 2026-07-27 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 73374 | GBP | 2024-12-31 | 2025-07-16 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 1083 | GBP | 2024-12-31 | 2026-07-27 | filed | yes | `core:Equity` | micro-entity |
| equity | 1083 | GBP | 2024-12-31 | 2025-07-16 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 819 | GBP | 2024-12-31 | 2025-07-16 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 819 | GBP | 2024-12-31 | 2026-07-27 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 1083 | GBP | 2024-12-31 | 2025-07-16 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 264 | GBP | 2024-12-31 | 2025-07-16 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 264 | GBP | 2024-12-31 | 2026-07-27 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 1083 | GBP | 2024-12-31 | 2026-07-27 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2023-12-31 | 2024-08-05 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-12-31 | 2025-07-16 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 84889 | GBP | 2023-12-31 | 2024-08-05 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 84889 | GBP | 2023-12-31 | 2025-07-16 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 73249 | GBP | 2023-12-31 | 2024-08-05 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 73249 | GBP | 2023-12-31 | 2025-07-16 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 2255 | GBP | 2023-12-31 | 2025-07-16 | filed | yes | `core:Equity` | micro-entity |
| equity | 2255 | GBP | 2023-12-31 | 2024-08-05 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 739 | GBP | 2023-12-31 | 2024-08-05 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 739 | GBP | 2023-12-31 | 2025-07-16 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 2255 | GBP | 2023-12-31 | 2025-07-16 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 2255 | GBP | 2023-12-31 | 2024-08-05 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 1516 | GBP | 2023-12-31 | 2024-08-05 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 1516 | GBP | 2023-12-31 | 2025-07-16 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2022-12-31 | 2024-08-05 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 59471 | GBP | 2022-12-31 | 2024-08-05 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 161998 | GBP | 2022-12-31 | 2024-08-05 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 102685 | GBP | 2022-12-31 | 2024-08-05 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 158 | GBP | 2022-12-31 | 2024-08-05 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 102685 | GBP | 2022-12-31 | 2024-08-05 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 102527 | GBP | 2022-12-31 | 2024-08-05 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2025-07-16: `{"superseded_document_id": "gb:03298022:doc:s8do-ttvrCh9RrduC3_A8nF7gFuORXxpy_aogkHjIVA", "restatements": [{"concept": "average_employees", "period_end": "2023-12-31", "old_value": "0.0000", "new_valu`

## C J S DESIGN LIMITED (`gb:03550934`)

- registration: `03550934` (GB), status active, incorporated 1998-04-22
- classification: ['71121'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 69 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-04-30 | 2026-01-30 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 4518 | GBP | 2025-04-30 | 2026-01-30 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 64947 | GBP | 2025-04-30 | 2026-01-30 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 60429 | GBP | 2025-04-30 | 2026-01-30 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-04-30 | 2026-01-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 83 | GBP | 2025-04-30 | 2026-01-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 183 | GBP | 2025-04-30 | 2026-01-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 183 | GBP | 2025-04-30 | 2026-01-30 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 9084 | GBP | 2025-04-30 | 2026-01-30 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 9163 | GBP | 2025-04-30 | 2026-01-30 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-04-30 | 2025-01-31 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-04-30 | 2026-01-30 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 8625 | GBP | 2024-04-30 | 2026-01-30 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 8625 | GBP | 2024-04-30 | 2025-01-31 | filed | no | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 37432 | GBP | 2024-04-30 | 2026-01-30 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 37432 | GBP | 2024-04-30 | 2025-01-31 | filed | no | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 28807 | GBP | 2024-04-30 | 2025-01-31 | filed | no | `frs-core:Debtors` | total-exemption-full |
| debtors | 28807 | GBP | 2024-04-30 | 2026-01-30 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -19128 | GBP | 2024-04-30 | 2026-01-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-04-30 | 2026-01-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -19129 | GBP | 2024-04-30 | 2025-01-31 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity | -19028 | GBP | 2024-04-30 | 2026-01-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-04-30 | 2025-01-31 | filed | no | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 1 | GBP | 2024-04-30 | 2025-01-31 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | -19029 | GBP | 2024-04-30 | 2025-01-31 | filed | no | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | -19028 | GBP | 2024-04-30 | 2026-01-30 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -7597 | GBP | 2024-04-30 | 2026-01-30 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -5198 | GBP | 2024-04-30 | 2025-01-31 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -7596 | GBP | 2024-04-30 | 2026-01-30 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -5197 | GBP | 2024-04-30 | 2025-01-31 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-04-30 | 2025-01-31 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-04-30 | 2024-01-31 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 13689 | GBP | 2023-04-30 | 2025-01-31 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| cash | 13689 | GBP | 2023-04-30 | 2024-01-31 | filed | no | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 49281 | GBP | 2023-04-30 | 2024-01-31 | filed | no | `frs-core:CurrentAssets` | total-exemption-full |
| current_assets | 49281 | GBP | 2023-04-30 | 2025-01-31 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 35592 | GBP | 2023-04-30 | 2024-01-31 | filed | no | `frs-core:Debtors` | total-exemption-full |
| debtors | 35592 | GBP | 2023-04-30 | 2025-01-31 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-04-30 | 2025-01-31 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-04-30 | 2024-01-31 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1224 | GBP | 2023-04-30 | 2024-01-31 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1224 | GBP | 2023-04-30 | 2025-01-31 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 184 | GBP | 2023-04-30 | 2025-01-31 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| fixed_assets | 184 | GBP | 2023-04-30 | 2024-01-31 | filed | no | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 1324 | GBP | 2023-04-30 | 2024-01-31 | filed | no | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 1324 | GBP | 2023-04-30 | 2025-01-31 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 17869 | GBP | 2023-04-30 | 2024-01-31 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 17869 | GBP | 2023-04-30 | 2025-01-31 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 18053 | GBP | 2023-04-30 | 2024-01-31 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 18053 | GBP | 2023-04-30 | 2025-01-31 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0 | xbrli:pure | 2022-04-30 | 2024-01-31 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 17838 | GBP | 2022-04-30 | 2024-01-31 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 52240 | GBP | 2022-04-30 | 2024-01-31 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 34402 | GBP | 2022-04-30 | 2024-01-31 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1519 | GBP | 2022-04-30 | 2024-01-31 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2022-04-30 | 2024-01-31 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 556 | GBP | 2022-04-30 | 2024-01-31 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 1619 | GBP | 2022-04-30 | 2024-01-31 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 20730 | GBP | 2022-04-30 | 2024-01-31 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 21286 | GBP | 2022-04-30 | 2024-01-31 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2026-01-30: `{"superseded_document_id": "gb:03550934:doc:G6RHJj-LdB_8ATV6iGBzOTySRZUBSAu7DLzH3yR24io", "restatements": [{"concept": "net_current_assets", "period_end": "2024-04-30", "old_value": "-5198.0000", "new`

## AXIOM GB LIMITED (`gb:03787813`)

- registration: `03787813` (GB), status active, incorporated 1999-06-11
- classification: ['71121'] (sic_2007)
- records: 8 officers, 4 beneficial owners, 0 ownership statements, 2 security interests, 108 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.1 | xbrli:pure | 2025-12-31 | 2026-09-15 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 59791 | GBP | 2025-12-31 | 2026-09-15 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 113119 | GBP | 2025-12-31 | 2026-09-15 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 716647 | GBP | 2025-12-31 | 2026-09-15 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 470513 | GBP | 2025-12-31 | 2026-09-15 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 246959 | GBP | 2025-12-31 | 2026-09-15 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 246959 | GBP | 2025-12-31 | 2026-09-15 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 40030 | GBP | 2025-12-31 | 2026-09-15 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 39828 | GBP | 2025-12-31 | 2026-09-15 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 202 | GBP | 2025-12-31 | 2026-09-15 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 40030 | GBP | 2025-12-31 | 2026-09-15 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -246134 | GBP | 2025-12-31 | 2026-09-15 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 153149 | GBP | 2025-12-31 | 2026-09-15 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 10 | xbrli:pure | 2024-12-31 | 2025-09-30 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 0.1 | xbrli:pure | 2024-12-31 | 2026-09-15 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 77236 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 77236 | GBP | 2024-12-31 | 2026-09-15 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 79112 | GBP | 2024-12-31 | 2026-09-15 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 79112 | GBP | 2024-12-31 | 2025-09-30 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 377780 | GBP | 2024-12-31 | 2025-09-30 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 377780 | GBP | 2024-12-31 | 2026-09-15 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 249450 | GBP | 2024-12-31 | 2026-09-15 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 249450 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 101680 | GBP | 2024-12-31 | 2026-09-15 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 101680 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 101680 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 101680 | GBP | 2024-12-31 | 2026-09-15 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 35284 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `core:Equity` | total-exemption-full |
| equity | 35486 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 202 | GBP | 2024-12-31 | 2026-09-15 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 35486 | GBP | 2024-12-31 | 2026-09-15 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 35284 | GBP | 2024-12-31 | 2026-09-15 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 202 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `core:Equity` | total-exemption-full |
| net_assets | 35486 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 35486 | GBP | 2024-12-31 | 2026-09-15 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -128330 | GBP | 2024-12-31 | 2026-09-15 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -128330 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 114598 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 114598 | GBP | 2024-12-31 | 2026-09-15 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 12 | xbrli:pure | 2023-12-31 | 2025-09-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 12 | xbrli:pure | 2023-12-31 | 2024-06-13 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 77936 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 77936 | GBP | 2023-12-31 | 2024-06-13 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2023-12-31 | 2024-06-13 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 421599 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 421599 | GBP | 2023-12-31 | 2024-06-13 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 511409 | GBP | 2023-12-31 | 2024-06-13 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 511409 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 380940 | GBP | 2023-12-31 | 2024-06-13 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 380940 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 380940 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 380940 | GBP | 2023-12-31 | 2024-06-13 | filed | no | `core:Debtors` | total-exemption-full |
| equity | 237050 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 236848 | GBP | 2023-12-31 | 2024-06-13 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 202 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 202 | GBP | 2023-12-31 | 2024-06-13 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 236848 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 237050 | GBP | 2023-12-31 | 2024-06-13 | filed | no | `core:Equity` | total-exemption-full |
| net_assets | 237050 | GBP | 2023-12-31 | 2024-06-13 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 237050 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 89810 | GBP | 2023-12-31 | 2024-06-13 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 89810 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 237050 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 237050 | GBP | 2023-12-31 | 2024-06-13 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 13 | xbrli:pure | 2022-12-31 | 2024-06-13 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 700016 | GBP | 2022-12-31 | 2024-06-13 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 34578 | GBP | 2022-12-31 | 2024-06-13 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 770742 | GBP | 2022-12-31 | 2024-06-13 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 1001403 | GBP | 2022-12-31 | 2024-06-13 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 223805 | GBP | 2022-12-31 | 2024-06-13 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 223805 | GBP | 2022-12-31 | 2024-06-13 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 205756 | GBP | 2022-12-31 | 2024-06-13 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 205554 | GBP | 2022-12-31 | 2024-06-13 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 202 | GBP | 2022-12-31 | 2024-06-13 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 205756 | GBP | 2022-12-31 | 2024-06-13 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 230661 | GBP | 2022-12-31 | 2024-06-13 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 262223 | GBP | 2022-12-31 | 2024-06-13 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2026-09-15: `{"superseded_document_id": "gb:03787813:doc:LEa0fcHRd9YxEVzxM-519YpE2xosRlRafqHOcRk0op4", "restatements": [{"concept": "average_employees", "period_end": "2024-12-31", "old_value": "10.0000", "new_val`

## FIRST B2B LIMITED (`gb:04024845`)

- registration: `04024845` (GB), status active, incorporated 2000-06-30
- classification: ['62090'] (sic_2007)
- records: 16 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 100 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.16 | xbrli:pure | 2025-03-31 | 2025-12-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 128359 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 1775 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 255813 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 546248 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 417889 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 417889 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShares'}` | 149 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 149 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 288827 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 288678 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass2'}` | 40 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass3'}` | 10 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 99 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 288827 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 290435 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 290602 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0.18 | xbrli:pure | 2024-03-31 | 2025-12-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 18 | xbrli:pure | 2024-03-31 | 2024-12-20 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 161973 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 161973 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 12289 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 12289 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 243807 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 243807 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 542466 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 542466 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 380493 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 380493 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 380493 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 380493 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 149 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass2'}` | 40 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 292169 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 292020 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShares'}` | 149 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass3'}` | 10 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 292020 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:Equity` | total-exemption-full |
| equity | 292169 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 99 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShares'}` | 149 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 149 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 292169 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 292169 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 298659 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 298659 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 304458 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 304458 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 18 | xbrli:pure | 2023-03-31 | 2024-12-20 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 141998 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 21740 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 258427 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 542018 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 400020 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 400020 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShares'}` | 149 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 149 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 276734 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 276883 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 276883 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 283591 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 298623 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2025-12-30: `{"superseded_document_id": "gb:04024845:doc:GQF6Jxnv-KqsFdY0rVEhSR71IW6zWP0IK6tJZN6rifE", "restatements": [{"concept": "average_employees", "period_end": "2024-03-31", "old_value": "18.0000", "new_val`

## XENOSYS LIMITED (`gb:04357526`)

- registration: `04357526` (GB), status active, incorporated 2002-01-21
- classification: ['62020'] (sic_2007)
- records: 5 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 60 filings, 2 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-04-30 | 2026-04-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 2046 | GBP | 2025-04-30 | 2026-04-30 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 170504 | GBP | 2025-04-30 | 2026-04-30 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 264394 | GBP | 2025-04-30 | 2026-04-30 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 492948 | GBP | 2025-04-30 | 2026-04-30 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 401654 | GBP | 2025-04-30 | 2026-04-30 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 492948 | GBP | 2025-04-30 | 2026-04-30 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 93890 | GBP | 2025-04-30 | 2026-04-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 495544 | GBP | 2025-04-30 | 2026-04-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-04-30 | 2026-04-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | -2 | xbrli:pure | 2024-04-30 | 2025-05-28 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | None |
| average_employees | -2 | xbrli:pure | 2024-04-30 | 2025-04-30 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 88561 | GBP | 2024-04-30 | 2025-04-30 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 88559 | GBP | 2024-04-30 | 2025-05-28 | filed | yes | `core:CashBankOnHand` | None |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 11732 | GBP | 2024-04-30 | 2025-05-28 | filed | no | `core:Creditors` | None |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 11732 | GBP | 2024-04-30 | 2026-04-30 | filed | yes | `core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 11732 | GBP | 2024-04-30 | 2025-04-30 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 127016 | GBP | 2024-04-30 | 2025-04-30 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 109038 | GBP | 2024-04-30 | 2025-05-28 | filed | no | `core:Creditors` | None |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 108488 | GBP | 2024-04-30 | 2026-04-30 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 139919 | GBP | 2024-04-30 | 2025-05-28 | filed | no | `core:CurrentAssets` | None |
| current_assets | 139921 | GBP | 2024-04-30 | 2025-04-30 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 139919 | GBP | 2024-04-30 | 2026-04-30 | filed | yes | `core:CurrentAssets` | micro-entity |
| debtors | 51360 | GBP | 2024-04-30 | 2025-04-30 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 51360 | GBP | 2024-04-30 | 2025-05-28 | filed | yes | `core:Debtors` | None |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-04-30 | 2025-04-30 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 413821 | GBP | 2024-04-30 | 2025-04-30 | filed | no | `core:Equity` | total-exemption-full |
| equity | 413921 | GBP | 2024-04-30 | 2025-04-30 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 431797 | GBP | 2024-04-30 | 2025-05-28 | filed | yes | `core:Equity` | None |
| equity | 431897 | GBP | 2024-04-30 | 2025-05-28 | filed | no | `core:Equity` | None |
| equity | 431897 | GBP | 2024-04-30 | 2026-04-30 | filed | yes | `core:Equity` | micro-entity |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-04-30 | 2025-05-28 | filed | yes | `core:Equity` | None |
| fixed_assets | 412748 | GBP | 2024-04-30 | 2025-04-30 | filed | no | `core:FixedAssets` | total-exemption-full |
| fixed_assets | 412748 | GBP | 2024-04-30 | 2026-04-30 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 412748 | GBP | 2024-04-30 | 2025-05-28 | filed | no | `core:FixedAssets` | None |
| net_assets | 431897 | GBP | 2024-04-30 | 2025-05-28 | filed | no | `core:NetAssetsLiabilities` | None |
| net_assets | 413921 | GBP | 2024-04-30 | 2025-04-30 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 431897 | GBP | 2024-04-30 | 2026-04-30 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 12905 | GBP | 2024-04-30 | 2025-04-30 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 31431 | GBP | 2024-04-30 | 2026-04-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 30881 | GBP | 2024-04-30 | 2025-05-28 | filed | no | `core:NetCurrentAssetsLiabilities` | None |
| total_assets_less_current_liabilities | 444179 | GBP | 2024-04-30 | 2026-04-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | -2 | xbrli:pure | 2023-04-30 | 2025-05-28 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | None |
| average_employees | -2 | xbrli:pure | 2023-04-30 | 2025-04-30 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 146260 | GBP | 2023-04-30 | 2025-05-28 | filed | yes | `core:CashBankOnHand` | None |
| cash | 146260 | GBP | 2023-04-30 | 2025-04-30 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 21674 | GBP | 2023-04-30 | 2025-05-28 | filed | yes | `core:Creditors` | None |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 21674 | GBP | 2023-04-30 | 2025-04-30 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 126748 | GBP | 2023-04-30 | 2025-05-28 | filed | yes | `core:Creditors` | None |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 126748 | GBP | 2023-04-30 | 2025-04-30 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 238110 | GBP | 2023-04-30 | 2025-05-28 | filed | yes | `core:CurrentAssets` | None |
| current_assets | 238110 | GBP | 2023-04-30 | 2025-04-30 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors | 91850 | GBP | 2023-04-30 | 2025-04-30 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 91850 | GBP | 2023-04-30 | 2025-05-28 | filed | yes | `core:Debtors` | None |
| equity | 421869 | GBP | 2023-04-30 | 2025-04-30 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-04-30 | 2025-04-30 | filed | no | `core:Equity` | total-exemption-full |
| equity | 421869 | GBP | 2023-04-30 | 2025-05-28 | filed | yes | `core:Equity` | None |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-04-30 | 2025-05-28 | filed | yes | `core:Equity` | None |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 421769 | GBP | 2023-04-30 | 2025-04-30 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 421769 | GBP | 2023-04-30 | 2025-05-28 | filed | yes | `core:Equity` | None |
| fixed_assets | 332181 | GBP | 2023-04-30 | 2025-05-28 | filed | yes | `core:FixedAssets` | None |
| fixed_assets | 332181 | GBP | 2023-04-30 | 2025-04-30 | filed | no | `core:FixedAssets` | total-exemption-full |
| net_assets | 421869 | GBP | 2023-04-30 | 2025-05-28 | filed | yes | `core:NetAssetsLiabilities` | None |
| net_assets | 421869 | GBP | 2023-04-30 | 2025-04-30 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 111362 | GBP | 2023-04-30 | 2025-04-30 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 111362 | GBP | 2023-04-30 | 2025-05-28 | filed | yes | `core:NetCurrentAssetsLiabilities` | None |

_No coverage facts for the latest run._

- event restatement @ 2025-05-28: `{"superseded_document_id": "gb:04357526:doc:Q3CRd-QBNv3GWoOIfnDUu8ct_pQU96Osgf0p1gJkMAQ", "restatements": [{"concept": "current_assets", "period_end": "2024-04-30", "old_value": "139921.0000", "new_va`
- event restatement @ 2026-04-30: `{"superseded_document_id": "gb:04357526:doc:wm2iDyTxhMl8I41ibHRgQDpjT5IfvvNF8KMkLJ3Fhbc", "restatements": [{"concept": "creditors_within_one_year", "period_end": "2024-04-30", "old_value": "109038.000`

## PYRAMID TECHNICAL CONSULTANTS EUROPE LTD (`gb:04802355`)

- registration: `04802355` (GB), status active, incorporated 2003-06-18
- classification: ['62090'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 55 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-06-30 | 2025-08-26 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 434309 | GBP | 2025-06-30 | 2025-08-26 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity | 439078 | GBP | 2025-06-30 | 2025-08-26 | filed | yes | `ns5:Equity` | micro-entity |
| fixed_assets | 46670 | GBP | 2025-06-30 | 2025-08-26 | filed | yes | `ns5:FixedAssets` | micro-entity |
| net_current_assets | 392408 | GBP | 2025-06-30 | 2025-08-26 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 439078 | GBP | 2025-06-30 | 2025-08-26 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2024-06-30 | 2024-09-18 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | xbrli:pure | 2024-06-30 | 2025-08-26 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 363881 | GBP | 2024-06-30 | 2025-08-26 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| current_assets | 363881 | GBP | 2024-06-30 | 2024-09-18 | filed | no | `ns5:CurrentAssets` | micro-entity |
| equity | 337113 | GBP | 2024-06-30 | 2025-08-26 | filed | yes | `ns5:Equity` | micro-entity |
| equity | 337113 | GBP | 2024-06-30 | 2024-09-18 | filed | no | `ns5:Equity` | micro-entity |
| fixed_assets | 18401 | GBP | 2024-06-30 | 2025-08-26 | filed | yes | `ns5:FixedAssets` | micro-entity |
| fixed_assets | 18401 | GBP | 2024-06-30 | 2024-09-18 | filed | no | `ns5:FixedAssets` | micro-entity |
| net_current_assets | 318712 | GBP | 2024-06-30 | 2024-09-18 | filed | no | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 318712 | GBP | 2024-06-30 | 2025-08-26 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 337113 | GBP | 2024-06-30 | 2025-08-26 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 337113 | GBP | 2024-06-30 | 2024-09-18 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-06-30 | 2024-09-18 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 1 | xbrli:pure | 2023-06-30 | 2023-09-29 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 298766 | GBP | 2023-06-30 | 2023-09-29 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| current_assets | 298766 | GBP | 2023-06-30 | 2024-09-18 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 274008 | GBP | 2023-06-30 | 2023-09-29 | filed | yes | `ns5:Equity` | micro-entity |
| equity | 274008 | GBP | 2023-06-30 | 2024-09-18 | filed | yes | `ns5:Equity` | micro-entity |
| fixed_assets `{'OriginalRevisedDataDimension': 'Original'}` | 19830 | GBP | 2023-06-30 | 2023-09-29 | filed | yes | `ns5:FixedAssets` | micro-entity |
| fixed_assets | 19830 | GBP | 2023-06-30 | 2024-09-18 | filed | yes | `ns5:FixedAssets` | micro-entity |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 254178 | GBP | 2023-06-30 | 2023-09-29 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 254178 | GBP | 2023-06-30 | 2024-09-18 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 274008 | GBP | 2023-06-30 | 2023-09-29 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 274008 | GBP | 2023-06-30 | 2024-09-18 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 0 | xbrli:pure | 2022-06-30 | 2023-09-29 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 212051 | GBP | 2022-06-30 | 2023-09-29 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 182662 | GBP | 2022-06-30 | 2023-09-29 | filed | yes | `ns5:Equity` | micro-entity |
| fixed_assets `{'OriginalRevisedDataDimension': 'Original'}` | 24204 | GBP | 2022-06-30 | 2023-09-29 | filed | yes | `ns5:FixedAssets` | micro-entity |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 158458 | GBP | 2022-06-30 | 2023-09-29 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 182662 | GBP | 2022-06-30 | 2023-09-29 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._
