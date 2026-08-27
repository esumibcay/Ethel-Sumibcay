<!-- PR TARGET: https://github.com/esumibcay/Ethel-Sumibcay | Stage 1.1 (2.5 pts) -->
# Stage 1.1 review — engagement brief · **91 / 100** (A-) · 2.28 / 2.5 pts

**Brief:** [`docs/briefs/perfect-competition-brief.md`](https://github.com/esumibcay/Ethel-Sumibcay/blob/main/docs/briefs/perfect-competition-brief.md)

> Re-graded 2026-08-26. Your previous result was 38, held rather than entered because the brief had no hypothesis in it. You wrote one, and it is one of the two or three strongest in the cohort. This score is entered.

| Criterion | Earned | Notes |
|---|---|---|
| Problem restated in your own voice | 28 / 30 | This is the best problem statement I have read in this stage. It is accurate, it is in your voice rather than the case README's, and it gets the hard part right: "planting more beds of the same crop makes all of that crop's beds harder to manage because of diminishing returns." That word all is the whole mechanism. Two people in this cohort have already built workbooks that apply the penalty only to the newest bed, and their models are tens of thousands of dollars off because of it. You have the caps right at 20 / 20 / 30, the price-taker framing right, and the labor constraint identified as the thing that actually binds. The two points off are for what is not there: no numbers. The prices, the hours per bed, and the diminishing-returns rates are the evidence your hypothesis rests on, and quoting them would have made the next criterion easier too. |
| Hypothesis names a specific mix | 25 / 25 | Six tomato beds, 20 carrot beds, 24 mesclun beds. Three real integers, no ranges, no percentages, no "balanced mix." That is exactly what this criterion asks for. |
| Economic mechanism | 20 / 25 | You reason crop by crop and you get the ordering right: tomatoes get expensive fastest so you keep them small, carrots stay cheap so you take the cap, mesclun sits between. That ordering is the 10 percent, 2.5 percent, and 1.25 percent diminishing-returns rates, correctly ranked, and you arrived at it from the economics rather than from a number in a cell. Five points off for the same reason as above: the argument is qualitative where the case hands you the quantities. "Tomatoes get hard very fast" is right; "the 20th tomato bed takes roughly 6.7 times the labor per bed of the first, and at $8,800 a bed that catches up sooner than the carrot price does at $2,094" is the same claim with the evidence attached. One thing you skipped that costs a little: you do not say which crops you think stop because marginal cost reaches the price and which stop because they hit a bed cap. Your own numbers imply carrots stop at the cap and tomatoes stop on economics — saying so out loud is a sharper claim than the mix alone. |
| Falsifiability and process | 18 / 20 | Three named outcomes, each tied to a specific assumption that it would break. "If the model plants fewer than 20 carrot beds, then labor or diminishing returns must have stopped carrots earlier than I expected." That is a real falsification condition and it is rarer than it should be — eight of the eleven briefs I graded in the first pass either had no such section or had the circular version of it, "I would know I was wrong if the model showed a different mix," which is true of every hypothesis ever written. Yours are not that. The brief is at the correct path now, the commit message says what changed, and it was committed before any modeling. Two points off because no AI critique session for this brief is logged in prompt-log.md — the stage asks for it, and the last entry there is the 2026-08-18 scaffolding session. |
| **Final** | **91 / 100** | earned on merit |

### What changed

Last time the problem statement was already right and the hypothesis was missing. You kept the part that was working and added the part that was not, which is the correct response to feedback and less common than you would think — the usual instinct is to rewrite everything.

You also fixed the duplicated folder path. Your brief was at docs/briefs/docs/briefs/perfect-competition-brief.md and is now where it belongs. That mattered more than it looks: a file at the wrong path may not be found at all, and in a real repository the reviewer does not go looking.

### The one thing worth sitting with

Your tomato call is 6 beds. I am not going to tell you what the model returns, because Stage 3 is where that comparison happens and it is worth more if you have not been told the answer. But here is the question your own brief raises and does not answer: you say tomatoes get expensive fast, and that is right. What you have not accounted for is that the farmer's own 720 field hours are the expensive labor at $34.72 an hour, and once those run out, every additional hour is a temporary worker at $17.36. Cheaper labor arriving partway up the schedule does something interesting to marginal cost, and it happens right around where you have set your tomato number.

If your prediction turns out low, that is very likely why. Work out what you think happens to the marginal-cost curve at the moment the labor source switches, and write it down now, before you build. Whether you turn out to be right or wrong, you will have a much better Stage 3 memo than someone reconstructing the reasoning afterwards.

### Looking ahead

Stage 1.2 asks for capabilities/marginal-analysis/spec.md before the workbook exists, then an audit of what gets built from it. Your folder and a stub are already there. Put the published check figures into the spec as acceptance criteria before you build anything — the mix, the profit, the hand-check at one bed of each crop. Both completed workbooks in this cohort so far have costing errors that a check-figure table would have caught in a minute, and neither spec had one.

The labor sentence you wrote in this brief — the one about all of a crop's beds getting harder, not just the newest — belongs in that spec, in the exact words you used here. It is the single formula that decides whether the model is right.

---

### How to work this review

Treat this PR the way an analyst treats feedback from a senior reviewer — a review is a proposal to engage with, not a checklist to rubber-stamp.

1. **Read it yourself first.** Form your own view before you change anything. Disagreeing *with a documented reason* is a legitimate, senior response.
2. **Stress-test it with an LLM.** Paste this review and your brief into your assistant and ask it to (a) explain anything you are unsure of, and (b) argue the *other side* — where might the reviewer be wrong, and what would you give up by making each change.
3. **Then write the changes yourself.** For a brief, this matters more than usual: a hypothesis you did not generate cannot be honestly compared against your model in Stage 3, and that comparison is the entire point of writing the brief first.
4. **Close the loop.** Reply in this thread with what you changed and what you pushed back on, then commit and push.

*One standing rule for this stage: do not revise your hypothesis to match what your model later tells you. If the model contradicts the brief, that is a finding, not an error — Stage 3 asks you to explain the gap, and a brief quietly edited to be right afterwards has nothing left to explain.*

— Adam
