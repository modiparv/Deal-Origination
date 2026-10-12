# Ingest spot-check

- database: `data/engine.db`
- latest run: `20261012T084455Z-401d5985`
- companies in store: 25000; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## PRO ENG PROJECT AND ENGINEERING SERVICES LIMITED (`gb:02198191`)

- registration: `02198191` (GB), status active, incorporated 1987-11-25
- classification: ['71129'] (sic_2007)
- records: 5 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 87 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## STRUCTURAL REPAIRS & SPECIALIST SERVICES LIMITED (`gb:02771845`)

- registration: `02771845` (GB), status active, incorporated 1992-12-08
- classification: ['43999', '71129'] (sic_2007)
- records: 11 officers, 3 beneficial owners, 1 ownership statements, 1 security interests, 105 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 14 | xbrli:pure | 2025-12-31 | 2026-07-29 | filed | yes | `d:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 981198 | GBP | 2025-12-31 | 2026-07-29 | filed | yes | `d:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 7788 | GBP | 2025-12-31 | 2026-07-29 | filed | yes | `d:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 951607 | GBP | 2025-12-31 | 2026-07-29 | filed | yes | `d:Creditors` | total-exemption-full |
| current_assets | 3322862 | GBP | 2025-12-31 | 2026-07-29 | filed | yes | `d:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 1844214 | GBP | 2025-12-31 | 2026-07-29 | filed | yes | `d:Debtors` | total-exemption-full |
| equity | 2467772 | GBP | 2025-12-31 | 2026-07-29 | filed | yes | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2025-12-31 | 2026-07-29 | filed | yes | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2466772 | GBP | 2025-12-31 | 2026-07-29 | filed | yes | `d:Equity` | total-exemption-full |
| fixed_assets | 123735 | GBP | 2025-12-31 | 2026-07-29 | filed | yes | `d:FixedAssets` | total-exemption-full |
| net_assets | 2467772 | GBP | 2025-12-31 | 2026-07-29 | filed | yes | `d:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 2371255 | GBP | 2025-12-31 | 2026-07-29 | filed | yes | `d:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 2494990 | GBP | 2025-12-31 | 2026-07-29 | filed | yes | `d:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 13 | xbrli:pure | 2024-12-31 | 2025-09-29 | filed | no | `d:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 13 | xbrli:pure | 2024-12-31 | 2026-07-29 | filed | yes | `d:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 525155 | GBP | 2024-12-31 | 2026-07-29 | filed | yes | `d:CashBankOnHand` | total-exemption-full |
| cash | 525155 | GBP | 2024-12-31 | 2025-09-29 | filed | no | `d:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 12979 | GBP | 2024-12-31 | 2026-07-29 | filed | yes | `d:Creditors` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 12979 | GBP | 2024-12-31 | 2025-09-29 | filed | no | `d:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 659721 | GBP | 2024-12-31 | 2025-09-29 | filed | no | `d:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 659721 | GBP | 2024-12-31 | 2026-07-29 | filed | yes | `d:Creditors` | total-exemption-full |
| current_assets | 3214316 | GBP | 2024-12-31 | 2025-09-29 | filed | no | `d:CurrentAssets` | total-exemption-full |
| current_assets | 3214316 | GBP | 2024-12-31 | 2026-07-29 | filed | yes | `d:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 2289095 | GBP | 2024-12-31 | 2025-09-29 | filed | no | `d:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 2289095 | GBP | 2024-12-31 | 2026-07-29 | filed | yes | `d:Debtors` | total-exemption-full |
| equity | 2614807 | GBP | 2024-12-31 | 2026-07-29 | filed | yes | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2613807 | GBP | 2024-12-31 | 2026-07-29 | filed | yes | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2024-12-31 | 2026-07-29 | filed | yes | `d:Equity` | total-exemption-full |
| equity | 2614807 | GBP | 2024-12-31 | 2025-09-29 | filed | no | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2613807 | GBP | 2024-12-31 | 2025-09-29 | filed | no | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2024-12-31 | 2025-09-29 | filed | no | `d:Equity` | total-exemption-full |
| fixed_assets | 93834 | GBP | 2024-12-31 | 2025-09-29 | filed | no | `d:FixedAssets` | total-exemption-full |
| fixed_assets | 93834 | GBP | 2024-12-31 | 2026-07-29 | filed | yes | `d:FixedAssets` | total-exemption-full |
| net_assets | 2614807 | GBP | 2024-12-31 | 2025-09-29 | filed | no | `d:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 2614807 | GBP | 2024-12-31 | 2026-07-29 | filed | yes | `d:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 2554595 | GBP | 2024-12-31 | 2026-07-29 | filed | yes | `d:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 2554595 | GBP | 2024-12-31 | 2025-09-29 | filed | no | `d:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 2648429 | GBP | 2024-12-31 | 2025-09-29 | filed | no | `d:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 2648429 | GBP | 2024-12-31 | 2026-07-29 | filed | yes | `d:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 14 | xbrli:pure | 2023-12-31 | 2025-09-29 | filed | yes | `d:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 14 | xbrli:pure | 2023-12-31 | 2024-07-19 | filed | no | `d:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 1032538 | GBP | 2023-12-31 | 2025-09-29 | filed | yes | `d:CashBankOnHand` | total-exemption-full |
| cash | 1032538 | GBP | 2023-12-31 | 2024-07-19 | filed | no | `d:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 307036 | GBP | 2023-12-31 | 2024-07-19 | filed | no | `d:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 307036 | GBP | 2023-12-31 | 2025-09-29 | filed | yes | `d:Creditors` | total-exemption-full |
| current_assets | 2102445 | GBP | 2023-12-31 | 2025-09-29 | filed | yes | `d:CurrentAssets` | total-exemption-full |
| current_assets | 2102445 | GBP | 2023-12-31 | 2024-07-19 | filed | no | `d:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 542520 | GBP | 2023-12-31 | 2024-07-19 | filed | no | `d:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 542520 | GBP | 2023-12-31 | 2025-09-29 | filed | yes | `d:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1853050 | GBP | 2023-12-31 | 2025-09-29 | filed | yes | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2023-12-31 | 2024-07-19 | filed | no | `d:Equity` | total-exemption-full |
| equity | 1854050 | GBP | 2023-12-31 | 2025-09-29 | filed | yes | `d:Equity` | total-exemption-full |
| equity | 1854050 | GBP | 2023-12-31 | 2024-07-19 | filed | no | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1853050 | GBP | 2023-12-31 | 2024-07-19 | filed | no | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2023-12-31 | 2025-09-29 | filed | yes | `d:Equity` | total-exemption-full |
| fixed_assets | 75236 | GBP | 2023-12-31 | 2025-09-29 | filed | yes | `d:FixedAssets` | total-exemption-full |
| fixed_assets | 75236 | GBP | 2023-12-31 | 2024-07-19 | filed | no | `d:FixedAssets` | total-exemption-full |
| net_assets | 1854050 | GBP | 2023-12-31 | 2025-09-29 | filed | yes | `d:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 1854050 | GBP | 2023-12-31 | 2024-07-19 | filed | no | `d:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1795409 | GBP | 2023-12-31 | 2025-09-29 | filed | yes | `d:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1795409 | GBP | 2023-12-31 | 2024-07-19 | filed | no | `d:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1870645 | GBP | 2023-12-31 | 2025-09-29 | filed | yes | `d:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1870645 | GBP | 2023-12-31 | 2024-07-19 | filed | no | `d:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 13 | xbrli:pure | 2022-12-31 | 2024-07-19 | filed | yes | `d:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 920398 | GBP | 2022-12-31 | 2024-07-19 | filed | yes | `d:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 451050 | GBP | 2022-12-31 | 2024-07-19 | filed | yes | `d:Creditors` | total-exemption-full |
| current_assets | 2075437 | GBP | 2022-12-31 | 2024-07-19 | filed | yes | `d:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 659284 | GBP | 2022-12-31 | 2024-07-19 | filed | yes | `d:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2022-12-31 | 2024-07-19 | filed | yes | `d:Equity` | total-exemption-full |
| equity | 1668964 | GBP | 2022-12-31 | 2024-07-19 | filed | yes | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1667964 | GBP | 2022-12-31 | 2024-07-19 | filed | yes | `d:Equity` | total-exemption-full |
| fixed_assets | 56072 | GBP | 2022-12-31 | 2024-07-19 | filed | yes | `d:FixedAssets` | total-exemption-full |
| net_assets | 1668964 | GBP | 2022-12-31 | 2024-07-19 | filed | yes | `d:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1624387 | GBP | 2022-12-31 | 2024-07-19 | filed | yes | `d:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1680459 | GBP | 2022-12-31 | 2024-07-19 | filed | yes | `d:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## EA-RS FIRE ENGINEERING LIMITED (`gb:03151149`)

