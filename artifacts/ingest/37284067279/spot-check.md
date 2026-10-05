# Ingest spot-check

- database: `data/engine.db`
- latest run: `20261005T083142Z-fbe469a5`
- companies in store: 19400; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## QUANTUS SERVICES LIMITED (`gb:02023293`)

- registration: `02023293` (GB), status active, incorporated 1986-05-28
- classification: ['71129'] (sic_2007)
- records: 2 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 99 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.02 | xbrli:pure | 2025-05-31 | 2026-01-26 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 67575 | GBP | 2025-05-31 | 2026-01-26 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 145392 | GBP | 2025-05-31 | 2026-01-26 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| equity | 803427 | GBP | 2025-05-31 | 2026-01-26 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 726525 | GBP | 2025-05-31 | 2026-01-26 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | 803427 | GBP | 2025-05-31 | 2026-01-26 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 78002 | GBP | 2025-05-31 | 2026-01-26 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 804527 | GBP | 2025-05-31 | 2026-01-26 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0.01 | xbrli:pure | 2024-05-31 | 2026-01-26 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-05-31 | 2025-02-11 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 10572 | GBP | 2024-05-31 | 2026-01-26 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 10572 | GBP | 2024-05-31 | 2025-02-11 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 208391 | GBP | 2024-05-31 | 2026-01-26 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 208391 | GBP | 2024-05-31 | 2025-02-11 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 815712 | GBP | 2024-05-31 | 2025-02-11 | filed | no | `core:Equity` | micro-entity |
| equity | 815712 | GBP | 2024-05-31 | 2026-01-26 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 726525 | GBP | 2024-05-31 | 2026-01-26 | filed | yes | `core:FixedAssets` | total-exemption-full |
| fixed_assets | 726525 | GBP | 2024-05-31 | 2025-02-11 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | 815712 | GBP | 2024-05-31 | 2026-01-26 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 197819 | GBP | 2024-05-31 | 2026-01-26 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 924344 | GBP | 2024-05-31 | 2026-01-26 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-05-31 | 2025-02-11 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-05-31 | 2024-02-26 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 12215 | GBP | 2023-05-31 | 2025-02-11 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 12215 | GBP | 2023-05-31 | 2024-02-26 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 184267 | GBP | 2023-05-31 | 2024-02-26 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 184267 | GBP | 2023-05-31 | 2025-02-11 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 780090 | GBP | 2023-05-31 | 2025-02-11 | filed | yes | `core:Equity` | micro-entity |
| equity | 780090 | GBP | 2023-05-31 | 2024-02-26 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 726525 | GBP | 2023-05-31 | 2025-02-11 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 726525 | GBP | 2023-05-31 | 2024-02-26 | filed | no | `core:FixedAssets` | micro-entity |
| average_employees | 1 | xbrli:pure | 2022-05-31 | 2024-02-26 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 11148 | GBP | 2022-05-31 | 2024-02-26 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 155137 | GBP | 2022-05-31 | 2024-02-26 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 738522 | GBP | 2022-05-31 | 2024-02-26 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 726525 | GBP | 2022-05-31 | 2024-02-26 | filed | yes | `core:FixedAssets` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2026-01-26: `{"superseded_document_id": "gb:02023293:doc:PU8qllvJPDHFdnvOVpMzkROukQEYt6S13CRMSwmExl8", "restatements": [{"concept": "average_employees", "period_end": "2024-05-31", "old_value": "1.0000", "new_valu`

## M & M INTERNATIONAL (U.K.) LIMITED (`gb:02547501`)

- registration: `02547501` (GB), status active, incorporated 1990-10-10
- classification: ['71129'] (sic_2007)
- records: 9 officers, 2 beneficial owners, 0 ownership statements, 1 security interests, 116 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 6 | xbrli:pure | 2025-12-31 | 2026-04-20 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 52386 | GBP | 2025-12-31 | 2026-04-20 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 54222 | GBP | 2025-12-31 | 2026-04-20 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 252014 | GBP | 2025-12-31 | 2026-04-20 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 65673 | GBP | 2025-12-31 | 2026-04-20 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 212644 | GBP | 2025-12-31 | 2026-04-20 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 22581 | GBP | 2025-12-31 | 2026-04-20 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 190063 | GBP | 2025-12-31 | 2026-04-20 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 212644 | GBP | 2025-12-31 | 2026-04-20 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 197792 | GBP | 2025-12-31 | 2026-04-20 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 214803 | GBP | 2025-12-31 | 2026-04-20 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 6 | xbrli:pure | 2024-12-31 | 2025-04-25 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 6 | xbrli:pure | 2024-12-31 | 2026-04-20 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 59591 | GBP | 2024-12-31 | 2026-04-20 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 59591 | GBP | 2024-12-31 | 2025-04-25 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 49694 | GBP | 2024-12-31 | 2025-04-25 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 49694 | GBP | 2024-12-31 | 2026-04-20 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 243170 | GBP | 2024-12-31 | 2026-04-20 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 243170 | GBP | 2024-12-31 | 2025-04-25 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors | 45211 | GBP | 2024-12-31 | 2025-04-25 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 45211 | GBP | 2024-12-31 | 2026-04-20 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 189424 | GBP | 2024-12-31 | 2026-04-20 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 22581 | GBP | 2024-12-31 | 2025-04-25 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 22581 | GBP | 2024-12-31 | 2026-04-20 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 212005 | GBP | 2024-12-31 | 2026-04-20 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 189424 | GBP | 2024-12-31 | 2025-04-25 | filed | no | `core:Equity` | total-exemption-full |
| equity | 212005 | GBP | 2024-12-31 | 2025-04-25 | filed | no | `core:Equity` | total-exemption-full |
| net_assets | 212005 | GBP | 2024-12-31 | 2025-04-25 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 212005 | GBP | 2024-12-31 | 2026-04-20 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 193476 | GBP | 2024-12-31 | 2025-04-25 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 193476 | GBP | 2024-12-31 | 2026-04-20 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 214692 | GBP | 2024-12-31 | 2026-04-20 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 214692 | GBP | 2024-12-31 | 2025-04-25 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 7 | xbrli:pure | 2023-12-31 | 2025-04-25 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 7 | xbrli:pure | 2023-12-31 | 2024-04-27 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 109098 | GBP | 2023-12-31 | 2025-04-25 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 109098 | GBP | 2023-12-31 | 2024-04-27 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 175101 | GBP | 2023-12-31 | 2025-04-25 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 175101 | GBP | 2023-12-31 | 2024-04-27 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 352513 | GBP | 2023-12-31 | 2024-04-27 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 352513 | GBP | 2023-12-31 | 2025-04-25 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 63564 | GBP | 2023-12-31 | 2025-04-25 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 63564 | GBP | 2023-12-31 | 2024-04-27 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 176422 | GBP | 2023-12-31 | 2025-04-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 176422 | GBP | 2023-12-31 | 2024-04-27 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 22581 | GBP | 2023-12-31 | 2025-04-25 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 199003 | GBP | 2023-12-31 | 2024-04-27 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 22581 | GBP | 2023-12-31 | 2024-04-27 | filed | no | `core:Equity` | total-exemption-full |
| equity | 199003 | GBP | 2023-12-31 | 2025-04-25 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 199003 | GBP | 2023-12-31 | 2024-04-27 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 199003 | GBP | 2023-12-31 | 2025-04-25 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 177412 | GBP | 2023-12-31 | 2024-04-27 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 177412 | GBP | 2023-12-31 | 2025-04-25 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 201838 | GBP | 2023-12-31 | 2025-04-25 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 201838 | GBP | 2023-12-31 | 2024-04-27 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 7 | xbrli:pure | 2022-12-31 | 2024-04-27 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 81808 | GBP | 2022-12-31 | 2024-04-27 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 143993 | GBP | 2022-12-31 | 2024-04-27 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 319436 | GBP | 2022-12-31 | 2024-04-27 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 68731 | GBP | 2022-12-31 | 2024-04-27 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 22581 | GBP | 2022-12-31 | 2024-04-27 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 186869 | GBP | 2022-12-31 | 2024-04-27 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 164288 | GBP | 2022-12-31 | 2024-04-27 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 186869 | GBP | 2022-12-31 | 2024-04-27 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 175443 | GBP | 2022-12-31 | 2024-04-27 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 189550 | GBP | 2022-12-31 | 2024-04-27 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## WARRINGAH FIELD & COUNTRY LTD (`gb:02920741`)

