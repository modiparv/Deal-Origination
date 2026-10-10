# Ingest spot-check

- database: `data/engine.db`
- latest run: `20261010T081107Z-099fab5f`
- companies in store: 23400; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## DORSET SOFTWARE SERVICES LIMITED (`gb:02150469`)

- registration: `02150469` (GB), status active, incorporated 1987-07-27
- classification: ['62012'] (sic_2007)
- records: 8 officers, 1 beneficial owners, 0 ownership statements, 2 security interests, 126 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1.48 | xbrli:pure | 2025-02-28 | 2025-11-25 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | small |
| cash | 4121737 | GBP | 2025-02-28 | 2025-11-25 | filed | yes | `core:CashBankOnHand` | small |
| current_assets | 5461356 | GBP | 2025-02-28 | 2025-11-25 | filed | yes | `core:CurrentAssets` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1339619 | GBP | 2025-02-28 | 2025-11-25 | filed | yes | `core:Debtors` | small |
| debtors | 1339619 | GBP | 2025-02-28 | 2025-11-25 | filed | yes | `core:Debtors` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-02-28 | 2025-11-25 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 100 | GBP | 2025-02-28 | 2025-11-25 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3897512 | GBP | 2025-02-28 | 2025-11-25 | filed | yes | `core:Equity` | small |
| equity | 3897612 | GBP | 2025-02-28 | 2025-11-25 | filed | yes | `core:Equity` | small |
| fixed_assets | 209149 | GBP | 2025-02-28 | 2025-11-25 | filed | yes | `core:FixedAssets` | small |
| net_assets | 3897612 | GBP | 2025-02-28 | 2025-11-25 | filed | yes | `core:NetAssetsLiabilities` | small |
| net_current_assets | 3740884 | GBP | 2025-02-28 | 2025-11-25 | filed | yes | `core:NetCurrentAssetsLiabilities` | small |
| total_assets_less_current_liabilities | 3950033 | GBP | 2025-02-28 | 2025-11-25 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | small |
| average_employees | 1.3800000000000001 | xbrli:pure | 2024-02-29 | 2025-11-25 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | small |
| average_employees | 138 | xbrli:pure | 2024-02-29 | 2024-11-28 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | small |
| cash | 2720629 | GBP | 2024-02-29 | 2025-11-25 | filed | yes | `core:CashBankOnHand` | small |
| cash | 2720629 | GBP | 2024-02-29 | 2024-11-28 | filed | no | `core:CashBankOnHand` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1147225 | GBP | 2024-02-29 | 2024-11-28 | filed | yes | `core:Creditors` | small |
| current_assets | 3702752 | GBP | 2024-02-29 | 2024-11-28 | filed | no | `core:CurrentAssets` | small |
| current_assets | 3702752 | GBP | 2024-02-29 | 2025-11-25 | filed | yes | `core:CurrentAssets` | small |
| debtors | 982123 | GBP | 2024-02-29 | 2024-11-28 | filed | no | `core:Debtors` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 982123 | GBP | 2024-02-29 | 2024-11-28 | filed | no | `core:Debtors` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 982123 | GBP | 2024-02-29 | 2025-11-25 | filed | yes | `core:Debtors` | small |
| debtors | 982123 | GBP | 2024-02-29 | 2025-11-25 | filed | yes | `core:Debtors` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-02-29 | 2024-11-28 | filed | no | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 100 | GBP | 2024-02-29 | 2025-11-25 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-02-29 | 2025-11-25 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2792920 | GBP | 2024-02-29 | 2025-11-25 | filed | yes | `core:Equity` | small |
| equity | 2793020 | GBP | 2024-02-29 | 2025-11-25 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2792920 | GBP | 2024-02-29 | 2024-11-28 | filed | no | `core:Equity` | small |
| equity | 2793020 | GBP | 2024-02-29 | 2024-11-28 | filed | no | `core:Equity` | small |
| fixed_assets | 316889 | GBP | 2024-02-29 | 2025-11-25 | filed | yes | `core:FixedAssets` | small |
| fixed_assets | 316889 | GBP | 2024-02-29 | 2024-11-28 | filed | no | `core:FixedAssets` | small |
| net_assets | 2793020 | GBP | 2024-02-29 | 2024-11-28 | filed | no | `core:NetAssetsLiabilities` | small |
| net_assets | 2793020 | GBP | 2024-02-29 | 2025-11-25 | filed | yes | `core:NetAssetsLiabilities` | small |
| net_current_assets | 2555527 | GBP | 2024-02-29 | 2025-11-25 | filed | yes | `core:NetCurrentAssetsLiabilities` | small |
| net_current_assets | 2555527 | GBP | 2024-02-29 | 2024-11-28 | filed | no | `core:NetCurrentAssetsLiabilities` | small |
| total_assets_less_current_liabilities | 2872416 | GBP | 2024-02-29 | 2024-11-28 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | small |
| total_assets_less_current_liabilities | 2872416 | GBP | 2024-02-29 | 2025-11-25 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | small |
| average_employees | 119 | xbrli:pure | 2023-02-28 | 2023-11-30 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | small |
| average_employees | 119 | xbrli:pure | 2023-02-28 | 2024-11-28 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | small |
| cash | 2790670 | GBP | 2023-02-28 | 2023-11-30 | filed | no | `core:CashBankOnHand` | small |
| cash | 2790670 | GBP | 2023-02-28 | 2024-11-28 | filed | yes | `core:CashBankOnHand` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1256377 | GBP | 2023-02-28 | 2023-11-30 | filed | no | `core:Creditors` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1256377 | GBP | 2023-02-28 | 2024-11-28 | filed | yes | `core:Creditors` | small |
| current_assets | 3473192 | GBP | 2023-02-28 | 2023-11-30 | filed | no | `core:CurrentAssets` | small |
| current_assets | 3473192 | GBP | 2023-02-28 | 2024-11-28 | filed | yes | `core:CurrentAssets` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 682522 | GBP | 2023-02-28 | 2024-11-28 | filed | yes | `core:Debtors` | small |
| debtors | 682522 | GBP | 2023-02-28 | 2024-11-28 | filed | yes | `core:Debtors` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 682522 | GBP | 2023-02-28 | 2023-11-30 | filed | no | `core:Debtors` | small |
| debtors | 682522 | GBP | 2023-02-28 | 2023-11-30 | filed | no | `core:Debtors` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2508790 | GBP | 2023-02-28 | 2023-11-30 | filed | no | `core:Equity` | small |
| equity | 2508890 | GBP | 2023-02-28 | 2024-11-28 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-02-28 | 2023-11-30 | filed | no | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2508790 | GBP | 2023-02-28 | 2024-11-28 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-02-28 | 2024-11-28 | filed | yes | `core:Equity` | small |
| equity | 2508890 | GBP | 2023-02-28 | 2023-11-30 | filed | no | `core:Equity` | small |
| fixed_assets | 387836 | GBP | 2023-02-28 | 2023-11-30 | filed | no | `core:FixedAssets` | small |
| fixed_assets | 387836 | GBP | 2023-02-28 | 2024-11-28 | filed | yes | `core:FixedAssets` | small |
| net_assets | 2508890 | GBP | 2023-02-28 | 2024-11-28 | filed | yes | `core:NetAssetsLiabilities` | small |
| net_assets | 2508890 | GBP | 2023-02-28 | 2023-11-30 | filed | no | `core:NetAssetsLiabilities` | small |
| net_current_assets | 2216815 | GBP | 2023-02-28 | 2023-11-30 | filed | no | `core:NetCurrentAssetsLiabilities` | small |
| net_current_assets | 2216815 | GBP | 2023-02-28 | 2024-11-28 | filed | yes | `core:NetCurrentAssetsLiabilities` | small |
| total_assets_less_current_liabilities | 2604651 | GBP | 2023-02-28 | 2024-11-28 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | small |
| total_assets_less_current_liabilities | 2604651 | GBP | 2023-02-28 | 2023-11-30 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | small |
| average_employees | 101 | xbrli:pure | 2022-02-28 | 2023-11-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | small |
| cash | 2397707 | GBP | 2022-02-28 | 2023-11-30 | filed | yes | `core:CashBankOnHand` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1193090 | GBP | 2022-02-28 | 2023-11-30 | filed | yes | `core:Creditors` | small |
| current_assets | 2914475 | GBP | 2022-02-28 | 2023-11-30 | filed | yes | `core:CurrentAssets` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 516768 | GBP | 2022-02-28 | 2023-11-30 | filed | yes | `core:Debtors` | small |
| debtors | 516768 | GBP | 2022-02-28 | 2023-11-30 | filed | yes | `core:Debtors` | small |
| equity | 2003045 | GBP | 2022-02-28 | 2023-11-30 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2022-02-28 | 2023-11-30 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2002945 | GBP | 2022-02-28 | 2023-11-30 | filed | yes | `core:Equity` | small |
| fixed_assets | 345752 | GBP | 2022-02-28 | 2023-11-30 | filed | yes | `core:FixedAssets` | small |
| net_assets | 2003045 | GBP | 2022-02-28 | 2023-11-30 | filed | yes | `core:NetAssetsLiabilities` | small |
| net_current_assets | 1721385 | GBP | 2022-02-28 | 2023-11-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | small |
| total_assets_less_current_liabilities | 2067137 | GBP | 2022-02-28 | 2023-11-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | small |

