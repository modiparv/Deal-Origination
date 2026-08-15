# Ingest spot-check

- database: `data/engine.db`
- latest run: `20260815T025225Z-e2428643`
- companies in store: 4200; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## S.A. YORK DESIGN FACILITIES LIMITED (`gb:01254396`)

- registration: `01254396` (GB), status active, incorporated 1976-04-12
- classification: ['71111'] (sic_2007)
- records: 3 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 92 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## DAILEY ENGINEERING SERVICES LIMITED (`gb:01540497`)

- registration: `01540497` (GB), status active, incorporated 1981-01-22
- classification: ['71122'] (sic_2007)
- records: 2 officers, 2 beneficial owners, 0 ownership statements, 1 security interests, 87 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-03-31 | 2025-10-14 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 756 | GBP | 2025-03-31 | 2025-10-14 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| equity | -8626 | GBP | 2025-03-31 | 2025-10-14 | filed | yes | `frs-core:Equity` | micro-entity |
| fixed_assets | 238 | GBP | 2025-03-31 | 2025-10-14 | filed | yes | `frs-core:FixedAssets` | micro-entity |
| net_assets | -8626 | GBP | 2025-03-31 | 2025-10-14 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -7904 | GBP | 2025-03-31 | 2025-10-14 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | -7666 | GBP | 2025-03-31 | 2025-10-14 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | xbrli:pure | 2024-03-31 | 2025-10-14 | filed | yes | `frs-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-03-31 | 2025-03-26 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 718 | GBP | 2024-03-31 | 2025-03-26 | filed | yes | `core:CashBankOnHand` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 14089 | GBP | 2024-03-31 | 2025-03-26 | filed | yes | `core:Creditors` | unaudited-abridged |
| current_assets | 982 | GBP | 2024-03-31 | 2025-03-26 | filed | no | `core:CurrentAssets` | unaudited-abridged |
| current_assets | 718 | GBP | 2024-03-31 | 2025-10-14 | filed | yes | `frs-core:CurrentAssets` | micro-entity |
| debtors | 264 | GBP | 2024-03-31 | 2025-03-26 | filed | yes | `core:Debtors` | unaudited-abridged |
| equity | 213321 | GBP | 2024-03-31 | 2025-03-26 | filed | no | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2024-03-31 | 2025-03-26 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 213221 | GBP | 2024-03-31 | 2025-03-26 | filed | yes | `core:Equity` | unaudited-abridged |
| equity | 216421 | GBP | 2024-03-31 | 2025-10-14 | filed | yes | `frs-core:Equity` | micro-entity |
| fixed_assets | 226499 | GBP | 2024-03-31 | 2025-10-14 | filed | yes | `frs-core:FixedAssets` | micro-entity |
| gross_profit | 6350 | GBP | 2024-03-31 | 2025-03-26 | filed | yes | `core:GrossProfitLoss` | unaudited-abridged |
| net_assets | 216421 | GBP | 2024-03-31 | 2025-10-14 | filed | yes | `frs-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 213321 | GBP | 2024-03-31 | 2025-03-26 | filed | no | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | -8904 | GBP | 2024-03-31 | 2025-10-14 | filed | yes | `frs-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | -13107 | GBP | 2024-03-31 | 2025-03-26 | filed | no | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| operating_profit | 323 | GBP | 2024-03-31 | 2025-03-26 | filed | yes | `core:OperatingProfitLoss` | unaudited-abridged |
| profit_before_tax | 430 | GBP | 2024-03-31 | 2025-03-26 | filed | yes | `core:ProfitLossOnOrdinaryActivitiesBeforeTax` | unaudited-abridged |
| profit_for_period | 523 | GBP | 2024-03-31 | 2025-03-26 | filed | yes | `core:ProfitLoss` | unaudited-abridged |
| tax_charge | -93 | GBP | 2024-03-31 | 2025-03-26 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | unaudited-abridged |
| total_assets_less_current_liabilities | 213392 | GBP | 2024-03-31 | 2025-03-26 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 217595 | GBP | 2024-03-31 | 2025-10-14 | filed | yes | `frs-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-03-31 | 2025-03-26 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| average_employees | 2 | xbrli:pure | 2023-03-31 | 2023-12-26 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 3059 | GBP | 2023-03-31 | 2023-12-26 | filed | no | `core:CashBankOnHand` | unaudited-abridged |
| cash | 3059 | GBP | 2023-03-31 | 2025-03-26 | filed | yes | `core:CashBankOnHand` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 17062 | GBP | 2023-03-31 | 2023-12-26 | filed | no | `core:Creditors` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 17062 | GBP | 2023-03-31 | 2025-03-26 | filed | yes | `core:Creditors` | unaudited-abridged |
| current_assets | 3323 | GBP | 2023-03-31 | 2025-03-26 | filed | yes | `core:CurrentAssets` | unaudited-abridged |
| current_assets | 3323 | GBP | 2023-03-31 | 2023-12-26 | filed | no | `core:CurrentAssets` | unaudited-abridged |
| debtors | 264 | GBP | 2023-03-31 | 2023-12-26 | filed | no | `core:Debtors` | unaudited-abridged |
| debtors | 264 | GBP | 2023-03-31 | 2025-03-26 | filed | yes | `core:Debtors` | unaudited-abridged |
| equity | 212798 | GBP | 2023-03-31 | 2025-03-26 | filed | yes | `core:Equity` | unaudited-abridged |
| equity | 212798 | GBP | 2023-03-31 | 2023-12-26 | filed | no | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-03-31 | 2025-03-26 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 212698 | GBP | 2023-03-31 | 2025-03-26 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 212698 | GBP | 2023-03-31 | 2023-12-26 | filed | no | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2023-03-31 | 2023-12-26 | filed | no | `core:Equity` | unaudited-abridged |
| gross_profit | 9049 | GBP | 2023-03-31 | 2025-03-26 | filed | yes | `core:GrossProfitLoss` | unaudited-abridged |
| net_assets | 212798 | GBP | 2023-03-31 | 2025-03-26 | filed | yes | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_assets | 212798 | GBP | 2023-03-31 | 2023-12-26 | filed | no | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | -13739 | GBP | 2023-03-31 | 2023-12-26 | filed | no | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| net_current_assets | -13739 | GBP | 2023-03-31 | 2025-03-26 | filed | yes | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| operating_profit | 3712 | GBP | 2023-03-31 | 2025-03-26 | filed | yes | `core:OperatingProfitLoss` | unaudited-abridged |
| profit_before_tax | 3761 | GBP | 2023-03-31 | 2025-03-26 | filed | yes | `core:ProfitLossOnOrdinaryActivitiesBeforeTax` | unaudited-abridged |
| profit_for_period | 5024 | GBP | 2023-03-31 | 2025-03-26 | filed | yes | `core:ProfitLoss` | unaudited-abridged |
| tax_charge | -1263 | GBP | 2023-03-31 | 2025-03-26 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | unaudited-abridged |
| total_assets_less_current_liabilities | 212962 | GBP | 2023-03-31 | 2023-12-26 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 212962 | GBP | 2023-03-31 | 2025-03-26 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |
| average_employees | 2 | xbrli:pure | 2022-03-31 | 2023-12-26 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | unaudited-abridged |
| cash | 674 | GBP | 2022-03-31 | 2023-12-26 | filed | yes | `core:CashBankOnHand` | unaudited-abridged |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 19875 | GBP | 2022-03-31 | 2023-12-26 | filed | yes | `core:Creditors` | unaudited-abridged |
| current_assets | 1218 | GBP | 2022-03-31 | 2023-12-26 | filed | yes | `core:CurrentAssets` | unaudited-abridged |
| debtors | 544 | GBP | 2022-03-31 | 2023-12-26 | filed | yes | `core:Debtors` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 207674 | GBP | 2022-03-31 | 2025-03-26 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 100 | GBP | 2022-03-31 | 2023-12-26 | filed | yes | `core:Equity` | unaudited-abridged |
| equity | 207774 | GBP | 2022-03-31 | 2023-12-26 | filed | yes | `core:Equity` | unaudited-abridged |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 207674 | GBP | 2022-03-31 | 2023-12-26 | filed | no | `core:Equity` | unaudited-abridged |
| net_assets | 207774 | GBP | 2022-03-31 | 2023-12-26 | filed | yes | `core:NetAssetsLiabilities` | unaudited-abridged |
| net_current_assets | -18657 | GBP | 2022-03-31 | 2023-12-26 | filed | yes | `core:NetCurrentAssetsLiabilities` | unaudited-abridged |
| total_assets_less_current_liabilities | 208306 | GBP | 2022-03-31 | 2023-12-26 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | unaudited-abridged |