- registration: `03151149` (GB), status active, incorporated 1996-01-25
- classification: ['71129'] (sic_2007)
- records: 18 officers, 3 beneficial owners, 0 ownership statements, 12 security interests, 166 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 93 | xbrli:pure | 2024-09-30 | 2025-06-26 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | full |
| cash | 498105 | GBP | 2024-09-30 | 2025-06-26 | filed | yes | `core:CashBankOnHand` | full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 6370973 | GBP | 2024-09-30 | 2025-06-26 | filed | yes | `core:Creditors` | full |
| current_assets | 9747764 | GBP | 2024-09-30 | 2025-06-26 | filed | yes | `core:CurrentAssets` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 9039597 | GBP | 2024-09-30 | 2025-06-26 | filed | yes | `core:Debtors` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 9039597 | GBP | 2024-09-30 | 2025-06-26 | filed | yes | `core:Debtors` | full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 400 | GBP | 2024-09-30 | 2025-06-26 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 6211266 | GBP | 2024-09-30 | 2025-06-26 | filed | yes | `core:Equity` | full |
| equity | 6272266 | GBP | 2024-09-30 | 2025-06-26 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 60000 | GBP | 2024-09-30 | 2025-06-26 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 600 | GBP | 2024-09-30 | 2025-06-26 | filed | yes | `core:Equity` | full |
| fixed_assets | 2894376 | GBP | 2024-09-30 | 2025-06-26 | filed | yes | `core:FixedAssets` | full |
| gross_profit | 6689481 | GBP | 2024-09-30 | 2025-06-26 | filed | yes | `core:GrossProfitLoss` | full |
| net_assets | 6272266 | GBP | 2024-09-30 | 2025-06-26 | filed | yes | `core:NetAssetsLiabilities` | full |
| net_current_assets | 3376791 | GBP | 2024-09-30 | 2025-06-26 | filed | yes | `core:NetCurrentAssetsLiabilities` | full |
| profit_before_tax | 1613326 | GBP | 2024-09-30 | 2025-06-26 | filed | yes | `core:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period | 2198999 | GBP | 2024-09-30 | 2025-06-26 | filed | yes | `core:ProfitLoss` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2198999 | GBP | 2024-09-30 | 2025-06-26 | filed | yes | `core:ProfitLoss` | full |
| revenue | 31725485 | GBP | 2024-09-30 | 2025-06-26 | filed | yes | `core:TurnoverRevenue` | full |
| revenue `{'OperatingSegmentsDimension': 'ReportableOperatingSegment1'}` | 31725485 | GBP | 2024-09-30 | 2025-06-26 | filed | yes | `core:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'UnitedKingdom'}` | 31725485 | GBP | 2024-09-30 | 2025-06-26 | filed | yes | `core:TurnoverRevenue` | full |
| staff_costs | 5965271 | GBP | 2024-09-30 | 2025-06-26 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | full |
| tax_charge | -585673 | GBP | 2024-09-30 | 2025-06-26 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| total_assets_less_current_liabilities | 6271167 | GBP | 2024-09-30 | 2025-06-26 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | full |
| average_employees | 85 | xbrli:pure | 2023-09-30 | 2025-06-26 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | full |
| average_employees | 85 | xbrli:pure | 2023-09-30 | 2024-08-19 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | full |
| cash | 1124600 | GBP | 2023-09-30 | 2025-06-26 | filed | yes | `core:CashBankOnHand` | full |
| cash | 1124600 | GBP | 2023-09-30 | 2024-08-19 | filed | no | `core:CashBankOnHand` | full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 10399742 | GBP | 2023-09-30 | 2025-06-26 | filed | yes | `core:Creditors` | full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 10399742 | GBP | 2023-09-30 | 2024-08-19 | filed | no | `core:Creditors` | full |
| current_assets | 11255144 | GBP | 2023-09-30 | 2025-06-26 | filed | yes | `core:CurrentAssets` | full |
| current_assets | 11255144 | GBP | 2023-09-30 | 2024-08-19 | filed | no | `core:CurrentAssets` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 9862810 | GBP | 2023-09-30 | 2025-06-26 | filed | yes | `core:Debtors` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 9862810 | GBP | 2023-09-30 | 2025-06-26 | filed | yes | `core:Debtors` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 9862810 | GBP | 2023-09-30 | 2024-08-19 | filed | no | `core:Debtors` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 9862810 | GBP | 2023-09-30 | 2024-08-19 | filed | no | `core:Debtors` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 600 | GBP | 2023-09-30 | 2024-08-19 | filed | no | `core:Equity` | full |
| equity | 4073267 | GBP | 2023-09-30 | 2024-08-19 | filed | no | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 4012267 | GBP | 2023-09-30 | 2025-06-26 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 400 | GBP | 2023-09-30 | 2024-08-19 | filed | no | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 400 | GBP | 2023-09-30 | 2025-06-26 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 60000 | GBP | 2023-09-30 | 2025-06-26 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 600 | GBP | 2023-09-30 | 2025-06-26 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 4012267 | GBP | 2023-09-30 | 2024-08-19 | filed | no | `core:Equity` | full |
| equity | 4073267 | GBP | 2023-09-30 | 2025-06-26 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 60000 | GBP | 2023-09-30 | 2024-08-19 | filed | no | `core:Equity` | full |
| fixed_assets | 3254744 | GBP | 2023-09-30 | 2025-06-26 | filed | yes | `core:FixedAssets` | full |
| fixed_assets | 3254744 | GBP | 2023-09-30 | 2024-08-19 | filed | no | `core:FixedAssets` | full |
| gross_profit | 4501569 | GBP | 2023-09-30 | 2024-08-19 | filed | no | `core:GrossProfitLoss` | full |
| gross_profit | 4501569 | GBP | 2023-09-30 | 2025-06-26 | filed | yes | `core:GrossProfitLoss` | full |
| net_assets | 4073267 | GBP | 2023-09-30 | 2024-08-19 | filed | no | `core:NetAssetsLiabilities` | full |
| net_assets | 4073267 | GBP | 2023-09-30 | 2025-06-26 | filed | yes | `core:NetAssetsLiabilities` | full |
| net_current_assets | 855402 | GBP | 2023-09-30 | 2025-06-26 | filed | yes | `core:NetCurrentAssetsLiabilities` | full |
| net_current_assets | 855402 | GBP | 2023-09-30 | 2024-08-19 | filed | no | `core:NetCurrentAssetsLiabilities` | full |
| profit_before_tax | 536224 | GBP | 2023-09-30 | 2025-06-26 | filed | yes | `core:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_before_tax | 536224 | GBP | 2023-09-30 | 2024-08-19 | filed | no | `core:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 787801 | GBP | 2023-09-30 | 2024-08-19 | filed | no | `core:ProfitLoss` | full |
| profit_for_period | 787801 | GBP | 2023-09-30 | 2025-06-26 | filed | yes | `core:ProfitLoss` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 787801 | GBP | 2023-09-30 | 2025-06-26 | filed | yes | `core:ProfitLoss` | full |
| profit_for_period | 787801 | GBP | 2023-09-30 | 2024-08-19 | filed | no | `core:ProfitLoss` | full |
| revenue | 27452634 | GBP | 2023-09-30 | 2025-06-26 | filed | yes | `core:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'UnitedKingdom'}` | 27452634 | GBP | 2023-09-30 | 2025-06-26 | filed | yes | `core:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'UnitedKingdom'}` | 27452634 | GBP | 2023-09-30 | 2024-08-19 | filed | no | `core:TurnoverRevenue` | full |
| revenue `{'OperatingSegmentsDimension': 'ReportableOperatingSegment1'}` | 27452634 | GBP | 2023-09-30 | 2024-08-19 | filed | no | `core:TurnoverRevenue` | full |
| revenue | 27452634 | GBP | 2023-09-30 | 2024-08-19 | filed | no | `core:TurnoverRevenue` | full |
| revenue `{'OperatingSegmentsDimension': 'ReportableOperatingSegment1'}` | 27452634 | GBP | 2023-09-30 | 2025-06-26 | filed | yes | `core:TurnoverRevenue` | full |
| staff_costs | 4956744 | GBP | 2023-09-30 | 2024-08-19 | filed | no | `core:StaffCostsEmployeeBenefitsExpense` | full |
| staff_costs | 4956744 | GBP | 2023-09-30 | 2025-06-26 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | full |
| tax_charge | -251577 | GBP | 2023-09-30 | 2025-06-26 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| tax_charge | -251577 | GBP | 2023-09-30 | 2024-08-19 | filed | no | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| total_assets_less_current_liabilities | 4110146 | GBP | 2023-09-30 | 2024-08-19 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | full |
| total_assets_less_current_liabilities | 4110146 | GBP | 2023-09-30 | 2025-06-26 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | full |
| average_employees | 73 | xbrli:pure | 2022-09-30 | 2024-08-19 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | full |
| cash | 538949 | GBP | 2022-09-30 | 2024-08-19 | filed | yes | `core:CashBankOnHand` | full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 17153 | GBP | 2022-09-30 | 2024-08-19 | filed | yes | `core:Creditors` | full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 6802889 | GBP | 2022-09-30 | 2024-08-19 | filed | yes | `core:Creditors` | full |
| current_assets | 7356245 | GBP | 2022-09-30 | 2024-08-19 | filed | yes | `core:CurrentAssets` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 6742578 | GBP | 2022-09-30 | 2024-08-19 | filed | yes | `core:Debtors` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 6742578 | GBP | 2022-09-30 | 2024-08-19 | filed | yes | `core:Debtors` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 600 | GBP | 2022-09-30 | 2024-08-19 | filed | no | `core:Equity` | full |
| equity | 3285466 | GBP | 2022-09-30 | 2025-06-26 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 60000 | GBP | 2022-09-30 | 2025-06-26 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3224466 | GBP | 2022-09-30 | 2025-06-26 | filed | yes | `core:Equity` | full |
| equity | 3285466 | GBP | 2022-09-30 | 2024-08-19 | filed | no | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 600 | GBP | 2022-09-30 | 2025-06-26 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3224466 | GBP | 2022-09-30 | 2024-08-19 | filed | no | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 400 | GBP | 2022-09-30 | 2024-08-19 | filed | no | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 60000 | GBP | 2022-09-30 | 2024-08-19 | filed | no | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 400 | GBP | 2022-09-30 | 2025-06-26 | filed | yes | `core:Equity` | full |
| fixed_assets | 2775723 | GBP | 2022-09-30 | 2024-08-19 | filed | yes | `core:FixedAssets` | full |
| gross_profit | 5050140 | GBP | 2022-09-30 | 2024-08-19 | filed | yes | `core:GrossProfitLoss` | full |
| net_assets | 3285466 | GBP | 2022-09-30 | 2024-08-19 | filed | yes | `core:NetAssetsLiabilities` | full |
| net_current_assets | 553356 | GBP | 2022-09-30 | 2024-08-19 | filed | yes | `core:NetCurrentAssetsLiabilities` | full |
| profit_before_tax | 791289 | GBP | 2022-09-30 | 2024-08-19 | filed | yes | `core:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 880563 | GBP | 2022-09-30 | 2024-08-19 | filed | yes | `core:ProfitLoss` | full |
| profit_for_period | 880563 | GBP | 2022-09-30 | 2024-08-19 | filed | yes | `core:ProfitLoss` | full |
| revenue | 18670630 | GBP | 2022-09-30 | 2024-08-19 | filed | yes | `core:TurnoverRevenue` | full |
| revenue `{'OperatingSegmentsDimension': 'ReportableOperatingSegment1'}` | 18670630 | GBP | 2022-09-30 | 2024-08-19 | filed | yes | `core:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'UnitedKingdom'}` | 18670630 | GBP | 2022-09-30 | 2024-08-19 | filed | yes | `core:TurnoverRevenue` | full |
| staff_costs | 4318234 | GBP | 2022-09-30 | 2024-08-19 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | full |
| tax_charge | -89274 | GBP | 2022-09-30 | 2024-08-19 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| total_assets_less_current_liabilities | 3329079 | GBP | 2022-09-30 | 2024-08-19 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | full |
| equity | 2409703 | GBP | 2021-09-30 | 2024-08-19 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2343903 | GBP | 2021-09-30 | 2024-08-19 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 64800 | GBP | 2021-09-30 | 2024-08-19 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 600 | GBP | 2021-09-30 | 2024-08-19 | filed | yes | `core:Equity` | full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 400 | GBP | 2021-09-30 | 2024-08-19 | filed | yes | `core:Equity` | full |

