<!-- PR TARGET: https://github.com/esumibcay/Ethel-Sumibcay | Stage 1.2 -->
# Stage 1.2 review — spec, build, audit

**Spec:** [`capabilities/marginal-analysis/spec.md`](https://github.com/esumibcay/Ethel-Sumibcay/blob/main/capabilities/marginal-analysis/spec.md)

> Re-graded 2026-09-02 against your 1 September commits. You have been reviewed on this before. All three are fixed, your Checks sheet now reads ALL PASS, and you found the wage-rounding defect yourself and traced it to the cent before I told you about it.

| Criterion | Where it stands |
|---|---|
| Spec completeness — inputs, structure, calculation flow | Stronger this pass. The derived-input rule is the gain, and you wrote it as a general rule rather than three one-off fixes: any input whose source is itself a ratio — a salary over annual hours, a fraction of an hour — is stored as that ratio and never as a rounded display figure. That is the version that protects the next input as well as these three. You added a second rule of the same shape for the bed-cap column, requiring it to reference the named inputs so it cannot drift out of sync. What is still open: what is still missing: there is no statement of how the standalone marginal-cost schedules hold the other two crops, and the structure section still does not say what the Checks sheet must contain, which is why two of your own listed outputs never became checks. |
| Spec validation rules | Stronger this pass, and the The deduction was exactly this: no tolerances anywhere. There is now a Validation tolerances section, and the sentence that opens it is the right reason for having one — "a check with no tolerance either passes by luck or fails on rounding, and neither outcome tells you anything." The three bands are well chosen: $5 on profit, exact on the integer decisions because a deviation there is a real disagreement rather than rounding, 0.01 hours on the hand check. What is still open: the second labor anchor, which is still not there — your q = 1 check passes even on a model that applies the diminishing-returns factor once instead of compounding it by q, and a q = 10 check (2,334.368214 hours) is the one that catches that. |
| Workbook satisfies the contract | Stronger this pass. All three defects are gone. FARMER_WAGE is 50000/1440, TEMP_WAGE is 25000/1440, HRS_PER_BED_CARROT is 5/6, and profit now comes out at $42,761.66 against $42,775.16 before. The bed-cap cells reference their named inputs. And there is only one workbook at the graded path now, so your own reproduction steps open the file they describe. Everything reconciles to my figures: 5,277.2161 labor hours, 3.1647 temp workers, blended rate $19.7298. What is still open: the standalone P = MC crossings are computed on the Cost sheet but never checked on the Checks sheet — they are in your spec's Outputs list, so they should have a required value, an actual, and a status like everything else — and the Farm Profit Lab cross-check is still not run. |
| Audit note | Stronger this pass. Six findings now, and the two new ones are both real, both traced with exact figures, and both caught by checks you had written earlier — see below. Half a point off for the Farm Profit Lab cross-check, which is on the stage checklist and is the only check you have that is genuinely independent of your own workbook. |

> YOU FOUND THE $13.16 YOURSELF, AND THAT IS THE WHOLE POINT OF THIS STAGE

> "FARMER_WAGE and TEMP_WAGE were entered as typed, rounded decimals ($34.72 and $17.36) instead of the exact ratios. Same issue with HRS_PER_BED_CARROT, entered as 0.833 instead of 5/6. This produced a Checks-sheet profit of $42,775.16 against the published $42,762 — a FAIL."

> I had traced that difference to the same three cells and was going to tell you about it. You got there first, and you got there the way you are supposed to: a check you wrote failed, you did not shrug at a $13 discrepancy, and you followed it to its cause rather than widening the tolerance until it passed.

> The number is small and the failure mode is not. Three inputs rounded at the third decimal moved the answer by thirteen dollars on a $42,000 result. On a model with more inputs, or one where the rounding compounds instead of cancelling, the same defect moves the answer by an amount that matters — and it never announces itself, because a rounded input looks exactly like a correct one.

> Two other people in this cohort wrote spec rules against this defect before building. You are the only one who found it live in your own workbook and fixed it at the source.

### The second finding is the more interesting one

"Optimization!C5:C7 (the bed-cap column) were typed constants instead of formulas — and two of them were simply wrong (0 instead of 20 and 30). This made the Optimization sheet show Carrots and Mesclun as VIOLATED even though the Checks sheet, which references the named ranges directly, correctly showed them SATISFIED."

Two sheets disagreed about whether the model was feasible. That is the situation where most people pick the sheet they trust and move on. You worked out which one was right and why, and the answer — the sheet that referenced named ranges was right, the one with typed numbers was wrong — is the whole argument for named ranges in one sentence.

And you noted that your own integrity check, the one that counts calculated cells that are not formulas, had already flagged those three cells. A check you built for a general reason caught a specific bug you were not looking for. That is the second time in this submission that happened.

### The gap left, in the order I would spend them

- Run the Farm Profit Lab cross-check. It is the only check you have that does not depend on your own workbook being right. Compare marginal costs rather than totals — the lab includes the $20,000 fixed cost in its totals and your model excludes it, so its totals run $20,000 high at every bed count and the offset cancels in the subtraction. Tomato bed 11 is the one to use: the lab moves from $61,827 to $71,218, a marginal cost of about $9,391.

- Add the q = 10 labor anchor to the spec and to Checks. Required value 2,334.368214 hours. It takes two minutes and it is the check that catches the single most likely structural defect in this model.

- Promote the three standalone crossings to Checks rows. You already compute them, and your spec lists them as outputs. Required values 10, 10, and 6, tolerance one bed.

### Where this sits

You are one of four people in the cohort with a finished, audited workbook, and yours is the one that has been through the most repair. The zero-constraint finding, the wage rounding, the pasted cap cells — three structural defects found and fixed through the spec rather than patched in the sheet.

For Stage 1.3, your audit trail is the material. A model that was wrong three times and is right now, with each failure written down and traced, is a better story than a model that worked immediately, and it is a more honest one.

---

### How to work this review

Treat this PR the way an analyst treats feedback from a senior reviewer — a review is a proposal to engage with, not a checklist to rubber-stamp.

1. **Read it yourself first.** Form your own view before you change anything. Disagreeing *with a documented reason* is a legitimate, senior response.
2. **Stress-test it with an LLM.** Paste this review and your spec into your assistant and ask it to (a) explain anything you are unsure of, and (b) argue the *other side*.
3. **Then correct the spec, not the workbook.** When a check fails, you fix the specification and regenerate, so the document keeps describing what was actually built.
4. **Close the loop.** Reply in this thread with what you changed and what you pushed back on, then commit and push.

*Your score and the per-criterion breakdown are in your Lamaku comment, not here — this repository is public.*

— Adam
