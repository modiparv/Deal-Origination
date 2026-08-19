# Ingest spot-check

- database: `data/engine.db`
- latest run: `20260819T025755Z-7e7e512b`
- companies in store: 6600; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## MICROFT TECHNOLOGY LIMITED (`gb:01418657`)

- registration: `01418657` (GB), status active, incorporated 1979-05-09
- classification: ['62020'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 1 security interests, 99 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-08-31 | 2026-05-24 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 255 | GBP | 2025-08-31 | 2026-05-24 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| equity | -13799 | GBP | 2025-08-31 | 2026-05-24 | filed | yes | `frs-core:Equity` | micro-entity |
| net_assets | -13799 | GBP | 2025-08-31 | 2026-05-24 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -13799 | GBP | 2025-08-31 | 2026-05-24 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -13799 | GBP | 2025-08-31 | 2026-05-24 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-08-31 | 2024-12-02 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-08-31 | 2026-05-24 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 12054 | GBP | 2024-08-31 | 2024-12-02 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 263 | GBP | 2024-08-31 | 2026-05-24 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| current_assets | 263 | GBP | 2024-08-31 | 2024-12-02 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | -11792 | GBP | 2024-08-31 | 2026-05-24 | filed | yes | `frs-core:Equity` | micro-entity |
| equity | -11791 | GBP | 2024-08-31 | 2024-12-02 | filed | no | `core:Equity` | micro-entity |
| net_assets | -11791 | GBP | 2024-08-31 | 2024-12-02 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | -11792 | GBP | 2024-08-31 | 2026-05-24 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -11791 | GBP | 2024-08-31 | 2024-12-02 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -11792 | GBP | 2024-08-31 | 2026-05-24 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -11792 | GBP | 2024-08-31 | 2026-05-24 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -11791 | GBP | 2024-08-31 | 2024-12-02 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-08-31 | 2024-12-02 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-08-31 | 2023-12-12 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 10747 | GBP | 2023-08-31 | 2023-12-12 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 10747 | GBP | 2023-08-31 | 2024-12-02 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 331 | GBP | 2023-08-31 | 2023-12-12 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 331 | GBP | 2023-08-31 | 2024-12-02 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -10416 | GBP | 2023-08-31 | 2024-12-02 | filed | yes | `core:Equity` | micro-entity |
| equity | -10416 | GBP | 2023-08-31 | 2023-12-12 | filed | no | `core:Equity` | micro-entity |
| net_assets | -10416 | GBP | 2023-08-31 | 2023-12-12 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | -10416 | GBP | 2023-08-31 | 2024-12-02 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -10416 | GBP | 2023-08-31 | 2024-12-02 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -10416 | GBP | 2023-08-31 | 2023-12-12 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -10416 | GBP | 2023-08-31 | 2023-12-12 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -10416 | GBP | 2023-08-31 | 2024-12-02 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2022-08-31 | 2023-12-12 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 9510 | GBP | 2022-08-31 | 2023-12-12 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 564 | GBP | 2022-08-31 | 2023-12-12 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -8946 | GBP | 2022-08-31 | 2023-12-12 | filed | yes | `core:Equity` | micro-entity |
| net_assets | -8946 | GBP | 2022-08-31 | 2023-12-12 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -8946 | GBP | 2022-08-31 | 2023-12-12 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -8946 | GBP | 2022-08-31 | 2023-12-12 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2026-05-24: `{"superseded_document_id": "gb:01418657:doc:fOFiPGgp5ApfoHAAGLMfF4SwR180Eneq4xcKJyGKbG4", "restatements": [{"concept": "net_current_assets", "period_end": "2024-08-31", "old_value": "-11791.0000", "ne`

## ANTAR INFORMATION TECHNOLOGY LIMITED (`gb:01792081`)

- registration: `01792081` (GB), status active, incorporated 1984-02-15
- classification: ['62020'] (sic_2007)
- records: 13 officers, 1 beneficial owners, 0 ownership statements, 3 security interests, 123 filings, 2 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.06 | xbrli:pure | 2025-08-31 | 2026-05-28 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 63829 | GBP | 2025-08-31 | 2026-05-28 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 90843 | GBP | 2025-08-31 | 2026-05-28 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 28880 | GBP | 2025-08-31 | 2026-05-28 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 1866 | GBP | 2025-08-31 | 2026-05-28 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 28880 | GBP | 2025-08-31 | 2026-05-28 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 27014 | GBP | 2025-08-31 | 2026-05-28 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 28880 | GBP | 2025-08-31 | 2026-05-28 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0.06 | xbrli:pure | 2024-08-31 | 2026-05-28 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 6 | iso4217:GBP | 2024-08-31 | 2025-05-13 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 8386 | GBP | 2024-08-31 | 2025-05-13 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 46457 | GBP | 2024-08-31 | 2026-05-28 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 44847 | GBP | 2024-08-31 | 2025-05-13 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 73474 | GBP | 2024-08-31 | 2026-05-28 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 73474 | GBP | 2024-08-31 | 2025-05-13 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | 24857 | GBP | 2024-08-31 | 2026-05-28 | filed | yes | `core:Equity` | micro-entity |
| equity | 24857 | GBP | 2024-08-31 | 2025-05-13 | filed | no | `uk-core:Equity` | micro-entity |
| fixed_assets | 5675 | GBP | 2024-08-31 | 2026-05-28 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 5675 | GBP | 2024-08-31 | 2025-05-13 | filed | no | `uk-core:FixedAssets` | micro-entity |
| net_assets | 24857 | GBP | 2024-08-31 | 2025-05-13 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 24857 | GBP | 2024-08-31 | 2026-05-28 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 27568 | GBP | 2024-08-31 | 2026-05-28 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 29178 | GBP | 2024-08-31 | 2025-05-13 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 34853 | GBP | 2024-08-31 | 2025-05-13 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 33243 | GBP | 2024-08-31 | 2026-05-28 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 6 | iso4217:GBP | 2023-08-31 | 2024-05-28 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 5 | iso4217:GBP | 2023-08-31 | 2025-05-13 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 18456 | GBP | 2023-08-31 | 2025-05-13 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 18456 | GBP | 2023-08-31 | 2024-05-28 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 51732 | GBP | 2023-08-31 | 2025-05-13 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 51732 | GBP | 2023-08-31 | 2024-05-28 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 107579 | GBP | 2023-08-31 | 2024-05-28 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 107579 | GBP | 2023-08-31 | 2025-05-13 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 42459 | GBP | 2023-08-31 | 2024-05-28 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 42459 | GBP | 2023-08-31 | 2025-05-13 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 4871 | GBP | 2023-08-31 | 2025-05-13 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 4871 | GBP | 2023-08-31 | 2024-05-28 | filed | no | `uk-core:FixedAssets` | micro-entity |
| net_assets | 42459 | GBP | 2023-08-31 | 2024-05-28 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 42459 | GBP | 2023-08-31 | 2025-05-13 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 57374 | GBP | 2023-08-31 | 2025-05-13 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 57374 | GBP | 2023-08-31 | 2024-05-28 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 62245 | GBP | 2023-08-31 | 2024-05-28 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 62245 | GBP | 2023-08-31 | 2025-05-13 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 6 | iso4217:GBP | 2022-08-31 | 2024-05-28 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 28266 | GBP | 2022-08-31 | 2024-05-28 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 55526 | GBP | 2022-08-31 | 2024-05-28 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 119307 | GBP | 2022-08-31 | 2024-05-28 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 44238 | GBP | 2022-08-31 | 2024-05-28 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 6498 | GBP | 2022-08-31 | 2024-05-28 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 44238 | GBP | 2022-08-31 | 2024-05-28 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 67436 | GBP | 2022-08-31 | 2024-05-28 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 73934 | GBP | 2022-08-31 | 2024-05-28 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2025-05-13: `{"superseded_document_id": "gb:01792081:doc:_iagWrhDz9-evldij3jPJQIhX96LTC1UMb2_cgwD1do", "restatements": [{"concept": "average_employees", "period_end": "2023-08-31", "old_value": "6.0000", "new_valu`
- event restatement @ 2026-05-28: `{"superseded_document_id": "gb:01792081:doc:1SJ237tBnP3JCXj6cX6DWxaHz1pRmWgH41fFZItBZyE", "restatements": [{"concept": "net_current_assets", "period_end": "2024-08-31", "old_value": "29178.0000", "new`

## GEOPLAN SPATIAL INTELLIGENCE LIMITED (`gb:02039116`)

- registration: `02039116` (GB), status active, incorporated 1986-07-21
- classification: ['62012'] (sic_2007)
- records: 5 officers, 1 beneficial owners, 0 ownership statements, 7 security interests, 137 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.1 | xbrli:pure | 2026-01-31 | 2026-05-26 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 283022 | GBP | 2026-01-31 | 2026-05-26 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1021241 | GBP | 2026-01-31 | 2026-05-26 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 1252457 | GBP | 2026-01-31 | 2026-05-26 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 969435 | GBP | 2026-01-31 | 2026-05-26 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 969435 | GBP | 2026-01-31 | 2026-05-26 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 150000 | GBP | 2026-01-31 | 2026-05-26 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3452239 | GBP | 2026-01-31 | 2026-05-26 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 4488944 | GBP | 2026-01-31 | 2026-05-26 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 826705 | GBP | 2026-01-31 | 2026-05-26 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 60000 | GBP | 2026-01-31 | 2026-05-26 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 4619949 | GBP | 2026-01-31 | 2026-05-26 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | 4488944 | GBP | 2026-01-31 | 2026-05-26 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 231216 | GBP | 2026-01-31 | 2026-05-26 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 4851165 | GBP | 2026-01-31 | 2026-05-26 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 10 | xbrli:pure | 2025-01-31 | 2025-06-10 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 0.1 | xbrli:pure | 2025-01-31 | 2026-05-26 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 226432 | GBP | 2025-01-31 | 2025-06-10 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 226432 | GBP | 2025-01-31 | 2026-05-26 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 769019 | GBP | 2025-01-31 | 2026-05-26 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 769019 | GBP | 2025-01-31 | 2025-06-10 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 908694 | GBP | 2025-01-31 | 2025-06-10 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 908694 | GBP | 2025-01-31 | 2026-05-26 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 682262 | GBP | 2025-01-31 | 2025-06-10 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 682262 | GBP | 2025-01-31 | 2026-05-26 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 682262 | GBP | 2025-01-31 | 2025-06-10 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 682262 | GBP | 2025-01-31 | 2026-05-26 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3293877 | GBP | 2025-01-31 | 2026-05-26 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 60000 | GBP | 2025-01-31 | 2026-05-26 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 150000 | GBP | 2025-01-31 | 2026-05-26 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 826705 | GBP | 2025-01-31 | 2025-06-10 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 826705 | GBP | 2025-01-31 | 2026-05-26 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 4330582 | GBP | 2025-01-31 | 2025-06-10 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 60000 | GBP | 2025-01-31 | 2025-06-10 | filed | no | `core:Equity` | total-exemption-full |
| equity | 4330582 | GBP | 2025-01-31 | 2026-05-26 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 150000 | GBP | 2025-01-31 | 2025-06-10 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3293877 | GBP | 2025-01-31 | 2025-06-10 | filed | no | `core:Equity` | total-exemption-full |
| fixed_assets | 4535928 | GBP | 2025-01-31 | 2026-05-26 | filed | yes | `core:FixedAssets` | total-exemption-full |
| fixed_assets | 4535928 | GBP | 2025-01-31 | 2025-06-10 | filed | no | `core:FixedAssets` | total-exemption-full |
| net_assets | 4330582 | GBP | 2025-01-31 | 2026-05-26 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 4330582 | GBP | 2025-01-31 | 2025-06-10 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 139675 | GBP | 2025-01-31 | 2026-05-26 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 139675 | GBP | 2025-01-31 | 2025-06-10 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 4675603 | GBP | 2025-01-31 | 2025-06-10 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 4675603 | GBP | 2025-01-31 | 2026-05-26 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 10 | xbrli:pure | 2024-01-31 | 2025-06-10 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 10 | xbrli:pure | 2024-01-31 | 2024-07-22 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 236979 | GBP | 2024-01-31 | 2025-06-10 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 236979 | GBP | 2024-01-31 | 2024-07-22 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2024-01-31 | 2024-07-22 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1405277 | GBP | 2024-01-31 | 2025-06-10 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1405277 | GBP | 2024-01-31 | 2024-07-22 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 1173778 | GBP | 2024-01-31 | 2024-07-22 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 1173778 | GBP | 2024-01-31 | 2025-06-10 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 936799 | GBP | 2024-01-31 | 2025-06-10 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 936799 | GBP | 2024-01-31 | 2025-06-10 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 936799 | GBP | 2024-01-31 | 2024-07-22 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 936799 | GBP | 2024-01-31 | 2024-07-22 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3033130 | GBP | 2024-01-31 | 2025-06-10 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 4069835 | GBP | 2024-01-31 | 2025-06-10 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 826705 | GBP | 2024-01-31 | 2024-07-22 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 150000 | GBP | 2024-01-31 | 2025-06-10 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 60000 | GBP | 2024-01-31 | 2024-07-22 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 60000 | GBP | 2024-01-31 | 2025-06-10 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 4069835 | GBP | 2024-01-31 | 2024-07-22 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3033130 | GBP | 2024-01-31 | 2024-07-22 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 150000 | GBP | 2024-01-31 | 2024-07-22 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 826705 | GBP | 2024-01-31 | 2025-06-10 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 4676850 | GBP | 2024-01-31 | 2024-07-22 | filed | no | `core:FixedAssets` | total-exemption-full |
| fixed_assets | 4676850 | GBP | 2024-01-31 | 2025-06-10 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | 4069835 | GBP | 2024-01-31 | 2024-07-22 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 4069835 | GBP | 2024-01-31 | 2025-06-10 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -231499 | GBP | 2024-01-31 | 2024-07-22 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -231499 | GBP | 2024-01-31 | 2025-06-10 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_for_period | 68250 | GBP | 2024-01-31 | 2024-07-22 | filed | yes | `core:ProfitLoss` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 68250 | GBP | 2024-01-31 | 2024-07-22 | filed | yes | `core:ProfitLoss` | total-exemption-full |
| total_assets_less_current_liabilities | 4445351 | GBP | 2024-01-31 | 2024-07-22 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 4445351 | GBP | 2024-01-31 | 2025-06-10 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 12 | xbrli:pure | 2023-01-31 | 2024-07-22 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 649118 | GBP | 2023-01-31 | 2024-07-22 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 1451476 | GBP | 2023-01-31 | 2024-07-22 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 805780 | GBP | 2023-01-31 | 2024-07-22 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 1882843 | GBP | 2023-01-31 | 2024-07-22 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 1233725 | GBP | 2023-01-31 | 2024-07-22 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1233725 | GBP | 2023-01-31 | 2024-07-22 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2964880 | GBP | 2023-01-31 | 2024-07-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 3553770 | GBP | 2023-01-31 | 2024-07-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 378890 | GBP | 2023-01-31 | 2024-07-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 60000 | GBP | 2023-01-31 | 2024-07-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 150000 | GBP | 2023-01-31 | 2024-07-22 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 3959147 | GBP | 2023-01-31 | 2024-07-22 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | 3553770 | GBP | 2023-01-31 | 2024-07-22 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1077063 | GBP | 2023-01-31 | 2024-07-22 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_for_period | 220285 | GBP | 2023-01-31 | 2024-07-22 | filed | yes | `core:ProfitLoss` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 220285 | GBP | 2023-01-31 | 2024-07-22 | filed | yes | `core:ProfitLoss` | total-exemption-full |
| total_assets_less_current_liabilities | 5036210 | GBP | 2023-01-31 | 2024-07-22 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 60000 | GBP | 2022-01-31 | 2024-07-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2744595 | GBP | 2022-01-31 | 2024-07-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 150000 | GBP | 2022-01-31 | 2024-07-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 378890 | GBP | 2022-01-31 | 2024-07-22 | filed | yes | `core:Equity` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2026-05-26: `{"superseded_document_id": "gb:02039116:doc:HVXd1CTNlF4A69RQXFmKm8epjoag3zm22vJ7HynMJ6U", "restatements": [{"concept": "average_employees", "period_end": "2025-01-31", "old_value": "10.0000", "new_val`

## TRANSMATIC FYLLAN LIMITED (`gb:02243105`)

- registration: `02243105` (GB), status active, incorporated 1988-04-11
- classification: ['43999', '62090', '71122'] (sic_2007)
- records: 3 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 94 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | xbrli:pure | 2025-04-30 | 2026-01-05 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 65940 | GBP | 2025-04-30 | 2026-01-05 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 65950 | GBP | 2025-04-30 | 2026-01-05 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 10 | GBP | 2025-04-30 | 2026-01-05 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 65950 | GBP | 2025-04-30 | 2026-01-05 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 65940 | GBP | 2025-04-30 | 2026-01-05 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 65950 | GBP | 2025-04-30 | 2026-01-05 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2024-04-30 | 2026-01-05 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | xbrli:pure | 2024-04-30 | 2025-01-06 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 65940 | GBP | 2024-04-30 | 2025-01-06 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 65940 | GBP | 2024-04-30 | 2026-01-05 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 65950 | GBP | 2024-04-30 | 2026-01-05 | filed | yes | `core:Equity` | micro-entity |
| equity | 65950 | GBP | 2024-04-30 | 2025-01-06 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 10 | GBP | 2024-04-30 | 2026-01-05 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 10 | GBP | 2024-04-30 | 2025-01-06 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | 65950 | GBP | 2024-04-30 | 2026-01-05 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 65950 | GBP | 2024-04-30 | 2025-01-06 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 65940 | GBP | 2024-04-30 | 2025-01-06 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 65940 | GBP | 2024-04-30 | 2026-01-05 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 65950 | GBP | 2024-04-30 | 2026-01-05 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 65950 | GBP | 2024-04-30 | 2025-01-06 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2023-04-30 | 2025-01-06 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | xbrli:pure | 2023-04-30 | 2024-01-19 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 65940 | GBP | 2023-04-30 | 2025-01-06 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 65940 | GBP | 2023-04-30 | 2024-01-19 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 65950 | GBP | 2023-04-30 | 2024-01-19 | filed | no | `core:Equity` | micro-entity |
| equity | 65950 | GBP | 2023-04-30 | 2025-01-06 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 10 | GBP | 2023-04-30 | 2024-01-19 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 10 | GBP | 2023-04-30 | 2025-01-06 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 65950 | GBP | 2023-04-30 | 2025-01-06 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 65950 | GBP | 2023-04-30 | 2024-01-19 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 65940 | GBP | 2023-04-30 | 2024-01-19 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 65940 | GBP | 2023-04-30 | 2025-01-06 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 65950 | GBP | 2023-04-30 | 2024-01-19 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 65950 | GBP | 2023-04-30 | 2025-01-06 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2022-04-30 | 2024-01-19 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 67336 | GBP | 2022-04-30 | 2024-01-19 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 67346 | GBP | 2022-04-30 | 2024-01-19 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 10 | GBP | 2022-04-30 | 2024-01-19 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 67346 | GBP | 2022-04-30 | 2024-01-19 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 67336 | GBP | 2022-04-30 | 2024-01-19 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 67346 | GBP | 2022-04-30 | 2024-01-19 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## INSKIP GEE ARCHITECTS LIMITED (`gb:02415604`)

- registration: `02415604` (GB), status active, incorporated 1989-08-22
- classification: ['71111'] (sic_2007)
- records: 6 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 103 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 13 | xbrli:pure | 2025-11-30 | 2026-07-24 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 361285 | GBP | 2025-11-30 | 2026-07-24 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 222914 | GBP | 2025-11-30 | 2026-07-24 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 812699 | GBP | 2025-11-30 | 2026-07-24 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 196392 | GBP | 2025-11-30 | 2026-07-24 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 564063 | GBP | 2025-11-30 | 2026-07-24 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 574063 | GBP | 2025-11-30 | 2026-07-24 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 5500 | GBP | 2025-11-30 | 2026-07-24 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 4500 | GBP | 2025-11-30 | 2026-07-24 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 574063 | GBP | 2025-11-30 | 2026-07-24 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 589785 | GBP | 2025-11-30 | 2026-07-24 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 593813 | GBP | 2025-11-30 | 2026-07-24 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 13 | xbrli:pure | 2024-11-30 | 2025-08-20 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 13 | xbrli:pure | 2024-11-30 | 2026-07-24 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 286101 | GBP | 2024-11-30 | 2025-08-20 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 286101 | GBP | 2024-11-30 | 2026-07-24 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 270983 | GBP | 2024-11-30 | 2026-07-24 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 270983 | GBP | 2024-11-30 | 2025-08-20 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 677545 | GBP | 2024-11-30 | 2026-07-24 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 677545 | GBP | 2024-11-30 | 2025-08-20 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors | 261498 | GBP | 2024-11-30 | 2026-07-24 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 261498 | GBP | 2024-11-30 | 2025-08-20 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 4500 | GBP | 2024-11-30 | 2025-08-20 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 5500 | GBP | 2024-11-30 | 2025-08-20 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 401941 | GBP | 2024-11-30 | 2026-07-24 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 411941 | GBP | 2024-11-30 | 2026-07-24 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 411941 | GBP | 2024-11-30 | 2025-08-20 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 5500 | GBP | 2024-11-30 | 2026-07-24 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 401941 | GBP | 2024-11-30 | 2025-08-20 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 4500 | GBP | 2024-11-30 | 2026-07-24 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 411941 | GBP | 2024-11-30 | 2025-08-20 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 411941 | GBP | 2024-11-30 | 2026-07-24 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 406562 | GBP | 2024-11-30 | 2026-07-24 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 406562 | GBP | 2024-11-30 | 2025-08-20 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 411941 | GBP | 2024-11-30 | 2026-07-24 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 13 | xbrli:pure | 2023-11-30 | 2025-08-20 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 13 | xbrli:pure | 2023-11-30 | 2024-08-30 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 59192 | GBP | 2023-11-30 | 2024-08-30 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 59192 | GBP | 2023-11-30 | 2025-08-20 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 159651 | GBP | 2023-11-30 | 2024-08-30 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 159651 | GBP | 2023-11-30 | 2025-08-20 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 363602 | GBP | 2023-11-30 | 2024-08-30 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 363602 | GBP | 2023-11-30 | 2025-08-20 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 94184 | GBP | 2023-11-30 | 2025-08-20 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 94184 | GBP | 2023-11-30 | 2024-08-30 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 5500 | GBP | 2023-11-30 | 2025-08-20 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 4500 | GBP | 2023-11-30 | 2025-08-20 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 199659 | GBP | 2023-11-30 | 2024-08-30 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 5500 | GBP | 2023-11-30 | 2024-08-30 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 199659 | GBP | 2023-11-30 | 2025-08-20 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 209659 | GBP | 2023-11-30 | 2025-08-20 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 4500 | GBP | 2023-11-30 | 2024-08-30 | filed | no | `core:Equity` | total-exemption-full |
| equity | 209659 | GBP | 2023-11-30 | 2024-08-30 | filed | no | `core:Equity` | total-exemption-full |
| net_assets | 209659 | GBP | 2023-11-30 | 2024-08-30 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 209659 | GBP | 2023-11-30 | 2025-08-20 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 203951 | GBP | 2023-11-30 | 2025-08-20 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 203951 | GBP | 2023-11-30 | 2024-08-30 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| average_employees | 10 | xbrli:pure | 2022-11-30 | 2024-08-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 85821 | GBP | 2022-11-30 | 2024-08-30 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 245417 | GBP | 2022-11-30 | 2024-08-30 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 297491 | GBP | 2022-11-30 | 2024-08-30 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 22532 | GBP | 2022-11-30 | 2024-08-30 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 5500 | GBP | 2022-11-30 | 2024-08-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 4500 | GBP | 2022-11-30 | 2024-08-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 49048 | GBP | 2022-11-30 | 2024-08-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 59048 | GBP | 2022-11-30 | 2024-08-30 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 59048 | GBP | 2022-11-30 | 2024-08-30 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 52074 | GBP | 2022-11-30 | 2024-08-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## MAGOG INDUSTRIES LIMITED (`gb:02569243`)

- registration: `02569243` (GB), status active, incorporated 1990-12-17
- classification: ['71129'] (sic_2007)
- records: 11 officers, 2 beneficial owners, 0 ownership statements, 2 security interests, 122 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 12 | xbrli:pure | 2024-12-31 | 2025-09-12 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 2446447 | GBP | 2024-12-31 | 2025-09-12 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 2827135 | GBP | 2024-12-31 | 2025-09-12 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 253098 | GBP | 2024-12-31 | 2025-09-12 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 250000 | GBP | 2024-12-31 | 2025-09-12 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 292901 | GBP | 2024-12-31 | 2025-09-12 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2255626 | GBP | 2024-12-31 | 2025-09-12 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 427961 | GBP | 2024-12-31 | 2025-09-12 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 2798527 | GBP | 2024-12-31 | 2025-09-12 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 2383730 | GBP | 2024-12-31 | 2025-09-12 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 2811691 | GBP | 2024-12-31 | 2025-09-12 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 10 | xbrli:pure | 2023-12-31 | 2024-09-30 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 10 | xbrli:pure | 2023-12-31 | 2025-09-12 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 1993789 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `frs-core:CashBankOnHand` | total-exemption-full |
| cash | 1993789 | GBP | 2023-12-31 | 2025-09-12 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 2535721 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `frs-core:CurrentAssets` | total-exemption-full |
| current_assets | 2535721 | GBP | 2023-12-31 | 2025-09-12 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 407577 | GBP | 2023-12-31 | 2025-09-12 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| debtors | 407577 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 292901 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 250000 | GBP | 2023-12-31 | 2025-09-12 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 292901 | GBP | 2023-12-31 | 2025-09-12 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1830214 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 250000 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1830214 | GBP | 2023-12-31 | 2025-09-12 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 433425 | GBP | 2023-12-31 | 2025-09-12 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| fixed_assets | 433425 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 2373115 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 2373115 | GBP | 2023-12-31 | 2025-09-12 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1952939 | GBP | 2023-12-31 | 2025-09-12 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1952939 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 2386364 | GBP | 2023-12-31 | 2025-09-12 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 2386364 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 10 | xbrli:pure | 2022-12-31 | 2023-09-21 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 10 | xbrli:pure | 2022-12-31 | 2024-09-30 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 1526991 | GBP | 2022-12-31 | 2023-09-21 | filed | no | `frs-core:CashBankOnHand` | total-exemption-full |
| cash | 1526991 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 1926013 | GBP | 2022-12-31 | 2023-09-21 | filed | no | `frs-core:CurrentAssets` | total-exemption-full |
| current_assets | 1926013 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 234121 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| debtors | 234121 | GBP | 2022-12-31 | 2023-09-21 | filed | no | `frs-core:Debtors` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1224957 | GBP | 2022-12-31 | 2023-09-21 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 250000 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'ShareCapital'}` | 250000 | GBP | 2022-12-31 | 2023-09-21 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1224957 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RevaluationReserve'}` | 295901 | GBP | 2022-12-31 | 2023-09-21 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 295901 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 439933 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| fixed_assets | 439933 | GBP | 2022-12-31 | 2023-09-21 | filed | no | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 1770858 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 1770858 | GBP | 2022-12-31 | 2023-09-21 | filed | no | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1341206 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1341206 | GBP | 2022-12-31 | 2023-09-21 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1781139 | GBP | 2022-12-31 | 2023-09-21 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1781139 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 12 | xbrli:pure | 2021-12-31 | 2023-09-21 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 1092140 | GBP | 2021-12-31 | 2023-09-21 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 1467011 | GBP | 2021-12-31 | 2023-09-21 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 273806 | GBP | 2021-12-31 | 2023-09-21 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'ShareCapital'}` | 250000 | GBP | 2021-12-31 | 2023-09-21 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 679440 | GBP | 2021-12-31 | 2023-09-21 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RevaluationReserve'}` | 295901 | GBP | 2021-12-31 | 2023-09-21 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 448947 | GBP | 2021-12-31 | 2023-09-21 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 1225341 | GBP | 2021-12-31 | 2023-09-21 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 787096 | GBP | 2021-12-31 | 2023-09-21 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1236043 | GBP | 2021-12-31 | 2023-09-21 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## R.N.B. CONTROLS LIMITED (`gb:02706263`)

