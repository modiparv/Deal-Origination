# Ingest spot-check

- database: `data/engine.db`
- latest run: `20261109T091757Z-41eb4d4d`
- companies in store: 47400; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## HEALTH CARE DESIGN LIMITED (`gb:02724336`)

- registration: `02724336` (GB), status active, incorporated 1992-06-19
- classification: ['71111'] (sic_2007)
- records: 7 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 91 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 3 | xbrli:pure | 2026-04-30 | 2026-08-27 | filed | yes | `d:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 601657 | GBP | 2026-04-30 | 2026-08-27 | filed | yes | `d:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 43324 | GBP | 2026-04-30 | 2026-08-27 | filed | yes | `d:Creditors` | total-exemption-full |
| current_assets | 661638 | GBP | 2026-04-30 | 2026-08-27 | filed | yes | `d:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 59981 | GBP | 2026-04-30 | 2026-08-27 | filed | yes | `d:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 620155 | GBP | 2026-04-30 | 2026-08-27 | filed | yes | `d:Equity` | total-exemption-full |
| equity | 620395 | GBP | 2026-04-30 | 2026-08-27 | filed | yes | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 240 | GBP | 2026-04-30 | 2026-08-27 | filed | yes | `d:Equity` | total-exemption-full |
| fixed_assets | 2775 | GBP | 2026-04-30 | 2026-08-27 | filed | yes | `d:FixedAssets` | total-exemption-full |
| net_assets | 620395 | GBP | 2026-04-30 | 2026-08-27 | filed | yes | `d:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 618314 | GBP | 2026-04-30 | 2026-08-27 | filed | yes | `d:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 621089 | GBP | 2026-04-30 | 2026-08-27 | filed | yes | `d:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 3 | xbrli:pure | 2025-04-30 | 2025-10-22 | filed | no | `d:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 3 | xbrli:pure | 2025-04-30 | 2026-08-27 | filed | yes | `d:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 925474 | GBP | 2025-04-30 | 2025-10-22 | filed | no | `d:CashBankOnHand` | total-exemption-full |
| cash | 925474 | GBP | 2025-04-30 | 2026-08-27 | filed | yes | `d:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 135858 | GBP | 2025-04-30 | 2026-08-27 | filed | yes | `d:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 135858 | GBP | 2025-04-30 | 2025-10-22 | filed | no | `d:Creditors` | total-exemption-full |
| current_assets | 1004187 | GBP | 2025-04-30 | 2026-08-27 | filed | yes | `d:CurrentAssets` | total-exemption-full |
| current_assets | 1004187 | GBP | 2025-04-30 | 2025-10-22 | filed | no | `d:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 78713 | GBP | 2025-04-30 | 2025-10-22 | filed | no | `d:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 78713 | GBP | 2025-04-30 | 2026-08-27 | filed | yes | `d:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 240 | GBP | 2025-04-30 | 2026-08-27 | filed | yes | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 240 | GBP | 2025-04-30 | 2025-10-22 | filed | no | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 868484 | GBP | 2025-04-30 | 2026-08-27 | filed | yes | `d:Equity` | total-exemption-full |
| equity | 868724 | GBP | 2025-04-30 | 2026-08-27 | filed | yes | `d:Equity` | total-exemption-full |
| equity | 868724 | GBP | 2025-04-30 | 2025-10-22 | filed | no | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 868484 | GBP | 2025-04-30 | 2025-10-22 | filed | no | `d:Equity` | total-exemption-full |
| fixed_assets | 527 | GBP | 2025-04-30 | 2025-10-22 | filed | no | `d:FixedAssets` | total-exemption-full |
| fixed_assets | 527 | GBP | 2025-04-30 | 2026-08-27 | filed | yes | `d:FixedAssets` | total-exemption-full |
| net_assets | 868724 | GBP | 2025-04-30 | 2025-10-22 | filed | no | `d:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 868724 | GBP | 2025-04-30 | 2026-08-27 | filed | yes | `d:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 868329 | GBP | 2025-04-30 | 2025-10-22 | filed | no | `d:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 868329 | GBP | 2025-04-30 | 2026-08-27 | filed | yes | `d:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 868856 | GBP | 2025-04-30 | 2026-08-27 | filed | yes | `d:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 868856 | GBP | 2025-04-30 | 2025-10-22 | filed | no | `d:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-04-30 | 2025-01-24 | filed | no | `d:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-04-30 | 2025-10-22 | filed | yes | `d:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 992774 | GBP | 2024-04-30 | 2025-01-24 | filed | no | `d:CashBankOnHand` | total-exemption-full |
| cash | 992774 | GBP | 2024-04-30 | 2025-10-22 | filed | yes | `d:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 162110 | GBP | 2024-04-30 | 2025-10-22 | filed | yes | `d:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 162110 | GBP | 2024-04-30 | 2025-01-24 | filed | no | `d:Creditors` | total-exemption-full |
| current_assets | 1097122 | GBP | 2024-04-30 | 2025-10-22 | filed | yes | `d:CurrentAssets` | total-exemption-full |
| current_assets | 1097122 | GBP | 2024-04-30 | 2025-01-24 | filed | no | `d:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 104348 | GBP | 2024-04-30 | 2025-10-22 | filed | yes | `d:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 104348 | GBP | 2024-04-30 | 2025-01-24 | filed | no | `d:Debtors` | total-exemption-full |
| equity | 935556 | GBP | 2024-04-30 | 2025-10-22 | filed | yes | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 240 | GBP | 2024-04-30 | 2025-01-24 | filed | no | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 935316 | GBP | 2024-04-30 | 2025-10-22 | filed | yes | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 935316 | GBP | 2024-04-30 | 2025-01-24 | filed | no | `d:Equity` | total-exemption-full |
| equity | 935556 | GBP | 2024-04-30 | 2025-01-24 | filed | no | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 240 | GBP | 2024-04-30 | 2025-10-22 | filed | yes | `d:Equity` | total-exemption-full |
| fixed_assets | 672 | GBP | 2024-04-30 | 2025-01-24 | filed | no | `d:FixedAssets` | total-exemption-full |
| fixed_assets | 672 | GBP | 2024-04-30 | 2025-10-22 | filed | yes | `d:FixedAssets` | total-exemption-full |
| net_assets | 935556 | GBP | 2024-04-30 | 2025-01-24 | filed | no | `d:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 935556 | GBP | 2024-04-30 | 2025-10-22 | filed | yes | `d:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 935012 | GBP | 2024-04-30 | 2025-01-24 | filed | no | `d:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 935012 | GBP | 2024-04-30 | 2025-10-22 | filed | yes | `d:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 935684 | GBP | 2024-04-30 | 2025-01-24 | filed | no | `d:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 935684 | GBP | 2024-04-30 | 2025-10-22 | filed | yes | `d:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-04-30 | 2025-01-24 | filed | yes | `d:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 880239 | GBP | 2023-04-30 | 2025-01-24 | filed | yes | `d:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 169215 | GBP | 2023-04-30 | 2025-01-24 | filed | yes | `d:Creditors` | total-exemption-full |
| current_assets | 1077851 | GBP | 2023-04-30 | 2025-01-24 | filed | yes | `d:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 197612 | GBP | 2023-04-30 | 2025-01-24 | filed | yes | `d:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 240 | GBP | 2023-04-30 | 2025-01-24 | filed | yes | `d:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 909345 | GBP | 2023-04-30 | 2025-01-24 | filed | yes | `d:Equity` | total-exemption-full |
| equity | 909585 | GBP | 2023-04-30 | 2025-01-24 | filed | yes | `d:Equity` | total-exemption-full |
| fixed_assets | 1172 | GBP | 2023-04-30 | 2025-01-24 | filed | yes | `d:FixedAssets` | total-exemption-full |
| net_assets | 909585 | GBP | 2023-04-30 | 2025-01-24 | filed | yes | `d:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 908636 | GBP | 2023-04-30 | 2025-01-24 | filed | yes | `d:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 909808 | GBP | 2023-04-30 | 2025-01-24 | filed | yes | `d:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## SHED K.M. LIMITED (`gb:03395362`)

