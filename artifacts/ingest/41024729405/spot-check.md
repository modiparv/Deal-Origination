# Ingest spot-check

- database: `data/engine.db`
- latest run: `20261030T081132Z-c7f49298`
- companies in store: 39400; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## UNITECH ENGINEERING SERVICES LIMITED (`gb:02561637`)

- registration: `02561637` (GB), status active, incorporated 1990-11-23
- classification: ['71129'] (sic_2007)
- records: 8 officers, 3 beneficial owners, 0 ownership statements, 8 security interests, 122 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 12 | xbrli:pure | 2025-03-31 | 2025-08-05 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 92255 | GBP | 2025-03-31 | 2025-08-05 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 360445 | GBP | 2025-03-31 | 2025-08-05 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 548839 | GBP | 2025-03-31 | 2025-08-05 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 235032 | GBP | 2025-03-31 | 2025-08-05 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 235032 | GBP | 2025-03-31 | 2025-08-05 | filed | yes | `core:Debtors` | total-exemption-full |
| net_assets | 221872 | GBP | 2025-03-31 | 2025-08-05 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 188394 | GBP | 2025-03-31 | 2025-08-05 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 231627 | GBP | 2025-03-31 | 2025-08-05 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 14 | xbrli:pure | 2024-03-31 | 2024-08-15 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 14 | xbrli:pure | 2024-03-31 | 2025-08-05 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 95892 | GBP | 2024-03-31 | 2024-08-15 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 95892 | GBP | 2024-03-31 | 2025-08-05 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 64900 | GBP | 2024-03-31 | 2024-08-15 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 64900 | GBP | 2024-03-31 | 2025-08-05 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 391468 | GBP | 2024-03-31 | 2024-08-15 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 391468 | GBP | 2024-03-31 | 2025-08-05 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 896044 | GBP | 2024-03-31 | 2025-08-05 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 896044 | GBP | 2024-03-31 | 2024-08-15 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 599482 | GBP | 2024-03-31 | 2024-08-15 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 599482 | GBP | 2024-03-31 | 2025-08-05 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 599482 | GBP | 2024-03-31 | 2024-08-15 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 599482 | GBP | 2024-03-31 | 2025-08-05 | filed | yes | `core:Debtors` | total-exemption-full |
| net_assets | 472002 | GBP | 2024-03-31 | 2024-08-15 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 472002 | GBP | 2024-03-31 | 2025-08-05 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 504576 | GBP | 2024-03-31 | 2025-08-05 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 504576 | GBP | 2024-03-31 | 2024-08-15 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 546184 | GBP | 2024-03-31 | 2024-08-15 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 546184 | GBP | 2024-03-31 | 2025-08-05 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 13 | xbrli:pure | 2023-03-31 | 2024-08-15 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 13 | xbrli:pure | 2023-03-31 | 2023-10-18 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 50000 | GBP | 2023-03-31 | 2023-10-18 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 50000 | GBP | 2023-03-31 | 2024-08-15 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 130098 | GBP | 2023-03-31 | 2023-10-18 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 130098 | GBP | 2023-03-31 | 2024-08-15 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 643253 | GBP | 2023-03-31 | 2024-08-15 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 643253 | GBP | 2023-03-31 | 2023-10-18 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 1031010 | GBP | 2023-03-31 | 2023-10-18 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 1031010 | GBP | 2023-03-31 | 2024-08-15 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 806772 | GBP | 2023-03-31 | 2023-10-18 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 806772 | GBP | 2023-03-31 | 2023-10-18 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 806772 | GBP | 2023-03-31 | 2024-08-15 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 806772 | GBP | 2023-03-31 | 2024-08-15 | filed | yes | `core:Debtors` | total-exemption-full |
| net_assets | 285278 | GBP | 2023-03-31 | 2024-08-15 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 285278 | GBP | 2023-03-31 | 2023-10-18 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 387757 | GBP | 2023-03-31 | 2023-10-18 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 387757 | GBP | 2023-03-31 | 2024-08-15 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 420736 | GBP | 2023-03-31 | 2024-08-15 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 420736 | GBP | 2023-03-31 | 2023-10-18 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 9 | xbrli:pure | 2022-03-31 | 2023-10-18 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 219373 | GBP | 2022-03-31 | 2023-10-18 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 182292 | GBP | 2022-03-31 | 2023-10-18 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 482383 | GBP | 2022-03-31 | 2023-10-18 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 864602 | GBP | 2022-03-31 | 2023-10-18 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 537521 | GBP | 2022-03-31 | 2023-10-18 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 537521 | GBP | 2022-03-31 | 2023-10-18 | filed | yes | `core:Debtors` | total-exemption-full |
| net_assets | 231633 | GBP | 2022-03-31 | 2023-10-18 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 382219 | GBP | 2022-03-31 | 2023-10-18 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 420172 | GBP | 2022-03-31 | 2023-10-18 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## CONTEMPORARY CONTROLS LTD (`gb:03196119`)

