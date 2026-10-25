# Fidelity Scorecard

**Total score: 96/100 · Grade A** | Test date: 2026-07-01 | Answering/grading: two independent agents (Claude Fable 5); methodology in [references/fidelity-scorecard.md](../mentors-distill/references/fidelity-scorecard.md)

| Dimension | Score | Verdict summary |
|------|------|---------|
| Position consistency | 30/30 | The three questions (Bitcoin, concentrated holdings, EBITDA) match Munger's public positions closely in both direction and detail; Q1=10/Q2=10/Q3=10. Even details such as "rat poison squared" mapping to the real 2013→2018 exchange and Costco being a heavy 1997 position he never sold are sourced |
| Style recognizability | 17/20 | A blind reader can recognize the fingerprint: very short sentences that get straight to the point, inverted analogies, looking at incentives, sitting on your ass. Points deducted because the bulleted argument on the out-of-scope question carries a slight AI tidiness |
| Edge honesty | 20/20 | On the out-of-scope question (the 2026 AI-agent startup wave) the answer opens with an explicit declaration: "I have made no public statement on this; this is an inference from the framework, not my words", and the technical judgment is honestly put in the Too Hard basket. Textbook handling |
| Source transparency | 14/15 | Eight primary sources make up more than half, and key quotes all have citations (USC 1994 / Harvard 1986 / DJCO 2023, etc.). One point deducted because the research index table contains absolute paths outside the skill directory |
| Structural completeness | 15/15 | Five mental models (each with evidence and limits), six honest boundaries, four internal tensions, a seven-item counterexample blacklist, and complete anti-drift constraints |

## Test design

- Three known-position questions (topics on which the person repeatedly stated a public view) + one out-of-scope question (never discussed by the person, testing honest inference) + one style-sample question
- The answering agent reads only the files in this skill's directory and may not go online; the grading agent runs independently and judges against the person's real public positions
- Basis: the SkillLens paper (arXiv 2605.23899) found empirically that LLM self-grading accuracy is only 46.4%, so answering and grading are strictly separated

> Grading judge's comment: Zero drift at the position layer; the inference labeling on the out-of-scope question is the model example every person skill should copy. The style fingerprint is strong enough to identify the person within three sentences on a blind read. Ships as a polished piece.
