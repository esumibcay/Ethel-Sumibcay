# Ethel Sumibcay — feedback, sweep of 2026-10-05

My apologies for leaving #8 unanswered for twelve days. Until recently my reviews read the files you pushed but not the comment threads, so your note went unseen; that is fixed, and I read every thread now, open and closed. The "global" wording was mine, and it was too narrow.

This pull request answers #8.

## Research paper review — pre-deadline read

**What I read.** `drafts/2026-10-01-draft.md` in full, including Appendix A · `docs/briefs/research-brief.md` and `capabilities/economic-research/spec.md`, with the changes since my last read · `data/README.md` and the CSVs the draft draws on · `analysis/figures/fig1.py` and `fig2.py` · the commits since my last read.

**What I did not open this pass.** The committed figure images (I checked the scripts that draw them) · `prompt-log.md` · your Case 1 files · `AGENTS.md`, `CLAUDE.md`. If something in those changes an item below, say so and I will look.

---

#8: a local challenge was always a fine subject for this paper, and the nurse-residency paper you chose is a good one. All four items from my last read are closed. The Aiken study now sits as staffing context, "so it is context for the decision rather than part of the ROI." The alternatives are named, with the reason they are not computed. Figure 1's script saves to the file the draft shows, and the data table draws cleanly. Every number in the draft traces to a committed file or the spec, and the Appendix A arithmetic checks through to the 1.26 and 1.54 ratios and the two break-even shares. What is left is the economics at the edges of the ROI.

**Is a new graduate as costly to replace as the average nurse?** The avoided cost uses $60,090 per departure, the average for all staff RNs. The program is about first-year new graduates. Is replacing one of them as costly as replacing an average RN, with the orientation, the overtime and the agency cover that a departure sets off? If not, which way does that move the 1.26, and does the paper say so?

**What happens after year one?** The paper already says what counting one year leaves out: the ROI "counts only first-year savings," and if the program keeps nurses beyond 12 months, "the true return could be higher." That is the right direction. What is left is how much. Does Silvestre et al. (2017) carry evidence on retention in year two? If it does, could it put a number on how much higher the return could be, and would that number change your recommendation?

**One label.** Figure 1's x-axis label, in `analysis/figures/fig1.py` line 23, still says "(2019 dollars)" for an index deflated by CPI. The percent changes are unaffected, but the label should name what the axis shows. On **github.com**: open `analysis/figures/fig1.py`, click the pencil icon, fix line 23, commit, and rerun the script so the image updates. Or, in **Claude Code or Codex** opened in your portfolio repository: "Fix the x-axis label on line 23 of `analysis/figures/fig1.py` so it matches what is plotted, rerun the script, and show me the new figure."

The paper you uploaded to Lamaku matches the draft I read, word for word. You can upload a revised copy to Lamaku before the deadline, and the latest upload is the one I grade. If you do, this is the order I would work in:

**In order:**

1. Answer in the text whether a new graduate costs as much to replace as the average RN, and which way that moves the ratio.
2. Answer in the text whether Silvestre et al. (2017) has year-two retention evidence that could put a number on the return beyond year one.
3. Fix Figure 1's axis label and rerun the script.
