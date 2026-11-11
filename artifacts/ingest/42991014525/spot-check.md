# Ingest spot-check

- database: `data/engine.db`
- latest run: `20261111T085729Z-753207fb`
- companies in store: 49000; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## IONICAL LIMITED (`gb:02752143`)

- registration: `02752143` (GB), status active, incorporated 1992-10-01
- classification: ['62012'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 1 security interests, 103 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | iso4217:GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 29236 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 23521 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 194 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -52471 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:Equity` | micro-entity |
| net_assets | -52471 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -23327 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -23235 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-03-31 | 2024-12-31 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 30129 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 30129 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 23521 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 23521 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 1 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 1 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | -53557 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `core:Equity` | micro-entity |
| equity | -53557 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2024-03-31 | 2024-12-31 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | -53557 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | -53557 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -23520 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -23520 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -23428 | GBP | 2024-03-31 | 2024-12-31 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -23428 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 3 | iso4217:GBP | 2023-03-31 | 2023-12-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 37039 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 37039 | GBP | 2023-03-31 | 2023-12-30 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 23301 | GBP | 2023-03-31 | 2023-12-30 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 23301 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 116 | GBP | 2023-03-31 | 2023-12-30 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 116 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -60132 | GBP | 2023-03-31 | 2023-12-30 | filed | no | `core:Equity` | micro-entity |
| equity | -60132 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2023-03-31 | 2023-12-30 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 0 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | -60132 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | -60132 | GBP | 2023-03-31 | 2023-12-30 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -23185 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -23185 | GBP | 2023-03-31 | 2023-12-30 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -23093 | GBP | 2023-03-31 | 2024-12-31 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -23093 | GBP | 2023-03-31 | 2023-12-30 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 48133 | GBP | 2022-03-31 | 2023-12-30 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 37815 | GBP | 2022-03-31 | 2023-12-30 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 75211 | GBP | 2022-03-31 | 2023-12-30 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -10645 | GBP | 2022-03-31 | 2023-12-30 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2022-03-31 | 2023-12-30 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | -10645 | GBP | 2022-03-31 | 2023-12-30 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 37396 | GBP | 2022-03-31 | 2023-12-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 37488 | GBP | 2022-03-31 | 2023-12-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## CH DESIGN EUROPE LIMITED (`gb:03431772`)

- registration: `03431772` (GB), status active, incorporated 1997-09-10
- classification: ['71111'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 79 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.01 | xbrli:pure | 2024-12-31 | 2025-12-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 23244 | GBP | 2024-12-31 | 2025-12-30 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 61217 | GBP | 2024-12-31 | 2025-12-30 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 37973 | GBP | 2024-12-31 | 2025-12-30 | filed | yes | `core:Equity` | micro-entity |
| net_assets | 37973 | GBP | 2024-12-31 | 2025-12-30 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 37973 | GBP | 2024-12-31 | 2025-12-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| average_employees | 0.01 | xbrli:pure | 2023-12-31 | 2025-12-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-12-31 | 2024-09-30 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 28696 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 28696 | GBP | 2023-12-31 | 2025-12-30 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 65869 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 65869 | GBP | 2023-12-31 | 2025-12-30 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 37173 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:Equity` | micro-entity |
| equity | 37173 | GBP | 2023-12-31 | 2025-12-30 | filed | yes | `core:Equity` | micro-entity |
| net_assets | 37173 | GBP | 2023-12-31 | 2025-12-30 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 37173 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 37173 | GBP | 2023-12-31 | 2025-12-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 37173 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2022-12-31 | 2024-09-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 26185 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 67303 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 41118 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:Equity` | micro-entity |
| net_assets | 41118 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 41118 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2025-12-30: `{"superseded_document_id": "gb:03431772:doc:2WvzlQMZ4SGJwMdb6DvoC6R7Jl3Uozgw8fnGmzWrp7I", "restatements": [{"concept": "average_employees", "period_end": "2023-12-31", "old_value": "1.0000", "new_valu`

## ADVANCED WEB DESIGNS LIMITED (`gb:03956949`)

- registration: `03956949` (GB), status active, incorporated 2000-03-27
- classification: ['62090'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 61 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 3 | xbrli:pure | 2025-03-31 | 2025-12-29 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 37579 | GBP | 2025-03-31 | 2025-12-29 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity | 68 | GBP | 2025-03-31 | 2025-12-29 | filed | yes | `ns5:Equity` | micro-entity |
| fixed_assets | 1294 | GBP | 2025-03-31 | 2025-12-29 | filed | yes | `ns5:FixedAssets` | micro-entity |
| net_assets | 68 | GBP | 2025-03-31 | 2025-12-29 | filed | yes | `ns5:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 347 | GBP | 2025-03-31 | 2025-12-29 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 1641 | GBP | 2025-03-31 | 2025-12-29 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 4 | xbrli:pure | 2024-03-31 | 2024-12-22 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 4 | xbrli:pure | 2024-03-31 | 2025-12-29 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 45665 | GBP | 2024-03-31 | 2024-12-22 | filed | no | `ns5:CurrentAssets` | micro-entity |
| current_assets | 45665 | GBP | 2024-03-31 | 2025-12-29 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity | -915 | GBP | 2024-03-31 | 2025-12-29 | filed | yes | `ns5:Equity` | micro-entity |
| equity | -915 | GBP | 2024-03-31 | 2024-12-22 | filed | no | `ns5:Equity` | micro-entity |
| fixed_assets | 1725 | GBP | 2024-03-31 | 2024-12-22 | filed | no | `ns5:FixedAssets` | micro-entity |
| fixed_assets | 1725 | GBP | 2024-03-31 | 2025-12-29 | filed | yes | `ns5:FixedAssets` | micro-entity |
| net_assets | -915 | GBP | 2024-03-31 | 2024-12-22 | filed | no | `ns5:NetAssetsLiabilities` | micro-entity |
| net_assets | -915 | GBP | 2024-03-31 | 2025-12-29 | filed | yes | `ns5:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 7246 | GBP | 2024-03-31 | 2025-12-29 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 7246 | GBP | 2024-03-31 | 2024-12-22 | filed | no | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 8971 | GBP | 2024-03-31 | 2025-12-29 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 8971 | GBP | 2024-03-31 | 2024-12-22 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 4 | xbrli:pure | 2023-03-31 | 2024-12-22 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 4 | xbrli:pure | 2023-03-31 | 2023-12-18 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 52947 | GBP | 2023-03-31 | 2023-12-18 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| current_assets | 52947 | GBP | 2023-03-31 | 2024-12-22 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | -8565 | GBP | 2023-03-31 | 2023-12-18 | filed | yes | `ns5:Equity` | micro-entity |
| equity | -8565 | GBP | 2023-03-31 | 2024-12-22 | filed | yes | `ns5:Equity` | micro-entity |
| fixed_assets `{'OriginalRevisedDataDimension': 'Original'}` | 2546 | GBP | 2023-03-31 | 2023-12-18 | filed | yes | `ns5:FixedAssets` | micro-entity |
| fixed_assets | 2546 | GBP | 2023-03-31 | 2024-12-22 | filed | yes | `ns5:FixedAssets` | micro-entity |
| net_assets `{'OriginalRevisedDataDimension': 'Original'}` | -8565 | GBP | 2023-03-31 | 2023-12-18 | filed | yes | `ns5:NetAssetsLiabilities` | micro-entity |
| net_assets | -8565 | GBP | 2023-03-31 | 2024-12-22 | filed | yes | `ns5:NetAssetsLiabilities` | micro-entity |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 8596 | GBP | 2023-03-31 | 2023-12-18 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 8596 | GBP | 2023-03-31 | 2024-12-22 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 11142 | GBP | 2023-03-31 | 2023-12-18 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 11142 | GBP | 2023-03-31 | 2024-12-22 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 5 | xbrli:pure | 2022-03-31 | 2023-12-18 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 48160 | GBP | 2022-03-31 | 2023-12-18 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | -13689 | GBP | 2022-03-31 | 2023-12-18 | filed | yes | `ns5:Equity` | micro-entity |
| fixed_assets `{'OriginalRevisedDataDimension': 'Original'}` | 4409 | GBP | 2022-03-31 | 2023-12-18 | filed | yes | `ns5:FixedAssets` | micro-entity |
| net_assets `{'OriginalRevisedDataDimension': 'Original'}` | -13689 | GBP | 2022-03-31 | 2023-12-18 | filed | yes | `ns5:NetAssetsLiabilities` | micro-entity |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 10028 | GBP | 2022-03-31 | 2023-12-18 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 14437 | GBP | 2022-03-31 | 2023-12-18 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## SHARP AND HILL I.T. SERVICES LIMITED (`gb:04507365`)

- registration: `04507365` (GB), status active, incorporated 2002-08-09
- classification: ['62020'] (sic_2007)
- records: 5 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 64 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2024-08-31 | 2024-11-20 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 241 | GBP | 2024-08-31 | 2024-11-20 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 23112 | GBP | 2024-08-31 | 2024-11-20 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 22871 | GBP | 2024-08-31 | 2024-11-20 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 12759 | GBP | 2024-08-31 | 2024-11-20 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2024-08-31 | 2024-11-20 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -16908 | GBP | 2024-08-31 | 2024-11-20 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 6600 | GBP | 2024-08-31 | 2024-11-20 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | -16907 | GBP | 2024-08-31 | 2024-11-20 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -23507 | GBP | 2024-08-31 | 2024-11-20 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -16907 | GBP | 2024-08-31 | 2024-11-20 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-08-31 | 2024-11-20 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-08-31 | 2024-11-15 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 133 | GBP | 2023-08-31 | 2024-11-15 | filed | no | `frs-core:CashBankOnHand` | total-exemption-full |
| cash | 133 | GBP | 2023-08-31 | 2024-11-20 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 23344 | GBP | 2023-08-31 | 2024-11-15 | filed | no | `frs-core:CurrentAssets` | total-exemption-full |
| current_assets | 23344 | GBP | 2023-08-31 | 2024-11-20 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 23211 | GBP | 2023-08-31 | 2024-11-20 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| debtors | 23211 | GBP | 2023-08-31 | 2024-11-20 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| debtors | 23211 | GBP | 2023-08-31 | 2024-11-15 | filed | no | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -43507 | GBP | 2023-08-31 | 2024-11-20 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -43507 | GBP | 2023-08-31 | 2024-11-15 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2023-08-31 | 2024-11-15 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2023-08-31 | 2024-11-20 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 6938 | GBP | 2023-08-31 | 2024-11-15 | filed | no | `frs-core:FixedAssets` | total-exemption-full |
| fixed_assets | 6937 | GBP | 2023-08-31 | 2024-11-20 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | -43506 | GBP | 2023-08-31 | 2024-11-20 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | -43506 | GBP | 2023-08-31 | 2024-11-15 | filed | no | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -20530 | GBP | 2023-08-31 | 2024-11-20 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -20531 | GBP | 2023-08-31 | 2024-11-15 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -13593 | GBP | 2023-08-31 | 2024-11-20 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -13593 | GBP | 2023-08-31 | 2024-11-15 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2022-08-31 | 2024-11-06 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2022-08-31 | 2024-11-15 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 18475 | GBP | 2022-08-31 | 2024-11-15 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| cash | 18475 | GBP | 2022-08-31 | 2024-11-06 | filed | no | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 40997 | GBP | 2022-08-31 | 2024-11-06 | filed | no | `frs-core:CurrentAssets` | total-exemption-full |
| current_assets | 40997 | GBP | 2022-08-31 | 2024-11-15 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 22522 | GBP | 2022-08-31 | 2024-11-15 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| debtors | 22522 | GBP | 2022-08-31 | 2024-11-06 | filed | no | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -24336 | GBP | 2022-08-31 | 2024-11-15 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2022-08-31 | 2024-11-06 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2022-08-31 | 2024-11-15 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -24336 | GBP | 2022-08-31 | 2024-11-06 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'OtherReservesSubtotal'}` | 0 | GBP | 2022-08-31 | 2024-11-06 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 8681 | GBP | 2022-08-31 | 2024-11-06 | filed | no | `frs-core:FixedAssets` | total-exemption-full |
| fixed_assets | 8681 | GBP | 2022-08-31 | 2024-11-15 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | -24335 | GBP | 2022-08-31 | 2024-11-06 | filed | no | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | -24335 | GBP | 2022-08-31 | 2024-11-15 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -3103 | GBP | 2022-08-31 | 2024-11-06 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -3103 | GBP | 2022-08-31 | 2024-11-15 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 5578 | GBP | 2022-08-31 | 2024-11-15 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 5578 | GBP | 2022-08-31 | 2024-11-06 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2021-08-31 | 2024-11-06 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 66527 | GBP | 2021-08-31 | 2024-11-06 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 67668 | GBP | 2021-08-31 | 2024-11-06 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 1141 | GBP | 2021-08-31 | 2024-11-06 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'OtherReservesSubtotal'}` | 8115 | GBP | 2021-08-31 | 2024-11-06 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 876 | GBP | 2021-08-31 | 2024-11-06 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2021-08-31 | 2024-11-06 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 15745 | GBP | 2021-08-31 | 2024-11-06 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 8992 | GBP | 2021-08-31 | 2024-11-06 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 26163 | GBP | 2021-08-31 | 2024-11-06 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 41908 | GBP | 2021-08-31 | 2024-11-06 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2024-11-20: `{"superseded_document_id": "gb:04507365:doc:h9IVTyrHTgSSSv_X_egUM022yCP2dkojM3GPuejJeG0", "restatements": [{"concept": "fixed_assets", "period_end": "2023-08-31", "old_value": "6938.0000", "new_value"`

## URBAN BEACH LIMITED (`gb:05077962`)

- registration: `05077962` (GB), status active, incorporated 2004-03-18
- classification: ['62020'] (sic_2007)
- records: 3 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 52 filings, 2 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | xbrli:pure | 2025-03-31 | 2025-12-22 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 5467 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 22201 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 4356 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -24752 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:Equity` | micro-entity |
| net_assets | -24752 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -17845 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -17845 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-03-31 | 2025-01-17 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-03-31 | 2025-12-22 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 9567 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 9567 | GBP | 2024-03-31 | 2025-01-17 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 13346 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 14786 | GBP | 2024-03-31 | 2025-01-17 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 2945 | GBP | 2024-03-31 | 2025-01-17 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 2944 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -21409 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:Equity` | micro-entity |
| equity | 21408 | GBP | 2024-03-31 | 2025-01-17 | filed | no | `uk-core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2024-03-31 | 2025-01-17 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | -21409 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 21408 | GBP | 2024-03-31 | 2025-01-17 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -10402 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 11841 | GBP | 2024-03-31 | 2025-01-17 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 11841 | GBP | 2024-03-31 | 2025-01-17 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -10402 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2023-03-31 | 2023-12-22 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-03-31 | 2025-01-17 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 17328 | GBP | 2023-03-31 | 2025-01-17 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 21957 | GBP | 2023-03-31 | 2023-12-22 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 4628 | GBP | 2023-03-31 | 2025-01-17 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 4537 | GBP | 2023-03-31 | 2025-01-17 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 4537 | GBP | 2023-03-31 | 2023-12-22 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | 17006 | GBP | 2023-03-31 | 2023-12-22 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 17005 | GBP | 2023-03-31 | 2025-01-17 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 414 | GBP | 2023-03-31 | 2023-12-22 | filed | no | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 414 | GBP | 2023-03-31 | 2025-01-17 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 17006 | GBP | 2023-03-31 | 2023-12-22 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 17005 | GBP | 2023-03-31 | 2025-01-17 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 91 | GBP | 2023-03-31 | 2025-01-17 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 17420 | GBP | 2023-03-31 | 2023-12-22 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 17006 | GBP | 2023-03-31 | 2023-12-22 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 323 | GBP | 2023-03-31 | 2025-01-17 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2022-03-31 | 2023-12-22 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 37276 | GBP | 2022-03-31 | 2023-12-22 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 78028 | GBP | 2022-03-31 | 2023-12-22 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 43255 | GBP | 2022-03-31 | 2023-12-22 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 2503 | GBP | 2022-03-31 | 2023-12-22 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 43255 | GBP | 2022-03-31 | 2023-12-22 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 40752 | GBP | 2022-03-31 | 2023-12-22 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 43255 | GBP | 2022-03-31 | 2023-12-22 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2025-01-17: `{"superseded_document_id": "gb:05077962:doc:gReSa4USsINzwRTpKN08scA9zHLk8rj3Hrhd4V9eTEI", "restatements": [{"concept": "creditors_within_one_year", "period_end": "2023-03-31", "old_value": "21957.0000`
- event restatement @ 2025-12-22: `{"superseded_document_id": "gb:05077962:doc:VD7yLmAYDyn1SG5yYDbDDlbgyslKQ6NyTjb0lYHx1wk", "restatements": [{"concept": "current_assets", "period_end": "2024-03-31", "old_value": "2945.0000", "new_valu`

## GRIMBLE CONSULTING LIMITED (`gb:05611847`)

- registration: `05611847` (GB), status active, incorporated 2005-11-03
- classification: ['62020'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 54 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-11-30 | 2026-08-27 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 4662 | GBP | 2025-11-30 | 2026-08-27 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 7107 | GBP | 2025-11-30 | 2026-08-27 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 2445 | GBP | 2025-11-30 | 2026-08-27 | filed | yes | `core:Equity` | micro-entity |
| net_assets | 2445 | GBP | 2025-11-30 | 2026-08-27 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 2445 | GBP | 2025-11-30 | 2026-08-27 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 2445 | GBP | 2025-11-30 | 2026-08-27 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-11-30 | 2026-08-27 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-11-30 | 2025-08-28 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 6582 | GBP | 2024-11-30 | 2025-08-28 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 6582 | GBP | 2024-11-30 | 2026-08-27 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 11794 | GBP | 2024-11-30 | 2025-08-28 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 11794 | GBP | 2024-11-30 | 2026-08-27 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 5212 | GBP | 2024-11-30 | 2026-08-27 | filed | yes | `core:Equity` | micro-entity |
| equity | 5212 | GBP | 2024-11-30 | 2025-08-28 | filed | no | `core:Equity` | micro-entity |
| net_assets | 5212 | GBP | 2024-11-30 | 2025-08-28 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 5212 | GBP | 2024-11-30 | 2026-08-27 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 5212 | GBP | 2024-11-30 | 2026-08-27 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 5212 | GBP | 2024-11-30 | 2025-08-28 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 5212 | GBP | 2024-11-30 | 2025-08-28 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 5212 | GBP | 2024-11-30 | 2026-08-27 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-11-30 | 2024-08-23 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-11-30 | 2025-08-28 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 28373 | GBP | 2023-11-30 | 2025-08-28 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 38116 | GBP | 2023-11-30 | 2024-08-23 | filed | no | `ns5:CurrentAssets` | micro-entity |
| current_assets | 38116 | GBP | 2023-11-30 | 2025-08-28 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 10496 | GBP | 2023-11-30 | 2025-08-28 | filed | yes | `core:Equity` | micro-entity |
| equity | 10496 | GBP | 2023-11-30 | 2024-08-23 | filed | no | `ns5:Equity` | micro-entity |
| fixed_assets | 753 | GBP | 2023-11-30 | 2024-08-23 | filed | no | `ns5:FixedAssets` | micro-entity |
| fixed_assets | 753 | GBP | 2023-11-30 | 2025-08-28 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 10496 | GBP | 2023-11-30 | 2025-08-28 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 9743 | GBP | 2023-11-30 | 2024-08-23 | filed | no | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 9743 | GBP | 2023-11-30 | 2025-08-28 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 10496 | GBP | 2023-11-30 | 2024-08-23 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 10496 | GBP | 2023-11-30 | 2025-08-28 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2022-11-30 | 2024-08-23 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 38874 | GBP | 2022-11-30 | 2024-08-23 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity | 15312 | GBP | 2022-11-30 | 2024-08-23 | filed | yes | `ns5:Equity` | micro-entity |
| fixed_assets | 1506 | GBP | 2022-11-30 | 2024-08-23 | filed | yes | `ns5:FixedAssets` | micro-entity |
| net_current_assets | 13806 | GBP | 2022-11-30 | 2024-08-23 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 15312 | GBP | 2022-11-30 | 2024-08-23 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## T CARNELL ENGINEERING LTD (`gb:06133369`)

- registration: `06133369` (GB), status active, incorporated 2007-03-01
- classification: ['71129'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 46 filings, 2 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-03-31 | 2025-12-20 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 16737 | GBP | 2025-03-31 | 2025-12-20 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 719 | GBP | 2025-03-31 | 2025-12-20 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 32846 | GBP | 2025-03-31 | 2025-12-20 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 18671 | GBP | 2025-03-31 | 2025-12-20 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 1434 | GBP | 2025-03-31 | 2025-12-20 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1434 | GBP | 2025-03-31 | 2025-12-20 | filed | yes | `core:Debtors` | total-exemption-full |
| net_assets | 9946 | GBP | 2025-03-31 | 2025-12-20 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -14175 | GBP | 2025-03-31 | 2025-12-20 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 15083 | GBP | 2025-03-31 | 2025-12-20 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-03-31 | 2025-12-20 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 0 | xbrli:pure | 2024-03-31 | 2024-12-02 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 16311 | GBP | 2024-03-31 | 2024-12-02 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 16311 | GBP | 2024-03-31 | 2025-12-20 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 5731 | GBP | 2024-03-31 | 2024-12-02 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 5731 | GBP | 2024-03-31 | 2025-12-20 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 41253 | GBP | 2024-03-31 | 2025-12-20 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 41253 | GBP | 2024-03-31 | 2024-12-02 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 20483 | GBP | 2024-03-31 | 2025-12-20 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 20483 | GBP | 2024-03-31 | 2024-12-02 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 3672 | GBP | 2024-03-31 | 2025-12-20 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 3672 | GBP | 2024-03-31 | 2024-12-02 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 3672 | GBP | 2024-03-31 | 2025-12-20 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 3672 | GBP | 2024-03-31 | 2024-12-02 | filed | no | `core:Debtors` | total-exemption-full |
| net_assets | 4535 | GBP | 2024-03-31 | 2025-12-20 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 4535 | GBP | 2024-03-31 | 2024-12-02 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -20770 | GBP | 2024-03-31 | 2024-12-02 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -20770 | GBP | 2024-03-31 | 2025-12-20 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 16138 | GBP | 2024-03-31 | 2025-12-20 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 16138 | GBP | 2024-03-31 | 2024-12-02 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-03-31 | 2023-11-15 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-03-31 | 2024-12-02 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 18824 | GBP | 2023-03-31 | 2023-11-15 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 18824 | GBP | 2023-03-31 | 2024-12-02 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 14202 | GBP | 2023-03-31 | 2024-12-02 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 14202 | GBP | 2023-03-31 | 2023-11-15 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 32888 | GBP | 2023-03-31 | 2023-11-15 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 32889 | GBP | 2023-03-31 | 2024-12-02 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 31727 | GBP | 2023-03-31 | 2024-12-02 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 31726 | GBP | 2023-03-31 | 2023-11-15 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors | 11402 | GBP | 2023-03-31 | 2023-11-15 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 11403 | GBP | 2023-03-31 | 2024-12-02 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 11403 | GBP | 2023-03-31 | 2024-12-02 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-03-31 | 2023-11-15 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 22265 | GBP | 2023-03-31 | 2023-11-15 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 22365 | GBP | 2023-03-31 | 2023-11-15 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 22365 | GBP | 2023-03-31 | 2024-12-02 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 22365 | GBP | 2023-03-31 | 2023-11-15 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -1162 | GBP | 2023-03-31 | 2023-11-15 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -1162 | GBP | 2023-03-31 | 2024-12-02 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 45418 | GBP | 2023-03-31 | 2024-12-02 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 45418 | GBP | 2023-03-31 | 2023-11-15 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2022-03-31 | 2023-11-15 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 12923 | GBP | 2022-03-31 | 2023-11-15 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 45407 | GBP | 2022-03-31 | 2023-11-15 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 45879 | GBP | 2022-03-31 | 2023-11-15 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 31456 | GBP | 2022-03-31 | 2023-11-15 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 25232 | GBP | 2022-03-31 | 2023-11-15 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 25332 | GBP | 2022-03-31 | 2023-11-15 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2022-03-31 | 2023-11-15 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 25332 | GBP | 2022-03-31 | 2023-11-15 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 472 | GBP | 2022-03-31 | 2023-11-15 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 31163 | GBP | 2022-03-31 | 2023-11-15 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2024-12-02: `{"superseded_document_id": "gb:06133369:doc:p_6GEd5oIOJPP5AM4mt9gX4Xnz1C8q3ysr319x232ag", "restatements": [{"concept": "current_assets", "period_end": "2023-03-31", "old_value": "31726.0000", "new_val`
- event restatement @ 2025-12-20: `{"superseded_document_id": "gb:06133369:doc:ZoR1pyB_kqQ08IJsseBEKbP-Xcrsyur0nuZ3jZM5zdI", "restatements": [{"concept": "average_employees", "period_end": "2024-03-31", "old_value": "0.0000", "new_valu`

## A I K A T E K LTD (`gb:06525230`)

- registration: `06525230` (GB), status active, incorporated 2008-03-05
- classification: ['62020'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 59 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | iso4217:GBP | 2025-03-31 | 2025-12-30 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 169 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 0 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 169 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 169 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 169 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 169 | GBP | 2025-03-31 | 2025-12-30 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2024-03-31 | 2024-12-28 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | dormant |
| average_employees | 0 | iso4217:GBP | 2024-03-31 | 2025-12-30 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 169 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 169 | GBP | 2024-03-31 | 2024-12-28 | filed | no | `core:Creditors` | dormant |
| current_assets | 0 | GBP | 2024-03-31 | 2024-12-28 | filed | no | `core:CurrentAssets` | dormant |
| current_assets | 0 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | -169 | GBP | 2024-03-31 | 2024-12-28 | filed | no | `core:Equity` | dormant |
| equity | 169 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2024-03-31 | 2024-12-28 | filed | no | `core:FixedAssets` | dormant |
| fixed_assets | 0 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 169 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | -169 | GBP | 2024-03-31 | 2024-12-28 | filed | no | `core:NetAssetsLiabilities` | dormant |
| net_current_assets | -169 | GBP | 2024-03-31 | 2024-12-28 | filed | no | `core:NetCurrentAssetsLiabilities` | dormant |
| net_current_assets | 169 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 169 | GBP | 2024-03-31 | 2025-12-30 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -169 | GBP | 2024-03-31 | 2024-12-28 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | dormant |
| average_employees | 0 | iso4217:GBP | 2023-03-31 | 2023-12-31 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | dormant |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 169 | GBP | 2023-03-31 | 2024-12-28 | filed | yes | `core:Creditors` | dormant |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 169 | GBP | 2023-03-31 | 2023-12-31 | filed | no | `core:Creditors` | dormant |
| current_assets | 0 | GBP | 2023-03-31 | 2023-12-31 | filed | no | `core:CurrentAssets` | dormant |
| current_assets | 0 | GBP | 2023-03-31 | 2024-12-28 | filed | yes | `core:CurrentAssets` | dormant |
| equity | -169 | GBP | 2023-03-31 | 2024-12-28 | filed | yes | `core:Equity` | dormant |
| equity | -169 | GBP | 2023-03-31 | 2023-12-31 | filed | no | `core:Equity` | dormant |
| fixed_assets | 0 | GBP | 2023-03-31 | 2024-12-28 | filed | yes | `core:FixedAssets` | dormant |
| fixed_assets | 0 | GBP | 2023-03-31 | 2023-12-31 | filed | no | `core:FixedAssets` | dormant |
| net_assets | -169 | GBP | 2023-03-31 | 2024-12-28 | filed | yes | `core:NetAssetsLiabilities` | dormant |
| net_assets | -169 | GBP | 2023-03-31 | 2023-12-31 | filed | no | `core:NetAssetsLiabilities` | dormant |
| net_current_assets | -169 | GBP | 2023-03-31 | 2023-12-31 | filed | no | `core:NetCurrentAssetsLiabilities` | dormant |
| net_current_assets | -169 | GBP | 2023-03-31 | 2024-12-28 | filed | yes | `core:NetCurrentAssetsLiabilities` | dormant |
| total_assets_less_current_liabilities | -169 | GBP | 2023-03-31 | 2023-12-31 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | dormant |
| total_assets_less_current_liabilities | -169 | GBP | 2023-03-31 | 2024-12-28 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | dormant |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 169 | GBP | 2022-03-31 | 2023-12-31 | filed | yes | `core:Creditors` | dormant |
| current_assets | 91 | GBP | 2022-03-31 | 2023-12-31 | filed | yes | `core:CurrentAssets` | dormant |
| equity | -78 | GBP | 2022-03-31 | 2023-12-31 | filed | yes | `core:Equity` | dormant |
| fixed_assets | 0 | GBP | 2022-03-31 | 2023-12-31 | filed | yes | `core:FixedAssets` | dormant |
| net_assets | -78 | GBP | 2022-03-31 | 2023-12-31 | filed | yes | `core:NetAssetsLiabilities` | dormant |
| net_current_assets | -78 | GBP | 2022-03-31 | 2023-12-31 | filed | yes | `core:NetCurrentAssetsLiabilities` | dormant |
| total_assets_less_current_liabilities | -78 | GBP | 2022-03-31 | 2023-12-31 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | dormant |

_No coverage facts for the latest run._

- event restatement @ 2025-12-30: `{"superseded_document_id": "gb:06525230:doc:W1ijf9gLgmR0XF6lHedEWiHm46vDKVqLpH_FN_iNBew", "restatements": [{"concept": "net_current_assets", "period_end": "2024-03-31", "old_value": "-169.0000", "new_`

## M-POWER SYSTEMS LIMITED (`gb:06890844`)

- registration: `06890844` (GB), status active, incorporated 2009-04-29
- classification: ['62020'] (sic_2007)
- records: 1 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 44 filings, 2 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | xbrli:pure | 2025-04-30 | 2026-01-24 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 53030 | GBP | 2025-04-30 | 2026-01-24 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 42960 | GBP | 2025-04-30 | 2026-01-24 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -8312 | GBP | 2025-04-30 | 2026-01-24 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 1758 | GBP | 2025-04-30 | 2026-01-24 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | -8312 | GBP | 2025-04-30 | 2026-01-24 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -10070 | GBP | 2025-04-30 | 2026-01-24 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -8312 | GBP | 2025-04-30 | 2026-01-24 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2024-04-30 | 2026-01-24 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | xbrli:pure | 2024-04-30 | 2025-01-09 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 9450 | GBP | 2024-04-30 | 2025-01-09 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1521 | GBP | 2024-04-30 | 2025-01-09 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 50074 | GBP | 2024-04-30 | 2026-01-24 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 31511 | GBP | 2024-04-30 | 2025-01-09 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 41212 | GBP | 2024-04-30 | 2026-01-24 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 20833 | GBP | 2024-04-30 | 2025-01-09 | filed | no | `core:Equity` | micro-entity |
| equity | -7104 | GBP | 2024-04-30 | 2026-01-24 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 1758 | GBP | 2024-04-30 | 2026-01-24 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 293 | GBP | 2024-04-30 | 2025-01-09 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | 20833 | GBP | 2024-04-30 | 2025-01-09 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | -7104 | GBP | 2024-04-30 | 2026-01-24 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -8862 | GBP | 2024-04-30 | 2026-01-24 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 29990 | GBP | 2024-04-30 | 2025-01-09 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -7104 | GBP | 2024-04-30 | 2026-01-24 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 30283 | GBP | 2024-04-30 | 2025-01-09 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2023-04-30 | 2025-01-09 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | xbrli:pure | 2023-04-30 | 2024-01-29 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 4896 | GBP | 2023-04-30 | 2025-01-09 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 47899 | GBP | 2023-04-30 | 2024-01-29 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 53437 | GBP | 2023-04-30 | 2025-01-09 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 33518 | GBP | 2023-04-30 | 2025-01-09 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 7355 | GBP | 2023-04-30 | 2024-01-29 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | -40251 | GBP | 2023-04-30 | 2024-01-29 | filed | no | `core:Equity` | micro-entity |
| equity | -24522 | GBP | 2023-04-30 | 2025-01-09 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 293 | GBP | 2023-04-30 | 2025-01-09 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 293 | GBP | 2023-04-30 | 2024-01-29 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | -24522 | GBP | 2023-04-30 | 2025-01-09 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | -40251 | GBP | 2023-04-30 | 2024-01-29 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -40544 | GBP | 2023-04-30 | 2024-01-29 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -19919 | GBP | 2023-04-30 | 2025-01-09 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -40251 | GBP | 2023-04-30 | 2024-01-29 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -19626 | GBP | 2023-04-30 | 2025-01-09 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2022-04-30 | 2024-01-29 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 46166 | GBP | 2022-04-30 | 2024-01-29 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 0 | GBP | 2022-04-30 | 2024-01-29 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -45873 | GBP | 2022-04-30 | 2024-01-29 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 293 | GBP | 2022-04-30 | 2024-01-29 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | -45873 | GBP | 2022-04-30 | 2024-01-29 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -46166 | GBP | 2022-04-30 | 2024-01-29 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -45873 | GBP | 2022-04-30 | 2024-01-29 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2025-01-09: `{"superseded_document_id": "gb:06890844:doc:v-eiq4KS-WnZrNJcGrQvubSOigpShnLZuij14u0ROuA", "restatements": [{"concept": "current_assets", "period_end": "2023-04-30", "old_value": "7355.0000", "new_valu`
- event restatement @ 2026-01-24: `{"superseded_document_id": "gb:06890844:doc:qvJI47GIp8_rgaI9kpAgUcBzR4ckMHZosBhVKENRm0k", "restatements": [{"concept": "fixed_assets", "period_end": "2024-04-30", "old_value": "293.0000", "new_value":`
