# Ingest spot-check

- database: `data/engine.db`
- latest run: `20261014T071241Z-fd1cdb4b`
- companies in store: 26600; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## STAMPNOTES LIMITED (`gb:02246312`)

- registration: `02246312` (GB), status active, incorporated 1988-04-20
- classification: ['62020'] (sic_2007)
- records: 3 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 101 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-09-30 | 2026-06-29 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 473 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 4321 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 126434 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 123000 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 126434 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 3848 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 126848 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-09-30 | 2026-06-29 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-09-30 | 2025-06-27 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 507 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 507 | GBP | 2024-09-30 | 2025-06-27 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 11264 | GBP | 2024-09-30 | 2025-06-27 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 11264 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 130361 | GBP | 2024-09-30 | 2025-06-27 | filed | no | `core:Equity` | micro-entity |
| equity | 130361 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 120000 | GBP | 2024-09-30 | 2025-06-27 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 120000 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 130361 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 130361 | GBP | 2024-09-30 | 2025-06-27 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 10757 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 10757 | GBP | 2024-09-30 | 2025-06-27 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 130757 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 130757 | GBP | 2024-09-30 | 2025-06-27 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-09-30 | 2025-06-27 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-09-30 | 2024-04-05 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 160 | GBP | 2023-09-30 | 2025-06-27 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 160 | GBP | 2023-09-30 | 2024-04-05 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 10375 | GBP | 2023-09-30 | 2024-04-05 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 10375 | GBP | 2023-09-30 | 2025-06-27 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 134693 | GBP | 2023-09-30 | 2024-04-05 | filed | no | `core:Equity` | micro-entity |
| equity | 134693 | GBP | 2023-09-30 | 2025-06-27 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 125000 | GBP | 2023-09-30 | 2025-06-27 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 125000 | GBP | 2023-09-30 | 2024-04-05 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | 134693 | GBP | 2023-09-30 | 2024-04-05 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 134693 | GBP | 2023-09-30 | 2025-06-27 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 10215 | GBP | 2023-09-30 | 2025-06-27 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 10215 | GBP | 2023-09-30 | 2024-04-05 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 135215 | GBP | 2023-09-30 | 2024-04-05 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 135215 | GBP | 2023-09-30 | 2025-06-27 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2022-09-30 | 2024-04-05 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 160 | GBP | 2022-09-30 | 2024-04-05 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 144262 | GBP | 2022-09-30 | 2024-04-05 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 143676 | GBP | 2022-09-30 | 2024-04-05 | filed | yes | `core:Equity` | micro-entity |
| net_assets | 143676 | GBP | 2022-09-30 | 2024-04-05 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 144102 | GBP | 2022-09-30 | 2024-04-05 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 144102 | GBP | 2022-09-30 | 2024-04-05 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## BURNESS CORLETT THREE QUAYS (LONDON) LIMITED (`gb:02832627`)