- registration: `03395362` (GB), status active, incorporated 1997-07-01
- classification: ['71111'] (sic_2007)
- records: 13 officers, 1 beneficial owners, 0 ownership statements, 3 security interests, 103 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.38 | xbrli:pure | 2025-06-30 | 2026-03-13 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 1513397 | GBP | 2025-06-30 | 2026-03-13 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1029088 | GBP | 2025-06-30 | 2026-03-13 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 3644446 | GBP | 2025-06-30 | 2026-03-13 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 2131049 | GBP | 2025-06-30 | 2026-03-13 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1150 | GBP | 2025-06-30 | 2026-03-13 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2671257 | GBP | 2025-06-30 | 2026-03-13 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 12150 | GBP | 2025-06-30 | 2026-03-13 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 2684557 | GBP | 2025-06-30 | 2026-03-13 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 92265 | GBP | 2025-06-30 | 2026-03-13 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | 2684557 | GBP | 2025-06-30 | 2026-03-13 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 2615358 | GBP | 2025-06-30 | 2026-03-13 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 2707623 | GBP | 2025-06-30 | 2026-03-13 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 32 | xbrli:pure | 2024-06-30 | 2024-09-06 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 0.37 | xbrli:pure | 2024-06-30 | 2026-03-13 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 1098329 | GBP | 2024-06-30 | 2026-03-13 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 1098329 | GBP | 2024-06-30 | 2024-09-06 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 492887 | GBP | 2024-06-30 | 2026-03-13 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 3098176 | GBP | 2024-06-30 | 2024-09-06 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 3098175 | GBP | 2024-06-30 | 2026-03-13 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1999847 | GBP | 2024-06-30 | 2024-09-06 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 1999846 | GBP | 2024-06-30 | 2026-03-13 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 1999847 | GBP | 2024-06-30 | 2024-09-06 | filed | no | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1150 | GBP | 2024-06-30 | 2024-09-06 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2681112 | GBP | 2024-06-30 | 2026-03-13 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 12150 | GBP | 2024-06-30 | 2026-03-13 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 12150 | GBP | 2024-06-30 | 2024-09-06 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 2694412 | GBP | 2024-06-30 | 2026-03-13 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1150 | GBP | 2024-06-30 | 2026-03-13 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2681112 | GBP | 2024-06-30 | 2024-09-06 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 2694412 | GBP | 2024-06-30 | 2024-09-06 | filed | no | `ns5:Equity` | total-exemption-full |
| fixed_assets | 89124 | GBP | 2024-06-30 | 2026-03-13 | filed | yes | `core:FixedAssets` | total-exemption-full |
| fixed_assets | 89123 | GBP | 2024-06-30 | 2024-09-06 | filed | no | `ns5:FixedAssets` | total-exemption-full |
| net_assets | 2694412 | GBP | 2024-06-30 | 2026-03-13 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 2605289 | GBP | 2024-06-30 | 2024-09-06 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 2605288 | GBP | 2024-06-30 | 2026-03-13 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 2694412 | GBP | 2024-06-30 | 2026-03-13 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 2694412 | GBP | 2024-06-30 | 2024-09-06 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 43 | xbrli:pure | 2023-06-30 | 2024-06-28 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 43 | xbrli:pure | 2023-06-30 | 2024-09-06 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 723258 | GBP | 2023-06-30 | 2024-09-06 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 723258 | GBP | 2023-06-30 | 2024-06-28 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 2346247 | GBP | 2023-06-30 | 2024-06-28 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 2346247 | GBP | 2023-06-30 | 2024-09-06 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 1622989 | GBP | 2023-06-30 | 2024-09-06 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 1622989 | GBP | 2023-06-30 | 2024-06-28 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1622989 | GBP | 2023-06-30 | 2024-06-28 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1622989 | GBP | 2023-06-30 | 2024-09-06 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1150 | GBP | 2023-06-30 | 2024-09-06 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 2061316 | GBP | 2023-06-30 | 2024-06-28 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1150 | GBP | 2023-06-30 | 2024-06-28 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 2061316 | GBP | 2023-06-30 | 2024-09-06 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2048016 | GBP | 2023-06-30 | 2024-06-28 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 12150 | GBP | 2023-06-30 | 2024-06-28 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2048016 | GBP | 2023-06-30 | 2024-09-06 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 12150 | GBP | 2023-06-30 | 2024-09-06 | filed | yes | `ns5:Equity` | total-exemption-full |
| fixed_assets | 98292 | GBP | 2023-06-30 | 2024-09-06 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| fixed_assets | 98292 | GBP | 2023-06-30 | 2024-06-28 | filed | no | `ns5:FixedAssets` | total-exemption-full |
| net_assets | 2061316 | GBP | 2023-06-30 | 2024-06-28 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1963024 | GBP | 2023-06-30 | 2024-06-28 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1963024 | GBP | 2023-06-30 | 2024-09-06 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 2061316 | GBP | 2023-06-30 | 2024-09-06 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 2061316 | GBP | 2023-06-30 | 2024-06-28 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 49 | xbrli:pure | 2022-06-30 | 2024-06-28 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 1246560 | GBP | 2022-06-30 | 2024-06-28 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 3333039 | GBP | 2022-06-30 | 2024-06-28 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 1956479 | GBP | 2022-06-30 | 2024-06-28 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1956479 | GBP | 2022-06-30 | 2024-06-28 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 12150 | GBP | 2022-06-30 | 2024-06-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1150 | GBP | 2022-06-30 | 2024-06-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2982477 | GBP | 2022-06-30 | 2024-06-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 2995777 | GBP | 2022-06-30 | 2024-06-28 | filed | yes | `ns5:Equity` | total-exemption-full |
| fixed_assets | 96569 | GBP | 2022-06-30 | 2024-06-28 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| net_assets | 2995777 | GBP | 2022-06-30 | 2024-06-28 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 2904722 | GBP | 2022-06-30 | 2024-06-28 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 3001291 | GBP | 2022-06-30 | 2024-06-28 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2026-03-13: `{"superseded_document_id": "gb:03395362:doc:eKw0iwqIXHmjVRiIOuUG4VyqAYmVXGjrm1P159h8pOY", "restatements": [{"concept": "fixed_assets", "period_end": "2024-06-30", "old_value": "89123.0000", "new_value`