- registration: `03196119` (GB), status active, incorporated 1996-05-09
- classification: ['62020', '62090'] (sic_2007)
- records: 8 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 97 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.02 | xbrli:pure | 2024-12-31 | 2025-09-03 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | full |
| cash | 51977 | GBP | 2024-12-31 | 2025-09-03 | filed | yes | `core:CashBankOnHand` | full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 98028 | GBP | 2024-12-31 | 2025-09-03 | filed | yes | `core:Creditors` | full |
| current_assets | 356923 | GBP | 2024-12-31 | 2025-09-03 | filed | yes | `core:CurrentAssets` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 161788 | GBP | 2024-12-31 | 2025-09-03 | filed | yes | `core:Debtors` | full |
| debtors | 161788 | GBP | 2024-12-31 | 2025-09-03 | filed | yes | `core:Debtors` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 95000 | GBP | 2024-12-31 | 2025-09-03 | filed | yes | `core:Equity` | full |
| equity | 258918 | GBP | 2024-12-31 | 2025-09-03 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 163918 | GBP | 2024-12-31 | 2025-09-03 | filed | yes | `core:Equity` | full |
| net_current_assets | 258895 | GBP | 2024-12-31 | 2025-09-03 | filed | yes | `core:NetCurrentAssetsLiabilities` | full |
| profit_before_tax | 19388 | GBP | 2024-12-31 | 2025-09-03 | filed | yes | `core:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period | 19388 | GBP | 2024-12-31 | 2025-09-03 | filed | yes | `core:ProfitLoss` | full |
| tax_charge | 0 | GBP | 2024-12-31 | 2025-09-03 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| total_assets_less_current_liabilities | 258918 | GBP | 2024-12-31 | 2025-09-03 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | full |
| average_employees | 0.02 | xbrli:pure | 2023-12-31 | 2025-09-03 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | full |
| average_employees | 2 | xbrli:pure | 2023-12-31 | 2024-09-04 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | full |
| cash | 54510 | GBP | 2023-12-31 | 2024-09-04 | filed | no | `core:CashBankOnHand` | full |
| cash | 54510 | GBP | 2023-12-31 | 2025-09-03 | filed | yes | `core:CashBankOnHand` | full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 135090 | GBP | 2023-12-31 | 2025-09-03 | filed | yes | `core:Creditors` | full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 135090 | GBP | 2023-12-31 | 2024-09-04 | filed | no | `core:Creditors` | full |
| current_assets | 374325 | GBP | 2023-12-31 | 2024-09-04 | filed | no | `core:CurrentAssets` | full |
| current_assets | 374325 | GBP | 2023-12-31 | 2025-09-03 | filed | yes | `core:CurrentAssets` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 157718 | GBP | 2023-12-31 | 2024-09-04 | filed | no | `core:Debtors` | full |
| debtors | 157718 | GBP | 2023-12-31 | 2024-09-04 | filed | no | `core:Debtors` | full |
| debtors | 157718 | GBP | 2023-12-31 | 2025-09-03 | filed | yes | `core:Debtors` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 157718 | GBP | 2023-12-31 | 2025-09-03 | filed | yes | `core:Debtors` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 95000 | GBP | 2023-12-31 | 2024-09-04 | filed | no | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 144530 | GBP | 2023-12-31 | 2025-09-03 | filed | yes | `core:Equity` | full |
| equity | 239530 | GBP | 2023-12-31 | 2025-09-03 | filed | yes | `core:Equity` | full |
| equity | 239530 | GBP | 2023-12-31 | 2024-09-04 | filed | no | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 95000 | GBP | 2023-12-31 | 2025-09-03 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 144530 | GBP | 2023-12-31 | 2024-09-04 | filed | no | `core:Equity` | full |
| net_current_assets | 239235 | GBP | 2023-12-31 | 2024-09-04 | filed | no | `core:NetCurrentAssetsLiabilities` | full |
| net_current_assets | 239235 | GBP | 2023-12-31 | 2025-09-03 | filed | yes | `core:NetCurrentAssetsLiabilities` | full |
| profit_before_tax | 72973 | GBP | 2023-12-31 | 2024-09-04 | filed | no | `core:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_before_tax | 72973 | GBP | 2023-12-31 | 2025-09-03 | filed | yes | `core:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period | 72973 | GBP | 2023-12-31 | 2025-09-03 | filed | yes | `core:ProfitLoss` | full |
| profit_for_period | 72973 | GBP | 2023-12-31 | 2024-09-04 | filed | no | `core:ProfitLoss` | full |
| tax_charge | 0 | GBP | 2023-12-31 | 2025-09-03 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| tax_charge | 0 | GBP | 2023-12-31 | 2024-09-04 | filed | no | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| total_assets_less_current_liabilities | 239530 | GBP | 2023-12-31 | 2024-09-04 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | full |
| total_assets_less_current_liabilities | 239530 | GBP | 2023-12-31 | 2025-09-03 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | full |
| average_employees | 2 | xbrli:pure | 2022-12-31 | 2024-09-04 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | full |
| cash | 54773 | GBP | 2022-12-31 | 2024-09-04 | filed | yes | `core:CashBankOnHand` | full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 230741 | GBP | 2022-12-31 | 2024-09-04 | filed | yes | `core:Creditors` | full |
| current_assets | 396597 | GBP | 2022-12-31 | 2024-09-04 | filed | yes | `core:CurrentAssets` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 192739 | GBP | 2022-12-31 | 2024-09-04 | filed | yes | `core:Debtors` | full |
| debtors | 192739 | GBP | 2022-12-31 | 2024-09-04 | filed | yes | `core:Debtors` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 71557 | GBP | 2022-12-31 | 2024-09-04 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 95000 | GBP | 2022-12-31 | 2024-09-04 | filed | yes | `core:Equity` | full |
| equity | 166557 | GBP | 2022-12-31 | 2024-09-04 | filed | yes | `core:Equity` | full |
| net_current_assets | 165856 | GBP | 2022-12-31 | 2024-09-04 | filed | yes | `core:NetCurrentAssetsLiabilities` | full |
| profit_before_tax | 36807 | GBP | 2022-12-31 | 2024-09-04 | filed | yes | `core:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period | 36807 | GBP | 2022-12-31 | 2024-09-04 | filed | yes | `core:ProfitLoss` | full |
| tax_charge | 0 | GBP | 2022-12-31 | 2024-09-04 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| total_assets_less_current_liabilities | 166557 | GBP | 2022-12-31 | 2024-09-04 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | full |

_No coverage facts for the latest run._

- event restatement @ 2025-09-03: `{"superseded_document_id": "gb:03196119:doc:oJUT0lcm3N5oTb5aYW2TsDtCCC-v3pfXK3v1ydNfaFU", "restatements": [{"concept": "average_employees", "period_end": "2023-12-31", "old_value": "2.0000", "new_valu`

## ADVANIA UK LIMITED (`gb:03645998`)

- registration: `03645998` (GB), status active, incorporated 1998-10-07
- classification: ['62020'] (sic_2007)
- records: 25 officers, 3 beneficial owners, 0 ownership statements, 15 security interests, 183 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## DESIGNS FOR LIGHTING LTD (`gb:04081039`)