_No coverage facts for the latest run._

- event restatement @ 2025-10-14: `{"superseded_document_id": "gb:01540497:doc:pmLgMWvhXOC0IiLIvXo_w1rPrqJm9_P-yyU_wbbZ0kc", "restatements": [{"concept": "current_assets", "period_end": "2024-03-31", "old_value": "982.0000", "new_value`

## SWIFTSYSTEM LIMITED (`gb:01810384`)

- registration: `01810384` (GB), status active, incorporated 1984-04-19
- classification: ['62011'] (sic_2007)
- records: 3 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 106 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | iso4217:GBP | 2025-03-31 | 2025-10-02 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1446 | GBP | 2025-03-31 | 2025-10-02 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 100 | GBP | 2025-03-31 | 2025-10-02 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 1346 | GBP | 2025-03-31 | 2025-10-02 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2025-03-31 | 2025-10-02 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 1346 | GBP | 2025-03-31 | 2025-10-02 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 1346 | GBP | 2025-03-31 | 2025-10-02 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 1346 | GBP | 2025-03-31 | 2025-10-02 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-03-31 | 2025-10-02 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-03-31 | 2024-06-05 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 728 | GBP | 2024-03-31 | 2025-10-02 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 728 | GBP | 2024-03-31 | 2024-06-05 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 56 | GBP | 2024-03-31 | 2025-10-02 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 56 | GBP | 2024-03-31 | 2024-06-05 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | 354 | GBP | 2024-03-31 | 2025-10-02 | filed | yes | `uk-core:Equity` | micro-entity |
| equity | 354 | GBP | 2024-03-31 | 2024-06-05 | filed | no | `uk-core:Equity` | micro-entity |
| fixed_assets | 456 | GBP | 2024-03-31 | 2025-10-02 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 456 | GBP | 2024-03-31 | 2024-06-05 | filed | no | `uk-core:FixedAssets` | micro-entity |
| net_assets | 354 | GBP | 2024-03-31 | 2024-06-05 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 354 | GBP | 2024-03-31 | 2025-10-02 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 672 | GBP | 2024-03-31 | 2025-10-02 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 672 | GBP | 2024-03-31 | 2024-06-05 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 216 | GBP | 2024-03-31 | 2025-10-02 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 216 | GBP | 2024-03-31 | 2024-06-05 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-03-31 | 2023-06-13 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-03-31 | 2024-06-05 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 262 | GBP | 2023-03-31 | 2024-06-05 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 262 | GBP | 2023-03-31 | 2023-06-13 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 1242 | GBP | 2023-03-31 | 2023-06-13 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 1242 | GBP | 2023-03-31 | 2024-06-05 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 1647 | GBP | 2023-03-31 | 2023-06-13 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 1647 | GBP | 2023-03-31 | 2024-06-05 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 1017 | GBP | 2023-03-31 | 2024-06-05 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 1017 | GBP | 2023-03-31 | 2023-06-13 | filed | no | `uk-core:FixedAssets` | micro-entity |
| net_assets | 1647 | GBP | 2023-03-31 | 2023-06-13 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 1647 | GBP | 2023-03-31 | 2024-06-05 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 980 | GBP | 2023-03-31 | 2024-06-05 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 980 | GBP | 2023-03-31 | 2023-06-13 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 1997 | GBP | 2023-03-31 | 2023-06-13 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 1997 | GBP | 2023-03-31 | 2024-06-05 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2022-03-31 | 2023-06-13 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 602 | GBP | 2022-03-31 | 2023-06-13 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 6620 | GBP | 2022-03-31 | 2023-06-13 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 6894 | GBP | 2022-03-31 | 2023-06-13 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 1726 | GBP | 2022-03-31 | 2023-06-13 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 6894 | GBP | 2022-03-31 | 2023-06-13 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 6018 | GBP | 2022-03-31 | 2023-06-13 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 7744 | GBP | 2022-03-31 | 2023-06-13 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