- registration: `02832627` (GB), status active, incorporated 1993-07-02
- classification: ['71122'] (sic_2007)
- records: 18 officers, 1 beneficial owners, 0 ownership statements, 4 security interests, 140 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | xbrli:pure | 2025-03-31 | 2025-12-31 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 92 | GBP | 2025-03-31 | 2025-12-31 | filed | yes | `core:CashBankOnHand` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 80681 | GBP | 2025-03-31 | 2025-12-31 | filed | yes | `core:Creditors` | unaudited-abridged |
| current_assets | 40095 | GBP | 2025-03-31 | 2025-12-31 | filed | yes | `core:CurrentAssets` | unaudited-abridged |
| debtors | 40003 | GBP | 2025-03-31 | 2025-12-31 | filed | yes | `core:Debtors` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -69086 | GBP | 2025-03-31 | 2025-12-31 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 25000 | GBP | 2025-03-31 | 2025-12-31 | filed | yes | `core:Equity` | unaudited-abridged |
| equity | -40586 | GBP | 2025-03-31 | 2025-12-31 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 3500 | GBP | 2025-03-31 | 2025-12-31 | filed | yes | `core:Equity` | unaudited-abridged |
| net_assets | -40586 | GBP | 2025-03-31 | 2025-12-31 | filed | yes | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | -40586 | GBP | 2025-03-31 | 2025-12-31 | filed | yes | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | -40586 | GBP | 2025-03-31 | 2025-12-31 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 0 | xbrli:pure | 2024-03-31 | 2025-12-31 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| average_employees | 0 | xbrli:pure | 2024-03-31 | 2024-12-19 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 92 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `core:CashBankOnHand` | unaudited-abridged |
| cash | 92 | GBP | 2024-03-31 | 2025-12-31 | filed | yes | `core:CashBankOnHand` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 80681 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `core:Creditors` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 80681 | GBP | 2024-03-31 | 2025-12-31 | filed | yes | `core:Creditors` | unaudited-abridged |
| current_assets | 40095 | GBP | 2024-03-31 | 2025-12-31 | filed | yes | `core:CurrentAssets` | unaudited-abridged |
| current_assets | 40095 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `core:CurrentAssets` | unaudited-abridged |
| debtors | 40003 | GBP | 2024-03-31 | 2025-12-31 | filed | yes | `core:Debtors` | unaudited-abridged |
| debtors | 40003 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `core:Debtors` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 25000 | GBP | 2024-03-31 | 2025-12-31 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 3500 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -69086 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -69086 | GBP | 2024-03-31 | 2025-12-31 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 3500 | GBP | 2024-03-31 | 2025-12-31 | filed | yes | `core:Equity` | unaudited-abridged |
| equity | -40586 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `core:Equity` | unaudited-abridged |
| equity | -40586 | GBP | 2024-03-31 | 2025-12-31 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 25000 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `core:Equity` | unaudited-abridged |
| net_assets | -40586 | GBP | 2024-03-31 | 2025-12-31 | filed | yes | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_assets | -40586 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | -40586 | GBP | 2024-03-31 | 2025-12-31 | filed | yes | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| net_current_assets | -40586 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | -40586 | GBP | 2024-03-31 | 2025-12-31 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | -40586 | GBP | 2024-03-31 | 2024-12-19 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 0 | xbrli:pure | 2023-03-31 | 2024-12-19 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| average_employees | 0 | xbrli:pure | 2023-03-31 | 2023-11-14 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 92 | GBP | 2023-03-31 | 2023-11-14 | filed | no | `core:CashBankOnHand` | unaudited-abridged |
| cash | 92 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `core:CashBankOnHand` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 80681 | GBP | 2023-03-31 | 2023-11-14 | filed | no | `core:Creditors` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 80681 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `core:Creditors` | unaudited-abridged |
| current_assets | 40095 | GBP | 2023-03-31 | 2023-11-14 | filed | no | `core:CurrentAssets` | unaudited-abridged |
| current_assets | 40095 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `core:CurrentAssets` | unaudited-abridged |
| debtors | 40003 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `core:Debtors` | unaudited-abridged |
| debtors | 40003 | GBP | 2023-03-31 | 2023-11-14 | filed | no | `core:Debtors` | unaudited-abridged |
| equity | -40586 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 25000 | GBP | 2023-03-31 | 2023-11-14 | filed | no | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -69086 | GBP | 2023-03-31 | 2023-11-14 | filed | no | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 3500 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 3500 | GBP | 2023-03-31 | 2023-11-14 | filed | no | `core:Equity` | unaudited-abridged |
| equity | -40586 | GBP | 2023-03-31 | 2023-11-14 | filed | no | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 25000 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -69086 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `core:Equity` | unaudited-abridged |
| net_assets | -40586 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_assets | -40586 | GBP | 2023-03-31 | 2023-11-14 | filed | no | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | -40586 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| net_current_assets | -40586 | GBP | 2023-03-31 | 2023-11-14 | filed | no | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | -40586 | GBP | 2023-03-31 | 2023-11-14 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | -40586 | GBP | 2023-03-31 | 2024-12-19 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 0 | xbrli:pure | 2022-03-31 | 2023-11-14 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 92 | GBP | 2022-03-31 | 2023-11-14 | filed | yes | `core:CashBankOnHand` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 80681 | GBP | 2022-03-31 | 2023-11-14 | filed | yes | `core:Creditors` | unaudited-abridged |
| current_assets | 40095 | GBP | 2022-03-31 | 2023-11-14 | filed | yes | `core:CurrentAssets` | unaudited-abridged |
| debtors | 40003 | GBP | 2022-03-31 | 2023-11-14 | filed | yes | `core:Debtors` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 3500 | GBP | 2022-03-31 | 2023-11-14 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 25000 | GBP | 2022-03-31 | 2023-11-14 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -69086 | GBP | 2022-03-31 | 2023-11-14 | filed | yes | `core:Equity` | unaudited-abridged |
| equity | -40586 | GBP | 2022-03-31 | 2023-11-14 | filed | yes | `core:Equity` | unaudited-abridged |
| net_assets | -40586 | GBP | 2022-03-31 | 2023-11-14 | filed | yes | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | -40586 | GBP | 2022-03-31 | 2023-11-14 | filed | yes | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | -40586 | GBP | 2022-03-31 | 2023-11-14 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |

_No coverage facts for the latest run._

## ITIM LIMITED (`gb:03208792`)

- registration: `03208792` (GB), status active, incorporated 1996-06-06
- classification: ['62012'] (sic_2007)
- records: 22 officers, 1 beneficial owners, 0 ownership statements, 8 security interests, 188 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## M.P.E. SITE ENGINEERING LIMITED (`gb:03522090`)

- registration: `03522090` (GB), status active, incorporated 1998-03-04
- classification: ['71129'] (sic_2007)
- records: 6 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 74 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-03-31 | 2025-11-09 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 11161 | GBP | 2025-03-31 | 2025-11-09 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 12525 | GBP | 2025-03-31 | 2025-11-09 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 5007 | GBP | 2025-03-31 | 2025-11-09 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 4783 | GBP | 2025-03-31 | 2025-11-09 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 5007 | GBP | 2025-03-31 | 2025-11-09 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 1364 | GBP | 2025-03-31 | 2025-11-09 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 6147 | GBP | 2025-03-31 | 2025-11-09 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-03-31 | 2025-11-09 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-03-31 | 2024-10-20 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 8317 | GBP | 2024-03-31 | 2024-10-20 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 8317 | GBP | 2024-03-31 | 2025-11-09 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 3990 | GBP | 2024-03-31 | 2025-11-09 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 3990 | GBP | 2024-03-31 | 2024-10-20 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | -359 | GBP | 2024-03-31 | 2024-10-20 | filed | no | `core:Equity` | micro-entity |
| equity | -359 | GBP | 2024-03-31 | 2025-11-09 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 4868 | GBP | 2024-03-31 | 2025-11-09 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 4868 | GBP | 2024-03-31 | 2024-10-20 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | -359 | GBP | 2024-03-31 | 2024-10-20 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | -359 | GBP | 2024-03-31 | 2025-11-09 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -4327 | GBP | 2024-03-31 | 2024-10-20 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -4327 | GBP | 2024-03-31 | 2025-11-09 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 541 | GBP | 2024-03-31 | 2024-10-20 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 541 | GBP | 2024-03-31 | 2025-11-09 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-03-31 | 2024-10-20 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-03-31 | 2023-12-06 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 8079 | GBP | 2023-03-31 | 2024-10-20 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 8079 | GBP | 2023-03-31 | 2023-12-06 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 5615 | GBP | 2023-03-31 | 2024-10-20 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 5615 | GBP | 2023-03-31 | 2023-12-06 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 189 | GBP | 2023-03-31 | 2024-10-20 | filed | yes | `core:Equity` | micro-entity |
| equity | 189 | GBP | 2023-03-31 | 2023-12-06 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 3533 | GBP | 2023-03-31 | 2023-12-06 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 3533 | GBP | 2023-03-31 | 2024-10-20 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 189 | GBP | 2023-03-31 | 2023-12-06 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 189 | GBP | 2023-03-31 | 2024-10-20 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -2464 | GBP | 2023-03-31 | 2023-12-06 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -2464 | GBP | 2023-03-31 | 2024-10-20 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 1069 | GBP | 2023-03-31 | 2023-12-06 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 1069 | GBP | 2023-03-31 | 2024-10-20 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2022-03-31 | 2023-12-06 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 15798 | GBP | 2022-03-31 | 2023-12-06 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 15492 | GBP | 2022-03-31 | 2023-12-06 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 1195 | GBP | 2022-03-31 | 2023-12-06 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 2221 | GBP | 2022-03-31 | 2023-12-06 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 1195 | GBP | 2022-03-31 | 2023-12-06 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -306 | GBP | 2022-03-31 | 2023-12-06 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 1915 | GBP | 2022-03-31 | 2023-12-06 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## BIO TRADING LIMITED (`gb:03812170`)

