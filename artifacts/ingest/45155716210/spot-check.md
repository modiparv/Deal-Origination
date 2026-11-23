# Ingest spot-check

- database: `data/engine.db`
- latest run: `20261123T102440Z-921dce67`
- companies in store: 58600; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## APTECH (POWDER SYSTEMS) LIMITED (`gb:02925646`)

- registration: `02925646` (GB), status active, incorporated 1994-05-04
- classification: ['71121'] (sic_2007)
- records: 7 officers, 2 beneficial owners, 0 ownership statements, 5 security interests, 91 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.14 | xbrli:pure | 2025-07-31 | 2026-04-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 998840 | GBP | 2025-07-31 | 2026-04-30 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 400874 | GBP | 2025-07-31 | 2026-04-30 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 2334561 | GBP | 2025-07-31 | 2026-04-30 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 1000279 | GBP | 2025-07-31 | 2026-04-30 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 900 | GBP | 2025-07-31 | 2026-04-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1981158 | GBP | 2025-07-31 | 2026-04-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 20859 | GBP | 2025-07-31 | 2026-04-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 2003017 | GBP | 2025-07-31 | 2026-04-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-07-31 | 2026-04-30 | filed | yes | `core:Equity` | total-exemption-full |
| net_current_assets | 1933687 | GBP | 2025-07-31 | 2026-04-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 2003017 | GBP | 2025-07-31 | 2026-04-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0.11 | xbrli:pure | 2024-07-31 | 2026-04-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 11 | xbrli:pure | 2024-07-31 | 2025-04-30 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 1095902 | GBP | 2024-07-31 | 2026-04-30 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 1095902 | GBP | 2024-07-31 | 2025-04-30 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 72866 | GBP | 2024-07-31 | 2026-04-30 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 72866 | GBP | 2024-07-31 | 2025-04-30 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 1634724 | GBP | 2024-07-31 | 2026-04-30 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 1634724 | GBP | 2024-07-31 | 2025-04-30 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors | 220747 | GBP | 2024-07-31 | 2026-04-30 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 102707 | GBP | 2024-07-31 | 2025-04-30 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 220747 | GBP | 2024-07-31 | 2025-04-30 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1595653 | GBP | 2024-07-31 | 2026-04-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-07-31 | 2026-04-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1595653 | GBP | 2024-07-31 | 2025-04-30 | filed | no | `core:Equity` | total-exemption-full |
| equity | 1609605 | GBP | 2024-07-31 | 2026-04-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 12952 | GBP | 2024-07-31 | 2025-04-30 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 900 | GBP | 2024-07-31 | 2025-04-30 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-07-31 | 2025-04-30 | filed | no | `core:Equity` | total-exemption-full |
| equity | 1609605 | GBP | 2024-07-31 | 2025-04-30 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 900 | GBP | 2024-07-31 | 2026-04-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 12952 | GBP | 2024-07-31 | 2026-04-30 | filed | yes | `core:Equity` | total-exemption-full |
| net_current_assets | 1561858 | GBP | 2024-07-31 | 2026-04-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1561858 | GBP | 2024-07-31 | 2025-04-30 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1609605 | GBP | 2024-07-31 | 2026-04-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1609605 | GBP | 2024-07-31 | 2025-04-30 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 12 | xbrli:pure | 2023-07-31 | 2024-04-25 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 12 | xbrli:pure | 2023-07-31 | 2025-04-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 1280581 | GBP | 2023-07-31 | 2025-04-30 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 1280581 | GBP | 2023-07-31 | 2024-04-25 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 313472 | GBP | 2023-07-31 | 2024-04-25 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 313472 | GBP | 2023-07-31 | 2025-04-30 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 2143602 | GBP | 2023-07-31 | 2025-04-30 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 2143602 | GBP | 2023-07-31 | 2024-04-25 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors | 577781 | GBP | 2023-07-31 | 2024-04-25 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 577781 | GBP | 2023-07-31 | 2025-04-30 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 557418 | GBP | 2023-07-31 | 2024-04-25 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 557418 | GBP | 2023-07-31 | 2025-04-30 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 1877560 | GBP | 2023-07-31 | 2024-04-25 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-07-31 | 2025-04-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 1877560 | GBP | 2023-07-31 | 2025-04-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1873221 | GBP | 2023-07-31 | 2024-04-25 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 900 | GBP | 2023-07-31 | 2024-04-25 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1873221 | GBP | 2023-07-31 | 2025-04-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-07-31 | 2024-04-25 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 3339 | GBP | 2023-07-31 | 2025-04-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 900 | GBP | 2023-07-31 | 2025-04-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 3339 | GBP | 2023-07-31 | 2024-04-25 | filed | no | `core:Equity` | total-exemption-full |
| net_assets | 1877560 | GBP | 2023-07-31 | 2024-04-25 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1830130 | GBP | 2023-07-31 | 2025-04-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1830130 | GBP | 2023-07-31 | 2024-04-25 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1877560 | GBP | 2023-07-31 | 2024-04-25 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1877560 | GBP | 2023-07-31 | 2025-04-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 12 | xbrli:pure | 2022-07-31 | 2024-04-25 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 1333166 | GBP | 2022-07-31 | 2024-04-25 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 469671 | GBP | 2022-07-31 | 2024-04-25 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 2340180 | GBP | 2022-07-31 | 2024-04-25 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 726940 | GBP | 2022-07-31 | 2024-04-25 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 726940 | GBP | 2022-07-31 | 2024-04-25 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 900 | GBP | 2022-07-31 | 2024-04-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2022-07-31 | 2024-04-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1891104 | GBP | 2022-07-31 | 2024-04-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 7730 | GBP | 2022-07-31 | 2024-04-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 1899834 | GBP | 2022-07-31 | 2024-04-25 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 1899834 | GBP | 2022-07-31 | 2024-04-25 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1870509 | GBP | 2022-07-31 | 2024-04-25 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1900745 | GBP | 2022-07-31 | 2024-04-25 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2026-04-30: `{"superseded_document_id": "gb:02925646:doc:RaeTDUt-luIwxdbL64KLq6Z_L46aHomZF2EzL4w3-vU", "restatements": [{"concept": "average_employees", "period_end": "2024-07-31", "old_value": "11.0000", "new_val`

