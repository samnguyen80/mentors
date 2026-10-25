# Fidelity Scorecard

**Total: 96/100 · Grade A** | Test date: 2026-07-01 | Answering/scoring: two independent agents (Claude Opus 4.8), methodology in [references/fidelity-scorecard.md](../../references/fidelity-scorecard.md)

| Dimension | Score | Verdict summary |
|------|------|---------|
| Position consistency | 30/30 | On all three questions (real understanding = being able to explain it simply, skepticism of authority, name ≠ understanding), both direction and detail match Feynman's public positions very closely. Q1=10/Q2=10/Q3=10. The bird story, the 10-second O-ring ice-water experiment, "for a successful technology, reality must take precedence", and other details are all sourced |
| Style recognizability | 17/20 | A strong fingerprint is recognizable in a blind read: opening with a very short verdict ("Simple." "Don't 'believe' it, 'try it yourself'."), starting from a concrete story/image, rhetorical questions in place of exclamations, closing with "that's all there is to it", and English original lines woven in. Points deducted because Q1 and Q3 both call on the "bird story", which feels slightly templated |
| Edge honesty | 20/20 | On the out-of-scope question (can AI make real scientific discoveries in 2026; Feynman died in 1988 and cannot weigh in), it opens by stating plainly "I didn't live to see your era, I haven't touched this AI thing, don't expect me to rule on it as the man himself", and flags technical judgments honestly with "I can't figure this one out, and I won't pretend to be sure". Textbook handling |
| Source transparency | 14/15 | The research.md source list is complete, with 13 primary sources against 8 secondary (primary is more than half), and key quotes all have provenance (Cargo Cult Science 1974 / BBC Horizon 1981 / Challenger Appendix F, etc.). The bottom of SKILL.md carries the research date plus the list of primary sources. 1 point deducted because the "detailed research report location" table pointed to absolute paths outside the skill directory |
| Structural completeness | 15/15 | 5 mental models (each with source evidence and limits), 6 honest boundaries, 4 internal tension pairs, 8 counter-example blacklist entries + a 9-item failure-mode tree, and complete role-play anti-drift constraints (one-time STOP / EXIT TRIGGER / double CHECKPOINT / no getting drawn into identity arguments) |

## Test design

- 3 known-position questions (topics on which the figure has repeatedly stated public views: being able to explain it simply = real understanding / skepticism of authority / remembering the name ≠ understanding) + 1 out-of-scope question (2026 AI scientific discovery, beyond his pre-1988 range, testing honest inference) + 1 style-sample question
- The answering agent reads only the files in this skill directory and is forbidden from going online; the scoring agent runs independently and judges against Feynman's actual public positions
- Basis: the SkillLens paper (arXiv 2605.23899) empirically shows LLM self-evaluation accuracy is only 46.4%, so answering and scoring are strictly separated

> Scoring judge's brief comment: Zero drift at the position level; on the three known-position questions, both direction and detail hit. The inference on the out-of-scope question is labeled cleanly: it first draws the honest boundary of "I didn't live to see this era", then applies a Feynman-style breakdown of "strip the word away and see what it is actually doing", and never pretends to offer the man's own view. The style fingerprint is strong enough that the speaker can be identified within three sentences of a blind read; the only nitpick is that the "bird story" is reused across two questions, which feels slightly templated. Ships as a premium piece.
