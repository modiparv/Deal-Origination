# Ingest spot-check

- database: `data/engine.db`
- latest run: `20261116T090636Z-b184c801`
- companies in store: 53000; sampled: 10 (deterministic stride)

Every figure below is a filed observation citing its source document's period end and filed date; `current = no` marks superseded observations retained for the restatement record.

## WEST YORKSHIRE SOCIETY OF ARCHITECTS (`gb:00021805`)

- registration: `00021805` (GB), status active, incorporated 1885-11-14
- classification: ['71111'] (sic_2007)
- records: 23 officers, 2 beneficial owners, 0 ownership statements, 0 security interests, 136 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## DESIGN TECHNOLOGY LIMITED (`gb:02828342`)

- registration: `02828342` (GB), status active, incorporated 1993-06-18
- classification: ['61300', '62020'] (sic_2007)
- records: 7 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 97 filings, 1 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | iso4217:GBP | 2025-06-30 | 2026-02-04 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 38969 | GBP | 2025-06-30 | 2026-02-04 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 3409 | GBP | 2025-06-30 | 2026-02-04 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 11323 | GBP | 2025-06-30 | 2026-02-04 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 46883 | GBP | 2025-06-30 | 2026-02-04 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 11323 | GBP | 2025-06-30 | 2026-02-04 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -35560 | GBP | 2025-06-30 | 2026-02-04 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| profit_for_period | 5244 | GBP | 2025-06-30 | 2026-02-04 | filed | yes | `core:ProfitLoss` | micro-entity |
| revenue | 8699 | GBP | 2025-06-30 | 2026-02-04 | filed | yes | `core:TurnoverRevenue` | micro-entity |
| total_assets_less_current_liabilities | 11323 | GBP | 2025-06-30 | 2026-02-04 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2024-06-30 | 2025-03-15 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 40424 | GBP | 2024-06-30 | 2025-03-15 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 40424 | GBP | 2024-06-30 | 2026-02-04 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2024-06-30 | 2025-03-15 | filed | no | `uk-core:Creditors` | micro-entity |
| current_assets | 6384 | GBP | 2024-06-30 | 2025-03-15 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 6384 | GBP | 2024-06-30 | 2026-02-04 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 30318 | GBP | 2024-06-30 | 2026-02-04 | filed | yes | `core:Equity` | micro-entity |
| equity | 30318 | GBP | 2024-06-30 | 2025-03-15 | filed | no | `uk-core:Equity` | micro-entity |
| fixed_assets | 64358 | GBP | 2024-06-30 | 2026-02-04 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 64358 | GBP | 2024-06-30 | 2025-03-15 | filed | no | `uk-core:FixedAssets` | micro-entity |
| net_assets | 30318 | GBP | 2024-06-30 | 2026-02-04 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 30318 | GBP | 2024-06-30 | 2025-03-15 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | -34040 | GBP | 2024-06-30 | 2026-02-04 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 6384 | GBP | 2024-06-30 | 2025-03-15 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| profit_for_period | -1071 | GBP | 2024-06-30 | 2026-02-04 | filed | yes | `core:ProfitLoss` | micro-entity |
| revenue | 2446 | GBP | 2024-06-30 | 2026-02-04 | filed | yes | `core:TurnoverRevenue` | micro-entity |
| total_assets_less_current_liabilities | 30318 | GBP | 2024-06-30 | 2026-02-04 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 70742 | GBP | 2024-06-30 | 2025-03-15 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-06-30 | 2024-03-01 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-06-30 | 2025-03-15 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 37840 | GBP | 2023-06-30 | 2025-03-15 | filed | yes | `uk-core:Creditors` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 37840 | GBP | 2023-06-30 | 2024-03-01 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2023-06-30 | 2024-03-01 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2023-06-30 | 2025-03-15 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 6385 | GBP | 2023-06-30 | 2024-03-01 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 6385 | GBP | 2023-06-30 | 2025-03-15 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| depreciation_amortisation | 0 | GBP | 2023-06-30 | 2024-03-01 | filed | yes | `core:DepreciationAmortisationImpairmentExpense` | micro-entity |
| equity | 32828 | GBP | 2023-06-30 | 2024-03-01 | filed | no | `core:Equity` | micro-entity |
| equity | 32828 | GBP | 2023-06-30 | 2025-03-15 | filed | yes | `uk-core:Equity` | micro-entity |
| fixed_assets | 64283 | GBP | 2023-06-30 | 2024-03-01 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 64283 | GBP | 2023-06-30 | 2025-03-15 | filed | yes | `uk-core:FixedAssets` | micro-entity |
| net_assets | 32828 | GBP | 2023-06-30 | 2024-03-01 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 32828 | GBP | 2023-06-30 | 2025-03-15 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 6385 | GBP | 2023-06-30 | 2025-03-15 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 6385 | GBP | 2023-06-30 | 2024-03-01 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| profit_for_period | 456 | GBP | 2023-06-30 | 2024-03-01 | filed | yes | `core:ProfitLoss` | micro-entity |
| revenue | 4711 | GBP | 2023-06-30 | 2024-03-01 | filed | yes | `core:TurnoverRevenue` | micro-entity |
| staff_costs | 0 | GBP | 2023-06-30 | 2024-03-01 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | micro-entity |
| tax_charge | 0 | GBP | 2023-06-30 | 2024-03-01 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | micro-entity |
| total_assets_less_current_liabilities | 70668 | GBP | 2023-06-30 | 2025-03-15 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 70668 | GBP | 2023-06-30 | 2024-03-01 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 35951 | GBP | 2022-06-30 | 2024-03-01 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2022-06-30 | 2024-03-01 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 6851 | GBP | 2022-06-30 | 2024-03-01 | filed | yes | `core:CurrentAssets` | micro-entity |
| depreciation_amortisation | 0 | GBP | 2022-06-30 | 2024-03-01 | filed | yes | `core:DepreciationAmortisationImpairmentExpense` | micro-entity |
| equity | 35108 | GBP | 2022-06-30 | 2024-03-01 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 64208 | GBP | 2022-06-30 | 2024-03-01 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 35108 | GBP | 2022-06-30 | 2024-03-01 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 6851 | GBP | 2022-06-30 | 2024-03-01 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| profit_for_period | 880 | GBP | 2022-06-30 | 2024-03-01 | filed | yes | `core:ProfitLoss` | micro-entity |
| revenue | 3283 | GBP | 2022-06-30 | 2024-03-01 | filed | yes | `core:TurnoverRevenue` | micro-entity |
| staff_costs | 0 | GBP | 2022-06-30 | 2024-03-01 | filed | yes | `core:StaffCostsEmployeeBenefitsExpense` | micro-entity |
| tax_charge | 0 | GBP | 2022-06-30 | 2024-03-01 | filed | yes | `core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` | micro-entity |
| total_assets_less_current_liabilities | 71059 | GBP | 2022-06-30 | 2024-03-01 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