## PIONEER SOFTWARE LTD (`gb:03634312`)

- registration: `03634312` (GB), status active, incorporated 1998-09-17
- classification: ['62012'] (sic_2007)
- records: 5 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 93 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 3 | xbrli:pure | 2025-09-30 | 2026-04-07 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 390019 | GBP | 2025-09-30 | 2026-04-07 | filed | yes | `ns5:CashBankOnHand` | unaudited-abridged |
| current_assets | 397695 | GBP | 2025-09-30 | 2026-04-07 | filed | yes | `ns5:CurrentAssets` | unaudited-abridged |
| debtors | 7676 | GBP | 2025-09-30 | 2026-04-07 | filed | yes | `ns5:Debtors` | unaudited-abridged |
| equity | 387800 | GBP | 2025-09-30 | 2026-04-07 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 387797 | GBP | 2025-09-30 | 2026-04-07 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 3 | GBP | 2025-09-30 | 2026-04-07 | filed | yes | `ns5:Equity` | unaudited-abridged |
| net_assets | 387800 | GBP | 2025-09-30 | 2026-04-07 | filed | yes | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 348513 | GBP | 2025-09-30 | 2026-04-07 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 388915 | GBP | 2025-09-30 | 2026-04-07 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 3 | xbrli:pure | 2024-09-30 | 2025-03-14 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| average_employees | 3 | xbrli:pure | 2024-09-30 | 2026-04-07 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 51702 | GBP | 2024-09-30 | 2025-03-14 | filed | no | `ns5:CashBankOnHand` | unaudited-abridged |
| cash | 51702 | GBP | 2024-09-30 | 2026-04-07 | filed | yes | `ns5:CashBankOnHand` | unaudited-abridged |
| current_assets | 338819 | GBP | 2024-09-30 | 2026-04-07 | filed | yes | `ns5:CurrentAssets` | unaudited-abridged |
| current_assets | 338819 | GBP | 2024-09-30 | 2025-03-14 | filed | no | `ns5:CurrentAssets` | unaudited-abridged |
| debtors | 287117 | GBP | 2024-09-30 | 2026-04-07 | filed | yes | `ns5:Debtors` | unaudited-abridged |
| debtors | 287117 | GBP | 2024-09-30 | 2025-03-14 | filed | no | `ns5:Debtors` | unaudited-abridged |
| equity | 344008 | GBP | 2024-09-30 | 2026-04-07 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 344005 | GBP | 2024-09-30 | 2026-04-07 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 344005 | GBP | 2024-09-30 | 2025-03-14 | filed | no | `ns5:Equity` | unaudited-abridged |
| equity | 344008 | GBP | 2024-09-30 | 2025-03-14 | filed | no | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 3 | GBP | 2024-09-30 | 2025-03-14 | filed | no | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 3 | GBP | 2024-09-30 | 2026-04-07 | filed | yes | `ns5:Equity` | unaudited-abridged |
| net_assets | 344008 | GBP | 2024-09-30 | 2025-03-14 | filed | no | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_assets | 344008 | GBP | 2024-09-30 | 2026-04-07 | filed | yes | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 283351 | GBP | 2024-09-30 | 2026-04-07 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 283351 | GBP | 2024-09-30 | 2025-03-14 | filed | no | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 346469 | GBP | 2024-09-30 | 2025-03-14 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 346469 | GBP | 2024-09-30 | 2026-04-07 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 3 | xbrli:pure | 2023-09-30 | 2024-02-06 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| average_employees | 3 | xbrli:pure | 2023-09-30 | 2025-03-14 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 290446 | GBP | 2023-09-30 | 2025-03-14 | filed | yes | `ns5:CashBankOnHand` | unaudited-abridged |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 290446 | GBP | 2023-09-30 | 2024-02-06 | filed | yes | `ns5:CashBankOnHand` | unaudited-abridged |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 297900 | GBP | 2023-09-30 | 2024-02-06 | filed | yes | `ns5:CurrentAssets` | unaudited-abridged |
| current_assets | 297900 | GBP | 2023-09-30 | 2025-03-14 | filed | yes | `ns5:CurrentAssets` | unaudited-abridged |
| debtors `{'OriginalRevisedDataDimension': 'Original'}` | 7454 | GBP | 2023-09-30 | 2024-02-06 | filed | yes | `ns5:Debtors` | unaudited-abridged |
| debtors | 7454 | GBP | 2023-09-30 | 2025-03-14 | filed | yes | `ns5:Debtors` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 3 | GBP | 2023-09-30 | 2024-02-06 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 269234 | GBP | 2023-09-30 | 2024-02-06 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 269237 | GBP | 2023-09-30 | 2024-02-06 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 269234 | GBP | 2023-09-30 | 2025-03-14 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity | 269237 | GBP | 2023-09-30 | 2025-03-14 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 3 | GBP | 2023-09-30 | 2025-03-14 | filed | yes | `ns5:Equity` | unaudited-abridged |
| net_assets `{'OriginalRevisedDataDimension': 'Original'}` | 269237 | GBP | 2023-09-30 | 2024-02-06 | filed | yes | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_assets | 269237 | GBP | 2023-09-30 | 2025-03-14 | filed | yes | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 218498 | GBP | 2023-09-30 | 2024-02-06 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 218498 | GBP | 2023-09-30 | 2025-03-14 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 271121 | GBP | 2023-09-30 | 2024-02-06 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 271121 | GBP | 2023-09-30 | 2025-03-14 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 3 | xbrli:pure | 2022-09-30 | 2024-02-06 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 209344 | GBP | 2022-09-30 | 2024-02-06 | filed | yes | `ns5:CashBankOnHand` | unaudited-abridged |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 215054 | GBP | 2022-09-30 | 2024-02-06 | filed | yes | `ns5:CurrentAssets` | unaudited-abridged |
| debtors `{'OriginalRevisedDataDimension': 'Original'}` | 5710 | GBP | 2022-09-30 | 2024-02-06 | filed | yes | `ns5:Debtors` | unaudited-abridged |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 189270 | GBP | 2022-09-30 | 2024-02-06 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 3 | GBP | 2022-09-30 | 2024-02-06 | filed | yes | `ns5:Equity` | unaudited-abridged |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 189273 | GBP | 2022-09-30 | 2024-02-06 | filed | yes | `ns5:Equity` | unaudited-abridged |
| net_assets `{'OriginalRevisedDataDimension': 'Original'}` | 189273 | GBP | 2022-09-30 | 2024-02-06 | filed | yes | `ns5:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 138967 | GBP | 2022-09-30 | 2024-02-06 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 190352 | GBP | 2022-09-30 | 2024-02-06 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |

_No coverage facts for the latest run._

## CARNGLAZE LIMITED (`gb:04282560`)

- registration: `04282560` (GB), status active, incorporated 2001-09-06
- classification: ['71111'] (sic_2007)
- records: 5 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 66 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-09-30 | 2026-01-22 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 63396 | GBP | 2025-09-30 | 2026-01-22 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 28536 | GBP | 2025-09-30 | 2026-01-22 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 27509 | GBP | 2025-09-30 | 2026-01-22 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 12303 | GBP | 2025-09-30 | 2026-01-22 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 77902 | GBP | 2025-09-30 | 2026-01-22 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 12303 | GBP | 2025-09-30 | 2026-01-22 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -1027 | GBP | 2025-09-30 | 2026-01-22 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 76875 | GBP | 2025-09-30 | 2026-01-22 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-09-30 | 2025-05-21 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-09-30 | 2026-01-22 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2024-09-30 | 2026-01-22 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 29155 | GBP | 2024-09-30 | 2025-05-21 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 27978 | GBP | 2024-09-30 | 2026-01-22 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 28885 | GBP | 2024-09-30 | 2025-05-21 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 28885 | GBP | 2024-09-30 | 2026-01-22 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 7 | GBP | 2024-09-30 | 2025-05-21 | filed | no | `core:Equity` | micro-entity |
| equity | 6 | GBP | 2024-09-30 | 2026-01-22 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 277 | GBP | 2024-09-30 | 2025-05-21 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 276 | GBP | 2024-09-30 | 2026-01-22 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 7 | GBP | 2024-09-30 | 2025-05-21 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 6 | GBP | 2024-09-30 | 2026-01-22 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 907 | GBP | 2024-09-30 | 2026-01-22 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -270 | GBP | 2024-09-30 | 2025-05-21 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 1183 | GBP | 2024-09-30 | 2026-01-22 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 7 | GBP | 2024-09-30 | 2025-05-21 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-09-30 | 2025-05-21 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-09-30 | 2024-06-13 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 22835 | GBP | 2023-09-30 | 2024-06-13 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 22835 | GBP | 2023-09-30 | 2025-05-21 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 20452 | GBP | 2023-09-30 | 2024-06-13 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 20452 | GBP | 2023-09-30 | 2025-05-21 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 54 | GBP | 2023-09-30 | 2024-06-13 | filed | no | `core:Equity` | micro-entity |
| equity | 54 | GBP | 2023-09-30 | 2025-05-21 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 2437 | GBP | 2023-09-30 | 2025-05-21 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 2437 | GBP | 2023-09-30 | 2024-06-13 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | 54 | GBP | 2023-09-30 | 2024-06-13 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 54 | GBP | 2023-09-30 | 2025-05-21 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -2383 | GBP | 2023-09-30 | 2025-05-21 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -2383 | GBP | 2023-09-30 | 2024-06-13 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 54 | GBP | 2023-09-30 | 2024-06-13 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 54 | GBP | 2023-09-30 | 2025-05-21 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2022-09-30 | 2024-06-13 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 11517 | GBP | 2022-09-30 | 2024-06-13 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 6670 | GBP | 2022-09-30 | 2024-06-13 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 26 | GBP | 2022-09-30 | 2024-06-13 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 4873 | GBP | 2022-09-30 | 2024-06-13 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 26 | GBP | 2022-09-30 | 2024-06-13 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -4847 | GBP | 2022-09-30 | 2024-06-13 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 26 | GBP | 2022-09-30 | 2024-06-13 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2026-01-22: `{"superseded_document_id": "gb:04282560:doc:mUzL80dkAs4RUW8XjaW-eUqgQguYgbSINrcXE6dewH4", "restatements": [{"concept": "fixed_assets", "period_end": "2024-09-30", "old_value": "277.0000", "new_value":`

## NETRING LIMITED (`gb:04950488`)

- registration: `04950488` (GB), status active, incorporated 2003-11-03
- classification: ['62090'] (sic_2007)
- records: 5 officers, 2 beneficial owners, 0 ownership statements, 1 security interests, 61 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 14 | xbrli:pure | 2025-03-31 | 2025-12-16 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 40532 | GBP | 2025-03-31 | 2025-12-16 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 148946 | GBP | 2025-03-31 | 2025-12-16 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 59584 | GBP | 2025-03-31 | 2025-12-16 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 59584 | GBP | 2025-03-31 | 2025-12-16 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 210815 | GBP | 2025-03-31 | 2025-12-16 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 210817 | GBP | 2025-03-31 | 2025-12-16 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2025-03-31 | 2025-12-16 | filed | yes | `ns5:Equity` | total-exemption-full |
| fixed_assets | 207070 | GBP | 2025-03-31 | 2025-12-16 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| net_assets | 210817 | GBP | 2025-03-31 | 2025-12-16 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 13519 | GBP | 2025-03-31 | 2025-12-16 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 220589 | GBP | 2025-03-31 | 2025-12-16 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 8 | xbrli:pure | 2024-03-31 | 2025-12-16 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 8 | xbrli:pure | 2024-03-31 | 2024-12-18 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 32195 | GBP | 2024-03-31 | 2024-12-18 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 32195 | GBP | 2024-03-31 | 2025-12-16 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 116245 | GBP | 2024-03-31 | 2024-12-18 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 116245 | GBP | 2024-03-31 | 2025-12-16 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 63357 | GBP | 2024-03-31 | 2025-12-16 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 63357 | GBP | 2024-03-31 | 2024-12-18 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 63357 | GBP | 2024-03-31 | 2025-12-16 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 63357 | GBP | 2024-03-31 | 2024-12-18 | filed | no | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 180688 | GBP | 2024-03-31 | 2025-12-16 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 180690 | GBP | 2024-03-31 | 2025-12-16 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 180690 | GBP | 2024-03-31 | 2024-12-18 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-03-31 | 2025-12-16 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 180688 | GBP | 2024-03-31 | 2024-12-18 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-03-31 | 2024-12-18 | filed | no | `ns5:Equity` | total-exemption-full |
| fixed_assets | 163652 | GBP | 2024-03-31 | 2025-12-16 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| fixed_assets | 163652 | GBP | 2024-03-31 | 2024-12-18 | filed | no | `ns5:FixedAssets` | total-exemption-full |
| net_assets | 180690 | GBP | 2024-03-31 | 2024-12-18 | filed | no | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 180690 | GBP | 2024-03-31 | 2025-12-16 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 35761 | GBP | 2024-03-31 | 2025-12-16 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 35761 | GBP | 2024-03-31 | 2024-12-18 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 199413 | GBP | 2024-03-31 | 2024-12-18 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 199413 | GBP | 2024-03-31 | 2025-12-16 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 8 | xbrli:pure | 2023-03-31 | 2023-11-07 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 8 | xbrli:pure | 2023-03-31 | 2024-12-18 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 34950 | GBP | 2023-03-31 | 2023-11-07 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 34950 | GBP | 2023-03-31 | 2024-12-18 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 105633 | GBP | 2023-03-31 | 2023-11-07 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 105633 | GBP | 2023-03-31 | 2024-12-18 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 40507 | GBP | 2023-03-31 | 2024-12-18 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 40507 | GBP | 2023-03-31 | 2023-11-07 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original'}` | 40507 | GBP | 2023-03-31 | 2023-11-07 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 40507 | GBP | 2023-03-31 | 2024-12-18 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-03-31 | 2024-12-18 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 153869 | GBP | 2023-03-31 | 2023-11-07 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 153869 | GBP | 2023-03-31 | 2024-12-18 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 2 | GBP | 2023-03-31 | 2023-11-07 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 153867 | GBP | 2023-03-31 | 2023-11-07 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 153867 | GBP | 2023-03-31 | 2024-12-18 | filed | yes | `ns5:Equity` | total-exemption-full |
| fixed_assets `{'OriginalRevisedDataDimension': 'Original'}` | 129042 | GBP | 2023-03-31 | 2023-11-07 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| fixed_assets | 129042 | GBP | 2023-03-31 | 2024-12-18 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| net_assets `{'OriginalRevisedDataDimension': 'Original'}` | 153869 | GBP | 2023-03-31 | 2023-11-07 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 153869 | GBP | 2023-03-31 | 2024-12-18 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 44047 | GBP | 2023-03-31 | 2023-11-07 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 44047 | GBP | 2023-03-31 | 2024-12-18 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 173089 | GBP | 2023-03-31 | 2024-12-18 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 173089 | GBP | 2023-03-31 | 2023-11-07 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 8 | xbrli:pure | 2022-03-31 | 2023-11-07 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 42004 | GBP | 2022-03-31 | 2023-11-07 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 75490 | GBP | 2022-03-31 | 2023-11-07 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original'}` | 17228 | GBP | 2022-03-31 | 2023-11-07 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 17228 | GBP | 2022-03-31 | 2023-11-07 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 2 | GBP | 2022-03-31 | 2023-11-07 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 123468 | GBP | 2022-03-31 | 2023-11-07 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 123470 | GBP | 2022-03-31 | 2023-11-07 | filed | yes | `ns5:Equity` | total-exemption-full |
| fixed_assets `{'OriginalRevisedDataDimension': 'Original'}` | 97750 | GBP | 2022-03-31 | 2023-11-07 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| net_assets `{'OriginalRevisedDataDimension': 'Original'}` | 123470 | GBP | 2022-03-31 | 2023-11-07 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 25720 | GBP | 2022-03-31 | 2023-11-07 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 123470 | GBP | 2022-03-31 | 2023-11-07 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## SRI RAGHAV IT SERVICES LIMITED (`gb:05601268`)

- registration: `05601268` (GB), status active, incorporated 2005-10-24
- classification: ['62020'] (sic_2007)
- records: 4 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 58 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 3 | xbrli:pure | 2025-10-31 | 2026-07-28 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 16876 | GBP | 2025-10-31 | 2026-07-28 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 304281 | GBP | 2025-10-31 | 2026-07-28 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 288610 | GBP | 2025-10-31 | 2026-07-28 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 1205 | GBP | 2025-10-31 | 2026-07-28 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 288610 | GBP | 2025-10-31 | 2026-07-28 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 287405 | GBP | 2025-10-31 | 2026-07-28 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 288610 | GBP | 2025-10-31 | 2026-07-28 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 3 | xbrli:pure | 2024-10-31 | 2026-07-28 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 3 | xbrli:pure | 2024-10-31 | 2025-07-29 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 52854 | GBP | 2024-10-31 | 2025-07-29 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 52854 | GBP | 2024-10-31 | 2026-07-28 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 308102 | GBP | 2024-10-31 | 2026-07-28 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 308102 | GBP | 2024-10-31 | 2025-07-29 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 256616 | GBP | 2024-10-31 | 2025-07-29 | filed | no | `core:Equity` | micro-entity |
| equity | 256616 | GBP | 2024-10-31 | 2026-07-28 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 1368 | GBP | 2024-10-31 | 2026-07-28 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 1368 | GBP | 2024-10-31 | 2025-07-29 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | 256616 | GBP | 2024-10-31 | 2026-07-28 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 256616 | GBP | 2024-10-31 | 2025-07-29 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 255248 | GBP | 2024-10-31 | 2026-07-28 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 255248 | GBP | 2024-10-31 | 2025-07-29 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 256616 | GBP | 2024-10-31 | 2025-07-29 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 256616 | GBP | 2024-10-31 | 2026-07-28 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 3 | xbrli:pure | 2023-10-31 | 2025-07-29 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 3 | xbrli:pure | 2023-10-31 | 2024-07-30 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 2050 | GBP | 2023-10-31 | 2024-07-30 | filed | no | `core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 2050 | GBP | 2023-10-31 | 2025-07-29 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 23690 | GBP | 2023-10-31 | 2025-07-29 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 23690 | GBP | 2023-10-31 | 2024-07-30 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 273846 | GBP | 2023-10-31 | 2025-07-29 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 273846 | GBP | 2023-10-31 | 2024-07-30 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 249816 | GBP | 2023-10-31 | 2025-07-29 | filed | yes | `core:Equity` | micro-entity |
| equity | 249816 | GBP | 2023-10-31 | 2024-07-30 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 1710 | GBP | 2023-10-31 | 2025-07-29 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 1710 | GBP | 2023-10-31 | 2024-07-30 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | 249816 | GBP | 2023-10-31 | 2024-07-30 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 249816 | GBP | 2023-10-31 | 2025-07-29 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 250156 | GBP | 2023-10-31 | 2024-07-30 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 250156 | GBP | 2023-10-31 | 2025-07-29 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 251866 | GBP | 2023-10-31 | 2024-07-30 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 251866 | GBP | 2023-10-31 | 2025-07-29 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 3 | xbrli:pure | 2022-10-31 | 2024-07-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 64462 | GBP | 2022-10-31 | 2024-07-30 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 300046 | GBP | 2022-10-31 | 2024-07-30 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 237802 | GBP | 2022-10-31 | 2024-07-30 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 2218 | GBP | 2022-10-31 | 2024-07-30 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 237802 | GBP | 2022-10-31 | 2024-07-30 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 235584 | GBP | 2022-10-31 | 2024-07-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 237802 | GBP | 2022-10-31 | 2024-07-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## NOORTECH LTD (`gb:06197959`)

- registration: `06197959` (GB), status active, incorporated 2007-04-02
- classification: ['62020'] (sic_2007)
- records: 2 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 52 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | iso4217:GBP | 2025-06-30 | 2026-01-31 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 8544 | GBP | 2025-06-30 | 2026-01-31 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 399 | GBP | 2025-06-30 | 2026-01-31 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 8145 | GBP | 2025-06-30 | 2026-01-31 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 8145 | GBP | 2025-06-30 | 2026-01-31 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 8145 | GBP | 2025-06-30 | 2026-01-31 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 8145 | GBP | 2025-06-30 | 2026-01-31 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2024-06-30 | 2025-03-31 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2024-06-30 | 2026-01-31 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 7974 | GBP | 2024-06-30 | 2025-03-31 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 7974 | GBP | 2024-06-30 | 2026-01-31 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 386 | GBP | 2024-06-30 | 2025-03-31 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 386 | GBP | 2024-06-30 | 2026-01-31 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 7588 | GBP | 2024-06-30 | 2025-03-31 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 7588 | GBP | 2024-06-30 | 2026-01-31 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 7588 | GBP | 2024-06-30 | 2025-03-31 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 7588 | GBP | 2024-06-30 | 2026-01-31 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 7588 | GBP | 2024-06-30 | 2025-03-31 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 7588 | GBP | 2024-06-30 | 2026-01-31 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 7588 | GBP | 2024-06-30 | 2025-03-31 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 7588 | GBP | 2024-06-30 | 2026-01-31 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2023-06-30 | 2025-03-31 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2023-06-30 | 2024-03-31 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 7447 | GBP | 2023-06-30 | 2025-03-31 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 7447 | GBP | 2023-06-30 | 2024-03-31 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 430 | GBP | 2023-06-30 | 2024-03-31 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 430 | GBP | 2023-06-30 | 2025-03-31 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 7017 | GBP | 2023-06-30 | 2024-03-31 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 7017 | GBP | 2023-06-30 | 2025-03-31 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 7017 | GBP | 2023-06-30 | 2024-03-31 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 7017 | GBP | 2023-06-30 | 2025-03-31 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 7017 | GBP | 2023-06-30 | 2025-03-31 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 7017 | GBP | 2023-06-30 | 2024-03-31 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 7017 | GBP | 2023-06-30 | 2024-03-31 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 7017 | GBP | 2023-06-30 | 2025-03-31 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2022-06-30 | 2024-03-31 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 6947 | GBP | 2022-06-30 | 2024-03-31 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 434 | GBP | 2022-06-30 | 2024-03-31 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 6513 | GBP | 2022-06-30 | 2024-03-31 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 6513 | GBP | 2022-06-30 | 2024-03-31 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 6513 | GBP | 2022-06-30 | 2024-03-31 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 6513 | GBP | 2022-06-30 | 2024-03-31 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## SAPIO SYSTEMS LIMITED (`gb:06662876`)

- registration: `06662876` (GB), status active, incorporated 2008-08-04
- classification: ['62012'] (sic_2007)
- records: 2 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 56 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 4 | xbrli:pure | 2025-06-25 | 2026-03-25 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 49368 | GBP | 2025-06-25 | 2026-03-25 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 135136 | GBP | 2025-06-25 | 2026-03-25 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 85768 | GBP | 2025-06-25 | 2026-03-25 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 64126 | GBP | 2025-06-25 | 2026-03-25 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 781 | GBP | 2025-06-25 | 2026-03-25 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 60000 | GBP | 2025-06-25 | 2026-03-25 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2025-06-25 | 2026-03-25 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 3352 | GBP | 2025-06-25 | 2026-03-25 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 60881 | GBP | 2025-06-25 | 2026-03-25 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 57529 | GBP | 2025-06-25 | 2026-03-25 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 60881 | GBP | 2025-06-25 | 2026-03-25 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 4 | xbrli:pure | 2024-06-29 | 2026-03-25 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 4 | xbrli:pure | 2024-06-29 | 2025-09-25 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 33089 | GBP | 2024-06-29 | 2026-03-25 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| cash | 33089 | GBP | 2024-06-29 | 2025-09-25 | filed | no | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 44466 | GBP | 2024-06-29 | 2025-09-25 | filed | no | `frs-core:CurrentAssets` | total-exemption-full |
| current_assets | 44466 | GBP | 2024-06-29 | 2026-03-25 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 11377 | GBP | 2024-06-29 | 2026-03-25 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 11377 | GBP | 2024-06-29 | 2026-03-25 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| debtors | 11377 | GBP | 2024-06-29 | 2025-09-25 | filed | no | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-06-29 | 2026-03-25 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 60000 | GBP | 2024-06-29 | 2025-09-25 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -44993 | GBP | 2024-06-29 | 2025-09-25 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -44993 | GBP | 2024-06-29 | 2026-03-25 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-06-29 | 2025-09-25 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 60000 | GBP | 2024-06-29 | 2026-03-25 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 2451 | GBP | 2024-06-29 | 2025-09-25 | filed | no | `frs-core:FixedAssets` | total-exemption-full |
| fixed_assets | 2451 | GBP | 2024-06-29 | 2026-03-25 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 15107 | GBP | 2024-06-29 | 2025-09-25 | filed | no | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 15107 | GBP | 2024-06-29 | 2026-03-25 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 12656 | GBP | 2024-06-29 | 2026-03-25 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 12656 | GBP | 2024-06-29 | 2025-09-25 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 15107 | GBP | 2024-06-29 | 2025-09-25 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 15107 | GBP | 2024-06-29 | 2026-03-25 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 4 | xbrli:pure | 2023-06-29 | 2025-09-25 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 10378 | GBP | 2023-06-29 | 2025-09-25 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 40947 | GBP | 2023-06-29 | 2025-09-25 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 30569 | GBP | 2023-06-29 | 2025-09-25 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -38912 | GBP | 2023-06-29 | 2025-09-25 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-06-29 | 2025-09-25 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 60000 | GBP | 2023-06-29 | 2025-09-25 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 2451 | GBP | 2023-06-29 | 2025-09-25 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 21188 | GBP | 2023-06-29 | 2025-09-25 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 18737 | GBP | 2023-06-29 | 2025-09-25 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 21188 | GBP | 2023-06-29 | 2025-09-25 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## ALLCLOUD NETWORKS LIMITED (`gb:07088039`)

- registration: `07088039` (GB), status active, incorporated 2009-11-26
- classification: ['62020'] (sic_2007)
- records: 1 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 44 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | iso4217:GBP | 2025-11-30 | 2025-12-15 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 57683 | GBP | 2025-11-30 | 2025-12-15 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 58167 | GBP | 2025-11-30 | 2025-12-15 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 384 | GBP | 2025-11-30 | 2025-12-15 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 58167 | GBP | 2025-11-30 | 2025-12-15 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 57683 | GBP | 2025-11-30 | 2025-12-15 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 58167 | GBP | 2025-11-30 | 2025-12-15 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2024-11-30 | 2025-12-15 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2024-11-30 | 2025-01-10 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2024-11-30 | 2025-01-10 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2024-11-30 | 2025-01-10 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 60784 | GBP | 2024-11-30 | 2025-12-15 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 60784 | GBP | 2024-11-30 | 2025-01-10 | filed | no | `core:CurrentAssets` | micro-entity |
| depreciation_amortisation | 83 | GBP | 2024-11-30 | 2025-01-10 | filed | yes | `core:DepreciationAmortisationImpairmentExpense` | micro-entity |
| equity | 61336 | GBP | 2024-11-30 | 2025-01-10 | filed | no | `core:Equity` | micro-entity |
| equity | 61336 | GBP | 2024-11-30 | 2025-12-15 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 452 | GBP | 2024-11-30 | 2025-12-15 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 452 | GBP | 2024-11-30 | 2025-01-10 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | 61336 | GBP | 2024-11-30 | 2025-12-15 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 61336 | GBP | 2024-11-30 | 2025-01-10 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 60784 | GBP | 2024-11-30 | 2025-12-15 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 60784 | GBP | 2024-11-30 | 2025-01-10 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| profit_for_period | -3460 | GBP | 2024-11-30 | 2025-01-10 | filed | yes | `core:ProfitLoss` | micro-entity |
| revenue | 0 | GBP | 2024-11-30 | 2025-01-10 | filed | yes | `core:TurnoverRevenue` | micro-entity |
| staff_costs | 0 | GBP | 2024-11-30 | 2025-01-10 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | micro-entity |
| total_assets_less_current_liabilities | 61336 | GBP | 2024-11-30 | 2025-01-10 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 61336 | GBP | 2024-11-30 | 2025-12-15 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-11-30 | 2024-02-17 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 0 | GBP | 2023-11-30 | 2025-01-10 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2023-11-30 | 2025-01-10 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 64141 | GBP | 2023-11-30 | 2025-01-10 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 64141 | GBP | 2023-11-30 | 2024-02-17 | filed | no | `core:CurrentAssets` | micro-entity |
| depreciation_amortisation | 96 | GBP | 2023-11-30 | 2025-01-10 | filed | yes | `core:DepreciationAmortisationImpairmentExpense` | micro-entity |
| depreciation_amortisation | 96 | GBP | 2023-11-30 | 2024-02-17 | filed | no | `core:DepreciationAmortisationImpairmentExpense` | micro-entity |
| equity | 64776 | GBP | 2023-11-30 | 2025-01-10 | filed | yes | `core:Equity` | micro-entity |
| equity | 64776 | GBP | 2023-11-30 | 2024-02-17 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 535 | GBP | 2023-11-30 | 2025-01-10 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 535 | GBP | 2023-11-30 | 2024-02-17 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | 64776 | GBP | 2023-11-30 | 2024-02-17 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 64776 | GBP | 2023-11-30 | 2025-01-10 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 64141 | GBP | 2023-11-30 | 2025-01-10 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 64141 | GBP | 2023-11-30 | 2024-02-17 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| profit_for_period | -2139 | GBP | 2023-11-30 | 2024-02-17 | filed | no | `core:ProfitLoss` | micro-entity |
| profit_for_period | -2139 | GBP | 2023-11-30 | 2025-01-10 | filed | yes | `core:ProfitLoss` | micro-entity |
| revenue | 0 | GBP | 2023-11-30 | 2024-02-17 | filed | no | `core:TurnoverRevenue` | micro-entity |
| revenue | 0 | GBP | 2023-11-30 | 2025-01-10 | filed | yes | `core:TurnoverRevenue` | micro-entity |
| staff_costs | 0 | GBP | 2023-11-30 | 2025-01-10 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | micro-entity |
| staff_costs | 0 | GBP | 2023-11-30 | 2024-02-17 | filed | no | `core:StaffCostsEmployeeBenefitsExpense` | micro-entity |
| total_assets_less_current_liabilities | 64776 | GBP | 2023-11-30 | 2025-01-10 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 64776 | GBP | 2023-11-30 | 2024-02-17 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| current_assets | 66184 | GBP | 2022-11-30 | 2024-02-17 | filed | yes | `core:CurrentAssets` | micro-entity |
| depreciation_amortisation | 112 | GBP | 2022-11-30 | 2024-02-17 | filed | yes | `core:DepreciationAmortisationImpairmentExpense` | micro-entity |
| equity | 66915 | GBP | 2022-11-30 | 2024-02-17 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 631 | GBP | 2022-11-30 | 2024-02-17 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 66915 | GBP | 2022-11-30 | 2024-02-17 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 66184 | GBP | 2022-11-30 | 2024-02-17 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| profit_for_period | -2060 | GBP | 2022-11-30 | 2024-02-17 | filed | yes | `core:ProfitLoss` | micro-entity |
| revenue | 0 | GBP | 2022-11-30 | 2024-02-17 | filed | yes | `core:TurnoverRevenue` | micro-entity |
| staff_costs | 0 | GBP | 2022-11-30 | 2024-02-17 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | micro-entity |
| total_assets_less_current_liabilities | 66915 | GBP | 2022-11-30 | 2024-02-17 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## HIGH PRESSURE SERVICES LIMITED (`gb:07448741`)

- registration: `07448741` (GB), status active, incorporated 2010-11-23
- classification: ['71129'] (sic_2007)
- records: 2 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 52 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2024-03-31 | 2024-07-09 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 0 | GBP | 2024-03-31 | 2024-07-09 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 18268 | GBP | 2024-03-31 | 2024-07-09 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 18268 | GBP | 2024-03-31 | 2024-07-09 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-03-31 | 2024-07-09 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -1752 | GBP | 2024-03-31 | 2024-07-09 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 203 | GBP | 2024-03-31 | 2024-07-09 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | -1750 | GBP | 2024-03-31 | 2024-07-09 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 13096 | GBP | 2024-03-31 | 2024-07-09 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 13299 | GBP | 2024-03-31 | 2024-07-09 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-03-31 | 2024-07-09 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2023-03-31 | 2023-12-07 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 2808 | GBP | 2023-03-31 | 2023-12-07 | filed | no | `frs-core:CashBankOnHand` | total-exemption-full |
| cash | 2808 | GBP | 2023-03-31 | 2024-07-09 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 25959 | GBP | 2023-03-31 | 2023-12-07 | filed | no | `frs-core:CurrentAssets` | total-exemption-full |
| current_assets | 25959 | GBP | 2023-03-31 | 2024-07-09 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 23151 | GBP | 2023-03-31 | 2023-12-07 | filed | no | `frs-core:Debtors` | total-exemption-full |
| debtors | 23151 | GBP | 2023-03-31 | 2024-07-09 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -865 | GBP | 2023-03-31 | 2024-07-09 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-03-31 | 2024-07-09 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -865 | GBP | 2023-03-31 | 2023-12-07 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-03-31 | 2023-12-07 | filed | no | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 271 | GBP | 2023-03-31 | 2023-12-07 | filed | no | `frs-core:FixedAssets` | total-exemption-full |
| fixed_assets | 271 | GBP | 2023-03-31 | 2024-07-09 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | -863 | GBP | 2023-03-31 | 2023-12-07 | filed | no | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | -863 | GBP | 2023-03-31 | 2024-07-09 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 16264 | GBP | 2023-03-31 | 2024-07-09 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 16264 | GBP | 2023-03-31 | 2023-12-07 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 16535 | GBP | 2023-03-31 | 2023-12-07 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 16535 | GBP | 2023-03-31 | 2024-07-09 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2022-03-31 | 2022-12-21 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2022-03-31 | 2023-12-07 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 2808 | GBP | 2022-03-31 | 2023-12-07 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| cash | 2808 | GBP | 2022-03-31 | 2022-12-21 | filed | no | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 37843 | GBP | 2022-03-31 | 2023-12-07 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| current_assets | 37843 | GBP | 2022-03-31 | 2022-12-21 | filed | no | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 35035 | GBP | 2022-03-31 | 2023-12-07 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| debtors | 35035 | GBP | 2022-03-31 | 2022-12-21 | filed | no | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2022-03-31 | 2023-12-07 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2022-03-31 | 2022-12-21 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 87 | GBP | 2022-03-31 | 2022-12-21 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 87 | GBP | 2022-03-31 | 2023-12-07 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 361 | GBP | 2022-03-31 | 2023-12-07 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| fixed_assets | 361 | GBP | 2022-03-31 | 2022-12-21 | filed | no | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 89 | GBP | 2022-03-31 | 2023-12-07 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 89 | GBP | 2022-03-31 | 2022-12-21 | filed | no | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -272 | GBP | 2022-03-31 | 2022-12-21 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | -272 | GBP | 2022-03-31 | 2023-12-07 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 89 | GBP | 2022-03-31 | 2023-12-07 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 89 | GBP | 2022-03-31 | 2022-12-21 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 2 | xbrli:pure | 2021-03-31 | 2022-12-21 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 7009 | GBP | 2021-03-31 | 2022-12-21 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 51763 | GBP | 2021-03-31 | 2022-12-21 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 44754 | GBP | 2021-03-31 | 2022-12-21 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2 | GBP | 2021-03-31 | 2022-12-21 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2021-03-31 | 2022-12-21 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 480 | GBP | 2021-03-31 | 2022-12-21 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 4 | GBP | 2021-03-31 | 2022-12-21 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -476 | GBP | 2021-03-31 | 2022-12-21 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 4 | GBP | 2021-03-31 | 2022-12-21 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._
