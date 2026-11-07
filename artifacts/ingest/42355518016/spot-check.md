# Ingest spot-check

- database: `data/engine.db`
- latest run: `20261107T082745Z-5d4c8ab3`
- companies in store: 45800; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## CLOCKING IN MACHINES LIMITED (`gb:02697648`)

- registration: `02697648` (GB), status active, incorporated 1992-03-11
- classification: ['47910', '62020', '62030', '62090'] (sic_2007)
- records: 9 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 91 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-12-31 | 2026-05-12 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 9402 | GBP | 2025-12-31 | 2026-05-12 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 3728 | GBP | 2025-12-31 | 2026-05-12 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 9409 | GBP | 2025-12-31 | 2026-05-12 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 7 | GBP | 2025-12-31 | 2026-05-12 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 7 | GBP | 2025-12-31 | 2026-05-12 | filed | yes | `core:Debtors` | total-exemption-full |
| net_assets | 5681 | GBP | 2025-12-31 | 2026-05-12 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-12-31 | 2025-08-18 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-12-31 | 2026-05-12 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 6555 | GBP | 2024-12-31 | 2025-08-18 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 6555 | GBP | 2024-12-31 | 2026-05-12 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 4652 | GBP | 2024-12-31 | 2026-05-12 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 4652 | GBP | 2024-12-31 | 2025-08-18 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 6871 | GBP | 2024-12-31 | 2025-08-18 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 6871 | GBP | 2024-12-31 | 2026-05-12 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 316 | GBP | 2024-12-31 | 2025-08-18 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 316 | GBP | 2024-12-31 | 2026-05-12 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 316 | GBP | 2024-12-31 | 2025-08-18 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 316 | GBP | 2024-12-31 | 2026-05-12 | filed | yes | `core:Debtors` | total-exemption-full |
| net_assets | 2219 | GBP | 2024-12-31 | 2025-08-18 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 2219 | GBP | 2024-12-31 | 2026-05-12 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-12-31 | 2025-08-18 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-12-31 | 2024-07-02 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 6096 | GBP | 2023-12-31 | 2025-08-18 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 6096 | GBP | 2023-12-31 | 2024-07-02 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5359 | GBP | 2023-12-31 | 2024-07-02 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5359 | GBP | 2023-12-31 | 2025-08-18 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 6810 | GBP | 2023-12-31 | 2024-07-02 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 6810 | GBP | 2023-12-31 | 2025-08-18 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 714 | GBP | 2023-12-31 | 2024-07-02 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 714 | GBP | 2023-12-31 | 2025-08-18 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 714 | GBP | 2023-12-31 | 2025-08-18 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 714 | GBP | 2023-12-31 | 2024-07-02 | filed | no | `core:Debtors` | total-exemption-full |
| net_assets | 1451 | GBP | 2023-12-31 | 2025-08-18 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 1451 | GBP | 2023-12-31 | 2024-07-02 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2022-12-31 | 2024-07-02 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 3110 | GBP | 2022-12-31 | 2024-07-02 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 4670 | GBP | 2022-12-31 | 2024-07-02 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 3868 | GBP | 2022-12-31 | 2024-07-02 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 758 | GBP | 2022-12-31 | 2024-07-02 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 758 | GBP | 2022-12-31 | 2024-07-02 | filed | yes | `core:Debtors` | total-exemption-full |
| net_assets | -802 | GBP | 2022-12-31 | 2024-07-02 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## Y. O CONSULTANTS LIMITED (`gb:03354042`)

