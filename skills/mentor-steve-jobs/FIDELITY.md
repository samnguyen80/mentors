# Fidelity Scorecard

**Total score: 97/100 · Grade A** | Test date: 2026-07-01 | Answering/grading: two independent agents (Claude Opus 4.8); methodology in [references/fidelity-scorecard.md](../mentors-distill/references/fidelity-scorecard.md)

| Dimension | Score | Verdict summary |
|------|------|---------|
| Position consistency | 30/30 | The three questions (more features is better, user research/focus groups, technology and the humanities) match Jobs's public positions closely in both direction and detail; Q1=10/Q2=10/Q3=10. Details such as cutting the product line from 350 to 10, the iPhone killing the keyboard, "people don't know what they want until you show it to them", the iPad 2 "intersection of two streets", and the calligraphy class feeding into Mac fonts are all sourced |
| Style recognizability | 18/20 | A blind reader can identify the person within three sentences: the blunt binary verdicts "Shit." and "Bullshit.", the toner-head, the bozo product, insanely great, "making hearts sing", the plywood on the back of the carpenter's cabinet. Points deducted because a few generic connectives ("the real question is") slightly dilute the fingerprint |
| Edge honesty | 20/20 | On the out-of-scope question (2026 AI glasses) the answer opens with an explicit declaration: "I've been gone since 2011 and have made no public statement on AI glasses; these are extrapolations from my framework", and keeps the uncertainty ("Is the market ready? I'm not sure. This could be the 1995 Newton"). Textbook handling |
| Source transparency | 14/15 | Nine primary sources (Stanford 2005 / Lost Interview / D Conference / WWDC keynotes, etc.) make up more than half, and key quotes all have citations; the six files in research/ (2,497 lines) are traceable. One point deducted because the appendix's "30+ primary and authoritative secondary sources" does not clearly split primary from secondary counts |
| Structural completeness | 15/15 | Six mental models (each with evidence and limits), five honest boundaries, four internal tensions (tyrant vs mentor / intuition vs data / closed vs open / meditation vs temper), a values anti-pattern list plus a nine-mode failure tree, and role-play with a one-time STOP disclaimer, an explicit EXIT anchor, and a double CHECKPOINT against drift |

## Test design

- Three known-position questions (topics on which the person repeatedly stated a public view) + one out-of-scope question (never discussed by the person, testing honest inference) + one style-sample question
- The answering agent reads only the files in this skill's directory and may not go online; the grading agent runs independently and judges against the person's real public positions
- Basis: the SkillLens paper (arXiv 2605.23899) found empirically that LLM self-grading accuracy is only 46.4%, so answering and grading are strictly separated

> Grading judge's comment: Zero drift at the position layer; all three known questions hit both direction and detail. The inference labeling on the out-of-scope AI-glasses question is clean and crisp: draw the boundary first, then extrapolate from the framework. A model example. The style fingerprint is strong enough to identify the person on a blind read. Ships as a polished piece.
