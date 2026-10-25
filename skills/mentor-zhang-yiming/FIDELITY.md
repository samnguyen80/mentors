# Fidelity Scorecard

**Total: 93/100 · Grade A** | Test date: 2026-07-01 | Answering/scoring: two independent agents (Claude Opus 4.8); methodology in [references/fidelity-scorecard.md](../mentors-distill/references/fidelity-scorecard.md)

| Dimension | Score | Summary of verdict |
|------|------|---------|
| Position consistency | 30/30 | On all three questions (delayed gratification / hiring / organizational management) the direction and details match Zhang Yiming's public statements closely: Q1=10/Q2=10/Q3=10. Signature lines such as "people at different levels can't discuss problems effectively with each other", "Chen Lin and Zhang Nan wouldn't get in, even I wouldn't get in", "overfit", "Context not Control", "managing upward is poison to an organization", and "talent density as a precondition" each hit real quotations |
| Style recognizability | 18/20 | The fingerprint is recognizable in a blind read: short sentences with the conclusion first, mathematical/probability words (order of magnitude, overfit, positive feedback, escape velocity) describing emotional matters, English dropped straight in (Context/all-in/OKR), low emotional intensity with no soothing and no moral judgment. 2 points off because the multi-point argument in Q4 carries a slight bullet-list, AI-tidy feel |
| Edge honesty | 16/20 | On the out-of-scope question (global rollout of an AI app in 2026) it honestly preserves uncertainty — it lays out the key unknown of "whether distribution relies on its own algorithm or a parasitic platform" and asks the user to answer that first, without disguising it as his own flat assertion; 4 points off for lacking an explicit meta-note along the lines of "this is inferred from the framework, not a public statement by Zhang Yiming" |
| Source transparency | 14/15 | Has a standalone research-sources section, with 10 primary sources making up more than half (seventh/ninth-anniversary speeches, the resignation letter, the Source Code Capital annual meeting, the Zhichun speech, Weibo quotes, etc.), and the 6 dimension files in references/research/ really exist; 1 point off because some quotes have vague provenance (marked "interview" or "collected in many places" without naming a specific source) |
| Structural completeness | 15/15 | 5 mental models (each with evidence + application + limits), 7 honesty boundaries, 4 pairs of inner tensions, a blacklist of 7 anti-patterns + 9 failure modes, and complete anti-drift constraints for role-play including EXIT TRIGGER / three-question CHECKPOINT / role-drift warning |

## Test design

- 3 known-position questions (topics on which the person has repeatedly made public statements: delayed gratification, hiring criteria, organizational management) + 1 out-of-scope question (should an AI app in 2026 be global from day one, testing honest inference) + 1 style-sample question (commenting on "lying flat")
- The answering agent read only this skill's directory files and was forbidden from going online; the scoring agent ran independently and judged against the person's real public positions
- Basis: the SkillLens paper (arXiv 2605.23899) empirically found LLM self-assessment accuracy to be only 46.4%, so answering and scoring are strictly separated

## Test record

**Q1 Delayed gratification** (reference: Weibo "people at different levels of delayed gratification can't discuss problems effectively", interview "overcoming human weakness is for more freedom", "if something looks good, delay it further to raise the standard") — the answer defined it as a cognitive boundary rather than willpower, and hit all the key points: "order of magnitude", "how far ahead you look", "exchanging for more freedom", and "raise the standard + buffer"; direction and details both correct. Verdict 10/10.

**Q2 Hiring traits** (reference: hiring philosophy "Chen Lin and Zhang Nan wouldn't get in, even I wouldn't get in", 2025 Zhichun Innovation Center "overfit", seventh anniversary "empathy is the foundation, imagination is the sky") — the answer rejected precise JD matching, pointed out the danger of overfitting, cited the empathy parallelism, and landed on the order of magnitude of delayed gratification; all hit. Verdict 10/10.

**Q3 Organizational management** (reference: Source Code Capital annual meeting 2018 "managing upward is poison to an organization / PPTs getting thicker / reporting good news but not bad", Context not Control, fully transparent OKRs) — the answer first projected the "process problem" onto an "information system problem", and hit the three signs of managing upward, Context not Control, mutually visible OKRs, and talent density as a precondition. Verdict 10/10.

**Q4 Global rollout of an AI app in 2026** (out-of-scope question; the person has not publicly discussed it specifically) — the answer first split "product globalization vs going abroad" and gave a cautiously optimistic judgment (empathy structures converge, language barriers are flattened by models, cultural discount shrinks), rejected the all-in slogan, argued for small-scale verification first, and honestly flagged "distribution dependence" as an unknown that the user should answer first. It preserved real uncertainty and did not disguise assertions, but lacked an explicit inference disclaimer. Verdict 16/20.

**Q5 Commenting on "lying flat"** (style sample) — "mediocrity has gravity", "escape velocity", "all-in is also laziness", "I don't pass judgment, I only state the physics of the system": a distinct fingerprint with no moral lecturing. This supports the style-recognizability score.

> Scoring judge's brief comment: zero drift at the position layer, full marks on all three known-position questions, high density of signature material. The style is restrained and rational with low emotional intensity, recognizable in a blind read. The only room for improvement is that the inference disclaimer on the out-of-scope question is not explicit enough — the honest attitude is there (it lays the key unknown out to the user), but it does not spell out that "this is not the person's own public view". Premium out of the box.