_No coverage facts for the latest run._

## AASHI CONSULTING LIMITED (`gb:03454073`)

- registration: `03454073` (GB), status active, incorporated 1997-10-23
- classification: ['62012'] (sic_2007)
- records: 5 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 76 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-10-31 | 2026-07-17 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5822 | GBP | 2025-10-31 | 2026-07-17 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 118 | GBP | 2025-10-31 | 2026-07-17 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -5666 | GBP | 2025-10-31 | 2026-07-17 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 158 | GBP | 2025-10-31 | 2026-07-17 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | -5666 | GBP | 2025-10-31 | 2026-07-17 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -5704 | GBP | 2025-10-31 | 2026-07-17 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -5546 | GBP | 2025-10-31 | 2026-07-17 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-10-31 | 2026-07-17 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-10-31 | 2025-07-30 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5582 | GBP | 2024-10-31 | 2026-07-17 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5582 | GBP | 2024-10-31 | 2025-07-30 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 220 | GBP | 2024-10-31 | 2025-07-30 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 220 | GBP | 2024-10-31 | 2026-07-17 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -5271 | GBP | 2024-10-31 | 2026-07-17 | filed | yes | `core:Equity` | micro-entity |
| equity | -5271 | GBP | 2024-10-31 | 2025-07-30 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 211 | GBP | 2024-10-31 | 2026-07-17 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 211 | GBP | 2024-10-31 | 2025-07-30 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | -5271 | GBP | 2024-10-31 | 2025-07-30 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | -5271 | GBP | 2024-10-31 | 2026-07-17 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -5362 | GBP | 2024-10-31 | 2026-07-17 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -5362 | GBP | 2024-10-31 | 2025-07-30 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -5151 | GBP | 2024-10-31 | 2025-07-30 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -5151 | GBP | 2024-10-31 | 2026-07-17 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-10-31 | 2025-07-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-10-31 | 2024-07-29 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 4897 | GBP | 2023-10-31 | 2025-07-30 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5137 | GBP | 2023-10-31 | 2024-07-29 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 4 | GBP | 2023-10-31 | 2025-07-30 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 4 | GBP | 2023-10-31 | 2024-07-29 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | 4852 | GBP | 2023-10-31 | 2024-07-29 | filed | no | `uk-core:Equity` | micro-entity |
| equity | -4852 | GBP | 2023-10-31 | 2025-07-30 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 281 | GBP | 2023-10-31 | 2024-07-29 | filed | no | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 281 | GBP | 2023-10-31 | 2025-07-30 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 4852 | GBP | 2023-10-31 | 2024-07-29 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | -4852 | GBP | 2023-10-31 | 2025-07-30 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -4893 | GBP | 2023-10-31 | 2025-07-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 5133 | GBP | 2023-10-31 | 2024-07-29 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -4612 | GBP | 2023-10-31 | 2025-07-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 4852 | GBP | 2023-10-31 | 2024-07-29 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2022-10-31 | 2024-07-29 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 4664 | GBP | 2022-10-31 | 2024-07-29 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 0 | GBP | 2022-10-31 | 2024-07-29 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 4289 | GBP | 2022-10-31 | 2024-07-29 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 375 | GBP | 2022-10-31 | 2024-07-29 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 4289 | GBP | 2022-10-31 | 2024-07-29 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 4664 | GBP | 2022-10-31 | 2024-07-29 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 4289 | GBP | 2022-10-31 | 2024-07-29 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2025-07-30: `{"superseded_document_id": "gb:03454073:doc:nNFtLcgRL2D4FsJjjzarG4ty6OE0G30Vcm5MA1wb3DY", "restatements": [{"concept": "creditors_within_one_year", "period_end": "2023-10-31", "old_value": "5137.0000"`