- event restatement @ 2026-02-04: `{"superseded_document_id": "gb:02828342:doc:Z8Qxoo5dNErhbkHrDl08KRAncCMP0gruHmILoA4mHvU", "restatements": [{"concept": "creditors_within_one_year", "period_end": "2024-06-30", "old_value": "0.0000", "`

## EASYVISTA LIMITED (`gb:03516042`)

- registration: `03516042` (GB), status active, incorporated 1998-02-24
- classification: ['62090'] (sic_2007)
- records: 19 officers, 2 beneficial owners, 2 ownership statements, 2 security interests, 140 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0.05 | xbrli:pure | 2024-12-31 | 2026-02-11 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | small |
| cash | 40 | GBP | 2024-12-31 | 2026-02-11 | filed | yes | `core:CashBankOnHand` | small |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 485023 | GBP | 2024-12-31 | 2026-02-11 | filed | yes | `core:Creditors` | small |
| current_assets | 1016643 | GBP | 2024-12-31 | 2026-02-11 | filed | yes | `core:CurrentAssets` | small |
| debtors | 1016603 | GBP | 2024-12-31 | 2026-02-11 | filed | yes | `core:Debtors` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -458545 | GBP | 2024-12-31 | 2026-02-11 | filed | yes | `core:Equity` | small |
| equity | 527438 | GBP | 2024-12-31 | 2026-02-11 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 920000 | GBP | 2024-12-31 | 2026-02-11 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 65983 | GBP | 2024-12-31 | 2026-02-11 | filed | yes | `core:Equity` | small |
| net_assets | 527438 | GBP | 2024-12-31 | 2026-02-11 | filed | yes | `core:NetAssetsLiabilities` | small |
| net_current_assets | 531620 | GBP | 2024-12-31 | 2026-02-11 | filed | yes | `core:NetCurrentAssetsLiabilities` | small |
| total_assets_less_current_liabilities | 536291 | GBP | 2024-12-31 | 2026-02-11 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | small |
| average_employees | 0.06 | xbrli:pure | 2023-12-31 | 2026-02-11 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | small |
| cash | 40 | GBP | 2023-12-31 | 2026-02-11 | filed | yes | `core:CashBankOnHand` | small |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 316359 | GBP | 2023-12-31 | 2026-02-11 | filed | yes | `core:Creditors` | small |
| current_assets | 1192865 | GBP | 2023-12-31 | 2026-02-11 | filed | yes | `core:CurrentAssets` | small |
| debtors | 1192825 | GBP | 2023-12-31 | 2026-02-11 | filed | yes | `core:Debtors` | small |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -130955 | GBP | 2023-12-31 | 2026-02-11 | filed | yes | `core:Equity` | small |
| equity | 855028 | GBP | 2023-12-31 | 2026-02-11 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'SharePremium'}` | 65983 | GBP | 2023-12-31 | 2026-02-11 | filed | yes | `core:Equity` | small |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 920000 | GBP | 2023-12-31 | 2026-02-11 | filed | yes | `core:Equity` | small |
| net_assets | 855028 | GBP | 2023-12-31 | 2026-02-11 | filed | yes | `core:NetAssetsLiabilities` | small |
| net_current_assets | 876506 | GBP | 2023-12-31 | 2026-02-11 | filed | yes | `core:NetCurrentAssetsLiabilities` | small |
| total_assets_less_current_liabilities | 880510 | GBP | 2023-12-31 | 2026-02-11 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | small |

_No coverage facts for the latest run._

## PYRAMID DISTRIBUTION LIMITED (`gb:04093028`)

- registration: `04093028` (GB), status active, incorporated 2000-10-19
- classification: ['46510', '62020'] (sic_2007)
- records: 8 officers, 3 beneficial owners, 0 ownership statements, 11 security interests, 112 filings, 0 events, 3 source documents

_No figures persisted for this company._

_No coverage facts for the latest run._

## MATTHEW HILTON LIMITED (`gb:04682314`)

- registration: `04682314` (GB), status active, incorporated 2003-02-28
- classification: ['71129'] (sic_2007)
- records: 4 officers, 1 beneficial owners, 0 ownership statements, 1 security interests, 74 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-03-31 | 2025-12-22 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 386509 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 413648 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 13279 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 413648 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 407423 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 420702 | GBP | 2025-03-31 | 2025-12-22 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 3 | xbrli:pure | 2024-03-31 | 2025-12-22 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 3 | xbrli:pure | 2024-03-31 | 2025-02-04 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 386221 | GBP | 2024-03-31 | 2025-02-04 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 386221 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 424489 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:Equity` | micro-entity |
| equity | 424489 | GBP | 2024-03-31 | 2025-02-04 | filed | no | `core:Equity` | micro-entity |
| fixed_assets | 17531 | GBP | 2024-03-31 | 2025-02-04 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 17531 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 424489 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 424489 | GBP | 2024-03-31 | 2025-02-04 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 412585 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 412585 | GBP | 2024-03-31 | 2025-02-04 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 430116 | GBP | 2024-03-31 | 2025-12-22 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 430116 | GBP | 2024-03-31 | 2025-02-04 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 3 | xbrli:pure | 2023-03-31 | 2023-12-22 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 3 | xbrli:pure | 2023-03-31 | 2025-02-04 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 438484 | GBP | 2023-03-31 | 2023-12-22 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 438484 | GBP | 2023-03-31 | 2025-02-04 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 457322 | GBP | 2023-03-31 | 2023-12-22 | filed | no | `core:Equity` | micro-entity |
| equity | 457322 | GBP | 2023-03-31 | 2025-02-04 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 23503 | GBP | 2023-03-31 | 2023-12-22 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 23503 | GBP | 2023-03-31 | 2025-02-04 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 457322 | GBP | 2023-03-31 | 2023-12-22 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 457322 | GBP | 2023-03-31 | 2025-02-04 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 440091 | GBP | 2023-03-31 | 2025-02-04 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 440091 | GBP | 2023-03-31 | 2023-12-22 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 463594 | GBP | 2023-03-31 | 2025-02-04 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 463594 | GBP | 2023-03-31 | 2023-12-22 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 3 | xbrli:pure | 2022-03-31 | 2023-12-22 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 405002 | GBP | 2022-03-31 | 2023-12-22 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 431090 | GBP | 2022-03-31 | 2023-12-22 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 30304 | GBP | 2022-03-31 | 2023-12-22 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 431090 | GBP | 2022-03-31 | 2023-12-22 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 406981 | GBP | 2022-03-31 | 2023-12-22 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 437285 | GBP | 2022-03-31 | 2023-12-22 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## DIGITAL LINES LIMITED (`gb:05293518`)

