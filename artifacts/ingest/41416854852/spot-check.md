# Ingest spot-check

- database: `data/engine.db`
- latest run: `20261102T085818Z-77d2682f`
- companies in store: 41800; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## BENNETT WILLIAMS PARTNERSHIP (MIDLANDS) LIMITED (`gb:02613008`)

- registration: `02613008` (GB), status active, incorporated 1991-05-21
- classification: ['71122'] (sic_2007)
- records: 14 officers, 4 beneficial owners, 0 ownership statements, 3 security interests, 123 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 11 | xbrli:pure | 2025-04-30 | 2026-01-16 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 434780 | GBP | 2025-04-30 | 2026-01-16 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 643114 | GBP | 2025-04-30 | 2026-01-16 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 208334 | GBP | 2025-04-30 | 2026-01-16 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 208334 | GBP | 2025-04-30 | 2026-01-16 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 407626 | GBP | 2025-04-30 | 2026-01-16 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 402626 | GBP | 2025-04-30 | 2026-01-16 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 5000 | GBP | 2025-04-30 | 2026-01-16 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 407626 | GBP | 2025-04-30 | 2026-01-16 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 395605 | GBP | 2025-04-30 | 2026-01-16 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 411547 | GBP | 2025-04-30 | 2026-01-16 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 11 | xbrli:pure | 2024-04-30 | 2025-01-07 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 11 | xbrli:pure | 2024-04-30 | 2026-01-16 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 279263 | GBP | 2024-04-30 | 2026-01-16 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 279263 | GBP | 2024-04-30 | 2025-01-07 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 524603 | GBP | 2024-04-30 | 2025-01-07 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 524603 | GBP | 2024-04-30 | 2026-01-16 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 245340 | GBP | 2024-04-30 | 2025-01-07 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 245340 | GBP | 2024-04-30 | 2025-01-07 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 245340 | GBP | 2024-04-30 | 2026-01-16 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 245340 | GBP | 2024-04-30 | 2026-01-16 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 5000 | GBP | 2024-04-30 | 2025-01-07 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 369291 | GBP | 2024-04-30 | 2026-01-16 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 369291 | GBP | 2024-04-30 | 2025-01-07 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 374291 | GBP | 2024-04-30 | 2025-01-07 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 5000 | GBP | 2024-04-30 | 2026-01-16 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 374291 | GBP | 2024-04-30 | 2026-01-16 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 374291 | GBP | 2024-04-30 | 2025-01-07 | filed | no | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 374291 | GBP | 2024-04-30 | 2026-01-16 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 361143 | GBP | 2024-04-30 | 2026-01-16 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 361143 | GBP | 2024-04-30 | 2025-01-07 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 378569 | GBP | 2024-04-30 | 2025-01-07 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 378569 | GBP | 2024-04-30 | 2026-01-16 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 11 | xbrli:pure | 2023-04-30 | 2025-01-07 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 11 | xbrli:pure | 2023-04-30 | 2024-01-24 | filed | no | `ns6:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 184434 | GBP | 2023-04-30 | 2024-01-24 | filed | no | `ns6:CashBankOnHand` | total-exemption-full |
| cash | 184434 | GBP | 2023-04-30 | 2025-01-07 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 610700 | GBP | 2023-04-30 | 2024-01-24 | filed | no | `ns6:CurrentAssets` | total-exemption-full |
| current_assets | 610700 | GBP | 2023-04-30 | 2025-01-07 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 426266 | GBP | 2023-04-30 | 2024-01-24 | filed | no | `ns6:Debtors` | total-exemption-full |
| debtors | 426266 | GBP | 2023-04-30 | 2024-01-24 | filed | no | `ns6:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 426266 | GBP | 2023-04-30 | 2025-01-07 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 426266 | GBP | 2023-04-30 | 2025-01-07 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 397684 | GBP | 2023-04-30 | 2025-01-07 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 5000 | GBP | 2023-04-30 | 2025-01-07 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 5000 | GBP | 2023-04-30 | 2024-01-24 | filed | no | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 392684 | GBP | 2023-04-30 | 2024-01-24 | filed | no | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 392684 | GBP | 2023-04-30 | 2025-01-07 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 397684 | GBP | 2023-04-30 | 2024-01-24 | filed | no | `ns6:Equity` | total-exemption-full |
| net_assets | 397684 | GBP | 2023-04-30 | 2024-01-24 | filed | no | `ns6:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 397684 | GBP | 2023-04-30 | 2025-01-07 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 384371 | GBP | 2023-04-30 | 2024-01-24 | filed | no | `ns6:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 384371 | GBP | 2023-04-30 | 2025-01-07 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 400814 | GBP | 2023-04-30 | 2024-01-24 | filed | no | `ns6:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 400814 | GBP | 2023-04-30 | 2025-01-07 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 10 | xbrli:pure | 2022-04-30 | 2024-01-24 | filed | yes | `ns6:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 160069 | GBP | 2022-04-30 | 2024-01-24 | filed | yes | `ns6:CashBankOnHand` | total-exemption-full |
| current_assets | 479097 | GBP | 2022-04-30 | 2024-01-24 | filed | yes | `ns6:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 319028 | GBP | 2022-04-30 | 2024-01-24 | filed | yes | `ns6:Debtors` | total-exemption-full |
| debtors | 319028 | GBP | 2022-04-30 | 2024-01-24 | filed | yes | `ns6:Debtors` | total-exemption-full |
| equity | 322425 | GBP | 2022-04-30 | 2024-01-24 | filed | yes | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 5000 | GBP | 2022-04-30 | 2024-01-24 | filed | yes | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 317425 | GBP | 2022-04-30 | 2024-01-24 | filed | yes | `ns6:Equity` | total-exemption-full |
| net_assets | 322425 | GBP | 2022-04-30 | 2024-01-24 | filed | yes | `ns6:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 310572 | GBP | 2022-04-30 | 2024-01-24 | filed | yes | `ns6:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 325095 | GBP | 2022-04-30 | 2024-01-24 | filed | yes | `ns6:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## RED DOVE CONSULTANTS LIMITED (`gb:03254303`)

