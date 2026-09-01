<!-- PR TARGET: https://github.com/esumibcay/Ethel-Sumibcay | Stage 1.2 (8 pts) -->
# Stage 1.2 review — spec, build, audit

**Provisional score 76 out of 100 — that would be 11.40 of the 15 points for this stage — held, not entered. The stage is not due until 6 September and there are three specific defects your own workbook is already reporting.**

**Spec:** [`capabilities/marginal-analysis/spec.md`](https://github.com/esumibcay/Ethel-Sumibcay/blob/main/capabilities/marginal-analysis/spec.md)

> Graded 2026-08-31, first pass. You have a real specification and a real, working model that finds the correct optimal mix and the correct standalone crossings. It also fails two of its own checks, and the failures are honest ones you wrote the checks to catch. That is the system working. Fix them and this moves a long way in six days.

| Criterion | Earned | Notes |
|---|---|---|
| Spec completeness — inputs, structure, calculation flow | 30 / 37.5 | Complete enough to build from, which is the bar, and several parts are better than that. All 23 inputs carry a value, a unit, and a source. The labor function is correct with the exponent on q. The costing order is explicit and right — the farmer's 720 hours are applied against combined hours across all three crops first, regardless of which crop they belong to — and the blended rate is defined at the farm level rather than per crop, which is the convention most people get wrong. And one line does real work: "computed the same way at every bed count — the model should not assume marginal cost only increases." That is a rule against a shortcut a builder would otherwise take, and your workbook found the non-monotonicity because of it. |
| Spec validation rules | 19 / 25 | The reproduction section is the strongest part of the document and nobody else wrote one. Nine numbered steps that take a reader from opening the file to confirming the constraints, including both Solver starting points and the instruction to compare them. That is a procedure someone else could follow, which is what reproducibility means. Six points off for one omission that is costing you a passing check: there are no tolerances anywhere. Step 7 says confirm profit equals $42,762, full stop, so a $13 difference reads as a failure identical in kind to a $13,000 one. |
| Workbook satisfies the contract | 17 / 25 | There is a genuine model here: five sheets, 25 defined names, over 1,300 formulas on the Cost sheet, zero error cells, and it gets the answer — optimal mix 10 / 20 / 30 at 60 beds, standalone crossings at 10, 10, and 6, and "MC monotonically rising? No" recorded for all three crops. Finding the non-monotonicity is worth saying out loud; most builds paper over it. Eight points off for three defects, all listed below and all fixable. |
| Audit note | 10 / 12.5 | Four findings and one of them is the best single audit entry in the cohort — see below. Two and a half points off because the audit predates the two failures your Checks sheet is now reporting, and because the Farm Profit Lab cross-check on the stage checklist has not been run. |
| **Final** | **76 / 100** | held |

### The zero-constraint finding, which is the best thing in this submission

"The initial build had zero constraints entered in Solver. Running the optimizer with no constraints produced 74 total beds and a profit of $45,039 — both physically impossible under the case's 64-bed limit, and higher than the correct answer."

Read what you actually did there. A tool returned a number that was better than the target, and instead of taking it you asked whether it could be true, checked it against a physical limit, found it could not, and traced it to a setup error. Then you wrote it down as a structural defect in the AI-generated build rather than quietly fixing it.

A more profitable answer is the hardest kind of wrong answer to catch, because nothing about it feels like an error. That entry is the single most transferable thing in this stage's submissions and it is worth the audit section on its own.

### The three defects, in the order i would fix them

1. Your profit is $13.16 high, and it is entirely rounding in the wage rates. Your Checks sheet reports $42,775.16 against $42,762 and marks it FAIL. The cause is that FARMER_WAGE and TEMP_WAGE are typed as 34.72 and 17.36, and HRS_PER_BED_CARROT as 0.833. The true figures are $50,000 / 1,440 = $34.7222..., $25,000 / 1,440 = $17.3611..., and five sixths of an hour. Derive them from the underlying values instead of typing the rounded display figures and the $13 disappears. Your own total labor hours show it: you have 5,276.82 where the correct figure is 5,277.216, and the 0.393-hour gap is exactly the carrot rounding. This is worth understanding rather than just fixing — a discrepancy small enough to look like a modeling subtlety and large enough to fail a check is the most expensive kind to chase.

2. Three calculated cells are pasted values. Your own integrity check finds them and reports FAIL against an expected zero. Find them and replace them with formulas. A pasted number is a defect even when it is the right number, because it stops updating the moment an input changes — which is precisely what Solver does on every run.

3. Your Optimization sheet and your Checks sheet disagree with each other. Optimization shows "Carrots 20 beds, cap 0, VIOLATED" and "Mesclun 30 beds, cap 0, VIOLATED", while the Checks sheet shows the same two constraints against caps of 20 and 30 and marks both SATISFIED. The cap column on Optimization is reading zeros. Both cannot be right, and a reader who opens the Optimization sheet first sees a model that is violating its own constraints.

### The filename problem, which is small and will cost you if it is not fixed

The graded path is capabilities/marginal-analysis/model.xlsx. That file exists in your repository and contains a single sheet named Model with three cells in it. Your actual work is in capabilities/marginal-analysis/1.2 - Perfect Competition Model.xlsx.

So step 1 of your own reproduction procedure — "Open model.xlsx in Excel desktop" — opens the wrong file, and a reviewer following your instructions finds an empty workbook.

Rename the real workbook to model.xlsx and delete the stub. Also worth avoiding for the rest of the course: spaces and periods in filenames make paths awkward to reference from a spec, a script, or a URL.

### Two smaller things

- capabilities/marginal-analysis/README.md still carries its PLACEHOLDER comment and says "Empty until the first engagement is written." You have a brief, a spec, and a workbook. That README is the file a reader opens to find out what is in the folder.

- Add tolerances to your validation rules — profit within $5, crossings within a bed, hours within 0.01. A check with no tolerance either passes by luck or fails on rounding, and neither outcome tells you anything.

### Why this is held rather than entered

The stage is not due until 6 September and your workbook is currently reporting two of its own checks as failing. Entering 76 today would record the state of a model mid-repair.

The number is here so you know where you stand. The three defects above are hours of work, not days, and the audit entry you have already written is the hard part.

### A note on the point value, new as of today

This stage is now worth **15 points** rather than the 8 in the stage brief, and **Stage 1.3** — the analysis, the memo, and the prompt log — is now worth **15** as well. Cases 2 and 3 have been dropped for this cohort, so Case 1 *is* the case.

In practice: this stage and the next one are together worth **30 of the 35 points** on the case. Stage 0 and Stage 1.1 are 2.5 each. The weight has moved onto the build and the analysis, which is where the work actually is.

Nothing about the grading changes — the score is still out of 100 and converted at the end. The stage brief and the case page still show the old numbers; they have not been updated yet.

---

### How to work this review

Treat this PR the way an analyst treats feedback from a senior reviewer — a review is a proposal to engage with, not a checklist to rubber-stamp.

1. **Read it yourself first.** Form your own view before you change anything. Disagreeing *with a documented reason* is a legitimate, senior response.
2. **Stress-test it with an LLM.** Paste this review and your spec into your assistant and ask it to (a) explain anything you are unsure of, and (b) argue the *other side* — where might the reviewer be wrong, and what would you give up by making each change.
3. **Then correct the spec, not the workbook.** This is the rule that makes the stage work: when a check fails, you fix the specification and regenerate, so the document keeps describing what was actually built.
4. **Close the loop.** Reply in this thread with what you changed and what you pushed back on, then commit and push.

*Nothing here is final. Stage 1.2 is not due until 6 September, and the stage is re-graded from scratch at the deadline.*

— Adam