- registration: `05293518` (GB), status active, incorporated 2004-11-22
- classification: ['61100', '62012'] (sic_2007)
- records: 5 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 60 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-11-30 | 2026-06-09 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 62384 | GBP | 2025-11-30 | 2026-06-09 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 225963 | GBP | 2025-11-30 | 2026-06-09 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 166083 | GBP | 2025-11-30 | 2026-06-09 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 2904 | GBP | 2025-11-30 | 2026-06-09 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 166083 | GBP | 2025-11-30 | 2026-06-09 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 163579 | GBP | 2025-11-30 | 2026-06-09 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 166483 | GBP | 2025-11-30 | 2026-06-09 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-11-30 | 2026-06-09 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-11-30 | 2025-08-18 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 55497 | GBP | 2024-11-30 | 2025-08-18 | filed | no | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 55497 | GBP | 2024-11-30 | 2026-06-09 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 173015 | GBP | 2024-11-30 | 2025-08-18 | filed | no | `core:CurrentAssets` | micro-entity |
| current_assets | 173015 | GBP | 2024-11-30 | 2026-06-09 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 118358 | GBP | 2024-11-30 | 2025-08-18 | filed | no | `core:Equity` | micro-entity |
| equity | 118358 | GBP | 2024-11-30 | 2026-06-09 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 1240 | GBP | 2024-11-30 | 2026-06-09 | filed | yes | `core:FixedAssets` | micro-entity |
| fixed_assets | 1240 | GBP | 2024-11-30 | 2025-08-18 | filed | no | `core:FixedAssets` | micro-entity |
| net_assets | 118358 | GBP | 2024-11-30 | 2026-06-09 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 118358 | GBP | 2024-11-30 | 2025-08-18 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 117518 | GBP | 2024-11-30 | 2025-08-18 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 117518 | GBP | 2024-11-30 | 2026-06-09 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 118758 | GBP | 2024-11-30 | 2026-06-09 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 118758 | GBP | 2024-11-30 | 2025-08-18 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-11-30 | 2025-08-18 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-11-30 | 2024-04-17 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 33899 | GBP | 2023-11-30 | 2025-08-18 | filed | yes | `core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 33899 | GBP | 2023-11-30 | 2024-04-17 | filed | no | `core:Creditors` | micro-entity |
| current_assets | 165516 | GBP | 2023-11-30 | 2025-08-18 | filed | yes | `core:CurrentAssets` | micro-entity |
| current_assets | 165516 | GBP | 2023-11-30 | 2024-04-17 | filed | no | `core:CurrentAssets` | micro-entity |
| equity | 132707 | GBP | 2023-11-30 | 2024-04-17 | filed | no | `core:Equity` | micro-entity |
| equity | 132707 | GBP | 2023-11-30 | 2025-08-18 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 1490 | GBP | 2023-11-30 | 2024-04-17 | filed | no | `core:FixedAssets` | micro-entity |
| fixed_assets | 1490 | GBP | 2023-11-30 | 2025-08-18 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 132707 | GBP | 2023-11-30 | 2025-08-18 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_assets | 132707 | GBP | 2023-11-30 | 2024-04-17 | filed | no | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 131617 | GBP | 2023-11-30 | 2024-04-17 | filed | no | `core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 131617 | GBP | 2023-11-30 | 2025-08-18 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 133107 | GBP | 2023-11-30 | 2025-08-18 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 133107 | GBP | 2023-11-30 | 2024-04-17 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2022-11-30 | 2024-04-17 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 29035 | GBP | 2022-11-30 | 2024-04-17 | filed | yes | `core:Creditors` | micro-entity |
| current_assets | 124791 | GBP | 2022-11-30 | 2024-04-17 | filed | yes | `core:CurrentAssets` | micro-entity |
| equity | 97160 | GBP | 2022-11-30 | 2024-04-17 | filed | yes | `core:Equity` | micro-entity |
| fixed_assets | 1804 | GBP | 2022-11-30 | 2024-04-17 | filed | yes | `core:FixedAssets` | micro-entity |
| net_assets | 97160 | GBP | 2022-11-30 | 2024-04-17 | filed | yes | `core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 95756 | GBP | 2022-11-30 | 2024-04-17 | filed | yes | `core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 97560 | GBP | 2022-11-30 | 2024-04-17 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## RKH DESIGN LTD (`gb:05870984`)