## HUNTER-FLEMING LIMITED (`gb:03720556`)

- registration: `03720556` (GB), status active, incorporated 1999-02-25
- classification: ['86102'] (sic_2007)
- records: 22 officers, 1 beneficial owners, 0 ownership statements, 6 security interests, 159 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | iso4217:GBP | 2024-12-31 | 2025-09-24 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 2740000 | GBP | 2024-12-31 | 2025-09-24 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 3429 | GBP | 2024-12-31 | 2025-09-24 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 26650 | GBP | 2024-12-31 | 2025-09-24 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 2719921 | GBP | 2024-12-31 | 2025-09-24 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 2719921 | GBP | 2024-12-31 | 2025-09-24 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 24079 | GBP | 2024-12-31 | 2025-09-24 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 24079 | GBP | 2024-12-31 | 2025-09-24 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2023-12-31 | 2025-09-24 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2023-12-31 | 2024-09-16 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 2715000 | GBP | 2023-12-31 | 2025-09-24 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 2715000 | GBP | 2023-12-31 | 2024-09-16 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 3399 | GBP | 2023-12-31 | 2024-09-16 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 3399 | GBP | 2023-12-31 | 2025-09-24 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 28646 | GBP | 2023-12-31 | 2024-09-16 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 28646 | GBP | 2023-12-31 | 2025-09-24 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 2692920 | GBP | 2023-12-31 | 2025-09-24 | filed | yes | `uk-core:Equity` | micro-entity |
| equity | 2692920 | GBP | 2023-12-31 | 2024-09-16 | filed | no | `uk-core:Equity` | micro-entity |
| net_assets | 2692920 | GBP | 2023-12-31 | 2024-09-16 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 2692920 | GBP | 2023-12-31 | 2025-09-24 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 26080 | GBP | 2023-12-31 | 2025-09-24 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 26080 | GBP | 2023-12-31 | 2024-09-16 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 26080 | GBP | 2023-12-31 | 2025-09-24 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 26080 | GBP | 2023-12-31 | 2024-09-16 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2022-12-31 | 2023-09-28 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2022-12-31 | 2024-09-16 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 2665000 | GBP | 2022-12-31 | 2024-09-16 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 2665000 | GBP | 2022-12-31 | 2023-09-28 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 944 | GBP | 2022-12-31 | 2024-09-16 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 944 | GBP | 2022-12-31 | 2023-09-28 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 3144 | GBP | 2022-12-31 | 2023-09-28 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 3144 | GBP | 2022-12-31 | 2024-09-16 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 2666014 | GBP | 2022-12-31 | 2023-09-28 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 2666014 | GBP | 2022-12-31 | 2024-09-16 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 2666014 | GBP | 2022-12-31 | 2023-09-28 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 2666014 | GBP | 2022-12-31 | 2024-09-16 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 2986 | GBP | 2022-12-31 | 2023-09-28 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 2986 | GBP | 2022-12-31 | 2024-09-16 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 2986 | GBP | 2022-12-31 | 2024-09-16 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 2986 | GBP | 2022-12-31 | 2023-09-28 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2021-12-31 | 2023-09-28 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 2645000 | GBP | 2021-12-31 | 2023-09-28 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1559 | GBP | 2021-12-31 | 2023-09-28 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 10302 | GBP | 2021-12-31 | 2023-09-28 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 2639613 | GBP | 2021-12-31 | 2023-09-28 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 2639613 | GBP | 2021-12-31 | 2023-09-28 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 9387 | GBP | 2021-12-31 | 2023-09-28 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 9387 | GBP | 2021-12-31 | 2023-09-28 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## CSSL LTD (`gb:03996773`)