Coverage @ 2025-03-31: 8/21 concepts available (average_employees, creditors_within_one_year, current_assets, equity, fixed_assets, net_assets, net_current_assets, total_assets_less_current_liabilities)
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

## RAKEWELL LIMITED (`gb:02009194`)

- registration: `02009194` (GB), status active, incorporated 1986-04-11
- classification: ['26400', '47910', '62012'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 95 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | iso4217:GBP | 2025-09-30 | 2025-11-18 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5326 | GBP | 2025-09-30 | 2025-11-18 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 0 | GBP | 2025-09-30 | 2025-11-18 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 5826 | GBP | 2025-09-30 | 2025-11-18 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 0 | GBP | 2025-09-30 | 2025-11-18 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 5826 | GBP | 2025-09-30 | 2025-11-18 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 5326 | GBP | 2025-09-30 | 2025-11-18 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 5326 | GBP | 2025-09-30 | 2025-11-18 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2024-09-30 | 2025-11-18 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2024-09-30 | 2025-03-21 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5980 | GBP | 2024-09-30 | 2025-11-18 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5980 | GBP | 2024-09-30 | 2025-03-21 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 1310 | GBP | 2024-09-30 | 2025-03-21 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 1311 | GBP | 2024-09-30 | 2025-11-18 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 4983 | GBP | 2024-09-30 | 2025-11-18 | filed | yes | `uk-core:Equity` | micro-entity |
| equity | 4983 | GBP | 2024-09-30 | 2025-03-21 | filed | no | `uk-core:Equity` | micro-entity |
| fixed_assets | 59 | GBP | 2024-09-30 | 2025-11-18 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 59 | GBP | 2024-09-30 | 2025-03-21 | filed | no | `uk-core:FixedAssets` | micro-entity |
| net_assets | 4983 | GBP | 2024-09-30 | 2025-03-21 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 4983 | GBP | 2024-09-30 | 2025-11-18 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 4542 | GBP | 2024-09-30 | 2025-11-18 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 4542 | GBP | 2024-09-30 | 2025-03-21 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 4483 | GBP | 2024-09-30 | 2025-11-18 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 4483 | GBP | 2024-09-30 | 2025-03-21 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2023-09-30 | 2023-10-26 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2023-09-30 | 2025-03-21 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5744 | GBP | 2023-09-30 | 2025-03-21 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5744 | GBP | 2023-09-30 | 2023-10-26 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 1683 | GBP | 2023-09-30 | 2025-03-21 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 1683 | GBP | 2023-09-30 | 2023-10-26 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | 4083 | GBP | 2023-09-30 | 2025-03-21 | filed | yes | `uk-core:Equity` | micro-entity |
| equity | 4083 | GBP | 2023-09-30 | 2023-10-26 | filed | no | `uk-core:Equity` | micro-entity |
| fixed_assets | 232 | GBP | 2023-09-30 | 2025-03-21 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| fixed_assets | 232 | GBP | 2023-09-30 | 2023-10-26 | filed | no | `uk-core:FixedAssets` | micro-entity |
| net_assets | 4083 | GBP | 2023-09-30 | 2025-03-21 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 4083 | GBP | 2023-09-30 | 2023-10-26 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 3865 | GBP | 2023-09-30 | 2023-10-26 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 3865 | GBP | 2023-09-30 | 2025-03-21 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 3633 | GBP | 2023-09-30 | 2025-03-21 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 3633 | GBP | 2023-09-30 | 2023-10-26 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2022-09-30 | 2023-10-26 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 5219 | GBP | 2022-09-30 | 2023-10-26 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 1124 | GBP | 2022-09-30 | 2023-10-26 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 4202 | GBP | 2022-09-30 | 2023-10-26 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 415 | GBP | 2022-09-30 | 2023-10-26 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 4202 | GBP | 2022-09-30 | 2023-10-26 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 4067 | GBP | 2022-09-30 | 2023-10-26 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 3652 | GBP | 2022-09-30 | 2023-10-26 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2025-11-18: `{"superseded_document_id": "gb:02009194:doc:3ghEBJW9xscNTLXiEA70a2E4e8FuWJX6Nqupq1OQrbI", "restatements": [{"concept": "current_assets", "period_end": "2024-09-30", "old_value": "1310.0000", "new_valu`

## DATA SYSTEMS (COMPUTERS) LIMITED (`gb:02179329`)

- registration: `02179329` (GB), status active, incorporated 1987-10-15
- classification: ['62090'] (sic_2007)
- records: 5 officers, 3 beneficial owners, 0 ownership statements, 2 security interests, 103 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 10 | xbrli:pure | 2025-03-31 | 2025-12-10 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 2583262 | GBP | 2025-03-31 | 2025-12-10 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 3854592 | GBP | 2025-03-31 | 2025-12-10 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 854446 | GBP | 2025-03-31 | 2025-12-10 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 854446 | GBP | 2025-03-31 | 2025-12-10 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 2863980 | GBP | 2025-03-31 | 2025-12-10 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 20000 | GBP | 2025-03-31 | 2025-12-10 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2843980 | GBP | 2025-03-31 | 2025-12-10 | filed | yes | `ns5:Equity` | total-exemption-full |
| fixed_assets | 195870 | GBP | 2025-03-31 | 2025-12-10 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| net_assets | 2863980 | GBP | 2025-03-31 | 2025-12-10 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 2693662 | GBP | 2025-03-31 | 2025-12-10 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 2889532 | GBP | 2025-03-31 | 2025-12-10 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 13 | xbrli:pure | 2024-03-31 | 2025-12-10 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 13 | xbrli:pure | 2024-03-31 | 2025-01-21 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 1718625 | GBP | 2024-03-31 | 2025-12-10 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 1718625 | GBP | 2024-03-31 | 2025-01-21 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 3227312 | GBP | 2024-03-31 | 2025-12-10 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 3227312 | GBP | 2024-03-31 | 2025-01-21 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 1168296 | GBP | 2024-03-31 | 2025-12-10 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 1168296 | GBP | 2024-03-31 | 2025-01-21 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 1168296 | GBP | 2024-03-31 | 2025-01-21 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 1168296 | GBP | 2024-03-31 | 2025-12-10 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 2571254 | GBP | 2024-03-31 | 2025-01-21 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 20000 | GBP | 2024-03-31 | 2025-01-21 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 20000 | GBP | 2024-03-31 | 2025-12-10 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2551254 | GBP | 2024-03-31 | 2025-12-10 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 2571254 | GBP | 2024-03-31 | 2025-12-10 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2551254 | GBP | 2024-03-31 | 2025-01-21 | filed | no | `ns5:Equity` | total-exemption-full |
| fixed_assets | 262678 | GBP | 2024-03-31 | 2025-01-21 | filed | no | `ns5:FixedAssets` | total-exemption-full |
| fixed_assets | 262678 | GBP | 2024-03-31 | 2025-12-10 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| net_assets | 2571254 | GBP | 2024-03-31 | 2025-12-10 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 2571254 | GBP | 2024-03-31 | 2025-01-21 | filed | no | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 2371241 | GBP | 2024-03-31 | 2025-01-21 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 2371241 | GBP | 2024-03-31 | 2025-12-10 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 2633919 | GBP | 2024-03-31 | 2025-01-21 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 2633919 | GBP | 2024-03-31 | 2025-12-10 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 12 | xbrli:pure | 2023-03-31 | 2023-10-13 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 12 | xbrli:pure | 2023-03-31 | 2025-01-21 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 1036858 | GBP | 2023-03-31 | 2023-10-13 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 1036858 | GBP | 2023-03-31 | 2025-01-21 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 3098178 | GBP | 2023-03-31 | 2023-10-13 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 3098178 | GBP | 2023-03-31 | 2025-01-21 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 1657573 | GBP | 2023-03-31 | 2025-01-21 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 1657573 | GBP | 2023-03-31 | 2025-01-21 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original'}` | 1657573 | GBP | 2023-03-31 | 2023-10-13 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1657573 | GBP | 2023-03-31 | 2023-10-13 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 2444696 | GBP | 2023-03-31 | 2025-01-21 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2424696 | GBP | 2023-03-31 | 2025-01-21 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 20000 | GBP | 2023-03-31 | 2023-10-13 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2424696 | GBP | 2023-03-31 | 2023-10-13 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 20000 | GBP | 2023-03-31 | 2025-01-21 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 2444696 | GBP | 2023-03-31 | 2023-10-13 | filed | yes | `ns5:Equity` | total-exemption-full |
| fixed_assets | 255355 | GBP | 2023-03-31 | 2025-01-21 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| fixed_assets `{'OriginalRevisedDataDimension': 'Original'}` | 255355 | GBP | 2023-03-31 | 2023-10-13 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| net_assets | 2444696 | GBP | 2023-03-31 | 2025-01-21 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets `{'OriginalRevisedDataDimension': 'Original'}` | 2444696 | GBP | 2023-03-31 | 2023-10-13 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 2235430 | GBP | 2023-03-31 | 2025-01-21 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 2235430 | GBP | 2023-03-31 | 2023-10-13 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 2490785 | GBP | 2023-03-31 | 2025-01-21 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 2490785 | GBP | 2023-03-31 | 2023-10-13 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees `{'OriginalRevisedDataDimension': 'Original'}` | 13 | xbrli:pure | 2022-03-31 | 2023-10-13 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash `{'OriginalRevisedDataDimension': 'Original'}` | 1107114 | GBP | 2022-03-31 | 2023-10-13 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 3095404 | GBP | 2022-03-31 | 2023-10-13 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original'}` | 1591725 | GBP | 2022-03-31 | 2023-10-13 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'OriginalRevisedDataDimension': 'Original', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 1591725 | GBP | 2022-03-31 | 2023-10-13 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original'}` | 2126213 | GBP | 2022-03-31 | 2023-10-13 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'OriginalRevisedDataDimension': 'Original'}` | 20000 | GBP | 2022-03-31 | 2023-10-13 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'OriginalRevisedDataDimension': 'Original', 'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 2106213 | GBP | 2022-03-31 | 2023-10-13 | filed | yes | `ns5:Equity` | total-exemption-full |
| fixed_assets `{'OriginalRevisedDataDimension': 'Original'}` | 34915 | GBP | 2022-03-31 | 2023-10-13 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| net_assets `{'OriginalRevisedDataDimension': 'Original'}` | 2126213 | GBP | 2022-03-31 | 2023-10-13 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets `{'OriginalRevisedDataDimension': 'Original'}` | 2095068 | GBP | 2022-03-31 | 2023-10-13 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities `{'OriginalRevisedDataDimension': 'Original'}` | 2129983 | GBP | 2022-03-31 | 2023-10-13 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## NEVRUN LIMITED (`gb:02326134`)

