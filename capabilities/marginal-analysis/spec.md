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
| FARMER_WAGE | =50,000 / 1,440 ($34.7222...) | $/hr | derived from the $50,000 farmer salary ÷ 1,440 hrs rather than the rounded display figure |
| TEMP_WORKERS_MAX | 4 | count | case scenario table |
| TEMP_HOURS_PER_WORKER | 1,440 | hrs | case scenario table |
| TEMP_WAGE | =25,000 / 1,440 ($17.3611...) | $/hr | derived the same way as FARMER_WAGE |
| BED_CAP_TOMATO | 20 | beds | case scenario table |
| PRICE_TOMATO | 8,800 | $/bed | case scenario table |
| HRS_PER_BED_TOMATO | 2.50 | hrs/week/bed | case scenario table |
| FERT_TOMATO | 880 | $/bed | case scenario table |
| DIM_PCT_TOMATO | 10.00% | %/bed | case scenario table |
| BED_CAP_CARROT | 20 | beds | case scenario table |
| PRICE_CARROT | 2,094 | $/bed | case scenario table |
| HRS_PER_BED_CARROT | =5/6 (0.8333...) | hrs/week/bed | stored as the exact fraction rather than the rounded 0.833 display figure |
| FERT_CARROT | 440 | $/bed | case scenario table |
| DIM_PCT_CARROT | 2.50% | %/bed | case scenario table |
| BED_CAP_MESCLUN | 30 | beds | case scenario table |
| PRICE_MESCLUN | 2,700 | $/bed | case scenario table |
| HRS_PER_BED_MESCLUN | 1.25 | hrs/week/bed | case scenario table |
| FERT_MESCLUN | 880 | $/bed | case scenario table |
| DIM_PCT_MESCLUN | 1.25% | %/bed | case scenario table |


## Method

**Structure:**
- Inputs sheet — all named inputs above, one per row. FARMER_WAGE, TEMP_WAGE, and HRS_PER_BED_CARROT are entered as formulas deriving the exact value from its underlying source, not as typed, rounded decimals — any input whose case-scenario source is itself a ratio (a salary over annual hours, a fraction of an hour) is stored as that ratio, never as a rounded display figure, so no input on this sheet silently drifts from its source.
- Labor sheet — labor hours per bed count, per crop, using the labor formula
- Cost sheet — labor cost, fertilizer cost, revenue, and marginal cost per bed count, per crop
- Optimization sheet — the three bed-count changing cells, the constraints, and the Solver setup. The bed-cap column (C5:C7) references the named bed-cap inputs directly (=BED_CAP_TOMATO, =BED_CAP_CARROT, =BED_CAP_MESCLUN), not typed numbers, so it cannot drift out of sync with the Checks sheet or the Inputs sheet.
- Checks sheet — the q=1 hand check, the check-figure comparisons, and pass/fail flags

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

## Validation tolerances
A check with no tolerance either passes by luck or fails on rounding, and neither outcome tells you anything, so every check-figure comparison below uses one:

- Season profit: within $5 of the published figure.
- Optimal bed counts, standalone crossing points: exact — these are integer decisions, so any deviation reflects a real disagreement, not rounding.
- Hand-check hours (LABOR_HRS_TOMATO(1)): within 0.01 hours.
  
## Reproduction

Steps to reproduce this model's results from model.xlsx:

1. Open model.xlsx in Excel desktop (not the web version — Solver requires the desktop app).
2. Confirm all inputs on the Inputs sheet match the values in the table above, including the three derived-formula cells (FARMER_WAGE, TEMP_WAGE, HRS_PER_BED_CARROT).
3. By hand, verify LABOR_HRS_TOMATO(1) = 1 × 2.50 × 36 × 1.10 hours.
4. Open Solver, set changing cells to the three bed counts, objective to maximize profit, method to GRG Nonlinear with integer constraints, and constraints per the case (bed caps, 64 total, ≤4 temp workers).
5. Run Solver starting from bed counts 0/0/0; record the result.
6. Reset and run Solver again starting from 20/0/0; record the result and compare to step 5.
7. Confirm the optimal mix equals Tomatoes 10, Carrots 20, Mesclun 30, and season profit is within $5 of $42,762.
8. Confirm no error cells (#REF!, #DIV/0!, #NAME?) and that every calculated cell contains a formula, not a pasted value.
9. Confirm all constraint-check cells show as satisfied.

## Audit Findings

- Named ranges: Spot-checked several input cells (PRICE_TOMATO, WEEKS, FARMER_WAGE, DIM_PCT_TOMATO, and others) via the Name Box and the named-range dropdown. All confirmed as proper named ranges matching the spec.
- Solver constraints — critical defect found and fixed: The initial build had zero constraints entered in Solver. Running the optimizer with no constraints produced 74 total beds and a profit of $45,039 — both physically impossible under the case's 64-bed limit, and higher than the correct answer. After adding all required constraints (tomato beds ≤ 20, carrot beds ≤ 20, mesclun beds ≤ 30, total beds ≤ 64, temp workers ≤ 4, and integer constraints on the three bed-count cells), re-running Solver produced results close to Tomatoes 10 / Carrots 20 / Mesclun 30 with profit near $42,762 — matching the published check figures. This is recorded as a structural defect in the initial AI-generated build, corrected through the spec-audit-regenerate loop.
- q=1 hand check: By hand, 1 bed of tomatoes should require 1 × 2.50 × 36 × 1.10 = 99 hours - confirmed.
- Error cell scan: Scanned all sheets via Ctrl+F for #REF!, #DIV/0!, and #NAME? — none found.
- Wage-rate rounding — defect found and fixed: FARMER_WAGE and TEMP_WAGE were entered as typed, rounded decimals ($34.72 and $17.36) instead of the exact ratios ($50,000/1,440 and $25,000/1,440). Same issue with HRS_PER_BED_CARROT, entered as 0.833 instead of 5/6. This produced a Checks-sheet profit of $42,775.16 against the published $42,762 — a FAIL. Fixed by replacing each with a formula deriving the exact value from its source, and added a $5 tolerance to the profit check going forward, since exact-cent matching against a rounded published figure isn't a meaningful bar.
- Pasted-value cap cells — defect found and fixed: Optimization!C5:C7 (the bed-cap column) were typed constants instead of formulas — and two of them (C6, C7) were simply wrong (0 instead of 20 and 30). This made the Optimization sheet show Carrots and Mesclun as VIOLATED even though the Checks sheet, which references the named ranges directly, correctly showed them SATISFIED. The integrity check (calculated cells that aren't formulas) also flagged these same three cells. Fixed by replacing each with a direct reference to its named bed-cap input (=BED_CAP_TOMATO, =BED_CAP_CARROT, =BED_CAP_MESCLUN).