- registration: `03354042` (GB), status active, incorporated 1997-04-16
- classification: ['62020', '62090'] (sic_2007)
- records: 4 officers, 3 beneficial owners, 0 ownership statements, 0 security interests, 87 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | iso4217:GBP | 2025-04-30 | 2026-04-02 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 5807 | GBP | 2025-04-30 | 2026-04-02 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 37984 | GBP | 2025-04-30 | 2026-04-02 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 1235 | GBP | 2025-04-30 | 2026-04-02 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 41263 | GBP | 2025-04-30 | 2026-04-02 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 4332 | GBP | 2025-04-30 | 2026-04-02 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 41263 | GBP | 2025-04-30 | 2026-04-02 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 36749 | GBP | 2025-04-30 | 2026-04-02 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 32417 | GBP | 2025-04-30 | 2026-04-02 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-04-30 | 2026-04-02 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-04-30 | 2025-04-26 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 8565 | GBP | 2024-04-30 | 2026-04-02 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 8565 | GBP | 2024-04-30 | 2025-04-26 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 36850 | GBP | 2024-04-30 | 2026-04-02 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 36850 | GBP | 2024-04-30 | 2025-04-26 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 2968 | GBP | 2024-04-30 | 2025-04-26 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 2968 | GBP | 2024-04-30 | 2026-04-02 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 39457 | GBP | 2024-04-30 | 2026-04-02 | filed | yes | `uk-core:Equity` | micro-entity |
| equity | 39457 | GBP | 2024-04-30 | 2025-04-26 | filed | no | `uk-core:Equity` | micro-entity |
| fixed_assets | 4862 | GBP | 2024-04-30 | 2026-04-02 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 39457 | GBP | 2024-04-30 | 2025-04-26 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 39457 | GBP | 2024-04-30 | 2026-04-02 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 33882 | GBP | 2024-04-30 | 2026-04-02 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 33882 | GBP | 2024-04-30 | 2025-04-26 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 29020 | GBP | 2024-04-30 | 2025-04-26 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 29020 | GBP | 2024-04-30 | 2026-04-02 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-04-30 | 2024-04-26 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-04-30 | 2025-04-26 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 12830 | GBP | 2023-04-30 | 2025-04-26 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 12830 | GBP | 2023-04-30 | 2024-04-26 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 38978 | GBP | 2023-04-30 | 2025-04-26 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 38978 | GBP | 2023-04-30 | 2024-04-26 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 9491 | GBP | 2023-04-30 | 2025-04-26 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 9491 | GBP | 2023-04-30 | 2024-04-26 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | 40458 | GBP | 2023-04-30 | 2024-04-26 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 40458 | GBP | 2023-04-30 | 2025-04-26 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 5459 | GBP | 2023-04-30 | 2024-04-26 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 40458 | GBP | 2023-04-30 | 2025-04-26 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 40458 | GBP | 2023-04-30 | 2024-04-26 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 29487 | GBP | 2023-04-30 | 2025-04-26 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 29487 | GBP | 2023-04-30 | 2024-04-26 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 24028 | GBP | 2023-04-30 | 2024-04-26 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 24028 | GBP | 2023-04-30 | 2025-04-26 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2022-04-30 | 2024-04-26 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 16046 | GBP | 2022-04-30 | 2024-04-26 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 36638 | GBP | 2022-04-30 | 2024-04-26 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 8682 | GBP | 2022-04-30 | 2024-04-26 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 39712 | GBP | 2022-04-30 | 2024-04-26 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 6130 | GBP | 2022-04-30 | 2024-04-26 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 39712 | GBP | 2022-04-30 | 2024-04-26 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 27956 | GBP | 2022-04-30 | 2024-04-26 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 21826 | GBP | 2022-04-30 | 2024-04-26 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## VCT LTD. (`gb:03859697`)