_No coverage facts for the latest run._

- event restatement @ 2025-11-25: `{"superseded_document_id": "gb:02150469:doc:b0b0jzr_lWmXLE6UybR57d-wtMWUoUHL0ZyN4OIw5LA", "restatements": [{"concept": "average_employees", "period_end": "2024-02-29", "old_value": "138.0000", "new_va`

## NU NETWORK PRODUCTS LIMITED (`gb:02716629`)

- registration: `02716629` (GB), status active, incorporated 1992-05-20
- classification: ['62020'] (sic_2007)
- records: 12 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 101 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-07-31 | 2026-04-24 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 2027682 | GBP | 2025-07-31 | 2026-04-24 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 2304790 | GBP | 2025-07-31 | 2026-04-24 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 277108 | GBP | 2025-07-31 | 2026-04-24 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 277108 | GBP | 2025-07-31 | 2026-04-24 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 1800969 | GBP | 2025-07-31 | 2026-04-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1790899 | GBP | 2025-07-31 | 2026-04-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 72 | GBP | 2025-07-31 | 2026-04-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 9970 | GBP | 2025-07-31 | 2026-04-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 28 | GBP | 2025-07-31 | 2026-04-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 1800969 | GBP | 2025-07-31 | 2026-04-24 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1800102 | GBP | 2025-07-31 | 2026-04-24 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1801258 | GBP | 2025-07-31 | 2026-04-24 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-07-31 | 2026-04-24 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-07-31 | 2025-04-22 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 1434138 | GBP | 2024-07-31 | 2026-04-24 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 1434138 | GBP | 2024-07-31 | 2025-04-22 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 1732917 | GBP | 2024-07-31 | 2026-04-24 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 1732917 | GBP | 2024-07-31 | 2025-04-22 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 298779 | GBP | 2024-07-31 | 2026-04-24 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 298779 | GBP | 2024-07-31 | 2025-04-22 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 298779 | GBP | 2024-07-31 | 2025-04-22 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 298779 | GBP | 2024-07-31 | 2026-04-24 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 9970 | GBP | 2024-07-31 | 2025-04-22 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 28 | GBP | 2024-07-31 | 2026-04-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 28 | GBP | 2024-07-31 | 2025-04-22 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1199481 | GBP | 2024-07-31 | 2026-04-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 1209551 | GBP | 2024-07-31 | 2026-04-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 9970 | GBP | 2024-07-31 | 2026-04-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1199481 | GBP | 2024-07-31 | 2025-04-22 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 72 | GBP | 2024-07-31 | 2025-04-22 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 1209551 | GBP | 2024-07-31 | 2025-04-22 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 72 | GBP | 2024-07-31 | 2026-04-24 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 1209551 | GBP | 2024-07-31 | 2025-04-22 | filed | no | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 1209551 | GBP | 2024-07-31 | 2026-04-24 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1208343 | GBP | 2024-07-31 | 2026-04-24 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1208343 | GBP | 2024-07-31 | 2025-04-22 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1209849 | GBP | 2024-07-31 | 2025-04-22 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1209849 | GBP | 2024-07-31 | 2026-04-24 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-07-31 | 2025-04-22 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-07-31 | 2024-04-26 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 2863063 | GBP | 2023-07-31 | 2024-04-26 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 2863063 | GBP | 2023-07-31 | 2025-04-22 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 3157789 | GBP | 2023-07-31 | 2025-04-22 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 3157789 | GBP | 2023-07-31 | 2024-04-26 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 294726 | GBP | 2023-07-31 | 2025-04-22 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 294726 | GBP | 2023-07-31 | 2024-04-26 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 294726 | GBP | 2023-07-31 | 2025-04-22 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 294726 | GBP | 2023-07-31 | 2024-04-26 | filed | no | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 72 | GBP | 2023-07-31 | 2025-04-22 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 28 | GBP | 2023-07-31 | 2025-04-22 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2662516 | GBP | 2023-07-31 | 2024-04-26 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 72 | GBP | 2023-07-31 | 2024-04-26 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2662516 | GBP | 2023-07-31 | 2025-04-22 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 9970 | GBP | 2023-07-31 | 2024-04-26 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 2672586 | GBP | 2023-07-31 | 2024-04-26 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 28 | GBP | 2023-07-31 | 2024-04-26 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 9970 | GBP | 2023-07-31 | 2025-04-22 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 2672586 | GBP | 2023-07-31 | 2025-04-22 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 2672586 | GBP | 2023-07-31 | 2024-04-26 | filed | no | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 2672586 | GBP | 2023-07-31 | 2025-04-22 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 2672438 | GBP | 2023-07-31 | 2025-04-22 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 2672438 | GBP | 2023-07-31 | 2024-04-26 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 2672970 | GBP | 2023-07-31 | 2025-04-22 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 2672970 | GBP | 2023-07-31 | 2024-04-26 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2022-07-31 | 2024-04-26 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 2573568 | GBP | 2022-07-31 | 2024-04-26 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 2907273 | GBP | 2022-07-31 | 2024-04-26 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 333705 | GBP | 2022-07-31 | 2024-04-26 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 333705 | GBP | 2022-07-31 | 2024-04-26 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 2340731 | GBP | 2022-07-31 | 2024-04-26 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 9970 | GBP | 2022-07-31 | 2024-04-26 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 72 | GBP | 2022-07-31 | 2024-04-26 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 28 | GBP | 2022-07-31 | 2024-04-26 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2330661 | GBP | 2022-07-31 | 2024-04-26 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 2340731 | GBP | 2022-07-31 | 2024-04-26 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 2339248 | GBP | 2022-07-31 | 2024-04-26 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 2340969 | GBP | 2022-07-31 | 2024-04-26 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## IDYLLIC PROPERTIES LIMITED (`gb:03088733`)

- registration: `03088733` (GB), status active, incorporated 1995-08-08
- classification: ['55209', '68100', '71111'] (sic_2007)
- records: 3 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 75 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | xbrli:pure | 2025-09-30 | 2026-08-12 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 10248 | GBP | 2025-09-30 | 2026-08-12 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 581088 | GBP | 2025-09-30 | 2026-08-12 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 48248 | GBP | 2025-09-30 | 2026-08-12 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 38000 | GBP | 2025-09-30 | 2026-08-12 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 100 | GBP | 2025-09-30 | 2026-08-12 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 294971 | GBP | 2025-09-30 | 2026-08-12 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-09-30 | 2026-08-12 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 294871 | GBP | 2025-09-30 | 2026-08-12 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 294971 | GBP | 2025-09-30 | 2026-08-12 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -532840 | GBP | 2025-09-30 | 2026-08-12 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 348569 | GBP | 2025-09-30 | 2026-08-12 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0 | xbrli:pure | 2024-09-30 | 2026-08-12 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 0 | xbrli:pure | 2024-09-30 | 2025-07-28 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 9225 | GBP | 2024-09-30 | 2026-08-12 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 8658 | GBP | 2024-09-30 | 2025-07-28 | filed | no | `core:CashBankOnHand` | unaudited-abridged |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 462574 | GBP | 2024-09-30 | 2026-08-12 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 610974 | GBP | 2024-09-30 | 2025-07-28 | filed | yes | `core:Creditors` | unaudited-abridged |
| current_assets | 61225 | GBP | 2024-09-30 | 2026-08-12 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 63158 | GBP | 2024-09-30 | 2025-07-28 | filed | no | `core:CurrentAssets` | unaudited-abridged |
| debtors | 54500 | GBP | 2024-09-30 | 2025-07-28 | filed | no | `core:Debtors` | unaudited-abridged |
| debtors | 52000 | GBP | 2024-09-30 | 2026-08-12 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 100 | GBP | 2024-09-30 | 2026-08-12 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-09-30 | 2026-08-12 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 282655 | GBP | 2024-09-30 | 2025-07-28 | filed | no | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 294242 | GBP | 2024-09-30 | 2026-08-12 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 294342 | GBP | 2024-09-30 | 2026-08-12 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 282755 | GBP | 2024-09-30 | 2025-07-28 | filed | no | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-09-30 | 2025-07-28 | filed | no | `core:Equity` | unaudited-abridged |
| fixed_assets | 881489 | GBP | 2024-09-30 | 2025-07-28 | filed | yes | `core:FixedAssets` | unaudited-abridged |
| net_assets | 294342 | GBP | 2024-09-30 | 2026-08-12 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 282755 | GBP | 2024-09-30 | 2025-07-28 | filed | no | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | -401349 | GBP | 2024-09-30 | 2026-08-12 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -547816 | GBP | 2024-09-30 | 2025-07-28 | filed | no | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 347940 | GBP | 2024-09-30 | 2026-08-12 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 333673 | GBP | 2024-09-30 | 2025-07-28 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 0 | xbrli:pure | 2023-09-30 | 2025-07-28 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 466346 | GBP | 2023-09-30 | 2025-07-28 | filed | yes | `core:Creditors` | unaudited-abridged |
| current_assets | 54500 | GBP | 2023-09-30 | 2025-07-28 | filed | yes | `core:CurrentAssets` | unaudited-abridged |
| debtors | 54500 | GBP | 2023-09-30 | 2025-07-28 | filed | yes | `core:Debtors` | unaudited-abridged |
| equity | 282326 | GBP | 2023-09-30 | 2025-07-28 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-09-30 | 2025-07-28 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 282226 | GBP | 2023-09-30 | 2025-07-28 | filed | yes | `core:Equity` | unaudited-abridged |
| fixed_assets | 745090 | GBP | 2023-09-30 | 2025-07-28 | filed | yes | `core:FixedAssets` | unaudited-abridged |
| net_assets | 282326 | GBP | 2023-09-30 | 2025-07-28 | filed | yes | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | -411846 | GBP | 2023-09-30 | 2025-07-28 | filed | yes | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 333244 | GBP | 2023-09-30 | 2025-07-28 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |

_No coverage facts for the latest run._

- event restatement @ 2026-08-12: `{"superseded_document_id": "gb:03088733:doc:lGBWFBtrWYH1rmZILu7yMSBuj3fq74V6z7fAhc8nqE8", "restatements": [{"concept": "debtors", "period_end": "2024-09-30", "old_value": "54500.0000", "new_value": "5`

## GLENDENE I.T. LIMITED (`gb:03383189`)

- registration: `03383189` (GB), status active, incorporated 1997-06-06
- classification: ['62020', '62090', '63110'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 69 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2026-06-30 | 2026-08-06 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 33164 | GBP | 2026-06-30 | 2026-08-06 | filed | yes | `ns5:CashBankOnHand` | unaudited-abridged |
| current_assets | 33205 | GBP | 2026-06-30 | 2026-08-06 | filed | yes | `ns5:CurrentAssets` | unaudited-abridged |
| debtors | 41 | GBP | 2026-06-30 | 2026-08-06 | filed | yes | `ns5:Debtors` | unaudited-abridged |
| equity | 33205 | GBP | 2026-06-30 | 2026-08-06 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10 | GBP | 2026-06-30 | 2026-08-06 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 33195 | GBP | 2026-06-30 | 2026-08-06 | filed | yes | `ns5:Equity` | unaudited-abridged |
| net_current_assets | 33205 | GBP | 2026-06-30 | 2026-08-06 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 33205 | GBP | 2026-06-30 | 2026-08-06 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 1 | xbrli:pure | 2025-06-30 | 2026-08-06 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| average_employees | 1 | xbrli:pure | 2025-06-30 | 2025-09-27 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 109857 | GBP | 2025-06-30 | 2026-08-06 | filed | yes | `ns5:CashBankOnHand` | unaudited-abridged |
| cash | 109857 | GBP | 2025-06-30 | 2025-09-27 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 110732 | GBP | 2025-06-30 | 2026-08-06 | filed | yes | `ns5:CurrentAssets` | unaudited-abridged |
| current_assets | 110732 | GBP | 2025-06-30 | 2025-09-27 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 875 | GBP | 2025-06-30 | 2026-08-06 | filed | yes | `ns5:Debtors` | unaudited-abridged |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 875 | GBP | 2025-06-30 | 2025-09-27 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 875 | GBP | 2025-06-30 | 2025-09-27 | filed | no | `ns5:Debtors` | total-exemption-full |
| equity | 98625 | GBP | 2025-06-30 | 2025-09-27 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 98615 | GBP | 2025-06-30 | 2025-09-27 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 98615 | GBP | 2025-06-30 | 2026-08-06 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity | 98625 | GBP | 2025-06-30 | 2026-08-06 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10 | GBP | 2025-06-30 | 2025-09-27 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'FurtherSpecificReserve3ComponentTotalEquity'}` | 0 | GBP | 2025-06-30 | 2025-09-27 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10 | GBP | 2025-06-30 | 2026-08-06 | filed | yes | `ns5:Equity` | unaudited-abridged |
| net_assets | 98625 | GBP | 2025-06-30 | 2025-09-27 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 98625 | GBP | 2025-06-30 | 2025-09-27 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 98625 | GBP | 2025-06-30 | 2026-08-06 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 98625 | GBP | 2025-06-30 | 2025-09-27 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 98625 | GBP | 2025-06-30 | 2026-08-06 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 1 | xbrli:pure | 2024-06-30 | 2024-08-27 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| average_employees | 1 | xbrli:pure | 2024-06-30 | 2025-09-27 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 49779 | GBP | 2024-06-30 | 2024-08-27 | filed | no | `ns5:CashBankOnHand` | unaudited-abridged |
| cash | 49779 | GBP | 2024-06-30 | 2025-09-27 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 156309 | GBP | 2024-06-30 | 2025-09-27 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 156309 | GBP | 2024-06-30 | 2024-08-27 | filed | no | `ns5:CurrentAssets` | unaudited-abridged |
| debtors | 37 | GBP | 2024-06-30 | 2025-09-27 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 37 | GBP | 2024-06-30 | 2024-08-27 | filed | no | `ns5:Debtors` | unaudited-abridged |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 37 | GBP | 2024-06-30 | 2025-09-27 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10 | GBP | 2024-06-30 | 2025-09-27 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 58604 | GBP | 2024-06-30 | 2024-08-27 | filed | no | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 58604 | GBP | 2024-06-30 | 2025-09-27 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'FurtherSpecificReserve3ComponentTotalEquity'}` | 49869 | GBP | 2024-06-30 | 2025-09-27 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'FurtherSpecificReserve3ComponentTotalEquity'}` | 49869 | GBP | 2024-06-30 | 2024-08-27 | filed | no | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10 | GBP | 2024-06-30 | 2024-08-27 | filed | no | `ns5:Equity` | unaudited-abridged |
| equity | 108483 | GBP | 2024-06-30 | 2024-08-27 | filed | no | `ns5:Equity` | unaudited-abridged |
| equity | 108483 | GBP | 2024-06-30 | 2025-09-27 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | 108483 | GBP | 2024-06-30 | 2024-08-27 | filed | no | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_assets | 108483 | GBP | 2024-06-30 | 2025-09-27 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 125106 | GBP | 2024-06-30 | 2025-09-27 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 125106 | GBP | 2024-06-30 | 2024-08-27 | filed | no | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 125106 | GBP | 2024-06-30 | 2024-08-27 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 125106 | GBP | 2024-06-30 | 2025-09-27 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-06-30 | 2024-08-27 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 60619 | GBP | 2023-06-30 | 2024-08-27 | filed | yes | `ns5:CashBankOnHand` | unaudited-abridged |
| current_assets | 157635 | GBP | 2023-06-30 | 2024-08-27 | filed | yes | `ns5:CurrentAssets` | unaudited-abridged |
| debtors | 47 | GBP | 2023-06-30 | 2024-08-27 | filed | yes | `ns5:Debtors` | unaudited-abridged |
| equity | 102190 | GBP | 2023-06-30 | 2024-08-27 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'FurtherSpecificReserve3ComponentTotalEquity'}` | 42727 | GBP | 2023-06-30 | 2024-08-27 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10 | GBP | 2023-06-30 | 2024-08-27 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 59453 | GBP | 2023-06-30 | 2024-08-27 | filed | yes | `ns5:Equity` | unaudited-abridged |
| net_assets | 102190 | GBP | 2023-06-30 | 2024-08-27 | filed | yes | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 116432 | GBP | 2023-06-30 | 2024-08-27 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 116432 | GBP | 2023-06-30 | 2024-08-27 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |

_No coverage facts for the latest run._

## SWIFTOOL PRECISION ENGINEERING LIMITED (`gb:03634212`)