## CODE GLOBAL LIMITED (`gb:03911730`)

- registration: `03911730` (GB), status active, incorporated 2000-01-21
- classification: ['62090'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 71 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-12-31 | 2026-05-05 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 27266 | GBP | 2025-12-31 | 2026-05-05 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity | 102 | GBP | 2025-12-31 | 2026-05-05 | filed | yes | `ns5:Equity` | micro-entity |
| fixed_assets | 895 | GBP | 2025-12-31 | 2026-05-05 | filed | yes | `ns5:FixedAssets` | micro-entity |
| net_assets | 102 | GBP | 2025-12-31 | 2026-05-05 | filed | yes | `ns5:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 15803 | GBP | 2025-12-31 | 2026-05-05 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 16698 | GBP | 2025-12-31 | 2026-05-05 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-12-31 | 2026-05-05 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-12-31 | 2025-07-30 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 29461 | GBP | 2024-12-31 | 2026-05-05 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| current_assets | 29461 | GBP | 2024-12-31 | 2025-07-30 | filed | no | `ns5:CurrentAssets` | micro-entity |
| equity | 100 | GBP | 2024-12-31 | 2026-05-05 | filed | yes | `ns5:Equity` | micro-entity |
| equity | 100 | GBP | 2024-12-31 | 2025-07-30 | filed | no | `ns5:Equity` | micro-entity |
| fixed_assets | 1193 | GBP | 2024-12-31 | 2025-07-30 | filed | no | `ns5:FixedAssets` | micro-entity |
| fixed_assets | 1193 | GBP | 2024-12-31 | 2026-05-05 | filed | yes | `ns5:FixedAssets` | micro-entity |
| net_assets | 100 | GBP | 2024-12-31 | 2025-07-30 | filed | no | `ns5:NetAssetsLiabilities` | micro-entity |
| net_assets | 100 | GBP | 2024-12-31 | 2026-05-05 | filed | yes | `ns5:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 18939 | GBP | 2024-12-31 | 2026-05-05 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 18939 | GBP | 2024-12-31 | 2025-07-30 | filed | no | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 20132 | GBP | 2024-12-31 | 2025-07-30 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 20132 | GBP | 2024-12-31 | 2026-05-05 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-12-31 | 2024-04-19 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-12-31 | 2025-07-30 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 37218 | GBP | 2023-12-31 | 2025-07-30 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| current_assets | 37218 | GBP | 2023-12-31 | 2024-04-19 | filed | no | `ns5:CurrentAssets` | micro-entity |
| equity | 120 | GBP | 2023-12-31 | 2025-07-30 | filed | yes | `ns5:Equity` | micro-entity |
| equity | 120 | GBP | 2023-12-31 | 2024-04-19 | filed | no | `ns5:Equity` | micro-entity |
| fixed_assets | 1619 | GBP | 2023-12-31 | 2025-07-30 | filed | yes | `ns5:FixedAssets` | micro-entity |
| fixed_assets | 1619 | GBP | 2023-12-31 | 2024-04-19 | filed | no | `ns5:FixedAssets` | micro-entity |
| net_assets | 120 | GBP | 2023-12-31 | 2025-07-30 | filed | yes | `ns5:NetAssetsLiabilities` | micro-entity |
| net_assets | 120 | GBP | 2023-12-31 | 2024-04-19 | filed | no | `ns5:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 21887 | GBP | 2023-12-31 | 2024-04-19 | filed | no | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 21887 | GBP | 2023-12-31 | 2025-07-30 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 23506 | GBP | 2023-12-31 | 2025-07-30 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 23506 | GBP | 2023-12-31 | 2024-04-19 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2022-12-31 | 2024-04-19 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 38083 | GBP | 2022-12-31 | 2024-04-19 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity | 110 | GBP | 2022-12-31 | 2024-04-19 | filed | yes | `ns5:Equity` | micro-entity |
| fixed_assets | 1769 | GBP | 2022-12-31 | 2024-04-19 | filed | yes | `ns5:FixedAssets` | micro-entity |
| net_assets | 110 | GBP | 2022-12-31 | 2024-04-19 | filed | yes | `ns5:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 23653 | GBP | 2022-12-31 | 2024-04-19 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 25422 | GBP | 2022-12-31 | 2024-04-19 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## TSE (IT) SERVICES LIMITED (`gb:04437454`)

- registration: `04437454` (GB), status active, incorporated 2002-05-13
- classification: ['62020'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 59 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.01 | xbrli:pure | 2026-05-31 | 2026-07-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 10600 | GBP | 2026-05-31 | 2026-07-30 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 18333 | GBP | 2026-05-31 | 2026-07-30 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 8621 | GBP | 2026-05-31 | 2026-07-30 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 888 | GBP | 2026-05-31 | 2026-07-30 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 8621 | GBP | 2026-05-31 | 2026-07-30 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 7733 | GBP | 2026-05-31 | 2026-07-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 8621 | GBP | 2026-05-31 | 2026-07-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0.01 | xbrli:pure | 2025-05-31 | 2026-07-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2025-05-31 | 2025-07-31 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 13704 | GBP | 2025-05-31 | 2026-07-30 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 13704 | GBP | 2025-05-31 | 2025-07-31 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 20690 | GBP | 2025-05-31 | 2025-07-31 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 20690 | GBP | 2025-05-31 | 2026-07-30 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 6986 | GBP | 2025-05-31 | 2025-07-31 | filed | no | `core:Equity` | micro-entity |
| equity | 6986 | GBP | 2025-05-31 | 2026-07-30 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2025-05-31 | 2026-07-30 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 6986 | GBP | 2025-05-31 | 2026-07-30 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 6986 | GBP | 2025-05-31 | 2025-07-31 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 6986 | GBP | 2025-05-31 | 2026-07-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 6986 | GBP | 2025-05-31 | 2025-07-31 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 6986 | GBP | 2025-05-31 | 2026-07-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 6986 | GBP | 2025-05-31 | 2025-07-31 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-05-31 | 2025-07-31 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 9460 | GBP | 2024-05-31 | 2025-07-31 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 12215 | GBP | 2024-05-31 | 2025-07-31 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 2755 | GBP | 2024-05-31 | 2025-07-31 | filed | yes | `core:Equity` | micro-entity |
| net_assets | 2755 | GBP | 2024-05-31 | 2025-07-31 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 2755 | GBP | 2024-05-31 | 2025-07-31 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 2755 | GBP | 2024-05-31 | 2025-07-31 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-05-24 | 2024-08-14 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 10384 | GBP | 2024-05-24 | 2024-08-14 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 28111 | GBP | 2024-05-24 | 2024-08-14 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 17727 | GBP | 2024-05-24 | 2024-08-14 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 17727 | GBP | 2024-05-24 | 2024-08-14 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 17727 | GBP | 2024-05-24 | 2024-08-14 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 17727 | GBP | 2024-05-24 | 2024-08-14 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-05-31 | 2024-08-14 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 12380 | GBP | 2023-05-31 | 2024-08-14 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 28517 | GBP | 2023-05-31 | 2024-08-14 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 16137 | GBP | 2023-05-31 | 2024-08-14 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 16137 | GBP | 2023-05-31 | 2024-08-14 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 16137 | GBP | 2023-05-31 | 2024-08-14 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 16137 | GBP | 2023-05-31 | 2024-08-14 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2026-07-30: `{"superseded_document_id": "gb:04437454:doc:OnncLr39MUH5Qpd8PCW5LpTtYbjGCUzdbXpfhB6qWpQ", "restatements": [{"concept": "average_employees", "period_end": "2025-05-31", "old_value": "1.0000", "new_valu`

## ROLEMS UK LIMITED (`gb:04986655`)

- registration: `04986655` (GB), status active, incorporated 2003-12-05
- classification: ['62030'] (sic_2007)
- records: 3 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 54 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | iso4217:GBP | 2024-12-31 | 2025-04-14 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 7101 | GBP | 2024-12-31 | 2025-04-14 | filed | yes | `core:Creditors` | micro-entity |
| equity | -4757 | GBP | 2024-12-31 | 2025-04-14 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 288 | GBP | 2024-12-31 | 2025-04-14 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | -4757 | GBP | 2024-12-31 | 2025-04-14 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -5045 | GBP | 2024-12-31 | 2025-04-14 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| profit_for_period | -5850 | GBP | 2024-12-31 | 2025-04-14 | filed | yes | `core:ProfitLoss` | micro-entity |
| staff_costs | 7850 | GBP | 2024-12-31 | 2025-04-14 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | micro-entity |
| total_assets_less_current_liabilities | -4757 | GBP | 2024-12-31 | 2025-04-14 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-12-31 | 2024-01-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 6552 | GBP | 2023-12-31 | 2025-04-14 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 6552 | GBP | 2023-12-31 | 2024-01-30 | filed | no | `core:Creditors` | micro-entity |
| equity | -5351 | GBP | 2023-12-31 | 2024-01-30 | filed | no | `core:Equity` | micro-entity |
| equity | -5351 | GBP | 2023-12-31 | 2025-04-14 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 164 | GBP | 2023-12-31 | 2025-04-14 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 164 | GBP | 2023-12-31 | 2024-01-30 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | -5351 | GBP | 2023-12-31 | 2025-04-14 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | -5351 | GBP | 2023-12-31 | 2024-01-30 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -5515 | GBP | 2023-12-31 | 2024-01-30 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -5515 | GBP | 2023-12-31 | 2025-04-14 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| profit_for_period | -7245 | GBP | 2023-12-31 | 2024-01-30 | filed | no | `core:ProfitLoss` | micro-entity |
| profit_for_period | -7245 | GBP | 2023-12-31 | 2025-04-14 | filed | yes | `core:ProfitLoss` | micro-entity |
| revenue | 6490 | GBP | 2023-12-31 | 2024-01-30 | filed | yes | `core:TurnoverRevenue` | micro-entity |
| staff_costs | 11285 | GBP | 2023-12-31 | 2025-04-14 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | micro-entity |
| staff_costs | 11285 | GBP | 2023-12-31 | 2024-01-30 | filed | no | `core:StaffCostsEmployeeBenefitsExpense` | micro-entity |
| total_assets_less_current_liabilities | -5351 | GBP | 2023-12-31 | 2025-04-14 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -5351 | GBP | 2023-12-31 | 2024-01-30 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2022-12-31 | 2023-01-29 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5562 | GBP | 2022-12-31 | 2023-01-29 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5562 | GBP | 2022-12-31 | 2024-01-30 | filed | yes | `core:Creditors` | micro-entity |
| equity | -4312 | GBP | 2022-12-31 | 2023-01-29 | filed | no | `core:Equity` | micro-entity |
| equity | -4312 | GBP | 2022-12-31 | 2024-01-30 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 564 | GBP | 2022-12-31 | 2023-01-29 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 564 | GBP | 2022-12-31 | 2024-01-30 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | -4312 | GBP | 2022-12-31 | 2024-01-30 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | -4312 | GBP | 2022-12-31 | 2023-01-29 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -4876 | GBP | 2022-12-31 | 2023-01-29 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -4876 | GBP | 2022-12-31 | 2024-01-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| profit_for_period | -5489 | GBP | 2022-12-31 | 2024-01-30 | filed | yes | `core:ProfitLoss` | micro-entity |
| profit_for_period | -5489 | GBP | 2022-12-31 | 2023-01-29 | filed | no | `core:ProfitLoss` | micro-entity |
| revenue | 10817 | GBP | 2022-12-31 | 2023-01-29 | filed | no | `core:TurnoverRevenue` | micro-entity |
| revenue | 10817 | GBP | 2022-12-31 | 2024-01-30 | filed | yes | `core:TurnoverRevenue` | micro-entity |
| staff_costs | 9721 | GBP | 2022-12-31 | 2023-01-29 | filed | no | `core:StaffCostsEmployeeBenefitsExpense` | micro-entity |
| staff_costs | 9721 | GBP | 2022-12-31 | 2024-01-30 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | micro-entity |
| total_assets_less_current_liabilities | -4312 | GBP | 2022-12-31 | 2024-01-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -4312 | GBP | 2022-12-31 | 2023-01-29 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5144 | GBP | 2021-12-31 | 2023-01-29 | filed | yes | `core:Creditors` | micro-entity |
| equity | -4519 | GBP | 2021-12-31 | 2023-01-29 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 288 | GBP | 2021-12-31 | 2023-01-29 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | -4519 | GBP | 2021-12-31 | 2023-01-29 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -4807 | GBP | 2021-12-31 | 2023-01-29 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| profit_for_period | -3683 | GBP | 2021-12-31 | 2023-01-29 | filed | yes | `core:ProfitLoss` | micro-entity |
| revenue | 11984 | GBP | 2021-12-31 | 2023-01-29 | filed | yes | `core:TurnoverRevenue` | micro-entity |
| staff_costs | 8348 | GBP | 2021-12-31 | 2023-01-29 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | micro-entity |
| total_assets_less_current_liabilities | -4519 | GBP | 2021-12-31 | 2023-01-29 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## PMZ CONSULTING SERVICES LIMITED (`gb:05507363`)

- registration: `05507363` (GB), status active, incorporated 2005-07-13
- classification: ['62011'] (sic_2007)
- records: 3 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 64 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-07-31 | 2025-10-02 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 27334 | GBP | 2025-07-31 | 2025-10-02 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 27401 | GBP | 2025-07-31 | 2025-10-02 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 67 | GBP | 2025-07-31 | 2025-10-02 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2025-07-31 | 2025-10-02 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 27986 | GBP | 2025-07-31 | 2025-10-02 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 723 | GBP | 2025-07-31 | 2025-10-02 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 27987 | GBP | 2025-07-31 | 2025-10-02 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 27401 | GBP | 2025-07-31 | 2025-10-02 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 28124 | GBP | 2025-07-31 | 2025-10-02 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-07-31 | 2025-10-02 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-07-31 | 2024-09-10 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 45311 | GBP | 2024-07-31 | 2024-09-10 | filed | no | `frs-core:CashBankOnHand` | total-exemption-full |
| cash | 45311 | GBP | 2024-07-31 | 2025-10-02 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 45377 | GBP | 2024-07-31 | 2024-09-10 | filed | no | `frs-core:CurrentAssets` | total-exemption-full |
| current_assets | 45377 | GBP | 2024-07-31 | 2025-10-02 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 66 | GBP | 2024-07-31 | 2025-10-02 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| debtors | 66 | GBP | 2024-07-31 | 2024-09-10 | filed | no | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 46792 | GBP | 2024-07-31 | 2024-09-10 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2024-07-31 | 2024-09-10 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 46792 | GBP | 2024-07-31 | 2025-10-02 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2024-07-31 | 2025-10-02 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 1748 | GBP | 2024-07-31 | 2025-10-02 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| fixed_assets | 1748 | GBP | 2024-07-31 | 2024-09-10 | filed | no | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 46793 | GBP | 2024-07-31 | 2025-10-02 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 46793 | GBP | 2024-07-31 | 2024-09-10 | filed | no | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 45377 | GBP | 2024-07-31 | 2024-09-10 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 45377 | GBP | 2024-07-31 | 2025-10-02 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 47125 | GBP | 2024-07-31 | 2025-10-02 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 47125 | GBP | 2024-07-31 | 2024-09-10 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-07-31 | 2023-11-30 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-07-31 | 2024-09-10 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 77714 | GBP | 2023-07-31 | 2024-09-10 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| cash | 77714 | GBP | 2023-07-31 | 2023-11-30 | filed | no | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 78763 | GBP | 2023-07-31 | 2023-11-30 | filed | no | `frs-core:CurrentAssets` | total-exemption-full |
| current_assets | 78763 | GBP | 2023-07-31 | 2024-09-10 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 1049 | GBP | 2023-07-31 | 2024-09-10 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| debtors | 1049 | GBP | 2023-07-31 | 2023-11-30 | filed | no | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2023-07-31 | 2024-09-10 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2023-07-31 | 2023-11-30 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 81146 | GBP | 2023-07-31 | 2024-09-10 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 81146 | GBP | 2023-07-31 | 2023-11-30 | filed | no | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 2945 | GBP | 2023-07-31 | 2023-11-30 | filed | no | `frs-core:FixedAssets` | total-exemption-full |
| fixed_assets | 2945 | GBP | 2023-07-31 | 2024-09-10 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 81147 | GBP | 2023-07-31 | 2023-11-30 | filed | no | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 81147 | GBP | 2023-07-31 | 2024-09-10 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 78762 | GBP | 2023-07-31 | 2024-09-10 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 78762 | GBP | 2023-07-31 | 2023-11-30 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 81707 | GBP | 2023-07-31 | 2024-09-10 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 81707 | GBP | 2023-07-31 | 2023-11-30 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2022-07-31 | 2023-11-30 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 100086 | GBP | 2022-07-31 | 2023-11-30 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 101487 | GBP | 2022-07-31 | 2023-11-30 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 1401 | GBP | 2022-07-31 | 2023-11-30 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 103215 | GBP | 2022-07-31 | 2023-11-30 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2022-07-31 | 2023-11-30 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 3075 | GBP | 2022-07-31 | 2023-11-30 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 103216 | GBP | 2022-07-31 | 2023-11-30 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 100725 | GBP | 2022-07-31 | 2023-11-30 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 103800 | GBP | 2022-07-31 | 2023-11-30 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## MURPHY GEOSPATIAL UK LTD (`gb:06012484`)

- registration: `06012484` (GB), status active, incorporated 2006-11-28
- classification: ['71122'] (sic_2007)
- records: 15 officers, 5 beneficial owners, 0 ownership statements, 4 security interests, 106 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 169 | xbrli:pure | 2023-12-31 | 2024-12-05 | filed | yes | `c:AverageNumberEmployeesDuringPeriod` | full |
| cash | 1868560 | GBP | 2023-12-31 | 2024-12-05 | filed | yes | `c:CashBankOnHand` | full |
| current_assets | 6943911 | GBP | 2023-12-31 | 2024-12-05 | filed | yes | `c:CurrentAssets` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 5075351 | GBP | 2023-12-31 | 2024-12-05 | filed | yes | `c:Debtors` | full |
| equity | 3249838 | GBP | 2023-12-31 | 2024-12-05 | filed | yes | `c:Equity` | full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 22616 | GBP | 2023-12-31 | 2024-12-05 | filed | yes | `c:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3226221 | GBP | 2023-12-31 | 2024-12-05 | filed | yes | `c:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1001 | GBP | 2023-12-31 | 2024-12-05 | filed | yes | `c:Equity` | full |
| fixed_assets | 1207813 | GBP | 2023-12-31 | 2024-12-05 | filed | yes | `c:FixedAssets` | full |
| gross_profit | 8892836 | GBP | 2023-12-31 | 2024-12-05 | filed | yes | `c:GrossProfitLoss` | full |
| net_assets | 3249838 | GBP | 2023-12-31 | 2024-12-05 | filed | yes | `c:NetAssetsLiabilities` | full |
| net_current_assets | 2549252 | GBP | 2023-12-31 | 2024-12-05 | filed | yes | `c:NetCurrentAssetsLiabilities` | full |
| operating_profit | 2517689 | GBP | 2023-12-31 | 2024-12-05 | filed | yes | `c:OperatingProfitLoss` | full |
| profit_before_tax | 2474910 | GBP | 2023-12-31 | 2024-12-05 | filed | yes | `c:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period | 2001482 | GBP | 2023-12-31 | 2024-12-05 | filed | yes | `c:ProfitLoss` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2001482 | GBP | 2023-12-31 | 2024-12-05 | filed | yes | `c:ProfitLoss` | full |
| revenue | 18519550 | GBP | 2023-12-31 | 2024-12-05 | filed | yes | `c:TurnoverRevenue` | full |
| staff_costs | 8693731 | GBP | 2023-12-31 | 2024-12-05 | filed | yes | `c:StaffCostsEmployeeBenefitsExpense` | full |
| tax_charge | 473428 | GBP | 2023-12-31 | 2024-12-05 | filed | yes | `c:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| total_assets_less_current_liabilities | 3757065 | GBP | 2023-12-31 | 2024-12-05 | filed | yes | `c:TotalAssetsLessCurrentLiabilities` | full |
| average_employees | 137 | xbrli:pure | 2022-12-31 | 2024-12-05 | filed | yes | `c:AverageNumberEmployeesDuringPeriod` | full |
| cash | 663665 | GBP | 2022-12-31 | 2024-12-05 | filed | yes | `c:CashBankOnHand` | full |
| current_assets | 3816524 | GBP | 2022-12-31 | 2024-12-05 | filed | yes | `c:CurrentAssets` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 3152859 | GBP | 2022-12-31 | 2024-12-05 | filed | yes | `c:Debtors` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1001 | GBP | 2022-12-31 | 2024-12-05 | filed | yes | `c:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1224739 | GBP | 2022-12-31 | 2024-12-05 | filed | yes | `c:Equity` | full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 22616 | GBP | 2022-12-31 | 2024-12-05 | filed | yes | `c:Equity` | full |
| equity | 1248356 | GBP | 2022-12-31 | 2024-12-05 | filed | yes | `c:Equity` | full |
| fixed_assets | 689921 | GBP | 2022-12-31 | 2024-12-05 | filed | yes | `c:FixedAssets` | full |
| gross_profit | 5322576 | GBP | 2022-12-31 | 2024-12-05 | filed | yes | `c:GrossProfitLoss` | full |
| net_assets | 1248356 | GBP | 2022-12-31 | 2024-12-05 | filed | yes | `c:NetAssetsLiabilities` | full |
| net_current_assets | 822254 | GBP | 2022-12-31 | 2024-12-05 | filed | yes | `c:NetCurrentAssetsLiabilities` | full |
| operating_profit | 115589 | GBP | 2022-12-31 | 2024-12-05 | filed | yes | `c:OperatingProfitLoss` | full |
| profit_before_tax | 54595 | GBP | 2022-12-31 | 2024-12-05 | filed | yes | `c:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period | 21250 | GBP | 2022-12-31 | 2024-12-05 | filed | yes | `c:ProfitLoss` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 21250 | GBP | 2022-12-31 | 2024-12-05 | filed | yes | `c:ProfitLoss` | full |
| revenue | 12185392 | GBP | 2022-12-31 | 2024-12-05 | filed | yes | `c:TurnoverRevenue` | full |
| staff_costs | 6475766 | GBP | 2022-12-31 | 2024-12-05 | filed | yes | `c:StaffCostsEmployeeBenefitsExpense` | full |
| tax_charge | 33345 | GBP | 2022-12-31 | 2024-12-05 | filed | yes | `c:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| total_assets_less_current_liabilities | 1512175 | GBP | 2022-12-31 | 2024-12-05 | filed | yes | `c:TotalAssetsLessCurrentLiabilities` | full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 22616 | GBP | 2022-01-01 | 2024-12-05 | filed | yes | `c:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1001 | GBP | 2022-01-01 | 2024-12-05 | filed | yes | `c:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1203489 | GBP | 2022-01-01 | 2024-12-05 | filed | yes | `c:Equity` | full |
| equity | 1227106 | GBP | 2022-01-01 | 2024-12-05 | filed | yes | `c:Equity` | full |

_No coverage facts for the latest run._

## MG FOLLON DESIGN SERVICES LTD (`gb:06427700`)

- registration: `06427700` (GB), status active, incorporated 2007-11-14
- classification: ['71122'] (sic_2007)
- records: 3 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 43 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.02 | xbrli:pure | 2025-11-30 | 2026-03-20 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 26625 | GBP | 2025-11-30 | 2026-03-20 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5586 | GBP | 2025-11-30 | 2026-03-20 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 28644 | GBP | 2025-11-30 | 2026-03-20 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2019 | GBP | 2025-11-30 | 2026-03-20 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 2019 | GBP | 2025-11-30 | 2026-03-20 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200 | GBP | 2025-11-30 | 2026-03-20 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 23058 | GBP | 2025-11-30 | 2026-03-20 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 22858 | GBP | 2025-11-30 | 2026-03-20 | filed | yes | `core:Equity` | total-exemption-full |
| net_current_assets | 23058 | GBP | 2025-11-30 | 2026-03-20 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| average_employees | 0.02 | xbrli:pure | 2024-11-30 | 2026-03-20 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-11-30 | 2025-02-17 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 21251 | GBP | 2024-11-30 | 2025-02-17 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 21251 | GBP | 2024-11-30 | 2026-03-20 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5267 | GBP | 2024-11-30 | 2026-03-20 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5267 | GBP | 2024-11-30 | 2025-02-17 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 24296 | GBP | 2024-11-30 | 2026-03-20 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 24296 | GBP | 2024-11-30 | 2025-02-17 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 3045 | GBP | 2024-11-30 | 2026-03-20 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 3045 | GBP | 2024-11-30 | 2026-03-20 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 3045 | GBP | 2024-11-30 | 2025-02-17 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 3045 | GBP | 2024-11-30 | 2025-02-17 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 18829 | GBP | 2024-11-30 | 2025-02-17 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200 | GBP | 2024-11-30 | 2026-03-20 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 19029 | GBP | 2024-11-30 | 2025-02-17 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200 | GBP | 2024-11-30 | 2025-02-17 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 18829 | GBP | 2024-11-30 | 2026-03-20 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 19029 | GBP | 2024-11-30 | 2026-03-20 | filed | yes | `core:Equity` | total-exemption-full |
| net_current_assets | 19029 | GBP | 2024-11-30 | 2025-02-17 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 19029 | GBP | 2024-11-30 | 2026-03-20 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-11-30 | 2024-03-25 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-11-30 | 2025-02-17 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 15180 | GBP | 2023-11-30 | 2024-03-25 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 15180 | GBP | 2023-11-30 | 2025-02-17 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 4439 | GBP | 2023-11-30 | 2024-03-25 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 4439 | GBP | 2023-11-30 | 2025-02-17 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 16050 | GBP | 2023-11-30 | 2024-03-25 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 16050 | GBP | 2023-11-30 | 2025-02-17 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 870 | GBP | 2023-11-30 | 2025-02-17 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 870 | GBP | 2023-11-30 | 2025-02-17 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 870 | GBP | 2023-11-30 | 2024-03-25 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 870 | GBP | 2023-11-30 | 2024-03-25 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 11411 | GBP | 2023-11-30 | 2025-02-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 11611 | GBP | 2023-11-30 | 2025-02-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 11611 | GBP | 2023-11-30 | 2024-03-25 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200 | GBP | 2023-11-30 | 2024-03-25 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200 | GBP | 2023-11-30 | 2025-02-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 11411 | GBP | 2023-11-30 | 2024-03-25 | filed | no | `core:Equity` | total-exemption-full |
| net_current_assets | 11611 | GBP | 2023-11-30 | 2025-02-17 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 11611 | GBP | 2023-11-30 | 2024-03-25 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_for_period | 13965 | GBP | 2023-11-30 | 2024-03-25 | filed | yes | `core:ProfitLoss` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 13965 | GBP | 2023-11-30 | 2024-03-25 | filed | yes | `core:ProfitLoss` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2022-11-30 | 2024-03-25 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 17171 | GBP | 2022-11-30 | 2024-03-25 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 4764 | GBP | 2022-11-30 | 2024-03-25 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 18460 | GBP | 2022-11-30 | 2024-03-25 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1289 | GBP | 2022-11-30 | 2024-03-25 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 1289 | GBP | 2022-11-30 | 2024-03-25 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 13696 | GBP | 2022-11-30 | 2024-03-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 13496 | GBP | 2022-11-30 | 2024-03-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200 | GBP | 2022-11-30 | 2024-03-25 | filed | yes | `core:Equity` | total-exemption-full |
| net_current_assets | 13696 | GBP | 2022-11-30 | 2024-03-25 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_for_period | 15245 | GBP | 2022-11-30 | 2024-03-25 | filed | yes | `core:ProfitLoss` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 15245 | GBP | 2022-11-30 | 2024-03-25 | filed | yes | `core:ProfitLoss` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 11551 | GBP | 2021-11-30 | 2024-03-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200 | GBP | 2021-11-30 | 2024-03-25 | filed | yes | `core:Equity` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2026-03-20: `{"superseded_document_id": "gb:06427700:doc:hGb4Qjb5YlDpnSck9c1t-r_v3Xj29G-jUFP2VC2ai60", "restatements": [{"concept": "average_employees", "period_end": "2024-11-30", "old_value": "2.0000", "new_valu`

## MATTHEW COLLIN CONSULTING LTD (`gb:06856040`)

- registration: `06856040` (GB), status active, incorporated 2009-03-23
- classification: ['71122'] (sic_2007)
- records: 1 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 37 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | iso4217:GBP | 2025-03-23 | 2025-12-23 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2025-03-23 | 2025-12-23 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 15000 | GBP | 2025-03-23 | 2025-12-23 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 38136 | GBP | 2025-03-23 | 2025-12-23 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 23296 | GBP | 2025-03-23 | 2025-12-23 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 160 | GBP | 2025-03-23 | 2025-12-23 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 23296 | GBP | 2025-03-23 | 2025-12-23 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 23136 | GBP | 2025-03-23 | 2025-12-23 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 23296 | GBP | 2025-03-23 | 2025-12-23 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-03-23 | 2025-12-23 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-03-23 | 2024-12-23 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2024-03-23 | 2024-12-23 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2024-03-23 | 2025-12-23 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 15000 | GBP | 2024-03-23 | 2025-12-23 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 15000 | GBP | 2024-03-23 | 2024-12-23 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 33955 | GBP | 2024-03-23 | 2025-12-23 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 33955 | GBP | 2024-03-23 | 2024-12-23 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | 19078 | GBP | 2024-03-23 | 2025-12-23 | filed | yes | `uk-core:Equity` | micro-entity |
| equity | 19078 | GBP | 2024-03-23 | 2024-12-23 | filed | no | `uk-core:Equity` | micro-entity |
| fixed_assets | 123 | GBP | 2024-03-23 | 2025-12-23 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 123 | GBP | 2024-03-23 | 2024-12-23 | filed | no | `uk-core:FixedAssets` | micro-entity |
| net_assets | 19078 | GBP | 2024-03-23 | 2024-12-23 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 19078 | GBP | 2024-03-23 | 2025-12-23 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 18955 | GBP | 2024-03-23 | 2024-12-23 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 18955 | GBP | 2024-03-23 | 2025-12-23 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 19078 | GBP | 2024-03-23 | 2025-12-23 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 19078 | GBP | 2024-03-23 | 2024-12-23 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-03-23 | 2023-12-23 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-03-23 | 2024-12-23 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2023-03-23 | 2023-12-23 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2023-03-23 | 2024-12-23 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 15000 | GBP | 2023-03-23 | 2024-12-23 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 15000 | GBP | 2023-03-23 | 2023-12-23 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 25097 | GBP | 2023-03-23 | 2023-12-23 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 25097 | GBP | 2023-03-23 | 2024-12-23 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 10362 | GBP | 2023-03-23 | 2023-12-23 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 10362 | GBP | 2023-03-23 | 2024-12-23 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 265 | GBP | 2023-03-23 | 2024-12-23 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 265 | GBP | 2023-03-23 | 2023-12-23 | filed | no | `uk-core:FixedAssets` | micro-entity |
| net_assets | 10362 | GBP | 2023-03-23 | 2024-12-23 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 10362 | GBP | 2023-03-23 | 2023-12-23 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 10097 | GBP | 2023-03-23 | 2024-12-23 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 10097 | GBP | 2023-03-23 | 2023-12-23 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 10362 | GBP | 2023-03-23 | 2023-12-23 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 10362 | GBP | 2023-03-23 | 2024-12-23 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2022-03-23 | 2023-12-23 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2022-03-23 | 2023-12-23 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 30000 | GBP | 2022-03-23 | 2023-12-23 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 43171 | GBP | 2022-03-23 | 2023-12-23 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 14969 | GBP | 2022-03-23 | 2023-12-23 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 1798 | GBP | 2022-03-23 | 2023-12-23 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 14969 | GBP | 2022-03-23 | 2023-12-23 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 13171 | GBP | 2022-03-23 | 2023-12-23 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 14969 | GBP | 2022-03-23 | 2023-12-23 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._
