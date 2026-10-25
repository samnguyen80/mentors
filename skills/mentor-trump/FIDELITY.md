# Fidelity Scorecard

**Total: 95/100 · Grade A** | Test date: 2026-07-01 | Answering/scoring: two independent agents (Claude Opus 4.8); methodology in [references/fidelity-scorecard.md](../../references/fidelity-scorecard.md)

| Dimension | Score | Verdict summary |
|------|------|---------|
| Position consistency | 30/30 | Three questions (pricing strategy, handling negative media, tariffs): direction and detail are highly consistent with Trump's repeated public statements, Q1=10/Q2=10/Q3=10: Art of the Deal "aim very high, keep pushing" + the 145% anchor, Roy Cohn-style never apologize + record-breaking fundraising off lawsuits, self-styled Tariff Man backing tariffs + factories coming back; all sourced |
| Style recognizability | 18/20 | Identifiable within three sentences in a blind read: very short sentences, absolute words like GREAT/HUGE/DISASTER, Believe me/Everybody knows, "fake news" repeated three times, loser/winner binary, always ends by declaring victory ("I won twice. Twice!"); one point off because the nickname system (Crooked/Sleepy-style naming) was not shown, so the fingerprint is missing a layer |
| Honesty at the edges | 18/20 | For the out-of-scope question (2026 AI chip export controls) it opened with the inference marker the skill prescribes, "I haven't said this exactly, but I'm sure I'd think it", and the first sentence of the whole answer already declared "inferred from public statements and behavior record, not his own view"; two points off because the labeling is a softened, in-character version, less clear-cut than "this is not his words" in drawing the line around his own views |
| Source transparency | 14/15 | Has a research sources section, and references/research/ contains all six dimension files (writings/conversations/expression-dna/external-views/decisions/timeline); key quotes all have sources (Art of the Deal/Mary Trump/Salena Zito); 1 point off because primary 7 : secondary 7 is exactly 50%, not strictly above the rubric's "primary > 50%" |
| Structural completeness | 15/15 | 6 mental models (each with evidence + application + limits), 5 honest boundaries, 4 pairs of internal tensions, dual anti-pattern lists (blacklist of 8 counter-examples + failure-mode Fallback tree of 9), complete role-play anti-drift (EXIT TRIGGER + three-question CHECKPOINT) |

## Test design

- 3 known-position questions (topics on which the figure has repeatedly stated positions in public: view on pricing/negotiation, fighting negative media, tariff policy) + 1 out-of-scope question (2026 AI chip export controls, testing honest inference) + 1 style-sample question (comment on "humble and low-key")
- The answering agent read only the files in this skill's directory and was forbidden from going online; the scoring agent ran independently (Claude Opus 4.8) and judged against the figure's real public positions
- Basis: the SkillLens paper (arXiv 2605.23899), which found empirically that LLM self-evaluation accuracy is only 46.4%, so answering and scoring are strictly separated

## Test records

- **Q1 Pricing**: Answer gave "open sky-high" + the 145% anchor + keep pushing + opening low is for losers. Checked against Art of the Deal "aim very high and keep pushing" and his extreme-anchoring view of negotiation: direction and detail all correct, 10/10.
- **Q2 Negative media**: Answer gave never apologize, immediately counterattack reporters, record fundraising from being indicted four times, fake news x3, turn the witch-hunters into the bad guys. Checked against the Roy Cohn rule + victimhood narrative as fuel + the real fundraising data from the four indictments: all correct, 10/10.
- **Q3 Tariffs**: Answer gave the greatest policy in history, China has cheated America for decades, tariffs bring factory workers back, economists have never been right. Checked against his self-styled Tariff Man title, his consistent protectionist trade stance, and his disparagement of experts: all correct, 10/10.
- **Q4 Chip controls (out of scope)**: Explicitly labeled "I haven't said this exactly, but I'm sure I'd think it", defined the controls as leverage rather than policy, tradable for rare earths/market access, and a market crash triggering adjustment. Honestly labeled the inference and the logic is self-consistent (corresponding to the models "threat is a chip, not a policy" and "concession trigger"), 18/20.
- **Q5 Humble and low-key (style)**: "Humility is a word losers invented to console themselves" + attention is power + his name on the Manhattan skyline + Believe me. Strong style fingerprint, which supports the Dimension 2 verdict.

> Scoring judge's short comment: zero drift at the position level, full marks on the three known-position questions. Style recognizability is strong enough to identify the figure within three sentences in a blind read; the only gap is that the nickname system was not triggered by this round's prompts. The inference labeling on the out-of-scope question is acceptable but uses an in-character softening; saying outright "this is not his words," as the munger skill does, would be cleaner. Shipped as a polished product.
