<!-- PR TARGET: https://github.com/esumibcay/Ethel-Sumibcay | Individual Research Paper -->
# Individual Research Paper — pre-deadline read

**What I read.** `docs/briefs/research-brief.md` and `capabilities/economic-research/spec.md` in
full · the diff between them and the versions I read last time · `data/README.md` · `prompt-log.md` ·
the commits since my last read.

**What I did not open this pass.** The review file you merged, which is my own last read · your
Case 1 files · `AGENTS.md`, `RESUME.md`. If something in those changes an item below, say so and I
will look.

---

You changed the topic, and you changed it the right way: brief and spec both moved to nurse turnover
and retention in the same set of commits, so the history records the amendment and there is nothing
for the paper to drift from. The spec is no longer the template — five named sources, a mechanism
written as a chain from inelastic supply through turnover cost to a retention program that pays for
itself, a figure with its reading rule, success criteria that map to your falsification list. That is
the file I asked for. The items below are in dependency order, and the first is a real economics
problem worth getting right.

**Your elasticity and your figure measure different things.** The spec defines elasticity as the
percentage change in RN employment divided by the percentage change in the real median wage. The
figure plots RN wage growth against the RN vacancy or turnover rate. Employment is a count of nurses
working; vacancy is a stock of unfilled posts; turnover is a flow of leavers — and the definition uses
the one the chart leaves out. Choose. If the claim is inelastic supply, the chart is the definition,
employment change against real wage change. If what you want to show is that vacancies persist while
wages rise, that is excess demand — a different and equally good claim — and the spec should call it
that. Either way, say this in the spec: a ratio of observed employment change to observed wage change
is only a supply elasticity if demand held still, and your own brief lists reasons it did not — aging
populations, rising acuity. Call the ratio what it is, or argue why demand was stable over your
window. And settle "vacancy or turnover"; they answer different questions.

**The brief is still wider than the spec.** The spec's chained mechanism is the paper; the brief still
carries four analysis strands and five falsification bullets, with global migration as its own strand
and its own bullet where the spec — correctly — has made it "one sentence, one stat." Bring the brief
down to the spec.

**Who is asking which retention strategy pays best?** That is a hospital's question, and no hospital
is named. A chief nursing officer or a CFO, at what kind of hospital? Name one. And pick one framing
for the brief: it currently says the challenge is global, while the spec's data are the NSI report
and BLS OEWS, both US. A US hospital case on its own is a perfectly good paper — you do not need the
global frame to justify it. Keep it as one sentence of context if you like it, or drop it; either
way, the brief and the data should be telling the same story.

**Thresholds are still words.** The spec maps each falsification condition to a data result, but the
results read "flat or declining" and "strong negative relationship." Before you pull anything: turnover
rising by how many points over how many years counts as rising; a ratio below what counts as inelastic;
a program cost above what share of avoided turnover cost counts as not paying.

**The recommendation rests on one borrowed case study.** The ROI is to be computed or quoted from a
single published program evaluation. Say in the spec how you move that program's cost and effect to
your case hospital — NSI's cost per turnover times the departures the program avoided is the natural
bridge — so the ratio is yours and not just cited. And Aiken et al. needs a year and a title; the NSI
edition is a to-do you wrote yourself.

**Nothing is pulled.** `data/README.md` is unchanged. The NSI report and OEWS are public; your own
spec says to record source, publication date and transformations for every series. Start with those
two.

**In order:**

1. Make the figure match the elasticity definition, or rename the claim; settle vacancy versus turnover.
2. Cut the brief down to the spec's single mechanism.
3. Name the hospital decision-maker, and pick one framing — US case or global context.
4. Put a number on each falsification threshold.
5. Write the ROI bridge into the spec, and complete the Aiken and NSI citations.
6. Pull NSI and OEWS into `data/`, recorded per your own rule.