- registration: `02706263` (GB), status active, incorporated 1992-04-13
- classification: ['71129'] (sic_2007)
- records: 5 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 79 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.02 | xbrli:pure | 2025-04-30 | 2025-09-29 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 33286 | GBP | 2025-04-30 | 2025-09-29 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| current_assets | 43777 | GBP | 2025-04-30 | 2025-09-29 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 8811 | GBP | 2025-04-30 | 2025-09-29 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 8811 | GBP | 2025-04-30 | 2025-09-29 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 100 | GBP | 2025-04-30 | 2025-09-29 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 620 | GBP | 2025-04-30 | 2025-09-29 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass2'}` | 100 | GBP | 2025-04-30 | 2025-09-29 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShares'}` | 200 | GBP | 2025-04-30 | 2025-09-29 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 820 | GBP | 2025-04-30 | 2025-09-29 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200 | GBP | 2025-04-30 | 2025-09-29 | filed | yes | `core:Equity` | total-exemption-full |
| net_current_assets | -140887 | GBP | 2025-04-30 | 2025-09-29 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 820 | GBP | 2025-04-30 | 2025-09-29 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0.02 | xbrli:pure | 2024-04-30 | 2025-09-29 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-04-30 | 2025-01-09 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 43949 | GBP | 2024-04-30 | 2025-09-29 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 43949 | GBP | 2024-04-30 | 2025-01-09 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| current_assets | 50623 | GBP | 2024-04-30 | 2025-09-29 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 50625 | GBP | 2024-04-30 | 2025-01-09 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5220 | GBP | 2024-04-30 | 2025-01-09 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5218 | GBP | 2024-04-30 | 2025-09-29 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 5220 | GBP | 2024-04-30 | 2025-01-09 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 5218 | GBP | 2024-04-30 | 2025-09-29 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 790 | GBP | 2024-04-30 | 2025-09-29 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200 | GBP | 2024-04-30 | 2025-09-29 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200 | GBP | 2024-04-30 | 2025-01-09 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass2'}` | 100 | GBP | 2024-04-30 | 2025-09-29 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 790 | GBP | 2024-04-30 | 2025-01-09 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShares'}` | 200 | GBP | 2024-04-30 | 2025-09-29 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShares'}` | 200 | GBP | 2024-04-30 | 2025-01-09 | filed | no | `core:Equity` | total-exemption-full |
| equity | 990 | GBP | 2024-04-30 | 2025-09-29 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 990 | GBP | 2024-04-30 | 2025-01-09 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 100 | GBP | 2024-04-30 | 2025-09-29 | filed | yes | `core:Equity` | total-exemption-full |
| net_current_assets | -121422 | GBP | 2024-04-30 | 2025-09-29 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -121420 | GBP | 2024-04-30 | 2025-01-09 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 990 | GBP | 2024-04-30 | 2025-01-09 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 990 | GBP | 2024-04-30 | 2025-09-29 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-04-30 | 2023-12-19 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-04-30 | 2025-01-09 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 26829 | GBP | 2023-04-30 | 2023-12-19 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 26829 | GBP | 2023-04-30 | 2025-01-09 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| current_assets | 33122 | GBP | 2023-04-30 | 2023-12-19 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 33122 | GBP | 2023-04-30 | 2025-01-09 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5269 | GBP | 2023-04-30 | 2023-12-19 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 5269 | GBP | 2023-04-30 | 2023-12-19 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5269 | GBP | 2023-04-30 | 2025-01-09 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 5269 | GBP | 2023-04-30 | 2025-01-09 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShares'}` | 200 | GBP | 2023-04-30 | 2025-01-09 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 94 | GBP | 2023-04-30 | 2025-01-09 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200 | GBP | 2023-04-30 | 2025-01-09 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 294 | GBP | 2023-04-30 | 2025-01-09 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShares'}` | 200 | GBP | 2023-04-30 | 2023-12-19 | filed | no | `core:Equity` | total-exemption-full |
| equity | 294 | GBP | 2023-04-30 | 2023-12-19 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200 | GBP | 2023-04-30 | 2023-12-19 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 94 | GBP | 2023-04-30 | 2023-12-19 | filed | no | `core:Equity` | total-exemption-full |
| net_current_assets | -119310 | GBP | 2023-04-30 | 2025-01-09 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -119310 | GBP | 2023-04-30 | 2023-12-19 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 294 | GBP | 2023-04-30 | 2025-01-09 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 294 | GBP | 2023-04-30 | 2023-12-19 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2022-04-30 | 2023-12-19 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 22913 | GBP | 2022-04-30 | 2023-12-19 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| current_assets | 28792 | GBP | 2022-04-30 | 2023-12-19 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 4663 | GBP | 2022-04-30 | 2023-12-19 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 4663 | GBP | 2022-04-30 | 2023-12-19 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShares'}` | 200 | GBP | 2022-04-30 | 2023-12-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 307 | GBP | 2022-04-30 | 2023-12-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200 | GBP | 2022-04-30 | 2023-12-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 107 | GBP | 2022-04-30 | 2023-12-19 | filed | yes | `core:Equity` | total-exemption-full |
| net_current_assets | -122983 | GBP | 2022-04-30 | 2023-12-19 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 307 | GBP | 2022-04-30 | 2023-12-19 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2025-09-29: `{"superseded_document_id": "gb:02706263:doc:8yANIpYacy2c4HMY793FGDUfO5uajxOl5hOk133ZToU", "restatements": [{"concept": "debtors", "period_end": "2024-04-30", "old_value": "5220.0000", "new_value": "52`