- registration: `03634212` (GB), status active, incorporated 1998-09-17
- classification: ['25990', '71122'] (sic_2007)
- records: 5 officers, 3 beneficial owners, 0 ownership statements, 9 security interests, 101 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 125 | xbrli:pure | 2025-09-30 | 2026-06-29 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | medium |
| cash | 760 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `ns5:CashBankOnHand` | medium |
| current_assets | 10053901 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `ns5:CurrentAssets` | medium |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 5664839 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `ns5:Debtors` | medium |
| debtors | 5664839 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `ns5:Debtors` | medium |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `ns5:Equity` | medium |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 1148511 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `ns5:Equity` | medium |
| equity | 5573801 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `ns5:Equity` | medium |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 4425090 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `ns5:Equity` | medium |
| fixed_assets | 9619388 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `ns5:FixedAssets` | medium |
| gross_profit | 6276711 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `ns5:GrossProfitLoss` | medium |
| net_assets | 5573801 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `ns5:NetAssetsLiabilities` | medium |
| net_current_assets | 1935248 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | medium |
| operating_profit | 318 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `ns5:OperatingProfitLoss` | medium |
| profit_before_tax | -600512 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `ns5:ProfitLossOnOrdinaryActivitiesBeforeTax` | medium |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -136554 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `ns5:ProfitLoss` | medium |
| profit_for_period | -136554 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `ns5:ProfitLoss` | medium |
| revenue `{'GeographicSegmentsDimension': 'UnitedStates'}` | 13590 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `ns5:TurnoverRevenue` | medium |
| revenue | 15501128 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `ns5:TurnoverRevenue` | medium |
| revenue `{'GeographicSegmentsDimension': 'TotalGeographicSegmentsIncludingAnyUnallocatedAmount'}` | 15501128 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `ns5:TurnoverRevenue` | medium |
| revenue `{'GeographicSegmentsDimension': 'SouthAmerica'}` | 1188679 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `ns5:TurnoverRevenue` | medium |
| revenue `{'GeographicSegmentsDimension': 'Europe'}` | 648913 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `ns5:TurnoverRevenue` | medium |
| revenue `{'GeographicSegmentsDimension': 'Asia'}` | 477341 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `ns5:TurnoverRevenue` | medium |
| revenue `{'GeographicSegmentsDimension': 'UnitedKingdom'}` | 13048597 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `ns5:TurnoverRevenue` | medium |
| staff_costs | 5665918 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `ns5:StaffCostsEmployeeBenefitsExpense` | medium |
| tax_charge | -463958 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `ns5:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | medium |
| total_assets_less_current_liabilities | 11554636 | GBP | 2025-09-30 | 2026-06-29 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | medium |
| average_employees | 133 | xbrli:pure | 2024-09-30 | 2026-06-29 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | medium |
| average_employees | 133 | xbrli:pure | 2024-09-30 | 2025-05-23 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | medium |
| cash | 1728 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `ns5:CashBankOnHand` | medium |
| cash | 1728 | GBP | 2024-09-30 | 2025-05-23 | filed | no | `ns5:CashBankOnHand` | medium |
| current_assets | 18903522 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `ns5:CurrentAssets` | medium |
| current_assets | 18903522 | GBP | 2024-09-30 | 2025-05-23 | filed | no | `ns5:CurrentAssets` | medium |
| debtors | 12708859 | GBP | 2024-09-30 | 2025-05-23 | filed | no | `ns5:Debtors` | medium |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 12708859 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `ns5:Debtors` | medium |
| debtors | 12708859 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `ns5:Debtors` | medium |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 12708859 | GBP | 2024-09-30 | 2025-05-23 | filed | no | `ns5:Debtors` | medium |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 5211644 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `ns5:Equity` | medium |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `ns5:Equity` | medium |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 1148511 | GBP | 2024-09-30 | 2025-05-23 | filed | no | `ns5:Equity` | medium |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200 | GBP | 2024-09-30 | 2025-05-23 | filed | no | `ns5:Equity` | medium |
| equity | 6360355 | GBP | 2024-09-30 | 2025-05-23 | filed | no | `ns5:Equity` | medium |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 1148511 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `ns5:Equity` | medium |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 5211644 | GBP | 2024-09-30 | 2025-05-23 | filed | no | `ns5:Equity` | medium |
| equity | 6360355 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `ns5:Equity` | medium |
| fixed_assets | 10362918 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `ns5:FixedAssets` | medium |
| fixed_assets | 10362918 | GBP | 2024-09-30 | 2025-05-23 | filed | no | `ns5:FixedAssets` | medium |
| gross_profit | 9772633 | GBP | 2024-09-30 | 2025-05-23 | filed | no | `ns5:GrossProfitLoss` | medium |
| gross_profit | 9772633 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `ns5:GrossProfitLoss` | medium |
| net_assets | 6360355 | GBP | 2024-09-30 | 2025-05-23 | filed | no | `ns5:NetAssetsLiabilities` | medium |
| net_assets | 6360355 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `ns5:NetAssetsLiabilities` | medium |
| net_current_assets | 2323162 | GBP | 2024-09-30 | 2025-05-23 | filed | no | `ns5:NetCurrentAssetsLiabilities` | medium |
| net_current_assets | 2323162 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | medium |
| operating_profit | 3116402 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `ns5:OperatingProfitLoss` | medium |
| operating_profit | 3116402 | GBP | 2024-09-30 | 2025-05-23 | filed | no | `ns5:OperatingProfitLoss` | medium |
| profit_before_tax | 2284209 | GBP | 2024-09-30 | 2025-05-23 | filed | no | `ns5:ProfitLossOnOrdinaryActivitiesBeforeTax` | medium |
| profit_before_tax | 2284209 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `ns5:ProfitLossOnOrdinaryActivitiesBeforeTax` | medium |
| profit_for_period | 1761200 | GBP | 2024-09-30 | 2025-05-23 | filed | no | `ns5:ProfitLoss` | medium |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1761200 | GBP | 2024-09-30 | 2025-05-23 | filed | yes | `ns5:ProfitLoss` | medium |
| profit_for_period | 1761200 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `ns5:ProfitLoss` | medium |
| revenue `{'GeographicSegmentsDimension': 'Asia'}` | 490170 | GBP | 2024-09-30 | 2025-05-23 | filed | no | `ns5:TurnoverRevenue` | medium |
| revenue `{'GeographicSegmentsDimension': 'UnitedKingdom'}` | 25651914 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `ns5:TurnoverRevenue` | medium |
| revenue `{'GeographicSegmentsDimension': 'TotalGeographicSegmentsIncludingAnyUnallocatedAmount'}` | 27841152 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `ns5:TurnoverRevenue` | medium |
| revenue `{'GeographicSegmentsDimension': 'TotalGeographicSegmentsIncludingAnyUnallocatedAmount'}` | 27841152 | GBP | 2024-09-30 | 2025-05-23 | filed | no | `ns5:TurnoverRevenue` | medium |
| revenue | 27841152 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `ns5:TurnoverRevenue` | medium |
| revenue `{'GeographicSegmentsDimension': 'Asia'}` | 490170 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `ns5:TurnoverRevenue` | medium |
| revenue `{'GeographicSegmentsDimension': 'Europe'}` | 437494 | GBP | 2024-09-30 | 2025-05-23 | filed | no | `ns5:TurnoverRevenue` | medium |
| revenue | 27841152 | GBP | 2024-09-30 | 2025-05-23 | filed | no | `ns5:TurnoverRevenue` | medium |
| revenue `{'GeographicSegmentsDimension': 'SouthAmerica'}` | 973837 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `ns5:TurnoverRevenue` | medium |
| revenue `{'GeographicSegmentsDimension': 'SouthAmerica'}` | 973837 | GBP | 2024-09-30 | 2025-05-23 | filed | no | `ns5:TurnoverRevenue` | medium |
| revenue `{'GeographicSegmentsDimension': 'UnitedStates'}` | 175 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `ns5:TurnoverRevenue` | medium |
| revenue `{'GeographicSegmentsDimension': 'UnitedStates'}` | 175 | GBP | 2024-09-30 | 2025-05-23 | filed | no | `ns5:TurnoverRevenue` | medium |
| revenue `{'GeographicSegmentsDimension': 'Europe'}` | 437494 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `ns5:TurnoverRevenue` | medium |
| revenue `{'GeographicSegmentsDimension': 'UnitedKingdom'}` | 25651914 | GBP | 2024-09-30 | 2025-05-23 | filed | no | `ns5:TurnoverRevenue` | medium |
| staff_costs | 6212670 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `ns5:StaffCostsEmployeeBenefitsExpense` | medium |
| staff_costs | 6212670 | GBP | 2024-09-30 | 2025-05-23 | filed | no | `ns5:StaffCostsEmployeeBenefitsExpense` | medium |
| tax_charge | 523009 | GBP | 2024-09-30 | 2025-05-23 | filed | no | `ns5:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | medium |
| tax_charge | 523009 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `ns5:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | medium |
| total_assets_less_current_liabilities | 12686080 | GBP | 2024-09-30 | 2025-05-23 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | medium |
| total_assets_less_current_liabilities | 12686080 | GBP | 2024-09-30 | 2026-06-29 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | medium |
| average_employees | 115 | xbrli:pure | 2023-09-30 | 2025-05-23 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | medium |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 115 | xbrli:pure | 2023-09-30 | 2024-02-16 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | full |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 796 | GBP | 2023-09-30 | 2024-02-16 | filed | yes | `ns5:CashBankOnHand` | full |
| cash | 796 | GBP | 2023-09-30 | 2025-05-23 | filed | yes | `ns5:CashBankOnHand` | medium |
| current_assets | 14638120 | GBP | 2023-09-30 | 2025-05-23 | filed | yes | `ns5:CurrentAssets` | medium |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 14638120 | GBP | 2023-09-30 | 2024-02-16 | filed | yes | `ns5:CurrentAssets` | full |
| debtors `{'OriginalRevisedDataDimension': 'Original'}` | 9641092 | GBP | 2023-09-30 | 2024-02-16 | filed | yes | `ns5:Debtors` | full |
| debtors | 9641092 | GBP | 2023-09-30 | 2025-05-23 | filed | yes | `ns5:Debtors` | medium |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 9641092 | GBP | 2023-09-30 | 2025-05-23 | filed | yes | `ns5:Debtors` | medium |
| debtors `{'OriginalRevisedDataDimension': 'Original', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 9641092 | GBP | 2023-09-30 | 2024-02-16 | filed | yes | `ns5:Debtors` | full |
| equity | 5599155 | GBP | 2023-09-30 | 2025-05-23 | filed | no | `ns5:Equity` | medium |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 4450444 | GBP | 2023-09-30 | 2025-05-23 | filed | no | `ns5:Equity` | medium |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 200 | GBP | 2023-09-30 | 2024-02-16 | filed | yes | `ns5:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200 | GBP | 2023-09-30 | 2026-06-29 | filed | yes | `ns5:Equity` | medium |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 1148511 | GBP | 2023-09-30 | 2025-05-23 | filed | no | `ns5:Equity` | medium |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 5599155 | GBP | 2023-09-30 | 2024-02-16 | filed | yes | `ns5:Equity` | full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 4450444 | GBP | 2023-09-30 | 2024-02-16 | filed | yes | `ns5:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200 | GBP | 2023-09-30 | 2025-05-23 | filed | no | `ns5:Equity` | medium |
| equity | 5599155 | GBP | 2023-09-30 | 2026-06-29 | filed | yes | `ns5:Equity` | medium |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 1148511 | GBP | 2023-09-30 | 2026-06-29 | filed | yes | `ns5:Equity` | medium |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 4450444 | GBP | 2023-09-30 | 2026-06-29 | filed | yes | `ns5:Equity` | medium |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RevaluationReserve'}` | 1148511 | GBP | 2023-09-30 | 2024-02-16 | filed | yes | `ns5:Equity` | full |
| fixed_assets | 9552932 | GBP | 2023-09-30 | 2025-05-23 | filed | yes | `ns5:FixedAssets` | medium |
| fixed_assets `{'OriginalRevisedDataDimension': 'Original'}` | 9552932 | GBP | 2023-09-30 | 2024-02-16 | filed | yes | `ns5:FixedAssets` | full |
| gross_profit `{'OriginalRevisedDataDimension': 'Original'}` | 7725813 | GBP | 2023-09-30 | 2024-02-16 | filed | yes | `ns5:GrossProfitLoss` | full |
| gross_profit | 7725813 | GBP | 2023-09-30 | 2025-05-23 | filed | yes | `ns5:GrossProfitLoss` | medium |
| net_assets `{'OriginalRevisedDataDimension': 'Original'}` | 5599155 | GBP | 2023-09-30 | 2024-02-16 | filed | yes | `ns5:NetAssetsLiabilities` | full |
| net_assets | 5599155 | GBP | 2023-09-30 | 2025-05-23 | filed | yes | `ns5:NetAssetsLiabilities` | medium |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 1812871 | GBP | 2023-09-30 | 2024-02-16 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | full |
| net_current_assets | 1812871 | GBP | 2023-09-30 | 2025-05-23 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | medium |
| operating_profit `{'OriginalRevisedDataDimension': 'Original'}` | 2959676 | GBP | 2023-09-30 | 2024-02-16 | filed | yes | `ns5:OperatingProfitLoss` | full |
| operating_profit | 2436938 | GBP | 2023-09-30 | 2025-05-23 | filed | yes | `ns5:OperatingProfitLoss` | medium |
| profit_before_tax `{'OriginalRevisedDataDimension': 'Original'}` | 2422132 | GBP | 2023-09-30 | 2024-02-16 | filed | yes | `ns5:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_before_tax | 1899394 | GBP | 2023-09-30 | 2025-05-23 | filed | yes | `ns5:ProfitLossOnOrdinaryActivitiesBeforeTax` | medium |
| profit_for_period `{'OriginalRevisedDataDimension': 'Original'}` | 2133898 | GBP | 2023-09-30 | 2024-02-16 | filed | yes | `ns5:ProfitLoss` | full |
| profit_for_period `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2133898 | GBP | 2023-09-30 | 2024-02-16 | filed | yes | `ns5:ProfitLoss` | full |
| profit_for_period | 1611160 | GBP | 2023-09-30 | 2025-05-23 | filed | yes | `ns5:ProfitLoss` | medium |
| revenue `{'GeographicSegmentsDimension': 'Europe'}` | 412101 | GBP | 2023-09-30 | 2025-05-23 | filed | yes | `ns5:TurnoverRevenue` | medium |
| revenue | 21088949 | GBP | 2023-09-30 | 2025-05-23 | filed | yes | `ns5:TurnoverRevenue` | medium |
| revenue `{'GeographicSegmentsDimension': 'UnitedKingdom'}` | 18382025 | GBP | 2023-09-30 | 2025-05-23 | filed | yes | `ns5:TurnoverRevenue` | medium |
| revenue `{'OriginalRevisedDataDimension': 'Original', 'GeographicSegmentsDimension': 'UnitedKingdom'}` | 18382025 | GBP | 2023-09-30 | 2024-02-16 | filed | yes | `ns5:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'Asia'}` | 579664 | GBP | 2023-09-30 | 2025-05-23 | filed | yes | `ns5:TurnoverRevenue` | medium |
| revenue `{'GeographicSegmentsDimension': 'Europe', 'OriginalRevisedDataDimension': 'Original'}` | 412101 | GBP | 2023-09-30 | 2024-02-16 | filed | yes | `ns5:TurnoverRevenue` | full |
| revenue `{'OriginalRevisedDataDimension': 'Original', 'GeographicSegmentsDimension': 'TotalGeographicSegmentsIncludingAnyUnallocatedAmount'}` | 21088949 | GBP | 2023-09-30 | 2024-02-16 | filed | yes | `ns5:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'TotalGeographicSegmentsIncludingAnyUnallocatedAmount'}` | 21088949 | GBP | 2023-09-30 | 2025-05-23 | filed | yes | `ns5:TurnoverRevenue` | medium |
| revenue `{'GeographicSegmentsDimension': 'UnitedStates'}` | 10935 | GBP | 2023-09-30 | 2025-05-23 | filed | yes | `ns5:TurnoverRevenue` | medium |
| revenue `{'GeographicSegmentsDimension': 'UnitedStates', 'OriginalRevisedDataDimension': 'Original'}` | 10935 | GBP | 2023-09-30 | 2024-02-16 | filed | yes | `ns5:TurnoverRevenue` | full |
| revenue `{'OriginalRevisedDataDimension': 'Original', 'GeographicSegmentsDimension': 'Asia'}` | 579664 | GBP | 2023-09-30 | 2024-02-16 | filed | yes | `ns5:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'SouthAmerica', 'OriginalRevisedDataDimension': 'Original'}` | 1234323 | GBP | 2023-09-30 | 2024-02-16 | filed | yes | `ns5:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'SouthAmerica'}` | 1234323 | GBP | 2023-09-30 | 2025-05-23 | filed | yes | `ns5:TurnoverRevenue` | medium |
| revenue `{'OriginalRevisedDataDimension': 'Original'}` | 21088949 | GBP | 2023-09-30 | 2024-02-16 | filed | yes | `ns5:TurnoverRevenue` | full |
| staff_costs `{'OriginalRevisedDataDimension': 'Original'}` | 4890745 | GBP | 2023-09-30 | 2024-02-16 | filed | yes | `ns5:StaffCostsEmployeeBenefitsExpense` | full |
| staff_costs | 4890745 | GBP | 2023-09-30 | 2025-05-23 | filed | yes | `ns5:StaffCostsEmployeeBenefitsExpense` | medium |
| tax_charge `{'OriginalRevisedDataDimension': 'Original'}` | 288234 | GBP | 2023-09-30 | 2024-02-16 | filed | yes | `ns5:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| tax_charge | 288234 | GBP | 2023-09-30 | 2025-05-23 | filed | yes | `ns5:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | medium |
| total_assets_less_current_liabilities | 11365803 | GBP | 2023-09-30 | 2025-05-23 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | medium |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 11365803 | GBP | 2023-09-30 | 2024-02-16 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | full |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 120 | xbrli:pure | 2022-09-30 | 2024-02-16 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | full |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 62214 | GBP | 2022-09-30 | 2024-02-16 | filed | yes | `ns5:CashBankOnHand` | full |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 7492819 | GBP | 2022-09-30 | 2024-02-16 | filed | yes | `ns5:CurrentAssets` | full |
| debtors `{'OriginalRevisedDataDimension': 'Original', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 4178195 | GBP | 2022-09-30 | 2024-02-16 | filed | yes | `ns5:Debtors` | full |
| debtors `{'OriginalRevisedDataDimension': 'Original'}` | 4178195 | GBP | 2022-09-30 | 2024-02-16 | filed | yes | `ns5:Debtors` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3589284 | GBP | 2022-09-30 | 2025-05-23 | filed | yes | `ns5:Equity` | medium |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 625773 | GBP | 2022-09-30 | 2025-05-23 | filed | yes | `ns5:Equity` | medium |
| equity | 4215257 | GBP | 2022-09-30 | 2025-05-23 | filed | yes | `ns5:Equity` | medium |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 200 | GBP | 2022-09-30 | 2024-02-16 | filed | yes | `ns5:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200 | GBP | 2022-09-30 | 2025-05-23 | filed | yes | `ns5:Equity` | medium |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RevaluationReserve'}` | 625773 | GBP | 2022-09-30 | 2024-02-16 | filed | yes | `ns5:Equity` | full |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 4215257 | GBP | 2022-09-30 | 2024-02-16 | filed | yes | `ns5:Equity` | full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3589284 | GBP | 2022-09-30 | 2024-02-16 | filed | yes | `ns5:Equity` | full |
| fixed_assets `{'OriginalRevisedDataDimension': 'Original'}` | 8587338 | GBP | 2022-09-30 | 2024-02-16 | filed | yes | `ns5:FixedAssets` | full |
| gross_profit `{'OriginalRevisedDataDimension': 'Original'}` | 4948207 | GBP | 2022-09-30 | 2024-02-16 | filed | yes | `ns5:GrossProfitLoss` | full |
| net_assets `{'OriginalRevisedDataDimension': 'Original'}` | 4215257 | GBP | 2022-09-30 | 2024-02-16 | filed | yes | `ns5:NetAssetsLiabilities` | full |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 1363983 | GBP | 2022-09-30 | 2024-02-16 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | full |
| operating_profit `{'OriginalRevisedDataDimension': 'Original'}` | 455460 | GBP | 2022-09-30 | 2024-02-16 | filed | yes | `ns5:OperatingProfitLoss` | full |
| profit_before_tax `{'OriginalRevisedDataDimension': 'Original'}` | 186286 | GBP | 2022-09-30 | 2024-02-16 | filed | yes | `ns5:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period `{'OriginalRevisedDataDimension': 'Original'}` | 264676 | GBP | 2022-09-30 | 2024-02-16 | filed | yes | `ns5:ProfitLoss` | full |
| revenue `{'GeographicSegmentsDimension': 'UnitedStates', 'OriginalRevisedDataDimension': 'Original'}` | 29873 | GBP | 2022-09-30 | 2024-02-16 | filed | yes | `ns5:TurnoverRevenue` | full |
| revenue `{'OriginalRevisedDataDimension': 'Original', 'GeographicSegmentsDimension': 'TotalGeographicSegmentsIncludingAnyUnallocatedAmount'}` | 11666136 | GBP | 2022-09-30 | 2024-02-16 | filed | yes | `ns5:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'SouthAmerica', 'OriginalRevisedDataDimension': 'Original'}` | 924776 | GBP | 2022-09-30 | 2024-02-16 | filed | yes | `ns5:TurnoverRevenue` | full |
| revenue `{'OriginalRevisedDataDimension': 'Original', 'GeographicSegmentsDimension': 'Asia'}` | 125433 | GBP | 2022-09-30 | 2024-02-16 | filed | yes | `ns5:TurnoverRevenue` | full |
| revenue `{'OriginalRevisedDataDimension': 'Original', 'GeographicSegmentsDimension': 'UnitedKingdom'}` | 10161947 | GBP | 2022-09-30 | 2024-02-16 | filed | yes | `ns5:TurnoverRevenue` | full |
| revenue `{'OriginalRevisedDataDimension': 'Original'}` | 11666136 | GBP | 2022-09-30 | 2024-02-16 | filed | yes | `ns5:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'Europe', 'OriginalRevisedDataDimension': 'Original'}` | 336695 | GBP | 2022-09-30 | 2024-02-16 | filed | yes | `ns5:TurnoverRevenue` | full |
| staff_costs `{'OriginalRevisedDataDimension': 'Original'}` | 4515807 | GBP | 2022-09-30 | 2024-02-16 | filed | yes | `ns5:StaffCostsEmployeeBenefitsExpense` | full |
| tax_charge `{'OriginalRevisedDataDimension': 'Original'}` | -78390 | GBP | 2022-09-30 | 2024-02-16 | filed | yes | `ns5:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 9951321 | GBP | 2022-09-30 | 2024-02-16 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RevaluationReserve'}` | 531604 | GBP | 2021-09-30 | 2024-02-16 | filed | yes | `ns5:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 200 | GBP | 2021-09-30 | 2024-02-16 | filed | yes | `ns5:Equity` | full |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 4150581 | GBP | 2021-09-30 | 2024-02-16 | filed | yes | `ns5:Equity` | full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 3618777 | GBP | 2021-09-30 | 2024-02-16 | filed | yes | `ns5:Equity` | full |