- registration: `03859697` (GB), status active, incorporated 1999-10-12
- classification: ['26511', '71121', '71122', '72190'] (sic_2007)
- records: 8 officers, 3 beneficial owners, 0 ownership statements, 0 security interests, 80 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 21 | xbrli:pure | 2025-04-04 | 2025-12-09 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 295780 | GBP | 2025-04-04 | 2025-12-09 | filed | yes | `ns5:CashBankOnHand` | unaudited-abridged |
| current_assets | 1463113 | GBP | 2025-04-04 | 2025-12-09 | filed | yes | `ns5:CurrentAssets` | unaudited-abridged |
| debtors | 391822 | GBP | 2025-04-04 | 2025-12-09 | filed | yes | `ns5:Debtors` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 100 | GBP | 2025-04-04 | 2025-12-09 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity | 1147477 | GBP | 2025-04-04 | 2025-12-09 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200 | GBP | 2025-04-04 | 2025-12-09 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1147177 | GBP | 2025-04-04 | 2025-12-09 | filed | yes | `ns5:Equity` | unaudited-abridged |
| net_assets | 1147477 | GBP | 2025-04-04 | 2025-12-09 | filed | yes | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 1089805 | GBP | 2025-04-04 | 2025-12-09 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 1162565 | GBP | 2025-04-04 | 2025-12-09 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 19 | xbrli:pure | 2024-04-04 | 2025-12-09 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| average_employees | 19 | xbrli:pure | 2024-04-04 | 2025-03-31 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 196312 | GBP | 2024-04-04 | 2025-12-09 | filed | yes | `ns5:CashBankOnHand` | unaudited-abridged |
| cash | 196312 | GBP | 2024-04-04 | 2025-03-31 | filed | no | `ns5:CashBankOnHand` | unaudited-abridged |
| current_assets | 1237819 | GBP | 2024-04-04 | 2025-03-31 | filed | no | `ns5:CurrentAssets` | unaudited-abridged |
| current_assets | 1237819 | GBP | 2024-04-04 | 2025-12-09 | filed | yes | `ns5:CurrentAssets` | unaudited-abridged |
| debtors | 470097 | GBP | 2024-04-04 | 2025-12-09 | filed | yes | `ns5:Debtors` | unaudited-abridged |
| debtors | 470097 | GBP | 2024-04-04 | 2025-03-31 | filed | no | `ns5:Debtors` | unaudited-abridged |
| equity | 961425 | GBP | 2024-04-04 | 2025-12-09 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 961125 | GBP | 2024-04-04 | 2025-12-09 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 100 | GBP | 2024-04-04 | 2025-12-09 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200 | GBP | 2024-04-04 | 2025-12-09 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 100 | GBP | 2024-04-04 | 2025-03-31 | filed | no | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 961125 | GBP | 2024-04-04 | 2025-03-31 | filed | no | `ns5:Equity` | unaudited-abridged |
| equity | 961425 | GBP | 2024-04-04 | 2025-03-31 | filed | no | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200 | GBP | 2024-04-04 | 2025-03-31 | filed | no | `ns5:Equity` | unaudited-abridged |
| net_assets | 961425 | GBP | 2024-04-04 | 2025-03-31 | filed | no | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_assets | 961425 | GBP | 2024-04-04 | 2025-12-09 | filed | yes | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 927101 | GBP | 2024-04-04 | 2025-12-09 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 927101 | GBP | 2024-04-04 | 2025-03-31 | filed | no | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 970530 | GBP | 2024-04-04 | 2025-03-31 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 970530 | GBP | 2024-04-04 | 2025-12-09 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 16 | xbrli:pure | 2023-04-04 | 2023-12-20 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| average_employees | 16 | xbrli:pure | 2023-04-04 | 2025-03-31 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 149425 | GBP | 2023-04-04 | 2025-03-31 | filed | yes | `ns5:CashBankOnHand` | unaudited-abridged |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 149425 | GBP | 2023-04-04 | 2023-12-20 | filed | yes | `ns5:CashBankOnHand` | unaudited-abridged |
| current_assets | 1022735 | GBP | 2023-04-04 | 2025-03-31 | filed | yes | `ns5:CurrentAssets` | unaudited-abridged |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 1022735 | GBP | 2023-04-04 | 2023-12-20 | filed | yes | `ns5:CurrentAssets` | unaudited-abridged |
| debtors `{'OriginalRevisedDataDimension': 'Original'}` | 449872 | GBP | 2023-04-04 | 2023-12-20 | filed | yes | `ns5:Debtors` | unaudited-abridged |
| debtors | 449872 | GBP | 2023-04-04 | 2025-03-31 | filed | yes | `ns5:Debtors` | unaudited-abridged |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 100 | GBP | 2023-04-04 | 2023-12-20 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 881562 | GBP | 2023-04-04 | 2023-12-20 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 200 | GBP | 2023-04-04 | 2023-12-20 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200 | GBP | 2023-04-04 | 2025-03-31 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 881262 | GBP | 2023-04-04 | 2023-12-20 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 100 | GBP | 2023-04-04 | 2025-03-31 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 881262 | GBP | 2023-04-04 | 2025-03-31 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity | 881562 | GBP | 2023-04-04 | 2025-03-31 | filed | yes | `ns5:Equity` | unaudited-abridged |
| net_assets | 881562 | GBP | 2023-04-04 | 2025-03-31 | filed | yes | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_assets `{'OriginalRevisedDataDimension': 'Original'}` | 881562 | GBP | 2023-04-04 | 2023-12-20 | filed | yes | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 835183 | GBP | 2023-04-04 | 2025-03-31 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 835183 | GBP | 2023-04-04 | 2023-12-20 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 890249 | GBP | 2023-04-04 | 2023-12-20 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 890249 | GBP | 2023-04-04 | 2025-03-31 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 14 | xbrli:pure | 2022-04-04 | 2023-12-20 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 117321 | GBP | 2022-04-04 | 2023-12-20 | filed | yes | `ns5:CashBankOnHand` | unaudited-abridged |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 813427 | GBP | 2022-04-04 | 2023-12-20 | filed | yes | `ns5:CurrentAssets` | unaudited-abridged |
| debtors `{'OriginalRevisedDataDimension': 'Original'}` | 285425 | GBP | 2022-04-04 | 2023-12-20 | filed | yes | `ns5:Debtors` | unaudited-abridged |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 100 | GBP | 2022-04-04 | 2023-12-20 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 200 | GBP | 2022-04-04 | 2023-12-20 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 671640 | GBP | 2022-04-04 | 2023-12-20 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 671340 | GBP | 2022-04-04 | 2023-12-20 | filed | yes | `ns5:Equity` | unaudited-abridged |
| net_assets `{'OriginalRevisedDataDimension': 'Original'}` | 671640 | GBP | 2022-04-04 | 2023-12-20 | filed | yes | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 636377 | GBP | 2022-04-04 | 2023-12-20 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 677171 | GBP | 2022-04-04 | 2023-12-20 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |

_No coverage facts for the latest run._

## INGLETON WOOD INVESTMENTS LIMITED (`gb:04363240`)