- registration: `02920741` (GB), status active, incorporated 1994-04-20
- classification: ['01700', '62090', '70221'] (sic_2007)
- records: 2 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 69 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | xbrli:pure | 2025-04-30 | 2025-11-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 529 | GBP | 2025-04-30 | 2025-11-30 | filed | yes | `core:CashBankOnHand` | unaudited-abridged |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 215511 | GBP | 2025-04-30 | 2025-11-30 | filed | yes | `core:Creditors` | unaudited-abridged |
| current_assets | 1292 | GBP | 2025-04-30 | 2025-11-30 | filed | yes | `core:CurrentAssets` | unaudited-abridged |
| debtors | 763 | GBP | 2025-04-30 | 2025-11-30 | filed | yes | `core:Debtors` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2025-04-30 | 2025-11-30 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -202902 | GBP | 2025-04-30 | 2025-11-30 | filed | yes | `core:Equity` | unaudited-abridged |
| equity | -202900 | GBP | 2025-04-30 | 2025-11-30 | filed | yes | `core:Equity` | unaudited-abridged |
| fixed_assets | 11319 | GBP | 2025-04-30 | 2025-11-30 | filed | yes | `core:FixedAssets` | unaudited-abridged |
| gross_profit | 0 | GBP | 2025-04-30 | 2025-11-30 | filed | yes | `core:GrossProfitLoss` | unaudited-abridged |
| net_assets | -202900 | GBP | 2025-04-30 | 2025-11-30 | filed | yes | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 1292 | GBP | 2025-04-30 | 2025-11-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| operating_profit | -10406 | GBP | 2025-04-30 | 2025-11-30 | filed | yes | `core:OperatingProfitLoss` | unaudited-abridged |
| profit_before_tax | -10502 | GBP | 2025-04-30 | 2025-11-30 | filed | yes | `core:ProfitLossOnOrdinaryActivitiesBeforeTax` | unaudited-abridged |
| profit_for_period | -10502 | GBP | 2025-04-30 | 2025-11-30 | filed | yes | `core:ProfitLoss` | unaudited-abridged |
| total_assets_less_current_liabilities | 12611 | GBP | 2025-04-30 | 2025-11-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 0 | xbrli:pure | 2024-04-30 | 2025-11-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| average_employees | 0 | xbrli:pure | 2024-04-30 | 2024-12-30 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 1197 | GBP | 2024-04-30 | 2025-11-30 | filed | yes | `core:CashBankOnHand` | unaudited-abridged |
| cash | 1197 | GBP | 2024-04-30 | 2024-12-30 | filed | no | `core:CashBankOnHand` | unaudited-abridged |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 208942 | GBP | 2024-04-30 | 2025-11-30 | filed | yes | `core:Creditors` | unaudited-abridged |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 208942 | GBP | 2024-04-30 | 2024-12-30 | filed | no | `core:Creditors` | unaudited-abridged |
| current_assets | 1453 | GBP | 2024-04-30 | 2024-12-30 | filed | no | `core:CurrentAssets` | unaudited-abridged |
| current_assets | 1453 | GBP | 2024-04-30 | 2025-11-30 | filed | yes | `core:CurrentAssets` | unaudited-abridged |
| debtors | 256 | GBP | 2024-04-30 | 2024-12-30 | filed | no | `core:Debtors` | unaudited-abridged |
| debtors | 256 | GBP | 2024-04-30 | 2025-11-30 | filed | yes | `core:Debtors` | unaudited-abridged |
| equity | -192398 | GBP | 2024-04-30 | 2024-12-30 | filed | no | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -192400 | GBP | 2024-04-30 | 2024-12-30 | filed | no | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-04-30 | 2025-11-30 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-04-30 | 2024-12-30 | filed | no | `core:Equity` | unaudited-abridged |
| equity | -192398 | GBP | 2024-04-30 | 2025-11-30 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -192400 | GBP | 2024-04-30 | 2025-11-30 | filed | yes | `core:Equity` | unaudited-abridged |
| fixed_assets | 15091 | GBP | 2024-04-30 | 2025-11-30 | filed | yes | `core:FixedAssets` | unaudited-abridged |
| fixed_assets | 15091 | GBP | 2024-04-30 | 2024-12-30 | filed | no | `core:FixedAssets` | unaudited-abridged |
| gross_profit | 0 | GBP | 2024-04-30 | 2025-11-30 | filed | yes | `core:GrossProfitLoss` | unaudited-abridged |
| gross_profit | 0 | GBP | 2024-04-30 | 2024-12-30 | filed | no | `core:GrossProfitLoss` | unaudited-abridged |
| net_assets | -192398 | GBP | 2024-04-30 | 2024-12-30 | filed | no | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_assets | -192398 | GBP | 2024-04-30 | 2025-11-30 | filed | yes | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 1453 | GBP | 2024-04-30 | 2025-11-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| net_current_assets | 1453 | GBP | 2024-04-30 | 2024-12-30 | filed | no | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| operating_profit | -12682 | GBP | 2024-04-30 | 2024-12-30 | filed | no | `core:OperatingProfitLoss` | unaudited-abridged |
| operating_profit | -12682 | GBP | 2024-04-30 | 2025-11-30 | filed | yes | `core:OperatingProfitLoss` | unaudited-abridged |
| profit_before_tax | -12778 | GBP | 2024-04-30 | 2025-11-30 | filed | yes | `core:ProfitLossOnOrdinaryActivitiesBeforeTax` | unaudited-abridged |
| profit_before_tax | -12778 | GBP | 2024-04-30 | 2024-12-30 | filed | no | `core:ProfitLossOnOrdinaryActivitiesBeforeTax` | unaudited-abridged |
| profit_for_period | -12778 | GBP | 2024-04-30 | 2025-11-30 | filed | yes | `core:ProfitLoss` | unaudited-abridged |
| profit_for_period | -12778 | GBP | 2024-04-30 | 2024-12-30 | filed | no | `core:ProfitLoss` | unaudited-abridged |
| total_assets_less_current_liabilities | 16544 | GBP | 2024-04-30 | 2024-12-30 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 16544 | GBP | 2024-04-30 | 2025-11-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 0 | xbrli:pure | 2023-04-30 | 2024-12-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| average_employees | 0 | xbrli:pure | 2023-04-30 | 2024-01-01 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 6537 | GBP | 2023-04-30 | 2024-01-01 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 6537 | GBP | 2023-04-30 | 2024-12-30 | filed | yes | `core:CashBankOnHand` | unaudited-abridged |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 206604 | GBP | 2023-04-30 | 2024-01-01 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 206604 | GBP | 2023-04-30 | 2024-12-30 | filed | yes | `core:Creditors` | unaudited-abridged |
| current_assets | 6862 | GBP | 2023-04-30 | 2024-01-01 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 6862 | GBP | 2023-04-30 | 2024-12-30 | filed | yes | `core:CurrentAssets` | unaudited-abridged |
| debtors | 325 | GBP | 2023-04-30 | 2024-01-01 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 325 | GBP | 2023-04-30 | 2024-12-30 | filed | yes | `core:Debtors` | unaudited-abridged |
| equity | -179620 | GBP | 2023-04-30 | 2024-01-01 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-04-30 | 2024-12-30 | filed | yes | `core:Equity` | unaudited-abridged |
| equity | -179620 | GBP | 2023-04-30 | 2024-12-30 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -179622 | GBP | 2023-04-30 | 2024-01-01 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -179622 | GBP | 2023-04-30 | 2024-12-30 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-04-30 | 2024-01-01 | filed | no | `core:Equity` | total-exemption-full |
| fixed_assets | 20122 | GBP | 2023-04-30 | 2024-12-30 | filed | yes | `core:FixedAssets` | unaudited-abridged |
| fixed_assets | 20122 | GBP | 2023-04-30 | 2024-01-01 | filed | no | `core:FixedAssets` | total-exemption-full |
| gross_profit | 0 | GBP | 2023-04-30 | 2024-12-30 | filed | yes | `core:GrossProfitLoss` | unaudited-abridged |
| gross_profit | 0 | GBP | 2023-04-30 | 2024-01-01 | filed | no | `core:GrossProfitLoss` | total-exemption-full |
| net_assets | -179620 | GBP | 2023-04-30 | 2024-12-30 | filed | yes | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_assets | -179620 | GBP | 2023-04-30 | 2024-01-01 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 6862 | GBP | 2023-04-30 | 2024-01-01 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 6862 | GBP | 2023-04-30 | 2024-12-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| operating_profit | -13212 | GBP | 2023-04-30 | 2024-12-30 | filed | yes | `core:OperatingProfitLoss` | unaudited-abridged |
| operating_profit | -13212 | GBP | 2023-04-30 | 2024-01-01 | filed | no | `core:OperatingProfitLoss` | total-exemption-full |
| profit_before_tax | -13302 | GBP | 2023-04-30 | 2024-01-01 | filed | no | `core:ProfitLossOnOrdinaryActivitiesBeforeTax` | total-exemption-full |
| profit_before_tax | -13302 | GBP | 2023-04-30 | 2024-12-30 | filed | yes | `core:ProfitLossOnOrdinaryActivitiesBeforeTax` | unaudited-abridged |
| profit_for_period | -13302 | GBP | 2023-04-30 | 2024-12-30 | filed | yes | `core:ProfitLoss` | unaudited-abridged |
| profit_for_period | -13302 | GBP | 2023-04-30 | 2024-01-01 | filed | no | `core:ProfitLoss` | total-exemption-full |
| revenue | 0 | GBP | 2023-04-30 | 2024-01-01 | filed | yes | `core:TurnoverRevenue` | total-exemption-full |
| total_assets_less_current_liabilities | 26984 | GBP | 2023-04-30 | 2024-12-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 26984 | GBP | 2023-04-30 | 2024-01-01 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0 | xbrli:pure | 2022-04-30 | 2024-01-01 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 429 | GBP | 2022-04-30 | 2024-01-01 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 168754 | GBP | 2022-04-30 | 2024-01-01 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 559 | GBP | 2022-04-30 | 2024-01-01 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 130 | GBP | 2022-04-30 | 2024-01-01 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | -166318 | GBP | 2022-04-30 | 2024-01-01 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -166320 | GBP | 2022-04-30 | 2024-01-01 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2022-04-30 | 2024-01-01 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 1877 | GBP | 2022-04-30 | 2024-01-01 | filed | yes | `core:FixedAssets` | total-exemption-full |
| gross_profit | 0 | GBP | 2022-04-30 | 2024-01-01 | filed | yes | `core:GrossProfitLoss` | total-exemption-full |
| net_assets | -166318 | GBP | 2022-04-30 | 2024-01-01 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 559 | GBP | 2022-04-30 | 2024-01-01 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| operating_profit | -5053 | GBP | 2022-04-30 | 2024-01-01 | filed | yes | `core:OperatingProfitLoss` | total-exemption-full |
| profit_before_tax | -5143 | GBP | 2022-04-30 | 2024-01-01 | filed | yes | `core:ProfitLossOnOrdinaryActivitiesBeforeTax` | total-exemption-full |
| profit_for_period | -5143 | GBP | 2022-04-30 | 2024-01-01 | filed | yes | `core:ProfitLoss` | total-exemption-full |
| revenue | 0 | GBP | 2022-04-30 | 2024-01-01 | filed | yes | `core:TurnoverRevenue` | total-exemption-full |
| total_assets_less_current_liabilities | 2436 | GBP | 2022-04-30 | 2024-01-01 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## THERMAX EUROPE LIMITED (`gb:03183441`)