_No coverage facts for the latest run._

## NETWORK22 LIMITED (`gb:03893806`)

- registration: `03893806` (GB), status active, incorporated 1999-12-14
- classification: ['62020'] (sic_2007)
- records: 8 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 85 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-12-31 | 2026-10-01 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 50691 | GBP | 2025-12-31 | 2026-10-01 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 49513 | GBP | 2025-12-31 | 2026-10-01 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 71545 | GBP | 2025-12-31 | 2026-10-01 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 3104 | GBP | 2025-12-31 | 2026-10-01 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 45597 | GBP | 2025-12-31 | 2026-10-01 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-12-31 | 2026-10-01 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 45497 | GBP | 2025-12-31 | 2026-10-01 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 45597 | GBP | 2025-12-31 | 2026-10-01 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 22032 | GBP | 2025-12-31 | 2026-10-01 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 48308 | GBP | 2025-12-31 | 2026-10-01 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-12-31 | 2026-10-01 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2024-12-31 | 2025-09-30 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 2869 | GBP | 2024-12-31 | 2026-10-01 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 2869 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 22592 | GBP | 2024-12-31 | 2026-10-01 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 22592 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 20795 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 20795 | GBP | 2024-12-31 | 2026-10-01 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 176 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 176 | GBP | 2024-12-31 | 2026-10-01 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-12-31 | 2026-10-01 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 15808 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 15808 | GBP | 2024-12-31 | 2026-10-01 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 15908 | GBP | 2024-12-31 | 2026-10-01 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 15908 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `core:Equity` | total-exemption-full |
| net_assets | 15908 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 15908 | GBP | 2024-12-31 | 2026-10-01 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -1797 | GBP | 2024-12-31 | 2026-10-01 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -1797 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 16837 | GBP | 2024-12-31 | 2026-10-01 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 16837 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-12-31 | 2024-12-31 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-12-31 | 2025-09-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 661 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 661 | GBP | 2023-12-31 | 2024-12-31 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 20463 | GBP | 2023-12-31 | 2024-12-31 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 20463 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 18526 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 18526 | GBP | 2023-12-31 | 2024-12-31 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors | 115 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 115 | GBP | 2023-12-31 | 2024-12-31 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 20964 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 20864 | GBP | 2023-12-31 | 2024-12-31 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 20864 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 20964 | GBP | 2023-12-31 | 2024-12-31 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-12-31 | 2024-12-31 | filed | no | `core:Equity` | total-exemption-full |
| net_assets | 20964 | GBP | 2023-12-31 | 2024-12-31 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 20964 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -1937 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -1937 | GBP | 2023-12-31 | 2024-12-31 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 22905 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 22905 | GBP | 2023-12-31 | 2024-12-31 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2022-12-31 | 2024-12-31 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 29580 | GBP | 2022-12-31 | 2024-12-31 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 30633 | GBP | 2022-12-31 | 2024-12-31 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 30633 | GBP | 2022-12-31 | 2024-12-31 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2022-12-31 | 2024-12-31 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 30739 | GBP | 2022-12-31 | 2024-12-31 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 30839 | GBP | 2022-12-31 | 2024-12-31 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 30839 | GBP | 2022-12-31 | 2024-12-31 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1053 | GBP | 2022-12-31 | 2024-12-31 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 34175 | GBP | 2022-12-31 | 2024-12-31 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## ACUITY SOFTWARE TECHNOLOGIES LIMITED (`gb:04151643`)

