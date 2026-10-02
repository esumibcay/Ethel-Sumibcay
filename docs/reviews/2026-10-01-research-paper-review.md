<!-- PR TARGET: https://github.com/esumibcay/Ethel-Sumibcay | Individual Research Paper -->
# Research paper review — pre-deadline read

**What I read.** `drafts/2026-09-27-draft.md` in full, and its differences from the 09-26 draft · `docs/briefs/research-brief.md` and `capabilities/economic-research/spec.md` in full, with the changes since my last read · `data/README.md` and all four CSVs · `analysis/figures/fig1.py` and `fig2.py` · the committed Figure 1 image · the new prompt-log entries and your reflection · the portfolio table in the root README.

**What I did not open this pass.** The committed Figure 2 image (I checked the script that draws it instead) · `AGENTS.md`, `CLAUDE.md` · your Case 1 files · my own last review, which you added to `docs/reviews/`. If something in those changes an item below, say so and I will look.

---

**A note on privacy.** Your repository is public, and some of you have built your paper around your own business, which is great. Just be careful with personal information and anything your company would treat as confidential: customer names or records, pricing, contracts, or financials that aren't already public. If that's a concern, add those files or that content to your .gitignore and send them to me by email instead. The paper doesn't need GitHub to be graded.

Your note on #8 that you were leaving the first topic was the right call, and this read is on the nurse-residency paper you chose instead. Thank you for sending me the NSI report by email. That was the right call, and I read the numbers your draft takes from it as sourced to the NSI report you sent, with your two NSI files in `data/` as the record.

This is a paper now, and a good one. All three items from my last read are closed. You also went one step past what I asked: the break-even share ("at least about 80% of the published effect, or about 65% if it pays only ongoing costs") is the most useful sentence in the paper for a CFO, because it turns "most of the effect" into a number someone can track. Your reflection says it plainly: "At first, I wanted to find a way to make the results fit my expectations." Your prompt log also records the fourth falsification condition you added after seeing the data and then removed. That is a catch you made in your own files, and it is the discipline the whole paper runs on.

Every load-bearing number in the draft traces to a committed file or to the spec's cited values. What remains is small.

**The Aiken sentence claims more than Aiken measured.** The draft says "Turnover also affects patient outcomes," then cites a study of patients per nurse. Your own spec calls it "the staffing-to-quality link." Does a study of patients per nurse show what turnover does? If not, what links a nurse leaving to a patient's outcome, and can you show it? Bridge it, or say staffing rather than turnover.

**The brief and spec promise alternatives the draft does not discuss.** Both say wage increases, bonuses, and working-condition changes "are discussed as alternatives but not computed." The draft mentions "a broader retention strategy" but never names them. You have two honest options: add two or three sentences to the recommendation naming them and saying why none is computed (the spec already has the reason), or take the line out of the brief and spec. Either is fine; amending the plan is a sanctioned move, and the history records it.

**Figure 1's script saves a different file from the one the draft shows.** `fig1.py` writes `figure1_employment_wage.png`; the draft embeds `figure1_employment_wage_1.png`. Today they are the same chart, but a rerun after any data fix would not reach the paper. Make the two names match.

**One line breaks the data table.** In `data/README.md`, "Report is available from NSI's website" sits between the table's header and its first row, so GitHub stops drawing the table there. Move it below the table.

**In order:**

1. Decide whether Aiken supports a claim about turnover; bridge it if so, or call it staffing.
2. Name the alternatives in the recommendation, or drop the promise from the brief and spec.
3. Make `fig1.py` save to the file the draft embeds.
4. Move the NSI line in `data/README.md` below the table.
