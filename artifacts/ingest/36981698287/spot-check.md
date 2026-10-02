# Ingest spot-check

- database: `data/engine.db`
- latest run: `20261002T080203Z-3b343935`
- companies in store: 17000; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## DESIGNSPAN LIMITED (`gb:01934305`)

- registration: `01934305` (GB), status active, incorporated 1985-07-29
- classification: ['71121'] (sic_2007)
- records: 4 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 87 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-08-31 | 2026-05-30 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 37757 | GBP | 2025-08-31 | 2026-05-30 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 56413 | GBP | 2025-08-31 | 2026-05-30 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 18656 | GBP | 2025-08-31 | 2026-05-30 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 18656 | GBP | 2025-08-31 | 2026-05-30 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 23883 | GBP | 2025-08-31 | 2026-05-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2025-08-31 | 2026-05-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 22883 | GBP | 2025-08-31 | 2026-05-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | 23262 | GBP | 2025-08-31 | 2026-05-30 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 23883 | GBP | 2025-08-31 | 2026-05-30 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-08-31 | 2026-05-30 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-08-31 | 2025-05-25 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 36417 | GBP | 2024-08-31 | 2026-05-30 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 36417 | GBP | 2024-08-31 | 2025-05-25 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 53611 | GBP | 2024-08-31 | 2025-05-25 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 53611 | GBP | 2024-08-31 | 2026-05-30 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 17194 | GBP | 2024-08-31 | 2025-05-25 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 17194 | GBP | 2024-08-31 | 2026-05-30 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 17194 | GBP | 2024-08-31 | 2025-05-25 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 17194 | GBP | 2024-08-31 | 2026-05-30 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2024-08-31 | 2026-05-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 21368 | GBP | 2024-08-31 | 2025-05-25 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 22368 | GBP | 2024-08-31 | 2025-05-25 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 22368 | GBP | 2024-08-31 | 2026-05-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2024-08-31 | 2025-05-25 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 21368 | GBP | 2024-08-31 | 2026-05-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | 21483 | GBP | 2024-08-31 | 2025-05-25 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 21483 | GBP | 2024-08-31 | 2026-05-30 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 22368 | GBP | 2024-08-31 | 2025-05-25 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 22368 | GBP | 2024-08-31 | 2026-05-30 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-08-31 | 2024-05-26 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-08-31 | 2025-05-25 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 50169 | GBP | 2023-08-31 | 2024-05-26 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 50169 | GBP | 2023-08-31 | 2025-05-25 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 58784 | GBP | 2023-08-31 | 2025-05-25 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 58784 | GBP | 2023-08-31 | 2024-05-26 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 8615 | GBP | 2023-08-31 | 2025-05-25 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 8615 | GBP | 2023-08-31 | 2024-05-26 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 8615 | GBP | 2023-08-31 | 2024-05-26 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 8615 | GBP | 2023-08-31 | 2025-05-25 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2023-08-31 | 2024-05-26 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 40559 | GBP | 2023-08-31 | 2025-05-25 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2023-08-31 | 2025-05-25 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 40559 | GBP | 2023-08-31 | 2024-05-26 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 41559 | GBP | 2023-08-31 | 2024-05-26 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 41559 | GBP | 2023-08-31 | 2025-05-25 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | 40814 | GBP | 2023-08-31 | 2024-05-26 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 40814 | GBP | 2023-08-31 | 2025-05-25 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 41559 | GBP | 2023-08-31 | 2025-05-25 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 41559 | GBP | 2023-08-31 | 2024-05-26 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2022-08-31 | 2024-05-26 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 35515 | GBP | 2022-08-31 | 2024-05-26 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 45595 | GBP | 2022-08-31 | 2024-05-26 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 10080 | GBP | 2022-08-31 | 2024-05-26 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 10080 | GBP | 2022-08-31 | 2024-05-26 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 29847 | GBP | 2022-08-31 | 2024-05-26 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 28847 | GBP | 2022-08-31 | 2024-05-26 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2022-08-31 | 2024-05-26 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | 29312 | GBP | 2022-08-31 | 2024-05-26 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 29847 | GBP | 2022-08-31 | 2024-05-26 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## THE UCC GROUP LIMITED (`gb:02439347`)