- registration: `03812170` (GB), status active, incorporated 1999-07-22
- classification: ['46190', '59113', '59120', '62020'] (sic_2007)
- records: 12 officers, 3 beneficial owners, 0 ownership statements, 0 security interests, 131 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 3 | xbrli:pure | 2025-09-30 | 2026-02-03 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 9714 | GBP | 2025-09-30 | 2026-02-03 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 159039 | GBP | 2025-09-30 | 2026-02-03 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 149325 | GBP | 2025-09-30 | 2026-02-03 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 149325 | GBP | 2025-09-30 | 2026-02-03 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 112554 | GBP | 2025-09-30 | 2026-02-03 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 278 | GBP | 2025-09-30 | 2026-02-03 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 112871 | GBP | 2025-09-30 | 2026-02-03 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 20 | GBP | 2025-09-30 | 2026-02-03 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 19 | GBP | 2025-09-30 | 2026-02-03 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | 112871 | GBP | 2025-09-30 | 2026-02-03 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 112871 | GBP | 2025-09-30 | 2026-02-03 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 30 | xbrli:pure | 2024-09-30 | 2026-02-03 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 30 | xbrli:pure | 2024-09-30 | 2025-03-31 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 100762 | GBP | 2024-09-30 | 2026-02-03 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 100762 | GBP | 2024-09-30 | 2025-03-31 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 408926 | GBP | 2024-09-30 | 2025-03-31 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 408926 | GBP | 2024-09-30 | 2026-02-03 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 308164 | GBP | 2024-09-30 | 2025-03-31 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 308164 | GBP | 2024-09-30 | 2026-02-03 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 308164 | GBP | 2024-09-30 | 2026-02-03 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 308164 | GBP | 2024-09-30 | 2025-03-31 | filed | no | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 19 | GBP | 2024-09-30 | 2026-02-03 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 20 | GBP | 2024-09-30 | 2025-03-31 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 124267 | GBP | 2024-09-30 | 2026-02-03 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 216 | GBP | 2024-09-30 | 2026-02-03 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 124012 | GBP | 2024-09-30 | 2025-03-31 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 19 | GBP | 2024-09-30 | 2025-03-31 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 216 | GBP | 2024-09-30 | 2025-03-31 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 124012 | GBP | 2024-09-30 | 2026-02-03 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 124267 | GBP | 2024-09-30 | 2025-03-31 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 20 | GBP | 2024-09-30 | 2026-02-03 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 124267 | GBP | 2024-09-30 | 2025-03-31 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 124267 | GBP | 2024-09-30 | 2025-03-31 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 124267 | GBP | 2024-09-30 | 2026-02-03 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 124267 | GBP | 2024-09-30 | 2026-02-03 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 124267 | GBP | 2024-09-30 | 2025-03-31 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 37 | xbrli:pure | 2023-03-31 | 2025-03-31 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 345472 | GBP | 2023-03-31 | 2025-03-31 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 852212 | GBP | 2023-03-31 | 2025-03-31 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 506740 | GBP | 2023-03-31 | 2025-03-31 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 506740 | GBP | 2023-03-31 | 2025-03-31 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 20 | GBP | 2023-03-31 | 2025-03-31 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 19 | GBP | 2023-03-31 | 2025-03-31 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 476901 | GBP | 2023-03-31 | 2025-03-31 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 216 | GBP | 2023-03-31 | 2025-03-31 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 477156 | GBP | 2023-03-31 | 2025-03-31 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 477156 | GBP | 2023-03-31 | 2025-03-31 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 458353 | GBP | 2023-03-31 | 2025-03-31 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 481567 | GBP | 2023-03-31 | 2025-03-31 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## STRIVE AV LIMITED (`gb:04102256`)