- registration: `03996773` (GB), status active, incorporated 2000-05-18
- classification: ['62012', '62020', '86220'] (sic_2007)
- records: 9 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 103 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-03-31 | 2025-08-04 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 36316 | GBP | 2025-03-31 | 2025-08-04 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 57504 | GBP | 2025-03-31 | 2025-08-04 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 21188 | GBP | 2025-03-31 | 2025-08-04 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 97340 | GBP | 2025-03-31 | 2025-08-04 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 60111 | GBP | 2025-03-31 | 2025-08-04 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2025-03-31 | 2025-08-04 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 121330 | GBP | 2025-03-31 | 2025-08-04 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 158451 | GBP | 2025-03-31 | 2025-08-04 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 38545 | GBP | 2025-03-31 | 2025-08-04 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 159875 | GBP | 2025-03-31 | 2025-08-04 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | iso4217:GBP | 2024-03-31 | 2025-05-29 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-03-31 | 2025-08-04 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 3770 | GBP | 2024-03-31 | 2025-08-04 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 4088 | GBP | 2024-03-31 | 2025-05-29 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 12988 | GBP | 2024-03-31 | 2025-05-29 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 15941 | GBP | 2024-03-31 | 2025-05-29 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 15941 | GBP | 2024-03-31 | 2025-08-04 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 12171 | GBP | 2024-03-31 | 2025-08-04 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity | 92518 | GBP | 2024-03-31 | 2025-05-29 | filed | yes | `uk-core:Equity` | micro-entity |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 19316 | GBP | 2024-03-31 | 2025-08-04 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2024-03-31 | 2025-08-04 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 72202 | GBP | 2024-03-31 | 2025-08-04 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 95818 | GBP | 2024-03-31 | 2025-08-04 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| fixed_assets | 95818 | GBP | 2024-03-31 | 2025-05-29 | filed | no | `uk-core:FixedAssets` | micro-entity |
| net_assets | 92518 | GBP | 2024-03-31 | 2025-08-04 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 92518 | GBP | 2024-03-31 | 2025-05-29 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 788 | GBP | 2024-03-31 | 2025-08-04 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 2953 | GBP | 2024-03-31 | 2025-05-29 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 96606 | GBP | 2024-03-31 | 2025-08-04 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 98771 | GBP | 2024-03-31 | 2025-05-29 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2023-05-31 | 2025-05-29 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2023-05-31 | 2025-05-29 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 25460 | GBP | 2023-05-31 | 2025-05-29 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 17685 | GBP | 2023-05-31 | 2025-05-29 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 56528 | GBP | 2023-05-31 | 2025-05-29 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 67343 | GBP | 2023-05-31 | 2025-05-29 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 56528 | GBP | 2023-05-31 | 2025-05-29 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 7775 | GBP | 2023-05-31 | 2025-05-29 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 59568 | GBP | 2023-05-31 | 2025-05-29 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2025-08-04: `{"superseded_document_id": "gb:03996773:doc:WKIojbrEMySYTBgW8OfCt3ZWtj-3eGHSN5T8pPIFFeI", "restatements": [{"concept": "net_current_assets", "period_end": "2024-03-31", "old_value": "2953.0000", "new_`