- registration: `02439347` (GB), status active, incorporated 1989-11-02
- classification: ['62020'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 87 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-12-31 | 2026-04-27 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| current_assets | 27849 | GBP | 2025-12-31 | 2026-04-27 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 27849 | GBP | 2025-12-31 | 2026-04-27 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 27750 | GBP | 2025-12-31 | 2026-04-27 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2025-12-31 | 2026-04-27 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 1 | GBP | 2025-12-31 | 2026-04-27 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 27752 | GBP | 2025-12-31 | 2026-04-27 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 27751 | GBP | 2025-12-31 | 2026-04-27 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 27752 | GBP | 2025-12-31 | 2026-04-27 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-12-31 | 2026-04-27 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-12-31 | 2026-02-19 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| current_assets | 27849 | GBP | 2024-12-31 | 2026-04-27 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| current_assets | 27849 | GBP | 2024-12-31 | 2026-02-19 | filed | no | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 27849 | GBP | 2024-12-31 | 2026-02-19 | filed | no | `frs-core:Debtors` | total-exemption-full |
| debtors | 27849 | GBP | 2024-12-31 | 2026-04-27 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 27750 | GBP | 2024-12-31 | 2026-04-27 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-12-31 | 2026-04-27 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-12-31 | 2026-02-19 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 27750 | GBP | 2024-12-31 | 2026-02-19 | filed | no | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 1 | GBP | 2024-12-31 | 2026-02-19 | filed | no | `frs-core:FixedAssets` | total-exemption-full |
| fixed_assets | 1 | GBP | 2024-12-31 | 2026-04-27 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 27752 | GBP | 2024-12-31 | 2026-04-27 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 27752 | GBP | 2024-12-31 | 2026-02-19 | filed | no | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 27751 | GBP | 2024-12-31 | 2026-04-27 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 27751 | GBP | 2024-12-31 | 2026-02-19 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 27752 | GBP | 2024-12-31 | 2026-04-27 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 27752 | GBP | 2024-12-31 | 2026-02-19 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-12-31 | 2026-02-19 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-12-31 | 2024-12-19 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| current_assets | 27849 | GBP | 2023-12-31 | 2024-12-19 | filed | no | `frs-core:CurrentAssets` | total-exemption-full |
| current_assets | 27849 | GBP | 2023-12-31 | 2026-02-19 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 27849 | GBP | 2023-12-31 | 2024-12-19 | filed | no | `frs-core:Debtors` | total-exemption-full |
| debtors | 27849 | GBP | 2023-12-31 | 2026-02-19 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 27750 | GBP | 2023-12-31 | 2026-02-19 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 27750 | GBP | 2023-12-31 | 2024-12-19 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-12-31 | 2024-12-19 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-12-31 | 2026-02-19 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 1 | GBP | 2023-12-31 | 2026-02-19 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| fixed_assets | 1 | GBP | 2023-12-31 | 2024-12-19 | filed | no | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 27850 | GBP | 2023-12-31 | 2024-12-19 | filed | no | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 27850 | GBP | 2023-12-31 | 2026-02-19 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 27849 | GBP | 2023-12-31 | 2024-12-19 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 27849 | GBP | 2023-12-31 | 2026-02-19 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 27850 | GBP | 2023-12-31 | 2024-12-19 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 27850 | GBP | 2023-12-31 | 2026-02-19 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2022-12-31 | 2024-12-19 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| current_assets | 27849 | GBP | 2022-12-31 | 2024-12-19 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 27849 | GBP | 2022-12-31 | 2024-12-19 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2022-12-31 | 2024-12-19 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 27750 | GBP | 2022-12-31 | 2024-12-19 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 1 | GBP | 2022-12-31 | 2024-12-19 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 27850 | GBP | 2022-12-31 | 2024-12-19 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 27849 | GBP | 2022-12-31 | 2024-12-19 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 27850 | GBP | 2022-12-31 | 2024-12-19 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## IIYAMA (UK) LIMITED (`gb:02792962`)

- registration: `02792962` (GB), status active, incorporated 1993-02-23
- classification: ['62020', '62090', '63110'] (sic_2007)
- records: 22 officers, 1 beneficial owners, 0 ownership statements, 2 security interests, 148 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 9 | xbrli:pure | 2025-12-31 | 2026-08-24 | filed | yes | `c:AverageNumberEmployeesDuringPeriod` | small |
| cash | 3761218 | GBP | 2025-12-31 | 2026-08-24 | filed | yes | `c:CashBankOnHand` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1815706 | GBP | 2025-12-31 | 2026-08-24 | filed | yes | `c:Creditors` | small |
| current_assets | 5431538 | GBP | 2025-12-31 | 2026-08-24 | filed | yes | `c:CurrentAssets` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 1670320 | GBP | 2025-12-31 | 2026-08-24 | filed | yes | `c:Debtors` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -1168024 | GBP | 2025-12-31 | 2026-08-24 | filed | yes | `c:Equity` | small |
| equity | 3744596 | GBP | 2025-12-31 | 2026-08-24 | filed | yes | `c:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1400001 | GBP | 2025-12-31 | 2026-08-24 | filed | yes | `c:Equity` | small |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 3512619 | GBP | 2025-12-31 | 2026-08-24 | filed | yes | `c:Equity` | small |
| fixed_assets | 128764 | GBP | 2025-12-31 | 2026-08-24 | filed | yes | `c:FixedAssets` | small |
| net_assets | 3744596 | GBP | 2025-12-31 | 2026-08-24 | filed | yes | `c:NetAssetsLiabilities` | small |
| net_current_assets | 3615832 | GBP | 2025-12-31 | 2026-08-24 | filed | yes | `c:NetCurrentAssetsLiabilities` | small |
| total_assets_less_current_liabilities | 3744596 | GBP | 2025-12-31 | 2026-08-24 | filed | yes | `c:TotalAssetsLessCurrentLiabilities` | small |
| average_employees | 7 | xbrli:pure | 2024-12-31 | 2025-09-30 | filed | no | `d:AverageNumberEmployeesDuringPeriod` | small |
| average_employees | 7 | xbrli:pure | 2024-12-31 | 2026-08-24 | filed | yes | `c:AverageNumberEmployeesDuringPeriod` | small |
| cash | 3652714 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `d:CashBankOnHand` | small |
| cash | 3652714 | GBP | 2024-12-31 | 2026-08-24 | filed | yes | `c:CashBankOnHand` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 687899 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `d:Creditors` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 687899 | GBP | 2024-12-31 | 2026-08-24 | filed | yes | `c:Creditors` | small |
| current_assets | 4041281 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `d:CurrentAssets` | small |
| current_assets | 4041281 | GBP | 2024-12-31 | 2026-08-24 | filed | yes | `c:CurrentAssets` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 388567 | GBP | 2024-12-31 | 2026-08-24 | filed | yes | `c:Debtors` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 388567 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `d:Debtors` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -1480370 | GBP | 2024-12-31 | 2026-08-24 | filed | yes | `c:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1400001 | GBP | 2024-12-31 | 2026-08-24 | filed | yes | `c:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -1480370 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `d:Equity` | small |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 3512619 | GBP | 2024-12-31 | 2026-08-24 | filed | yes | `c:Equity` | small |
| equity | 3432250 | GBP | 2024-12-31 | 2026-08-24 | filed | yes | `c:Equity` | small |
| equity | 3432250 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `d:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1400001 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `d:Equity` | small |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 3512619 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `d:Equity` | small |
| fixed_assets | 78868 | GBP | 2024-12-31 | 2026-08-24 | filed | yes | `c:FixedAssets` | small |
| fixed_assets | 78868 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `d:FixedAssets` | small |
| net_assets | 3432250 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `d:NetAssetsLiabilities` | small |
| net_assets | 3432250 | GBP | 2024-12-31 | 2026-08-24 | filed | yes | `c:NetAssetsLiabilities` | small |
| net_current_assets | 3353382 | GBP | 2024-12-31 | 2026-08-24 | filed | yes | `c:NetCurrentAssetsLiabilities` | small |
| net_current_assets | 3353382 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `d:NetCurrentAssetsLiabilities` | small |
| total_assets_less_current_liabilities | 3432250 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `d:TotalAssetsLessCurrentLiabilities` | small |
| total_assets_less_current_liabilities | 3432250 | GBP | 2024-12-31 | 2026-08-24 | filed | yes | `c:TotalAssetsLessCurrentLiabilities` | small |
| average_employees | 6 | xbrli:pure | 2023-12-31 | 2025-09-30 | filed | yes | `d:AverageNumberEmployeesDuringPeriod` | small |
| cash | 3455109 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `d:CashBankOnHand` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1017074 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `d:Creditors` | small |
| current_assets | 4161859 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `d:CurrentAssets` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 706750 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `d:Debtors` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1400001 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `d:Equity` | small |
| equity | 3193976 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `d:Equity` | small |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 3512619 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `d:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -1718644 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `d:Equity` | small |
| fixed_assets | 49191 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `d:FixedAssets` | small |
| net_assets | 3193976 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `d:NetAssetsLiabilities` | small |
| net_current_assets | 3144785 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `d:NetCurrentAssetsLiabilities` | small |
| total_assets_less_current_liabilities | 3193976 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `d:TotalAssetsLessCurrentLiabilities` | small |

_No coverage facts for the latest run._

## C N W CONSULTING LIMITED (`gb:03057923`)

- registration: `03057923` (GB), status active, incorporated 1995-05-18
- classification: ['62020'] (sic_2007)
- records: 3 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 66 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | iso4217:GBP | 2025-05-31 | 2026-02-15 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2025-05-31 | 2026-02-15 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2025-05-31 | 2026-02-15 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 6289 | GBP | 2025-05-31 | 2026-02-15 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 6389 | GBP | 2025-05-31 | 2026-02-15 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2025-05-31 | 2026-02-15 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 6389 | GBP | 2025-05-31 | 2026-02-15 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 6289 | GBP | 2025-05-31 | 2026-02-15 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 6389 | GBP | 2025-05-31 | 2026-02-15 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-05-31 | 2025-02-16 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-05-31 | 2026-02-15 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2024-05-31 | 2026-02-15 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2024-05-31 | 2025-02-16 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2024-05-31 | 2026-02-15 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2024-05-31 | 2025-02-16 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 6289 | GBP | 2024-05-31 | 2026-02-15 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 6289 | GBP | 2024-05-31 | 2025-02-16 | filed | no | `core:CurrentAssets` | micro-entity |
| depreciation_amortisation | 0 | GBP | 2024-05-31 | 2025-02-16 | filed | yes | `core:DepreciationAmortisationImpairmentExpense` | micro-entity |
| equity | 6389 | GBP | 2024-05-31 | 2026-02-15 | filed | yes | `uk-core:Equity` | micro-entity |
| equity | 6389 | GBP | 2024-05-31 | 2025-02-16 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2024-05-31 | 2025-02-16 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 0 | GBP | 2024-05-31 | 2026-02-15 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 6389 | GBP | 2024-05-31 | 2025-02-16 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 6389 | GBP | 2024-05-31 | 2026-02-15 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 6289 | GBP | 2024-05-31 | 2026-02-15 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 6289 | GBP | 2024-05-31 | 2025-02-16 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| profit_for_period | 0 | GBP | 2024-05-31 | 2025-02-16 | filed | yes | `core:ProfitLoss` | micro-entity |
| revenue | 0 | GBP | 2024-05-31 | 2025-02-16 | filed | yes | `core:TurnoverRevenue` | micro-entity |
| staff_costs | 0 | GBP | 2024-05-31 | 2025-02-16 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | micro-entity |
| tax_charge | 0 | GBP | 2024-05-31 | 2025-02-16 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | micro-entity |
| total_assets_less_current_liabilities | 6389 | GBP | 2024-05-31 | 2025-02-16 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 6389 | GBP | 2024-05-31 | 2026-02-15 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-05-31 | 2024-02-26 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2023-05-31 | 2025-02-16 | filed | yes | `core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2023-05-31 | 2024-02-26 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2023-05-31 | 2024-02-26 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2023-05-31 | 2025-02-16 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 6289 | GBP | 2023-05-31 | 2024-02-26 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 6289 | GBP | 2023-05-31 | 2025-02-16 | filed | yes | `core:CurrentAssets` | micro-entity |
| depreciation_amortisation | 0 | GBP | 2023-05-31 | 2024-02-26 | filed | no | `core:DepreciationAmortisationImpairmentExpense` | micro-entity |
| depreciation_amortisation | 0 | GBP | 2023-05-31 | 2025-02-16 | filed | yes | `core:DepreciationAmortisationImpairmentExpense` | micro-entity |
| equity | 6389 | GBP | 2023-05-31 | 2025-02-16 | filed | yes | `core:Equity` | micro-entity |
| equity | 6389 | GBP | 2023-05-31 | 2024-02-26 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2023-05-31 | 2025-02-16 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 0 | GBP | 2023-05-31 | 2024-02-26 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | 6389 | GBP | 2023-05-31 | 2025-02-16 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 6389 | GBP | 2023-05-31 | 2024-02-26 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 6289 | GBP | 2023-05-31 | 2024-02-26 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 6289 | GBP | 2023-05-31 | 2025-02-16 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| profit_for_period | 0 | GBP | 2023-05-31 | 2024-02-26 | filed | no | `core:ProfitLoss` | micro-entity |
| profit_for_period | 0 | GBP | 2023-05-31 | 2025-02-16 | filed | yes | `core:ProfitLoss` | micro-entity |
| revenue | 0 | GBP | 2023-05-31 | 2025-02-16 | filed | yes | `core:TurnoverRevenue` | micro-entity |
| revenue | 0 | GBP | 2023-05-31 | 2024-02-26 | filed | no | `core:TurnoverRevenue` | micro-entity |
| staff_costs | 0 | GBP | 2023-05-31 | 2024-02-26 | filed | no | `core:StaffCostsEmployeeBenefitsExpense` | micro-entity |
| staff_costs | 0 | GBP | 2023-05-31 | 2025-02-16 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | micro-entity |
| tax_charge | 0 | GBP | 2023-05-31 | 2024-02-26 | filed | no | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | micro-entity |
| tax_charge | 0 | GBP | 2023-05-31 | 2025-02-16 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | micro-entity |
| total_assets_less_current_liabilities | 6389 | GBP | 2023-05-31 | 2025-02-16 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 6389 | GBP | 2023-05-31 | 2024-02-26 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2022-05-31 | 2024-02-26 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2022-05-31 | 2024-02-26 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 6289 | GBP | 2022-05-31 | 2024-02-26 | filed | yes | `core:CurrentAssets` | micro-entity |
| depreciation_amortisation | 0 | GBP | 2022-05-31 | 2024-02-26 | filed | yes | `core:DepreciationAmortisationImpairmentExpense` | micro-entity |
| equity | 6389 | GBP | 2022-05-31 | 2024-02-26 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2022-05-31 | 2024-02-26 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 6389 | GBP | 2022-05-31 | 2024-02-26 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 6289 | GBP | 2022-05-31 | 2024-02-26 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| profit_for_period | 0 | GBP | 2022-05-31 | 2024-02-26 | filed | yes | `core:ProfitLoss` | micro-entity |
| revenue | 0 | GBP | 2022-05-31 | 2024-02-26 | filed | yes | `core:TurnoverRevenue` | micro-entity |
| staff_costs | 0 | GBP | 2022-05-31 | 2024-02-26 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | micro-entity |
| tax_charge | 0 | GBP | 2022-05-31 | 2024-02-26 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | micro-entity |
| total_assets_less_current_liabilities | 6389 | GBP | 2022-05-31 | 2024-02-26 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## INTELLIGENT DATA CAPTURE LIMITED (`gb:03271734`)

- registration: `03271734` (GB), status active, incorporated 1996-10-31
- classification: ['62090'] (sic_2007)
- records: 7 officers, 2 beneficial owners, 0 ownership statements, 1 security interests, 98 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 3 | xbrli:pure | 2025-04-30 | 2025-07-04 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 94710 | GBP | 2025-04-30 | 2025-07-04 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| equity | 102690 | GBP | 2025-04-30 | 2025-07-04 | filed | yes | `frs-core:Equity` | micro-entity |
| fixed_assets | 2760 | GBP | 2025-04-30 | 2025-07-04 | filed | yes | `frs-core:FixedAssets` | micro-entity |
| net_assets | 102690 | GBP | 2025-04-30 | 2025-07-04 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 100855 | GBP | 2025-04-30 | 2025-07-04 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 103615 | GBP | 2025-04-30 | 2025-07-04 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 3 | xbrli:pure | 2024-04-30 | 2025-07-04 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 3 | xbrli:pure | 2024-04-30 | 2024-06-12 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 1781 | GBP | 2024-04-30 | 2025-07-04 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| current_assets | 1781 | GBP | 2024-04-30 | 2024-06-12 | filed | no | `frs-core:CurrentAssets` | micro-entity |
| equity | -156958 | GBP | 2024-04-30 | 2025-07-04 | filed | yes | `frs-core:Equity` | micro-entity |
| equity | -156958 | GBP | 2024-04-30 | 2024-06-12 | filed | no | `frs-core:Equity` | micro-entity |
| fixed_assets | 100785 | GBP | 2024-04-30 | 2024-06-12 | filed | no | `frs-core:FixedAssets` | micro-entity |
| fixed_assets | 100785 | GBP | 2024-04-30 | 2025-07-04 | filed | yes | `frs-core:FixedAssets` | micro-entity |
| net_assets | -156958 | GBP | 2024-04-30 | 2025-07-04 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_assets | -156958 | GBP | 2024-04-30 | 2024-06-12 | filed | no | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -256943 | GBP | 2024-04-30 | 2024-06-12 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -256943 | GBP | 2024-04-30 | 2025-07-04 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -156158 | GBP | 2024-04-30 | 2025-07-04 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -156158 | GBP | 2024-04-30 | 2024-06-12 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 3 | xbrli:pure | 2023-04-30 | 2024-06-12 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 1622 | GBP | 2023-04-30 | 2024-06-12 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| equity | -180055 | GBP | 2023-04-30 | 2024-06-12 | filed | yes | `frs-core:Equity` | micro-entity |
| fixed_assets | 100000 | GBP | 2023-04-30 | 2024-06-12 | filed | yes | `frs-core:FixedAssets` | micro-entity |
| net_assets | -180055 | GBP | 2023-04-30 | 2024-06-12 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -279255 | GBP | 2023-04-30 | 2024-06-12 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -179255 | GBP | 2023-04-30 | 2024-06-12 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## CRESCENT MOTORCYCLE COMPANY LIMITED (`gb:03475588`)

- registration: `03475588` (GB), status active, incorporated 1997-12-03
- classification: ['71129'] (sic_2007)
- records: 6 officers, 1 beneficial owners, 0 ownership statements, 3 security interests, 98 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 49 | xbrli:pure | 2024-12-31 | 2025-08-07 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | medium |
| cash | 1649997 | GBP | 2024-12-31 | 2025-08-07 | filed | yes | `ns5:CashBankOnHand` | medium |
| current_assets | 5713387 | GBP | 2024-12-31 | 2025-08-07 | filed | yes | `ns5:CurrentAssets` | medium |
| debtors | 402164 | GBP | 2024-12-31 | 2025-08-07 | filed | yes | `ns5:Debtors` | medium |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 402164 | GBP | 2024-12-31 | 2025-08-07 | filed | yes | `ns5:Debtors` | medium |
| equity | 5771644 | GBP | 2024-12-31 | 2025-08-07 | filed | yes | `ns5:Equity` | medium |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 5771544 | GBP | 2024-12-31 | 2025-08-07 | filed | yes | `ns5:Equity` | medium |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-12-31 | 2025-08-07 | filed | yes | `ns5:Equity` | medium |
| fixed_assets | 2519909 | GBP | 2024-12-31 | 2025-08-07 | filed | yes | `ns5:FixedAssets` | medium |
| gross_profit | 1772781 | GBP | 2024-12-31 | 2025-08-07 | filed | yes | `ns5:GrossProfitLoss` | medium |
| net_assets | 5771644 | GBP | 2024-12-31 | 2025-08-07 | filed | yes | `ns5:NetAssetsLiabilities` | medium |
| net_current_assets | 3350600 | GBP | 2024-12-31 | 2025-08-07 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | medium |
| operating_profit | 197065 | GBP | 2024-12-31 | 2025-08-07 | filed | yes | `ns5:OperatingProfitLoss` | medium |
| profit_before_tax | 207200 | GBP | 2024-12-31 | 2025-08-07 | filed | yes | `ns5:ProfitLossOnOrdinaryActivitiesBeforeTax` | medium |
| profit_for_period | 212656 | GBP | 2024-12-31 | 2025-08-07 | filed | yes | `ns5:ProfitLoss` | medium |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 212656 | GBP | 2024-12-31 | 2025-08-07 | filed | yes | `ns5:ProfitLoss` | medium |
| revenue `{'GeographicSegmentsDimension': 'TotalGeographicSegmentsIncludingAnyUnallocatedAmount'}` | 19519514 | GBP | 2024-12-31 | 2025-08-07 | filed | yes | `ns5:TurnoverRevenue` | medium |
| revenue `{'GeographicSegmentsDimension': 'UnitedStates'}` | 25183 | GBP | 2024-12-31 | 2025-08-07 | filed | yes | `ns5:TurnoverRevenue` | medium |
| revenue `{'GeographicSegmentsDimension': 'UnitedKingdom'}` | 18243538 | GBP | 2024-12-31 | 2025-08-07 | filed | yes | `ns5:TurnoverRevenue` | medium |
| revenue | 19519514 | GBP | 2024-12-31 | 2025-08-07 | filed | yes | `ns5:TurnoverRevenue` | medium |
| revenue `{'GeographicSegmentsDimension': 'Asia'}` | 23 | GBP | 2024-12-31 | 2025-08-07 | filed | yes | `ns5:TurnoverRevenue` | medium |
| revenue `{'GeographicSegmentsDimension': 'Europe'}` | 1250221 | GBP | 2024-12-31 | 2025-08-07 | filed | yes | `ns5:TurnoverRevenue` | medium |
| staff_costs | 1860554 | GBP | 2024-12-31 | 2025-08-07 | filed | yes | `ns5:StaffCostsEmployeeBenefitsExpense` | medium |
| tax_charge | -5456 | GBP | 2024-12-31 | 2025-08-07 | filed | yes | `ns5:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | medium |
| total_assets_less_current_liabilities | 5870509 | GBP | 2024-12-31 | 2025-08-07 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | medium |
| average_employees | 49 | xbrli:pure | 2023-12-31 | 2025-08-07 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | medium |
| average_employees | 49 | xbrli:pure | 2023-12-31 | 2024-07-01 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | full |
| cash | 442461 | GBP | 2023-12-31 | 2025-08-07 | filed | yes | `ns5:CashBankOnHand` | medium |
| cash | 442461 | GBP | 2023-12-31 | 2024-07-01 | filed | no | `ns5:CashBankOnHand` | full |
| current_assets | 5696672 | GBP | 2023-12-31 | 2025-08-07 | filed | yes | `ns5:CurrentAssets` | medium |
| current_assets | 5696672 | GBP | 2023-12-31 | 2024-07-01 | filed | no | `ns5:CurrentAssets` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 462310 | GBP | 2023-12-31 | 2024-07-01 | filed | no | `ns5:Debtors` | full |
| debtors | 462310 | GBP | 2023-12-31 | 2025-08-07 | filed | yes | `ns5:Debtors` | medium |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 462310 | GBP | 2023-12-31 | 2025-08-07 | filed | yes | `ns5:Debtors` | medium |
| debtors | 462310 | GBP | 2023-12-31 | 2024-07-01 | filed | no | `ns5:Debtors` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 5558888 | GBP | 2023-12-31 | 2024-07-01 | filed | no | `ns5:Equity` | full |
| equity | 5558988 | GBP | 2023-12-31 | 2025-08-07 | filed | yes | `ns5:Equity` | medium |
| equity | 5558988 | GBP | 2023-12-31 | 2024-07-01 | filed | no | `ns5:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 5558888 | GBP | 2023-12-31 | 2025-08-07 | filed | yes | `ns5:Equity` | medium |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-12-31 | 2025-08-07 | filed | yes | `ns5:Equity` | medium |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-12-31 | 2024-07-01 | filed | no | `ns5:Equity` | full |
| fixed_assets | 2526317 | GBP | 2023-12-31 | 2025-08-07 | filed | yes | `ns5:FixedAssets` | medium |
| fixed_assets | 2526317 | GBP | 2023-12-31 | 2024-07-01 | filed | no | `ns5:FixedAssets` | full |
| gross_profit | 1694332 | GBP | 2023-12-31 | 2025-08-07 | filed | yes | `ns5:GrossProfitLoss` | medium |
| gross_profit | 1694332 | GBP | 2023-12-31 | 2024-07-01 | filed | no | `ns5:GrossProfitLoss` | full |
| net_assets | 5558988 | GBP | 2023-12-31 | 2025-08-07 | filed | yes | `ns5:NetAssetsLiabilities` | medium |
| net_assets | 5558988 | GBP | 2023-12-31 | 2024-07-01 | filed | no | `ns5:NetAssetsLiabilities` | full |
| net_current_assets | 3142029 | GBP | 2023-12-31 | 2025-08-07 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | medium |
| net_current_assets | 3142029 | GBP | 2023-12-31 | 2024-07-01 | filed | no | `ns5:NetCurrentAssetsLiabilities` | full |
| operating_profit | 254993 | GBP | 2023-12-31 | 2025-08-07 | filed | yes | `ns5:OperatingProfitLoss` | medium |
| operating_profit | 254993 | GBP | 2023-12-31 | 2024-07-01 | filed | no | `ns5:OperatingProfitLoss` | full |
| profit_before_tax | 257212 | GBP | 2023-12-31 | 2024-07-01 | filed | no | `ns5:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_before_tax | 257212 | GBP | 2023-12-31 | 2025-08-07 | filed | yes | `ns5:ProfitLossOnOrdinaryActivitiesBeforeTax` | medium |
| profit_for_period | 229407 | GBP | 2023-12-31 | 2025-08-07 | filed | yes | `ns5:ProfitLoss` | medium |
| profit_for_period | 229407 | GBP | 2023-12-31 | 2024-07-01 | filed | no | `ns5:ProfitLoss` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 229407 | GBP | 2023-12-31 | 2024-07-01 | filed | yes | `ns5:ProfitLoss` | full |
| revenue `{'GeographicSegmentsDimension': 'UnitedStates'}` | 24587 | GBP | 2023-12-31 | 2025-08-07 | filed | yes | `ns5:TurnoverRevenue` | medium |
| revenue `{'GeographicSegmentsDimension': 'Europe'}` | 1360905 | GBP | 2023-12-31 | 2024-07-01 | filed | no | `ns5:TurnoverRevenue` | full |
| revenue | 18044773 | GBP | 2023-12-31 | 2025-08-07 | filed | yes | `ns5:TurnoverRevenue` | medium |
| revenue `{'GeographicSegmentsDimension': 'Asia'}` | 43901 | GBP | 2023-12-31 | 2024-07-01 | filed | no | `ns5:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'Asia'}` | 43901 | GBP | 2023-12-31 | 2025-08-07 | filed | yes | `ns5:TurnoverRevenue` | medium |
| revenue `{'GeographicSegmentsDimension': 'UnitedKingdom'}` | 16614982 | GBP | 2023-12-31 | 2025-08-07 | filed | yes | `ns5:TurnoverRevenue` | medium |
| revenue | 18044773 | GBP | 2023-12-31 | 2024-07-01 | filed | no | `ns5:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'Europe'}` | 1360905 | GBP | 2023-12-31 | 2025-08-07 | filed | yes | `ns5:TurnoverRevenue` | medium |
| revenue `{'GeographicSegmentsDimension': 'TotalGeographicSegmentsIncludingAnyUnallocatedAmount'}` | 18044773 | GBP | 2023-12-31 | 2024-07-01 | filed | no | `ns5:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'UnitedStates'}` | 24587 | GBP | 2023-12-31 | 2024-07-01 | filed | no | `ns5:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'TotalGeographicSegmentsIncludingAnyUnallocatedAmount'}` | 18044773 | GBP | 2023-12-31 | 2025-08-07 | filed | yes | `ns5:TurnoverRevenue` | medium |
| revenue `{'GeographicSegmentsDimension': 'UnitedKingdom'}` | 16614982 | GBP | 2023-12-31 | 2024-07-01 | filed | no | `ns5:TurnoverRevenue` | full |
| staff_costs | 1805440 | GBP | 2023-12-31 | 2025-08-07 | filed | yes | `ns5:StaffCostsEmployeeBenefitsExpense` | medium |
| staff_costs | 1805440 | GBP | 2023-12-31 | 2024-07-01 | filed | no | `ns5:StaffCostsEmployeeBenefitsExpense` | full |
| tax_charge | 27805 | GBP | 2023-12-31 | 2025-08-07 | filed | yes | `ns5:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | medium |
| tax_charge | 27805 | GBP | 2023-12-31 | 2024-07-01 | filed | no | `ns5:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| total_assets_less_current_liabilities | 5668346 | GBP | 2023-12-31 | 2025-08-07 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | medium |
| total_assets_less_current_liabilities | 5668346 | GBP | 2023-12-31 | 2024-07-01 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | full |
| average_employees | 48 | xbrli:pure | 2022-12-31 | 2024-07-01 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | full |
| average_employees | 48 | xbrli:pure | 2022-12-31 | 2023-10-05 | filed | no | `ns6:AverageNumberEmployeesDuringPeriod` | full |
| cash | 1228703 | GBP | 2022-12-31 | 2024-07-01 | filed | yes | `ns5:CashBankOnHand` | full |
| cash | 1228703 | GBP | 2022-12-31 | 2023-10-05 | filed | no | `ns6:CashBankOnHand` | full |
| current_assets | 6648882 | GBP | 2022-12-31 | 2024-07-01 | filed | yes | `ns5:CurrentAssets` | full |
| current_assets | 6648882 | GBP | 2022-12-31 | 2023-10-05 | filed | no | `ns6:CurrentAssets` | full |
| debtors | 828689 | GBP | 2022-12-31 | 2023-10-05 | filed | no | `ns6:Debtors` | full |
| debtors | 828689 | GBP | 2022-12-31 | 2024-07-01 | filed | yes | `ns5:Debtors` | full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 828689 | GBP | 2022-12-31 | 2023-10-05 | filed | no | `ns6:Debtors` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 828689 | GBP | 2022-12-31 | 2024-07-01 | filed | yes | `ns5:Debtors` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 5329481 | GBP | 2022-12-31 | 2023-10-05 | filed | no | `ns6:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 5329481 | GBP | 2022-12-31 | 2024-07-01 | filed | no | `ns5:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 5329481 | GBP | 2022-12-31 | 2025-08-07 | filed | yes | `ns5:Equity` | medium |
| equity | 5329581 | GBP | 2022-12-31 | 2023-10-05 | filed | no | `ns6:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2022-12-31 | 2023-10-05 | filed | no | `ns6:Equity` | full |
| equity | 5329581 | GBP | 2022-12-31 | 2025-08-07 | filed | yes | `ns5:Equity` | medium |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2022-12-31 | 2024-07-01 | filed | no | `ns5:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2022-12-31 | 2025-08-07 | filed | yes | `ns5:Equity` | medium |
| equity | 5329581 | GBP | 2022-12-31 | 2024-07-01 | filed | no | `ns5:Equity` | full |
| fixed_assets | 2144721 | GBP | 2022-12-31 | 2023-10-05 | filed | no | `ns6:FixedAssets` | full |
| fixed_assets | 2144721 | GBP | 2022-12-31 | 2024-07-01 | filed | yes | `ns5:FixedAssets` | full |
| gross_profit | 1833281 | GBP | 2022-12-31 | 2023-10-05 | filed | no | `ns6:GrossProfitLoss` | full |
| gross_profit | 1833281 | GBP | 2022-12-31 | 2024-07-01 | filed | yes | `ns5:GrossProfitLoss` | full |
| net_assets | 5329581 | GBP | 2022-12-31 | 2023-10-05 | filed | no | `ns6:NetAssetsLiabilities` | full |
| net_assets | 5329581 | GBP | 2022-12-31 | 2024-07-01 | filed | yes | `ns5:NetAssetsLiabilities` | full |
| net_current_assets | 3209470 | GBP | 2022-12-31 | 2024-07-01 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | full |
| net_current_assets | 3209470 | GBP | 2022-12-31 | 2023-10-05 | filed | no | `ns6:NetCurrentAssetsLiabilities` | full |
| operating_profit | 530251 | GBP | 2022-12-31 | 2024-07-01 | filed | yes | `ns5:OperatingProfitLoss` | full |
| operating_profit | 530251 | GBP | 2022-12-31 | 2023-10-05 | filed | no | `ns6:OperatingProfitLoss` | full |
| profit_before_tax | 530251 | GBP | 2022-12-31 | 2024-07-01 | filed | yes | `ns5:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_before_tax | 530251 | GBP | 2022-12-31 | 2023-10-05 | filed | no | `ns6:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 427836 | GBP | 2022-12-31 | 2023-10-05 | filed | yes | `ns6:ProfitLoss` | full |
| profit_for_period | 427836 | GBP | 2022-12-31 | 2024-07-01 | filed | yes | `ns5:ProfitLoss` | full |
| profit_for_period | 427836 | GBP | 2022-12-31 | 2023-10-05 | filed | no | `ns6:ProfitLoss` | full |
| revenue | 18583879 | GBP | 2022-12-31 | 2023-10-05 | filed | no | `ns6:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'UnitedStates'}` | 58453 | GBP | 2022-12-31 | 2023-10-05 | filed | no | `ns6:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'TotalGeographicSegmentsIncludingAnyUnallocatedAmount'}` | 18583879 | GBP | 2022-12-31 | 2023-10-05 | filed | no | `ns6:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'UnitedKingdom'}` | 16939579 | GBP | 2022-12-31 | 2024-07-01 | filed | yes | `ns5:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'UnitedStates'}` | 58453 | GBP | 2022-12-31 | 2024-07-01 | filed | yes | `ns5:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'Asia'}` | 0 | GBP | 2022-12-31 | 2024-07-01 | filed | yes | `ns5:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'Europe'}` | 1585847 | GBP | 2022-12-31 | 2024-07-01 | filed | yes | `ns5:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'Europe'}` | 1585847 | GBP | 2022-12-31 | 2023-10-05 | filed | no | `ns6:TurnoverRevenue` | full |
| revenue | 18583879 | GBP | 2022-12-31 | 2024-07-01 | filed | yes | `ns5:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'UnitedKingdom'}` | 16939579 | GBP | 2022-12-31 | 2023-10-05 | filed | no | `ns6:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'TotalGeographicSegmentsIncludingAnyUnallocatedAmount'}` | 18583879 | GBP | 2022-12-31 | 2024-07-01 | filed | yes | `ns5:TurnoverRevenue` | full |
| staff_costs | 1705896 | GBP | 2022-12-31 | 2023-10-05 | filed | no | `ns6:StaffCostsEmployeeBenefitsExpense` | full |
| staff_costs | 1705896 | GBP | 2022-12-31 | 2024-07-01 | filed | yes | `ns5:StaffCostsEmployeeBenefitsExpense` | full |
| tax_charge | 102415 | GBP | 2022-12-31 | 2024-07-01 | filed | yes | `ns5:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| tax_charge | 102415 | GBP | 2022-12-31 | 2023-10-05 | filed | no | `ns6:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| total_assets_less_current_liabilities | 5354191 | GBP | 2022-12-31 | 2024-07-01 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | full |
| total_assets_less_current_liabilities | 5354191 | GBP | 2022-12-31 | 2023-10-05 | filed | no | `ns6:TotalAssetsLessCurrentLiabilities` | full |
| average_employees | 46 | xbrli:pure | 2021-12-31 | 2023-10-05 | filed | yes | `ns6:AverageNumberEmployeesDuringPeriod` | full |
| cash | 772795 | GBP | 2021-12-31 | 2023-10-05 | filed | yes | `ns6:CashBankOnHand` | full |
| current_assets | 5421003 | GBP | 2021-12-31 | 2023-10-05 | filed | yes | `ns6:CurrentAssets` | full |
| debtors | 662307 | GBP | 2021-12-31 | 2023-10-05 | filed | yes | `ns6:Debtors` | full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 662307 | GBP | 2021-12-31 | 2023-10-05 | filed | yes | `ns6:Debtors` | full |
| equity | 4901745 | GBP | 2021-12-31 | 2024-07-01 | filed | yes | `ns5:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 4901645 | GBP | 2021-12-31 | 2023-10-05 | filed | no | `ns6:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 4901645 | GBP | 2021-12-31 | 2024-07-01 | filed | yes | `ns5:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2021-12-31 | 2023-10-05 | filed | no | `ns6:Equity` | full |
| equity | 4901745 | GBP | 2021-12-31 | 2023-10-05 | filed | no | `ns6:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2021-12-31 | 2024-07-01 | filed | yes | `ns5:Equity` | full |
| fixed_assets | 2127572 | GBP | 2021-12-31 | 2023-10-05 | filed | yes | `ns6:FixedAssets` | full |
| gross_profit | 938372 | GBP | 2021-12-31 | 2023-10-05 | filed | yes | `ns6:GrossProfitLoss` | full |
| net_assets | 4901745 | GBP | 2021-12-31 | 2023-10-05 | filed | yes | `ns6:NetAssetsLiabilities` | full |
| net_current_assets | 2799852 | GBP | 2021-12-31 | 2023-10-05 | filed | yes | `ns6:NetCurrentAssetsLiabilities` | full |
| operating_profit | 160438 | GBP | 2021-12-31 | 2023-10-05 | filed | yes | `ns6:OperatingProfitLoss` | full |
| profit_before_tax | 160459 | GBP | 2021-12-31 | 2023-10-05 | filed | yes | `ns6:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period | 215044 | GBP | 2021-12-31 | 2023-10-05 | filed | yes | `ns6:ProfitLoss` | full |
| revenue `{'GeographicSegmentsDimension': 'UnitedStates'}` | 0 | GBP | 2021-12-31 | 2023-10-05 | filed | yes | `ns6:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'Europe'}` | 1142981 | GBP | 2021-12-31 | 2023-10-05 | filed | yes | `ns6:TurnoverRevenue` | full |
| revenue | 12676033 | GBP | 2021-12-31 | 2023-10-05 | filed | yes | `ns6:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'TotalGeographicSegmentsIncludingAnyUnallocatedAmount'}` | 12676033 | GBP | 2021-12-31 | 2023-10-05 | filed | yes | `ns6:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'UnitedKingdom'}` | 11531569 | GBP | 2021-12-31 | 2023-10-05 | filed | yes | `ns6:TurnoverRevenue` | full |
| staff_costs | 1422375 | GBP | 2021-12-31 | 2023-10-05 | filed | yes | `ns6:StaffCostsEmployeeBenefitsExpense` | full |
| tax_charge | -54585 | GBP | 2021-12-31 | 2023-10-05 | filed | yes | `ns6:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| total_assets_less_current_liabilities | 4927424 | GBP | 2021-12-31 | 2023-10-05 | filed | yes | `ns6:TotalAssetsLessCurrentLiabilities` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2020-12-31 | 2023-10-05 | filed | yes | `ns6:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 4872601 | GBP | 2020-12-31 | 2023-10-05 | filed | yes | `ns6:Equity` | full |
| equity | 4872701 | GBP | 2020-12-31 | 2023-10-05 | filed | yes | `ns6:Equity` | full |

