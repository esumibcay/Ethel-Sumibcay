# Spec: Economic Research Paper

## Decision-maker and case hospital

The paper is written for the chief financial officer of a U.S. nonprofit
community hospital with about 490 RNs, deciding whether to fund a nurse
residency program. The hospital is set to match the average hospital in the
NSI 2026 report: NSI reports that each 1-point change in RN turnover costs the
average hospital $294,976 a year, and $294,976 ÷ $60,090 per turnover
≈ 4.91 departures per point, which implies about 490 RNs.

## Data sources

- **Turnover and turnover cost:** NSI Nursing Solutions, Inc. (2026). *2026 NSI
  National Health Care Retention & RN Staffing Report* (covers January–December
  2025). Staff RN turnover rate for 2023–2025 and average cost per RN turnover
  ($60,090). Vacancy rates are not used.
- **Employment and wages:** U.S. Bureau of Labor Statistics, Occupational
  Employment and Wage Statistics (OEWS), national estimates for Registered Nurses
  (SOC 29-1141): employment and median annual wage, May 2015–May 2019.
- **Deflator:** U.S. Bureau of Labor Statistics, Consumer Price Index for All
  Urban Consumers (CPI-U), U.S. city average, annual averages for 2013 and
  2015–2025. Used to convert OEWS median wages to real dollars and to convert
  the program's 2013 costs to 2025 dollars.
- **Nurse residency program:** the new-graduate transition-to-practice program
  in Silvestre, J. H., Ulrich, B. T., Johnson, T., Spector, N., & Blegen, M. A.
  (2017). A multisite study on a new graduate registered nurse transition to
  practice program: Return on investment. *Nursing Economic$, 35*(3), 110–118.
  Randomized, controlled, multisite design; 1,032 new graduates in 70
  hospitals. Reported 12-month turnover: 15.5% with the program, 26.8% without
  (limited-control group). Reported cost per new graduate: $3,185 ongoing plus
  $723 one-time development = $3,908, in 2013 dollars. Mean new-graduate hires
  per hospital: 15.
- **Care quality (cited context, not a link in the chain):** Aiken, L. H.,
  Clarke, S. P., Sloane, D. M., Sochalski, J., & Silber, J. H. (2002). Hospital
  nurse staffing and patient mortality, nurse burnout, and job dissatisfaction.
  *JAMA, 288*(16), 1987–1993. Effect size: each additional patient per nurse
  → 7% higher odds of 30-day mortality (OR 1.07, 95% CI 1.03–1.12); surgical
  patients, 168 hospitals.

_Files in `data/`: `nsi_turnover.csv`,
`nsi_cost.csv`, `oews_rn_2015_2019.csv`, `cpi_u_annual.csv`. Source,
publication/pull date, and transformations for each are recorded in
`data/README.md`._

## Model / analysis plan

The mechanism is a chain of three links:

Inelastic RN supply → turnover costs → a nurse residency program that pays for
itself

1. **RN supply is inelastic.** Compute the observed employment–wage ratio:
   cumulative % change in RN employment ÷ cumulative % change in the real median
   RN wage, May 2015–May 2019.
   *Caveat:* this ratio equals the supply elasticity only if the observed changes
   came from demand shifting along a stable supply curve. Demand did shift
   (population aging, rising patient acuity), but supply may also have shifted
   (new graduates, changes in nursing-school capacity, retirements). The paper
   therefore calls it an *observed employment–wage ratio* and treats a value
   below 1.0 as consistent with inelastic supply, not as a precise elasticity.
   The 2015–2019 window is chosen to avoid the 2020–2021 pandemic shock.
   Links 2 and 3 do not depend on this link.
2. **Turnover is costly.** Report the NSI staff RN turnover rate for 2023–2025
   and the cost per RN turnover. At 17.6% turnover, the case hospital loses
   about 86 RNs a year, costing about $5.2 million.
