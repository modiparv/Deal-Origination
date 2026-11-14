# Ingest spot-check

- database: `data/engine.db`
- latest run: `20261114T084202Z-3c0922af`
- companies in store: 51400; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## BALLICOM LIMITED (`gb:02799428`)

- registration: `02799428` (GB), status active, incorporated 1993-03-15
- classification: ['46510', '62020', '62090'] (sic_2007)
- records: 12 officers, 5 beneficial owners, 0 ownership statements, 6 security interests, 128 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 25 | xbrli:pure | 2025-08-31 | 2025-12-12 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | medium |
| cash | 5660380 | GBP | 2025-08-31 | 2025-12-12 | filed | yes | `ns5:CashBankOnHand` | medium |
| current_assets | 10905541 | GBP | 2025-08-31 | 2025-12-12 | filed | yes | `ns5:CurrentAssets` | medium |
| debtors | 4834281 | GBP | 2025-08-31 | 2025-12-12 | filed | yes | `ns5:Debtors` | medium |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 4834281 | GBP | 2025-08-31 | 2025-12-12 | filed | yes | `ns5:Debtors` | medium |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 6471803 | GBP | 2025-08-31 | 2025-12-12 | filed | yes | `ns5:Equity` | medium |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10100 | GBP | 2025-08-31 | 2025-12-12 | filed | yes | `ns5:Equity` | medium |
| equity | 7411372 | GBP | 2025-08-31 | 2025-12-12 | filed | yes | `ns5:Equity` | medium |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 929469 | GBP | 2025-08-31 | 2025-12-12 | filed | yes | `ns5:Equity` | medium |
| fixed_assets | 1654802 | GBP | 2025-08-31 | 2025-12-12 | filed | yes | `ns5:FixedAssets` | medium |
| gross_profit | 3652709 | GBP | 2025-08-31 | 2025-12-12 | filed | yes | `ns5:GrossProfitLoss` | medium |
| net_assets | 7411372 | GBP | 2025-08-31 | 2025-12-12 | filed | yes | `ns5:NetAssetsLiabilities` | medium |
| net_current_assets | 5802421 | GBP | 2025-08-31 | 2025-12-12 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | medium |
| operating_profit | 1722540 | GBP | 2025-08-31 | 2025-12-12 | filed | yes | `ns5:OperatingProfitLoss` | medium |
| profit_before_tax | 1714104 | GBP | 2025-08-31 | 2025-12-12 | filed | yes | `ns5:ProfitLossOnOrdinaryActivitiesBeforeTax` | medium |
| profit_for_period | 1250612 | GBP | 2025-08-31 | 2025-12-12 | filed | yes | `ns5:ProfitLoss` | medium |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1250612 | GBP | 2025-08-31 | 2025-12-12 | filed | yes | `ns5:ProfitLoss` | medium |
| revenue | 39529976 | GBP | 2025-08-31 | 2025-12-12 | filed | yes | `ns5:TurnoverRevenue` | medium |
| staff_costs | 915314 | GBP | 2025-08-31 | 2025-12-12 | filed | yes | `ns5:StaffCostsEmployeeBenefitsExpense` | medium |
| tax_charge | 463492 | GBP | 2025-08-31 | 2025-12-12 | filed | yes | `ns5:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | medium |
| total_assets_less_current_liabilities | 7457223 | GBP | 2025-08-31 | 2025-12-12 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | medium |
| average_employees | 26 | xbrli:pure | 2024-08-31 | 2025-01-23 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | medium |
| average_employees | 26 | xbrli:pure | 2024-08-31 | 2025-12-12 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | medium |
| cash | 5665157 | GBP | 2024-08-31 | 2025-12-12 | filed | yes | `ns5:CashBankOnHand` | medium |
| cash | 5665157 | GBP | 2024-08-31 | 2025-01-23 | filed | no | `ns5:CashBankOnHand` | medium |
| current_assets | 10868949 | GBP | 2024-08-31 | 2025-01-23 | filed | no | `ns5:CurrentAssets` | medium |
| current_assets | 10868949 | GBP | 2024-08-31 | 2025-12-12 | filed | yes | `ns5:CurrentAssets` | medium |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 4098281 | GBP | 2024-08-31 | 2025-01-23 | filed | no | `ns5:Debtors` | medium |
| debtors | 4098281 | GBP | 2024-08-31 | 2025-01-23 | filed | no | `ns5:Debtors` | medium |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 4098281 | GBP | 2024-08-31 | 2025-12-12 | filed | yes | `ns5:Debtors` | medium |
| debtors | 4098281 | GBP | 2024-08-31 | 2025-12-12 | filed | yes | `ns5:Debtors` | medium |
| equity | 6160760 | GBP | 2024-08-31 | 2025-12-12 | filed | yes | `ns5:Equity` | medium |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10100 | GBP | 2024-08-31 | 2025-01-23 | filed | no | `ns5:Equity` | medium |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 929469 | GBP | 2024-08-31 | 2025-12-12 | filed | yes | `ns5:Equity` | medium |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 5221191 | GBP | 2024-08-31 | 2025-12-12 | filed | yes | `ns5:Equity` | medium |
| equity | 6160760 | GBP | 2024-08-31 | 2025-01-23 | filed | no | `ns5:Equity` | medium |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 929469 | GBP | 2024-08-31 | 2025-01-23 | filed | no | `ns5:Equity` | medium |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10100 | GBP | 2024-08-31 | 2025-12-12 | filed | yes | `ns5:Equity` | medium |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 5221191 | GBP | 2024-08-31 | 2025-01-23 | filed | no | `ns5:Equity` | medium |
| fixed_assets | 1731403 | GBP | 2024-08-31 | 2025-01-23 | filed | no | `ns5:FixedAssets` | medium |
| fixed_assets | 1731403 | GBP | 2024-08-31 | 2025-12-12 | filed | yes | `ns5:FixedAssets` | medium |
| gross_profit | 3519040 | GBP | 2024-08-31 | 2025-12-12 | filed | yes | `ns5:GrossProfitLoss` | medium |
| gross_profit | 3519040 | GBP | 2024-08-31 | 2025-01-23 | filed | no | `ns5:GrossProfitLoss` | medium |
| net_assets | 6160760 | GBP | 2024-08-31 | 2025-12-12 | filed | yes | `ns5:NetAssetsLiabilities` | medium |
| net_assets | 6160760 | GBP | 2024-08-31 | 2025-01-23 | filed | no | `ns5:NetAssetsLiabilities` | medium |
| net_current_assets | 4501081 | GBP | 2024-08-31 | 2025-12-12 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | medium |
| net_current_assets | 4501081 | GBP | 2024-08-31 | 2025-01-23 | filed | no | `ns5:NetCurrentAssetsLiabilities` | medium |
| operating_profit | 1873063 | GBP | 2024-08-31 | 2025-01-23 | filed | no | `ns5:OperatingProfitLoss` | medium |
| operating_profit | 1873063 | GBP | 2024-08-31 | 2025-12-12 | filed | yes | `ns5:OperatingProfitLoss` | medium |
| profit_before_tax | 1854984 | GBP | 2024-08-31 | 2025-01-23 | filed | no | `ns5:ProfitLossOnOrdinaryActivitiesBeforeTax` | medium |
| profit_before_tax | 1854984 | GBP | 2024-08-31 | 2025-12-12 | filed | yes | `ns5:ProfitLossOnOrdinaryActivitiesBeforeTax` | medium |
| profit_for_period | 1408555 | GBP | 2024-08-31 | 2025-12-12 | filed | yes | `ns5:ProfitLoss` | medium |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1408555 | GBP | 2024-08-31 | 2025-01-23 | filed | yes | `ns5:ProfitLoss` | medium |
| profit_for_period | 1408555 | GBP | 2024-08-31 | 2025-01-23 | filed | no | `ns5:ProfitLoss` | medium |
| revenue | 38824074 | GBP | 2024-08-31 | 2025-01-23 | filed | no | `ns5:TurnoverRevenue` | medium |
| revenue | 38824074 | GBP | 2024-08-31 | 2025-12-12 | filed | yes | `ns5:TurnoverRevenue` | medium |
| staff_costs | 870546 | GBP | 2024-08-31 | 2025-01-23 | filed | no | `ns5:StaffCostsEmployeeBenefitsExpense` | medium |
| staff_costs | 870546 | GBP | 2024-08-31 | 2025-12-12 | filed | yes | `ns5:StaffCostsEmployeeBenefitsExpense` | medium |
| tax_charge | 446429 | GBP | 2024-08-31 | 2025-01-23 | filed | no | `ns5:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | medium |
| tax_charge | 446429 | GBP | 2024-08-31 | 2025-12-12 | filed | yes | `ns5:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | medium |
| total_assets_less_current_liabilities | 6232484 | GBP | 2024-08-31 | 2025-12-12 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | medium |
| total_assets_less_current_liabilities | 6232484 | GBP | 2024-08-31 | 2025-01-23 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | medium |
| average_employees | 21 | xbrli:pure | 2023-08-31 | 2023-12-18 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | full |
| average_employees | 21 | xbrli:pure | 2023-08-31 | 2025-01-23 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | medium |
| cash | 3802924 | GBP | 2023-08-31 | 2023-12-18 | filed | no | `ns5:CashBankOnHand` | full |
| cash | 3802924 | GBP | 2023-08-31 | 2025-01-23 | filed | yes | `ns5:CashBankOnHand` | medium |
| current_assets | 9300463 | GBP | 2023-08-31 | 2025-01-23 | filed | yes | `ns5:CurrentAssets` | medium |
| current_assets | 9300463 | GBP | 2023-08-31 | 2023-12-18 | filed | no | `ns5:CurrentAssets` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 4937635 | GBP | 2023-08-31 | 2023-12-18 | filed | no | `ns5:Debtors` | full |
| debtors | 4937635 | GBP | 2023-08-31 | 2025-01-23 | filed | yes | `ns5:Debtors` | medium |
| debtors | 4937635 | GBP | 2023-08-31 | 2023-12-18 | filed | no | `ns5:Debtors` | full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 4937635 | GBP | 2023-08-31 | 2025-01-23 | filed | yes | `ns5:Debtors` | medium |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10100 | GBP | 2023-08-31 | 2023-12-18 | filed | no | `ns5:Equity` | full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 929469 | GBP | 2023-08-31 | 2025-01-23 | filed | no | `ns5:Equity` | medium |
| equity | 5202205 | GBP | 2023-08-31 | 2025-12-12 | filed | yes | `ns5:Equity` | medium |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 4262636 | GBP | 2023-08-31 | 2023-12-18 | filed | no | `ns5:Equity` | full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 929469 | GBP | 2023-08-31 | 2025-12-12 | filed | yes | `ns5:Equity` | medium |
| equity | 5202205 | GBP | 2023-08-31 | 2025-01-23 | filed | no | `ns5:Equity` | medium |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10100 | GBP | 2023-08-31 | 2025-01-23 | filed | no | `ns5:Equity` | medium |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10100 | GBP | 2023-08-31 | 2025-12-12 | filed | yes | `ns5:Equity` | medium |
| equity | 5202205 | GBP | 2023-08-31 | 2023-12-18 | filed | no | `ns5:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 4262636 | GBP | 2023-08-31 | 2025-12-12 | filed | yes | `ns5:Equity` | medium |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 4262636 | GBP | 2023-08-31 | 2025-01-23 | filed | no | `ns5:Equity` | medium |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 929469 | GBP | 2023-08-31 | 2023-12-18 | filed | no | `ns5:Equity` | full |
| fixed_assets | 1690425 | GBP | 2023-08-31 | 2025-01-23 | filed | yes | `ns5:FixedAssets` | medium |
| fixed_assets | 1690425 | GBP | 2023-08-31 | 2023-12-18 | filed | no | `ns5:FixedAssets` | full |
| gross_profit | 3705340 | GBP | 2023-08-31 | 2025-01-23 | filed | yes | `ns5:GrossProfitLoss` | medium |
| gross_profit | 3705340 | GBP | 2023-08-31 | 2023-12-18 | filed | no | `ns5:GrossProfitLoss` | full |
| net_assets | 5202205 | GBP | 2023-08-31 | 2025-01-23 | filed | yes | `ns5:NetAssetsLiabilities` | medium |
| net_assets | 5202205 | GBP | 2023-08-31 | 2023-12-18 | filed | no | `ns5:NetAssetsLiabilities` | full |
| net_current_assets | 3634128 | GBP | 2023-08-31 | 2025-01-23 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | medium |
| net_current_assets | 3634128 | GBP | 2023-08-31 | 2023-12-18 | filed | no | `ns5:NetCurrentAssetsLiabilities` | full |
| operating_profit | 2088981 | GBP | 2023-08-31 | 2025-01-23 | filed | yes | `ns5:OperatingProfitLoss` | medium |
| operating_profit | 2088981 | GBP | 2023-08-31 | 2023-12-18 | filed | no | `ns5:OperatingProfitLoss` | full |
| profit_before_tax | 2079503 | GBP | 2023-08-31 | 2023-12-18 | filed | no | `ns5:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_before_tax | 2079503 | GBP | 2023-08-31 | 2025-01-23 | filed | yes | `ns5:ProfitLossOnOrdinaryActivitiesBeforeTax` | medium |
| profit_for_period | 1640285 | GBP | 2023-08-31 | 2025-01-23 | filed | yes | `ns5:ProfitLoss` | medium |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1640285 | GBP | 2023-08-31 | 2023-12-18 | filed | yes | `ns5:ProfitLoss` | full |
| profit_for_period | 1640285 | GBP | 2023-08-31 | 2023-12-18 | filed | no | `ns5:ProfitLoss` | full |
| revenue | 40315133 | GBP | 2023-08-31 | 2023-12-18 | filed | no | `ns5:TurnoverRevenue` | full |
| revenue | 40315133 | GBP | 2023-08-31 | 2025-01-23 | filed | yes | `ns5:TurnoverRevenue` | medium |
| staff_costs | 792838 | GBP | 2023-08-31 | 2025-01-23 | filed | yes | `ns5:StaffCostsEmployeeBenefitsExpense` | medium |
| staff_costs | 792838 | GBP | 2023-08-31 | 2023-12-18 | filed | no | `ns5:StaffCostsEmployeeBenefitsExpense` | full |
| tax_charge | 439218 | GBP | 2023-08-31 | 2023-12-18 | filed | no | `ns5:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| tax_charge | 439218 | GBP | 2023-08-31 | 2025-01-23 | filed | yes | `ns5:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | medium |
| total_assets_less_current_liabilities | 5324553 | GBP | 2023-08-31 | 2025-01-23 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | medium |
| total_assets_less_current_liabilities | 5324553 | GBP | 2023-08-31 | 2023-12-18 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | full |
| average_employees | 20 | xbrli:pure | 2022-08-31 | 2023-12-18 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | full |
| cash | 3168032 | GBP | 2022-08-31 | 2023-12-18 | filed | yes | `ns5:CashBankOnHand` | full |
| current_assets | 7472940 | GBP | 2022-08-31 | 2023-12-18 | filed | yes | `ns5:CurrentAssets` | full |
| debtors | 3794482 | GBP | 2022-08-31 | 2023-12-18 | filed | yes | `ns5:Debtors` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 3794482 | GBP | 2022-08-31 | 2023-12-18 | filed | yes | `ns5:Debtors` | full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 829469 | GBP | 2022-08-31 | 2023-12-18 | filed | no | `ns5:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3019351 | GBP | 2022-08-31 | 2023-12-18 | filed | no | `ns5:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3019351 | GBP | 2022-08-31 | 2025-01-23 | filed | yes | `ns5:Equity` | medium |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 829469 | GBP | 2022-08-31 | 2025-01-23 | filed | yes | `ns5:Equity` | medium |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10100 | GBP | 2022-08-31 | 2023-12-18 | filed | no | `ns5:Equity` | full |
| equity | 3858920 | GBP | 2022-08-31 | 2025-01-23 | filed | yes | `ns5:Equity` | medium |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10100 | GBP | 2022-08-31 | 2025-01-23 | filed | yes | `ns5:Equity` | medium |
| equity | 3858920 | GBP | 2022-08-31 | 2023-12-18 | filed | no | `ns5:Equity` | full |
| fixed_assets | 1403280 | GBP | 2022-08-31 | 2023-12-18 | filed | yes | `ns5:FixedAssets` | full |
| gross_profit | 2989396 | GBP | 2022-08-31 | 2023-12-18 | filed | yes | `ns5:GrossProfitLoss` | full |
| net_assets | 3858920 | GBP | 2022-08-31 | 2023-12-18 | filed | yes | `ns5:NetAssetsLiabilities` | full |
| net_current_assets | 2461188 | GBP | 2022-08-31 | 2023-12-18 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | full |
| operating_profit | 1451056 | GBP | 2022-08-31 | 2023-12-18 | filed | yes | `ns5:OperatingProfitLoss` | full |
| profit_before_tax | 1447730 | GBP | 2022-08-31 | 2023-12-18 | filed | yes | `ns5:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period | 1192866 | GBP | 2022-08-31 | 2023-12-18 | filed | yes | `ns5:ProfitLoss` | full |
| revenue | 35517154 | GBP | 2022-08-31 | 2023-12-18 | filed | yes | `ns5:TurnoverRevenue` | full |
| staff_costs | 882786 | GBP | 2022-08-31 | 2023-12-18 | filed | yes | `ns5:StaffCostsEmployeeBenefitsExpense` | full |
| tax_charge | 254864 | GBP | 2022-08-31 | 2023-12-18 | filed | yes | `ns5:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| total_assets_less_current_liabilities | 3864468 | GBP | 2022-08-31 | 2023-12-18 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | full |
| equity | 3037331 | GBP | 2021-08-31 | 2023-12-18 | filed | yes | `ns5:Equity` | full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 829469 | GBP | 2021-08-31 | 2023-12-18 | filed | yes | `ns5:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10100 | GBP | 2021-08-31 | 2023-12-18 | filed | yes | `ns5:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2197762 | GBP | 2021-08-31 | 2023-12-18 | filed | yes | `ns5:Equity` | full |

_No coverage facts for the latest run._

## SYSTEMS AND SOFTWARE LIMITED (`gb:03482434`)

- registration: `03482434` (GB), status active, incorporated 1997-12-17
- classification: ['62020'] (sic_2007)
- records: 7 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 72 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2024-12-31 | 2025-07-03 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 26170 | GBP | 2024-12-31 | 2025-07-03 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 65371 | GBP | 2024-12-31 | 2025-07-03 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 51461 | GBP | 2024-12-31 | 2025-07-03 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 25291 | GBP | 2024-12-31 | 2025-07-03 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | -13895 | GBP | 2024-12-31 | 2025-07-03 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 1000 | GBP | 2024-12-31 | 2025-07-03 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | -14895 | GBP | 2024-12-31 | 2025-07-03 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | -13895 | GBP | 2024-12-31 | 2025-07-03 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -13910 | GBP | 2024-12-31 | 2025-07-03 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## NETCONNEX BROADBAND LIMITED (`gb:04042392`)

- registration: `04042392` (GB), status active, incorporated 2000-07-24
- classification: ['62090'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 75 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-07-31 | 2026-04-22 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 174814 | GBP | 2025-07-31 | 2026-04-22 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 1770 | GBP | 2025-07-31 | 2026-04-22 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 48107 | GBP | 2025-07-31 | 2026-04-22 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 229959 | GBP | 2025-07-31 | 2026-04-22 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 55145 | GBP | 2025-07-31 | 2026-04-22 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 49 | GBP | 2025-07-31 | 2026-04-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 210536 | GBP | 2025-07-31 | 2026-04-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 51 | GBP | 2025-07-31 | 2026-04-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 210436 | GBP | 2025-07-31 | 2026-04-22 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 210536 | GBP | 2025-07-31 | 2026-04-22 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 181852 | GBP | 2025-07-31 | 2026-04-22 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 223306 | GBP | 2025-07-31 | 2026-04-22 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-07-31 | 2025-04-24 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-07-31 | 2026-04-22 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 218000 | GBP | 2024-07-31 | 2026-04-22 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 218000 | GBP | 2024-07-31 | 2025-04-24 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 12232 | GBP | 2024-07-31 | 2025-04-24 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 12232 | GBP | 2024-07-31 | 2026-04-22 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 78310 | GBP | 2024-07-31 | 2025-04-24 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 78310 | GBP | 2024-07-31 | 2026-04-22 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 290636 | GBP | 2024-07-31 | 2025-04-24 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 290636 | GBP | 2024-07-31 | 2026-04-22 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 72636 | GBP | 2024-07-31 | 2025-04-24 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 72636 | GBP | 2024-07-31 | 2026-04-22 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 237803 | GBP | 2024-07-31 | 2025-04-24 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 49 | GBP | 2024-07-31 | 2025-04-24 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 51 | GBP | 2024-07-31 | 2026-04-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 237903 | GBP | 2024-07-31 | 2026-04-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 237803 | GBP | 2024-07-31 | 2026-04-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 237903 | GBP | 2024-07-31 | 2025-04-24 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 49 | GBP | 2024-07-31 | 2026-04-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 51 | GBP | 2024-07-31 | 2025-04-24 | filed | no | `core:Equity` | total-exemption-full |
| net_assets | 237903 | GBP | 2024-07-31 | 2025-04-24 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 237903 | GBP | 2024-07-31 | 2026-04-22 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 212326 | GBP | 2024-07-31 | 2025-04-24 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 212326 | GBP | 2024-07-31 | 2026-04-22 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 266135 | GBP | 2024-07-31 | 2026-04-22 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 266135 | GBP | 2024-07-31 | 2025-04-24 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-07-31 | 2025-04-24 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-07-31 | 2024-04-26 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 197441 | GBP | 2023-07-31 | 2024-04-26 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 197441 | GBP | 2023-07-31 | 2025-04-24 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 22435 | GBP | 2023-07-31 | 2025-04-24 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 22435 | GBP | 2023-07-31 | 2024-04-26 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 70795 | GBP | 2023-07-31 | 2024-04-26 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 70795 | GBP | 2023-07-31 | 2025-04-24 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 282702 | GBP | 2023-07-31 | 2024-04-26 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 282702 | GBP | 2023-07-31 | 2025-04-24 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 85261 | GBP | 2023-07-31 | 2024-04-26 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 85261 | GBP | 2023-07-31 | 2025-04-24 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 49 | GBP | 2023-07-31 | 2025-04-24 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 241250 | GBP | 2023-07-31 | 2024-04-26 | filed | no | `core:Equity` | total-exemption-full |
| equity | 241350 | GBP | 2023-07-31 | 2024-04-26 | filed | no | `core:Equity` | total-exemption-full |
| equity | 241350 | GBP | 2023-07-31 | 2025-04-24 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 49 | GBP | 2023-07-31 | 2024-04-26 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 51 | GBP | 2023-07-31 | 2025-04-24 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 241250 | GBP | 2023-07-31 | 2025-04-24 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 51 | GBP | 2023-07-31 | 2024-04-26 | filed | no | `core:Equity` | total-exemption-full |
| net_assets | 241350 | GBP | 2023-07-31 | 2024-04-26 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 241350 | GBP | 2023-07-31 | 2025-04-24 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 211907 | GBP | 2023-07-31 | 2025-04-24 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 211907 | GBP | 2023-07-31 | 2024-04-26 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 278785 | GBP | 2023-07-31 | 2024-04-26 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 278785 | GBP | 2023-07-31 | 2025-04-24 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2022-07-31 | 2024-04-26 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 263245 | GBP | 2022-07-31 | 2024-04-26 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 32385 | GBP | 2022-07-31 | 2024-04-26 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 112836 | GBP | 2022-07-31 | 2024-04-26 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 319692 | GBP | 2022-07-31 | 2024-04-26 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 56447 | GBP | 2022-07-31 | 2024-04-26 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 51 | GBP | 2022-07-31 | 2024-04-26 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 214907 | GBP | 2022-07-31 | 2024-04-26 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 214807 | GBP | 2022-07-31 | 2024-04-26 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 49 | GBP | 2022-07-31 | 2024-04-26 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 214907 | GBP | 2022-07-31 | 2024-04-26 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 206856 | GBP | 2022-07-31 | 2024-04-26 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 258292 | GBP | 2022-07-31 | 2024-04-26 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## TERRABASE LIMITED (`gb:04612938`)

- registration: `04612938` (GB), status active, incorporated 2002-12-10
- classification: ['62012', '62020'] (sic_2007)
- records: 4 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 64 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.03 | xbrli:pure | 2025-03-31 | 2025-12-22 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| debtors | 30058 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | -16525 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -16625 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | -16525 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -13936 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -6805 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0.03 | xbrli:pure | 2024-03-31 | 2025-12-22 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 3 | xbrli:pure | 2024-03-31 | 2024-12-18 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 21602 | GBP | 2024-03-31 | 2024-12-18 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 21602 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 21602 | GBP | 2024-03-31 | 2024-12-18 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -21744 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity | -21644 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity | -21644 | GBP | 2024-03-31 | 2024-12-18 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -21744 | GBP | 2024-03-31 | 2024-12-18 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-03-31 | 2024-12-18 | filed | no | `core:Equity` | total-exemption-full |
| net_assets | -21644 | GBP | 2024-03-31 | 2024-12-18 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | -21644 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -16268 | GBP | 2024-03-31 | 2024-12-18 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -16268 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -9957 | GBP | 2024-03-31 | 2024-12-18 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -9957 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 3 | xbrli:pure | 2023-03-31 | 2024-12-18 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 24027 | GBP | 2023-03-31 | 2024-12-18 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 24027 | GBP | 2023-03-31 | 2024-12-18 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | -19803 | GBP | 2023-03-31 | 2024-12-18 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -19903 | GBP | 2023-03-31 | 2024-12-18 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-03-31 | 2024-12-18 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | -19803 | GBP | 2023-03-31 | 2024-12-18 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -12707 | GBP | 2023-03-31 | 2024-12-18 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -6176 | GBP | 2023-03-31 | 2024-12-18 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2025-12-22: `{"superseded_document_id": "gb:04612938:doc:MJa435G2azIPnvwOyE7JURrmtflqHtGPo_RsSMWn2y8", "restatements": [{"concept": "average_employees", "period_end": "2024-03-31", "old_value": "3.0000", "new_valu`

## SCU ENTERPRISE LIMITED (`gb:05200107`)

- registration: `05200107` (GB), status active, incorporated 2004-08-09
- classification: ['62012'] (sic_2007)
- records: 6 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 55 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 3 | xbrli:pure | 2025-08-31 | 2026-02-27 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 720 | GBP | 2025-08-31 | 2026-02-27 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 6520 | GBP | 2025-08-31 | 2026-02-27 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 5800 | GBP | 2025-08-31 | 2026-02-27 | filed | yes | `core:Equity` | micro-entity |
| net_assets | 5800 | GBP | 2025-08-31 | 2026-02-27 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 5800 | GBP | 2025-08-31 | 2026-02-27 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 5800 | GBP | 2025-08-31 | 2026-02-27 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 3 | xbrli:pure | 2024-08-31 | 2025-05-16 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 3 | xbrli:pure | 2024-08-31 | 2026-02-27 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 720 | GBP | 2024-08-31 | 2026-02-27 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 720 | GBP | 2024-08-31 | 2025-05-16 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 12296 | GBP | 2024-08-31 | 2026-02-27 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 12296 | GBP | 2024-08-31 | 2025-05-16 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 11576 | GBP | 2024-08-31 | 2026-02-27 | filed | yes | `core:Equity` | micro-entity |
| equity | 11576 | GBP | 2024-08-31 | 2025-05-16 | filed | no | `core:Equity` | micro-entity |
| net_assets | 11576 | GBP | 2024-08-31 | 2025-05-16 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 11576 | GBP | 2024-08-31 | 2026-02-27 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 11576 | GBP | 2024-08-31 | 2026-02-27 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 11576 | GBP | 2024-08-31 | 2025-05-16 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 11576 | GBP | 2024-08-31 | 2025-05-16 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 11576 | GBP | 2024-08-31 | 2026-02-27 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2023-08-31 | 2024-04-25 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 3 | xbrli:pure | 2023-08-31 | 2025-05-16 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 260 | GBP | 2023-08-31 | 2025-05-16 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 260 | GBP | 2023-08-31 | 2024-04-25 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 472 | GBP | 2023-08-31 | 2024-04-25 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 472 | GBP | 2023-08-31 | 2025-05-16 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 212 | GBP | 2023-08-31 | 2024-04-25 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 212 | GBP | 2023-08-31 | 2025-05-16 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2023-08-31 | 2024-04-25 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 212 | GBP | 2023-08-31 | 2024-04-25 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 212 | GBP | 2023-08-31 | 2025-05-16 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 212 | GBP | 2023-08-31 | 2025-05-16 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 212 | GBP | 2023-08-31 | 2024-04-25 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 212 | GBP | 2023-08-31 | 2024-04-25 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 212 | GBP | 2023-08-31 | 2025-05-16 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2022-08-31 | 2024-04-25 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 245 | GBP | 2022-08-31 | 2024-04-25 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 14106 | GBP | 2022-08-31 | 2024-04-25 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 13861 | GBP | 2022-08-31 | 2024-04-25 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2022-08-31 | 2024-04-25 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 13861 | GBP | 2022-08-31 | 2024-04-25 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 13861 | GBP | 2022-08-31 | 2024-04-25 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 13861 | GBP | 2022-08-31 | 2024-04-25 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## NETWORKER UK LIMITED (`gb:05765115`)

- registration: `05765115` (GB), status active, incorporated 2006-03-31
- classification: ['62090'] (sic_2007)
- records: 9 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 74 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | xbrli:pure | 2025-03-31 | 2026-03-08 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 3941 | GBP | 2025-03-31 | 2026-03-08 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 20642 | GBP | 2025-03-31 | 2026-03-08 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 20657 | GBP | 2025-03-31 | 2026-03-08 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 3956 | GBP | 2025-03-31 | 2026-03-08 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 20657 | GBP | 2025-03-31 | 2026-03-08 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 16701 | GBP | 2025-03-31 | 2026-03-08 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 20657 | GBP | 2025-03-31 | 2026-03-08 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2024-03-31 | 2026-03-08 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | xbrli:pure | 2024-03-31 | 2024-12-18 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 7249 | GBP | 2024-03-31 | 2024-12-18 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 7249 | GBP | 2024-03-31 | 2026-03-08 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 24719 | GBP | 2024-03-31 | 2026-03-08 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 24719 | GBP | 2024-03-31 | 2024-12-18 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 21426 | GBP | 2024-03-31 | 2024-12-18 | filed | no | `core:Equity` | micro-entity |
| equity | 21426 | GBP | 2024-03-31 | 2026-03-08 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 3956 | GBP | 2024-03-31 | 2024-12-18 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 3956 | GBP | 2024-03-31 | 2026-03-08 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 21426 | GBP | 2024-03-31 | 2026-03-08 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 21426 | GBP | 2024-03-31 | 2024-12-18 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 17470 | GBP | 2024-03-31 | 2026-03-08 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 17470 | GBP | 2024-03-31 | 2024-12-18 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 21426 | GBP | 2024-03-31 | 2024-12-18 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 21426 | GBP | 2024-03-31 | 2026-03-08 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2023-03-31 | 2024-12-18 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | xbrli:pure | 2023-03-31 | 2023-12-18 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1693 | GBP | 2023-03-31 | 2023-12-18 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1693 | GBP | 2023-03-31 | 2024-12-18 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 36606 | GBP | 2023-03-31 | 2023-12-18 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 36606 | GBP | 2023-03-31 | 2024-12-18 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 34914 | GBP | 2023-03-31 | 2023-12-18 | filed | no | `core:Equity` | micro-entity |
| equity | 34914 | GBP | 2023-03-31 | 2024-12-18 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 1 | GBP | 2023-03-31 | 2023-12-18 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 1 | GBP | 2023-03-31 | 2024-12-18 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 34914 | GBP | 2023-03-31 | 2024-12-18 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 34914 | GBP | 2023-03-31 | 2023-12-18 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 34913 | GBP | 2023-03-31 | 2023-12-18 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 34913 | GBP | 2023-03-31 | 2024-12-18 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 34914 | GBP | 2023-03-31 | 2024-12-18 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 34914 | GBP | 2023-03-31 | 2023-12-18 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2022-03-31 | 2023-12-18 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 537 | GBP | 2022-03-31 | 2023-12-18 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 34994 | GBP | 2022-03-31 | 2023-12-18 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 34458 | GBP | 2022-03-31 | 2023-12-18 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 1 | GBP | 2022-03-31 | 2023-12-18 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 34458 | GBP | 2022-03-31 | 2023-12-18 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 34457 | GBP | 2022-03-31 | 2023-12-18 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 34458 | GBP | 2022-03-31 | 2023-12-18 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## KUREO LTD (`gb:06261049`)

- registration: `06261049` (GB), status active, incorporated 2007-05-29
- classification: ['71121'] (sic_2007)
- records: 2 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 47 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.01 | xbrli:pure | 2025-05-31 | 2026-02-03 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 8046 | GBP | 2025-05-31 | 2026-02-03 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 47586 | GBP | 2025-05-31 | 2026-02-03 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 42230 | GBP | 2025-05-31 | 2026-02-03 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 2690 | GBP | 2025-05-31 | 2026-02-03 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 42230 | GBP | 2025-05-31 | 2026-02-03 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 39540 | GBP | 2025-05-31 | 2026-02-03 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 42230 | GBP | 2025-05-31 | 2026-02-03 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-05-31 | 2024-12-16 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0.01 | xbrli:pure | 2024-05-31 | 2026-02-03 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 46919 | GBP | 2024-05-31 | 2026-02-03 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 46919 | GBP | 2024-05-31 | 2024-12-16 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 109267 | GBP | 2024-05-31 | 2024-12-16 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 109267 | GBP | 2024-05-31 | 2026-02-03 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 64311 | GBP | 2024-05-31 | 2026-02-03 | filed | yes | `core:Equity` | micro-entity |
| equity | 64311 | GBP | 2024-05-31 | 2024-12-16 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 1963 | GBP | 2024-05-31 | 2024-12-16 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 1963 | GBP | 2024-05-31 | 2026-02-03 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 64311 | GBP | 2024-05-31 | 2026-02-03 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 62348 | GBP | 2024-05-31 | 2026-02-03 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 64311 | GBP | 2024-05-31 | 2026-02-03 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-05-31 | 2024-12-16 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-05-31 | 2023-11-24 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 21538 | GBP | 2023-05-31 | 2023-11-24 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 21538 | GBP | 2023-05-31 | 2024-12-16 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 67629 | GBP | 2023-05-31 | 2024-12-16 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 67629 | GBP | 2023-05-31 | 2023-11-24 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 48709 | GBP | 2023-05-31 | 2024-12-16 | filed | yes | `core:Equity` | micro-entity |
| equity | 48709 | GBP | 2023-05-31 | 2023-11-24 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 2618 | GBP | 2023-05-31 | 2024-12-16 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 2618 | GBP | 2023-05-31 | 2023-11-24 | filed | no | `core:FixedAssets` | micro-entity |
| average_employees | 0 | xbrli:pure | 2022-05-31 | 2023-11-24 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 13614 | GBP | 2022-05-31 | 2023-11-24 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 60342 | GBP | 2022-05-31 | 2023-11-24 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 50218 | GBP | 2022-05-31 | 2023-11-24 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 3490 | GBP | 2022-05-31 | 2023-11-24 | filed | yes | `core:FixedAssets` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2026-02-03: `{"superseded_document_id": "gb:06261049:doc:h264KDxUH6HObEC18Fnfp3m1JwdoZVi2Qh6bcCNs0NY", "restatements": [{"concept": "average_employees", "period_end": "2024-05-31", "old_value": "1.0000", "new_valu`

## REM CONSULTANCY LIMITED (`gb:06668892`)

- registration: `06668892` (GB), status active, incorporated 2008-08-11
- classification: ['62012'] (sic_2007)
- records: 2 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 49 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-08-31 | 2026-05-06 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 8400 | GBP | 2025-08-31 | 2026-05-06 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 9154 | GBP | 2025-08-31 | 2026-05-06 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 4438 | GBP | 2025-08-31 | 2026-05-06 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 3684 | GBP | 2025-08-31 | 2026-05-06 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 4438 | GBP | 2025-08-31 | 2026-05-06 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 754 | GBP | 2025-08-31 | 2026-05-06 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 4438 | GBP | 2025-08-31 | 2026-05-06 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-08-31 | 2025-05-27 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-08-31 | 2026-05-06 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 50672 | GBP | 2024-08-31 | 2025-05-27 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 50672 | GBP | 2024-08-31 | 2026-05-06 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 89336 | GBP | 2024-08-31 | 2026-05-06 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 89336 | GBP | 2024-08-31 | 2025-05-27 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 43396 | GBP | 2024-08-31 | 2026-05-06 | filed | yes | `core:Equity` | micro-entity |
| equity | 43396 | GBP | 2024-08-31 | 2025-05-27 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 4766 | GBP | 2024-08-31 | 2025-05-27 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 4766 | GBP | 2024-08-31 | 2026-05-06 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 43396 | GBP | 2024-08-31 | 2025-05-27 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 43396 | GBP | 2024-08-31 | 2026-05-06 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 38664 | GBP | 2024-08-31 | 2026-05-06 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 38664 | GBP | 2024-08-31 | 2025-05-27 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 43430 | GBP | 2024-08-31 | 2025-05-27 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 43430 | GBP | 2024-08-31 | 2026-05-06 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-08-31 | 2025-05-27 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-08-31 | 2024-05-08 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 34726 | GBP | 2023-08-31 | 2025-05-27 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 48928 | GBP | 2023-08-31 | 2025-05-27 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 38073.4 | GBP | 2023-08-31 | 2024-05-08 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | 20256.87 | GBP | 2023-08-31 | 2024-05-08 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 20257 | GBP | 2023-08-31 | 2025-05-27 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 6355.67 | GBP | 2023-08-31 | 2024-05-08 | filed | no | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 6356 | GBP | 2023-08-31 | 2025-05-27 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 20256.87 | GBP | 2023-08-31 | 2024-05-08 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 20257 | GBP | 2023-08-31 | 2025-05-27 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 14202.2 | GBP | 2023-08-31 | 2024-05-08 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 14202 | GBP | 2023-08-31 | 2025-05-27 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 20557.87 | GBP | 2023-08-31 | 2024-05-08 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 20558 | GBP | 2023-08-31 | 2025-05-27 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2022-08-31 | 2024-05-08 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 55214.44 | GBP | 2022-08-31 | 2024-05-08 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 30268.35 | GBP | 2022-08-31 | 2024-05-08 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 6444.6 | GBP | 2022-08-31 | 2024-05-08 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 30268.35 | GBP | 2022-08-31 | 2024-05-08 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 23823.75 | GBP | 2022-08-31 | 2024-05-08 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 30268.35 | GBP | 2022-08-31 | 2024-05-08 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2025-05-27: `{"superseded_document_id": "gb:06668892:doc:vXJTU9SObf5ms4D3K5iFXsL4LKo2SIJdFWRvL8dhalI", "restatements": [{"concept": "fixed_assets", "period_end": "2023-08-31", "old_value": "6355.6700", "new_value"`

## UQ WEB DESIGN LTD (`gb:07105175`)

- registration: `07105175` (GB), status active, incorporated 2009-12-15
- classification: ['62090'] (sic_2007)
- records: 3 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 50 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-12-31 | 2026-02-17 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 23281 | GBP | 2025-12-31 | 2026-02-17 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| equity | 11008 | GBP | 2025-12-31 | 2026-02-17 | filed | yes | `frs-core:Equity` | micro-entity |
| fixed_assets | 673 | GBP | 2025-12-31 | 2026-02-17 | filed | yes | `frs-core:FixedAssets` | micro-entity |
| net_assets | 11008 | GBP | 2025-12-31 | 2026-02-17 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 11525 | GBP | 2025-12-31 | 2026-02-17 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 12198 | GBP | 2025-12-31 | 2026-02-17 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-12-31 | 2026-02-17 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-12-31 | 2025-01-28 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 15454 | GBP | 2024-12-31 | 2025-01-28 | filed | no | `ns5:CurrentAssets` | micro-entity |
| current_assets | 14889 | GBP | 2024-12-31 | 2026-02-17 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| equity | 2582 | GBP | 2024-12-31 | 2025-01-28 | filed | no | `ns5:Equity` | micro-entity |
| equity | 2582 | GBP | 2024-12-31 | 2026-02-17 | filed | yes | `frs-core:Equity` | micro-entity |
| fixed_assets | 487 | GBP | 2024-12-31 | 2026-02-17 | filed | yes | `frs-core:FixedAssets` | micro-entity |
| fixed_assets | 487 | GBP | 2024-12-31 | 2025-01-28 | filed | no | `ns5:FixedAssets` | micro-entity |
| net_assets | 2582 | GBP | 2024-12-31 | 2026-02-17 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 2582 | GBP | 2024-12-31 | 2025-01-28 | filed | no | `ns5:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 3101 | GBP | 2024-12-31 | 2026-02-17 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 2098 | GBP | 2024-12-31 | 2025-01-28 | filed | no | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 3588 | GBP | 2024-12-31 | 2026-02-17 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 2585 | GBP | 2024-12-31 | 2025-01-28 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 1 | xbrli:pure | 2023-12-31 | 2024-01-18 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-12-31 | 2025-01-28 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 11423 | GBP | 2023-12-31 | 2025-01-28 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 11423 | GBP | 2023-12-31 | 2024-01-18 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 74 | GBP | 2023-12-31 | 2024-01-18 | filed | yes | `ns5:Equity` | micro-entity |
| equity | 74 | GBP | 2023-12-31 | 2025-01-28 | filed | yes | `ns5:Equity` | micro-entity |
| fixed_assets | 974 | GBP | 2023-12-31 | 2025-01-28 | filed | yes | `ns5:FixedAssets` | micro-entity |
| fixed_assets `{'OriginalRevisedDataDimension': 'Original'}` | 974 | GBP | 2023-12-31 | 2024-01-18 | filed | yes | `ns5:FixedAssets` | micro-entity |
| net_assets | 74 | GBP | 2023-12-31 | 2025-01-28 | filed | yes | `ns5:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -900 | GBP | 2023-12-31 | 2025-01-28 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | -900 | GBP | 2023-12-31 | 2024-01-18 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 74 | GBP | 2023-12-31 | 2024-01-18 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 74 | GBP | 2023-12-31 | 2025-01-28 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 1 | xbrli:pure | 2022-12-31 | 2024-01-18 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 13072 | GBP | 2022-12-31 | 2024-01-18 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 75 | GBP | 2022-12-31 | 2024-01-18 | filed | yes | `ns5:Equity` | micro-entity |
| fixed_assets `{'OriginalRevisedDataDimension': 'Original'}` | 334 | GBP | 2022-12-31 | 2024-01-18 | filed | yes | `ns5:FixedAssets` | micro-entity |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | -259 | GBP | 2022-12-31 | 2024-01-18 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 75 | GBP | 2022-12-31 | 2024-01-18 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |

Coverage @ 2025-12-31: 7/21 concepts available (average_employees, current_assets, equity, fixed_assets, net_assets, net_current_assets, total_assets_less_current_liabilities)
- `cash`: filed_without_concept — regime 'micro-entity' omits this concept
- `creditors_after_one_year`: filed_without_concept — regime 'micro-entity' omits this concept
- `creditors_within_one_year`: filed_without_concept — absent though regime 'micro-entity' typically includes it
- `debtors`: filed_without_concept — regime 'micro-entity' omits this concept
- `depreciation_amortisation`: filed_without_concept — regime 'micro-entity' omits this concept
- `gross_profit`: filed_without_concept — regime 'micro-entity' omits this concept
- `operating_profit`: filed_without_concept — regime 'micro-entity' omits this concept
- `profit_before_tax`: filed_without_concept — regime 'micro-entity' omits this concept
- `profit_for_period`: filed_without_concept — regime 'micro-entity' omits this concept
- `retained_earnings`: filed_without_concept — regime 'micro-entity' omits this concept
- `revenue`: filed_without_concept — regime 'micro-entity' omits this concept
- `share_capital`: filed_without_concept — regime 'micro-entity' omits this concept
- `staff_costs`: filed_without_concept — regime 'micro-entity' omits this concept
- `tax_charge`: filed_without_concept — regime 'micro-entity' omits this concept

- event restatement @ 2026-02-17: `{"superseded_document_id": "gb:07105175:doc:WG9TNZ2TEyMzMjZwKFstVWzk97yZgch-O7iwcA9PTiM", "restatements": [{"concept": "current_assets", "period_end": "2024-12-31", "old_value": "15454.0000", "new_val`
