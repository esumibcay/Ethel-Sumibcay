# Prompt Log

A running record of significant AI sessions — not every prompt, but the ones that shaped a decision, a model, or a piece of writing in this repo.

## 2026-08-18 — Repo scaffolding

Used Claude to generate the initial repository structure following the [portfolio repo guide](https://adamwstauffer.github.io/ai-lms/portfolio-repo.html): root files, `.claude/skills/`, `capabilities/marginal-analysis/`, `docs/briefs/`, `docs/decisions/`, `data/`, `analysis/figures/`. All biographical and resume content left as placeholders for manual completion. No analysis or modeling content was generated — that starts with a brief.
## 2026-08-29 - Claude for excel

My initial total beds were wrong, it was >64. I realized that I didn't have constraints inputted in the solver. Taught me that knowing the case study and max beds allowed made me go back and resolve the error and not take AI output at face value. 


## 2026-09-11 — Stage 3: analysis, memo, and Stage 1.3 fixes
AI pulled exact MC and shadow-price numbers from my workbook, and I wrote each of the four analysis sections and the Stage 1 hypothesis comparison myself, checking each draft against the workbook before using it.

Got step-by-step Excel instructions (exact Cost-sheet columns and rows) for the two required figures — carrot MC-vs-price and the tomato MC dip — and built both charts myself.

Wrote the full memo myself. Used AI to help format the memo into the required YAML‑plus‑markdown structure for perfect-competition-memo.md. Claude checked all the numbers against my workbook (all correct, nothing needed fixing).


## 2026-09-12 — Updating from feedback 
Re-uploaded both PNG files properly this time and renamed them to remove spaces and a "#" character that could have broken rendering. Added sentences in the analysis text that actually point at each chart, which had been missing entirely.

Rewrote section 4's closing paragraph myself using the AVC figures Adam provided (carrots: $1,918.45 vs. $2,094 price; mesclun: $2,430.74 vs. $2,700 price), including the more precise "at the plan's endpoints" scoping he suggested over an unqualified "everywhere."

I recalculated the memo’s sensitivity number myself: bed 10’s $551.41 margin divided by the $8,800 price is 6.27%, not the 20% I originally guessed, so I rewrote that line with the correct figure.

Added the "Exercised in" section to capabilities/marginal-analysis/README.md linking to the Stage 3 analysis and memo.

## 2026-09-14

The earlier note about "renaming the PNGs to remove spaces and a # character" was incorrect. The filenames with spaces/# are the ones that stayed and are referenced; the hyphenated versions were deleted instead.

Updated Section 4 for precision: separated the carrot AVC claim (always below price at the plan's endpoint) from the mesclun AVC behavior (dips above price at beds 13–14, then recovers). The original wording lumped both crops together.

Removed two duplicate PNG files so only the correctly referenced charts remain in analysis/figures/.

## Reflection

In Stage 3, I used AI to pull the numbers, but the analysis itself was mine. I made a point of double‑checking the key figures I relied on, including the tomato marginal costs at beds 10 and 11 ($8,249 and $9,391) and the carrot and mesclun shadow prices ($352.49 and $246.47) in my Cost and Optimization sheets. Verifying those values against my workbook gave me confidence that the numbers I was using were correct.

Working through the guided questions also helped the economics click into place. The tomato bed‑10 versus bed‑11 comparison was the moment the stopping rule finally felt intuitive. Seeing the $8,249 and $9,391 marginal costs lined up against the $8,800 price made the P = MC cutoff concrete instead of theoretical, and it helped me understand how the model decides where to stop.

I also learned that AI can sound correct while being wrong in ways that matter. One draft stated the shutdown rule as "as long as P ≥ MC," which is incorrect—the rule uses average variable cost, and using the wrong statistic would have changed the entire conclusion about carrots and mesclun. Another AI-generated paragraph listed carrot marginal cost at $1,742 and mesclun's price at $1,800, neither of which matched my workbook. I also accepted a "20% price decline" sensitivity number that wasn't derived from anything, when the correct threshold is 6.27% based on bed 10's margin. Catching these mistakes showed me that verification isn't just a step in the process; it's what keeps the analysis tied to the actual model instead of a confident-sounding error.

Going forward, I'll treat every AI‑supplied number as something I need to verify myself. The back‑and‑forth was helpful for clarifying concepts, but the checking is what grounded the analysis and made me confident in the conclusions I reached.
