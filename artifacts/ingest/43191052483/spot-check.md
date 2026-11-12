# Ingest spot-check

- database: `data/engine.db`
- latest run: `20261112T092422Z-e24bba0e`
- companies in store: 49800; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## ENOTRAC UK LIMITED (`gb:02766532`)

- registration: `02766532` (GB), status active, incorporated 1992-11-20
- classification: ['62090', '71122', '74909'] (sic_2007)
- records: 8 officers, 2 beneficial owners, 1 ownership statements, 2 security interests, 93 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 9 | xbrli:pure | 2024-12-31 | 2025-08-27 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 230502 | GBP | 2024-12-31 | 2025-08-27 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 200000 | GBP | 2024-12-31 | 2025-08-27 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 637596 | GBP | 2024-12-31 | 2025-08-27 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 435838 | GBP | 2024-12-31 | 2025-08-27 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 205336 | GBP | 2024-12-31 | 2025-08-27 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | -390299 | GBP | 2024-12-31 | 2025-08-27 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -400299 | GBP | 2024-12-31 | 2025-08-27 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10000 | GBP | 2024-12-31 | 2025-08-27 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | -390299 | GBP | 2024-12-31 | 2025-08-27 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -201758 | GBP | 2024-12-31 | 2025-08-27 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -190299 | GBP | 2024-12-31 | 2025-08-27 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 9 | xbrli:pure | 2023-12-31 | 2024-08-22 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 9 | xbrli:pure | 2023-12-31 | 2025-08-27 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 108777 | GBP | 2023-12-31 | 2025-08-27 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 108777 | GBP | 2023-12-31 | 2024-08-22 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 280000 | GBP | 2023-12-31 | 2025-08-27 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 742043 | GBP | 2023-12-31 | 2025-08-27 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 569416 | GBP | 2023-12-31 | 2025-08-27 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 569416 | GBP | 2023-12-31 | 2024-08-22 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 460639 | GBP | 2023-12-31 | 2024-08-22 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 460639 | GBP | 2023-12-31 | 2025-08-27 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 460639 | GBP | 2023-12-31 | 2024-08-22 | filed | no | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -451370 | GBP | 2023-12-31 | 2024-08-22 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10000 | GBP | 2023-12-31 | 2025-08-27 | filed | yes | `core:Equity` | total-exemption-full |
| equity | -441370 | GBP | 2023-12-31 | 2024-08-22 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10000 | GBP | 2023-12-31 | 2024-08-22 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -451370 | GBP | 2023-12-31 | 2025-08-27 | filed | yes | `core:Equity` | total-exemption-full |
| equity | -441370 | GBP | 2023-12-31 | 2025-08-27 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | -441370 | GBP | 2023-12-31 | 2025-08-27 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | -441370 | GBP | 2023-12-31 | 2024-08-22 | filed | no | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -172627 | GBP | 2023-12-31 | 2024-08-22 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -172627 | GBP | 2023-12-31 | 2025-08-27 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -161370 | GBP | 2023-12-31 | 2024-08-22 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -161370 | GBP | 2023-12-31 | 2025-08-27 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 7 | xbrli:pure | 2022-12-31 | 2024-08-22 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 7 | xbrli:pure | 2022-12-31 | 2023-09-26 | filed | no | `ns6:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 78853 | GBP | 2022-12-31 | 2023-09-26 | filed | no | `ns6:CashBankOnHand` | total-exemption-full |
| cash | 78853 | GBP | 2022-12-31 | 2024-08-22 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 688288 | GBP | 2022-12-31 | 2023-09-26 | filed | no | `ns6:CurrentAssets` | total-exemption-full |
| current_assets | 688288 | GBP | 2022-12-31 | 2024-08-22 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 609435 | GBP | 2022-12-31 | 2024-08-22 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 609435 | GBP | 2022-12-31 | 2024-08-22 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 609435 | GBP | 2022-12-31 | 2023-09-26 | filed | no | `ns6:Debtors` | total-exemption-full |
| debtors | 609435 | GBP | 2022-12-31 | 2023-09-26 | filed | no | `ns6:Debtors` | total-exemption-full |
| equity | -509209 | GBP | 2022-12-31 | 2024-08-22 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -519209 | GBP | 2022-12-31 | 2023-09-26 | filed | no | `ns6:Equity` | total-exemption-full |
| equity | -509209 | GBP | 2022-12-31 | 2023-09-26 | filed | no | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -519209 | GBP | 2022-12-31 | 2024-08-22 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10000 | GBP | 2022-12-31 | 2024-08-22 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10000 | GBP | 2022-12-31 | 2023-09-26 | filed | no | `ns6:Equity` | total-exemption-full |
| net_assets | -509209 | GBP | 2022-12-31 | 2024-08-22 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | -509209 | GBP | 2022-12-31 | 2023-09-26 | filed | no | `ns6:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -195474 | GBP | 2022-12-31 | 2024-08-22 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -195474 | GBP | 2022-12-31 | 2023-09-26 | filed | no | `ns6:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -189209 | GBP | 2022-12-31 | 2024-08-22 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -189209 | GBP | 2022-12-31 | 2023-09-26 | filed | no | `ns6:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 7 | xbrli:pure | 2021-12-31 | 2023-09-26 | filed | yes | `ns6:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 94049 | GBP | 2021-12-31 | 2023-09-26 | filed | yes | `ns6:CashBankOnHand` | total-exemption-full |
| current_assets | 411851 | GBP | 2021-12-31 | 2023-09-26 | filed | yes | `ns6:CurrentAssets` | total-exemption-full |
| debtors | 317802 | GBP | 2021-12-31 | 2023-09-26 | filed | yes | `ns6:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 317802 | GBP | 2021-12-31 | 2023-09-26 | filed | yes | `ns6:Debtors` | total-exemption-full |
| equity | -498086 | GBP | 2021-12-31 | 2023-09-26 | filed | yes | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10000 | GBP | 2021-12-31 | 2023-09-26 | filed | yes | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -508086 | GBP | 2021-12-31 | 2023-09-26 | filed | yes | `ns6:Equity` | total-exemption-full |
| net_assets | -498086 | GBP | 2021-12-31 | 2023-09-26 | filed | yes | `ns6:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -102917 | GBP | 2021-12-31 | 2023-09-26 | filed | yes | `ns6:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -98086 | GBP | 2021-12-31 | 2023-09-26 | filed | yes | `ns6:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## KALEIDA LIMITED (`gb:03448831`)

- registration: `03448831` (GB), status active, incorporated 1997-10-13
- classification: ['62090'] (sic_2007)
- records: 7 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 97 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 7 | xbrli:pure | 2025-10-31 | 2026-09-08 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 57592 | GBP | 2025-10-31 | 2026-09-08 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 39280 | GBP | 2025-10-31 | 2026-09-08 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 341281 | GBP | 2025-10-31 | 2026-09-08 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 339752 | GBP | 2025-10-31 | 2026-09-08 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 282160 | GBP | 2025-10-31 | 2026-09-08 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | -37190 | GBP | 2025-10-31 | 2026-09-08 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'OtherReservesSubtotal'}` | 52 | GBP | 2025-10-31 | 2026-09-08 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -37290 | GBP | 2025-10-31 | 2026-09-08 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 48 | GBP | 2025-10-31 | 2026-09-08 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 52 | GBP | 2025-10-31 | 2026-09-08 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 3619 | GBP | 2025-10-31 | 2026-09-08 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | -37190 | GBP | 2025-10-31 | 2026-09-08 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -1529 | GBP | 2025-10-31 | 2026-09-08 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 2090 | GBP | 2025-10-31 | 2026-09-08 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 52 | GBP | 2024-11-01 | 2026-09-08 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'OtherReservesSubtotal'}` | 52 | GBP | 2024-11-01 | 2026-09-08 | filed | yes | `core:Equity` | total-exemption-full |
| average_employees | 7 | xbrli:pure | 2024-10-31 | 2026-09-08 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 7 | xbrli:pure | 2024-10-31 | 2025-07-21 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 7894 | GBP | 2024-10-31 | 2026-09-08 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 7894 | GBP | 2024-10-31 | 2025-07-21 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 66002 | GBP | 2024-10-31 | 2025-07-21 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 66002 | GBP | 2024-10-31 | 2026-09-08 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 231033 | GBP | 2024-10-31 | 2026-09-08 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 231033 | GBP | 2024-10-31 | 2025-07-21 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 243636 | GBP | 2024-10-31 | 2026-09-08 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 243636 | GBP | 2024-10-31 | 2025-07-21 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors | 235742 | GBP | 2024-10-31 | 2025-07-21 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 235742 | GBP | 2024-10-31 | 2026-09-08 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 48 | GBP | 2024-10-31 | 2025-07-21 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -48173 | GBP | 2024-10-31 | 2025-07-21 | filed | no | `core:Equity` | total-exemption-full |
| equity | -48073 | GBP | 2024-10-31 | 2026-09-08 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -48173 | GBP | 2024-10-31 | 2026-09-08 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 48 | GBP | 2024-10-31 | 2026-09-08 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 52 | GBP | 2024-10-31 | 2026-09-08 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 52 | GBP | 2024-10-31 | 2025-07-21 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'OtherReservesSubtotal'}` | 52 | GBP | 2024-10-31 | 2025-07-21 | filed | yes | `core:Equity` | total-exemption-full |
| equity | -48073 | GBP | 2024-10-31 | 2025-07-21 | filed | no | `core:Equity` | total-exemption-full |
| fixed_assets | 5326 | GBP | 2024-10-31 | 2025-07-21 | filed | no | `core:FixedAssets` | total-exemption-full |
| fixed_assets | 5326 | GBP | 2024-10-31 | 2026-09-08 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | -48073 | GBP | 2024-10-31 | 2025-07-21 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | -48073 | GBP | 2024-10-31 | 2026-09-08 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 12603 | GBP | 2024-10-31 | 2025-07-21 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 12603 | GBP | 2024-10-31 | 2026-09-08 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 17929 | GBP | 2024-10-31 | 2026-09-08 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 17929 | GBP | 2024-10-31 | 2025-07-21 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 52 | GBP | 2023-11-01 | 2026-09-08 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'OtherReservesSubtotal'}` | 52 | GBP | 2023-11-01 | 2026-09-08 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 52 | GBP | 2023-11-01 | 2025-07-21 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'OtherReservesSubtotal'}` | 52 | GBP | 2023-11-01 | 2025-07-21 | filed | no | `core:Equity` | total-exemption-full |
| average_employees | 7 | xbrli:pure | 2023-10-31 | 2025-07-21 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 7 | xbrli:pure | 2023-10-31 | 2024-07-31 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 35064 | GBP | 2023-10-31 | 2025-07-21 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 35064 | GBP | 2023-10-31 | 2024-07-31 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 100576 | GBP | 2023-10-31 | 2024-07-31 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 100576 | GBP | 2023-10-31 | 2025-07-21 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 191739 | GBP | 2023-10-31 | 2024-07-31 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 225567 | GBP | 2023-10-31 | 2025-07-21 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 212017 | GBP | 2023-10-31 | 2025-07-21 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 178189 | GBP | 2023-10-31 | 2024-07-31 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors | 176953 | GBP | 2023-10-31 | 2025-07-21 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 143125 | GBP | 2023-10-31 | 2024-07-31 | filed | no | `core:Debtors` | total-exemption-full |
| equity | -106278 | GBP | 2023-10-31 | 2025-07-21 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'OtherReservesSubtotal'}` | 52 | GBP | 2023-10-31 | 2024-07-31 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 52 | GBP | 2023-10-31 | 2024-07-31 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -106378 | GBP | 2023-10-31 | 2024-07-31 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 48 | GBP | 2023-10-31 | 2025-07-21 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 48 | GBP | 2023-10-31 | 2024-07-31 | filed | no | `core:Equity` | total-exemption-full |
| equity | -106278 | GBP | 2023-10-31 | 2024-07-31 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -106378 | GBP | 2023-10-31 | 2025-07-21 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 52 | GBP | 2023-10-31 | 2025-07-21 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 7848 | GBP | 2023-10-31 | 2024-07-31 | filed | no | `core:FixedAssets` | total-exemption-full |
| fixed_assets | 7848 | GBP | 2023-10-31 | 2025-07-21 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | -106278 | GBP | 2023-10-31 | 2025-07-21 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | -106278 | GBP | 2023-10-31 | 2024-07-31 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -13550 | GBP | 2023-10-31 | 2024-07-31 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -13550 | GBP | 2023-10-31 | 2025-07-21 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -5702 | GBP | 2023-10-31 | 2025-07-21 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -5702 | GBP | 2023-10-31 | 2024-07-31 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 52 | GBP | 2022-11-01 | 2025-07-21 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 52 | GBP | 2022-11-01 | 2024-07-31 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'OtherReservesSubtotal'}` | 52 | GBP | 2022-11-01 | 2024-07-31 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'OtherReservesSubtotal'}` | 52 | GBP | 2022-11-01 | 2025-07-21 | filed | yes | `core:Equity` | total-exemption-full |
| average_employees | 6 | xbrli:pure | 2022-10-31 | 2024-07-31 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 13982 | GBP | 2022-10-31 | 2024-07-31 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 136818 | GBP | 2022-10-31 | 2024-07-31 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 247515 | GBP | 2022-10-31 | 2024-07-31 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 169208 | GBP | 2022-10-31 | 2024-07-31 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 155226 | GBP | 2022-10-31 | 2024-07-31 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -199970 | GBP | 2022-10-31 | 2024-07-31 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 48 | GBP | 2022-10-31 | 2024-07-31 | filed | yes | `core:Equity` | total-exemption-full |
| equity | -199870 | GBP | 2022-10-31 | 2024-07-31 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 52 | GBP | 2022-10-31 | 2024-07-31 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 15255 | GBP | 2022-10-31 | 2024-07-31 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | -199870 | GBP | 2022-10-31 | 2024-07-31 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -78307 | GBP | 2022-10-31 | 2024-07-31 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -63052 | GBP | 2022-10-31 | 2024-07-31 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 52 | GBP | 2021-11-01 | 2024-07-31 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'OtherReservesSubtotal'}` | 52 | GBP | 2021-11-01 | 2024-07-31 | filed | yes | `core:Equity` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2025-07-21: `{"superseded_document_id": "gb:03448831:doc:NE170WWiWQUCu7gOGO7eT6lOEQ_TBN3-uqhRw617g40", "restatements": [{"concept": "debtors", "period_end": "2023-10-31", "old_value": "143125.0000", "new_value": "`