- registration: `04081039` (GB), status active, incorporated 2000-09-29
- classification: ['71129'] (sic_2007)
- records: 7 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 103 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 19 | xbrli:pure | 2026-03-31 | 2026-07-22 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 416617 | GBP | 2026-03-31 | 2026-07-22 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 274945 | GBP | 2026-03-31 | 2026-07-22 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 984292 | GBP | 2026-03-31 | 2026-07-22 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 304712 | GBP | 2026-03-31 | 2026-07-22 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 304712 | GBP | 2026-03-31 | 2026-07-22 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 727527 | GBP | 2026-03-31 | 2026-07-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 75 | GBP | 2026-03-31 | 2026-07-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 36935 | GBP | 2026-03-31 | 2026-07-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 160 | GBP | 2026-03-31 | 2026-07-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 690357 | GBP | 2026-03-31 | 2026-07-22 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 727527 | GBP | 2026-03-31 | 2026-07-22 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 709347 | GBP | 2026-03-31 | 2026-07-22 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| average_employees | 20 | xbrli:pure | 2025-03-31 | 2025-08-26 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 20 | xbrli:pure | 2025-03-31 | 2026-07-22 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 311127 | GBP | 2025-03-31 | 2026-07-22 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 311127 | GBP | 2025-03-31 | 2025-08-26 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 242296 | GBP | 2025-03-31 | 2025-08-26 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 242296 | GBP | 2025-03-31 | 2026-07-22 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 788146 | GBP | 2025-03-31 | 2026-07-22 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 788146 | GBP | 2025-03-31 | 2025-08-26 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors | 239956 | GBP | 2025-03-31 | 2026-07-22 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 239956 | GBP | 2025-03-31 | 2026-07-22 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 239956 | GBP | 2025-03-31 | 2025-08-26 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 239956 | GBP | 2025-03-31 | 2025-08-26 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 555666 | GBP | 2025-03-31 | 2026-07-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 36935 | GBP | 2025-03-31 | 2026-07-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 160 | GBP | 2025-03-31 | 2026-07-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 555666 | GBP | 2025-03-31 | 2025-08-26 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 36935 | GBP | 2025-03-31 | 2025-08-26 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 160 | GBP | 2025-03-31 | 2025-08-26 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 75 | GBP | 2025-03-31 | 2026-07-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 518496 | GBP | 2025-03-31 | 2026-07-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 518496 | GBP | 2025-03-31 | 2025-08-26 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 75 | GBP | 2025-03-31 | 2025-08-26 | filed | no | `core:Equity` | total-exemption-full |
| net_assets | 555666 | GBP | 2025-03-31 | 2026-07-22 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 555666 | GBP | 2025-03-31 | 2025-08-26 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 545850 | GBP | 2025-03-31 | 2025-08-26 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 545850 | GBP | 2025-03-31 | 2026-07-22 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| average_employees | 25 | xbrli:pure | 2024-03-31 | 2024-08-08 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 25 | xbrli:pure | 2024-03-31 | 2025-08-26 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 259088 | GBP | 2024-03-31 | 2025-08-26 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 259088 | GBP | 2024-03-31 | 2024-08-08 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 216922 | GBP | 2024-03-31 | 2025-08-26 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 216922 | GBP | 2024-03-31 | 2024-08-08 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 752946 | GBP | 2024-03-31 | 2024-08-08 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 752946 | GBP | 2024-03-31 | 2025-08-26 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 290478 | GBP | 2024-03-31 | 2025-08-26 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 290478 | GBP | 2024-03-31 | 2024-08-08 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 290478 | GBP | 2024-03-31 | 2025-08-26 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 290478 | GBP | 2024-03-31 | 2024-08-08 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 544410 | GBP | 2024-03-31 | 2024-08-08 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 160 | GBP | 2024-03-31 | 2024-08-08 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 544410 | GBP | 2024-03-31 | 2025-08-26 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 75 | GBP | 2024-03-31 | 2024-08-08 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 36935 | GBP | 2024-03-31 | 2025-08-26 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 36935 | GBP | 2024-03-31 | 2024-08-08 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 507240 | GBP | 2024-03-31 | 2024-08-08 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 75 | GBP | 2024-03-31 | 2025-08-26 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 160 | GBP | 2024-03-31 | 2025-08-26 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 507240 | GBP | 2024-03-31 | 2025-08-26 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 544410 | GBP | 2024-03-31 | 2025-08-26 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 544410 | GBP | 2024-03-31 | 2024-08-08 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 536024 | GBP | 2024-03-31 | 2024-08-08 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 536024 | GBP | 2024-03-31 | 2025-08-26 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| average_employees | 23 | xbrli:pure | 2023-03-31 | 2024-08-08 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 341960 | GBP | 2023-03-31 | 2024-08-08 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 194131 | GBP | 2023-03-31 | 2024-08-08 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 810965 | GBP | 2023-03-31 | 2024-08-08 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 252754 | GBP | 2023-03-31 | 2024-08-08 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 252754 | GBP | 2023-03-31 | 2024-08-08 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 160 | GBP | 2023-03-31 | 2024-08-08 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 36935 | GBP | 2023-03-31 | 2024-08-08 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 590580 | GBP | 2023-03-31 | 2024-08-08 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 627750 | GBP | 2023-03-31 | 2024-08-08 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 75 | GBP | 2023-03-31 | 2024-08-08 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 627750 | GBP | 2023-03-31 | 2024-08-08 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 616834 | GBP | 2023-03-31 | 2024-08-08 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## FIRE WITHOUT SMOKE SOFTWARE LIMITED (`gb:04522608`)

- registration: `04522608` (GB), status active, incorporated 2002-08-30
- classification: ['62012', '62020', '63110', '63120'] (sic_2007)
- records: 9 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 78 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | xbrli:pure | 2025-08-31 | 2026-05-29 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 12870 | GBP | 2025-08-31 | 2026-05-29 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | -10759 | GBP | 2025-08-31 | 2026-05-29 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -23629 | GBP | 2025-08-31 | 2026-05-29 | filed | yes | `core:Equity` | micro-entity |
| net_current_assets | -23629 | GBP | 2025-08-31 | 2026-05-29 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -23629 | GBP | 2025-08-31 | 2026-05-29 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2024-08-31 | 2025-05-23 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | xbrli:pure | 2024-08-31 | 2026-05-29 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 12870 | GBP | 2024-08-31 | 2026-05-29 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 12870 | GBP | 2024-08-31 | 2025-05-23 | filed | no | `core:Creditors` | micro-entity |
| current_assets | -10759 | GBP | 2024-08-31 | 2025-05-23 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | -10759 | GBP | 2024-08-31 | 2026-05-29 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -23629 | GBP | 2024-08-31 | 2025-05-23 | filed | no | `core:Equity` | micro-entity |
| equity | -23629 | GBP | 2024-08-31 | 2026-05-29 | filed | yes | `core:Equity` | micro-entity |
| net_current_assets | -23629 | GBP | 2024-08-31 | 2025-05-23 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -23629 | GBP | 2024-08-31 | 2026-05-29 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -23629 | GBP | 2024-08-31 | 2025-05-23 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -23629 | GBP | 2024-08-31 | 2026-05-29 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2023-08-31 | 2025-05-23 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | xbrli:pure | 2023-08-31 | 2024-05-28 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 12870 | GBP | 2023-08-31 | 2025-05-23 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 12870 | GBP | 2023-08-31 | 2024-05-28 | filed | no | `core:Creditors` | micro-entity |
| current_assets | -12740 | GBP | 2023-08-31 | 2025-05-23 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | -12740 | GBP | 2023-08-31 | 2024-05-28 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | -25610 | GBP | 2023-08-31 | 2024-05-28 | filed | no | `core:Equity` | micro-entity |
| equity | -25610 | GBP | 2023-08-31 | 2025-05-23 | filed | yes | `core:Equity` | micro-entity |
| net_current_assets | -25610 | GBP | 2023-08-31 | 2025-05-23 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -25610 | GBP | 2023-08-31 | 2024-05-28 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -25610 | GBP | 2023-08-31 | 2024-05-28 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -25610 | GBP | 2023-08-31 | 2025-05-23 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## R2C ONLINE LIMITED (`gb:04978908`)