- registration: `04102256` (GB), status active, incorporated 2000-11-06
- classification: ['62090'] (sic_2007)
- records: 18 officers, 3 beneficial owners, 0 ownership statements, 14 security interests, 151 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## ENS ASSOCIATES LIMITED (`gb:04401096`)

- registration: `04401096` (GB), status active, incorporated 2002-03-21
- classification: ['62090'] (sic_2007)
- records: 6 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 66 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-03-31 | 2025-12-24 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 11920 | GBP | 2025-03-31 | 2025-12-24 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 11920 | GBP | 2025-03-31 | 2025-12-24 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 0 | GBP | 2025-03-31 | 2025-12-24 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2025-03-31 | 2025-12-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 23634 | GBP | 2025-03-31 | 2025-12-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 23632 | GBP | 2025-03-31 | 2025-12-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | -9219 | GBP | 2025-03-31 | 2025-12-24 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 23634 | GBP | 2025-03-31 | 2025-12-24 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-03-31 | 2025-12-24 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-03-31 | 2024-12-23 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 6661 | GBP | 2024-03-31 | 2025-12-24 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 6661 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 15889 | GBP | 2024-03-31 | 2025-12-24 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 15889 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 9228 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 9228 | GBP | 2024-03-31 | 2025-12-24 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 42422 | GBP | 2024-03-31 | 2025-12-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 42424 | GBP | 2024-03-31 | 2025-12-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 42424 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 42422 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-03-31 | 2025-12-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `ns5:Equity` | total-exemption-full |
| net_current_assets | 240 | GBP | 2024-03-31 | 2025-12-24 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 240 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 42424 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 42424 | GBP | 2024-03-31 | 2025-12-24 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-03-31 | 2023-12-29 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-03-31 | 2024-12-23 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 81948 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 81948 | GBP | 2023-03-31 | 2023-12-29 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 81948 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 0 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-03-31 | 2023-12-29 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 22290 | GBP | 2023-03-31 | 2023-12-29 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 22290 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 22292 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 22292 | GBP | 2023-03-31 | 2023-12-29 | filed | no | `ns5:Equity` | total-exemption-full |
| net_current_assets | 13866 | GBP | 2023-03-31 | 2023-12-29 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 13866 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 22292 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 22292 | GBP | 2023-03-31 | 2023-12-29 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2022-03-31 | 2023-12-29 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 15282 | GBP | 2022-03-31 | 2023-12-29 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -47488 | GBP | 2022-03-31 | 2023-12-29 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2022-03-31 | 2023-12-29 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | -47486 | GBP | 2022-03-31 | 2023-12-29 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | -48550 | GBP | 2022-03-31 | 2023-12-29 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -47486 | GBP | 2022-03-31 | 2023-12-29 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## INSIGNIA CREATIVE LTD (`gb:04693927`)