- registration: `03183441` (GB), status active, incorporated 1996-04-09
- classification: ['71129'] (sic_2007)
- records: 18 officers, 3 beneficial owners, 1 ownership statements, 3 security interests, 119 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 8 | xbrli:pure | 2026-03-31 | 2026-06-01 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | full |
| cash | 7178389 | GBP | 2026-03-31 | 2026-06-01 | filed | yes | `ns5:CashBankOnHand` | full |
| current_assets | 8458414 | GBP | 2026-03-31 | 2026-06-01 | filed | yes | `ns5:CurrentAssets` | full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 857947 | GBP | 2026-03-31 | 2026-06-01 | filed | yes | `ns5:Debtors` | full |
| debtors | 857947 | GBP | 2026-03-31 | 2026-06-01 | filed | yes | `ns5:Debtors` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200000 | GBP | 2026-03-31 | 2026-06-01 | filed | yes | `ns5:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 7176475 | GBP | 2026-03-31 | 2026-06-01 | filed | yes | `ns5:Equity` | full |
| equity | 7376475 | GBP | 2026-03-31 | 2026-06-01 | filed | yes | `ns5:Equity` | full |
| gross_profit | 1195729 | GBP | 2026-03-31 | 2026-06-01 | filed | yes | `ns5:GrossProfitLoss` | full |
| net_assets | 7376475 | GBP | 2026-03-31 | 2026-06-01 | filed | yes | `ns5:NetAssetsLiabilities` | full |
| net_current_assets | 7374575 | GBP | 2026-03-31 | 2026-06-01 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | full |
| operating_profit | 368878 | GBP | 2026-03-31 | 2026-06-01 | filed | yes | `ns5:OperatingProfitLoss` | full |
| profit_before_tax | 554190 | GBP | 2026-03-31 | 2026-06-01 | filed | yes | `ns5:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 412271 | GBP | 2026-03-31 | 2026-06-01 | filed | yes | `ns5:ProfitLoss` | full |
| profit_for_period | 412271 | GBP | 2026-03-31 | 2026-06-01 | filed | yes | `ns5:ProfitLoss` | full |
| revenue `{'GeographicSegmentsDimension': 'UnitedKingdom'}` | 588570 | GBP | 2026-03-31 | 2026-06-01 | filed | yes | `ns5:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'Europe'}` | 4699778 | GBP | 2026-03-31 | 2026-06-01 | filed | yes | `ns5:TurnoverRevenue` | full |
| revenue | 5310196 | GBP | 2026-03-31 | 2026-06-01 | filed | yes | `ns5:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'TotalGeographicSegmentsIncludingAnyUnallocatedAmount'}` | 5310196 | GBP | 2026-03-31 | 2026-06-01 | filed | yes | `ns5:TurnoverRevenue` | full |
| staff_costs | 387163 | GBP | 2026-03-31 | 2026-06-01 | filed | yes | `ns5:StaffCostsEmployeeBenefitsExpense` | full |
| tax_charge | 141919 | GBP | 2026-03-31 | 2026-06-01 | filed | yes | `ns5:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| total_assets_less_current_liabilities | 7377108 | GBP | 2026-03-31 | 2026-06-01 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | full |
| average_employees | 7 | xbrli:pure | 2025-03-31 | 2026-06-01 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | full |
| average_employees | 7 | xbrli:pure | 2025-03-31 | 2025-06-26 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | full |
| cash | 6210331 | GBP | 2025-03-31 | 2025-06-26 | filed | no | `ns5:CashBankOnHand` | full |
| cash | 6210331 | GBP | 2025-03-31 | 2026-06-01 | filed | yes | `ns5:CashBankOnHand` | full |
| current_assets | 9874379 | GBP | 2025-03-31 | 2026-06-01 | filed | yes | `ns5:CurrentAssets` | full |
| current_assets | 9874379 | GBP | 2025-03-31 | 2025-06-26 | filed | no | `ns5:CurrentAssets` | full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 2539972 | GBP | 2025-03-31 | 2025-06-26 | filed | no | `ns5:Debtors` | full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 2539972 | GBP | 2025-03-31 | 2026-06-01 | filed | yes | `ns5:Debtors` | full |
| debtors | 2539972 | GBP | 2025-03-31 | 2026-06-01 | filed | yes | `ns5:Debtors` | full |
| debtors | 2539972 | GBP | 2025-03-31 | 2025-06-26 | filed | no | `ns5:Debtors` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200000 | GBP | 2025-03-31 | 2026-06-01 | filed | yes | `ns5:Equity` | full |
| equity | 6964204 | GBP | 2025-03-31 | 2025-06-26 | filed | no | `ns5:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 6764204 | GBP | 2025-03-31 | 2026-06-01 | filed | yes | `ns5:Equity` | full |
| equity | 6964204 | GBP | 2025-03-31 | 2026-06-01 | filed | yes | `ns5:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 6764204 | GBP | 2025-03-31 | 2025-06-26 | filed | no | `ns5:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200000 | GBP | 2025-03-31 | 2025-06-26 | filed | no | `ns5:Equity` | full |
| gross_profit | 1007877 | GBP | 2025-03-31 | 2026-06-01 | filed | yes | `ns5:GrossProfitLoss` | full |
| gross_profit | 1007877 | GBP | 2025-03-31 | 2025-06-26 | filed | no | `ns5:GrossProfitLoss` | full |
| net_assets | 6964204 | GBP | 2025-03-31 | 2026-06-01 | filed | yes | `ns5:NetAssetsLiabilities` | full |
| net_assets | 6964204 | GBP | 2025-03-31 | 2025-06-26 | filed | no | `ns5:NetAssetsLiabilities` | full |
| net_current_assets | 6961473 | GBP | 2025-03-31 | 2026-06-01 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | full |
| net_current_assets | 6961473 | GBP | 2025-03-31 | 2025-06-26 | filed | no | `ns5:NetCurrentAssetsLiabilities` | full |
| operating_profit | -48873 | GBP | 2025-03-31 | 2025-06-26 | filed | no | `ns5:OperatingProfitLoss` | full |
| operating_profit | -48873 | GBP | 2025-03-31 | 2026-06-01 | filed | yes | `ns5:OperatingProfitLoss` | full |
| profit_before_tax | 152220 | GBP | 2025-03-31 | 2025-06-26 | filed | no | `ns5:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_before_tax | 152220 | GBP | 2025-03-31 | 2026-06-01 | filed | yes | `ns5:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 117265 | GBP | 2025-03-31 | 2025-06-26 | filed | yes | `ns5:ProfitLoss` | full |
| profit_for_period | 117265 | GBP | 2025-03-31 | 2025-06-26 | filed | no | `ns5:ProfitLoss` | full |
| profit_for_period | 117265 | GBP | 2025-03-31 | 2026-06-01 | filed | yes | `ns5:ProfitLoss` | full |
| revenue | 3789971 | GBP | 2025-03-31 | 2026-06-01 | filed | yes | `ns5:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'Europe'}` | 2411432 | GBP | 2025-03-31 | 2025-06-26 | filed | no | `ns5:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'Europe'}` | 2411432 | GBP | 2025-03-31 | 2026-06-01 | filed | yes | `ns5:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'UnitedKingdom'}` | 351781 | GBP | 2025-03-31 | 2026-06-01 | filed | yes | `ns5:TurnoverRevenue` | full |
| revenue | 3789971 | GBP | 2025-03-31 | 2025-06-26 | filed | no | `ns5:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'TotalGeographicSegmentsIncludingAnyUnallocatedAmount'}` | 3789971 | GBP | 2025-03-31 | 2025-06-26 | filed | no | `ns5:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'UnitedKingdom'}` | 351781 | GBP | 2025-03-31 | 2025-06-26 | filed | no | `ns5:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'TotalGeographicSegmentsIncludingAnyUnallocatedAmount'}` | 3789971 | GBP | 2025-03-31 | 2026-06-01 | filed | yes | `ns5:TurnoverRevenue` | full |
| staff_costs | 336843 | GBP | 2025-03-31 | 2025-06-26 | filed | no | `ns5:StaffCostsEmployeeBenefitsExpense` | full |
| staff_costs | 336843 | GBP | 2025-03-31 | 2026-06-01 | filed | yes | `ns5:StaffCostsEmployeeBenefitsExpense` | full |
| tax_charge | 34955 | GBP | 2025-03-31 | 2026-06-01 | filed | yes | `ns5:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| tax_charge | 34955 | GBP | 2025-03-31 | 2025-06-26 | filed | no | `ns5:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| total_assets_less_current_liabilities | 6965131 | GBP | 2025-03-31 | 2025-06-26 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | full |
| total_assets_less_current_liabilities | 6965131 | GBP | 2025-03-31 | 2026-06-01 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | full |
| average_employees | 8 | xbrli:pure | 2024-03-31 | 2024-06-04 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | full |
| average_employees | 8 | xbrli:pure | 2024-03-31 | 2025-06-26 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | full |
| cash | 5642586 | GBP | 2024-03-31 | 2025-06-26 | filed | yes | `ns5:CashBankOnHand` | full |
| cash | 5642586 | GBP | 2024-03-31 | 2024-06-04 | filed | no | `ns5:CashBankOnHand` | full |
| current_assets | 7452585 | GBP | 2024-03-31 | 2024-06-04 | filed | no | `ns5:CurrentAssets` | full |
| current_assets | 7452585 | GBP | 2024-03-31 | 2025-06-26 | filed | yes | `ns5:CurrentAssets` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1727030 | GBP | 2024-03-31 | 2024-06-04 | filed | no | `ns5:Debtors` | full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 1727030 | GBP | 2024-03-31 | 2025-06-26 | filed | yes | `ns5:Debtors` | full |
| debtors | 1727030 | GBP | 2024-03-31 | 2024-06-04 | filed | no | `ns5:Debtors` | full |
| debtors | 1727030 | GBP | 2024-03-31 | 2025-06-26 | filed | yes | `ns5:Debtors` | full |
| equity | 6846939 | GBP | 2024-03-31 | 2024-06-04 | filed | no | `ns5:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200000 | GBP | 2024-03-31 | 2026-06-01 | filed | yes | `ns5:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200000 | GBP | 2024-03-31 | 2025-06-26 | filed | no | `ns5:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 6646939 | GBP | 2024-03-31 | 2025-06-26 | filed | no | `ns5:Equity` | full |
| equity | 6846939 | GBP | 2024-03-31 | 2025-06-26 | filed | no | `ns5:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 6646939 | GBP | 2024-03-31 | 2024-06-04 | filed | no | `ns5:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200000 | GBP | 2024-03-31 | 2024-06-04 | filed | no | `ns5:Equity` | full |
| equity | 6846939 | GBP | 2024-03-31 | 2026-06-01 | filed | yes | `ns5:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 6646939 | GBP | 2024-03-31 | 2026-06-01 | filed | yes | `ns5:Equity` | full |
| gross_profit | 1327552 | GBP | 2024-03-31 | 2025-06-26 | filed | yes | `ns5:GrossProfitLoss` | full |
| gross_profit | 1327552 | GBP | 2024-03-31 | 2024-06-04 | filed | no | `ns5:GrossProfitLoss` | full |
| net_assets | 6846939 | GBP | 2024-03-31 | 2024-06-04 | filed | no | `ns5:NetAssetsLiabilities` | full |
| net_assets | 6846939 | GBP | 2024-03-31 | 2025-06-26 | filed | yes | `ns5:NetAssetsLiabilities` | full |
| net_current_assets | 6841856 | GBP | 2024-03-31 | 2024-06-04 | filed | no | `ns5:NetCurrentAssetsLiabilities` | full |
| net_current_assets | 6841856 | GBP | 2024-03-31 | 2025-06-26 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | full |
| operating_profit | 209740 | GBP | 2024-03-31 | 2025-06-26 | filed | yes | `ns5:OperatingProfitLoss` | full |
| operating_profit | 209740 | GBP | 2024-03-31 | 2024-06-04 | filed | no | `ns5:OperatingProfitLoss` | full |
| profit_before_tax | 344509 | GBP | 2024-03-31 | 2024-06-04 | filed | no | `ns5:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_before_tax | 344509 | GBP | 2024-03-31 | 2025-06-26 | filed | yes | `ns5:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 256220 | GBP | 2024-03-31 | 2024-06-04 | filed | yes | `ns5:ProfitLoss` | full |
| profit_for_period | 256220 | GBP | 2024-03-31 | 2025-06-26 | filed | yes | `ns5:ProfitLoss` | full |
| profit_for_period | 256220 | GBP | 2024-03-31 | 2024-06-04 | filed | no | `ns5:ProfitLoss` | full |
| revenue `{'GeographicSegmentsDimension': 'Europe'}` | 5022246 | GBP | 2024-03-31 | 2025-06-26 | filed | yes | `ns5:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'TotalGeographicSegmentsIncludingAnyUnallocatedAmount'}` | 5755157 | GBP | 2024-03-31 | 2024-06-04 | filed | no | `ns5:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'UnitedKingdom'}` | 732911 | GBP | 2024-03-31 | 2025-06-26 | filed | yes | `ns5:TurnoverRevenue` | full |
| revenue | 5755157 | GBP | 2024-03-31 | 2025-06-26 | filed | yes | `ns5:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'TotalGeographicSegmentsIncludingAnyUnallocatedAmount'}` | 5755157 | GBP | 2024-03-31 | 2025-06-26 | filed | yes | `ns5:TurnoverRevenue` | full |
| revenue | 5755157 | GBP | 2024-03-31 | 2024-06-04 | filed | no | `ns5:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'Europe'}` | 5022246 | GBP | 2024-03-31 | 2024-06-04 | filed | no | `ns5:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'UnitedKingdom'}` | 732911 | GBP | 2024-03-31 | 2024-06-04 | filed | no | `ns5:TurnoverRevenue` | full |
| staff_costs | 366384 | GBP | 2024-03-31 | 2024-06-04 | filed | no | `ns5:StaffCostsEmployeeBenefitsExpense` | full |
| staff_costs | 366384 | GBP | 2024-03-31 | 2025-06-26 | filed | yes | `ns5:StaffCostsEmployeeBenefitsExpense` | full |
| tax_charge | 88289 | GBP | 2024-03-31 | 2025-06-26 | filed | yes | `ns5:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| tax_charge | 88289 | GBP | 2024-03-31 | 2024-06-04 | filed | no | `ns5:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| total_assets_less_current_liabilities | 6848634 | GBP | 2024-03-31 | 2024-06-04 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | full |
| total_assets_less_current_liabilities | 6848634 | GBP | 2024-03-31 | 2025-06-26 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | full |
| average_employees | 8 | xbrli:pure | 2023-03-31 | 2024-06-04 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | full |
| cash | 2756389 | GBP | 2023-03-31 | 2024-06-04 | filed | yes | `ns5:CashBankOnHand` | full |
| current_assets | 8519388 | GBP | 2023-03-31 | 2024-06-04 | filed | yes | `ns5:CurrentAssets` | full |
| debtors | 4617753 | GBP | 2023-03-31 | 2024-06-04 | filed | yes | `ns5:Debtors` | full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 4617753 | GBP | 2023-03-31 | 2024-06-04 | filed | yes | `ns5:Debtors` | full |
| equity | 6590719 | GBP | 2023-03-31 | 2024-06-04 | filed | no | `ns5:Equity` | full |
| equity | 6590719 | GBP | 2023-03-31 | 2025-06-26 | filed | yes | `ns5:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200000 | GBP | 2023-03-31 | 2025-06-26 | filed | yes | `ns5:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200000 | GBP | 2023-03-31 | 2024-06-04 | filed | no | `ns5:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 6390719 | GBP | 2023-03-31 | 2025-06-26 | filed | yes | `ns5:Equity` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 6390719 | GBP | 2023-03-31 | 2024-06-04 | filed | no | `ns5:Equity` | full |
| gross_profit | 877145 | GBP | 2023-03-31 | 2024-06-04 | filed | yes | `ns5:GrossProfitLoss` | full |
| net_assets | 6590719 | GBP | 2023-03-31 | 2024-06-04 | filed | yes | `ns5:NetAssetsLiabilities` | full |
| net_current_assets | 6584898 | GBP | 2023-03-31 | 2024-06-04 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | full |
| operating_profit | 247439 | GBP | 2023-03-31 | 2024-06-04 | filed | yes | `ns5:OperatingProfitLoss` | full |
| profit_before_tax | 301710 | GBP | 2023-03-31 | 2024-06-04 | filed | yes | `ns5:ProfitLossOnOrdinaryActivitiesBeforeTax` | full |
| profit_for_period | 244151 | GBP | 2023-03-31 | 2024-06-04 | filed | yes | `ns5:ProfitLoss` | full |
| revenue `{'GeographicSegmentsDimension': 'TotalGeographicSegmentsIncludingAnyUnallocatedAmount'}` | 6113102 | GBP | 2023-03-31 | 2024-06-04 | filed | yes | `ns5:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'Europe'}` | 4597740 | GBP | 2023-03-31 | 2024-06-04 | filed | yes | `ns5:TurnoverRevenue` | full |
| revenue `{'GeographicSegmentsDimension': 'UnitedKingdom'}` | 1268213 | GBP | 2023-03-31 | 2024-06-04 | filed | yes | `ns5:TurnoverRevenue` | full |
| revenue | 6113102 | GBP | 2023-03-31 | 2024-06-04 | filed | yes | `ns5:TurnoverRevenue` | full |
| staff_costs | 366103 | GBP | 2023-03-31 | 2024-06-04 | filed | yes | `ns5:StaffCostsEmployeeBenefitsExpense` | full |
| tax_charge | 57559 | GBP | 2023-03-31 | 2024-06-04 | filed | yes | `ns5:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | full |
| total_assets_less_current_liabilities | 6592660 | GBP | 2023-03-31 | 2024-06-04 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 6146568 | GBP | 2022-03-31 | 2024-06-04 | filed | yes | `ns5:Equity` | full |
| equity | 6346568 | GBP | 2022-03-31 | 2024-06-04 | filed | yes | `ns5:Equity` | full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 200000 | GBP | 2022-03-31 | 2024-06-04 | filed | yes | `ns5:Equity` | full |