## MERIDIAN NETWORK CONSULTANTS LIMITED (`gb:03078106`)

- registration: `03078106` (GB), status active, incorporated 1995-07-11
- classification: ['62020'] (sic_2007)
- records: 5 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 71 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-09-30 | 2026-06-24 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 113789 | GBP | 2025-09-30 | 2026-06-24 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| equity | 96496 | GBP | 2025-09-30 | 2026-06-24 | filed | yes | `frs-core:Equity` | micro-entity |
| fixed_assets | 31 | GBP | 2025-09-30 | 2026-06-24 | filed | yes | `frs-core:FixedAssets` | micro-entity |
| net_assets | 96496 | GBP | 2025-09-30 | 2026-06-24 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 96465 | GBP | 2025-09-30 | 2026-06-24 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 96496 | GBP | 2025-09-30 | 2026-06-24 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-09-30 | 2026-06-24 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-09-30 | 2025-06-18 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 55468 | GBP | 2024-09-30 | 2025-06-18 | filed | no | `frs-core:CurrentAssets` | micro-entity |
| current_assets | 55468 | GBP | 2024-09-30 | 2026-06-24 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| equity | 50795 | GBP | 2024-09-30 | 2026-06-24 | filed | yes | `frs-core:Equity` | micro-entity |
| equity | 50795 | GBP | 2024-09-30 | 2025-06-18 | filed | no | `frs-core:Equity` | micro-entity |
| fixed_assets | 31 | GBP | 2024-09-30 | 2025-06-18 | filed | no | `frs-core:FixedAssets` | micro-entity |
| fixed_assets | 31 | GBP | 2024-09-30 | 2026-06-24 | filed | yes | `frs-core:FixedAssets` | micro-entity |
| net_assets | 50795 | GBP | 2024-09-30 | 2025-06-18 | filed | no | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 50795 | GBP | 2024-09-30 | 2026-06-24 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 50764 | GBP | 2024-09-30 | 2025-06-18 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 50764 | GBP | 2024-09-30 | 2026-06-24 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 50795 | GBP | 2024-09-30 | 2026-06-24 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 50795 | GBP | 2024-09-30 | 2025-06-18 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-09-30 | 2025-06-18 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-09-30 | 2024-06-24 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 4670 | GBP | 2023-09-30 | 2024-06-24 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 68151 | GBP | 2023-09-30 | 2025-06-18 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| current_assets | 68151 | GBP | 2023-09-30 | 2024-06-24 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 63512 | GBP | 2023-09-30 | 2024-06-24 | filed | no | `core:Equity` | micro-entity |
| equity | 63512 | GBP | 2023-09-30 | 2025-06-18 | filed | yes | `frs-core:Equity` | micro-entity |
| fixed_assets | 31 | GBP | 2023-09-30 | 2025-06-18 | filed | yes | `frs-core:FixedAssets` | micro-entity |
| fixed_assets | 31 | GBP | 2023-09-30 | 2024-06-24 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | 63512 | GBP | 2023-09-30 | 2024-06-24 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 63512 | GBP | 2023-09-30 | 2025-06-18 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 63481 | GBP | 2023-09-30 | 2024-06-24 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 63481 | GBP | 2023-09-30 | 2025-06-18 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 63512 | GBP | 2023-09-30 | 2025-06-18 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2022-09-30 | 2024-06-24 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 6352 | GBP | 2022-09-30 | 2024-06-24 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 79756 | GBP | 2022-09-30 | 2024-06-24 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 73435 | GBP | 2022-09-30 | 2024-06-24 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 31 | GBP | 2022-09-30 | 2024-06-24 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 73435 | GBP | 2022-09-30 | 2024-06-24 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 73404 | GBP | 2022-09-30 | 2024-06-24 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |

_No coverage facts for the latest run._

## S.A.F. CONSULTING LIMITED (`gb:03403005`)

- registration: `03403005` (GB), status active, incorporated 1997-07-14
- classification: ['62030'] (sic_2007)
- records: 6 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 72 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-05-31 | 2026-01-14 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 5772 | GBP | 2025-05-31 | 2026-01-14 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 7710 | GBP | 2025-05-31 | 2026-01-14 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 7040 | GBP | 2025-05-31 | 2026-01-14 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 1268 | GBP | 2025-05-31 | 2026-01-14 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 20 | GBP | 2025-05-31 | 2026-01-14 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 22 | GBP | 2025-05-31 | 2026-01-14 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2025-05-31 | 2026-01-14 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 22 | GBP | 2025-05-31 | 2026-01-14 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -670 | GBP | 2025-05-31 | 2026-01-14 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-05-31 | 2025-01-13 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-05-31 | 2026-01-14 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 1975 | GBP | 2024-05-31 | 2025-01-13 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 1975 | GBP | 2024-05-31 | 2026-01-14 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 6884 | GBP | 2024-05-31 | 2026-01-14 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 6884 | GBP | 2024-05-31 | 2025-01-13 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 6760 | GBP | 2024-05-31 | 2026-01-14 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 6760 | GBP | 2024-05-31 | 2025-01-13 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors | 4785 | GBP | 2024-05-31 | 2025-01-13 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 4785 | GBP | 2024-05-31 | 2026-01-14 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-05-31 | 2026-01-14 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-05-31 | 2025-01-13 | filed | no | `core:Equity` | total-exemption-full |
| equity | 741 | GBP | 2024-05-31 | 2025-01-13 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 739 | GBP | 2024-05-31 | 2026-01-14 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 739 | GBP | 2024-05-31 | 2025-01-13 | filed | no | `core:Equity` | total-exemption-full |
| equity | 741 | GBP | 2024-05-31 | 2026-01-14 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 741 | GBP | 2024-05-31 | 2026-01-14 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 741 | GBP | 2024-05-31 | 2025-01-13 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -124 | GBP | 2024-05-31 | 2025-01-13 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -124 | GBP | 2024-05-31 | 2026-01-14 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-05-31 | 2024-02-28 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-05-31 | 2025-01-13 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 8788 | GBP | 2023-05-31 | 2024-02-28 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 8788 | GBP | 2023-05-31 | 2025-01-13 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 13975 | GBP | 2023-05-31 | 2024-02-28 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 13975 | GBP | 2023-05-31 | 2025-01-13 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 17471 | GBP | 2023-05-31 | 2025-01-13 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 17471 | GBP | 2023-05-31 | 2024-02-28 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors | 8683 | GBP | 2023-05-31 | 2025-01-13 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 8683 | GBP | 2023-05-31 | 2024-02-28 | filed | no | `core:Debtors` | total-exemption-full |
| equity | 4577 | GBP | 2023-05-31 | 2025-01-13 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 4575 | GBP | 2023-05-31 | 2024-02-28 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 4575 | GBP | 2023-05-31 | 2025-01-13 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-05-31 | 2024-02-28 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-05-31 | 2025-01-13 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 4577 | GBP | 2023-05-31 | 2024-02-28 | filed | no | `core:Equity` | total-exemption-full |
| net_assets | 4577 | GBP | 2023-05-31 | 2025-01-13 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 4577 | GBP | 2023-05-31 | 2024-02-28 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 3496 | GBP | 2023-05-31 | 2024-02-28 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 3496 | GBP | 2023-05-31 | 2025-01-13 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2022-05-31 | 2024-02-28 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 14479 | GBP | 2022-05-31 | 2024-02-28 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 23208 | GBP | 2022-05-31 | 2024-02-28 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 23162 | GBP | 2022-05-31 | 2024-02-28 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 8683 | GBP | 2022-05-31 | 2024-02-28 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 1305 | GBP | 2022-05-31 | 2024-02-28 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2022-05-31 | 2024-02-28 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1303 | GBP | 2022-05-31 | 2024-02-28 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 1305 | GBP | 2022-05-31 | 2024-02-28 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -46 | GBP | 2022-05-31 | 2024-02-28 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |

Coverage @ 2025-05-31: 8/21 concepts available (average_employees, cash, creditors_within_one_year, current_assets, debtors, equity, net_assets, net_current_assets)
- `creditors_after_one_year`: filed_without_concept — absent though regime 'total-exemption-full' typically includes it
- `depreciation_amortisation`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `fixed_assets`: filed_without_concept — absent though regime 'total-exemption-full' typically includes it
- `gross_profit`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `operating_profit`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `profit_before_tax`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `profit_for_period`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `retained_earnings`: filed_without_concept — absent though regime 'total-exemption-full' typically includes it
- `revenue`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `share_capital`: filed_without_concept — absent though regime 'total-exemption-full' typically includes it
- `staff_costs`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `tax_charge`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `total_assets_less_current_liabilities`: filed_without_concept — absent though regime 'total-exemption-full' typically includes it