- registration: `02326134` (GB), status active, incorporated 1988-12-07
- classification: ['62090'] (sic_2007)
- records: 2 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 85 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2026-04-05 | 2026-05-19 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 29294 | GBP | 2026-04-05 | 2026-05-19 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 253500 | GBP | 2026-04-05 | 2026-05-19 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 224205 | GBP | 2026-04-05 | 2026-05-19 | filed | yes | `core:Equity` | micro-entity |
| net_assets | 224205 | GBP | 2026-04-05 | 2026-05-19 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 224205 | GBP | 2026-04-05 | 2026-05-19 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 224205 | GBP | 2026-04-05 | 2026-05-19 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2025-04-05 | 2025-05-15 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 19522 | GBP | 2025-04-05 | 2025-05-15 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 19522 | GBP | 2025-04-05 | 2026-05-19 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 261618 | GBP | 2025-04-05 | 2026-05-19 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 261618 | GBP | 2025-04-05 | 2025-05-15 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| equity | 242096 | GBP | 2025-04-05 | 2025-05-15 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 242096 | GBP | 2025-04-05 | 2026-05-19 | filed | yes | `core:Equity` | micro-entity |
| net_assets | 242096 | GBP | 2025-04-05 | 2026-05-19 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 242096 | GBP | 2025-04-05 | 2025-05-15 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 242096 | GBP | 2025-04-05 | 2026-05-19 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 242096 | GBP | 2025-04-05 | 2025-05-15 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 242096 | GBP | 2025-04-05 | 2026-05-19 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 242096 | GBP | 2025-04-05 | 2025-05-15 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2024-04-05 | 2025-05-15 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2024-04-05 | 2024-06-25 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 42928 | GBP | 2024-04-05 | 2025-05-15 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 42928 | GBP | 2024-04-05 | 2024-06-25 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 291316 | GBP | 2024-04-05 | 2024-06-25 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 291316 | GBP | 2024-04-05 | 2025-05-15 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 248388 | GBP | 2024-04-05 | 2024-06-25 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 248388 | GBP | 2024-04-05 | 2025-05-15 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 248388 | GBP | 2024-04-05 | 2024-06-25 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 248388 | GBP | 2024-04-05 | 2025-05-15 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 248388 | GBP | 2024-04-05 | 2025-05-15 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 248388 | GBP | 2024-04-05 | 2024-06-25 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 248388 | GBP | 2024-04-05 | 2024-06-25 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 248388 | GBP | 2024-04-05 | 2025-05-15 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | iso4217:GBP | 2023-04-05 | 2024-06-25 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 17245 | GBP | 2023-04-05 | 2024-06-25 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 299064 | GBP | 2023-04-05 | 2024-06-25 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 281819 | GBP | 2023-04-05 | 2024-06-25 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 281819 | GBP | 2023-04-05 | 2024-06-25 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 281819 | GBP | 2023-04-05 | 2024-06-25 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 281819 | GBP | 2023-04-05 | 2024-06-25 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## REAL ASSET MANAGEMENT LIMITED (`gb:02454806`)