- registration: `04978908` (GB), status active, incorporated 2003-11-28
- classification: ['62012'] (sic_2007)
- records: 17 officers, 2 beneficial owners, 0 ownership statements, 4 security interests, 122 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 53 | xbrli:pure | 2025-12-31 | 2026-05-22 | filed | yes | `d:AverageNumberEmployeesDuringPeriod` | full |
| cash | 203782 | GBP | 2025-12-31 | 2026-05-22 | filed | yes | `d:CashBankOnHand` | full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 3388309 | GBP | 2025-12-31 | 2026-05-22 | filed | yes | `d:Creditors` | full |
| current_assets | 1012257 | GBP | 2025-12-31 | 2026-05-22 | filed | yes | `d:CurrentAssets` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 808475 | GBP | 2025-12-31 | 2026-05-22 | filed | yes | `d:Debtors` | full |
| equity | 1423951 | GBP | 2025-12-31 | 2026-05-22 | filed | yes | `d:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1670 | GBP | 2025-12-31 | 2026-05-22 | filed | yes | `d:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1422281 | GBP | 2025-12-31 | 2026-05-22 | filed | yes | `d:Equity` | full |
| fixed_assets | 3867288 | GBP | 2025-12-31 | 2026-05-22 | filed | yes | `d:FixedAssets` | full |
| gross_profit | 11826490 | GBP | 2025-12-31 | 2026-05-22 | filed | yes | `d:GrossProfitLoss` | full |
| net_assets | 1423951 | GBP | 2025-12-31 | 2026-05-22 | filed | yes | `d:NetAssetsLiabilities` | full |
| net_current_assets | -2376052 | GBP | 2025-12-31 | 2026-05-22 | filed | yes | `d:NetCurrentAssetsLiabilities` | full |
| operating_profit | 8634013 | GBP | 2025-12-31 | 2026-05-22 | filed | yes | `d:OperatingProfitLoss` | full |
| profit_before_tax | 8634013 | GBP | 2025-12-31 | 2026-05-22 | filed | yes | `d:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 6475509 | GBP | 2025-12-31 | 2026-05-22 | filed | yes | `d:ProfitLoss` | full |
| revenue | 12196607 | GBP | 2025-12-31 | 2026-05-22 | filed | yes | `d:TurnoverRevenue` | full |
| staff_costs | 2131008 | GBP | 2025-12-31 | 2026-05-22 | filed | yes | `d:StaffCostsEmployeeBenefitsExpense` | full |
| tax_charge | 2158504 | GBP | 2025-12-31 | 2026-05-22 | filed | yes | `d:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| total_assets_less_current_liabilities | 1491236 | GBP | 2025-12-31 | 2026-05-22 | filed | yes | `d:TotalAssetsLessCurrentLiabilities` | full |
| average_employees | 54 | xbrli:pure | 2024-12-31 | 2026-05-22 | filed | yes | `d:AverageNumberEmployeesDuringPeriod` | full |
| average_employees | 0 | xbrli:pure | 2024-12-31 | 2025-08-15 | filed | no | `d:AverageNumberEmployeesDuringPeriod` | full |
| cash | 1277367 | GBP | 2024-12-31 | 2026-05-22 | filed | yes | `d:CashBankOnHand` | full |
| cash | 1277367 | GBP | 2024-12-31 | 2025-08-15 | filed | no | `d:CashBankOnHand` | full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1992746 | GBP | 2024-12-31 | 2025-08-15 | filed | no | `d:Creditors` | full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1992746 | GBP | 2024-12-31 | 2026-05-22 | filed | yes | `d:Creditors` | full |
| current_assets | 20929575 | GBP | 2024-12-31 | 2026-05-22 | filed | yes | `d:CurrentAssets` | full |
| current_assets | 20929575 | GBP | 2024-12-31 | 2025-08-15 | filed | no | `d:CurrentAssets` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 19652208 | GBP | 2024-12-31 | 2025-08-15 | filed | no | `d:Debtors` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 19652208 | GBP | 2024-12-31 | 2026-05-22 | filed | yes | `d:Debtors` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1670 | GBP | 2024-12-31 | 2026-05-22 | filed | yes | `d:Equity` | full |
| equity | 22212303 | GBP | 2024-12-31 | 2026-05-22 | filed | yes | `d:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 22210633 | GBP | 2024-12-31 | 2025-08-15 | filed | no | `d:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1670 | GBP | 2024-12-31 | 2025-08-15 | filed | no | `d:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 22210633 | GBP | 2024-12-31 | 2026-05-22 | filed | yes | `d:Equity` | full |
| equity | 22212303 | GBP | 2024-12-31 | 2025-08-15 | filed | no | `d:Equity` | full |
| fixed_assets | 3371715 | GBP | 2024-12-31 | 2026-05-22 | filed | yes | `d:FixedAssets` | full |
| fixed_assets | 3371715 | GBP | 2024-12-31 | 2025-08-15 | filed | no | `d:FixedAssets` | full |
| gross_profit | 10234659 | GBP | 2024-12-31 | 2026-05-22 | filed | yes | `d:GrossProfitLoss` | full |
| gross_profit | 10234659 | GBP | 2024-12-31 | 2025-08-15 | filed | no | `d:GrossProfitLoss` | full |
| net_assets | 22212303 | GBP | 2024-12-31 | 2025-08-15 | filed | no | `d:NetAssetsLiabilities` | full |
| net_assets | 22212303 | GBP | 2024-12-31 | 2026-05-22 | filed | yes | `d:NetAssetsLiabilities` | full |
| net_current_assets | 18936829 | GBP | 2024-12-31 | 2026-05-22 | filed | yes | `d:NetCurrentAssetsLiabilities` | full |
| net_current_assets | 18936829 | GBP | 2024-12-31 | 2025-08-15 | filed | no | `d:NetCurrentAssetsLiabilities` | full |
| operating_profit | 6877260 | GBP | 2024-12-31 | 2026-05-22 | filed | yes | `d:OperatingProfitLoss` | full |
| operating_profit | 6877260 | GBP | 2024-12-31 | 2025-08-15 | filed | no | `d:OperatingProfitLoss` | full |
| profit_before_tax | 6884572 | GBP | 2024-12-31 | 2025-08-15 | filed | no | `d:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_before_tax | 6884572 | GBP | 2024-12-31 | 2026-05-22 | filed | yes | `d:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 5163430 | GBP | 2024-12-31 | 2025-08-15 | filed | no | `d:ProfitLoss` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 5163430 | GBP | 2024-12-31 | 2026-05-22 | filed | yes | `d:ProfitLoss` | full |
| revenue | 10616979 | GBP | 2024-12-31 | 2026-05-22 | filed | yes | `d:TurnoverRevenue` | full |
| revenue | 10616979 | GBP | 2024-12-31 | 2025-08-15 | filed | no | `d:TurnoverRevenue` | full |
| staff_costs | 2287967 | GBP | 2024-12-31 | 2025-08-15 | filed | no | `d:StaffCostsEmployeeBenefitsExpense` | full |
| staff_costs | 2287967 | GBP | 2024-12-31 | 2026-05-22 | filed | yes | `d:StaffCostsEmployeeBenefitsExpense` | full |
| tax_charge | 1721142 | GBP | 2024-12-31 | 2025-08-15 | filed | no | `d:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| tax_charge | 1721142 | GBP | 2024-12-31 | 2026-05-22 | filed | yes | `d:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| total_assets_less_current_liabilities | 22308544 | GBP | 2024-12-31 | 2026-05-22 | filed | yes | `d:TotalAssetsLessCurrentLiabilities` | full |
| total_assets_less_current_liabilities | 22308544 | GBP | 2024-12-31 | 2025-08-15 | filed | no | `d:TotalAssetsLessCurrentLiabilities` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 17047203 | GBP | 2024-01-01 | 2026-05-22 | filed | yes | `d:Equity` | full |
| average_employees | 54 | xbrli:pure | 2023-12-31 | 2024-06-24 | filed | no | `d:AverageNumberEmployeesDuringPeriod` | full |
| average_employees | 54 | xbrli:pure | 2023-12-31 | 2025-08-15 | filed | yes | `d:AverageNumberEmployeesDuringPeriod` | full |
| cash | 2064696 | GBP | 2023-12-31 | 2024-06-24 | filed | no | `d:CashBankOnHand` | full |
| cash | 2064696 | GBP | 2023-12-31 | 2025-08-15 | filed | yes | `d:CashBankOnHand` | full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1904458 | GBP | 2023-12-31 | 2025-08-15 | filed | yes | `d:Creditors` | full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1904458 | GBP | 2023-12-31 | 2024-06-24 | filed | no | `d:Creditors` | full |
| current_assets | 15986782 | GBP | 2023-12-31 | 2025-08-15 | filed | yes | `d:CurrentAssets` | full |
| current_assets | 15986782 | GBP | 2023-12-31 | 2024-06-24 | filed | no | `d:CurrentAssets` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 13922086 | GBP | 2023-12-31 | 2024-06-24 | filed | no | `d:Debtors` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 13922086 | GBP | 2023-12-31 | 2025-08-15 | filed | yes | `d:Debtors` | full |
| equity | 17048873 | GBP | 2023-12-31 | 2025-08-15 | filed | yes | `d:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1670 | GBP | 2023-12-31 | 2025-08-15 | filed | yes | `d:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 17047203 | GBP | 2023-12-31 | 2024-06-24 | filed | no | `d:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 17047203 | GBP | 2023-12-31 | 2025-08-15 | filed | yes | `d:Equity` | full |
| equity | 17048873 | GBP | 2023-12-31 | 2024-06-24 | filed | no | `d:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1670 | GBP | 2023-12-31 | 2024-06-24 | filed | no | `d:Equity` | full |
| fixed_assets | 3104299 | GBP | 2023-12-31 | 2025-08-15 | filed | yes | `d:FixedAssets` | full |
| fixed_assets | 3104299 | GBP | 2023-12-31 | 2024-06-24 | filed | no | `d:FixedAssets` | full |
| gross_profit | 8979735 | GBP | 2023-12-31 | 2025-08-15 | filed | yes | `d:GrossProfitLoss` | full |
| gross_profit | 8979735 | GBP | 2023-12-31 | 2024-06-24 | filed | no | `d:GrossProfitLoss` | full |
| net_assets | 17048873 | GBP | 2023-12-31 | 2024-06-24 | filed | no | `d:NetAssetsLiabilities` | full |
| net_assets | 17048873 | GBP | 2023-12-31 | 2025-08-15 | filed | yes | `d:NetAssetsLiabilities` | full |
| net_current_assets | 14082324 | GBP | 2023-12-31 | 2025-08-15 | filed | yes | `d:NetCurrentAssetsLiabilities` | full |
| net_current_assets | 14082324 | GBP | 2023-12-31 | 2024-06-24 | filed | no | `d:NetCurrentAssetsLiabilities` | full |
| operating_profit | 5908141 | GBP | 2023-12-31 | 2025-08-15 | filed | yes | `d:OperatingProfitLoss` | full |
| operating_profit | 5908141 | GBP | 2023-12-31 | 2024-06-24 | filed | no | `d:OperatingProfitLoss` | full |
| profit_before_tax | 5897151 | GBP | 2023-12-31 | 2024-06-24 | filed | no | `d:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_before_tax | 5897151 | GBP | 2023-12-31 | 2025-08-15 | filed | yes | `d:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 4513256 | GBP | 2023-12-31 | 2024-06-24 | filed | no | `d:ProfitLoss` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 4513256 | GBP | 2023-12-31 | 2025-08-15 | filed | yes | `d:ProfitLoss` | full |
| revenue | 9148459 | GBP | 2023-12-31 | 2024-06-24 | filed | no | `d:TurnoverRevenue` | full |
| revenue | 9148459 | GBP | 2023-12-31 | 2025-08-15 | filed | yes | `d:TurnoverRevenue` | full |
| staff_costs | 2106773 | GBP | 2023-12-31 | 2025-08-15 | filed | yes | `d:StaffCostsEmployeeBenefitsExpense` | full |
| staff_costs | 2106773 | GBP | 2023-12-31 | 2024-06-24 | filed | no | `d:StaffCostsEmployeeBenefitsExpense` | full |
| tax_charge | 1383895 | GBP | 2023-12-31 | 2024-06-24 | filed | no | `d:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| tax_charge | 1383895 | GBP | 2023-12-31 | 2025-08-15 | filed | yes | `d:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| total_assets_less_current_liabilities | 17186623 | GBP | 2023-12-31 | 2025-08-15 | filed | yes | `d:TotalAssetsLessCurrentLiabilities` | full |
| total_assets_less_current_liabilities | 17186623 | GBP | 2023-12-31 | 2024-06-24 | filed | no | `d:TotalAssetsLessCurrentLiabilities` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 12533947 | GBP | 2023-01-01 | 2025-08-15 | filed | yes | `d:Equity` | full |
| average_employees | 59 | xbrli:pure | 2022-12-31 | 2024-06-24 | filed | yes | `d:AverageNumberEmployeesDuringPeriod` | full |
| cash | 3362327 | GBP | 2022-12-31 | 2024-06-24 | filed | yes | `d:CashBankOnHand` | full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2615320 | GBP | 2022-12-31 | 2024-06-24 | filed | yes | `d:Creditors` | full |
| current_assets | 12378906 | GBP | 2022-12-31 | 2024-06-24 | filed | yes | `d:CurrentAssets` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 9016579 | GBP | 2022-12-31 | 2024-06-24 | filed | yes | `d:Debtors` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1670 | GBP | 2022-12-31 | 2024-06-24 | filed | yes | `d:Equity` | full |
| equity | 12535617 | GBP | 2022-12-31 | 2024-06-24 | filed | yes | `d:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 12533947 | GBP | 2022-12-31 | 2024-06-24 | filed | yes | `d:Equity` | full |
| fixed_assets | 2962943 | GBP | 2022-12-31 | 2024-06-24 | filed | yes | `d:FixedAssets` | full |
| gross_profit | 7343308 | GBP | 2022-12-31 | 2024-06-24 | filed | yes | `d:GrossProfitLoss` | full |
| net_assets | 12535617 | GBP | 2022-12-31 | 2024-06-24 | filed | yes | `d:NetAssetsLiabilities` | full |
| net_current_assets | 9763586 | GBP | 2022-12-31 | 2024-06-24 | filed | yes | `d:NetCurrentAssetsLiabilities` | full |
| operating_profit | 4031272 | GBP | 2022-12-31 | 2024-06-24 | filed | yes | `d:OperatingProfitLoss` | full |
| profit_before_tax | 4016128 | GBP | 2022-12-31 | 2024-06-24 | filed | yes | `d:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3588465 | GBP | 2022-12-31 | 2024-06-24 | filed | yes | `d:ProfitLoss` | full |
| revenue | 7751212 | GBP | 2022-12-31 | 2024-06-24 | filed | yes | `d:TurnoverRevenue` | full |
| staff_costs | 2331032 | GBP | 2022-12-31 | 2024-06-24 | filed | yes | `d:StaffCostsEmployeeBenefitsExpense` | full |
| tax_charge | 427663 | GBP | 2022-12-31 | 2024-06-24 | filed | yes | `d:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| total_assets_less_current_liabilities | 12726529 | GBP | 2022-12-31 | 2024-06-24 | filed | yes | `d:TotalAssetsLessCurrentLiabilities` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 8945482 | GBP | 2022-01-01 | 2024-06-24 | filed | yes | `d:Equity` | full |