- registration: `05870984` (GB), status active, incorporated 2006-07-10
- classification: ['62020'] (sic_2007)
- records: 5 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 61 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 0 | iso4217:GBP | 2025-03-31 | 2025-12-29 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 3920 | GBP | 2025-03-31 | 2025-12-29 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 4020 | GBP | 2025-03-31 | 2025-12-29 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 100 | GBP | 2025-03-31 | 2025-12-29 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 100 | GBP | 2025-03-31 | 2025-12-29 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 100 | GBP | 2025-03-31 | 2025-12-29 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 100 | GBP | 2025-03-31 | 2025-12-29 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2024-03-31 | 2024-12-30 | filed | no | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 0 | iso4217:GBP | 2024-03-31 | 2025-12-29 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 4490 | GBP | 2024-03-31 | 2024-12-30 | filed | no | `uk-core:Creditors` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 4490 | GBP | 2024-03-31 | 2025-12-29 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 4590 | GBP | 2024-03-31 | 2024-12-30 | filed | no | `uk-core:CurrentAssets` | micro-entity |
| current_assets | 4590 | GBP | 2024-03-31 | 2025-12-29 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 100 | GBP | 2024-03-31 | 2024-12-30 | filed | no | `uk-core:Equity` | micro-entity |
| equity | 100 | GBP | 2024-03-31 | 2025-12-29 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 100 | GBP | 2024-03-31 | 2025-12-29 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_assets | 100 | GBP | 2024-03-31 | 2024-12-30 | filed | no | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 100 | GBP | 2024-03-31 | 2025-12-29 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 100 | GBP | 2024-03-31 | 2024-12-30 | filed | no | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 100 | GBP | 2024-03-31 | 2024-12-30 | filed | no | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 100 | GBP | 2024-03-31 | 2025-12-29 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 1 | iso4217:GBP | 2023-03-30 | 2024-12-30 | filed | yes | `uk-core:AverageNumberEmployeesDuringPeriod` | micro-entity |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 0 | GBP | 2023-03-30 | 2024-12-30 | filed | yes | `uk-core:Creditors` | micro-entity |
| current_assets | 100 | GBP | 2023-03-30 | 2024-12-30 | filed | yes | `uk-core:CurrentAssets` | micro-entity |
| equity | 100 | GBP | 2023-03-30 | 2024-12-30 | filed | yes | `uk-core:Equity` | micro-entity |
| net_assets | 100 | GBP | 2023-03-30 | 2024-12-30 | filed | yes | `uk-core:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 100 | GBP | 2023-03-30 | 2024-12-30 | filed | yes | `uk-core:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 100 | GBP | 2023-03-30 | 2024-12-30 | filed | yes | `uk-core:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## MAKE ONLINE LIMITED (`gb:06364316`)

- registration: `06364316` (GB), status active, incorporated 2007-09-07
- classification: ['62090'] (sic_2007)
- records: 2 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 50 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 1 | xbrli:pure | 2025-09-30 | 2026-01-28 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 105728 | GBP | 2025-09-30 | 2026-01-28 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 82386 | GBP | 2025-09-30 | 2026-01-28 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 132899 | GBP | 2025-09-30 | 2026-01-28 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 27171 | GBP | 2025-09-30 | 2026-01-28 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 27171 | GBP | 2025-09-30 | 2026-01-28 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 10 | GBP | 2025-09-30 | 2026-01-28 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 51838 | GBP | 2025-09-30 | 2026-01-28 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 51848 | GBP | 2025-09-30 | 2026-01-28 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 51848 | GBP | 2025-09-30 | 2026-01-28 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 50513 | GBP | 2025-09-30 | 2026-01-28 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 52161 | GBP | 2025-09-30 | 2026-01-28 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-09-30 | 2026-01-28 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2024-09-30 | 2025-06-30 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 103080 | GBP | 2024-09-30 | 2025-06-30 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 103080 | GBP | 2024-09-30 | 2026-01-28 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 75542 | GBP | 2024-09-30 | 2026-01-28 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 75542 | GBP | 2024-09-30 | 2025-06-30 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 121955 | GBP | 2024-09-30 | 2025-06-30 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 121955 | GBP | 2024-09-30 | 2026-01-28 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 18875 | GBP | 2024-09-30 | 2025-06-30 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 18875 | GBP | 2024-09-30 | 2026-01-28 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 18875 | GBP | 2024-09-30 | 2026-01-28 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors | 18875 | GBP | 2024-09-30 | 2025-06-30 | filed | no | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 10 | GBP | 2024-09-30 | 2026-01-28 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 47728 | GBP | 2024-09-30 | 2026-01-28 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 47738 | GBP | 2024-09-30 | 2026-01-28 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 10 | GBP | 2024-09-30 | 2025-06-30 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 47728 | GBP | 2024-09-30 | 2025-06-30 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 47738 | GBP | 2024-09-30 | 2025-06-30 | filed | no | `core:Equity` | total-exemption-full |
| net_assets | 47738 | GBP | 2024-09-30 | 2026-01-28 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 47738 | GBP | 2024-09-30 | 2025-06-30 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 46413 | GBP | 2024-09-30 | 2026-01-28 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 46413 | GBP | 2024-09-30 | 2025-06-30 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 48049 | GBP | 2024-09-30 | 2026-01-28 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 48049 | GBP | 2024-09-30 | 2025-06-30 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-09-30 | 2025-06-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2023-09-30 | 2024-05-30 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 85844 | GBP | 2023-09-30 | 2025-06-30 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 85844 | GBP | 2023-09-30 | 2024-05-30 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 65185 | GBP | 2023-09-30 | 2024-05-30 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 65185 | GBP | 2023-09-30 | 2025-06-30 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 105335 | GBP | 2023-09-30 | 2025-06-30 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 105335 | GBP | 2023-09-30 | 2024-05-30 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors | 19491 | GBP | 2023-09-30 | 2025-06-30 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 19491 | GBP | 2023-09-30 | 2024-05-30 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 19491 | GBP | 2023-09-30 | 2024-05-30 | filed | no | `core:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 19491 | GBP | 2023-09-30 | 2025-06-30 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 41796 | GBP | 2023-09-30 | 2025-06-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 10 | GBP | 2023-09-30 | 2024-05-30 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 41796 | GBP | 2023-09-30 | 2024-05-30 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 10 | GBP | 2023-09-30 | 2025-06-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 41806 | GBP | 2023-09-30 | 2024-05-30 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 41806 | GBP | 2023-09-30 | 2025-06-30 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 41806 | GBP | 2023-09-30 | 2025-06-30 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 41806 | GBP | 2023-09-30 | 2024-05-30 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 40150 | GBP | 2023-09-30 | 2024-05-30 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 40150 | GBP | 2023-09-30 | 2025-06-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 42195 | GBP | 2023-09-30 | 2025-06-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 42195 | GBP | 2023-09-30 | 2024-05-30 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 1 | xbrli:pure | 2022-09-30 | 2024-05-30 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 71523 | GBP | 2022-09-30 | 2024-05-30 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 59387 | GBP | 2022-09-30 | 2024-05-30 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 96956 | GBP | 2022-09-30 | 2024-05-30 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 25433 | GBP | 2022-09-30 | 2024-05-30 | filed | yes | `core:Debtors` | total-exemption-full |
| debtors `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 25433 | GBP | 2022-09-30 | 2024-05-30 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 38550 | GBP | 2022-09-30 | 2024-05-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 38560 | GBP | 2022-09-30 | 2024-05-30 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital', 'RestatementsFirstTimeAdoptionDimension': 'PreviouslyStatedAmount'}` | 10 | GBP | 2022-09-30 | 2024-05-30 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 38560 | GBP | 2022-09-30 | 2024-05-30 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 37569 | GBP | 2022-09-30 | 2024-05-30 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 38793 | GBP | 2022-09-30 | 2024-05-30 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._