- registration: `04151643` (GB), status active, incorporated 2001-02-01
- classification: ['62012'] (sic_2007)
- records: 3 officers, 3 beneficial owners, 0 ownership statements, 2 security interests, 63 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.53 | xbrli:pure | 2025-03-31 | 2026-03-19 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 713067 | GBP | 2025-03-31 | 2026-03-19 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| current_assets | 1312082 | GBP | 2025-03-31 | 2026-03-19 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 599015 | GBP | 2025-03-31 | 2026-03-19 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 100 | GBP | 2025-03-31 | 2026-03-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1850843 | GBP | 2025-03-31 | 2026-03-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 1850943 | GBP | 2025-03-31 | 2026-03-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-03-31 | 2026-03-19 | filed | yes | `core:Equity` | total-exemption-full |
| net_current_assets | 666943 | GBP | 2025-03-31 | 2026-03-19 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1850943 | GBP | 2025-03-31 | 2026-03-19 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 46 | xbrli:pure | 2024-03-31 | 2025-03-31 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 0.46 | xbrli:pure | 2024-03-31 | 2026-03-19 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 439769 | GBP | 2024-03-31 | 2025-03-31 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 439769 | GBP | 2024-03-31 | 2026-03-19 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 645704 | GBP | 2024-03-31 | 2025-03-31 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 1253295 | GBP | 2024-03-31 | 2026-03-19 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 1253295 | GBP | 2024-03-31 | 2025-03-31 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors | 813526 | GBP | 2024-03-31 | 2026-03-19 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 813526 | GBP | 2024-03-31 | 2025-03-31 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 100 | GBP | 2024-03-31 | 2026-03-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 1791591 | GBP | 2024-03-31 | 2026-03-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-03-31 | 2025-03-31 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1791491 | GBP | 2024-03-31 | 2025-03-31 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1791491 | GBP | 2024-03-31 | 2026-03-19 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 1791591 | GBP | 2024-03-31 | 2025-03-31 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-03-31 | 2026-03-19 | filed | yes | `core:Equity` | total-exemption-full |
| net_current_assets | 607591 | GBP | 2024-03-31 | 2025-03-31 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 607591 | GBP | 2024-03-31 | 2026-03-19 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1791591 | GBP | 2024-03-31 | 2026-03-19 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1791591 | GBP | 2024-03-31 | 2025-03-31 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 44 | xbrli:pure | 2023-03-31 | 2025-03-31 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 44 | xbrli:pure | 2023-03-31 | 2023-12-21 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 185455 | GBP | 2023-03-31 | 2025-03-31 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 185455 | GBP | 2023-03-31 | 2023-12-21 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 555410 | GBP | 2023-03-31 | 2025-03-31 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 555410 | GBP | 2023-03-31 | 2023-12-21 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 1031793 | GBP | 2023-03-31 | 2023-12-21 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 1031793 | GBP | 2023-03-31 | 2025-03-31 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 846338 | GBP | 2023-03-31 | 2025-03-31 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 846338 | GBP | 2023-03-31 | 2023-12-21 | filed | no | `core:Debtors` | total-exemption-full |
| equity | 1660383 | GBP | 2023-03-31 | 2025-03-31 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1660283 | GBP | 2023-03-31 | 2023-12-21 | filed | no | `core:Equity` | total-exemption-full |
| equity | 1660383 | GBP | 2023-03-31 | 2023-12-21 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1660283 | GBP | 2023-03-31 | 2025-03-31 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-03-31 | 2023-12-21 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-03-31 | 2025-03-31 | filed | yes | `core:Equity` | total-exemption-full |
| net_current_assets | 476383 | GBP | 2023-03-31 | 2025-03-31 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 476383 | GBP | 2023-03-31 | 2023-12-21 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1660383 | GBP | 2023-03-31 | 2025-03-31 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1660383 | GBP | 2023-03-31 | 2023-12-21 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| cash | 129840 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 521509 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 899188 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 769348 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 1561679 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1561579 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `core:Equity` | total-exemption-full |
| net_current_assets | 377679 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1561679 | GBP | 2022-03-31 | 2023-12-21 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2026-03-19: `{"superseded_document_id": "gb:04151643:doc:osL3xxlcqYl_BV0Q1ufrZGKUZDOPSTjtnvi7rJQPKxU", "restatements": [{"concept": "average_employees", "period_end": "2024-03-31", "old_value": "46.0000", "new_val`

