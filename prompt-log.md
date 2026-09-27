# Prompt Log

A running record of significant AI sessions — not every prompt, but the ones that shaped a decision, a model, or a piece of writing in this repo.

## 2026-08-18 — Repo scaffolding (Claude)

Used Claude to generate the initial repository structure following the [portfolio repo guide](https://adamwstauffer.github.io/ai-lms/portfolio-repo.html): root files, `.claude/skills/`, `capabilities/marginal-analysis/`, `docs/briefs/`, `docs/decisions/`, `data/`, `analysis/figures/`. All biographical and resume content left as placeholders for manual completion. No analysis or modeling content was generated — that starts with a brief.

## 2026-08-29 — Solver constraints error (Claude)

My initial total beds were wrong, it was >64. I realized that I didn't have constraints inputted in the solver. Taught me that knowing the case study and max beds allowed made me go back and resolve the error and not take AI output at face value.

## 2026-09-11 — Stage 3, session 1: pulling MC and shadow-price numbers (Claude)

AI pulled exact MC and shadow-price numbers from my workbook, and I wrote each of the four analysis sections and the Stage 1 hypothesis comparison myself, checking each draft against the workbook before using it.

## 2026-09-11 — Stage 3, session 2: chart-building instructions (Claude)

Got step-by-step Excel instructions (exact Cost-sheet columns and rows) for the two required figures — carrot MC-vs-price and the tomato MC dip — and built both charts myself.

## 2026-09-11 — Stage 3, session 3: memo formatting (Claude)

Wrote the full memo myself. Used AI to help format the memo into the required YAML‑plus‑markdown structure for perfect-competition-memo.md. Claude checked all the numbers against my workbook (all correct, nothing needed fixing).

## 2026-09-12 — Feedback fixes: figures, section 4, memo sensitivity (Claude)

Re-uploaded both PNG files properly this time and renamed them to remove spaces and a "#" character that could have broken rendering. Added sentences in the analysis text that actually point at each chart, which had been missing entirely.

Rewrote section 4's closing paragraph myself using the AVC figures Adam provided (carrots: $1,918.45 vs. $2,094 price; mesclun: $2,430.74 vs. $2,700 price), including the more precise "at the plan's endpoints" scoping he suggested over an unqualified "everywhere."

I recalculated the memo's sensitivity number myself: bed 10's $551.41 margin divided by the $8,800 price is 6.27%, not the 20% I originally guessed, so I rewrote that line with the correct figure.

Added the "Exercised in" section to capabilities/marginal-analysis/README.md linking to the Stage 3 analysis and memo.

## 2026-09-14 — Correction: renaming note, section 4 precision, duplicate cleanup (Claude)

The earlier note about "renaming the PNGs to remove spaces and a # character" was incorrect. The filenames with spaces/# are the ones that stayed and are referenced; the hyphenated versions were deleted instead.

Updated Section 4 for precision: separated the carrot AVC claim (always below price at the plan's endpoint) from the mesclun AVC behavior (dips above price at beds 13–14, then recovers). The original wording lumped both crops together.

Removed two duplicate PNG files so only the correctly referenced charts remain in analysis/figures/.

## Reflection

In Stage 3, AI was used to pull the numbers, but the analysis itself was mine. I made a point of double‑checking the key figures I relied on, including the tomato marginal costs at beds 10 and 11 ($8,248.59 and $9,390.72) and the carrot and mesclun shadow prices ($352.49 and $246.47) in my Cost and Optimization sheets. Verifying those values against my workbook gave me confidence that the numbers I was using were correct.

Working through the guided questions helped the economics click into place. The tomato bed‑10 versus bed‑11 comparison was the moment the stopping rule finally felt intuitive. Seeing the $8,248.59 and $9,390.72 marginal costs lined up against the $8,800 price made the P = MC cutoff concrete instead of theoretical, and it helped me understand how the model decides where to stop.

I also learned that AI can sound correct while being wrong in ways that matter. One draft stated the shutdown rule as "as long as P ≥ MC," which is incorrect—the rule uses average variable cost, and using the wrong statistic would have changed the entire conclusion about carrots and mesclun. Another AI-generated paragraph listed carrot marginal cost at $1,742 and mesclun's price at $1,800, neither of which matched my workbook. I also accepted a "20% price decline" sensitivity number that wasn't derived from anything, when the correct threshold is 6.27% based on bed 10's margin. Catching these mistakes showed me that verification isn't just a step in the process; it's what keeps the analysis tied to the actual model instead of a confident-sounding error.

Going forward, I'll treat every AI‑supplied number as something to verify myself. The back‑and‑forth was helpful for clarifying concepts, but the checking is what grounded the analysis and made me confident in the conclusions I reached.

## 2026-09-24 — Research paper revisions per feedback (Claude)

Used Claude to interpret the 2026-09-22 research paper review and draft
revisions to the brief and spec: figure changed to employment vs. real wage,
vacancy dropped in favor of turnover, brief cut to one three-link mechanism,
CFO decision-maker named, numeric falsification thresholds added, ROI bridge
written into the spec, and Aiken, NSI, and Silvestre et al. citations completed.

Claude corrected an earlier error in its own draft: it had stated that the
employment–wage ratio is a supply elasticity only if demand held still; the
correct condition is that demand shifts along a stable supply curve, so the
threat is supply shifts. The spec caveat uses the corrected version.

Numbers supplied by AI that I need to verify myself: the 490-RN case hospital
(derived from NSI's $295,000 per turnover point ÷ $60,090), NSI's 17.6%
turnover and $60,090 cost, and the Silvestre et al. figures (15.5% vs. 26.8%
turnover, $3,185 + $723 cost per new graduate, mean of 15 hires per hospital).

Corrected the per-point turnover cost to NSI's exact $294,976 (still ≈ 490 RNs).

Data pulled: NSI 2026, BLS OEWS 2015–2019 (from BLS national news releases),
and BLS CPI-U. Against the thresholds set before pulling: link 1 fails (observed
employment–wage ratio ≈ 12.7, because real RN wages rose only ~0.7% while
employment rose ~8.6%); link 2 fails (turnover fell 0.8 points, 18.4% → 17.6%,
over 2023–2025); link 3 passes at the published effect (ROI ≈ 1.26) but fails
at half effect (≈ 0.63). Numbers to verify myself before the paper.

## 2026-09-26 — Responding to the 2026-09-26 review; figures (Claude)

Used Claude to work through the 2026-09-26 review. Claude recomputed the
employment–wage ratio from my data files (employment +8.6%, real median wage
+0.7%, ratio ≈ 12.7), which matches my professor's "around 12." Link 1 fails by
the threshold I set before pulling data. No other windows or measures were
tried.

Decisions I made:
- I first chose to drop link 1, then changed to keeping it and reporting that
  it failed. The brief and spec record the result, and Figure 1 shows it.
- I rewrote the research question as "Under what conditions does a nurse
  residency program generate a positive return…?" so the half-effect result
  shapes the recommendation.
- I used "nurse residency program" throughout, defined once as the Silvestre
  et al. (2017) program.

Claude flagged two problems in my own revision of the brief. First, I had added
a fourth falsification condition (the recommendation surviving a 50% cut in
effect) after seeing the data, and it already fails at 0.63. I removed it so
the list matches the three conditions set in advance. Second, link 1 was back
in the brief without its result stated. I added the result.

Other changes: link 2's result (−0.8 points) is now stated in the brief, with
the analysis resting on the 17.6% level. The economics list is trimmed to the
three concepts that match the three links. The ongoing-cost-only ratio is
reported beside the full-cost ratio. The Aiken et al. (2002) effect size is
recorded in the spec.

Figures: Claude drew Figure 1 (annual employment change vs. real wage change,
with the ratio = 1.0 line) and Figure 2 (ROI ratio vs. share of the published
effect achieved, full and ongoing-only cost, break-even at 1.0). The scripts
are in analysis/figures (fig1.py, fig2.py). fig1.py reads the data files
directly; fig2.py uses the figures from the ROI bridge in the spec.

AI-supplied figures and how they were checked:
- Aiken et al. effect size (7% higher odds of 30-day mortality per additional
  patient per nurse; OR 1.07, 95% CI 1.03–1.12): Claude supplied it from
  memory, then confirmed it against the article's abstract.
- Key numbers (12.7; −0.8 points; $101,853 avoided; $81,012 full cost; $66,024
  ongoing cost; break-even at 79.5% and 64.8%): Claude recomputed them from my
  files, and I checked them myself. They match.