## SSD CONSULTANTS LIMITED (`gb:03984862`)

- registration: `03984862` (GB), status active, incorporated 2000-05-03
- classification: ['62020'] (sic_2007)
- records: 5 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 68 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2026-05-31 | 2026-09-07 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 31007 | GBP | 2026-05-31 | 2026-09-07 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 318140 | GBP | 2026-05-31 | 2026-09-07 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 287721 | GBP | 2026-05-31 | 2026-09-07 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 1169 | GBP | 2026-05-31 | 2026-09-07 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 287721 | GBP | 2026-05-31 | 2026-09-07 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 287133 | GBP | 2026-05-31 | 2026-09-07 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 288302 | GBP | 2026-05-31 | 2026-09-07 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2025-05-31 | 2026-09-07 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2025-05-31 | 2026-01-05 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 33502 | GBP | 2025-05-31 | 2026-09-07 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 33502 | GBP | 2025-05-31 | 2026-01-05 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 313850 | GBP | 2025-05-31 | 2026-01-05 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 313850 | GBP | 2025-05-31 | 2026-09-07 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 281771 | GBP | 2025-05-31 | 2026-09-07 | filed | yes | `core:Equity` | micro-entity |
| equity | 281771 | GBP | 2025-05-31 | 2026-01-05 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 1423 | GBP | 2025-05-31 | 2026-09-07 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 1423 | GBP | 2025-05-31 | 2026-01-05 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | 281771 | GBP | 2025-05-31 | 2026-09-07 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 281771 | GBP | 2025-05-31 | 2026-01-05 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 280348 | GBP | 2025-05-31 | 2026-09-07 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 280348 | GBP | 2025-05-31 | 2026-01-05 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 281771 | GBP | 2025-05-31 | 2026-01-05 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 281771 | GBP | 2025-05-31 | 2026-09-07 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-05-31 | 2026-01-05 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-05-31 | 2025-02-21 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 30668 | GBP | 2024-05-31 | 2026-01-05 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 30668 | GBP | 2024-05-31 | 2025-02-21 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 307347 | GBP | 2024-05-31 | 2025-02-21 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 307347 | GBP | 2024-05-31 | 2026-01-05 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 277619 | GBP | 2024-05-31 | 2026-01-05 | filed | yes | `core:Equity` | micro-entity |
| equity | 277619 | GBP | 2024-05-31 | 2025-02-21 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 974 | GBP | 2024-05-31 | 2025-02-21 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 974 | GBP | 2024-05-31 | 2026-01-05 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 277619 | GBP | 2024-05-31 | 2026-01-05 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 277619 | GBP | 2024-05-31 | 2025-02-21 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 276679 | GBP | 2024-05-31 | 2026-01-05 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 276679 | GBP | 2024-05-31 | 2025-02-21 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 277653 | GBP | 2024-05-31 | 2025-02-21 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 277653 | GBP | 2024-05-31 | 2026-01-05 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-05-31 | 2025-02-21 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 35020 | GBP | 2023-05-31 | 2025-02-21 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 307088 | GBP | 2023-05-31 | 2025-02-21 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 274875 | GBP | 2023-05-31 | 2025-02-21 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 2820 | GBP | 2023-05-31 | 2025-02-21 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 274875 | GBP | 2023-05-31 | 2025-02-21 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 272068 | GBP | 2023-05-31 | 2025-02-21 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 274888 | GBP | 2023-05-31 | 2025-02-21 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## SISTEMZ LTD (`gb:04545879`)

