# Spec: Marginal Analysis

## Purpose

This model determines how many beds of tomatoes, carrots, and mesclun a market garden should plant across 64 available beds to maximize season profit, given that the farm is a price taker (P = MC governs the supply decision) and each crop's labor requirement rises with the number of beds planted (diminishing returns).

## Inputs

| Name | Value | Unit | Source |
|---|---|---|---|
| WEEKS | 36 | weeks | case scenario table |
| TOTAL_BEDS | 64 | beds | case scenario table |
| FIXED_COST | 20,000 | $ | case scenario table |
| FARMER_HOURS | 720 | hrs | case scenario table |
| FARMER_WAGE | 34.72 | $/hr | case scenario table |
| TEMP_WORKERS_MAX | 4 | count | case scenario table |
| TEMP_HOURS_PER_WORKER | 1,440 | hrs | case scenario table |
| TEMP_WAGE | 17.36 | $/hr | case scenario table |
| BED_CAP_TOMATO | 20 | beds | case scenario table |
| PRICE_TOMATO | 8,800 | $/bed | case scenario table |
| HRS_PER_BED_TOMATO | 2.50 | hrs/week/bed | case scenario table |
| FERT_TOMATO | 880 | $/bed | case scenario table |
| DIM_PCT_TOMATO | 10.00% | %/bed | case scenario table |
| BED_CAP_CARROT | 20 | beds | case scenario table |
| PRICE_CARROT | 2,094 | $/bed | case scenario table |
| HRS_PER_BED_CARROT | 0.833 | hrs/week/bed | case scenario table |
| FERT_CARROT | 440 | $/bed | case scenario table |
| DIM_PCT_CARROT | 2.50% | %/bed | case scenario table |
| BED_CAP_MESCLUN | 30 | beds | case scenario table |
| PRICE_MESCLUN | 2,700 | $/bed | case scenario table |
| HRS_PER_BED_MESCLUN | 1.25 | hrs/week/bed | case scenario table |
| FERT_MESCLUN | 880 | $/bed | case scenario table |
| DIM_PCT_MESCLUN | 1.25% | %/bed | case scenario table |

## Method

**Structure:**
- **Inputs sheet** — all named inputs above, one per row
- **Labor sheet** — labor hours per bed count, per crop, using the labor formula
- **Cost sheet** — labor cost, fertilizer cost, revenue, and marginal cost per bed count, per crop
- **Optimization sheet** — the three bed-count changing cells, the constraints, and the Solver setup
- **Checks sheet** — the q=1 hand check, the check-figure comparisons, and pass/fail flags

**Calculation logic:**
- LABOR_HRS_CROP(q) = q × HRS_PER_BED_CROP × WEEKS × (1 + DIM_PCT_CROP)^q, for each crop
- The farmer's 720 hours are applied against total combined labor hours across all three crops first, regardless of which crop the hours belong to. Any labor hours beyond 720 are covered by temporary workers, up to 4 workers × 1,440 hours each.
- Labor cost for every crop is priced using one blended rate, calculated as total labor dollars divided by total labor hours across the whole farm.
- Marginal cost for each crop is calculated as the labor cost of q beds minus the labor cost of q−1 beds, computed the same way at every bed count — the model should not assume marginal cost only increases.
- Profit = total revenue (price × beds, summed across all three crops) − total labor cost − total fertilizer cost − $20,000 fixed cost.
- Optimization: maximize profit; changing cells are the three bed counts; method is GRG Nonlinear with integer decisions; constraints are the three bed caps, 64 beds total, and temporary workers ≤ 4.

## Outputs

- Optimal number of beds per crop (tomatoes, carrots, mesclun)
- Total season profit
- Marginal cost at each bed count, per crop
- Standalone price ≈ marginal cost crossing point, per crop
- Value of relaxing a binding bed-cap constraint (shadow price), per crop

## Reproduction

Steps to reproduce this model's results from `model.xlsx`:
1. Open `model.xlsx` in Excel desktop (not the web version — Solver requires the desktop app).
2. Confirm all inputs on the Inputs sheet match the values in the table above.
3. By hand, verify LABOR_HRS_TOMATO(1) = 1 × 2.50 × 36 × 1.10 hours.
4. Open Solver, set changing cells to the three bed counts, objective to maximize profit, method to GRG Nonlinear with integer constraints, and constraints per the case (bed caps, 64 total, ≤4 temp workers).
5. Run Solver starting from bed counts 0/0/0; record the result.
6. Reset and run Solver again starting from 20/0/0; record the result and compare to step 5.
7. Confirm the optimal mix equals Tomatoes 10, Carrots 20, Mesclun 30, and season profit equals $42,762.
8. Confirm no error cells (#REF!, #DIV/0!, #NAME?) and that every calculated cell contains a formula, not a pasted value.
9. Confirm all constraint-check cells show as satisfied.