- registration: `03254303` (GB), status active, incorporated 1996-09-24
- classification: ['62012', '62020'] (sic_2007)
- records: 4 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 69 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-10-31 | 2026-07-24 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 339647.83 | GBP | 2025-10-31 | 2026-07-24 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 339647.83 | GBP | 2025-10-31 | 2026-07-24 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 339647.83 | GBP | 2025-10-31 | 2026-07-24 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 339647.83 | GBP | 2025-10-31 | 2026-07-24 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 339647.83 | GBP | 2025-10-31 | 2026-07-24 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-10-31 | 2025-07-24 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-10-31 | 2026-07-24 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 349264 | GBP | 2024-10-31 | 2026-07-24 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 349264 | GBP | 2024-10-31 | 2025-07-24 | filed | no | `core:Equity` | micro-entity |
| equity | 349264 | GBP | 2024-10-31 | 2026-07-24 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 349264 | GBP | 2024-10-31 | 2025-07-24 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 349264 | GBP | 2024-10-31 | 2025-07-24 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 349264 | GBP | 2024-10-31 | 2026-07-24 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 349264 | GBP | 2024-10-31 | 2026-07-24 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 349264 | GBP | 2024-10-31 | 2025-07-24 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 349264 | GBP | 2024-10-31 | 2026-07-24 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-10-31 | 2024-07-26 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 359985 | GBP | 2023-10-31 | 2024-07-26 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 359985 | GBP | 2023-10-31 | 2025-07-24 | filed | yes | `core:Equity` | micro-entity |
| equity | 359985 | GBP | 2023-10-31 | 2024-07-26 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 359985 | GBP | 2023-10-31 | 2025-07-24 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 359985 | GBP | 2023-10-31 | 2024-07-26 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 359985 | GBP | 2023-10-31 | 2025-07-24 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 359985 | GBP | 2023-10-31 | 2024-07-26 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 359985 | GBP | 2023-10-31 | 2024-07-26 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 359985 | GBP | 2023-10-31 | 2025-07-24 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| current_assets | 376210 | GBP | 2022-10-31 | 2024-07-26 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 376210 | GBP | 2022-10-31 | 2024-07-26 | filed | yes | `core:Equity` | micro-entity |
| net_assets | 376210 | GBP | 2022-10-31 | 2024-07-26 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 376210 | GBP | 2022-10-31 | 2024-07-26 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 376210 | GBP | 2022-10-31 | 2024-07-26 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## ERMS LIMITED (`gb:03724103`)

