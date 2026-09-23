# Spec: Economic Research Paper

## Data sources

- **Turnover and vacancy trends, and turnover cost:** NSI Nursing Solutions' annual *National Health Care Retention & RN Staffing Report* — publishes RN turnover rate, vacancy rate, and average cost-per-turnover figures by year. Pull the most recent 3-5 years to show trend, and cite the specific year/edition used.
- **Wage inflation and labor supply elasticity:** U.S. Bureau of Labor Statistics Occupational Employment and Wage Statistics (OEWS) for Registered Nurses — median annual wage and employment counts by year. Elasticity is approximated as % change in RN employment ÷ % change in real median wage over the same period.
- **Patient safety indicator:** a peer-reviewed staffing-outcomes source rather than a live series — e.g. the Aiken et al. nurse-to-patient-ratio and patient-mortality literature, or an AHRQ Quality Indicators report linking nurse staffing to adverse events. This is a cited estimate, not something measured from raw data, so record the exact study and its reported effect size.
- **Retention-strategy ROI:** one published case study or cost-benefit analysis of a specific retention program (e.g., a sign-on/retention bonus program, or a nurse residency/career-development program) — needs a specific citation with reported cost and reported retention or turnover-reduction effect, so a real ROI ratio can be computed or quoted rather than estimated.
- **Global migration context (one sentence, one stat):** WHO National Health Workforce Accounts or OECD Health Workforce Migration data — a single figure, foreign-trained nurses as a share of the workforce, case-study country vs. OECD average, most recent year available. Cited in-line to support the research question's "driven partly by global migration pressures" clause; not its own subsection in the paper.

_Record source, exact publication/date pulled, and any transformations (e.g., wage series deflated to real dollars) in `data/` per its README, for every series above._

## Model / analysis plan

The mechanism traced is: inelastic nursing labor supply → turnover stays high even as wages rise → high turnover drives direct costs (replacement, overtime, travel-nurse spend) and reduced staffing → reduced staffing correlates with worse patient-safety indicators → a retention strategy that reduces turnover pays for itself if its cost is lower than the turnover cost it avoids. Global migration is folded in as one driver of the labor-supply side of that mechanism, not a parallel analysis track.

Shown in three steps: (1) plot wage change against vacancy/employment change to demonstrate inelasticity, (2) tie the turnover/vacancy trend to its dollar cost using NSI's reported cost-per-turnover figure, (3) compute or cite the ROI of the chosen retention strategy as (turnover cost avoided) ÷ (program cost), and compare that ratio against the cost of continuing at the current turnover rate.

## Figures planned

One chart: RN wage growth (%) plotted against RN vacancy or turnover rate (%) over the same multi-year period. This is the figure the elasticity claim actually needs — a flat or shallow relationship supports "inelastic," a steep negative relationship would be evidence against the paper's central claim (see Success criteria and the brief's "What would prove me wrong").

## Success criteria

A finished paper has to:

- Show the turnover/vacancy trend with real, cited NSI figures and the dollar cost tied to it.
- Show the wage-vacancy relationship in the figure above, and state plainly whether it supports or weakens the inelastic-supply claim.
- Cite a specific, named study for the staffing-to-patient-safety link, not a general assertion.
- Report an ROI figure (or a cited one) for the chosen retention strategy, compared against the cost of unaddressed turnover, and cite the WHO/OECD migration stat in the same pass rather than as a separate section.

The hypothesis is weakened, per the brief's falsification section, if: the pulled turnover/vacancy series is flat or declining rather than rising; the wage-vacancy figure shows a strong negative relationship (elastic supply); the cited safety study shows no meaningful staffing-outcome link; the retention-strategy source shows a cost that exceeds the turnover cost it avoids; or migration data shows no meaningful contribution to the case-study country's shortage.