- registration: `04545879` (GB), status active, incorporated 2002-09-26
- classification: ['62020'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 64 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-09-30 | 2026-06-26 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 11 | GBP | 2025-09-30 | 2026-06-26 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 55 | GBP | 2025-09-30 | 2026-06-26 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 44 | GBP | 2025-09-30 | 2026-06-26 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -5431 | GBP | 2025-09-30 | 2026-06-26 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2025-09-30 | 2026-06-26 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | -5430 | GBP | 2025-09-30 | 2026-06-26 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | -5679 | GBP | 2025-09-30 | 2026-06-26 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -5430 | GBP | 2025-09-30 | 2026-06-26 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-09-30 | 2025-06-30 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-09-30 | 2026-06-26 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 49 | GBP | 2024-09-30 | 2026-06-26 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 49 | GBP | 2024-09-30 | 2025-06-30 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 62 | GBP | 2024-09-30 | 2026-06-26 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 62 | GBP | 2024-09-30 | 2025-06-30 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 13 | GBP | 2024-09-30 | 2025-06-30 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 13 | GBP | 2024-09-30 | 2026-06-26 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2024-09-30 | 2025-06-30 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -4640 | GBP | 2024-09-30 | 2026-06-26 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | -4639 | GBP | 2024-09-30 | 2026-06-26 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -4640 | GBP | 2024-09-30 | 2025-06-30 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | -4639 | GBP | 2024-09-30 | 2025-06-30 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2024-09-30 | 2026-06-26 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | -4639 | GBP | 2024-09-30 | 2026-06-26 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -4639 | GBP | 2024-09-30 | 2025-06-30 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -4639 | GBP | 2024-09-30 | 2026-06-26 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -4639 | GBP | 2024-09-30 | 2025-06-30 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-09-30 | 2025-06-30 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-09-30 | 2024-06-30 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 58 | GBP | 2023-09-30 | 2024-06-30 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 58 | GBP | 2023-09-30 | 2025-06-30 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 58 | GBP | 2023-09-30 | 2025-06-30 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 58 | GBP | 2023-09-30 | 2024-06-30 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 0 | GBP | 2023-09-30 | 2024-06-30 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 0 | GBP | 2023-09-30 | 2025-06-30 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -4214 | GBP | 2023-09-30 | 2024-06-30 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2023-09-30 | 2025-06-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -4214 | GBP | 2023-09-30 | 2025-06-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | -4213 | GBP | 2023-09-30 | 2024-06-30 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2023-09-30 | 2024-06-30 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | -4213 | GBP | 2023-09-30 | 2025-06-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | -4213 | GBP | 2023-09-30 | 2025-06-30 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -4213 | GBP | 2023-09-30 | 2024-06-30 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -4213 | GBP | 2023-09-30 | 2025-06-30 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -4213 | GBP | 2023-09-30 | 2024-06-30 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2022-03-31 | 2024-06-30 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 298 | GBP | 2022-03-31 | 2024-06-30 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 528 | GBP | 2022-03-31 | 2024-06-30 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 230 | GBP | 2022-03-31 | 2024-06-30 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2022-03-31 | 2024-06-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | -4228 | GBP | 2022-03-31 | 2024-06-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -4229 | GBP | 2022-03-31 | 2024-06-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | -4228 | GBP | 2022-03-31 | 2024-06-30 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -4228 | GBP | 2022-03-31 | 2024-06-30 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## IO CONTROLS LIMITED (`gb:05117494`)

- registration: `05117494` (GB), status active, incorporated 2004-05-04
- classification: ['71129', '96090'] (sic_2007)
- records: 5 officers, 2 beneficial owners, 0 ownership statements, 2 security interests, 78 filings, 2 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 33 | xbrli:pure | 2026-05-31 | 2026-09-18 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 34254 | GBP | 2026-05-31 | 2026-09-18 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 25335 | GBP | 2026-05-31 | 2026-09-18 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1031369 | GBP | 2026-05-31 | 2026-09-18 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 1259931 | GBP | 2026-05-31 | 2026-09-18 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 1192677 | GBP | 2026-05-31 | 2026-09-18 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1192677 | GBP | 2026-05-31 | 2026-09-18 | filed | yes | `core:Debtors` | total-exemption-full |
| fixed_assets | 194015 | GBP | 2026-05-31 | 2026-09-18 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | 382808 | GBP | 2026-05-31 | 2026-09-18 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 228562 | GBP | 2026-05-31 | 2026-09-18 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 422577 | GBP | 2026-05-31 | 2026-09-18 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 31 | xbrli:pure | 2025-05-31 | 2025-09-04 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 31 | xbrli:pure | 2025-05-31 | 2026-09-18 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 101002 | GBP | 2025-05-31 | 2025-09-04 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 101002 | GBP | 2025-05-31 | 2026-09-18 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 81777 | GBP | 2025-05-31 | 2026-09-18 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 81777 | GBP | 2025-05-31 | 2025-09-04 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 845205 | GBP | 2025-05-31 | 2025-09-04 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 846471 | GBP | 2025-05-31 | 2026-09-18 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 1132244 | GBP | 2025-05-31 | 2026-09-18 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 1132243 | GBP | 2025-05-31 | 2025-09-04 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 1001142 | GBP | 2025-05-31 | 2026-09-18 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1001142 | GBP | 2025-05-31 | 2026-09-18 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 1001141 | GBP | 2025-05-31 | 2025-09-04 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1001141 | GBP | 2025-05-31 | 2025-09-04 | filed | no | `core:Debtors` | total-exemption-full |
| fixed_assets | 203029 | GBP | 2025-05-31 | 2025-09-04 | filed | no | `core:FixedAssets` | total-exemption-full |
| fixed_assets | 203029 | GBP | 2025-05-31 | 2026-09-18 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | 392837 | GBP | 2025-05-31 | 2026-09-18 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 393931 | GBP | 2025-05-31 | 2025-09-04 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 287038 | GBP | 2025-05-31 | 2025-09-04 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 285773 | GBP | 2025-05-31 | 2026-09-18 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 488802 | GBP | 2025-05-31 | 2026-09-18 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 490067 | GBP | 2025-05-31 | 2025-09-04 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 26 | xbrli:pure | 2024-05-31 | 2025-02-17 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 26 | xbrli:pure | 2024-05-31 | 2025-09-04 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 53861 | GBP | 2024-05-31 | 2025-02-17 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 53861 | GBP | 2024-05-31 | 2025-09-04 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 109794 | GBP | 2024-05-31 | 2025-09-04 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 109794 | GBP | 2024-05-31 | 2025-02-17 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 948191 | GBP | 2024-05-31 | 2025-02-17 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 948190 | GBP | 2024-05-31 | 2025-09-04 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 1062081 | GBP | 2024-05-31 | 2025-09-04 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 1062082 | GBP | 2024-05-31 | 2025-02-17 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 978920 | GBP | 2024-05-31 | 2025-09-04 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 978921 | GBP | 2024-05-31 | 2025-02-17 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 978920 | GBP | 2024-05-31 | 2025-09-04 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 978921 | GBP | 2024-05-31 | 2025-02-17 | filed | no | `core:Debtors` | total-exemption-full |
| fixed_assets | 208296 | GBP | 2024-05-31 | 2025-02-17 | filed | no | `core:FixedAssets` | total-exemption-full |
| fixed_assets | 208296 | GBP | 2024-05-31 | 2025-09-04 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | 199138 | GBP | 2024-05-31 | 2025-09-04 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 199138 | GBP | 2024-05-31 | 2025-02-17 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 113891 | GBP | 2024-05-31 | 2025-02-17 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 113891 | GBP | 2024-05-31 | 2025-09-04 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 322187 | GBP | 2024-05-31 | 2025-02-17 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 322187 | GBP | 2024-05-31 | 2025-09-04 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 25 | xbrli:pure | 2023-05-31 | 2025-02-17 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 48564 | GBP | 2023-05-31 | 2025-02-17 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 176792 | GBP | 2023-05-31 | 2025-02-17 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 994696 | GBP | 2023-05-31 | 2025-02-17 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 1132498 | GBP | 2023-05-31 | 2025-02-17 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1046934 | GBP | 2023-05-31 | 2025-02-17 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 1046934 | GBP | 2023-05-31 | 2025-02-17 | filed | yes | `core:Debtors` | total-exemption-full |
| fixed_assets | 237588 | GBP | 2023-05-31 | 2025-02-17 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | 184799 | GBP | 2023-05-31 | 2025-02-17 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 137802 | GBP | 2023-05-31 | 2025-02-17 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 375390 | GBP | 2023-05-31 | 2025-02-17 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2025-09-04: `{"superseded_document_id": "gb:05117494:doc:tgF2FRKyd0b0KyysvAR_psgPjFzYi3L9AMMibzhW5Fo", "restatements": [{"concept": "debtors", "period_end": "2024-05-31", "old_value": "978921.0000", "new_value": "`
- event restatement @ 2026-09-18: `{"superseded_document_id": "gb:05117494:doc:34dmGyOcJiAvnpQeK0WfZc5bONSsPMAsP9t3XYibNLs", "restatements": [{"concept": "debtors", "period_end": "2025-05-31", "old_value": "1001141.0000", "new_value": `

## PUSHYA LIMITED (`gb:05671021`)

- registration: `05671021` (GB), status active, incorporated 2006-01-10
- classification: ['62020'] (sic_2007)
- records: 2 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 63 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-03-31 | 2025-12-30 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 56508.09 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 14.04 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 14.04 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 808.03 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 808.03 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-03-31 | 2025-12-30 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-03-31 | 2024-12-27 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 44472 | GBP | 2024-03-31 | 2024-12-27 | filed | no | `ns5:CurrentAssets` | micro-entity |
| current_assets | 44471.83 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 128 | GBP | 2024-03-31 | 2024-12-27 | filed | no | `ns5:Equity` | micro-entity |
| equity | 128.01 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 128 | GBP | 2024-03-31 | 2024-12-27 | filed | no | `ns5:NetAssetsLiabilities` | micro-entity |
| net_assets | 128.01 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 588.01 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 3461 | GBP | 2024-03-31 | 2024-12-27 | filed | no | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 3461 | GBP | 2024-03-31 | 2024-12-27 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 588.01 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-03-31 | 2024-12-27 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 2 | xbrli:pure | 2023-03-31 | 2023-12-20 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 102 | GBP | 2023-03-31 | 2023-12-20 | filed | yes | `ns5:CashBankOnHand` | unaudited-abridged |
| current_assets | 31400 | GBP | 2023-03-31 | 2024-12-27 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 31400 | GBP | 2023-03-31 | 2023-12-20 | filed | yes | `ns5:CurrentAssets` | unaudited-abridged |
| debtors `{'OriginalRevisedDataDimension': 'Original'}` | 31298 | GBP | 2023-03-31 | 2023-12-20 | filed | yes | `ns5:Debtors` | unaudited-abridged |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 15 | GBP | 2023-03-31 | 2023-12-20 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 17 | GBP | 2023-03-31 | 2023-12-20 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 2 | GBP | 2023-03-31 | 2023-12-20 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity | 17 | GBP | 2023-03-31 | 2024-12-27 | filed | yes | `ns5:Equity` | micro-entity |
| net_assets `{'OriginalRevisedDataDimension': 'Original'}` | 17 | GBP | 2023-03-31 | 2023-12-20 | filed | yes | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_assets | 17 | GBP | 2023-03-31 | 2024-12-27 | filed | yes | `ns5:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 5684 | GBP | 2023-03-31 | 2024-12-27 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 5684 | GBP | 2023-03-31 | 2023-12-20 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 5684 | GBP | 2023-03-31 | 2023-12-20 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 5684 | GBP | 2023-03-31 | 2024-12-27 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 2 | xbrli:pure | 2022-03-31 | 2023-12-20 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 1215 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `ns5:CashBankOnHand` | unaudited-abridged |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 32699 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `ns5:CurrentAssets` | unaudited-abridged |
| debtors `{'OriginalRevisedDataDimension': 'Original'}` | 31484 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `ns5:Debtors` | unaudited-abridged |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 291 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 293 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 2 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `ns5:Equity` | unaudited-abridged |
| net_assets `{'OriginalRevisedDataDimension': 'Original'}` | 293 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 7626 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 7626 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |

_No coverage facts for the latest run._

- event restatement @ 2025-12-30: `{"superseded_document_id": "gb:05671021:doc:-PmZw4mpxvzY7nf5bGcO_X5rhrClGwipIcLPvv7Eu9s", "restatements": [{"concept": "current_assets", "period_end": "2024-03-31", "old_value": "44472.0000", "new_val`

## LASERGRAM LTD (`gb:06173971`)

- registration: `06173971` (GB), status active, incorporated 2007-03-20
- classification: ['71121'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 57 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-03-31 | 2025-10-17 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 20533 | GBP | 2025-03-31 | 2025-10-17 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 23905 | GBP | 2025-03-31 | 2025-10-17 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 3372 | GBP | 2025-03-31 | 2025-10-17 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 1221 | GBP | 2025-03-31 | 2025-10-17 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1220 | GBP | 2025-03-31 | 2025-10-17 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2025-03-31 | 2025-10-17 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | 1221 | GBP | 2025-03-31 | 2025-10-17 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1221 | GBP | 2025-03-31 | 2025-10-17 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-03-31 | 2024-12-03 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-03-31 | 2025-10-17 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 20687 | GBP | 2024-03-31 | 2024-12-03 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 20687 | GBP | 2024-03-31 | 2025-10-17 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 24059 | GBP | 2024-03-31 | 2025-10-17 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 24059 | GBP | 2024-03-31 | 2024-12-03 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 3372 | GBP | 2024-03-31 | 2024-12-03 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 3372 | GBP | 2024-03-31 | 2025-10-17 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 4872 | GBP | 2024-03-31 | 2024-12-03 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2024-03-31 | 2025-10-17 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2024-03-31 | 2024-12-03 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 4873 | GBP | 2024-03-31 | 2025-10-17 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 4873 | GBP | 2024-03-31 | 2024-12-03 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 4872 | GBP | 2024-03-31 | 2025-10-17 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | 4873 | GBP | 2024-03-31 | 2024-12-03 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 4873 | GBP | 2024-03-31 | 2025-10-17 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 4873 | GBP | 2024-03-31 | 2024-12-03 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 4873 | GBP | 2024-03-31 | 2025-10-17 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-03-31 | 2024-12-03 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 1 | xbrli:pure | 2023-03-31 | 2023-12-11 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 16665 | GBP | 2023-03-31 | 2024-12-03 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 16665 | GBP | 2023-03-31 | 2023-12-11 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 20037 | GBP | 2023-03-31 | 2024-12-03 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 20037 | GBP | 2023-03-31 | 2023-12-11 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original'}` | 3372 | GBP | 2023-03-31 | 2023-12-11 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 3372 | GBP | 2023-03-31 | 2024-12-03 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 4188 | GBP | 2023-03-31 | 2023-12-11 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 1 | GBP | 2023-03-31 | 2023-12-11 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 4188 | GBP | 2023-03-31 | 2024-12-03 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 4187 | GBP | 2023-03-31 | 2023-12-11 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2023-03-31 | 2024-12-03 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 4187 | GBP | 2023-03-31 | 2024-12-03 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 4188 | GBP | 2023-03-31 | 2023-12-11 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 4188 | GBP | 2023-03-31 | 2024-12-03 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 4188 | GBP | 2023-03-31 | 2024-12-03 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 4188 | GBP | 2023-03-31 | 2023-12-11 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 1 | xbrli:pure | 2022-03-31 | 2023-12-11 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 13791 | GBP | 2022-03-31 | 2023-12-11 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 17163 | GBP | 2022-03-31 | 2023-12-11 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original'}` | 3372 | GBP | 2022-03-31 | 2023-12-11 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 1 | GBP | 2022-03-31 | 2023-12-11 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 3510 | GBP | 2022-03-31 | 2023-12-11 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3509 | GBP | 2022-03-31 | 2023-12-11 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 3510 | GBP | 2022-03-31 | 2023-12-11 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 3510 | GBP | 2022-03-31 | 2023-12-11 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## DAEBI MAUN LTD (`gb:06574014`)

- registration: `06574014` (GB), status active, incorporated 2008-04-23
- classification: ['62020'] (sic_2007)
- records: 3 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 41 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-06-30 | 2026-03-31 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 4632 | GBP | 2025-06-30 | 2026-03-31 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 19945 | GBP | 2025-06-30 | 2026-03-31 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 64 | GBP | 2025-06-30 | 2026-03-31 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -24433 | GBP | 2025-06-30 | 2026-03-31 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 130 | GBP | 2025-06-30 | 2026-03-31 | filed | yes | `core:FixedAssets` | micro-entity |
| net_current_assets | -19881 | GBP | 2025-06-30 | 2026-03-31 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -19751 | GBP | 2025-06-30 | 2026-03-31 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-06-30 | 2025-03-31 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-06-30 | 2026-03-31 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 9178 | GBP | 2024-06-30 | 2025-03-31 | filed | no | `core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 9178 | GBP | 2024-06-30 | 2026-03-31 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 17087 | GBP | 2024-06-30 | 2026-03-31 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 17087 | GBP | 2024-06-30 | 2025-03-31 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 42 | GBP | 2024-06-30 | 2026-03-31 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 42 | GBP | 2024-06-30 | 2025-03-31 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | -26800 | GBP | 2024-06-30 | 2025-03-31 | filed | no | `core:Equity` | micro-entity |
| equity | -26800 | GBP | 2024-06-30 | 2026-03-31 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 173 | GBP | 2024-06-30 | 2026-03-31 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 173 | GBP | 2024-06-30 | 2025-03-31 | filed | no | `core:FixedAssets` | micro-entity |
| net_current_assets | -17045 | GBP | 2024-06-30 | 2026-03-31 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -17045 | GBP | 2024-06-30 | 2025-03-31 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -16872 | GBP | 2024-06-30 | 2025-03-31 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -16872 | GBP | 2024-06-30 | 2026-03-31 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-06-30 | 2025-03-31 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-06-30 | 2024-06-19 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 14583 | GBP | 2023-06-30 | 2024-06-19 | filed | no | `core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 14583 | GBP | 2023-06-30 | 2025-03-31 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 7420 | GBP | 2023-06-30 | 2025-03-31 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 7420 | GBP | 2023-06-30 | 2024-06-19 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 4 | GBP | 2023-06-30 | 2025-03-31 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 4 | GBP | 2023-06-30 | 2024-06-19 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | -22218 | GBP | 2023-06-30 | 2025-03-31 | filed | yes | `core:Equity` | micro-entity |
| equity | -22218 | GBP | 2023-06-30 | 2024-06-19 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 231 | GBP | 2023-06-30 | 2024-06-19 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 231 | GBP | 2023-06-30 | 2025-03-31 | filed | yes | `core:FixedAssets` | micro-entity |
| net_current_assets | -7416 | GBP | 2023-06-30 | 2024-06-19 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -7416 | GBP | 2023-06-30 | 2025-03-31 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -7185 | GBP | 2023-06-30 | 2025-03-31 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -7185 | GBP | 2023-06-30 | 2024-06-19 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2022-06-30 | 2024-06-19 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 19583 | GBP | 2022-06-30 | 2024-06-19 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 4434 | GBP | 2022-06-30 | 2024-06-19 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 6555 | GBP | 2022-06-30 | 2024-06-19 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -17804 | GBP | 2022-06-30 | 2024-06-19 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 308 | GBP | 2022-06-30 | 2024-06-19 | filed | yes | `core:FixedAssets` | micro-entity |
| net_current_assets `{'RestatementsFirstTimeAdoptionDimension': 'RestatedAmount'}` | 2121 | GBP | 2022-06-30 | 2024-06-19 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities `{'RestatementsFirstTimeAdoptionDimension': 'RestatedAmount'}` | 2429 | GBP | 2022-06-30 | 2024-06-19 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## TOM SYKES LIMITED (`gb:06947397`)

- registration: `06947397` (GB), status active, incorporated 2009-06-29
- classification: ['62030', '62090'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 1 security interests, 58 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 3 | iso4217:GBP | 2024-12-31 | 2025-03-20 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 204648 | GBP | 2024-12-31 | 2025-03-20 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 251655 | GBP | 2024-12-31 | 2025-03-20 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 64330 | GBP | 2024-12-31 | 2025-03-20 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 17323 | GBP | 2024-12-31 | 2025-03-20 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 64330 | GBP | 2024-12-31 | 2025-03-20 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 47007 | GBP | 2024-12-31 | 2025-03-20 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 64330 | GBP | 2024-12-31 | 2025-03-20 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2023-12-31 | 2024-04-23 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 43135 | GBP | 2023-12-31 | 2025-03-20 | filed | yes | `core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 43135 | GBP | 2023-12-31 | 2024-04-23 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 30780 | GBP | 2023-12-31 | 2024-04-23 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 30780 | GBP | 2023-12-31 | 2025-03-20 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 108558 | GBP | 2023-12-31 | 2025-03-20 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 108558 | GBP | 2023-12-31 | 2024-04-23 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | 43158 | GBP | 2023-12-31 | 2025-03-20 | filed | yes | `core:Equity` | micro-entity |
| equity | 43158 | GBP | 2023-12-31 | 2024-04-23 | filed | no | `uk-core:Equity` | micro-entity |
| fixed_assets | 8514 | GBP | 2023-12-31 | 2025-03-20 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 8514 | GBP | 2023-12-31 | 2024-04-23 | filed | no | `uk-core:FixedAssets` | micro-entity |
| net_assets | 43158 | GBP | 2023-12-31 | 2024-04-23 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 43158 | GBP | 2023-12-31 | 2025-03-20 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 77778 | GBP | 2023-12-31 | 2024-04-23 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 77778 | GBP | 2023-12-31 | 2025-03-20 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 86293 | GBP | 2023-12-31 | 2025-03-20 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 86293 | GBP | 2023-12-31 | 2024-04-23 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2022-06-30 | 2024-04-23 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2022-06-30 | 2024-04-23 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2022-06-30 | 2024-04-23 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 0 | GBP | 2022-06-30 | 2024-04-23 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 1 | GBP | 2022-06-30 | 2024-04-23 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2022-06-30 | 2024-04-23 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 1 | GBP | 2022-06-30 | 2024-04-23 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 0 | GBP | 2022-06-30 | 2024-04-23 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 1 | GBP | 2022-06-30 | 2024-04-23 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._
