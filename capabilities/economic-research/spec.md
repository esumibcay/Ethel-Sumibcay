# Spec: Economic Research Paper

## Decision-maker and case hospital

The paper is written for the chief financial officer of a U.S. nonprofit
community hospital with about 490 RNs, deciding whether to fund a nurse
retention program. The hospital is set to match the average hospital in the
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
  the retention program's 2013 costs to 2025 dollars.
- **Retention program:** Silvestre, J. H., Ulrich, B. T., Johnson, T.,
  Spector, N., & Blegen, M. A. (2017). A multisite study on a new graduate
  registered nurse transition to practice program: Return on investment.
  *Nursing Economic$, 35*(3), 110–118. Randomized, controlled, multisite
  design; 1,032 new graduates in 70 hospitals. Reported 12-month turnover:
  15.5% with the program, 26.8% without (limited-control group). Reported cost
  per new graduate: $3,185 ongoing plus $723 one-time development = $3,908, in
  2013 dollars. Mean new-graduate hires per hospital: 15.
- **Care quality (cited context, not a link in the chain):** Aiken, L. H.,
  Clarke, S. P., Sloane, D. M., Sochalski, J., & Silber, J. H. (2002). Hospital
  nurse staffing and patient mortality, nurse burnout, and job dissatisfaction.
  *JAMA, 288*(16), 1987–1993. Record its reported effect size.

_Files in `data/`: `nsi_2026_retention_report.pdf`, `nsi_turnover.csv`,
`nsi_cost.csv`, `oews_rn_2015_2019.csv`, `cpi_u_annual.csv`. Source,
publication/pull date, and transformations for each are recorded in
`data/README.md`._

## Model / analysis plan

The mechanism is a chain of three links:

Inelastic RN supply → costly turnover → a retention program that pays for itself

1. **RN supply is inelastic.** Compute the observed employment–wage ratio:
   cumulative % change in RN employment ÷ cumulative % change in the real median
   RN wage, May 2015–May 2019.
   *Caveat:* this ratio equals the supply elasticity only if the observed changes
   came from demand shifting along a stable supply curve. Demand did shift
   (population aging, rising patient acuity), which is the movement that traces
   out supply, but supply may also have shifted (retirements, changes in
   nursing-school capacity). The paper therefore calls it an *observed
   employment–wage ratio* and treats a value below 1.0 as consistent with
   inelastic supply, not as a precise elasticity. The 2015–2019 window is chosen
   to avoid the 2020–2021 pandemic shock to supply.
2. **Turnover is costly.** Report the NSI staff RN turnover rate for 2023–2025
   and the cost per RN turnover. At 17.6% turnover, the case hospital loses
   about 86 RNs a year, costing about $5.2 million.
3. **A retention program pays for itself.** ROI bridge from Silvestre et al.
   (2017) to the case hospital:
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

   *Base case vs. conservative case:* the base case uses the full $3,908 per new
   graduate, including one-time development. A hospital adopting an existing
   program might pay only the $3,185 ongoing cost; the paper reports this as a
   secondary figure.

   *Scale:* the program covers only new graduates (about 15 of roughly 86
   annual departures), so it addresses a small share of the hospital's total
   turnover cost. The paper states this directly in the recommendation.

   Wage increases, bonuses, and working-condition changes are discussed as
   alternatives but not computed, because none has a published evaluation with a
   cost and an effect that can be moved to a single hospital.

**Recommendation:** the paper ends with a recommendation to the CFO (fund the
program or not), then recomputes the ROI ratio with the program's effect cut in
half (a 5.65-point turnover reduction) to test whether the recommendation holds.

## Figures planned

**Figure 1:** annual % change in RN employment (y-axis) against annual % change
in the real median RN wage (x-axis), BLS OEWS, May 2015–May 2019, wages deflated
by CPI-U. The figure matches the definition in link 1.

**Reading rule:** if the observed employment–wage ratio over the window is below
1.0, the figure supports link 1. At 1.0 or higher, link 1 fails, and the paper
reports that hospitals could hire their way out of turnover.

## Success criteria

A finished paper has to:

- Report the observed employment–wage ratio from OEWS and CPI-U, with Figure 1,
  and state plainly whether it supports or weakens the inelastic-supply claim.
- Report the NSI turnover trend for 2023–2025 and the cost per turnover, with the
  2026 edition cited.
- Compute the ROI ratio for the case hospital using the bridge above, not just
  quote the published figure, and state the new-graduate hiring assumption.
- Cite Aiken et al. (2002) for the staffing-to-quality link.
- End with a recommendation to the CFO, including the half-effect check and the
  program's share of total turnover cost.

## Falsification thresholds

These match the brief's "What would prove me wrong" and were set before any data
were pulled:

- **Link 1 fails** if the observed employment–wage ratio is 1.0 or higher.
- **Link 2 fails** if NSI RN turnover rose by less than 1.0 percentage point
  over 2023–2025. If it fails, the paper reports it; the ROI in link 3 depends
  on the level of turnover and cost per departure, not on the trend.
- **Link 3 fails** if the program's annual cost exceeds 100% of the annual
  turnover cost it avoids (ROI ratio below 1.0).