_No coverage facts for the latest run._

## LONGTHORPE ASSOCIATES LTD (`gb:03420775`)

- registration: `03420775` (GB), status active, incorporated 1997-08-18
- classification: ['71129'] (sic_2007)
- records: 5 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 72 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | iso4217:GBP | 2025-08-31 | 2026-03-17 | filed | yes | `pt:AverageNumberEmployeesDuringPeriod` | micro-entity |
| net_assets | 1697 | GBP | 2025-08-31 | 2026-03-17 | filed | yes | `pt:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 1573 | GBP | 2025-08-31 | 2026-03-17 | filed | yes | `pt:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 2383 | GBP | 2025-08-31 | 2026-03-17 | filed | yes | `pt:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-08-31 | 2025-02-27 | filed | yes | `pt:AverageNumberEmployeesDuringPeriod` | micro-entity |
| net_assets | 2817 | GBP | 2024-08-31 | 2026-03-17 | filed | yes | `pt:NetAssetsLiabilities` | micro-entity |
| net_assets | 2817 | GBP | 2024-08-31 | 2025-02-27 | filed | no | `pt:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 2397 | GBP | 2024-08-31 | 2025-02-27 | filed | yes | `pt:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 3477 | GBP | 2024-08-31 | 2025-02-27 | filed | no | `pt:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 3477 | GBP | 2024-08-31 | 2026-03-17 | filed | yes | `pt:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-08-31 | 2024-01-16 | filed | yes | `pt:AverageNumberEmployeesDuringPeriod` | micro-entity |
| net_assets | 3860 | GBP | 2023-08-31 | 2025-02-27 | filed | yes | `pt:NetAssetsLiabilities` | micro-entity |
| net_assets | 3860 | GBP | 2023-08-31 | 2024-01-16 | filed | no | `pt:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 3080 | GBP | 2023-08-31 | 2024-01-16 | filed | yes | `pt:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 4520 | GBP | 2023-08-31 | 2024-01-16 | filed | no | `pt:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 4520 | GBP | 2023-08-31 | 2025-02-27 | filed | yes | `pt:TotalAssetsLessCurrentLiabilities` | micro-entity |
| net_assets | 2421 | GBP | 2022-08-31 | 2024-01-16 | filed | yes | `pt:NetAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 3051 | GBP | 2022-08-31 | 2024-01-16 | filed | yes | `pt:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## G.D.M. CONSULTANCY LIMITED (`gb:03626801`)