## ENGHOUSE DEVELOPMENT (UK) LIMITED (`gb:04485978`)

- registration: `04485978` (GB), status active, incorporated 2002-07-15
- classification: ['61900', '62090'] (sic_2007)
- records: 13 officers, 1 beneficial owners, 0 ownership statements, 1 security interests, 101 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | xbrli:pure | 2025-10-31 | 2026-07-31 | filed | yes | `c:AverageNumberEmployeesDuringPeriod` | small |
| cash | 614413 | GBP | 2025-10-31 | 2026-07-31 | filed | yes | `c:CashBankOnHand` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 4252557 | GBP | 2025-10-31 | 2026-07-31 | filed | yes | `c:Creditors` | small |
| current_assets | 5360627 | GBP | 2025-10-31 | 2026-07-31 | filed | yes | `c:CurrentAssets` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments'}` | 3400000 | GBP | 2025-10-31 | 2026-07-31 | filed | yes | `c:Debtors` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 1346214 | GBP | 2025-10-31 | 2026-07-31 | filed | yes | `c:Debtors` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1108069 | GBP | 2025-10-31 | 2026-07-31 | filed | yes | `c:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2025-10-31 | 2026-07-31 | filed | yes | `c:Equity` | small |
| equity | 1108070 | GBP | 2025-10-31 | 2026-07-31 | filed | yes | `c:Equity` | small |
| net_assets | 1108070 | GBP | 2025-10-31 | 2026-07-31 | filed | yes | `c:NetAssetsLiabilities` | small |
| net_current_assets | 1108070 | GBP | 2025-10-31 | 2026-07-31 | filed | yes | `c:NetCurrentAssetsLiabilities` | small |
| total_assets_less_current_liabilities | 1108070 | GBP | 2025-10-31 | 2026-07-31 | filed | yes | `c:TotalAssetsLessCurrentLiabilities` | small |
| average_employees | 0 | xbrli:pure | 2024-10-31 | 2025-07-28 | filed | no | `d:AverageNumberEmployeesDuringPeriod` | small |
| average_employees | 0 | xbrli:pure | 2024-10-31 | 2026-07-31 | filed | yes | `c:AverageNumberEmployeesDuringPeriod` | small |
| cash | 6450890 | GBP | 2024-10-31 | 2026-07-31 | filed | yes | `c:CashBankOnHand` | small |
| cash | 6450890 | GBP | 2024-10-31 | 2025-07-28 | filed | no | `d:CashBankOnHand` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 12053769 | GBP | 2024-10-31 | 2025-07-28 | filed | no | `d:Creditors` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 12053769 | GBP | 2024-10-31 | 2026-07-31 | filed | yes | `c:Creditors` | small |
| current_assets | 13853568 | GBP | 2024-10-31 | 2025-07-28 | filed | no | `d:CurrentAssets` | small |
| current_assets | 13853568 | GBP | 2024-10-31 | 2026-07-31 | filed | yes | `c:CurrentAssets` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments'}` | 0 | GBP | 2024-10-31 | 2026-07-31 | filed | yes | `c:Debtors` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 7402678 | GBP | 2024-10-31 | 2026-07-31 | filed | yes | `c:Debtors` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 7402678 | GBP | 2024-10-31 | 2025-07-28 | filed | no | `d:Debtors` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2024-10-31 | 2026-07-31 | filed | yes | `c:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2024-10-31 | 2025-07-28 | filed | no | `d:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1799798 | GBP | 2024-10-31 | 2025-07-28 | filed | no | `d:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1799798 | GBP | 2024-10-31 | 2026-07-31 | filed | yes | `c:Equity` | small |
| equity | 1799799 | GBP | 2024-10-31 | 2025-07-28 | filed | no | `d:Equity` | small |
| equity | 1799799 | GBP | 2024-10-31 | 2026-07-31 | filed | yes | `c:Equity` | small |
| net_assets | 1799799 | GBP | 2024-10-31 | 2026-07-31 | filed | yes | `c:NetAssetsLiabilities` | small |
| net_assets | 1799799 | GBP | 2024-10-31 | 2025-07-28 | filed | no | `d:NetAssetsLiabilities` | small |
| net_current_assets | 1799799 | GBP | 2024-10-31 | 2026-07-31 | filed | yes | `c:NetCurrentAssetsLiabilities` | small |
| net_current_assets | 1799799 | GBP | 2024-10-31 | 2025-07-28 | filed | no | `d:NetCurrentAssetsLiabilities` | small |
| total_assets_less_current_liabilities | 1799799 | GBP | 2024-10-31 | 2025-07-28 | filed | no | `d:TotalAssetsLessCurrentLiabilities` | small |
| total_assets_less_current_liabilities | 1799799 | GBP | 2024-10-31 | 2026-07-31 | filed | yes | `c:TotalAssetsLessCurrentLiabilities` | small |
| average_employees | 0 | xbrli:pure | 2023-10-31 | 2025-07-28 | filed | yes | `d:AverageNumberEmployeesDuringPeriod` | small |
| average_employees | 0 | xbrli:pure | 2023-10-31 | 2024-07-29 | filed | no | `d:AverageNumberEmployeesDuringPeriod` | small |
| cash | 218992 | GBP | 2023-10-31 | 2025-07-28 | filed | yes | `d:CashBankOnHand` | small |
| cash | 218992 | GBP | 2023-10-31 | 2024-07-29 | filed | no | `d:CashBankOnHand` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 115453 | GBP | 2023-10-31 | 2025-07-28 | filed | yes | `d:Creditors` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 112136 | GBP | 2023-10-31 | 2024-07-29 | filed | no | `d:Creditors` | small |
| current_assets | 5834150 | GBP | 2023-10-31 | 2024-07-29 | filed | no | `d:CurrentAssets` | small |
| current_assets | 5837467 | GBP | 2023-10-31 | 2025-07-28 | filed | yes | `d:CurrentAssets` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 5615158 | GBP | 2023-10-31 | 2024-07-29 | filed | no | `d:Debtors` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 5618475 | GBP | 2023-10-31 | 2025-07-28 | filed | yes | `d:Debtors` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 5722013 | GBP | 2023-10-31 | 2025-07-28 | filed | yes | `d:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2023-10-31 | 2024-07-29 | filed | no | `d:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2023-10-31 | 2025-07-28 | filed | yes | `d:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 5722013 | GBP | 2023-10-31 | 2024-07-29 | filed | no | `d:Equity` | small |
| equity | 5722014 | GBP | 2023-10-31 | 2025-07-28 | filed | yes | `d:Equity` | small |
| equity | 5722014 | GBP | 2023-10-31 | 2024-07-29 | filed | no | `d:Equity` | small |
| net_assets | 5722014 | GBP | 2023-10-31 | 2025-07-28 | filed | yes | `d:NetAssetsLiabilities` | small |
| net_assets | 5722014 | GBP | 2023-10-31 | 2024-07-29 | filed | no | `d:NetAssetsLiabilities` | small |
| net_current_assets | 5722014 | GBP | 2023-10-31 | 2024-07-29 | filed | no | `d:NetCurrentAssetsLiabilities` | small |
| net_current_assets | 5722014 | GBP | 2023-10-31 | 2025-07-28 | filed | yes | `d:NetCurrentAssetsLiabilities` | small |
| total_assets_less_current_liabilities | 5722014 | GBP | 2023-10-31 | 2025-07-28 | filed | yes | `d:TotalAssetsLessCurrentLiabilities` | small |
| total_assets_less_current_liabilities | 5722014 | GBP | 2023-10-31 | 2024-07-29 | filed | no | `d:TotalAssetsLessCurrentLiabilities` | small |
| average_employees | 0 | xbrli:pure | 2022-10-31 | 2024-07-29 | filed | yes | `d:AverageNumberEmployeesDuringPeriod` | small |
| cash | 297352 | GBP | 2022-10-31 | 2024-07-29 | filed | yes | `d:CashBankOnHand` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 19373 | GBP | 2022-10-31 | 2024-07-29 | filed | yes | `d:Creditors` | small |
| current_assets | 4386058 | GBP | 2022-10-31 | 2024-07-29 | filed | yes | `d:CurrentAssets` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 4088706 | GBP | 2022-10-31 | 2024-07-29 | filed | yes | `d:Debtors` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2022-10-31 | 2024-07-29 | filed | yes | `d:Equity` | small |
| equity | 4366685 | GBP | 2022-10-31 | 2024-07-29 | filed | yes | `d:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 4366684 | GBP | 2022-10-31 | 2024-07-29 | filed | yes | `d:Equity` | small |
| net_assets | 4366685 | GBP | 2022-10-31 | 2024-07-29 | filed | yes | `d:NetAssetsLiabilities` | small |
| net_current_assets | 4366685 | GBP | 2022-10-31 | 2024-07-29 | filed | yes | `d:NetCurrentAssetsLiabilities` | small |
| total_assets_less_current_liabilities | 4366685 | GBP | 2022-10-31 | 2024-07-29 | filed | yes | `d:TotalAssetsLessCurrentLiabilities` | small |