- registration: `02454806` (GB), status active, incorporated 1989-12-21
- classification: ['62012'] (sic_2007)
- records: 22 officers, 2 beneficial owners, 0 ownership statements, 3 security interests, 192 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## CREEPERS LIMITED (`gb:02567971`)

- registration: `02567971` (GB), status active, incorporated 1990-12-12
- classification: ['71112'] (sic_2007)
- records: 8 officers, 2 beneficial owners, 0 ownership statements, 1 security interests, 125 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 37 | xbrli:pure | 2025-08-31 | 2026-05-21 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 1184322 | GBP | 2025-08-31 | 2026-05-21 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 2488902 | GBP | 2025-08-31 | 2026-05-21 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 574365 | GBP | 2025-08-31 | 2026-05-21 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 574365 | GBP | 2025-08-31 | 2026-05-21 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1999559 | GBP | 2025-08-31 | 2026-05-21 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 114 | GBP | 2025-08-31 | 2026-05-21 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 1999673 | GBP | 2025-08-31 | 2026-05-21 | filed | yes | `ns5:Equity` | total-exemption-full |
| fixed_assets | 470421 | GBP | 2025-08-31 | 2026-05-21 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| net_assets | 1999673 | GBP | 2025-08-31 | 2026-05-21 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1666150 | GBP | 2025-08-31 | 2026-05-21 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 2136571 | GBP | 2025-08-31 | 2026-05-21 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 41 | xbrli:pure | 2024-08-31 | 2026-05-21 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 41 | xbrli:pure | 2024-08-31 | 2025-05-21 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 1071637 | GBP | 2024-08-31 | 2026-05-21 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 1071637 | GBP | 2024-08-31 | 2025-05-21 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 2444961 | GBP | 2024-08-31 | 2026-05-21 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 2444961 | GBP | 2024-08-31 | 2025-05-21 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 714192 | GBP | 2024-08-31 | 2025-05-21 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 714192 | GBP | 2024-08-31 | 2025-05-21 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 714192 | GBP | 2024-08-31 | 2026-05-21 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 714192 | GBP | 2024-08-31 | 2026-05-21 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity | 1794893 | GBP | 2024-08-31 | 2025-05-21 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1794779 | GBP | 2024-08-31 | 2025-05-21 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 114 | GBP | 2024-08-31 | 2026-05-21 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 114 | GBP | 2024-08-31 | 2025-05-21 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | 1794893 | GBP | 2024-08-31 | 2026-05-21 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1794779 | GBP | 2024-08-31 | 2026-05-21 | filed | yes | `ns5:Equity` | total-exemption-full |
| fixed_assets | 390366 | GBP | 2024-08-31 | 2026-05-21 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| fixed_assets | 390366 | GBP | 2024-08-31 | 2025-05-21 | filed | no | `ns5:FixedAssets` | total-exemption-full |
| net_assets | 1794893 | GBP | 2024-08-31 | 2026-05-21 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 1794893 | GBP | 2024-08-31 | 2025-05-21 | filed | no | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1566110 | GBP | 2024-08-31 | 2025-05-21 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1566110 | GBP | 2024-08-31 | 2026-05-21 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1956476 | GBP | 2024-08-31 | 2026-05-21 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1956476 | GBP | 2024-08-31 | 2025-05-21 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 42 | xbrli:pure | 2023-08-31 | 2024-05-30 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 42 | xbrli:pure | 2023-08-31 | 2025-05-21 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 1124135 | GBP | 2023-08-31 | 2025-05-21 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 1124135 | GBP | 2023-08-31 | 2024-05-30 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 2397583 | GBP | 2023-08-31 | 2024-05-30 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 2397583 | GBP | 2023-08-31 | 2025-05-21 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 666960 | GBP | 2023-08-31 | 2024-05-30 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 666960 | GBP | 2023-08-31 | 2025-05-21 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 666960 | GBP | 2023-08-31 | 2025-05-21 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 666960 | GBP | 2023-08-31 | 2024-05-30 | filed | no | `ns5:Debtors` | total-exemption-full |
| equity | 1639872 | GBP | 2023-08-31 | 2025-05-21 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 114 | GBP | 2023-08-31 | 2024-05-30 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 114 | GBP | 2023-08-31 | 2025-05-21 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 1639872 | GBP | 2023-08-31 | 2024-05-30 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1639758 | GBP | 2023-08-31 | 2025-05-21 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1639758 | GBP | 2023-08-31 | 2024-05-30 | filed | no | `ns5:Equity` | total-exemption-full |
| fixed_assets | 403430 | GBP | 2023-08-31 | 2024-05-30 | filed | no | `ns5:FixedAssets` | total-exemption-full |
| fixed_assets | 403430 | GBP | 2023-08-31 | 2025-05-21 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| net_assets | 1639872 | GBP | 2023-08-31 | 2024-05-30 | filed | no | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 1639872 | GBP | 2023-08-31 | 2025-05-21 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1447000 | GBP | 2023-08-31 | 2025-05-21 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1447000 | GBP | 2023-08-31 | 2024-05-30 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1850430 | GBP | 2023-08-31 | 2025-05-21 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1850430 | GBP | 2023-08-31 | 2024-05-30 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 43 | xbrli:pure | 2022-08-31 | 2024-05-30 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 826161 | GBP | 2022-08-31 | 2024-05-30 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 1930509 | GBP | 2022-08-31 | 2024-05-30 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors | 603114 | GBP | 2022-08-31 | 2024-05-30 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 603114 | GBP | 2022-08-31 | 2024-05-30 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 1282215 | GBP | 2022-08-31 | 2024-05-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 114 | GBP | 2022-08-31 | 2024-05-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 1282329 | GBP | 2022-08-31 | 2024-05-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| fixed_assets | 344704 | GBP | 2022-08-31 | 2024-05-30 | filed | yes | `ns5:FixedAssets` | total-exemption-full |
| net_assets | 1282329 | GBP | 2022-08-31 | 2024-05-30 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 1114257 | GBP | 2022-08-31 | 2024-05-30 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 1458961 | GBP | 2022-08-31 | 2024-05-30 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

