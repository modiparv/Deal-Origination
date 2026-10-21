# Ingest spot-check

- database: `data/engine.db`
- latest run: `20261021T071116Z-736af48a`
- companies in store: 32200; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## WESTBAY ENGINEERS LIMITED (`gb:02394702`)

- registration: `02394702` (GB), status active, incorporated 1989-06-13
- classification: ['61900', '62012'] (sic_2007)
- records: 3 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 93 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-11-30 | 2026-04-09 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2025-11-30 | 2026-04-09 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 3189 | GBP | 2025-11-30 | 2026-04-09 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 30760 | GBP | 2025-11-30 | 2026-04-09 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 286755 | GBP | 2025-11-30 | 2026-04-09 | filed | yes | `core:Equity` | micro-entity |
| net_assets | 286755 | GBP | 2025-11-30 | 2026-04-09 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 27571 | GBP | 2025-11-30 | 2026-04-09 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 286755 | GBP | 2025-11-30 | 2026-04-09 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-11-30 | 2026-04-09 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-11-30 | 2025-05-19 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2024-11-30 | 2025-05-19 | filed | no | `core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2024-11-30 | 2026-04-09 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2010 | GBP | 2024-11-30 | 2025-05-19 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2010 | GBP | 2024-11-30 | 2026-04-09 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 26402 | GBP | 2024-11-30 | 2025-05-19 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 26402 | GBP | 2024-11-30 | 2026-04-09 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 283757 | GBP | 2024-11-30 | 2025-05-19 | filed | no | `core:Equity` | micro-entity |
| equity | 283757 | GBP | 2024-11-30 | 2026-04-09 | filed | yes | `core:Equity` | micro-entity |
| net_assets | 283757 | GBP | 2024-11-30 | 2025-05-19 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 283757 | GBP | 2024-11-30 | 2026-04-09 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 24392 | GBP | 2024-11-30 | 2026-04-09 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 24392 | GBP | 2024-11-30 | 2025-05-19 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 283757 | GBP | 2024-11-30 | 2026-04-09 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 283757 | GBP | 2024-11-30 | 2025-05-19 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-11-30 | 2025-05-19 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-11-30 | 2024-06-21 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2023-11-30 | 2025-05-19 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 678 | GBP | 2023-11-30 | 2025-05-19 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2023-11-30 | 2024-06-21 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 17760 | GBP | 2023-11-30 | 2025-05-19 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 17082 | GBP | 2023-11-30 | 2024-06-21 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 276725 | GBP | 2023-11-30 | 2024-06-21 | filed | no | `core:Equity` | micro-entity |
| equity | 276725 | GBP | 2023-11-30 | 2025-05-19 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 259643 | GBP | 2023-11-30 | 2024-06-21 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 276725 | GBP | 2023-11-30 | 2025-05-19 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 276725 | GBP | 2023-11-30 | 2024-06-21 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 17082 | GBP | 2023-11-30 | 2025-05-19 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 17082 | GBP | 2023-11-30 | 2024-06-21 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 276725 | GBP | 2023-11-30 | 2025-05-19 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 276725 | GBP | 2023-11-30 | 2024-06-21 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 3470 | GBP | 2022-11-30 | 2024-06-21 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 25484 | GBP | 2022-11-30 | 2024-06-21 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 275769 | GBP | 2022-11-30 | 2024-06-21 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 253755 | GBP | 2022-11-30 | 2024-06-21 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 275769 | GBP | 2022-11-30 | 2024-06-21 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 22014 | GBP | 2022-11-30 | 2024-06-21 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 275769 | GBP | 2022-11-30 | 2024-06-21 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2025-05-19: `{"superseded_document_id": "gb:02394702:doc:2UaSp-En311Eo3prYxcUeM8ahcX-PbSIwYWDb4-cqhk", "restatements": [{"concept": "current_assets", "period_end": "2023-11-30", "old_value": "17082.0000", "new_val`

## PEAR TECHNOLOGY SERVICES LIMITED (`gb:03013412`)

- registration: `03013412` (GB), status active, incorporated 1995-01-24
- classification: ['62012', '62020', '62090'] (sic_2007)
- records: 13 officers, 5 beneficial owners, 1 ownership statements, 0 security interests, 145 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.13 | xbrli:pure | 2025-03-31 | 2025-12-18 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 197126 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 2500 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 463426 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 375544 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 166876 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 166876 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 121373 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 205273 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 80950 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 1700 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1250 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 295655 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | 205273 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -87882 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 207773 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0.12 | xbrli:pure | 2024-03-31 | 2025-12-18 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 12 | xbrli:pure | 2024-03-31 | 2024-12-23 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 125131 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 125131 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 52500 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 52500 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 352375 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 352375 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 317836 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 317836 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 175680 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 175680 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 175680 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 175680 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 80950 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:Equity` | total-exemption-full |
| equity | 264597 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 1700 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1250 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 180697 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:Equity` | total-exemption-full |
| equity | 264597 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 1700 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 180697 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 80950 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1250 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 351636 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:FixedAssets` | total-exemption-full |
| fixed_assets | 351636 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | 264597 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 264597 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -34539 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -34539 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 317097 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 317097 | GBP | 2024-03-31 | 2024-12-23 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 14 | xbrli:pure | 2023-03-31 | 2023-12-19 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 14 | xbrli:pure | 2023-03-31 | 2024-12-23 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 169826 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 169826 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 22500 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 22500 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 140999 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 140999 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 368816 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 368816 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 180183 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 180183 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 180183 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 180183 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:Debtors` | total-exemption-full |
| equity | 422303 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 1700 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1250 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 1700 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1250 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 80950 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 80950 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 338403 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 338403 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:Equity` | total-exemption-full |
| equity | 422303 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:Equity` | total-exemption-full |
| fixed_assets | 216986 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:FixedAssets` | total-exemption-full |
| fixed_assets | 216986 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | 422303 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 422303 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 227817 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 227817 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 444803 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 444803 | GBP | 2023-03-31 | 2024-12-23 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 14 | xbrli:pure | 2022-03-31 | 2023-12-19 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 295243 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 32500 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 199341 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 531702 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 216720 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 216720 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 460045 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 1700 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1575 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 104828 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 568148 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 268287 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | 568148 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 332361 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 600648 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2025-12-18: `{"superseded_document_id": "gb:03013412:doc:nrtbZvaaC_pPIIf1G_H-9kCfDPMQOtddh1kv6DYMSvM", "restatements": [{"concept": "average_employees", "period_end": "2024-03-31", "old_value": "12.0000", "new_val`

## CONSCIOUS VISIONS LIMITED (`gb:03416138`)

- registration: `03416138` (GB), status active, incorporated 1997-08-07
- classification: ['47910', '62020', '68209'] (sic_2007)
- records: 5 officers, 1 beneficial owners, 0 ownership statements, 4 security interests, 75 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-08-31 | 2026-05-29 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 79864 | GBP | 2025-08-31 | 2026-05-29 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| equity | 341022 | GBP | 2025-08-31 | 2026-05-29 | filed | yes | `frs-core:Equity` | micro-entity |
| fixed_assets | 405900 | GBP | 2025-08-31 | 2026-05-29 | filed | yes | `frs-core:FixedAssets` | micro-entity |
| net_assets | 341022 | GBP | 2025-08-31 | 2026-05-29 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 79135 | GBP | 2025-08-31 | 2026-05-29 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 485035 | GBP | 2025-08-31 | 2026-05-29 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-08-31 | 2025-05-30 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-08-31 | 2026-05-29 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 90069 | GBP | 2024-08-31 | 2026-05-29 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| current_assets | 90069 | GBP | 2024-08-31 | 2025-05-30 | filed | no | `frs-core:CurrentAssets` | micro-entity |
| equity | 338184 | GBP | 2024-08-31 | 2025-05-30 | filed | no | `frs-core:Equity` | micro-entity |
| equity | 338184 | GBP | 2024-08-31 | 2026-05-29 | filed | yes | `frs-core:Equity` | micro-entity |
| fixed_assets | 405900 | GBP | 2024-08-31 | 2025-05-30 | filed | no | `frs-core:FixedAssets` | micro-entity |
| fixed_assets | 405900 | GBP | 2024-08-31 | 2026-05-29 | filed | yes | `frs-core:FixedAssets` | micro-entity |
| net_assets | 338184 | GBP | 2024-08-31 | 2026-05-29 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 338184 | GBP | 2024-08-31 | 2025-05-30 | filed | no | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 88209 | GBP | 2024-08-31 | 2026-05-29 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 88209 | GBP | 2024-08-31 | 2025-05-30 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 494109 | GBP | 2024-08-31 | 2026-05-29 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 494109 | GBP | 2024-08-31 | 2025-05-30 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-08-31 | 2024-05-28 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-08-31 | 2025-05-30 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| cash | 42024 | GBP | 2023-08-31 | 2024-05-28 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 107569 | GBP | 2023-08-31 | 2025-05-30 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| current_assets | 107569 | GBP | 2023-08-31 | 2024-05-28 | filed | no | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 55000 | GBP | 2023-08-31 | 2024-05-28 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2023-08-31 | 2024-05-28 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 343494 | GBP | 2023-08-31 | 2024-05-28 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity | 344494 | GBP | 2023-08-31 | 2025-05-30 | filed | yes | `frs-core:Equity` | micro-entity |
| fixed_assets | 405900 | GBP | 2023-08-31 | 2024-05-28 | filed | no | `frs-core:FixedAssets` | total-exemption-full |
| fixed_assets | 405900 | GBP | 2023-08-31 | 2025-05-30 | filed | yes | `frs-core:FixedAssets` | micro-entity |
| net_assets | 344494 | GBP | 2023-08-31 | 2024-05-28 | filed | no | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 344494 | GBP | 2023-08-31 | 2025-05-30 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 104746 | GBP | 2023-08-31 | 2024-05-28 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 105466 | GBP | 2023-08-31 | 2025-05-30 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 511366 | GBP | 2023-08-31 | 2025-05-30 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 510646 | GBP | 2023-08-31 | 2024-05-28 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 3 | xbrli:pure | 2022-08-31 | 2024-05-28 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 36306 | GBP | 2022-08-31 | 2024-05-28 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 123774 | GBP | 2022-08-31 | 2024-05-28 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 75604 | GBP | 2022-08-31 | 2024-05-28 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 349205 | GBP | 2022-08-31 | 2024-05-28 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2022-08-31 | 2024-05-28 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 405900 | GBP | 2022-08-31 | 2024-05-28 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 350205 | GBP | 2022-08-31 | 2024-05-28 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 122023 | GBP | 2022-08-31 | 2024-05-28 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 527923 | GBP | 2022-08-31 | 2024-05-28 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2025-05-30: `{"superseded_document_id": "gb:03416138:doc:aL6jYJMe9K8o6kuyTmdv-VUykqChHsm5BvDAv-WHheE", "restatements": [{"concept": "net_current_assets", "period_end": "2023-08-31", "old_value": "104746.0000", "ne`

## COMPUTER FRIENDLY CONSULTANTS LIMITED (`gb:03763879`)

- registration: `03763879` (GB), status active, incorporated 1999-05-04
- classification: ['62020'] (sic_2007)
- records: 8 officers, 3 beneficial owners, 1 ownership statements, 0 security interests, 86 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 4 | xbrli:pure | 2025-03-31 | 2025-11-18 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 40866 | GBP | 2025-03-31 | 2025-11-18 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| equity | 14157 | GBP | 2025-03-31 | 2025-11-18 | filed | yes | `frs-core:Equity` | micro-entity |
| fixed_assets | 46758 | GBP | 2025-03-31 | 2025-11-18 | filed | yes | `frs-core:FixedAssets` | micro-entity |
| net_assets | 14157 | GBP | 2025-03-31 | 2025-11-18 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -11914 | GBP | 2025-03-31 | 2025-11-18 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 34844 | GBP | 2025-03-31 | 2025-11-18 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 4 | xbrli:pure | 2024-03-31 | 2025-11-18 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 4 | xbrli:pure | 2024-03-31 | 2024-11-28 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 32204 | GBP | 2024-03-31 | 2024-11-28 | filed | no | `frs-core:CurrentAssets` | micro-entity |
| current_assets | 32204 | GBP | 2024-03-31 | 2025-11-18 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| equity | 14226 | GBP | 2024-03-31 | 2024-11-28 | filed | no | `frs-core:Equity` | micro-entity |
| equity | 14226 | GBP | 2024-03-31 | 2025-11-18 | filed | yes | `frs-core:Equity` | micro-entity |
| fixed_assets | 57879 | GBP | 2024-03-31 | 2024-11-28 | filed | no | `frs-core:FixedAssets` | micro-entity |
| fixed_assets | 57879 | GBP | 2024-03-31 | 2025-11-18 | filed | yes | `frs-core:FixedAssets` | micro-entity |
| net_assets | 14226 | GBP | 2024-03-31 | 2024-11-28 | filed | no | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 14226 | GBP | 2024-03-31 | 2025-11-18 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -10189 | GBP | 2024-03-31 | 2025-11-18 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -10189 | GBP | 2024-03-31 | 2024-11-28 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 47690 | GBP | 2024-03-31 | 2024-11-28 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 47690 | GBP | 2024-03-31 | 2025-11-18 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 4 | xbrli:pure | 2023-03-31 | 2023-06-26 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 4 | xbrli:pure | 2023-03-31 | 2024-11-28 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 58582 | GBP | 2023-03-31 | 2023-06-26 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 14671 | GBP | 2023-03-31 | 2023-06-26 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 34692 | GBP | 2023-03-31 | 2023-06-26 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 34692 | GBP | 2023-03-31 | 2024-11-28 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| equity | 9288 | GBP | 2023-03-31 | 2023-06-26 | filed | no | `core:Equity` | micro-entity |
| equity | 9288 | GBP | 2023-03-31 | 2024-11-28 | filed | yes | `frs-core:Equity` | micro-entity |
| fixed_assets | 47849 | GBP | 2023-03-31 | 2023-06-26 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 47849 | GBP | 2023-03-31 | 2024-11-28 | filed | yes | `frs-core:FixedAssets` | micro-entity |
| net_assets | 9288 | GBP | 2023-03-31 | 2024-11-28 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 20021 | GBP | 2023-03-31 | 2023-06-26 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 20021 | GBP | 2023-03-31 | 2024-11-28 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 67870 | GBP | 2023-03-31 | 2024-11-28 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 67870 | GBP | 2023-03-31 | 2023-06-26 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 4 | xbrli:pure | 2022-03-31 | 2023-06-26 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 28637 | GBP | 2022-03-31 | 2023-06-26 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 11211 | GBP | 2022-03-31 | 2023-06-26 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 31608 | GBP | 2022-03-31 | 2023-06-26 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 14448 | GBP | 2022-03-31 | 2023-06-26 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 23801 | GBP | 2022-03-31 | 2023-06-26 | filed | yes | `core:FixedAssets` | micro-entity |
| net_current_assets `{'RestatementsFirstTimeAdoptionDimension': 'RestatedAmount'}` | 20397 | GBP | 2022-03-31 | 2023-06-26 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities `{'RestatementsFirstTimeAdoptionDimension': 'RestatedAmount'}` | 44198 | GBP | 2022-03-31 | 2023-06-26 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## TPS SERVICES LIMITED (`gb:04118095`)

- registration: `04118095` (GB), status active, incorporated 2000-12-01
- classification: ['20411', '47750', '62090', '85590'] (sic_2007)
- records: 4 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 66 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-11-30 | 2026-07-16 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 12064 | GBP | 2025-11-30 | 2026-07-16 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 16792 | GBP | 2025-11-30 | 2026-07-16 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 4728 | GBP | 2025-11-30 | 2026-07-16 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2025-11-30 | 2026-07-16 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -3113 | GBP | 2025-11-30 | 2026-07-16 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 0 | GBP | 2025-11-30 | 2026-07-16 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | -3111 | GBP | 2025-11-30 | 2026-07-16 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -3111 | GBP | 2025-11-30 | 2026-07-16 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -3111 | GBP | 2025-11-30 | 2026-07-16 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-11-30 | 2026-07-16 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-11-30 | 2025-04-23 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 18656 | GBP | 2024-11-30 | 2025-04-23 | filed | no | `frs-core:CashBankOnHand` | total-exemption-full |
| cash | 18656 | GBP | 2024-11-30 | 2026-07-16 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 23384 | GBP | 2024-11-30 | 2026-07-16 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| current_assets | 23384 | GBP | 2024-11-30 | 2025-04-23 | filed | no | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 4728 | GBP | 2024-11-30 | 2026-07-16 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| debtors | 4728 | GBP | 2024-11-30 | 2025-04-23 | filed | no | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 4292 | GBP | 2024-11-30 | 2025-04-23 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-11-30 | 2025-04-23 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 4292 | GBP | 2024-11-30 | 2026-07-16 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-11-30 | 2026-07-16 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 45 | GBP | 2024-11-30 | 2026-07-16 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| fixed_assets | 45 | GBP | 2024-11-30 | 2025-04-23 | filed | no | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 4294 | GBP | 2024-11-30 | 2025-04-23 | filed | no | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 4294 | GBP | 2024-11-30 | 2026-07-16 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 4249 | GBP | 2024-11-30 | 2026-07-16 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 4249 | GBP | 2024-11-30 | 2025-04-23 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 4294 | GBP | 2024-11-30 | 2025-04-23 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 4294 | GBP | 2024-11-30 | 2026-07-16 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-11-30 | 2025-04-23 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-11-30 | 2024-08-07 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 22129 | GBP | 2023-11-30 | 2024-08-07 | filed | no | `frs-core:CashBankOnHand` | total-exemption-full |
| cash | 22129 | GBP | 2023-11-30 | 2025-04-23 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 26857 | GBP | 2023-11-30 | 2025-04-23 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| current_assets | 26857 | GBP | 2023-11-30 | 2024-08-07 | filed | no | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 4728 | GBP | 2023-11-30 | 2025-04-23 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| debtors | 4728 | GBP | 2023-11-30 | 2024-08-07 | filed | no | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-11-30 | 2024-08-07 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 6073 | GBP | 2023-11-30 | 2025-04-23 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-11-30 | 2025-04-23 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 6073 | GBP | 2023-11-30 | 2024-08-07 | filed | no | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 95 | GBP | 2023-11-30 | 2025-04-23 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| fixed_assets | 95 | GBP | 2023-11-30 | 2024-08-07 | filed | no | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 6075 | GBP | 2023-11-30 | 2024-08-07 | filed | no | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 6075 | GBP | 2023-11-30 | 2025-04-23 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 5980 | GBP | 2023-11-30 | 2025-04-23 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 5980 | GBP | 2023-11-30 | 2024-08-07 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 6075 | GBP | 2023-11-30 | 2024-08-07 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 6075 | GBP | 2023-11-30 | 2025-04-23 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2022-11-30 | 2024-08-07 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 48233 | GBP | 2022-11-30 | 2024-08-07 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 52961 | GBP | 2022-11-30 | 2024-08-07 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 4728 | GBP | 2022-11-30 | 2024-08-07 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2022-11-30 | 2024-08-07 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 20793 | GBP | 2022-11-30 | 2024-08-07 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 145 | GBP | 2022-11-30 | 2024-08-07 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 20795 | GBP | 2022-11-30 | 2024-08-07 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 20650 | GBP | 2022-11-30 | 2024-08-07 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 20795 | GBP | 2022-11-30 | 2024-08-07 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## FIRST CLASS SYSTEMS LTD (`gb:04477269`)

- registration: `04477269` (GB), status active, incorporated 2002-07-04
- classification: ['62012', '62020'] (sic_2007)
- records: 5 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 58 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-07-31 | 2025-12-29 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 18608 | GBP | 2025-07-31 | 2025-12-29 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 14444 | GBP | 2025-07-31 | 2025-12-29 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 18608 | GBP | 2025-07-31 | 2025-12-29 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| net_assets | 73107 | GBP | 2025-07-31 | 2025-12-29 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 4164 | GBP | 2025-07-31 | 2025-12-29 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-07-31 | 2025-12-29 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-07-31 | 2025-01-30 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 47290 | GBP | 2024-07-31 | 2025-12-29 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 47290 | GBP | 2024-07-31 | 2025-01-30 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 15570 | GBP | 2024-07-31 | 2025-12-29 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 15570 | GBP | 2024-07-31 | 2025-01-30 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 49448 | GBP | 2024-07-31 | 2025-01-30 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 49448 | GBP | 2024-07-31 | 2025-12-29 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 2158 | GBP | 2024-07-31 | 2025-01-30 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2158 | GBP | 2024-07-31 | 2025-01-30 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2158 | GBP | 2024-07-31 | 2025-12-29 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 2158 | GBP | 2024-07-31 | 2025-12-29 | filed | yes | `core:Debtors` | total-exemption-full |
| fixed_assets | 48576 | GBP | 2024-07-31 | 2025-01-30 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | 82454 | GBP | 2024-07-31 | 2025-12-29 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 82454 | GBP | 2024-07-31 | 2025-01-30 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 33878 | GBP | 2024-07-31 | 2025-01-30 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 33878 | GBP | 2024-07-31 | 2025-12-29 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-07-31 | 2025-01-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-07-31 | 2024-02-27 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 101718 | GBP | 2023-07-31 | 2024-02-27 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 101718 | GBP | 2023-07-31 | 2025-01-30 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 15102 | GBP | 2023-07-31 | 2024-02-27 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 15102 | GBP | 2023-07-31 | 2025-01-30 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 103791 | GBP | 2023-07-31 | 2025-01-30 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 103791 | GBP | 2023-07-31 | 2024-02-27 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 2073 | GBP | 2023-07-31 | 2025-01-30 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 2073 | GBP | 2023-07-31 | 2024-02-27 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 2073 | GBP | 2023-07-31 | 2025-01-30 | filed | yes | `core:Debtors` | total-exemption-full |
| fixed_assets | 15142 | GBP | 2023-07-31 | 2024-02-27 | filed | no | `core:FixedAssets` | total-exemption-full |
| fixed_assets | 15142 | GBP | 2023-07-31 | 2025-01-30 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | 103831 | GBP | 2023-07-31 | 2024-02-27 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 103831 | GBP | 2023-07-31 | 2025-01-30 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 88689 | GBP | 2023-07-31 | 2024-02-27 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 88689 | GBP | 2023-07-31 | 2025-01-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2022-07-31 | 2024-02-27 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 132631 | GBP | 2022-07-31 | 2024-02-27 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 20104 | GBP | 2022-07-31 | 2024-02-27 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 132631 | GBP | 2022-07-31 | 2024-02-27 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| fixed_assets | 424 | GBP | 2022-07-31 | 2024-02-27 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | 112951 | GBP | 2022-07-31 | 2024-02-27 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 112527 | GBP | 2022-07-31 | 2024-02-27 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## NAKED OBJECTS GROUP LIMITED (`gb:04842860`)

- registration: `04842860` (GB), status active, incorporated 2003-07-23
- classification: ['62012'] (sic_2007)
- records: 8 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 79 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 3 | xbrli:pure | 2025-12-31 | 2026-03-17 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 105046 | GBP | 2025-12-31 | 2026-03-17 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 12831 | GBP | 2025-12-31 | 2026-03-17 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 550 | GBP | 2025-12-31 | 2026-03-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 83368 | GBP | 2025-12-31 | 2026-03-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 350 | GBP | 2025-12-31 | 2026-03-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 84268 | GBP | 2025-12-31 | 2026-03-17 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 84268 | GBP | 2025-12-31 | 2026-03-17 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| average_employees | 3 | xbrli:pure | 2024-12-31 | 2025-05-21 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 3 | xbrli:pure | 2024-12-31 | 2026-03-17 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 99627 | GBP | 2024-12-31 | 2025-05-21 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 99627 | GBP | 2024-12-31 | 2026-03-17 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 420 | GBP | 2024-12-31 | 2025-05-21 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 420 | GBP | 2024-12-31 | 2026-03-17 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 70129 | GBP | 2024-12-31 | 2025-05-21 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 69229 | GBP | 2024-12-31 | 2026-03-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 70129 | GBP | 2024-12-31 | 2026-03-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 350 | GBP | 2024-12-31 | 2026-03-17 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 550 | GBP | 2024-12-31 | 2025-05-21 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 69229 | GBP | 2024-12-31 | 2025-05-21 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 350 | GBP | 2024-12-31 | 2025-05-21 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 550 | GBP | 2024-12-31 | 2026-03-17 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 70129 | GBP | 2024-12-31 | 2026-03-17 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 70129 | GBP | 2024-12-31 | 2025-05-21 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| average_employees | 3 | xbrli:pure | 2023-12-31 | 2024-05-21 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 3 | xbrli:pure | 2023-12-31 | 2025-05-21 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 106115 | GBP | 2023-12-31 | 2025-05-21 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 824 | GBP | 2023-12-31 | 2025-05-21 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 824 | GBP | 2023-12-31 | 2024-05-21 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 76582 | GBP | 2023-12-31 | 2025-05-21 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 550 | GBP | 2023-12-31 | 2025-05-21 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 350 | GBP | 2023-12-31 | 2025-05-21 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 75682 | GBP | 2023-12-31 | 2025-05-21 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 76582 | GBP | 2023-12-31 | 2025-05-21 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| average_employees | 3 | xbrli:pure | 2022-12-31 | 2024-05-21 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 704 | GBP | 2022-12-31 | 2024-05-21 | filed | yes | `ns5:Debtors` | total-exemption-full |

_No coverage facts for the latest run._

## EFINI DESIGN LIMITED (`gb:05210086`)

- registration: `05210086` (GB), status active, incorporated 2004-08-19
- classification: ['71122'] (sic_2007)
- records: 3 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 46 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2021-08-31 | 2022-03-01 | filed | yes | `ns6:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 514 | GBP | 2021-08-31 | 2022-03-01 | filed | yes | `ns6:CashBankOnHand` | total-exemption-full |
| current_assets | 642 | GBP | 2021-08-31 | 2022-03-01 | filed | yes | `ns6:CurrentAssets` | total-exemption-full |
| debtors | 128 | GBP | 2021-08-31 | 2022-03-01 | filed | yes | `ns6:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -11165 | GBP | 2021-08-31 | 2022-03-01 | filed | yes | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2021-08-31 | 2022-03-01 | filed | yes | `ns6:Equity` | total-exemption-full |
| equity | -10165 | GBP | 2021-08-31 | 2022-03-01 | filed | yes | `ns6:Equity` | total-exemption-full |
| net_assets | -10165 | GBP | 2021-08-31 | 2022-03-01 | filed | yes | `ns6:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -2912 | GBP | 2021-08-31 | 2022-03-01 | filed | yes | `ns6:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -11347 | GBP | 2021-08-31 | 2022-03-01 | filed | yes | `ns6:ProfitLoss` | total-exemption-full |
| total_assets_less_current_liabilities | -2165 | GBP | 2021-08-31 | 2022-03-01 | filed | yes | `ns6:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2020-08-31 | 2021-02-22 | filed | no | `ns6:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2020-08-31 | 2022-03-01 | filed | yes | `ns6:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 9701 | GBP | 2020-08-31 | 2022-03-01 | filed | yes | `ns6:CashBankOnHand` | total-exemption-full |
| cash | 9701 | GBP | 2020-08-31 | 2021-02-22 | filed | no | `ns6:CashBankOnHand` | total-exemption-full |
| current_assets | 9701 | GBP | 2020-08-31 | 2022-03-01 | filed | yes | `ns6:CurrentAssets` | total-exemption-full |
| current_assets | 9701 | GBP | 2020-08-31 | 2021-02-22 | filed | no | `ns6:CurrentAssets` | total-exemption-full |
| debtors | 0 | GBP | 2020-08-31 | 2022-03-01 | filed | yes | `ns6:Debtors` | total-exemption-full |
| debtors | 0 | GBP | 2020-08-31 | 2021-02-22 | filed | no | `ns6:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 182 | GBP | 2020-08-31 | 2021-02-22 | filed | no | `ns6:Equity` | total-exemption-full |
| equity | 1182 | GBP | 2020-08-31 | 2022-03-01 | filed | yes | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2020-08-31 | 2021-02-22 | filed | no | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 182 | GBP | 2020-08-31 | 2022-03-01 | filed | yes | `ns6:Equity` | total-exemption-full |
| equity | 1182 | GBP | 2020-08-31 | 2021-02-22 | filed | no | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2020-08-31 | 2022-03-01 | filed | yes | `ns6:Equity` | total-exemption-full |
| net_assets | 1182 | GBP | 2020-08-31 | 2022-03-01 | filed | yes | `ns6:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 186 | GBP | 2020-08-31 | 2022-03-01 | filed | yes | `ns6:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 186 | GBP | 2020-08-31 | 2021-02-22 | filed | no | `ns6:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 8406 | GBP | 2020-08-31 | 2021-02-22 | filed | yes | `ns6:ProfitLoss` | total-exemption-full |
| total_assets_less_current_liabilities | 1182 | GBP | 2020-08-31 | 2022-03-01 | filed | yes | `ns6:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1182 | GBP | 2020-08-31 | 2021-02-22 | filed | no | `ns6:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2019-08-31 | 2020-02-20 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2019-08-31 | 2021-02-22 | filed | yes | `ns6:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 0 | GBP | 2019-08-31 | 2021-02-22 | filed | yes | `ns6:CashBankOnHand` | total-exemption-full |
| cash | 0 | GBP | 2019-08-31 | 2020-02-20 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 22955 | GBP | 2019-08-31 | 2021-02-22 | filed | yes | `ns6:CurrentAssets` | total-exemption-full |
| current_assets | 22955 | GBP | 2019-08-31 | 2020-02-20 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 22955 | GBP | 2019-08-31 | 2020-02-20 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 22955 | GBP | 2019-08-31 | 2021-02-22 | filed | yes | `ns6:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2019-08-31 | 2020-02-20 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2019-08-31 | 2021-02-22 | filed | yes | `ns6:Equity` | total-exemption-full |
| equity | 9176 | GBP | 2019-08-31 | 2020-02-20 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 8176 | GBP | 2019-08-31 | 2020-02-20 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 8176 | GBP | 2019-08-31 | 2021-02-22 | filed | yes | `ns6:Equity` | total-exemption-full |
| equity | 9176 | GBP | 2019-08-31 | 2021-02-22 | filed | yes | `ns6:Equity` | total-exemption-full |
| net_current_assets | 7848 | GBP | 2019-08-31 | 2021-02-22 | filed | yes | `ns6:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 7848 | GBP | 2019-08-31 | 2020-02-20 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 30593 | GBP | 2019-08-31 | 2020-02-20 | filed | yes | `ns5:ProfitLoss` | total-exemption-full |
| total_assets_less_current_liabilities | 9176 | GBP | 2019-08-31 | 2020-02-20 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 9176 | GBP | 2019-08-31 | 2021-02-22 | filed | yes | `ns6:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2018-08-31 | 2020-02-20 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 2505 | GBP | 2018-08-31 | 2020-02-20 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 22675 | GBP | 2018-08-31 | 2020-02-20 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 20170 | GBP | 2018-08-31 | 2020-02-20 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 9183 | GBP | 2018-08-31 | 2020-02-20 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1000 | GBP | 2018-08-31 | 2020-02-20 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 8183 | GBP | 2018-08-31 | 2020-02-20 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_current_assets | 7412 | GBP | 2018-08-31 | 2020-02-20 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 9183 | GBP | 2018-08-31 | 2020-02-20 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## MALLARD DESIGN LIMITED (`gb:05699807`)

- registration: `05699807` (GB), status active, incorporated 2006-02-06
- classification: ['71129'] (sic_2007)
- records: 4 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 57 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2026-01-31 | 2026-10-12 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 25613 | GBP | 2026-01-31 | 2026-10-12 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| equity | 2765 | GBP | 2026-01-31 | 2026-10-12 | filed | yes | `frs-core:Equity` | micro-entity |
| fixed_assets | 103 | GBP | 2026-01-31 | 2026-10-12 | filed | yes | `frs-core:FixedAssets` | micro-entity |
| net_assets | 2765 | GBP | 2026-01-31 | 2026-10-12 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 3417 | GBP | 2026-01-31 | 2026-10-12 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 3520 | GBP | 2026-01-31 | 2026-10-12 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2025-01-31 | 2026-10-12 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2025-01-31 | 2025-09-12 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 19052 | GBP | 2025-01-31 | 2026-10-12 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| current_assets | 19052 | GBP | 2025-01-31 | 2025-09-12 | filed | no | `frs-core:CurrentAssets` | micro-entity |
| equity | 615 | GBP | 2025-01-31 | 2026-10-12 | filed | yes | `frs-core:Equity` | micro-entity |
| equity | 615 | GBP | 2025-01-31 | 2025-09-12 | filed | no | `frs-core:Equity` | micro-entity |
| fixed_assets | 128 | GBP | 2025-01-31 | 2026-10-12 | filed | yes | `frs-core:FixedAssets` | micro-entity |
| fixed_assets | 128 | GBP | 2025-01-31 | 2025-09-12 | filed | no | `frs-core:FixedAssets` | micro-entity |
| net_assets | 615 | GBP | 2025-01-31 | 2026-10-12 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 615 | GBP | 2025-01-31 | 2025-09-12 | filed | no | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 1183 | GBP | 2025-01-31 | 2026-10-12 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 1183 | GBP | 2025-01-31 | 2025-09-12 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 1311 | GBP | 2025-01-31 | 2026-10-12 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 1311 | GBP | 2025-01-31 | 2025-09-12 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-01-31 | 2024-10-28 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-01-31 | 2025-09-12 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 24083 | GBP | 2024-01-31 | 2025-09-12 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| current_assets | 24083 | GBP | 2024-01-31 | 2024-10-28 | filed | no | `frs-core:CurrentAssets` | micro-entity |
| equity | 1310 | GBP | 2024-01-31 | 2024-10-28 | filed | no | `frs-core:Equity` | micro-entity |
| equity | 1310 | GBP | 2024-01-31 | 2025-09-12 | filed | yes | `frs-core:Equity` | micro-entity |
| fixed_assets | 153 | GBP | 2024-01-31 | 2024-10-28 | filed | no | `frs-core:FixedAssets` | micro-entity |
| fixed_assets | 153 | GBP | 2024-01-31 | 2025-09-12 | filed | yes | `frs-core:FixedAssets` | micro-entity |
| net_assets | 1310 | GBP | 2024-01-31 | 2025-09-12 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 1310 | GBP | 2024-01-31 | 2024-10-28 | filed | no | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 1799 | GBP | 2024-01-31 | 2025-09-12 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 1799 | GBP | 2024-01-31 | 2024-10-28 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 1952 | GBP | 2024-01-31 | 2025-09-12 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 1952 | GBP | 2024-01-31 | 2024-10-28 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2023-01-31 | 2024-10-28 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 21575 | GBP | 2023-01-31 | 2024-10-28 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| equity | -260 | GBP | 2023-01-31 | 2024-10-28 | filed | yes | `frs-core:Equity` | micro-entity |
| fixed_assets | 184 | GBP | 2023-01-31 | 2024-10-28 | filed | yes | `frs-core:FixedAssets` | micro-entity |
| net_assets | -260 | GBP | 2023-01-31 | 2024-10-28 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 161 | GBP | 2023-01-31 | 2024-10-28 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 345 | GBP | 2023-01-31 | 2024-10-28 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._