_No coverage facts for the latest run._

- event restatement @ 2026-05-22: `{"superseded_document_id": "gb:04978908:doc:VAS5S691w58oh-lwrPSgiEowiDQR3BPKfOwmOH3Udsg", "restatements": [{"concept": "average_employees", "period_end": "2024-12-31", "old_value": "0.0000", "new_valu`

## DEPT PERSONALISED CONTENT LIMITED (`gb:05412266`)

- registration: `05412266` (GB), status active, incorporated 2005-04-04
- classification: ['62020'] (sic_2007)
- records: 10 officers, 2 beneficial owners, 0 ownership statements, 7 security interests, 93 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 171 | xbrli:pure | 2025-12-31 | 2026-09-24 | filed | yes | `e:AverageNumberEmployeesDuringPeriod` | full |
| cash | 584507 | GBP | 2025-12-31 | 2026-09-24 | filed | yes | `e:CashBankOnHand` | full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 10345769 | GBP | 2025-12-31 | 2026-09-24 | filed | yes | `e:Creditors` | full |
| current_assets | 18002419 | GBP | 2025-12-31 | 2026-09-24 | filed | yes | `e:CurrentAssets` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 17417912 | GBP | 2025-12-31 | 2026-09-24 | filed | yes | `e:Debtors` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 8345637 | GBP | 2025-12-31 | 2026-09-24 | filed | yes | `e:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-12-31 | 2026-09-24 | filed | yes | `e:Equity` | full |
| equity | 8345737 | GBP | 2025-12-31 | 2026-09-24 | filed | yes | `e:Equity` | full |
| fixed_assets | 860174 | GBP | 2025-12-31 | 2026-09-24 | filed | yes | `e:FixedAssets` | full |
| gross_profit | 13295267 | GBP | 2025-12-31 | 2026-09-24 | filed | yes | `e:GrossProfitLoss` | full |
| net_assets | 8345737 | GBP | 2025-12-31 | 2026-09-24 | filed | yes | `e:NetAssetsLiabilities` | full |
| net_current_assets | 7656650 | GBP | 2025-12-31 | 2026-09-24 | filed | yes | `e:NetCurrentAssetsLiabilities` | full |
| operating_profit | 4989824 | GBP | 2025-12-31 | 2026-09-24 | filed | yes | `e:OperatingProfitLoss` | full |
| profit_before_tax | 5137814 | GBP | 2025-12-31 | 2026-09-24 | filed | yes | `e:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 4963333 | GBP | 2025-12-31 | 2026-09-24 | filed | yes | `e:ProfitLoss` | full |
| revenue | 51305779 | GBP | 2025-12-31 | 2026-09-24 | filed | yes | `e:TurnoverRevenue` | full |
| staff_costs | 8884533 | GBP | 2025-12-31 | 2026-09-24 | filed | yes | `e:StaffCostsEmployeeBenefitsExpense` | full |
| tax_charge | 174481 | GBP | 2025-12-31 | 2026-09-24 | filed | yes | `e:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| total_assets_less_current_liabilities | 8516824 | GBP | 2025-12-31 | 2026-09-24 | filed | yes | `e:TotalAssetsLessCurrentLiabilities` | full |
| average_employees | 185 | xbrli:pure | 2024-12-31 | 2026-09-24 | filed | yes | `e:AverageNumberEmployeesDuringPeriod` | full |
| average_employees | 185 | xbrli:pure | 2024-12-31 | 2025-09-18 | filed | no | `e:AverageNumberEmployeesDuringPeriod` | full |
| cash | 4301977 | GBP | 2024-12-31 | 2026-09-24 | filed | yes | `e:CashBankOnHand` | full |
| cash | 4301977 | GBP | 2024-12-31 | 2025-09-18 | filed | no | `e:CashBankOnHand` | full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 7027978 | GBP | 2024-12-31 | 2026-09-24 | filed | yes | `e:Creditors` | full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 7027978 | GBP | 2024-12-31 | 2025-09-18 | filed | no | `e:Creditors` | full |
| current_assets | 9450503 | GBP | 2024-12-31 | 2026-09-24 | filed | yes | `e:CurrentAssets` | full |
| current_assets | 9450503 | GBP | 2024-12-31 | 2025-09-18 | filed | no | `e:CurrentAssets` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 5148526 | GBP | 2024-12-31 | 2025-09-18 | filed | no | `e:Debtors` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 5148526 | GBP | 2024-12-31 | 2026-09-24 | filed | yes | `e:Debtors` | full |
| equity | 3382404 | GBP | 2024-12-31 | 2026-09-24 | filed | yes | `e:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3382304 | GBP | 2024-12-31 | 2025-09-18 | filed | no | `e:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3382304 | GBP | 2024-12-31 | 2026-09-24 | filed | yes | `e:Equity` | full |
| equity | 3382404 | GBP | 2024-12-31 | 2025-09-18 | filed | no | `e:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-12-31 | 2026-09-24 | filed | yes | `e:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-12-31 | 2025-09-18 | filed | no | `e:Equity` | full |
| fixed_assets | 1165009 | GBP | 2024-12-31 | 2026-09-24 | filed | yes | `e:FixedAssets` | full |
| fixed_assets | 1165009 | GBP | 2024-12-31 | 2025-09-18 | filed | no | `e:FixedAssets` | full |
| gross_profit | 13955834 | GBP | 2024-12-31 | 2026-09-24 | filed | yes | `e:GrossProfitLoss` | full |
| gross_profit | 13955834 | GBP | 2024-12-31 | 2025-09-18 | filed | no | `e:GrossProfitLoss` | full |
| net_assets | 3382404 | GBP | 2024-12-31 | 2025-09-18 | filed | no | `e:NetAssetsLiabilities` | full |
| net_assets | 3382404 | GBP | 2024-12-31 | 2026-09-24 | filed | yes | `e:NetAssetsLiabilities` | full |
| net_current_assets | 2422525 | GBP | 2024-12-31 | 2025-09-18 | filed | no | `e:NetCurrentAssetsLiabilities` | full |
| net_current_assets | 2422525 | GBP | 2024-12-31 | 2026-09-24 | filed | yes | `e:NetCurrentAssetsLiabilities` | full |
| operating_profit | 5354459 | GBP | 2024-12-31 | 2026-09-24 | filed | yes | `e:OperatingProfitLoss` | full |
| operating_profit | 5354459 | GBP | 2024-12-31 | 2025-09-18 | filed | no | `e:OperatingProfitLoss` | full |
| profit_before_tax | 5172898 | GBP | 2024-12-31 | 2025-09-18 | filed | no | `e:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_before_tax | 5172898 | GBP | 2024-12-31 | 2026-09-24 | filed | yes | `e:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 4882248 | GBP | 2024-12-31 | 2026-09-24 | filed | yes | `e:ProfitLoss` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 4882248 | GBP | 2024-12-31 | 2025-09-18 | filed | no | `e:ProfitLoss` | full |
| revenue | 43982147 | GBP | 2024-12-31 | 2025-09-18 | filed | no | `e:TurnoverRevenue` | full |
| revenue | 43982147 | GBP | 2024-12-31 | 2026-09-24 | filed | yes | `e:TurnoverRevenue` | full |
| staff_costs | 8969561 | GBP | 2024-12-31 | 2025-09-18 | filed | no | `e:StaffCostsEmployeeBenefitsExpense` | full |
| staff_costs | 8969561 | GBP | 2024-12-31 | 2026-09-24 | filed | yes | `e:StaffCostsEmployeeBenefitsExpense` | full |
| tax_charge | 290650 | GBP | 2024-12-31 | 2025-09-18 | filed | no | `e:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| tax_charge | 290650 | GBP | 2024-12-31 | 2026-09-24 | filed | yes | `e:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| total_assets_less_current_liabilities | 3587534 | GBP | 2024-12-31 | 2026-09-24 | filed | yes | `e:TotalAssetsLessCurrentLiabilities` | full |
| total_assets_less_current_liabilities | 3587534 | GBP | 2024-12-31 | 2025-09-18 | filed | no | `e:TotalAssetsLessCurrentLiabilities` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3920840 | GBP | 2024-01-01 | 2026-09-24 | filed | yes | `e:Equity` | full |
| average_employees | 164 | xbrli:pure | 2023-12-31 | 2024-09-27 | filed | no | `e:AverageNumberEmployeesDuringPeriod` | full |
| average_employees | 164 | xbrli:pure | 2023-12-31 | 2025-09-18 | filed | yes | `e:AverageNumberEmployeesDuringPeriod` | full |
| cash | 4456395 | GBP | 2023-12-31 | 2025-09-18 | filed | yes | `e:CashBankOnHand` | full |
| cash | 4456395 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `e:CashBankOnHand` | full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 9588585 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `e:Creditors` | full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 9588585 | GBP | 2023-12-31 | 2025-09-18 | filed | yes | `e:Creditors` | full |
| current_assets | 12389097 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `e:CurrentAssets` | full |
| current_assets | 12389097 | GBP | 2023-12-31 | 2025-09-18 | filed | yes | `e:CurrentAssets` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 7932702 | GBP | 2023-12-31 | 2025-09-18 | filed | yes | `e:Debtors` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 7932702 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `e:Debtors` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3920840 | GBP | 2023-12-31 | 2025-09-18 | filed | yes | `e:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-12-31 | 2025-09-18 | filed | yes | `e:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3920840 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `e:Equity` | full |
| equity | 3920940 | GBP | 2023-12-31 | 2025-09-18 | filed | yes | `e:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `e:Equity` | full |
| equity | 3920940 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `e:Equity` | full |
| fixed_assets | 1379282 | GBP | 2023-12-31 | 2025-09-18 | filed | yes | `e:FixedAssets` | full |
| fixed_assets | 1379282 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `e:FixedAssets` | full |
| gross_profit | 12216185 | GBP | 2023-12-31 | 2025-09-18 | filed | yes | `e:GrossProfitLoss` | full |
| gross_profit | 12216185 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `e:GrossProfitLoss` | full |
| net_assets | 3920940 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `e:NetAssetsLiabilities` | full |
| net_assets | 3920940 | GBP | 2023-12-31 | 2025-09-18 | filed | yes | `e:NetAssetsLiabilities` | full |
| net_current_assets | 2800512 | GBP | 2023-12-31 | 2025-09-18 | filed | yes | `e:NetCurrentAssetsLiabilities` | full |
| net_current_assets | 2800512 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `e:NetCurrentAssetsLiabilities` | full |
| operating_profit | 5024309 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `e:OperatingProfitLoss` | full |
| operating_profit | 5024309 | GBP | 2023-12-31 | 2025-09-18 | filed | yes | `e:OperatingProfitLoss` | full |
| profit_before_tax | 5223846 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `e:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_before_tax | 5223846 | GBP | 2023-12-31 | 2025-09-18 | filed | yes | `e:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period | 5111512 | GBP | 2023-12-31 | 2024-09-27 | filed | yes | `e:ProfitLoss` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 5111512 | GBP | 2023-12-31 | 2025-09-18 | filed | yes | `e:ProfitLoss` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 5111512 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `e:ProfitLoss` | full |
| revenue | 39329922 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `e:TurnoverRevenue` | full |
| revenue | 39329922 | GBP | 2023-12-31 | 2025-09-18 | filed | yes | `e:TurnoverRevenue` | full |
| staff_costs | 7968244 | GBP | 2023-12-31 | 2025-09-18 | filed | yes | `e:StaffCostsEmployeeBenefitsExpense` | full |
| staff_costs | 7968244 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `e:StaffCostsEmployeeBenefitsExpense` | full |
| tax_charge | 112334 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `e:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| tax_charge | 112334 | GBP | 2023-12-31 | 2025-09-18 | filed | yes | `e:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| total_assets_less_current_liabilities | 4179794 | GBP | 2023-12-31 | 2025-09-18 | filed | yes | `e:TotalAssetsLessCurrentLiabilities` | full |
| total_assets_less_current_liabilities | 4179794 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `e:TotalAssetsLessCurrentLiabilities` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 5128133 | GBP | 2023-01-01 | 2025-09-18 | filed | yes | `e:Equity` | full |
| average_employees | 132 | xbrli:pure | 2022-12-31 | 2024-09-27 | filed | yes | `e:AverageNumberEmployeesDuringPeriod` | full |
| cash | 2351077 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `e:CashBankOnHand` | full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 7846023 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `e:Creditors` | full |
| current_assets | 12086860 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `e:CurrentAssets` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 9735783 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `e:Debtors` | full |
| equity | 5128233 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `e:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `e:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 5128133 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `e:Equity` | full |
| fixed_assets | 1152119 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `e:FixedAssets` | full |
| gross_profit | 16266182 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `e:GrossProfitLoss` | full |
| net_assets | 5128233 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `e:NetAssetsLiabilities` | full |
| net_current_assets | 4240837 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `e:NetCurrentAssetsLiabilities` | full |
| operating_profit | 2637509 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `e:OperatingProfitLoss` | full |
| profit_before_tax | 2576753 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `e:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period | 1868629 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `e:ProfitLoss` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1868629 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `e:ProfitLoss` | full |
| revenue | 19628189 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `e:TurnoverRevenue` | full |
| staff_costs | 4280018 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `e:StaffCostsEmployeeBenefitsExpense` | full |
| tax_charge | 708124 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `e:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| total_assets_less_current_liabilities | 5392956 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `e:TotalAssetsLessCurrentLiabilities` | full |
| equity | 3259604 | GBP | 2022-05-01 | 2024-09-27 | filed | yes | `e:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2022-05-01 | 2024-09-27 | filed | yes | `e:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3259504 | GBP | 2022-05-01 | 2024-09-27 | filed | yes | `e:Equity` | full |