_No coverage facts for the latest run._

- event restatement @ 2025-07-28: `{"superseded_document_id": "gb:04485978:doc:GWoHD0ef1D58yGCMJoo_RQboXZ2biANTiMyqPXCynsU", "restatements": [{"concept": "debtors", "period_end": "2023-10-31", "old_value": "5615158.0000", "new_value": `

## TRAVOLAB LTD (`gb:04834650`)

- registration: `04834650` (GB), status active, incorporated 2003-07-16
- classification: ['62012', '70229'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 80 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | xbrli:pure | 2025-12-31 | 2026-09-29 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 3559 | GBP | 2025-12-31 | 2026-09-29 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 19565 | GBP | 2025-12-31 | 2026-09-29 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 500695 | GBP | 2025-12-31 | 2026-09-29 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 399273 | GBP | 2025-12-31 | 2026-09-29 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 395714 | GBP | 2025-12-31 | 2026-09-29 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | -120987 | GBP | 2025-12-31 | 2026-09-29 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -131513 | GBP | 2025-12-31 | 2026-09-29 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10526 | GBP | 2025-12-31 | 2026-09-29 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | -120987 | GBP | 2025-12-31 | 2026-09-29 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -101422 | GBP | 2025-12-31 | 2026-09-29 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -101422 | GBP | 2025-12-31 | 2026-09-29 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0 | xbrli:pure | 2024-12-31 | 2026-09-29 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 0 | xbrli:pure | 2024-12-31 | 2025-09-30 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 1428 | GBP | 2024-12-31 | 2026-09-29 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 1428 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 24943 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 24943 | GBP | 2024-12-31 | 2026-09-29 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 491103 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 491103 | GBP | 2024-12-31 | 2026-09-29 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 397142 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 397142 | GBP | 2024-12-31 | 2026-09-29 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 395714 | GBP | 2024-12-31 | 2026-09-29 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 395714 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10526 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10526 | GBP | 2024-12-31 | 2026-09-29 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -129430 | GBP | 2024-12-31 | 2026-09-29 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -129430 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `core:Equity` | total-exemption-full |
| equity | -118904 | GBP | 2024-12-31 | 2026-09-29 | filed | yes | `core:Equity` | total-exemption-full |
| equity | -118904 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `core:Equity` | total-exemption-full |
| net_assets | -118904 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | -118904 | GBP | 2024-12-31 | 2026-09-29 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -93961 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -93961 | GBP | 2024-12-31 | 2026-09-29 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -93961 | GBP | 2024-12-31 | 2025-09-30 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -93961 | GBP | 2024-12-31 | 2026-09-29 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0 | xbrli:pure | 2023-12-31 | 2025-09-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 0 | xbrli:pure | 2023-12-31 | 2024-09-27 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 6430 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 6430 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 28559 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 28559 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 469548 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 469548 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 246876 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 246876 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors | 240446 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 240446 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `core:Debtors` | total-exemption-full |
| equity | -92706 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10526 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -103232 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10526 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `core:Equity` | total-exemption-full |
| equity | -92706 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -103232 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | -92706 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | -92706 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -222672 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -222672 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -64147 | GBP | 2023-12-31 | 2025-09-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -64147 | GBP | 2023-12-31 | 2024-09-27 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0 | xbrli:pure | 2022-12-31 | 2024-09-27 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 17287 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 34206 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 447678 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 275168 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 257881 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | -48191 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -58717 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 10526 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | -48191 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -172510 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | -13985 | GBP | 2022-12-31 | 2024-09-27 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._