## MH LOGISTICS ENGINEERING LIMITED (`gb:04280322`)

- registration: `04280322` (GB), status active, incorporated 2001-09-03
- classification: ['71122', '71129'] (sic_2007)
- records: 5 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 67 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-03-31 | 2025-12-15 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 26296 | GBP | 2025-03-31 | 2025-12-15 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 44792 | GBP | 2025-03-31 | 2025-12-15 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 20321 | GBP | 2025-03-31 | 2025-12-15 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 4974 | GBP | 2025-03-31 | 2025-12-15 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 20321 | GBP | 2025-03-31 | 2025-12-15 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 18496 | GBP | 2025-03-31 | 2025-12-15 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 23470 | GBP | 2025-03-31 | 2025-12-15 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-03-31 | 2025-12-15 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-03-31 | 2024-12-31 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 32618 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 32618 | GBP | 2024-03-31 | 2025-12-15 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 59961 | GBP | 2024-03-31 | 2025-12-15 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 59961 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 26560 | GBP | 2024-03-31 | 2025-12-15 | filed | yes | `core:Equity` | micro-entity |
| equity | 26560 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 5766 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 5766 | GBP | 2024-03-31 | 2025-12-15 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 26560 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 26560 | GBP | 2024-03-31 | 2025-12-15 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 27343 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 27343 | GBP | 2024-03-31 | 2025-12-15 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 33109 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 33109 | GBP | 2024-03-31 | 2025-12-15 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-03-31 | 2024-12-31 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-03-31 | 2023-12-21 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 34039 | GBP | 2023-03-31 | 2023-12-21 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 31943 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 65073 | GBP | 2023-03-31 | 2023-12-21 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 65072 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 33492 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `core:Equity` | micro-entity |
| equity | 33492 | GBP | 2023-03-31 | 2023-12-21 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 2459 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 2458 | GBP | 2023-03-31 | 2023-12-21 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | 33492 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 33129 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 35588 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2022-03-31 | 2023-12-21 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 43346 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 56064 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 13967 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 1249 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `core:FixedAssets` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2024-12-31: `{"superseded_document_id": "gb:04280322:doc:pJJtD4TxaVmCtBwtZPriOdQY3a3LhKrVgUEbqHyQWSI", "restatements": [{"concept": "fixed_assets", "period_end": "2023-03-31", "old_value": "2458.0000", "new_value"`