Coverage @ 2025-08-31: 9/21 concepts available (average_employees, cash, current_assets, debtors, equity, fixed_assets, net_assets, net_current_assets, total_assets_less_current_liabilities)
- `creditors_after_one_year`: filed_without_concept — absent though regime 'total-exemption-full' typically includes it
- `creditors_within_one_year`: filed_without_concept — absent though regime 'total-exemption-full' typically includes it
- `depreciation_amortisation`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `gross_profit`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `operating_profit`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `profit_before_tax`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `profit_for_period`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `retained_earnings`: filed_without_concept — absent though regime 'total-exemption-full' typically includes it
- `revenue`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `share_capital`: filed_without_concept — absent though regime 'total-exemption-full' typically includes it
- `staff_costs`: filed_without_concept — regime 'total-exemption-full' omits this concept
- `tax_charge`: filed_without_concept — regime 'total-exemption-full' omits this concept

## BBA ARCHITECTS LTD (`gb:02679820`)

- registration: `02679820` (GB), status active, incorporated 1992-01-22
- classification: ['71111'] (sic_2007)
- records: 14 officers, 4 beneficial owners, 0 ownership statements, 0 security interests, 134 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 13 | xbrli:pure | 2025-03-31 | 2025-12-08 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 29024 | GBP | 2025-03-31 | 2025-12-08 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 88416 | GBP | 2025-03-31 | 2025-12-08 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 59392 | GBP | 2025-03-31 | 2025-12-08 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 59392 | GBP | 2025-03-31 | 2025-12-08 | filed | yes | `ns5:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1125 | GBP | 2025-03-31 | 2025-12-08 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | -44125 | GBP | 2025-03-31 | 2025-12-08 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 2500 | GBP | 2025-03-31 | 2025-12-08 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -47750 | GBP | 2025-03-31 | 2025-12-08 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | -44125 | GBP | 2025-03-31 | 2025-12-08 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -9125 | GBP | 2025-03-31 | 2025-12-08 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| profit_for_period `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -6430 | GBP | 2025-03-31 | 2025-12-08 | filed | yes | `ns5:ProfitLoss` | total-exemption-full |
| profit_for_period | -6430 | GBP | 2025-03-31 | 2025-12-08 | filed | yes | `ns5:ProfitLoss` | total-exemption-full |
| total_assets_less_current_liabilities | -9125 | GBP | 2025-03-31 | 2025-12-08 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 16 | xbrli:pure | 2024-03-31 | 2024-12-30 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 16 | xbrli:pure | 2024-03-31 | 2025-12-08 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 58539 | GBP | 2024-03-31 | 2025-12-08 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 58539 | GBP | 2024-03-31 | 2024-12-30 | filed | no | `ns5:CashBankOnHand` | total-exemption-full |
| current_assets | 139651 | GBP | 2024-03-31 | 2025-12-08 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 139651 | GBP | 2024-03-31 | 2024-12-30 | filed | no | `ns5:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 81112 | GBP | 2024-03-31 | 2025-12-08 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 81112 | GBP | 2024-03-31 | 2024-12-30 | filed | no | `ns5:Debtors` | total-exemption-full |
| debtors | 81112 | GBP | 2024-03-31 | 2025-12-08 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 81112 | GBP | 2024-03-31 | 2024-12-30 | filed | no | `ns5:Debtors` | total-exemption-full |
| equity | -27195 | GBP | 2024-03-31 | 2025-12-08 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -31195 | GBP | 2024-03-31 | 2025-12-08 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1500 | GBP | 2024-03-31 | 2025-12-08 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -31195 | GBP | 2024-03-31 | 2024-12-30 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1500 | GBP | 2024-03-31 | 2024-12-30 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 2500 | GBP | 2024-03-31 | 2024-12-30 | filed | no | `ns5:Equity` | total-exemption-full |
| equity | -27195 | GBP | 2024-03-31 | 2024-12-30 | filed | no | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 2500 | GBP | 2024-03-31 | 2025-12-08 | filed | yes | `ns5:Equity` | total-exemption-full |
| net_assets | -27195 | GBP | 2024-03-31 | 2025-12-08 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | -27195 | GBP | 2024-03-31 | 2024-12-30 | filed | no | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 37805 | GBP | 2024-03-31 | 2024-12-30 | filed | no | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 37805 | GBP | 2024-03-31 | 2025-12-08 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 37805 | GBP | 2024-03-31 | 2024-12-30 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 37805 | GBP | 2024-03-31 | 2025-12-08 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 16 | xbrli:pure | 2023-03-31 | 2024-12-30 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 16 | xbrli:pure | 2023-03-31 | 2023-12-20 | filed | no | `ns6:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 131240 | GBP | 2023-03-31 | 2024-12-30 | filed | yes | `ns5:CashBankOnHand` | total-exemption-full |
| cash | 131240 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `ns6:CashBankOnHand` | total-exemption-full |
| current_assets | 279830 | GBP | 2023-03-31 | 2024-12-30 | filed | yes | `ns5:CurrentAssets` | total-exemption-full |
| current_assets | 279830 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `ns6:CurrentAssets` | total-exemption-full |
| debtors | 148590 | GBP | 2023-03-31 | 2024-12-30 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 148590 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `ns6:Debtors` | total-exemption-full |
| debtors `{'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments', 'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 148590 | GBP | 2023-03-31 | 2024-12-30 | filed | yes | `ns5:Debtors` | total-exemption-full |
| debtors | 148590 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `ns6:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 60576 | GBP | 2023-03-31 | 2024-12-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 2500 | GBP | 2023-03-31 | 2024-12-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1500 | GBP | 2023-03-31 | 2024-12-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity | 64576 | GBP | 2023-03-31 | 2024-12-30 | filed | yes | `ns5:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1500 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `ns6:Equity` | total-exemption-full |
| equity | 64576 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 60576 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 2500 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `ns6:Equity` | total-exemption-full |
| net_assets | 64576 | GBP | 2023-03-31 | 2024-12-30 | filed | yes | `ns5:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 64576 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `ns6:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 159576 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `ns6:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 159576 | GBP | 2023-03-31 | 2024-12-30 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 159576 | GBP | 2023-03-31 | 2023-12-20 | filed | no | `ns6:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 159576 | GBP | 2023-03-31 | 2024-12-30 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 13 | xbrli:pure | 2022-03-31 | 2023-12-20 | filed | yes | `ns6:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 105879 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `ns6:CashBankOnHand` | total-exemption-full |
| current_assets | 370474 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `ns6:CurrentAssets` | total-exemption-full |
| debtors | 264595 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `ns6:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear', 'FinancialInstrumentCurrentNon-currentDimension': 'CurrentFinancialInstruments'}` | 264595 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `ns6:Debtors` | total-exemption-full |
| equity | 117442 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 113442 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 2500 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `ns6:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 1500 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `ns6:Equity` | total-exemption-full |
| net_assets | 117442 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `ns6:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 212442 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `ns6:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 212442 | GBP | 2022-03-31 | 2023-12-20 | filed | yes | `ns6:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._
