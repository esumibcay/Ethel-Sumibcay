<!-- PR TARGET: https://github.com/esumibcay/Ethel-Sumibcay | Stage 1.1 (2.5 pts) -->
# Stage 1.1 review — engagement brief

**Scored 38 out of 100, and I am holding it rather than entering it. Held for revision; the deadline has not passed.**

**Brief:** [`docs/briefs/docs/briefs/perfect-competition-brief.md`](https://github.com/esumibcay/Ethel-Sumibcay/blob/main/docs/briefs/docs/briefs/perfect-competition-brief.md)

> You wrote a clear, correct explanation of the case — but the brief contains no hypothesis. There is no predicted mix of beds anywhere in it, and the hypothesis is the deliverable. On the rubric that comes to 38, which I am not entering, because this is a brief that is missing its last paragraph rather than a brief that was done poorly.

### What to do

The reason this stage exists, and the reason it is graded before the model: a prediction written before the model runs is falsifiable. The same sentence written afterwards is a summary of the output, and it teaches you nothing, because you can no longer tell "I understood the economics" from "I read the answer cell." Stage 3 asks you to compare what you predicted against what the model found — and that comparison cannot be reconstructed later. A wrong hypothesis, precisely reasoned, is worth as much as a correct one and considerably more than a lucky one.

What you did write is right, and it is worth keeping. "Because the farmers' market sets all the prices, the farm has no control over what it earns per bed — it's a price taker. That means the only real decision is how much to plant" is the case understood correctly, and "keep planting beds as long as the next bed earns more than it costs; when the marginal cost of the next bed reaches the market price, you stop" is the P = MC rule stated cleanly. You have the economics. What is missing is the step where you point it at a number.

One path problem to fix at the same time: the file is at docs/briefs/docs/briefs/perfect-competition-brief.md — the folder name got typed twice. The graded path is docs/briefs/perfect-competition-brief.md. Copy the contents, create the file at the correct path, and delete the nested docs/briefs/docs/ folder.

- State the problem in your own words. Half a page. What the farm is deciding (how many beds of tomatoes, carrots, and mesclun), what is fixed (the 36-week season, $20,000 of fixed costs, the prices, the per-crop caps of 20/20/30, the farmer's 720 field hours, up to four temp workers at 1,440 hours each), what you choose, and what limits the choice. Restating is not copying — if you cannot say it differently from the case README, you do not have it yet.

- Name a specific mix. Real bed counts: "I expect X tomato beds, Y carrot beds, Z mesclun beds." Not a range, not percentages, not "a balanced mix."

- Say why, using the numbers the case gives you. The mechanism that decides this case is diminishing returns: labor hours for q beds of a crop are q x hours-per-week-per-bed x 36 x (1 + rate)^q, where the rate is 10% a bed for tomatoes, 2.5% for carrots, and 1.25% for mesclun. That compounding is why marginal cost rises, and why the answer is not just "plant the crop with the highest price." Tomatoes earn $8,800 a bed against carrots' $2,094 — but the 20th tomato bed costs roughly 6.7 times the labor per bed of the first. Say which crops you think stop because marginal cost catches the price, and which stop because they hit a bed cap.

- Say how you would know you were wrong. Two or three named outcomes. "Carrots finishing below their 20-bed cap would mean something other than diminishing returns bound first." A prediction that survives every possible result is not a prediction.

- Commit it to docs/briefs/perfect-competition-brief.md with a message that says what changed — for example, "Add perfect-competition brief with mix hypothesis."

### Looking ahead

Stage 2 asks for a spec in capabilities/marginal-analysis/ before the workbook exists, then an audit of what the AI builds from it. The reasoning you put in this brief is the reasoning that spec runs on, so this is not a box to tick on the way past — it is the thinking Stage 2 is built on top of.

---

### How to work this review

Treat this PR the way an analyst treats feedback from a senior reviewer — a review is a proposal to engage with, not a checklist to rubber-stamp.

1. **Read it yourself first.** Form your own view before you change anything. Disagreeing *with a documented reason* is a legitimate, senior response.
2. **Stress-test it with an LLM.** Paste this review and your brief into your assistant and ask it to (a) explain anything you are unsure of, and (b) argue the *other side* — where might the reviewer be wrong, and what would you give up by making each change.
3. **Then write the changes yourself.** For a brief, this matters more than usual: a hypothesis you did not generate cannot be honestly compared against your model in Stage 3, and that comparison is the entire point of writing the brief first.
4. **Close the loop.** Reply in this thread with what you changed and what you pushed back on, then commit and push.

*One standing rule for this stage: do not revise your hypothesis to match what your model later tells you. If the model contradicts the brief, that is a finding, not an error — Stage 3 asks you to explain the gap, and a brief quietly edited to be right afterwards has nothing left to explain.*

— Adam