- registration: `04693927` (GB), status active, incorporated 2003-03-12
- classification: ['62090'] (sic_2007)
- records: 5 officers, 0 beneficial owners, 1 ownership statements, 0 security interests, 64 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 5 | xbrli:pure | 2025-03-31 | 2025-12-23 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 53494 | GBP | 2025-03-31 | 2025-12-23 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 102559 | GBP | 2025-03-31 | 2025-12-23 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 34065 | GBP | 2025-03-31 | 2025-12-23 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200 | GBP | 2025-03-31 | 2025-12-23 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 74539 | GBP | 2025-03-31 | 2025-12-23 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 4988 | GBP | 2025-03-31 | 2025-12-23 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 74739 | GBP | 2025-03-31 | 2025-12-23 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 69751 | GBP | 2025-03-31 | 2025-12-23 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 74739 | GBP | 2025-03-31 | 2025-12-23 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 6 | xbrli:pure | 2024-03-31 | 2025-12-23 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 6 | xbrli:pure | 2024-03-31 | 2024-12-17 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 35061 | GBP | 2024-03-31 | 2024-12-17 | filed | no | `frs-core:CashBankOnHand` | total-exemption-full |
| cash | 35061 | GBP | 2024-03-31 | 2025-12-23 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 96235 | GBP | 2024-03-31 | 2024-12-17 | filed | no | `frs-core:CurrentAssets` | total-exemption-full |
| current_assets | 96235 | GBP | 2024-03-31 | 2025-12-23 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 46174 | GBP | 2024-03-31 | 2024-12-17 | filed | no | `frs-core:Debtors` | total-exemption-full |
| debtors | 46174 | GBP | 2024-03-31 | 2025-12-23 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 76410 | GBP | 2024-03-31 | 2024-12-17 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 190 | GBP | 2024-03-31 | 2025-12-23 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 76410 | GBP | 2024-03-31 | 2025-12-23 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 190 | GBP | 2024-03-31 | 2024-12-17 | filed | no | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 5436 | GBP | 2024-03-31 | 2025-12-23 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| fixed_assets | 5436 | GBP | 2024-03-31 | 2024-12-17 | filed | no | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 76600 | GBP | 2024-03-31 | 2024-12-17 | filed | no | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 76600 | GBP | 2024-03-31 | 2025-12-23 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 71164 | GBP | 2024-03-31 | 2024-12-17 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 71164 | GBP | 2024-03-31 | 2025-12-23 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 76600 | GBP | 2024-03-31 | 2024-12-17 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 76600 | GBP | 2024-03-31 | 2025-12-23 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 6 | xbrli:pure | 2023-03-31 | 2023-12-21 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 6 | xbrli:pure | 2023-03-31 | 2024-12-17 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 38969 | GBP | 2023-03-31 | 2023-12-21 | filed | no | `frs-core:CashBankOnHand` | total-exemption-full |
| cash | 38969 | GBP | 2023-03-31 | 2024-12-17 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 93216 | GBP | 2023-03-31 | 2023-12-21 | filed | no | `frs-core:CurrentAssets` | total-exemption-full |
| current_assets | 93216 | GBP | 2023-03-31 | 2024-12-17 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 39247 | GBP | 2023-03-31 | 2024-12-17 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| debtors | 39247 | GBP | 2023-03-31 | 2023-12-21 | filed | no | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 72104 | GBP | 2023-03-31 | 2024-12-17 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 72104 | GBP | 2023-03-31 | 2023-12-21 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200 | GBP | 2023-03-31 | 2023-12-21 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200 | GBP | 2023-03-31 | 2024-12-17 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 4076 | GBP | 2023-03-31 | 2023-12-21 | filed | no | `frs-core:FixedAssets` | total-exemption-full |
| fixed_assets | 4076 | GBP | 2023-03-31 | 2024-12-17 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 72304 | GBP | 2023-03-31 | 2023-12-21 | filed | no | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 72304 | GBP | 2023-03-31 | 2024-12-17 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 68228 | GBP | 2023-03-31 | 2024-12-17 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 68228 | GBP | 2023-03-31 | 2023-12-21 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 72304 | GBP | 2023-03-31 | 2023-12-21 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 72304 | GBP | 2023-03-31 | 2024-12-17 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 6 | xbrli:pure | 2022-03-31 | 2023-12-21 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 39002 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 87511 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 33509 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 63311 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 3432 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 63511 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 60079 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 63511 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## ANDION IT LIMITED (`gb:05077901`)

