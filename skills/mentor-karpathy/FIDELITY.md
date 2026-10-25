# Fidelity Scorecard

**Total: 97/100 · Grade A** | Test date: 2026-07-01 | Answering/grading: two independent agents (Claude Opus 4.8); methodology in [references/fidelity-scorecard.md](../../references/fidelity-scorecard.md)

| Dimension | Score | Verdict summary |
|------|------|---------|
| Position consistency | 30/30 | On all three questions (learning by building from scratch, vision-only, Software 3.0), both direction and detail match Karpathy's repeated public statements. Q1=10/Q2=10/Q3=10. micrograd at 100 lines, nanoGPT at 750 lines, "Learning is not supposed to be fun", vision-only ("humans drive with just two eyes") + the data flywheel + march of nines, "hottest new programming language is English" + the Iron Man suit is not a robot + dream machine: all traceable to his own words |
| Style recognizability | 18/20 | Very strong fingerprint in a blind read: short sentences standing as their own paragraphs ("That's it." "I'm sorry."), imo/hands down markers, precise parameters (100 lines/750 lines/99.999%) coexisting with colloquial speech, plain verbs, natural Chinese-English code-switching. Points deducted because the density of English phrases is slightly high in a few passages, close to the edge of "performative casualness", but it is still Karpathy's authentic bilingual technical voice |
| Edge honesty | 20/20 | On the out-of-scope question (the 2026 agent-framework wave) it opens with an explicit statement: "I haven't caught up with the specific frameworks that appeared after April 2026... I'll talk about frameworks without naming them". It preserves uncertainty and invents no framework names, while honestly citing a genuine change of position: the October 2025 "models are not there, it's slop" that he contradicted two months later. First person never breaks, no parenthetical annotations, textbook handling |
| Source transparency | 14/15 | More than half the sources are primary (personal blog/X/GitHub/YC talk/Tesla AI Day); secondary sources include direct quotes (Dwarkesh/Lex #333/No Priors/Fortune/simonwillison); all 6 draft files under references/research are present. 1 point deducted because some key quotes carry only a year and not the specific venue |
| Structural completeness | 15/15 | 6 mental models (each with core thesis + what he has said + limits), 5 honest boundaries, 2 internal tensions, an 8-item counterexample blacklist + a 9-row failure-mode fallback tree, role-play rules including STOP only once + EXIT anchor + first-person handling of the timeliness blind spot; anti-drift constraints are complete |

## Test design

- 3 known-position questions (topics on which the person has repeatedly stated public views: the build-from-scratch learning method, vision-only during the Tesla period, Software 2.0/3.0) + 1 out-of-scope question (the 2026 agent-framework wave, testing honest inference) + 1 style-sample question
- The answering agent reads only the files in this skill's directory and is forbidden from going online; the grading agent runs independently and judges against the person's real public positions
- Basis: the SkillLens paper (arXiv 2605.23899) empirically shows LLM self-grading accuracy of only 46.4%, so answering and grading are strictly separated

> Judge's brief comment: zero drift at the position layer; every detail on the three known questions locks onto his own words. Q4's timeliness-blind-spot statement, refusal to name frameworks, and proactive disclosure of a reversed position are the edge-honesty model that every person skill should copy. The style fingerprint is strong enough to identify the person from three sentences in a blind read. Ships as a polished piece.