_No coverage facts for the latest run._

## ENVOY COMPUTER SERVICES LTD (`gb:03663737`)

- registration: `03663737` (GB), status active, incorporated 1998-11-06
- classification: ['62012'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 68 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | iso4217:GBP | 2025-03-31 | 2025-12-19 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 20363 | GBP | 2025-03-31 | 2025-12-19 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 3473 | GBP | 2025-03-31 | 2025-12-19 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 15446 | GBP | 2025-03-31 | 2025-12-19 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 1444 | GBP | 2025-03-31 | 2025-12-19 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 15446 | GBP | 2025-03-31 | 2025-12-19 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 16890 | GBP | 2025-03-31 | 2025-12-19 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 15446 | GBP | 2025-03-31 | 2025-12-19 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-03-31 | 2024-12-19 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-03-31 | 2025-12-19 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 25698 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 25698 | GBP | 2024-03-31 | 2025-12-19 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 17559 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 17559 | GBP | 2024-03-31 | 2025-12-19 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 6334 | GBP | 2024-03-31 | 2025-12-19 | filed | yes | `uk-core:Equity` | micro-entity |
| equity | 6334 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `uk-core:Equity` | micro-entity |
| fixed_assets | 1805 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 1805 | GBP | 2024-03-31 | 2025-12-19 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 6334 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 6334 | GBP | 2024-03-31 | 2025-12-19 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 8139 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 8139 | GBP | 2024-03-31 | 2025-12-19 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 6334 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 6334 | GBP | 2024-03-31 | 2025-12-19 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-03-31 | 2023-12-21 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-03-31 | 2024-12-19 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 28245 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 21499 | GBP | 2023-03-31 | 2023-12-21 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 18068 | GBP | 2023-03-31 | 2023-12-21 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 22769 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 905 | GBP | 2023-03-31 | 2023-12-21 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 3149 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 2526 | GBP | 2023-03-31 | 2023-12-21 | filed | no | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 2327 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 3149 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 905 | GBP | 2023-03-31 | 2023-12-21 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 5476 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 3431 | GBP | 2023-03-31 | 2023-12-21 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 3149 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 905 | GBP | 2023-03-31 | 2023-12-21 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2022-03-31 | 2023-12-21 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 21499 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 18068 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 905 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 2526 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 905 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 3431 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 905 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2024-12-19: `{"superseded_document_id": "gb:03663737:doc:ATFvGUXlXU3FY2HnRX6wveMq9oM3_Y55p8BBxCWj4H8", "restatements": [{"concept": "fixed_assets", "period_end": "2023-03-31", "old_value": "2526.0000", "new_value"`

## DFK SYSTEMS LTD (`gb:03865446`)

- registration: `03865446` (GB), status active, incorporated 1999-10-26
- classification: ['62020', '63120'] (sic_2007)
- records: 5 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 67 filings, 2 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-10-31 | 2026-04-16 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 3359 | GBP | 2025-10-31 | 2026-04-16 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 68739 | GBP | 2025-10-31 | 2026-04-16 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 67384 | GBP | 2025-10-31 | 2026-04-16 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 2804 | GBP | 2025-10-31 | 2026-04-16 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 67384 | GBP | 2025-10-31 | 2026-04-16 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 65380 | GBP | 2025-10-31 | 2026-04-16 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 68184 | GBP | 2025-10-31 | 2026-04-16 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-10-31 | 2026-04-16 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | -2 | xbrli:pure | 2024-10-31 | 2025-07-31 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 3442 | GBP | 2024-10-31 | 2026-04-16 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1842 | GBP | 2024-10-31 | 2025-07-31 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 57570 | GBP | 2024-10-31 | 2025-07-31 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 57570 | GBP | 2024-10-31 | 2026-04-16 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 56293 | GBP | 2024-10-31 | 2025-07-31 | filed | no | `core:Equity` | micro-entity |
| equity | 54693 | GBP | 2024-10-31 | 2026-04-16 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 565 | GBP | 2024-10-31 | 2025-07-31 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 565 | GBP | 2024-10-31 | 2026-04-16 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 54693 | GBP | 2024-10-31 | 2026-04-16 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 54128 | GBP | 2024-10-31 | 2026-04-16 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 55728 | GBP | 2024-10-31 | 2025-07-31 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 56293 | GBP | 2024-10-31 | 2025-07-31 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 54693 | GBP | 2024-10-31 | 2026-04-16 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2023-10-31 | 2024-07-25 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | -1 | xbrli:pure | 2023-10-31 | 2025-07-31 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2023-10-31 | 2024-07-25 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 10968 | GBP | 2023-10-31 | 2025-07-31 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 10668 | GBP | 2023-10-31 | 2024-07-25 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 57970 | GBP | 2023-10-31 | 2025-07-31 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 57971 | GBP | 2023-10-31 | 2024-07-25 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 47755 | GBP | 2023-10-31 | 2025-07-31 | filed | yes | `core:Equity` | micro-entity |
| equity | 48056 | GBP | 2023-10-31 | 2024-07-25 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 753 | GBP | 2023-10-31 | 2025-07-31 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 753 | GBP | 2023-10-31 | 2024-07-25 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | 48056 | GBP | 2023-10-31 | 2024-07-25 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 47002 | GBP | 2023-10-31 | 2025-07-31 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 47303 | GBP | 2023-10-31 | 2024-07-25 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 48056 | GBP | 2023-10-31 | 2024-07-25 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 47755 | GBP | 2023-10-31 | 2025-07-31 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2022-10-31 | 2024-07-25 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 405 | GBP | 2022-10-31 | 2024-07-25 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 1787 | GBP | 2022-10-31 | 2024-07-25 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 2385 | GBP | 2022-10-31 | 2024-07-25 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 1003 | GBP | 2022-10-31 | 2024-07-25 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 2385 | GBP | 2022-10-31 | 2024-07-25 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 1382 | GBP | 2022-10-31 | 2024-07-25 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 2385 | GBP | 2022-10-31 | 2024-07-25 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2025-07-31: `{"superseded_document_id": "gb:03865446:doc:7TZwWqPspsybg4nLcKUgjWxkDyH0ukGnjYlWERk_EO8", "restatements": [{"concept": "current_assets", "period_end": "2023-10-31", "old_value": "57971.0000", "new_val`
- event restatement @ 2026-04-16: `{"superseded_document_id": "gb:03865446:doc:_oTY-18j_4HOGTHsGKfixtYpBpjAXx4oJrbl7-7jaNs", "restatements": [{"concept": "creditors_within_one_year", "period_end": "2024-10-31", "old_value": "1842.0000"`

## BROMEX LIMITED (`gb:04062494`)

- registration: `04062494` (GB), status active, incorporated 2000-08-31
- classification: ['62020'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 62 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | iso4217:GBP | 2025-06-30 | 2026-03-29 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 56817 | GBP | 2025-06-30 | 2026-03-29 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 79100 | GBP | 2025-06-30 | 2026-03-29 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 25108 | GBP | 2025-06-30 | 2026-03-29 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 2825 | GBP | 2025-06-30 | 2026-03-29 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 25108 | GBP | 2025-06-30 | 2026-03-29 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 22283 | GBP | 2025-06-30 | 2026-03-29 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 25108 | GBP | 2025-06-30 | 2026-03-29 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-06-30 | 2025-03-30 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-06-30 | 2026-03-29 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 64902 | GBP | 2024-06-30 | 2025-03-30 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 64902 | GBP | 2024-06-30 | 2026-03-29 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 84268 | GBP | 2024-06-30 | 2025-03-30 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 84268 | GBP | 2024-06-30 | 2026-03-29 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 22159 | GBP | 2024-06-30 | 2025-03-30 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 22159 | GBP | 2024-06-30 | 2026-03-29 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 2793 | GBP | 2024-06-30 | 2025-03-30 | filed | no | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 2793 | GBP | 2024-06-30 | 2026-03-29 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 22159 | GBP | 2024-06-30 | 2026-03-29 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 22159 | GBP | 2024-06-30 | 2025-03-30 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 19366 | GBP | 2024-06-30 | 2026-03-29 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 19366 | GBP | 2024-06-30 | 2025-03-30 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 22159 | GBP | 2024-06-30 | 2025-03-30 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 22159 | GBP | 2024-06-30 | 2026-03-29 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-06-30 | 2024-03-30 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-06-30 | 2025-03-30 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 59452 | GBP | 2023-06-30 | 2024-03-30 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 59452 | GBP | 2023-06-30 | 2025-03-30 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 74656 | GBP | 2023-06-30 | 2025-03-30 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 74656 | GBP | 2023-06-30 | 2024-03-30 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | 17415 | GBP | 2023-06-30 | 2024-03-30 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 17415 | GBP | 2023-06-30 | 2025-03-30 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 2211 | GBP | 2023-06-30 | 2025-03-30 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 2211 | GBP | 2023-06-30 | 2024-03-30 | filed | no | `uk-core:FixedAssets` | micro-entity |
| net_assets | 17415 | GBP | 2023-06-30 | 2025-03-30 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 17415 | GBP | 2023-06-30 | 2024-03-30 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 15204 | GBP | 2023-06-30 | 2025-03-30 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 15204 | GBP | 2023-06-30 | 2024-03-30 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 17415 | GBP | 2023-06-30 | 2024-03-30 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 17415 | GBP | 2023-06-30 | 2025-03-30 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2022-06-30 | 2024-03-30 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 57933 | GBP | 2022-06-30 | 2024-03-30 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 69534 | GBP | 2022-06-30 | 2024-03-30 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 13013 | GBP | 2022-06-30 | 2024-03-30 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 1412 | GBP | 2022-06-30 | 2024-03-30 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 13013 | GBP | 2022-06-30 | 2024-03-30 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 11601 | GBP | 2022-06-30 | 2024-03-30 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 13013 | GBP | 2022-06-30 | 2024-03-30 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

Coverage @ 2025-06-30: 8/21 concepts available (average_employees, creditors_within_one_year, current_assets, equity, fixed_assets, net_assets, net_current_assets, total_assets_less_current_liabilities)
- `cash`: filed_without_concept — regime 'micro-entity' omits this concept
- `creditors_after_one_year`: filed_without_concept — regime 'micro-entity' omits this concept
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