- registration: `04363240` (GB), status active, incorporated 2002-01-30
- classification: ['71111'] (sic_2007)
- records: 14 officers, 3 beneficial owners, 0 ownership statements, 1 security interests, 116 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-03-31 | 2025-12-22 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 465657 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `ns5:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 500 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `ns5:Equity` | small |
| equity | 466157 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `ns5:Equity` | small |
| total_assets_less_current_liabilities | 466157 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | small |
| average_employees | 1 | xbrli:pure | 2024-03-31 | 2025-12-22 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | small |
| average_employees | 1 | xbrli:pure | 2024-03-31 | 2024-12-20 | filed | no | `d:AverageNumberEmployeesDuringPeriod` | small |
| equity | 466157 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `ns5:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 500 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `ns5:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 465657 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `ns5:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 500 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `d:Equity` | small |
| equity | 466157 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `d:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 465657 | GBP | 2024-03-31 | 2024-12-20 | filed | no | `d:Equity` | small |
| net_assets | 466157 | GBP | 2024-03-31 | 2024-12-20 | filed | yes | `d:NetAssetsLiabilities` | small |
| total_assets_less_current_liabilities | 466157 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | small |
| average_employees | 1 | xbrli:pure | 2023-03-31 | 2024-12-20 | filed | yes | `d:AverageNumberEmployeesDuringPeriod` | small |
| average_employees | 1 | xbrli:pure | 2023-03-31 | 2023-12-14 | filed | no | `d:AverageNumberEmployeesDuringPeriod` | small |
| equity | 466157 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `d:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 500 | GBP | 2023-03-31 | 2023-12-14 | filed | no | `d:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 465657 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `d:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 465657 | GBP | 2023-03-31 | 2023-12-14 | filed | no | `d:Equity` | small |
| equity | 466157 | GBP | 2023-03-31 | 2023-12-14 | filed | no | `d:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 500 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `d:Equity` | small |
| net_assets | 466157 | GBP | 2023-03-31 | 2023-12-14 | filed | no | `d:NetAssetsLiabilities` | small |
| net_assets | 466157 | GBP | 2023-03-31 | 2024-12-20 | filed | yes | `d:NetAssetsLiabilities` | small |
| average_employees | 1 | xbrli:pure | 2022-03-31 | 2023-12-14 | filed | yes | `d:AverageNumberEmployeesDuringPeriod` | small |
| equity | 466157 | GBP | 2022-03-31 | 2023-12-14 | filed | yes | `d:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 465657 | GBP | 2022-03-31 | 2023-12-14 | filed | yes | `d:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 500 | GBP | 2022-03-31 | 2023-12-14 | filed | yes | `d:Equity` | small |
| net_assets | 466157 | GBP | 2022-03-31 | 2023-12-14 | filed | yes | `d:NetAssetsLiabilities` | small |

_No coverage facts for the latest run._

## REDBRIX LIMITED (`gb:04890736`)

- registration: `04890736` (GB), status active, incorporated 2003-09-08
- classification: ['62012'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 64 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | iso4217:GBP | 2025-09-30 | 2026-02-22 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2025-09-30 | 2026-02-22 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2025-09-30 | 2026-02-22 | filed | yes | `uk-core:Creditors` | micro-entity |
| equity | 1 | GBP | 2025-09-30 | 2026-02-22 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 1 | GBP | 2025-09-30 | 2026-02-22 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 0 | GBP | 2025-09-30 | 2026-02-22 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 1 | GBP | 2025-09-30 | 2026-02-22 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-09-30 | 2025-06-30 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | dormant |
| average_employees | 1 | iso4217:GBP | 2024-09-30 | 2026-02-22 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2024-09-30 | 2026-02-22 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2024-09-30 | 2025-06-30 | filed | no | `core:Creditors` | dormant |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2024-09-30 | 2025-06-30 | filed | no | `core:Creditors` | dormant |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2024-09-30 | 2026-02-22 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 0 | GBP | 2024-09-30 | 2025-06-30 | filed | yes | `core:CurrentAssets` | dormant |
| equity | 1 | GBP | 2024-09-30 | 2025-06-30 | filed | no | `core:Equity` | dormant |
| equity | 1 | GBP | 2024-09-30 | 2026-02-22 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2024-09-30 | 2025-06-30 | filed | yes | `core:FixedAssets` | dormant |
| net_assets | 1 | GBP | 2024-09-30 | 2025-06-30 | filed | no | `core:NetAssetsLiabilities` | dormant |
| net_assets | 1 | GBP | 2024-09-30 | 2026-02-22 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 0 | GBP | 2024-09-30 | 2026-02-22 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 0 | GBP | 2024-09-30 | 2025-06-30 | filed | no | `core:NetCurrentAssetsLiabilities` | dormant |
| total_assets_less_current_liabilities | 1 | GBP | 2024-09-30 | 2026-02-22 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 1 | GBP | 2024-09-30 | 2025-06-30 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | dormant |
| average_employees | 1 | iso4217:GBP | 2023-09-30 | 2024-06-21 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | dormant |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2023-09-30 | 2024-06-21 | filed | no | `core:Creditors` | dormant |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2023-09-30 | 2025-06-30 | filed | yes | `core:Creditors` | dormant |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2023-09-30 | 2024-06-21 | filed | no | `core:Creditors` | dormant |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2023-09-30 | 2025-06-30 | filed | yes | `core:Creditors` | dormant |
| current_assets | 0 | GBP | 2023-09-30 | 2024-06-21 | filed | no | `core:CurrentAssets` | dormant |
| current_assets | 0 | GBP | 2023-09-30 | 2025-06-30 | filed | yes | `core:CurrentAssets` | dormant |
| equity | 1 | GBP | 2023-09-30 | 2025-06-30 | filed | yes | `core:Equity` | dormant |
| equity | 1 | GBP | 2023-09-30 | 2024-06-21 | filed | no | `core:Equity` | dormant |
| fixed_assets | 0 | GBP | 2023-09-30 | 2024-06-21 | filed | no | `core:FixedAssets` | dormant |
| fixed_assets | 0 | GBP | 2023-09-30 | 2025-06-30 | filed | yes | `core:FixedAssets` | dormant |
| net_assets | 1 | GBP | 2023-09-30 | 2024-06-21 | filed | no | `core:NetAssetsLiabilities` | dormant |
| net_assets | 1 | GBP | 2023-09-30 | 2025-06-30 | filed | yes | `core:NetAssetsLiabilities` | dormant |
| net_current_assets | 0 | GBP | 2023-09-30 | 2025-06-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | dormant |
| net_current_assets | 0 | GBP | 2023-09-30 | 2024-06-21 | filed | no | `core:NetCurrentAssetsLiabilities` | dormant |
| total_assets_less_current_liabilities | 1 | GBP | 2023-09-30 | 2025-06-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | dormant |
| total_assets_less_current_liabilities | 1 | GBP | 2023-09-30 | 2024-06-21 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | dormant |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2022-09-30 | 2024-06-21 | filed | yes | `core:Creditors` | dormant |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2022-09-30 | 2024-06-21 | filed | yes | `core:Creditors` | dormant |
| current_assets | 0 | GBP | 2022-09-30 | 2024-06-21 | filed | yes | `core:CurrentAssets` | dormant |
| equity | 1 | GBP | 2022-09-30 | 2024-06-21 | filed | yes | `core:Equity` | dormant |
| fixed_assets | 0 | GBP | 2022-09-30 | 2024-06-21 | filed | yes | `core:FixedAssets` | dormant |
| net_assets | 1 | GBP | 2022-09-30 | 2024-06-21 | filed | yes | `core:NetAssetsLiabilities` | dormant |
| net_current_assets | 0 | GBP | 2022-09-30 | 2024-06-21 | filed | yes | `core:NetCurrentAssetsLiabilities` | dormant |
| total_assets_less_current_liabilities | 1 | GBP | 2022-09-30 | 2024-06-21 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | dormant |

_No coverage facts for the latest run._

## EPX LIMITED (`gb:05400600`)

- registration: `05400600` (GB), status active, incorporated 2005-03-21
- classification: ['62020'] (sic_2007)
- records: 4 officers, 3 beneficial owners, 0 ownership statements, 0 security interests, 63 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 22 | xbrli:pure | 2025-03-31 | 2025-12-22 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 308385 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 749269 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 438705 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 438705 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 502385 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 502485 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `ns5:Equity` | total-exemption-full |
| fixed_assets | 48533 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| net_assets | 502485 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 471918 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 520451 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 20 | xbrli:pure | 2024-03-31 | 2024-11-26 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 20 | xbrli:pure | 2024-03-31 | 2025-12-22 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 237627 | GBP | 2024-03-31 | 2024-11-26 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 237627 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 714153 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 714153 | GBP | 2024-03-31 | 2024-11-26 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 472366 | GBP | 2024-03-31 | 2024-11-26 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 472366 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 472366 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 472366 | GBP | 2024-03-31 | 2024-11-26 | filed | no | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 396759 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 396759 | GBP | 2024-03-31 | 2024-11-26 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 396859 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 396859 | GBP | 2024-03-31 | 2024-11-26 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-03-31 | 2024-11-26 | filed | no | `ns5:Equity` | total-exemption-full |
| fixed_assets | 23619 | GBP | 2024-03-31 | 2024-11-26 | filed | no | `ns5:FixedAssets` | total-exemption-full |
| fixed_assets | 23619 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| net_assets | 396859 | GBP | 2024-03-31 | 2024-11-26 | filed | no | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 396859 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 394978 | GBP | 2024-03-31 | 2024-11-26 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 394978 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 418597 | GBP | 2024-03-31 | 2024-11-26 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 418597 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 21 | xbrli:pure | 2023-03-31 | 2024-11-26 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 21 | xbrli:pure | 2023-03-31 | 2023-11-23 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 98735 | GBP | 2023-03-31 | 2023-11-23 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 98736 | GBP | 2023-03-31 | 2024-11-26 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 26806 | GBP | 2023-03-31 | 2023-11-23 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 227771 | GBP | 2023-03-31 | 2023-11-23 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 492340 | GBP | 2023-03-31 | 2023-11-23 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 492340 | GBP | 2023-03-31 | 2024-11-26 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 389444 | GBP | 2023-03-31 | 2024-11-26 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 389445 | GBP | 2023-03-31 | 2023-11-23 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 389444 | GBP | 2023-03-31 | 2024-11-26 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 250578 | GBP | 2023-03-31 | 2024-11-26 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-03-31 | 2024-11-26 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 250678 | GBP | 2023-03-31 | 2024-11-26 | filed | yes | `ns5:Equity` | total-exemption-full |
| fixed_assets | 15749 | GBP | 2023-03-31 | 2024-11-26 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| net_assets | 250678 | GBP | 2023-03-31 | 2023-11-23 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 250678 | GBP | 2023-03-31 | 2024-11-26 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 264569 | GBP | 2023-03-31 | 2023-11-23 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 264568 | GBP | 2023-03-31 | 2024-11-26 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 280318 | GBP | 2023-03-31 | 2023-11-23 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 280317 | GBP | 2023-03-31 | 2024-11-26 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 19 | xbrli:pure | 2022-03-31 | 2023-11-23 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 241173 | GBP | 2022-03-31 | 2023-11-23 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 43492 | GBP | 2022-03-31 | 2023-11-23 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 183699 | GBP | 2022-03-31 | 2023-11-23 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 425922 | GBP | 2022-03-31 | 2023-11-23 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 179549 | GBP | 2022-03-31 | 2023-11-23 | filed | yes | `core:Debtors` | total-exemption-full |
| net_assets | 218271 | GBP | 2022-03-31 | 2023-11-23 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 242223 | GBP | 2022-03-31 | 2023-11-23 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 266347 | GBP | 2022-03-31 | 2023-11-23 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2024-11-26: `{"superseded_document_id": "gb:05400600:doc:Z5io4oMVCk-PsJoapyZY1-keZokHVQa8NJQ7sm7gOik", "restatements": [{"concept": "cash", "period_end": "2023-03-31", "old_value": "98735.0000", "new_value": "9873`

## XPERTEX LTD (`gb:05901645`)

- registration: `05901645` (GB), status active, incorporated 2006-08-10
- classification: ['62020', '62090', '95110'] (sic_2007)
- records: 9 officers, 3 beneficial owners, 0 ownership statements, 3 security interests, 80 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## RSP ARCHITECTS LIMITED (`gb:06325895`)

- registration: `06325895` (GB), status active, incorporated 2007-07-26
- classification: ['71111'] (sic_2007)
- records: 3 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 54 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-12-31 | 2026-09-16 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 2833 | GBP | 2025-12-31 | 2026-09-16 | filed | yes | `frs-core:CashBankOnHand` | unaudited-abridged |
| current_assets | 8972 | GBP | 2025-12-31 | 2026-09-16 | filed | yes | `frs-core:CurrentAssets` | unaudited-abridged |
| debtors | 6139 | GBP | 2025-12-31 | 2026-09-16 | filed | yes | `frs-core:Debtors` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 584 | GBP | 2025-12-31 | 2026-09-16 | filed | yes | `frs-core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-12-31 | 2026-09-16 | filed | yes | `frs-core:Equity` | unaudited-abridged |
| fixed_assets | 443 | GBP | 2025-12-31 | 2026-09-16 | filed | yes | `frs-core:FixedAssets` | unaudited-abridged |
| net_assets | 684 | GBP | 2025-12-31 | 2026-09-16 | filed | yes | `frs-core:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 241 | GBP | 2025-12-31 | 2026-09-16 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 684 | GBP | 2025-12-31 | 2026-09-16 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 2 | xbrli:pure | 2024-12-31 | 2026-09-16 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| average_employees | 2 | xbrli:pure | 2024-12-31 | 2025-09-29 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 4484 | GBP | 2024-12-31 | 2026-09-16 | filed | yes | `frs-core:CashBankOnHand` | unaudited-abridged |
| cash | 4484 | GBP | 2024-12-31 | 2025-09-29 | filed | no | `frs-core:CashBankOnHand` | unaudited-abridged |
| current_assets | 11549 | GBP | 2024-12-31 | 2025-09-29 | filed | no | `frs-core:CurrentAssets` | unaudited-abridged |
| current_assets | 11549 | GBP | 2024-12-31 | 2026-09-16 | filed | yes | `frs-core:CurrentAssets` | unaudited-abridged |
| debtors | 7065 | GBP | 2024-12-31 | 2026-09-16 | filed | yes | `frs-core:Debtors` | unaudited-abridged |
| debtors | 7065 | GBP | 2024-12-31 | 2025-09-29 | filed | no | `frs-core:Debtors` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-12-31 | 2025-09-29 | filed | no | `frs-core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-12-31 | 2026-09-16 | filed | yes | `frs-core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 586 | GBP | 2024-12-31 | 2026-09-16 | filed | yes | `frs-core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 586 | GBP | 2024-12-31 | 2025-09-29 | filed | no | `frs-core:Equity` | unaudited-abridged |
| fixed_assets | 591 | GBP | 2024-12-31 | 2025-09-29 | filed | no | `frs-core:FixedAssets` | unaudited-abridged |
| fixed_assets | 591 | GBP | 2024-12-31 | 2026-09-16 | filed | yes | `frs-core:FixedAssets` | unaudited-abridged |
| net_assets | 686 | GBP | 2024-12-31 | 2026-09-16 | filed | yes | `frs-core:NetAssetsLiabilities` | unaudited-abridged |
| net_assets | 686 | GBP | 2024-12-31 | 2025-09-29 | filed | no | `frs-core:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 95 | GBP | 2024-12-31 | 2025-09-29 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 95 | GBP | 2024-12-31 | 2026-09-16 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 686 | GBP | 2024-12-31 | 2025-09-29 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 686 | GBP | 2024-12-31 | 2026-09-16 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 2 | xbrli:pure | 2023-12-31 | 2024-09-19 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| average_employees | 1 | xbrli:pure | 2023-12-31 | 2025-09-29 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 4920 | GBP | 2023-12-31 | 2024-09-19 | filed | no | `frs-core:CashBankOnHand` | unaudited-abridged |
| cash | 4920 | GBP | 2023-12-31 | 2025-09-29 | filed | yes | `frs-core:CashBankOnHand` | unaudited-abridged |
| current_assets | 10991 | GBP | 2023-12-31 | 2024-09-19 | filed | no | `frs-core:CurrentAssets` | unaudited-abridged |
| current_assets | 10991 | GBP | 2023-12-31 | 2025-09-29 | filed | yes | `frs-core:CurrentAssets` | unaudited-abridged |
| debtors | 6071 | GBP | 2023-12-31 | 2024-09-19 | filed | no | `frs-core:Debtors` | unaudited-abridged |
| debtors | 6071 | GBP | 2023-12-31 | 2025-09-29 | filed | yes | `frs-core:Debtors` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-12-31 | 2025-09-29 | filed | yes | `frs-core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-12-31 | 2024-09-19 | filed | no | `frs-core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -100 | GBP | 2023-12-31 | 2024-09-19 | filed | no | `frs-core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -100 | GBP | 2023-12-31 | 2025-09-29 | filed | yes | `frs-core:Equity` | unaudited-abridged |
| fixed_assets | 2704 | GBP | 2023-12-31 | 2025-09-29 | filed | yes | `frs-core:FixedAssets` | unaudited-abridged |
| fixed_assets | 2704 | GBP | 2023-12-31 | 2024-09-19 | filed | no | `frs-core:FixedAssets` | unaudited-abridged |
| net_assets | 0 | GBP | 2023-12-31 | 2025-09-29 | filed | yes | `frs-core:NetAssetsLiabilities` | unaudited-abridged |
| net_assets | 0 | GBP | 2023-12-31 | 2024-09-19 | filed | no | `frs-core:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | -2704 | GBP | 2023-12-31 | 2024-09-19 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| net_current_assets | -2704 | GBP | 2023-12-31 | 2025-09-29 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 0 | GBP | 2023-12-31 | 2024-09-19 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 0 | GBP | 2023-12-31 | 2025-09-29 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 2 | xbrli:pure | 2022-12-31 | 2024-09-19 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 5729 | GBP | 2022-12-31 | 2024-09-19 | filed | yes | `frs-core:CashBankOnHand` | unaudited-abridged |
| current_assets | 12223 | GBP | 2022-12-31 | 2024-09-19 | filed | yes | `frs-core:CurrentAssets` | unaudited-abridged |
| debtors | 6494 | GBP | 2022-12-31 | 2024-09-19 | filed | yes | `frs-core:Debtors` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2022-12-31 | 2024-09-19 | filed | yes | `frs-core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 48 | GBP | 2022-12-31 | 2024-09-19 | filed | yes | `frs-core:Equity` | unaudited-abridged |
| fixed_assets | 2967 | GBP | 2022-12-31 | 2024-09-19 | filed | yes | `frs-core:FixedAssets` | unaudited-abridged |
| net_assets | 148 | GBP | 2022-12-31 | 2024-09-19 | filed | yes | `frs-core:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | -2819 | GBP | 2022-12-31 | 2024-09-19 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 148 | GBP | 2022-12-31 | 2024-09-19 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |

_No coverage facts for the latest run._

- event restatement @ 2025-09-29: `{"superseded_document_id": "gb:06325895:doc:FonGxTgAGglkvdRjK7Zcyyaix3CKH7VZVs2GFjfViGQ", "restatements": [{"concept": "average_employees", "period_end": "2023-12-31", "old_value": "2.0000", "new_valu`

## APNAFINANCE LTD (`gb:06767885`)

- registration: `06767885` (GB), status active, incorporated 2008-12-08
- classification: ['62090'] (sic_2007)
- records: 2 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 38 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | xbrli:pure | 2025-12-31 | 2026-09-28 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 11 | GBP | 2025-12-31 | 2026-09-28 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity | -17212 | GBP | 2025-12-31 | 2026-09-28 | filed | yes | `ns5:Equity` | micro-entity |
| fixed_assets | 308 | GBP | 2025-12-31 | 2026-09-28 | filed | yes | `ns5:FixedAssets` | micro-entity |
| net_current_assets | -17520 | GBP | 2025-12-31 | 2026-09-28 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -17212 | GBP | 2025-12-31 | 2026-09-28 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2024-12-31 | 2025-09-29 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | xbrli:pure | 2024-12-31 | 2026-09-28 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 2 | GBP | 2024-12-31 | 2026-09-28 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| current_assets | 2 | GBP | 2024-12-31 | 2025-09-29 | filed | no | `ns5:CurrentAssets` | micro-entity |
| equity | -16859 | GBP | 2024-12-31 | 2025-09-29 | filed | no | `ns5:Equity` | micro-entity |
| equity | -16859 | GBP | 2024-12-31 | 2026-09-28 | filed | yes | `ns5:Equity` | micro-entity |
| fixed_assets | 362 | GBP | 2024-12-31 | 2026-09-28 | filed | yes | `ns5:FixedAssets` | micro-entity |
| fixed_assets | 362 | GBP | 2024-12-31 | 2025-09-29 | filed | no | `ns5:FixedAssets` | micro-entity |
| net_current_assets | -17221 | GBP | 2024-12-31 | 2025-09-29 | filed | no | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -17221 | GBP | 2024-12-31 | 2026-09-28 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -16859 | GBP | 2024-12-31 | 2026-09-28 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -16859 | GBP | 2024-12-31 | 2025-09-29 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2023-12-31 | 2025-09-29 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | xbrli:pure | 2023-12-31 | 2024-09-24 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 175 | GBP | 2023-12-31 | 2024-09-24 | filed | no | `ns5:CurrentAssets` | micro-entity |
| current_assets | 175 | GBP | 2023-12-31 | 2025-09-29 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity | -16470 | GBP | 2023-12-31 | 2025-09-29 | filed | yes | `ns5:Equity` | micro-entity |
| equity | -16470 | GBP | 2023-12-31 | 2024-09-24 | filed | no | `ns5:Equity` | micro-entity |
| fixed_assets | 426 | GBP | 2023-12-31 | 2024-09-24 | filed | no | `ns5:FixedAssets` | micro-entity |
| fixed_assets | 426 | GBP | 2023-12-31 | 2025-09-29 | filed | yes | `ns5:FixedAssets` | micro-entity |
| net_current_assets | -16896 | GBP | 2023-12-31 | 2024-09-24 | filed | no | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -16896 | GBP | 2023-12-31 | 2025-09-29 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -16470 | GBP | 2023-12-31 | 2024-09-24 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -16470 | GBP | 2023-12-31 | 2025-09-29 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2022-12-31 | 2024-09-24 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 32 | GBP | 2022-12-31 | 2024-09-24 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity | -15486 | GBP | 2022-12-31 | 2024-09-24 | filed | yes | `ns5:Equity` | micro-entity |
| fixed_assets | 501 | GBP | 2022-12-31 | 2024-09-24 | filed | yes | `ns5:FixedAssets` | micro-entity |
| net_current_assets | -15987 | GBP | 2022-12-31 | 2024-09-24 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -15486 | GBP | 2022-12-31 | 2024-09-24 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |

Coverage @ 2025-12-31: 6/21 concepts available (average_employees, current_assets, equity, fixed_assets, net_current_assets, total_assets_less_current_liabilities)
- `cash`: filed_without_concept — regime 'micro-entity' omits this concept
- `creditors_after_one_year`: filed_without_concept — regime 'micro-entity' omits this concept
- `creditors_within_one_year`: filed_without_concept — absent though regime 'micro-entity' typically includes it
- `debtors`: filed_without_concept — regime 'micro-entity' omits this concept
- `depreciation_amortisation`: filed_without_concept — regime 'micro-entity' omits this concept
- `gross_profit`: filed_without_concept — regime 'micro-entity' omits this concept
- `net_assets`: filed_without_concept — absent though regime 'micro-entity' typically includes it
- `operating_profit`: filed_without_concept — regime 'micro-entity' omits this concept
- `profit_before_tax`: filed_without_concept — regime 'micro-entity' omits this concept
- `profit_for_period`: filed_without_concept — regime 'micro-entity' omits this concept
- `retained_earnings`: filed_without_concept — regime 'micro-entity' omits this concept
- `revenue`: filed_without_concept — regime 'micro-entity' omits this concept
- `share_capital`: filed_without_concept — regime 'micro-entity' omits this concept
- `staff_costs`: filed_without_concept — regime 'micro-entity' omits this concept
- `tax_charge`: filed_without_concept — regime 'micro-entity' omits this concept