## FRAMPTON TECHNICAL PROJECT SOLUTIONS LIMITED (`gb:06766731`)

- registration: `06766731` (GB), status active, incorporated 2008-12-05
- classification: ['62090'] (sic_2007)
- records: 3 officers, 1 beneficial owners, 0 ownership statements, 0 security interests, 37 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 2 | xbrli:pure | 2025-12-31 | 2026-09-24 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 27685 | GBP | 2025-12-31 | 2026-09-24 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity | 4737 | GBP | 2025-12-31 | 2026-09-24 | filed | yes | `ns5:Equity` | micro-entity |
| fixed_assets | 2237 | GBP | 2025-12-31 | 2026-09-24 | filed | yes | `ns5:FixedAssets` | micro-entity |
| net_assets | 4737 | GBP | 2025-12-31 | 2026-09-24 | filed | yes | `ns5:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 10452 | GBP | 2025-12-31 | 2026-09-24 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 12689 | GBP | 2025-12-31 | 2026-09-24 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-12-31 | 2025-09-23 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2024-12-31 | 2026-09-24 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 38320 | GBP | 2024-12-31 | 2025-09-23 | filed | no | `ns5:CurrentAssets` | micro-entity |
| current_assets | 38320 | GBP | 2024-12-31 | 2026-09-24 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity | 15730 | GBP | 2024-12-31 | 2025-09-23 | filed | no | `ns5:Equity` | micro-entity |
| equity | 15730 | GBP | 2024-12-31 | 2026-09-24 | filed | yes | `ns5:Equity` | micro-entity |
| fixed_assets | 2899 | GBP | 2024-12-31 | 2026-09-24 | filed | yes | `ns5:FixedAssets` | micro-entity |
| fixed_assets | 2899 | GBP | 2024-12-31 | 2025-09-23 | filed | no | `ns5:FixedAssets` | micro-entity |
| net_assets | 15730 | GBP | 2024-12-31 | 2026-09-24 | filed | yes | `ns5:NetAssetsLiabilities` | micro-entity |
| net_assets | 15730 | GBP | 2024-12-31 | 2025-09-23 | filed | no | `ns5:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 14031 | GBP | 2024-12-31 | 2025-09-23 | filed | no | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 14031 | GBP | 2024-12-31 | 2026-09-24 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 16930 | GBP | 2024-12-31 | 2025-09-23 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 16930 | GBP | 2024-12-31 | 2026-09-24 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-12-31 | 2025-09-23 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| average_employees | 2 | xbrli:pure | 2023-12-31 | 2024-09-23 | filed | no | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 24124 | GBP | 2023-12-31 | 2024-09-23 | filed | no | `ns5:CurrentAssets` | micro-entity |
| current_assets | 24124 | GBP | 2023-12-31 | 2025-09-23 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity | 12695 | GBP | 2023-12-31 | 2024-09-23 | filed | no | `ns5:Equity` | micro-entity |
| equity | 12695 | GBP | 2023-12-31 | 2025-09-23 | filed | yes | `ns5:Equity` | micro-entity |
| fixed_assets | 3562 | GBP | 2023-12-31 | 2025-09-23 | filed | yes | `ns5:FixedAssets` | micro-entity |
| fixed_assets | 3562 | GBP | 2023-12-31 | 2024-09-23 | filed | no | `ns5:FixedAssets` | micro-entity |
| net_assets | 12695 | GBP | 2023-12-31 | 2025-09-23 | filed | yes | `ns5:NetAssetsLiabilities` | micro-entity |
| net_assets | 12695 | GBP | 2023-12-31 | 2024-09-23 | filed | no | `ns5:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 12164 | GBP | 2023-12-31 | 2025-09-23 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| net_current_assets | 12164 | GBP | 2023-12-31 | 2024-09-23 | filed | no | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 15726 | GBP | 2023-12-31 | 2024-09-23 | filed | no | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 15726 | GBP | 2023-12-31 | 2025-09-23 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |
| average_employees | 2 | xbrli:pure | 2022-12-31 | 2024-09-23 | filed | yes | `ns5:AverageNumberEmployeesDuringPeriod` | micro-entity |
| current_assets | 55645 | GBP | 2022-12-31 | 2024-09-23 | filed | yes | `ns5:CurrentAssets` | micro-entity |
| equity | 19168 | GBP | 2022-12-31 | 2024-09-23 | filed | yes | `ns5:Equity` | micro-entity |
| fixed_assets | 4554 | GBP | 2022-12-31 | 2024-09-23 | filed | yes | `ns5:FixedAssets` | micro-entity |
| net_assets | 19168 | GBP | 2022-12-31 | 2024-09-23 | filed | yes | `ns5:NetAssetsLiabilities` | micro-entity |
| net_current_assets | 15812 | GBP | 2022-12-31 | 2024-09-23 | filed | yes | `ns5:NetCurrentAssetsLiabilities` | micro-entity |
| total_assets_less_current_liabilities | 20366 | GBP | 2022-12-31 | 2024-09-23 | filed | yes | `ns5:TotalAssetsLessCurrentLiabilities` | micro-entity |

_No coverage facts for the latest run._

## TECH RECYCLE LIMITED (`gb:07278838`)

- registration: `07278838` (GB), status active, incorporated 2010-06-09
- classification: ['62020'] (sic_2007)
- records: 5 officers, 3 beneficial owners, 0 ownership statements, 1 security interests, 66 filings, 0 events, 3 source documents

| concept | value | unit | period end | filed | basis | current | source tag | regime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average_employees | 23 | xbrli:pure | 2023-06-30 | 2024-03-28 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 176642 | GBP | 2023-06-30 | 2024-03-28 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 268074 | GBP | 2023-06-30 | 2024-03-28 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 398732 | GBP | 2023-06-30 | 2024-03-28 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 698384 | GBP | 2023-06-30 | 2024-03-28 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 521742 | GBP | 2023-06-30 | 2024-03-28 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | 222007 | GBP | 2023-06-30 | 2024-03-28 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 300 | GBP | 2023-06-30 | 2024-03-28 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 221657 | GBP | 2023-06-30 | 2024-03-28 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 50 | GBP | 2023-06-30 | 2024-03-28 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | 222007 | GBP | 2023-06-30 | 2024-03-28 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 299652 | GBP | 2023-06-30 | 2024-03-28 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 490081 | GBP | 2023-06-30 | 2024-03-28 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 28 | xbrli:pure | 2022-06-30 | 2023-03-24 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 28 | xbrli:pure | 2022-06-30 | 2024-03-28 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 257249 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| cash | 257249 | GBP | 2022-06-30 | 2023-03-24 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 263794 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 263794 | GBP | 2022-06-30 | 2023-03-24 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 379103 | GBP | 2022-06-30 | 2023-03-24 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 379103 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 599732 | GBP | 2022-06-30 | 2023-03-24 | filed | no | `core:CurrentAssets` | total-exemption-full |
| current_assets | 599732 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 342483 | GBP | 2022-06-30 | 2023-03-24 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 342483 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 300 | GBP | 2022-06-30 | 2023-03-24 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 171996 | GBP | 2022-06-30 | 2023-03-24 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 50 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 171996 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 300 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 179290 | GBP | 2022-06-30 | 2023-03-24 | filed | no | `core:Equity` | total-exemption-full |
| equity | 179290 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 6944 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 6944 | GBP | 2022-06-30 | 2023-03-24 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 50 | GBP | 2022-06-30 | 2023-03-24 | filed | no | `core:Equity` | total-exemption-full |
| net_assets | 179290 | GBP | 2022-06-30 | 2023-03-24 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 179290 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 220629 | GBP | 2022-06-30 | 2023-03-24 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 220629 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 443084 | GBP | 2022-06-30 | 2024-03-28 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 443084 | GBP | 2022-06-30 | 2023-03-24 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 20 | xbrli:pure | 2021-06-30 | 2022-03-22 | filed | no | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| average_employees | 20 | xbrli:pure | 2021-06-30 | 2023-03-24 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 244371 | GBP | 2021-06-30 | 2022-03-22 | filed | no | `core:CashBankOnHand` | total-exemption-full |
| cash | 244371 | GBP | 2021-06-30 | 2023-03-24 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 292087 | GBP | 2021-06-30 | 2023-03-24 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 292087 | GBP | 2021-06-30 | 2022-03-22 | filed | no | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 302093 | GBP | 2021-06-30 | 2023-03-24 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 302093 | GBP | 2021-06-30 | 2022-03-22 | filed | no | `core:Creditors` | total-exemption-full |
| current_assets | 470685 | GBP | 2021-06-30 | 2023-03-24 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| current_assets | 470685 | GBP | 2021-06-30 | 2022-03-22 | filed | no | `core:CurrentAssets` | total-exemption-full |
| debtors | 226314 | GBP | 2021-06-30 | 2022-03-22 | filed | no | `core:Debtors` | total-exemption-full |
| debtors | 226314 | GBP | 2021-06-30 | 2023-03-24 | filed | yes | `core:Debtors` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 90 | GBP | 2021-06-30 | 2022-03-22 | filed | no | `core:Equity` | total-exemption-full |
| equity | 7384 | GBP | 2021-06-30 | 2022-03-22 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 50 | GBP | 2021-06-30 | 2023-03-24 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 300 | GBP | 2021-06-30 | 2023-03-24 | filed | yes | `core:Equity` | total-exemption-full |
| equity | 7384 | GBP | 2021-06-30 | 2023-03-24 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 300 | GBP | 2021-06-30 | 2022-03-22 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 50 | GBP | 2021-06-30 | 2022-03-22 | filed | no | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | 90 | GBP | 2021-06-30 | 2023-03-24 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 6944 | GBP | 2021-06-30 | 2023-03-24 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 6944 | GBP | 2021-06-30 | 2022-03-22 | filed | no | `core:Equity` | total-exemption-full |
| net_assets | 7384 | GBP | 2021-06-30 | 2022-03-22 | filed | no | `core:NetAssetsLiabilities` | total-exemption-full |
| net_assets | 7384 | GBP | 2021-06-30 | 2023-03-24 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | 168592 | GBP | 2021-06-30 | 2023-03-24 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| net_current_assets | 168592 | GBP | 2021-06-30 | 2022-03-22 | filed | no | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 299471 | GBP | 2021-06-30 | 2023-03-24 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 299471 | GBP | 2021-06-30 | 2022-03-22 | filed | no | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |
| average_employees | 5 | xbrli:pure | 2020-06-30 | 2022-03-22 | filed | yes | `core:AverageNumberEmployeesDuringPeriod` | total-exemption-full |
| cash | 164704 | GBP | 2020-06-30 | 2022-03-22 | filed | yes | `core:CashBankOnHand` | total-exemption-full |
| creditors_after_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'AfterOneYear'}` | 139265 | GBP | 2020-06-30 | 2022-03-22 | filed | yes | `core:Creditors` | total-exemption-full |
| creditors_within_one_year `{'MaturitiesOrExpirationPeriodsDimension': 'WithinOneYear'}` | 239271 | GBP | 2020-06-30 | 2022-03-22 | filed | yes | `core:Creditors` | total-exemption-full |
| current_assets | 205195 | GBP | 2020-06-30 | 2022-03-22 | filed | yes | `core:CurrentAssets` | total-exemption-full |
| debtors | 40491 | GBP | 2020-06-30 | 2022-03-22 | filed | yes | `core:Debtors` | total-exemption-full |
| equity | -51750 | GBP | 2020-06-30 | 2022-03-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'CapitalRedemptionReserve'}` | 50 | GBP | 2020-06-30 | 2022-03-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RevaluationReserve'}` | 6944 | GBP | 2020-06-30 | 2022-03-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'ShareCapital'}` | 285 | GBP | 2020-06-30 | 2022-03-22 | filed | yes | `core:Equity` | total-exemption-full |
| equity `{'EquityClassesDimension': 'RetainedEarningsAccumulatedLosses'}` | -59029 | GBP | 2020-06-30 | 2022-03-22 | filed | yes | `core:Equity` | total-exemption-full |
| net_assets | -51750 | GBP | 2020-06-30 | 2022-03-22 | filed | yes | `core:NetAssetsLiabilities` | total-exemption-full |
| net_current_assets | -34076 | GBP | 2020-06-30 | 2022-03-22 | filed | yes | `core:NetCurrentAssetsLiabilities` | total-exemption-full |
| total_assets_less_current_liabilities | 87515 | GBP | 2020-06-30 | 2022-03-22 | filed | yes | `core:TotalAssetsLessCurrentLiabilities` | total-exemption-full |

_No coverage facts for the latest run._
