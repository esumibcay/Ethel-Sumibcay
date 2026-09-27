<!-- PR TARGET: https://github.com/esumibcay/Ethel-Sumibcay | Individual Research Paper -->
# Individual Research Paper — pre-deadline read

**What I read.** `docs/briefs/research-brief.md` and `capabilities/economic-research/spec.md` in full · `data/README.md` · all four CSVs in `data/` · the commits since my last read.

**What I did not open this pass.** `nsi_2026_retention_report.pdf` · `prompt-log.md` · your Case 1 files. If something in those changes an item below, say so and I will look.

---

**A note on privacy.** Your repository is public, and some of you have built your paper around your own business, which is great. Just be careful with personal information and anything your company would treat as confidential: customer names or records, pricing, contracts, or financials that aren't already public. If that's a concern, add those files or that content to your .gitignore and send them to me by email instead. The paper doesn't need GitHub to be graded.

Every item from my last read is closed, and closed well. Figure 1 now plots what link 1 defines. The ratio is honestly named an "observed employment–wage ratio," with a clear note on why it is only an elasticity if supply held still. Vacancy is gone, and the brief carries one chain. A CFO at a 490-RN community hospital owns the decision, and you derived that hospital size from NSI's own numbers, which is a neat piece of work. Each falsification condition has a number. The ROI bridge from Silvestre et al. to your hospital is written out step by step, and the data are in, with sources and transformations recorded. This is a finished design, and because it is finished, the numbers can now answer it. They answer in a way you should see before you draft.

**Your own data fail link 1, and that is a result, not a problem.** I ran your files. From May 2015 to May 2019, RN employment rose by roughly nine percent while the real median wage (your OEWS wage deflated by your CPI-U) rose by less than one percent. The ratio is around 12, not below 1.0. By the threshold you set before pulling anything, link 1 fails. Please check my arithmetic against your own. If it holds, you have two honest ways to write it. One: report that this measure does not show inelastic supply, and say why a ratio this large probably reflects both curves moving at once (the caveat you already wrote). Two: let link 1 go and rest the paper on links 2 and 3, which never needed it, since the ROI depends on the level of turnover and the cost per departure. Either is a stronger paper than one where the hypothesis quietly survives. The one move to avoid is trying other windows or measures until the ratio drops below 1. You set the test in advance so the data would decide, and here they have.

**Link 2 fails by your threshold too.** Your NSI file gives staff RN turnover rates of 18.4 (2023), 16.4 (2024) and 17.6 (2025): a fall of 0.8, where your threshold asks for a rise of at least 1.0. Your spec already says what to do ("the ROI in link 3 depends on the level of turnover … not on the trend"), so this is a sentence in the paper, not a redesign.

**The half-effect check changes the recommendation.** With your bridge, 15 new graduates × a 0.113 turnover reduction × $60,090 is about $102,000 avoided against about $81,000 of program cost in 2025 dollars, a ratio near 1.26. Cut the effect in half and it falls to about 0.63, below your link-3 threshold. So the robustness check you designed does real work: the recommendation holds only if the hospital gets most of the published effect. Say that directly to the CFO, and give the ongoing-cost-only figure beside it (about 1.54, or 0.77 at half effect), since that is what a hospital adopting an existing program would pay.

**In order:**

1. Recompute the employment–wage ratio from your files; if it is above 1.0, report link 1 as failed and choose how the paper handles it.
2. Report link 2's trend as it is, and lean on the turnover level.
3. Write the recommendation around the half-effect result: fund the program only if the hospital can expect most of the published effect.