_No coverage facts for the latest run._

## CEGEDIM E-BUSINESS LTD (`gb:05845790`)

- registration: `05845790` (GB), status active, incorporated 2006-06-14
- classification: ['62012', '62020', '62090'] (sic_2007)
- records: 15 officers, 1 beneficial owners, 1 ownership statements, 2 security interests, 104 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## PPV CONSULTANCY LTD (`gb:06368949`)

- registration: `06368949` (GB), status active, incorporated 2007-09-12
- classification: ['62020'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 60 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-09-30 | 2026-06-29 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 49766 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 49766 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 0 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 49912 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 428 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 50012 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 49584 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 50012 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-09-30 | 2025-06-24 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-09-30 | 2026-06-29 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 83859 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| cash | 83859 | GBP | 2024-09-30 | 2025-06-24 | filed | no | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 85310 | GBP | 2024-09-30 | 2025-06-24 | filed | no | `frs-core:CurrentAssets` | total-exemption-full |
| current_assets | 85310 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 1451 | GBP | 2024-09-30 | 2025-06-24 | filed | no | `frs-core:Debtors` | total-exemption-full |
| debtors | 1451 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-09-30 | 2025-06-24 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 85535 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 85535 | GBP | 2024-09-30 | 2025-06-24 | filed | no | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 428 | GBP | 2024-09-30 | 2025-06-24 | filed | no | `frs-core:FixedAssets` | total-exemption-full |
| fixed_assets | 428 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 85635 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 85635 | GBP | 2024-09-30 | 2025-06-24 | filed | no | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 85207 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 85207 | GBP | 2024-09-30 | 2025-06-24 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 85635 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 85635 | GBP | 2024-09-30 | 2025-06-24 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-09-30 | 2024-06-28 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-09-30 | 2025-06-24 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 108915 | GBP | 2023-09-30 | 2025-06-24 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| cash | 108915 | GBP | 2023-09-30 | 2024-06-28 | filed | no | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 111929 | GBP | 2023-09-30 | 2025-06-24 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| current_assets | 111929 | GBP | 2023-09-30 | 2024-06-28 | filed | no | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 3014 | GBP | 2023-09-30 | 2024-06-28 | filed | no | `frs-core:Debtors` | total-exemption-full |
| debtors | 3014 | GBP | 2023-09-30 | 2025-06-24 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-09-30 | 2024-06-28 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-09-30 | 2025-06-24 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 105721 | GBP | 2023-09-30 | 2025-06-24 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 105721 | GBP | 2023-09-30 | 2024-06-28 | filed | no | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 428 | GBP | 2023-09-30 | 2024-06-28 | filed | no | `frs-core:FixedAssets` | total-exemption-full |
| fixed_assets | 428 | GBP | 2023-09-30 | 2025-06-24 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 105821 | GBP | 2023-09-30 | 2025-06-24 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 105821 | GBP | 2023-09-30 | 2024-06-28 | filed | no | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 105393 | GBP | 2023-09-30 | 2024-06-28 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 105393 | GBP | 2023-09-30 | 2025-06-24 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 105821 | GBP | 2023-09-30 | 2025-06-24 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 105821 | GBP | 2023-09-30 | 2024-06-28 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2022-09-30 | 2024-06-28 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 99774 | GBP | 2022-09-30 | 2024-06-28 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 101938 | GBP | 2022-09-30 | 2024-06-28 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 2164 | GBP | 2022-09-30 | 2024-06-28 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2022-09-30 | 2024-06-28 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 95890 | GBP | 2022-09-30 | 2024-06-28 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 571 | GBP | 2022-09-30 | 2024-06-28 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 95990 | GBP | 2022-09-30 | 2024-06-28 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 95419 | GBP | 2022-09-30 | 2024-06-28 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 95990 | GBP | 2022-09-30 | 2024-06-28 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._