- registration: `03626801` (GB), status active, incorporated 1998-09-04
- classification: ['62020'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 65 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-03-31 | 2025-12-18 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1409 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 2365 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 331 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `core:Equity` | micro-entity |
| net_assets | 331 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 956 | GBP | 2025-03-31 | 2025-12-18 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-03-31 | 2024-12-17 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2024-03-31 | 2025-12-18 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 154 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 154 | GBP | 2024-03-31 | 2024-12-17 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 65 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 65 | GBP | 2024-03-31 | 2024-12-17 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | -239 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `core:Equity` | micro-entity |
| equity | -239 | GBP | 2024-03-31 | 2024-12-17 | filed | no | `core:Equity` | micro-entity |
| net_assets | -239 | GBP | 2024-03-31 | 2024-12-17 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | -239 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -89 | GBP | 2024-03-31 | 2025-12-18 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -89 | GBP | 2024-03-31 | 2024-12-17 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-03-31 | 2023-12-20 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | xbrli:pure | 2023-03-31 | 2024-12-17 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 404 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 404 | GBP | 2023-03-31 | 2024-12-17 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 544 | GBP | 2023-03-31 | 2024-12-17 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 544 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | -85 | GBP | 2023-03-31 | 2024-12-17 | filed | yes | `core:Equity` | micro-entity |
| equity | -85 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `core:Equity` | micro-entity |
| net_assets | -85 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | -85 | GBP | 2023-03-31 | 2024-12-17 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 140 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 140 | GBP | 2023-03-31 | 2024-12-17 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | xbrli:pure | 2022-03-31 | 2023-12-20 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 404 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 625 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | -55 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `core:Equity` | micro-entity |
| net_assets | -55 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 221 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## ORGASMIC LIMITED (`gb:03844011`)

- registration: `03844011` (GB), status active, incorporated 1999-09-17
- classification: ['47910', '62012', '62020'] (sic_2007)
- records: 5 officers, 1 beneficial owners, 0 ownership statements, 2 security interests, 77 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.01 | xbrli:pure | 2024-12-31 | 2025-09-23 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 5207 | GBP | 2024-12-31 | 2025-09-23 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| current_assets | 514511 | GBP | 2024-12-31 | 2025-09-23 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 509304 | GBP | 2024-12-31 | 2025-09-23 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | -2512245 | GBP | 2024-12-31 | 2025-09-23 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -2512246 | GBP | 2024-12-31 | 2025-09-23 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2024-12-31 | 2025-09-23 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 1 | GBP | 2024-12-31 | 2025-09-23 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 25305 | GBP | 2024-12-31 | 2025-09-23 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | -2512245 | GBP | 2024-12-31 | 2025-09-23 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 517493 | GBP | 2024-12-31 | 2025-09-23 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 542798 | GBP | 2024-12-31 | 2025-09-23 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 0.01 | xbrli:pure | 2023-12-31 | 2025-09-23 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-12-31 | 2024-09-30 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 8481 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 8481 | GBP | 2023-12-31 | 2025-09-23 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 2912212 | GBP | 2023-12-31 | 2024-09-30 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 13359 | GBP | 2023-12-31 | 2024-09-30 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 511386 | GBP | 2023-12-31 | 2025-09-23 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 511386 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors | 502905 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 502905 | GBP | 2023-12-31 | 2025-09-23 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | -2380527 | GBP | 2023-12-31 | 2025-09-23 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapitalOrdinaryShareClass1'}` | 1 | GBP | 2023-12-31 | 2025-09-23 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2023-12-31 | 2025-09-23 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -2380528 | GBP | 2023-12-31 | 2025-09-23 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:Equity` | total-exemption-full |
| equity | -2380527 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -2380528 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:Equity` | total-exemption-full |
| fixed_assets | 33658 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:FixedAssets` | total-exemption-full |
| fixed_assets | 33658 | GBP | 2023-12-31 | 2025-09-23 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | -2380527 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | -2380527 | GBP | 2023-12-31 | 2025-09-23 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 498027 | GBP | 2023-12-31 | 2025-09-23 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 498027 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 531685 | GBP | 2023-12-31 | 2025-09-23 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 531685 | GBP | 2023-12-31 | 2024-09-30 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2022-12-31 | 2024-09-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 3245 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'Non-currentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 2771296 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 4999 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 507938 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 504693 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -2241530 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity | -2241529 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:Equity` | total-exemption-full |
| fixed_assets | 26828 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:FixedAssets` | total-exemption-full |
| net_assets | -2241529 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 502939 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 529767 | GBP | 2022-12-31 | 2024-09-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

- event restatement @ 2025-09-23: `{"superseded_document_id": "gb:03844011:doc:CMWwpxVHog57juONZFrEZuzcXr27Bnw0pYYkHuXL3Q0", "restatements": [{"concept": "average_employees", "period_end": "2023-12-31", "old_value": "1.0000", "new_valu`

## JASK CONSULTANTS LIMITED (`gb:04055410`)

- registration: `04055410` (GB), status active, incorporated 2000-08-18
- classification: ['62020'] (sic_2007)
- records: 6 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 79 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-03-31 | 2025-12-17 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 57780 | GBP | 2025-03-31 | 2025-12-17 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 62853 | GBP | 2025-03-31 | 2025-12-17 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 5073 | GBP | 2025-03-31 | 2025-12-17 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 56480 | GBP | 2025-03-31 | 2025-12-17 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2025-03-31 | 2025-12-17 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 1939 | GBP | 2025-03-31 | 2025-12-17 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 56482 | GBP | 2025-03-31 | 2025-12-17 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 54912 | GBP | 2025-03-31 | 2025-12-17 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 56851 | GBP | 2025-03-31 | 2025-12-17 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-03-31 | 2025-12-17 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-03-31 | 2024-11-15 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 59094 | GBP | 2024-03-31 | 2024-11-15 | filed | no | `frs-core:CashBankOnHand` | total-exemption-full |
| cash | 59094 | GBP | 2024-03-31 | 2025-12-17 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 152949 | GBP | 2024-03-31 | 2025-12-17 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| current_assets | 152949 | GBP | 2024-03-31 | 2024-11-15 | filed | no | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 93855 | GBP | 2024-03-31 | 2024-11-15 | filed | no | `frs-core:Debtors` | total-exemption-full |
| debtors | 93855 | GBP | 2024-03-31 | 2025-12-17 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 127363 | GBP | 2024-03-31 | 2024-11-15 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-03-31 | 2025-12-17 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 127363 | GBP | 2024-03-31 | 2025-12-17 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2024-03-31 | 2024-11-15 | filed | no | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 2259 | GBP | 2024-03-31 | 2024-11-15 | filed | no | `frs-core:FixedAssets` | total-exemption-full |
| fixed_assets | 2259 | GBP | 2024-03-31 | 2025-12-17 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 127365 | GBP | 2024-03-31 | 2025-12-17 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 127365 | GBP | 2024-03-31 | 2024-11-15 | filed | no | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 125535 | GBP | 2024-03-31 | 2024-11-15 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 125535 | GBP | 2024-03-31 | 2025-12-17 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 127794 | GBP | 2024-03-31 | 2025-12-17 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 127794 | GBP | 2024-03-31 | 2024-11-15 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-03-31 | 2024-11-15 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-03-31 | 2023-12-19 | filed | no | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 170977 | GBP | 2023-03-31 | 2024-11-15 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| cash | 170977 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 215576 | GBP | 2023-03-31 | 2024-11-15 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| current_assets | 215576 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 44599 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `frs-core:Debtors` | total-exemption-full |
| debtors | 44599 | GBP | 2023-03-31 | 2024-11-15 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 205244 | GBP | 2023-03-31 | 2024-11-15 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2023-03-31 | 2024-11-15 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 205244 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 1662 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `frs-core:FixedAssets` | total-exemption-full |
| fixed_assets | 1662 | GBP | 2023-03-31 | 2024-11-15 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 205246 | GBP | 2023-03-31 | 2024-11-15 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 205246 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 203900 | GBP | 2023-03-31 | 2024-11-15 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 203900 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 205562 | GBP | 2023-03-31 | 2024-11-15 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 205562 | GBP | 2023-03-31 | 2023-12-19 | filed | no | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2022-03-31 | 2023-12-19 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 79232 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `frs-core:CashBankOnHand` | total-exemption-full |
| current_assets | 240300 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `frs-core:CurrentAssets` | total-exemption-full |
| debtors | 161068 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `frs-core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 225679 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `frs-core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 2 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `frs-core:Equity` | total-exemption-full |
| fixed_assets | 672 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `frs-core:FixedAssets` | total-exemption-full |
| net_assets | 225681 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `frs-core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 225126 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 225798 | GBP | 2022-03-31 | 2023-12-19 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## PKWARE UK LIMITED (`gb:04622744`)

- registration: `04622744` (GB), status active, incorporated 2002-12-20
- classification: ['62012'] (sic_2007)
- records: 13 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 85 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2024-12-31 | 2025-07-17 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | small |
| cash | 31577 | GBP | 2024-12-31 | 2025-07-17 | filed | yes | `core:CashBankOnHand` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 20568 | GBP | 2024-12-31 | 2025-07-17 | filed | yes | `core:Creditors` | small |
| current_assets | 615870 | GBP | 2024-12-31 | 2025-07-17 | filed | yes | `core:CurrentAssets` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 584293 | GBP | 2024-12-31 | 2025-07-17 | filed | yes | `core:Debtors` | small |
| debtors | 584293 | GBP | 2024-12-31 | 2025-07-17 | filed | yes | `core:Debtors` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 597747 | GBP | 2024-12-31 | 2025-07-17 | filed | yes | `core:Equity` | small |
| equity | 597847 | GBP | 2024-12-31 | 2025-07-17 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-12-31 | 2025-07-17 | filed | yes | `core:Equity` | small |
| net_assets | 597847 | GBP | 2024-12-31 | 2025-07-17 | filed | yes | `core:NetAssetsLiabilities` | small |
| net_current_assets | 595302 | GBP | 2024-12-31 | 2025-07-17 | filed | yes | `core:NetCurrentAssetsLiabilities` | small |
| total_assets_less_current_liabilities | 598444 | GBP | 2024-12-31 | 2025-07-17 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | small |
| average_employees | 1 | xbrli:pure | 2023-12-31 | 2024-08-08 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | small |
| average_employees | 1 | xbrli:pure | 2023-12-31 | 2025-07-17 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | small |
| cash | 24537 | GBP | 2023-12-31 | 2024-08-08 | filed | no | `core:CashBankOnHand` | small |
| cash | 24537 | GBP | 2023-12-31 | 2025-07-17 | filed | yes | `core:CashBankOnHand` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 19810 | GBP | 2023-12-31 | 2025-07-17 | filed | yes | `core:Creditors` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 19810 | GBP | 2023-12-31 | 2024-08-08 | filed | no | `core:Creditors` | small |
| current_assets | 575980 | GBP | 2023-12-31 | 2025-07-17 | filed | yes | `core:CurrentAssets` | small |
| current_assets | 575980 | GBP | 2023-12-31 | 2024-08-08 | filed | no | `core:CurrentAssets` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 551443 | GBP | 2023-12-31 | 2024-08-08 | filed | no | `core:Debtors` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 551443 | GBP | 2023-12-31 | 2025-07-17 | filed | yes | `core:Debtors` | small |
| debtors | 551443 | GBP | 2023-12-31 | 2025-07-17 | filed | yes | `core:Debtors` | small |
| debtors | 551443 | GBP | 2023-12-31 | 2024-08-08 | filed | no | `core:Debtors` | small |
| equity | 558032 | GBP | 2023-12-31 | 2025-07-17 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-12-31 | 2025-07-17 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-12-31 | 2024-08-08 | filed | no | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 557932 | GBP | 2023-12-31 | 2024-08-08 | filed | no | `core:Equity` | small |
| equity | 558032 | GBP | 2023-12-31 | 2024-08-08 | filed | no | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 557932 | GBP | 2023-12-31 | 2025-07-17 | filed | yes | `core:Equity` | small |
| net_assets | 558032 | GBP | 2023-12-31 | 2024-08-08 | filed | no | `core:NetAssetsLiabilities` | small |
| net_assets | 558032 | GBP | 2023-12-31 | 2025-07-17 | filed | yes | `core:NetAssetsLiabilities` | small |
| net_current_assets | 556170 | GBP | 2023-12-31 | 2024-08-08 | filed | no | `core:NetCurrentAssetsLiabilities` | small |
| net_current_assets | 556170 | GBP | 2023-12-31 | 2025-07-17 | filed | yes | `core:NetCurrentAssetsLiabilities` | small |
| total_assets_less_current_liabilities | 558398 | GBP | 2023-12-31 | 2024-08-08 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | small |
| total_assets_less_current_liabilities | 558398 | GBP | 2023-12-31 | 2025-07-17 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | small |
| average_employees | 3 | xbrli:pure | 2022-12-31 | 2023-09-25 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | small |
| average_employees | 3 | xbrli:pure | 2022-12-31 | 2024-08-08 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | small |
| cash | 25401 | GBP | 2022-12-31 | 2023-09-25 | filed | no | `core:CashBankOnHand` | small |
| cash | 25401 | GBP | 2022-12-31 | 2024-08-08 | filed | yes | `core:CashBankOnHand` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 35123 | GBP | 2022-12-31 | 2023-09-25 | filed | no | `core:Creditors` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 35123 | GBP | 2022-12-31 | 2024-08-08 | filed | yes | `core:Creditors` | small |
| current_assets | 547376 | GBP | 2022-12-31 | 2023-09-25 | filed | no | `core:CurrentAssets` | small |
| current_assets | 547376 | GBP | 2022-12-31 | 2024-08-08 | filed | yes | `core:CurrentAssets` | small |
| debtors | 521975 | GBP | 2022-12-31 | 2024-08-08 | filed | yes | `core:Debtors` | small |
| debtors | 521975 | GBP | 2022-12-31 | 2023-09-25 | filed | no | `core:Debtors` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 521975 | GBP | 2022-12-31 | 2023-09-25 | filed | no | `core:Debtors` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 521975 | GBP | 2022-12-31 | 2024-08-08 | filed | yes | `core:Debtors` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 514823 | GBP | 2022-12-31 | 2023-09-25 | filed | no | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2022-12-31 | 2024-08-08 | filed | yes | `core:Equity` | small |
| equity | 514923 | GBP | 2022-12-31 | 2023-09-25 | filed | no | `core:Equity` | small |
| equity | 514923 | GBP | 2022-12-31 | 2024-08-08 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2022-12-31 | 2023-09-25 | filed | no | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 514823 | GBP | 2022-12-31 | 2024-08-08 | filed | yes | `core:Equity` | small |
| net_assets | 514923 | GBP | 2022-12-31 | 2024-08-08 | filed | yes | `core:NetAssetsLiabilities` | small |
| net_assets | 514923 | GBP | 2022-12-31 | 2023-09-25 | filed | no | `core:NetAssetsLiabilities` | small |
| net_current_assets | 512253 | GBP | 2022-12-31 | 2024-08-08 | filed | yes | `core:NetCurrentAssetsLiabilities` | small |
| net_current_assets | 512253 | GBP | 2022-12-31 | 2023-09-25 | filed | no | `core:NetCurrentAssetsLiabilities` | small |
| total_assets_less_current_liabilities | 515289 | GBP | 2022-12-31 | 2023-09-25 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | small |
| total_assets_less_current_liabilities | 515289 | GBP | 2022-12-31 | 2024-08-08 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | small |
| average_employees | 3 | xbrli:pure | 2021-12-31 | 2023-09-25 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | small |
| cash | 23017 | GBP | 2021-12-31 | 2023-09-25 | filed | yes | `core:CashBankOnHand` | small |
| creditors_within_one_year `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 35330 | GBP | 2021-12-31 | 2023-09-25 | filed | yes | `core:Creditors` | small |
| current_assets | 500342 | GBP | 2021-12-31 | 2023-09-25 | filed | yes | `core:CurrentAssets` | small |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 477325 | GBP | 2021-12-31 | 2023-09-25 | filed | yes | `core:Debtors` | small |
| debtors | 477325 | GBP | 2021-12-31 | 2023-09-25 | filed | yes | `core:Debtors` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 468185 | GBP | 2021-12-31 | 2023-09-25 | filed | yes | `core:Equity` | small |
| equity | 468285 | GBP | 2021-12-31 | 2023-09-25 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2021-12-31 | 2023-09-25 | filed | yes | `core:Equity` | small |
| net_assets | 468285 | GBP | 2021-12-31 | 2023-09-25 | filed | yes | `core:NetAssetsLiabilities` | small |
| net_current_assets | 465012 | GBP | 2021-12-31 | 2023-09-25 | filed | yes | `core:NetCurrentAssetsLiabilities` | small |
| total_assets_less_current_liabilities | 468651 | GBP | 2021-12-31 | 2023-09-25 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | small |

_No coverage facts for the latest run._