- registration: `03724103` (GB), status active, incorporated 1999-03-02
- classification: ['62020'] (sic_2007)
- records: 2 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 66 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | iso4217:GBP | 2025-03-31 | 2025-12-31 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 1969 | GBP | 2025-03-31 | 2025-12-31 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 7987 | GBP | 2025-03-31 | 2025-12-31 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 19850 | GBP | 2025-03-31 | 2025-12-31 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 9894 | GBP | 2025-03-31 | 2025-12-31 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2025-03-31 | 2025-12-31 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 9894 | GBP | 2025-03-31 | 2025-12-31 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 11863 | GBP | 2025-03-31 | 2025-12-31 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 11863 | GBP | 2025-03-31 | 2025-12-31 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-03-31 | 2024-12-31 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 3387 | GBP | 2024-03-31 | 2025-12-31 | filed | yes | `core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 3387 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 20789 | GBP | 2024-03-31 | 2025-12-31 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 20789 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 26066 | GBP | 2024-03-31 | 2025-12-31 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 26066 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 1890 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `core:Equity` | micro-entity |
| equity | 1890 | GBP | 2024-03-31 | 2025-12-31 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2024-03-31 | 2025-12-31 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 0 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | 1890 | GBP | 2024-03-31 | 2025-12-31 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 1890 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 5277 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 5277 | GBP | 2024-03-31 | 2025-12-31 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 5277 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 5277 | GBP | 2024-03-31 | 2025-12-31 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-03-31 | 2023-12-29 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 4906 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 4906 | GBP | 2023-03-31 | 2023-12-29 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 25286 | GBP | 2023-03-31 | 2023-12-29 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 25286 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 30257 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 30257 | GBP | 2023-03-31 | 2023-12-29 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 65 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `core:Equity` | micro-entity |
| equity | 65 | GBP | 2023-03-31 | 2023-12-29 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 0 | GBP | 2023-03-31 | 2023-12-29 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | 65 | GBP | 2023-03-31 | 2023-12-29 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 65 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 4971 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 4971 | GBP | 2023-03-31 | 2023-12-29 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 4971 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 4971 | GBP | 2023-03-31 | 2023-12-29 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 12635 | GBP | 2022-03-31 | 2023-12-29 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 21279 | GBP | 2022-03-31 | 2023-12-29 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 33950 | GBP | 2022-03-31 | 2023-12-29 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 36 | GBP | 2022-03-31 | 2023-12-29 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2022-03-31 | 2023-12-29 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 36 | GBP | 2022-03-31 | 2023-12-29 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 12671 | GBP | 2022-03-31 | 2023-12-29 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 12671 | GBP | 2022-03-31 | 2023-12-29 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## METALWORKING SOLUTIONS LTD (`gb:04185389`)

- registration: `04185389` (GB), status active, incorporated 2001-03-22
- classification: ['45112', '45190', '70229', '71129'] (sic_2007)
- records: 18 officers, 4 beneficial owners, 0 ownership statements, 0 security interests, 178 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.01 | xbrli:pure | 2025-03-31 | 2026-06-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 45728 | GBP | 2025-03-31 | 2026-06-30 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 72515 | GBP | 2025-03-31 | 2026-06-30 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -6014 | GBP | 2025-03-31 | 2026-06-30 | filed | yes | `core:Equity` | micro-entity |
| net_assets | -6014 | GBP | 2025-03-31 | 2026-06-30 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 26787 | GBP | 2025-03-31 | 2026-06-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| average_employees | 0.01 | xbrli:pure | 2024-03-31 | 2026-06-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-03-31 | 2024-12-29 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 47091 | GBP | 2024-03-31 | 2026-06-30 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 47091 | GBP | 2024-03-31 | 2024-12-29 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 52395 | GBP | 2024-03-31 | 2024-12-29 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 52395 | GBP | 2024-03-31 | 2026-06-30 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -27497 | GBP | 2024-03-31 | 2024-12-29 | filed | no | `core:Equity` | micro-entity |
| equity | -27497 | GBP | 2024-03-31 | 2026-06-30 | filed | yes | `core:Equity` | micro-entity |
| net_assets | -27497 | GBP | 2024-03-31 | 2026-06-30 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 5304 | GBP | 2024-03-31 | 2026-06-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-03-31 | 2024-03-31 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-03-31 | 2024-12-29 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 45522 | GBP | 2023-03-31 | 2024-03-31 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 45522 | GBP | 2023-03-31 | 2024-12-29 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 48575 | GBP | 2023-03-31 | 2024-12-29 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 48575 | GBP | 2023-03-31 | 2024-03-31 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | -29748 | GBP | 2023-03-31 | 2024-12-29 | filed | yes | `core:Equity` | micro-entity |
| equity | -29748 | GBP | 2023-03-31 | 2024-03-31 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2023-03-31 | 2024-03-31 | filed | yes | `core:FixedAssets` | micro-entity |
| average_employees | 1 | xbrli:pure | 2022-03-31 | 2024-03-31 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 38201 | GBP | 2022-03-31 | 2024-03-31 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 48250 | GBP | 2022-03-31 | 2024-03-31 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -29306 | GBP | 2022-03-31 | 2024-03-31 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 541 | GBP | 2022-03-31 | 2024-03-31 | filed | yes | `core:FixedAssets` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2026-06-30: `{"superseded_document_id": "gb:04185389:doc:o6wViZDRQXKlqLbeWw_aWTrs-ybr0Ap0h6QvNPke0bA", "restatements": [{"concept": "average_employees", "period_end": "2024-03-31", "old_value": "1.0000", "new_valu`

## TRAILSTREAM LIMITED (`gb:04650419`)

- registration: `04650419` (GB), status active, incorporated 2003-01-28
- classification: ['59112', '62090'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 5 security interests, 74 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | xbrli:pure | 2024-12-31 | 2025-04-07 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 25395 | GBP | 2024-12-31 | 2025-04-07 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 26087 | GBP | 2024-12-31 | 2025-04-07 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 692 | GBP | 2024-12-31 | 2025-04-07 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 692 | GBP | 2024-12-31 | 2025-04-07 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 24475 | GBP | 2024-12-31 | 2025-04-07 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2024-12-31 | 2025-04-07 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 24476 | GBP | 2024-12-31 | 2025-04-07 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 24476 | GBP | 2024-12-31 | 2025-04-07 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 24476 | GBP | 2024-12-31 | 2025-04-07 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -5372 | GBP | 2024-12-31 | 2025-04-07 | filed | yes | `ns5:ProfitLoss` | total-exemption-full |
| total_assets_less_current_liabilities | 24476 | GBP | 2024-12-31 | 2025-04-07 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0 | xbrli:pure | 2024-03-31 | 2025-04-07 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 0 | xbrli:pure | 2024-03-31 | 2024-12-19 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 30601 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 30601 | GBP | 2024-03-31 | 2025-04-07 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 89238 | GBP | 2024-03-31 | 2025-04-07 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 89238 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 58637 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 58637 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 58637 | GBP | 2024-03-31 | 2025-04-07 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 58637 | GBP | 2024-03-31 | 2025-04-07 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 59447 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2024-03-31 | 2025-04-07 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 59448 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 59448 | GBP | 2024-03-31 | 2025-04-07 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 59447 | GBP | 2024-03-31 | 2025-04-07 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 59448 | GBP | 2024-03-31 | 2025-04-07 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 59448 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 71865 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 71865 | GBP | 2024-03-31 | 2025-04-07 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -18577 | GBP | 2024-03-31 | 2024-12-19 | filed | yes | `ns5:ProfitLoss` | total-exemption-full |
| total_assets_less_current_liabilities | 71865 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 71865 | GBP | 2024-03-31 | 2025-04-07 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0 | xbrli:pure | 2023-03-31 | 2024-12-19 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 57163 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 198068 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 140905 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 140905 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 96025 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 96024 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 96025 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 118008 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 118394 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## SYSTENA LIMITED (`gb:05137618`)

- registration: `05137618` (GB), status active, incorporated 2004-05-25
- classification: ['62020'] (sic_2007)
- records: 2 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 54 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-03-31 | 2025-12-19 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2426 | GBP | 2025-03-31 | 2025-12-19 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 3661 | GBP | 2025-03-31 | 2025-12-19 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 435 | GBP | 2025-03-31 | 2025-12-19 | filed | yes | `core:Equity` | micro-entity |
| net_current_assets | 1235 | GBP | 2025-03-31 | 2025-12-19 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 1235 | GBP | 2025-03-31 | 2025-12-19 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-03-31 | 2024-11-12 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-03-31 | 2025-12-19 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2071 | GBP | 2024-03-31 | 2024-11-12 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2071 | GBP | 2024-03-31 | 2025-12-19 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 3142 | GBP | 2024-03-31 | 2025-12-19 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 3142 | GBP | 2024-03-31 | 2024-11-12 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | 271 | GBP | 2024-03-31 | 2025-12-19 | filed | yes | `core:Equity` | micro-entity |
| equity | 271 | GBP | 2024-03-31 | 2024-11-12 | filed | no | `uk-core:Equity` | micro-entity |
| net_assets | 271 | GBP | 2024-03-31 | 2024-11-12 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 1071 | GBP | 2024-03-31 | 2025-12-19 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 1071 | GBP | 2024-03-31 | 2024-11-12 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 1071 | GBP | 2024-03-31 | 2025-12-19 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 1071 | GBP | 2024-03-31 | 2024-11-12 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-03-31 | 2024-11-12 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-03-31 | 2023-12-15 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 8057 | GBP | 2023-03-31 | 2024-11-12 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 8057 | GBP | 2023-03-31 | 2023-12-15 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 21031 | GBP | 2023-03-31 | 2023-12-15 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 21031 | GBP | 2023-03-31 | 2024-11-12 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 12174 | GBP | 2023-03-31 | 2024-11-12 | filed | yes | `uk-core:Equity` | micro-entity |
| equity | 12174 | GBP | 2023-03-31 | 2023-12-15 | filed | no | `uk-core:Equity` | micro-entity |
| net_assets | 12174 | GBP | 2023-03-31 | 2023-12-15 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 12174 | GBP | 2023-03-31 | 2024-11-12 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 12974 | GBP | 2023-03-31 | 2024-11-12 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 12974 | GBP | 2023-03-31 | 2023-12-15 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 12974 | GBP | 2023-03-31 | 2024-11-12 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 12974 | GBP | 2023-03-31 | 2023-12-15 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2022-03-31 | 2023-12-15 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 17723 | GBP | 2022-03-31 | 2023-12-15 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 41562 | GBP | 2022-03-31 | 2023-12-15 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 23039 | GBP | 2022-03-31 | 2023-12-15 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 23039 | GBP | 2022-03-31 | 2023-12-15 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 23839 | GBP | 2022-03-31 | 2023-12-15 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 23839 | GBP | 2022-03-31 | 2023-12-15 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## NOMINAL - T LTD (`gb:05599133`)

- registration: `05599133` (GB), status active, incorporated 2005-10-20
- classification: ['71129'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 58 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | iso4217:GBP | 2026-03-31 | 2026-07-01 | filed | yes | `pt:AverageNumberEmployeesDuringPeriod` | micro-entity |
| net_assets | 1751 | GBP | 2026-03-31 | 2026-07-01 | filed | yes | `pt:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 2629 | GBP | 2026-03-31 | 2026-07-01 | filed | yes | `pt:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 2999 | GBP | 2026-03-31 | 2026-07-01 | filed | yes | `pt:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2025-03-31 | 2025-07-11 | filed | yes | `pt:AverageNumberEmployeesDuringPeriod` | micro-entity |
| net_assets | 8263 | GBP | 2025-03-31 | 2026-07-01 | filed | yes | `pt:NetAssetsLiabilities` | micro-entity |
| net_assets | 8263 | GBP | 2025-03-31 | 2025-07-11 | filed | no | `pt:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 9408 | GBP | 2025-03-31 | 2025-07-11 | filed | yes | `pt:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 9463 | GBP | 2025-03-31 | 2025-07-11 | filed | no | `pt:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 9463 | GBP | 2025-03-31 | 2026-07-01 | filed | yes | `pt:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-03-31 | 2024-07-30 | filed | yes | `pt:AverageNumberEmployeesDuringPeriod` | micro-entity |
| net_assets | 2752 | GBP | 2024-03-31 | 2024-07-30 | filed | no | `pt:NetAssetsLiabilities` | micro-entity |
| net_assets | 2752 | GBP | 2024-03-31 | 2025-07-11 | filed | yes | `pt:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 3673 | GBP | 2024-03-31 | 2024-07-30 | filed | yes | `pt:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 3748 | GBP | 2024-03-31 | 2024-07-30 | filed | no | `pt:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 3748 | GBP | 2024-03-31 | 2025-07-11 | filed | yes | `pt:TotalAssetsLessCurrentLiabilities` | micro-entity |
| net_assets | 7094 | GBP | 2023-03-31 | 2024-07-30 | filed | yes | `pt:NetAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 8054 | GBP | 2023-03-31 | 2024-07-30 | filed | yes | `pt:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## ICW ASSOCIATES LIMITED (`gb:06040579`)

- registration: `06040579` (GB), status active, incorporated 2007-01-03
- classification: ['62020'] (sic_2007)
- records: 5 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 49 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-11-30 | 2026-07-13 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 42923 | GBP | 2025-11-30 | 2026-07-13 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 60036 | GBP | 2025-11-30 | 2026-07-13 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 17113 | GBP | 2025-11-30 | 2026-07-13 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 17113 | GBP | 2025-11-30 | 2026-07-13 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2025-11-30 | 2026-07-13 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 46716 | GBP | 2025-11-30 | 2026-07-13 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 46717 | GBP | 2025-11-30 | 2026-07-13 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 46717 | GBP | 2025-11-30 | 2026-07-13 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 46416 | GBP | 2025-11-30 | 2026-07-13 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 46717 | GBP | 2025-11-30 | 2026-07-13 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-11-30 | 2025-05-15 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| average_employees | 1 | xbrli:pure | 2024-11-30 | 2026-07-13 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 51137 | GBP | 2024-11-30 | 2025-05-15 | filed | no | `ns5:CashBankOnHand` | unaudited-abridged |
| cash | 51137 | GBP | 2024-11-30 | 2026-07-13 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 65948 | GBP | 2024-11-30 | 2026-07-13 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 65948 | GBP | 2024-11-30 | 2025-05-15 | filed | no | `ns5:CurrentAssets` | unaudited-abridged |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 14811 | GBP | 2024-11-30 | 2026-07-13 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 14811 | GBP | 2024-11-30 | 2025-05-15 | filed | no | `ns5:Debtors` | unaudited-abridged |
| debtors | 14811 | GBP | 2024-11-30 | 2026-07-13 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 51651 | GBP | 2024-11-30 | 2026-07-13 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2024-11-30 | 2025-05-15 | filed | no | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 51651 | GBP | 2024-11-30 | 2025-05-15 | filed | no | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2024-11-30 | 2026-07-13 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 51652 | GBP | 2024-11-30 | 2026-07-13 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 51652 | GBP | 2024-11-30 | 2025-05-15 | filed | no | `ns5:Equity` | unaudited-abridged |
| net_assets | 51652 | GBP | 2024-11-30 | 2025-05-15 | filed | no | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_assets | 51652 | GBP | 2024-11-30 | 2026-07-13 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 51201 | GBP | 2024-11-30 | 2026-07-13 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 51201 | GBP | 2024-11-30 | 2025-05-15 | filed | no | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 51802 | GBP | 2024-11-30 | 2026-07-13 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 51802 | GBP | 2024-11-30 | 2025-05-15 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 1 | xbrli:pure | 2023-11-30 | 2024-04-25 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| average_employees | 1 | xbrli:pure | 2023-11-30 | 2025-05-15 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 69942 | GBP | 2023-11-30 | 2024-04-25 | filed | no | `ns5:CashBankOnHand` | unaudited-abridged |
| cash | 69942 | GBP | 2023-11-30 | 2025-05-15 | filed | yes | `ns5:CashBankOnHand` | unaudited-abridged |
| current_assets | 77848 | GBP | 2023-11-30 | 2025-05-15 | filed | yes | `ns5:CurrentAssets` | unaudited-abridged |
| current_assets | 77848 | GBP | 2023-11-30 | 2024-04-25 | filed | no | `ns5:CurrentAssets` | unaudited-abridged |
| debtors | 7906 | GBP | 2023-11-30 | 2025-05-15 | filed | yes | `ns5:Debtors` | unaudited-abridged |
| debtors | 7906 | GBP | 2023-11-30 | 2024-04-25 | filed | no | `ns5:Debtors` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2023-11-30 | 2024-04-25 | filed | no | `ns5:Equity` | unaudited-abridged |
| equity | 63378 | GBP | 2023-11-30 | 2024-04-25 | filed | no | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2023-11-30 | 2025-05-15 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 63377 | GBP | 2023-11-30 | 2025-05-15 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity | 63378 | GBP | 2023-11-30 | 2025-05-15 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 63377 | GBP | 2023-11-30 | 2024-04-25 | filed | no | `ns5:Equity` | unaudited-abridged |
| net_assets | 63378 | GBP | 2023-11-30 | 2024-04-25 | filed | no | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_assets | 63378 | GBP | 2023-11-30 | 2025-05-15 | filed | yes | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 63179 | GBP | 2023-11-30 | 2024-04-25 | filed | no | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 63179 | GBP | 2023-11-30 | 2025-05-15 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 63445 | GBP | 2023-11-30 | 2024-04-25 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 63445 | GBP | 2023-11-30 | 2025-05-15 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 1 | xbrli:pure | 2022-11-30 | 2024-04-25 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 74285 | GBP | 2022-11-30 | 2024-04-25 | filed | yes | `ns5:CashBankOnHand` | unaudited-abridged |
| current_assets | 81850 | GBP | 2022-11-30 | 2024-04-25 | filed | yes | `ns5:CurrentAssets` | unaudited-abridged |
| debtors | 7565 | GBP | 2022-11-30 | 2024-04-25 | filed | yes | `ns5:Debtors` | unaudited-abridged |
| equity | 66651 | GBP | 2022-11-30 | 2024-04-25 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2022-11-30 | 2024-04-25 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 66650 | GBP | 2022-11-30 | 2024-04-25 | filed | yes | `ns5:Equity` | unaudited-abridged |
| net_assets | 66651 | GBP | 2022-11-30 | 2024-04-25 | filed | yes | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 66177 | GBP | 2022-11-30 | 2024-04-25 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 66762 | GBP | 2022-11-30 | 2024-04-25 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |

_No coverage facts for the latest run._

## MICROWORKS LIMITED (`gb:06434086`)

- registration: `06434086` (GB), status active, incorporated 2007-11-22
- classification: ['62012'] (sic_2007)
- records: 5 officers, 0 beneficial owners, 1 ownership statements, 0 security interests, 66 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 4 | xbrli:pure | 2025-12-31 | 2026-09-10 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 26351 | GBP | 2025-12-31 | 2026-09-10 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 434 | GBP | 2025-12-31 | 2026-09-10 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -27277 | GBP | 2025-12-31 | 2026-09-10 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 25 | GBP | 2025-12-31 | 2026-09-10 | filed | yes | `core:FixedAssets` | micro-entity |
| net_current_assets | -25917 | GBP | 2025-12-31 | 2026-09-10 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -25892 | GBP | 2025-12-31 | 2026-09-10 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 4 | xbrli:pure | 2024-12-31 | 2026-09-10 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 4 | xbrli:pure | 2024-12-31 | 2025-09-11 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 23172 | GBP | 2024-12-31 | 2026-09-10 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 23172 | GBP | 2024-12-31 | 2025-09-11 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 248 | GBP | 2024-12-31 | 2026-09-10 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 248 | GBP | 2024-12-31 | 2025-09-11 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | -23938 | GBP | 2024-12-31 | 2026-09-10 | filed | yes | `core:Equity` | micro-entity |
| equity | -23938 | GBP | 2024-12-31 | 2025-09-11 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 301 | GBP | 2024-12-31 | 2026-09-10 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 301 | GBP | 2024-12-31 | 2025-09-11 | filed | no | `core:FixedAssets` | micro-entity |
| net_current_assets | -22924 | GBP | 2024-12-31 | 2025-09-11 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -22924 | GBP | 2024-12-31 | 2026-09-10 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -22623 | GBP | 2024-12-31 | 2026-09-10 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -22623 | GBP | 2024-12-31 | 2025-09-11 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 4 | xbrli:pure | 2023-12-31 | 2024-09-02 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 4 | xbrli:pure | 2023-12-31 | 2025-09-11 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 17971 | GBP | 2023-12-31 | 2024-09-02 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 17971 | GBP | 2023-12-31 | 2025-09-11 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 497 | GBP | 2023-12-31 | 2024-09-02 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 497 | GBP | 2023-12-31 | 2025-09-11 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -18050 | GBP | 2023-12-31 | 2024-09-02 | filed | no | `core:Equity` | micro-entity |
| equity | -18050 | GBP | 2023-12-31 | 2025-09-11 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 579 | GBP | 2023-12-31 | 2024-09-02 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 579 | GBP | 2023-12-31 | 2025-09-11 | filed | yes | `core:FixedAssets` | micro-entity |
| net_current_assets | -17474 | GBP | 2023-12-31 | 2025-09-11 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -17474 | GBP | 2023-12-31 | 2024-09-02 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -16895 | GBP | 2023-12-31 | 2025-09-11 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -16895 | GBP | 2023-12-31 | 2024-09-02 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 4 | xbrli:pure | 2022-12-31 | 2024-09-02 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 18428 | GBP | 2022-12-31 | 2024-09-02 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 425 | GBP | 2022-12-31 | 2024-09-02 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -18382 | GBP | 2022-12-31 | 2024-09-02 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 721 | GBP | 2022-12-31 | 2024-09-02 | filed | yes | `core:FixedAssets` | micro-entity |
| net_current_assets | -18003 | GBP | 2022-12-31 | 2024-09-02 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -17282 | GBP | 2022-12-31 | 2024-09-02 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._