3. **The nurse residency program pays for itself.** ROI bridge from Silvestre
   et al. (2017) to the case hospital:
   - New-graduate hires per year = 15, the mean reported by Silvestre et al.
     (2017) across study hospitals (stated assumption)
   - Turnover reduction = 26.8% − 15.5% = 11.3 percentage points
   - Avoided departures = 15 × 0.113
   - Avoided cost = avoided departures × $60,090 (NSI 2026 cost per RN turnover)
   - Program cost = 15 × $3,908, converted from 2013 to 2025 dollars by CPI-U
     (2025 CPI-U ÷ 2013 CPI-U)
   - ROI ratio = avoided cost ÷ program cost

   *Why the ratio is ours:* Silvestre et al. computed savings using replacement
   costs of $41,085 (Lewin Group) and $98,879 (Jones), both in 2013 dollars.
   This paper substitutes NSI's current $60,090 and applies the study's effect
   to the case hospital's hiring volume, so the ROI is computed, not quoted.

   *Full cost vs. ongoing cost:* the base case uses the full $3,908 per new
   graduate, including one-time development. A hospital adopting an existing
   program might pay only the $3,185 ongoing cost; the paper reports both.

   *Scale:* the program reaches only the 15 new graduates hired each year; at the published effect it prevents about 1.7 of roughly 86 annual departures (about 2%). The paper states this directly in the recommendation.

   Wage increases, bonuses, and working-condition changes are discussed as
   alternatives but not computed, because none has a published evaluation with a
   cost and an effect that can be moved to a single hospital.

**Recommendation:** the paper ends with a conditional recommendation to the
CFO, built around the half-effect result: the ROI ratio recomputed with the
program's effect cut in half (a 5.65-point turnover reduction), on both full
and ongoing-only cost, and the break-even share of the published effect shown
in Figure 2. The recommendation states the condition under which the hospital
should fund the program.

## Figures planned

**Figure 1 (link 1):** annual % change in RN employment (y-axis) against annual
% change in the real median RN wage (x-axis), BLS OEWS, May 2016–May 2019, wages
deflated by CPI-U, with a reference line where the ratio equals 1.0. Drawn by
`analysis/figures/fig1.py`.

**Reading rule:** points below the reference line are consistent with inelastic
supply; points above it are not. The cumulative 2015–2019 ratio is stated in
the caption.

**Figure 2 (link 3):** ROI ratio (y-axis) against the share of the published
turnover effect the hospital achieves (x-axis, 0–100%), with two lines — full
cost ($3,908 per new graduate) and ongoing cost only ($3,185) — and a
horizontal break-even line at 1.0. Drawn by `analysis/figures/fig2.py`.

**Reading rule:** where each line crosses 1.0 is the minimum share of the
published effect the hospital must achieve for the program to pay for itself.
The half-effect point (50%) is marked on both lines.

## Success criteria

A finished paper has to:

- Report the observed employment–wage ratio with Figure 1 and state plainly
  that it does not support the inelastic-supply claim.
- Report the NSI turnover trend for 2023–2025 as it is, and the cost per
  turnover, with the 2026 edition cited.
- Compute the ROI ratio for the case hospital using the bridge above, not just
  quote the published figure, and state the new-graduate hiring assumption.
- Include Figure 2 with its break-even points.
- Cite Aiken et al. (2002) for the staffing-to-quality link.
- End with a conditional recommendation to the CFO, including the half-effect
  result on both cost bases and the program's share of total turnover cost.

## Falsification thresholds

These match the brief's "What would prove me wrong" and were set before any data
were pulled:

- **Link 1 fails** if the observed employment–wage ratio is 1.0 or higher.
- **Link 2 fails** if NSI RN turnover rose by less than 1.0 percentage point
  over 2023–2025. If it fails, the paper reports it; the ROI in link 3 depends
  on the level of turnover and cost per departure, not on the trend.
- **Link 3 fails** if the program's annual cost exceeds 100% of the annual
  turnover cost it avoids (ROI ratio below 1.0).

## Results against thresholds

Pulled 2026-09-24. Thresholds unchanged from the pre-data version. No other
years or measures were tried for link 1.

- **Link 1 — fails.** Employment +8.6% (2,745,910 → 2,982,280); real median
  wage +0.7% ($72,804 → $73,299 in 2019 dollars). Ratio ≈ 12.7 (≈ 12.2 in log
  changes). Every year-over-year pair is also above 1.0. The paper reports that
  this measure does not show inelastic supply; a ratio this large likely
  reflects supply and demand shifting together.
- **Link 2 — fails on trend, holds on level.** Turnover 18.4% → 16.4% → 17.6%
  (−0.8 points). The paper reports the trend in one sentence and relies on the
  level (17.6%) and cost per departure ($60,090).
- **Link 3 — conditional.** Avoided cost = 15 × 0.113 × $60,090 = $101,853.
  Program cost (CPI-U factor 321.943 ÷ 232.957 = 1.382): $81,012 full, $66,024
  ongoing only.

  | | Full effect | Half effect | Break-even share |
  |---|---|---|---|
  | Full cost | 1.26 | 0.63 | ~80% |
  | Ongoing cost only | 1.54 | 0.77 | ~65% |