## HORIZONTAL AND VERTICAL LTD (`gb:04567342`)

- registration: `04567342` (GB), status active, incorporated 2002-10-18
- classification: ['62020'] (sic_2007)
- records: 5 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 58 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-03-31 | 2025-12-10 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 7635 | GBP | 2025-03-31 | 2025-12-10 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity | -7045 | GBP | 2025-03-31 | 2025-12-10 | filed | yes | `ns5:Equity` | micro-entity |
| net_assets | -7045 | GBP | 2025-03-31 | 2025-12-10 | filed | yes | `ns5:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -5905 | GBP | 2025-03-31 | 2025-12-10 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -5905 | GBP | 2025-03-31 | 2025-12-10 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-03-31 | 2025-12-10 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-03-31 | 2024-12-16 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 28089 | GBP | 2024-03-31 | 2024-12-16 | filed | no | `ns5:CurrentAssets` | micro-entity |
| current_assets | 28089 | GBP | 2024-03-31 | 2025-12-10 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity | 1068 | GBP | 2024-03-31 | 2025-12-10 | filed | yes | `ns5:Equity` | micro-entity |
| equity | 1068 | GBP | 2024-03-31 | 2024-12-16 | filed | no | `ns5:Equity` | micro-entity |
| net_assets | 1068 | GBP | 2024-03-31 | 2025-12-10 | filed | yes | `ns5:NetAssetsLiabilities` | micro-entity |
| net_assets | 1068 | GBP | 2024-03-31 | 2024-12-16 | filed | no | `ns5:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 2168 | GBP | 2024-03-31 | 2025-12-10 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 2168 | GBP | 2024-03-31 | 2024-12-16 | filed | no | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 2168 | GBP | 2024-03-31 | 2024-12-16 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 2168 | GBP | 2024-03-31 | 2025-12-10 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 1 | xbrli:pure | 2023-03-31 | 2023-12-14 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-03-31 | 2024-12-16 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 4699 | GBP | 2023-03-31 | 2024-12-16 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 4699 | GBP | 2023-03-31 | 2023-12-14 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | -12826 | GBP | 2023-03-31 | 2023-12-14 | filed | yes | `ns5:Equity` | micro-entity |
| equity | -12826 | GBP | 2023-03-31 | 2024-12-16 | filed | yes | `ns5:Equity` | micro-entity |
| net_assets `{'OriginalRevisedDataDimension': 'Original'}` | -12826 | GBP | 2023-03-31 | 2023-12-14 | filed | yes | `ns5:NetAssetsLiabilities` | micro-entity |
| net_assets | -12826 | GBP | 2023-03-31 | 2024-12-16 | filed | yes | `ns5:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -11926 | GBP | 2023-03-31 | 2024-12-16 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | -11926 | GBP | 2023-03-31 | 2023-12-14 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | -11926 | GBP | 2023-03-31 | 2023-12-14 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -11926 | GBP | 2023-03-31 | 2024-12-16 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 1 | xbrli:pure | 2022-03-31 | 2023-12-14 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 24014 | GBP | 2022-03-31 | 2023-12-14 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 3114 | GBP | 2022-03-31 | 2023-12-14 | filed | yes | `ns5:Equity` | micro-entity |
| net_assets `{'OriginalRevisedDataDimension': 'Original'}` | 3114 | GBP | 2022-03-31 | 2023-12-14 | filed | yes | `ns5:NetAssetsLiabilities` | micro-entity |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 4014 | GBP | 2022-03-31 | 2023-12-14 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 4014 | GBP | 2022-03-31 | 2023-12-14 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## RENNER LTD (`gb:04861045`)

- registration: `04861045` (GB), status active, incorporated 2003-08-08
- classification: ['35110', '36000', '62020', '69202'] (sic_2007)
- records: 5 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 92 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | iso4217:GBP | 2023-06-30 | 2024-05-29 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 10838 | GBP | 2023-06-30 | 2024-05-29 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2162 | GBP | 2023-06-30 | 2024-05-29 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 10825 | GBP | 2023-06-30 | 2024-05-29 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 5447 | GBP | 2023-06-30 | 2024-05-29 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 7622 | GBP | 2023-06-30 | 2024-05-29 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 5447 | GBP | 2023-06-30 | 2024-05-29 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 8663 | GBP | 2023-06-30 | 2024-05-29 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 16285 | GBP | 2023-06-30 | 2024-05-29 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2022-06-30 | 2024-05-29 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2022-06-30 | 2023-03-31 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 12951 | GBP | 2022-06-30 | 2024-05-29 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 12951 | GBP | 2022-06-30 | 2023-03-31 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2022-06-30 | 2024-05-29 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 4250 | GBP | 2022-06-30 | 2024-05-29 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 4250 | GBP | 2022-06-30 | 2023-03-31 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | 594 | GBP | 2022-06-30 | 2024-05-29 | filed | yes | `uk-core:Equity` | micro-entity |
| equity | 594 | GBP | 2022-06-30 | 2023-03-31 | filed | no | `uk-core:Equity` | micro-entity |
| fixed_assets | 9295 | GBP | 2022-06-30 | 2024-05-29 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 9295 | GBP | 2022-06-30 | 2023-03-31 | filed | no | `uk-core:FixedAssets` | micro-entity |
| net_assets | 594 | GBP | 2022-06-30 | 2023-03-31 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 594 | GBP | 2022-06-30 | 2024-05-29 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 4250 | GBP | 2022-06-30 | 2024-05-29 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 4250 | GBP | 2022-06-30 | 2023-03-31 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 13545 | GBP | 2022-06-30 | 2024-05-29 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 13545 | GBP | 2022-06-30 | 2023-03-31 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2021-06-30 | 2022-06-20 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2021-06-30 | 2023-03-31 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 12852 | GBP | 2021-06-30 | 2023-03-31 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 12852 | GBP | 2021-06-30 | 2022-06-20 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 5727 | GBP | 2021-06-30 | 2022-06-20 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 5727 | GBP | 2021-06-30 | 2023-03-31 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 552 | GBP | 2021-06-30 | 2023-03-31 | filed | yes | `uk-core:Equity` | micro-entity |
| equity | 552 | GBP | 2021-06-30 | 2022-06-20 | filed | no | `uk-core:Equity` | micro-entity |
| fixed_assets | 7677 | GBP | 2021-06-30 | 2022-06-20 | filed | no | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 7677 | GBP | 2021-06-30 | 2023-03-31 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 552 | GBP | 2021-06-30 | 2023-03-31 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 552 | GBP | 2021-06-30 | 2022-06-20 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 5727 | GBP | 2021-06-30 | 2023-03-31 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 5727 | GBP | 2021-06-30 | 2022-06-20 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 13404 | GBP | 2021-06-30 | 2023-03-31 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 13404 | GBP | 2021-06-30 | 2022-06-20 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2020-06-30 | 2022-06-20 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 9000 | GBP | 2020-06-30 | 2022-06-20 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 6425 | GBP | 2020-06-30 | 2022-06-20 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 2925 | GBP | 2020-06-30 | 2022-06-20 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 5500 | GBP | 2020-06-30 | 2022-06-20 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 2925 | GBP | 2020-06-30 | 2022-06-20 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 6425 | GBP | 2020-06-30 | 2022-06-20 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 11925 | GBP | 2020-06-30 | 2022-06-20 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._