- registration: `05077901` (GB), status active, incorporated 2004-03-18
- classification: ['62012', '62020'] (sic_2007)
- records: 5 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 59 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | iso4217:GBP | 2026-03-31 | 2026-08-19 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 6421 | GBP | 2026-03-31 | 2026-08-19 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 71587 | GBP | 2026-03-31 | 2026-08-19 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 69241 | GBP | 2026-03-31 | 2026-08-19 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 69241 | GBP | 2026-03-31 | 2026-08-19 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 69241 | GBP | 2026-03-31 | 2026-08-19 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 69241 | GBP | 2026-03-31 | 2026-08-19 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2025-03-31 | 2025-08-19 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2025-03-31 | 2026-08-19 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 13214 | GBP | 2025-03-31 | 2025-08-19 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 13214 | GBP | 2025-03-31 | 2026-08-19 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 77266 | GBP | 2025-03-31 | 2026-08-19 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 77266 | GBP | 2025-03-31 | 2025-08-19 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | 73340 | GBP | 2025-03-31 | 2026-08-19 | filed | yes | `uk-core:Equity` | micro-entity |
| equity | 73340 | GBP | 2025-03-31 | 2025-08-19 | filed | no | `uk-core:Equity` | micro-entity |
| net_assets | 73340 | GBP | 2025-03-31 | 2026-08-19 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 73340 | GBP | 2025-03-31 | 2025-08-19 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 73340 | GBP | 2025-03-31 | 2025-08-19 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 73340 | GBP | 2025-03-31 | 2026-08-19 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 73340 | GBP | 2025-03-31 | 2025-08-19 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 73340 | GBP | 2025-03-31 | 2026-08-19 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2024-03-31 | 2024-08-23 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2024-03-31 | 2025-08-19 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2024-03-31 | 2024-08-23 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 22005 | GBP | 2024-03-31 | 2024-08-23 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 22005 | GBP | 2024-03-31 | 2025-08-19 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 75614 | GBP | 2024-03-31 | 2024-08-23 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 75614 | GBP | 2024-03-31 | 2025-08-19 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 58768 | GBP | 2024-03-31 | 2025-08-19 | filed | yes | `uk-core:Equity` | micro-entity |
| equity | 58768 | GBP | 2024-03-31 | 2024-08-23 | filed | no | `uk-core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2024-03-31 | 2024-08-23 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 58768 | GBP | 2024-03-31 | 2025-08-19 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 58768 | GBP | 2024-03-31 | 2024-08-23 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 58768 | GBP | 2024-03-31 | 2025-08-19 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 58768 | GBP | 2024-03-31 | 2024-08-23 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 58768 | GBP | 2024-03-31 | 2024-08-23 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 58768 | GBP | 2024-03-31 | 2025-08-19 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2023-03-31 | 2024-08-23 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2023-03-31 | 2024-08-23 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 4921 | GBP | 2023-03-31 | 2024-08-23 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 31364 | GBP | 2023-03-31 | 2024-08-23 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 26443 | GBP | 2023-03-31 | 2024-08-23 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2023-03-31 | 2024-08-23 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 26443 | GBP | 2023-03-31 | 2024-08-23 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 26443 | GBP | 2023-03-31 | 2024-08-23 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 26443 | GBP | 2023-03-31 | 2024-08-23 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._
