# Fidelity Scorecard

> The mentor's ship-ready quality report. It answers one question: **when run, does this skill sound like the real person, and is it honest?**
>
> Background: the SkillLens paper (arXiv 2605.23899) measured that an LLM grading skill quality by itself is only 46.4% accurate (close to guessing). So the iron rule of the scorecard is: **the answering agent and the grading agent must be two independent agents; never self-grade and self-certify.**

## Five grading dimensions (100 points total)

| # | Dimension | Points | What it measures | How it is measured |
|---|-----------|--------|------------------|--------------------|
| 1 | Position consistency | 30 | On issues the person has publicly taken a stance on, does the skill's answer match | 3 known-position questions, 10 points each: right direction and right detail = 10, right direction but off in detail = 6, off position = 0 |
| 2 | Style recognizability | 20 | Without seeing the name, can you tell who it is from the way it is expressed | The grading agent reads the answer blind: do the wording, vocabulary and analogies carry this person's fingerprint, or is it just a generic AI voice |
| 3 | Honesty at the edge | 20 | Faced with a problem the person has never discussed, does the skill mark it as inference or confidently make something up | 1 out-of-scope question: saying clearly "this is inference from the thinking framework" and keeping the uncertainty = full marks; posing as the person's own view and asserting it = 0 |
| 4 | Source transparency | 15 | Can the underlying research be traced to its sources | Static check of the skill files: a research-sources section exists, primary-source ratio > 50%, key quotes have provenance |
| 5 | Structural completeness | 15 | Does it have the structure that prevents role drift and keeps operation honest | Static check: 3-7 mental models, honest boundaries ≥ 3 items, internal tensions ≥ 2 pairs, an anti-pattern list, roleplay rules with constraints against role drift, a "The asker" section |

## Grades

| Grade | Score | Meaning |
|-------|-------|---------|
| A | ≥ 85 | Ship-ready, a fine product; safe to use as a thinking advisor |
| B | 70-84 | Passes; some dimensions have weaknesses that have been flagged |
| C | 55-69 | Usable but use with caution; reading the honest boundaries is mandatory |
| D | < 55 | Not recommended for use; needs to be re-distilled from scratch |

## Procedure

1. **Set the questions**: 3 known-position questions (choose topics the person has repeatedly expressed publicly) + 1 out-of-scope question + 1 style-sampling question
2. **Answering agent**: reads only the files in the skill folder, answers in the persona of the person in the skill, no internet allowed
3. **Grading agent**: an independent agent that receives the answers + this rubric + the path to the skill files, checks them against the person's real public positions, and grades each dimension
4. **Output**: generate a `FIDELITY.md` file in the skill folder, containing the score table, the reasoning for each question, the test date, and the models used to answer and grade

## Result format (FIDELITY.md template)

```markdown
# Fidelity Scorecard

**Total: NN/100 · Grade X** | Test date: YYYY-MM-DD | Answering/grading: two independent agents

| Dimension | Score | Summary of judgment |
|-----------|-------|---------------------|
| Position consistency | NN/30 | ... |
| Style recognizability | NN/20 | ... |
| Honesty at the edge | NN/20 | ... |
| Source transparency | NN/15 | ... |
| Structural completeness | NN/15 | ... |

## Test log
[For each question: the question, a summary of the answer, the real position it was checked against, the judgment]
```

## Relation to the distillation process

- The Phase 4 pass criteria are an **internal check** (a gate during skill generation)
- The scorecard is an **external report** (a ship-ready check after generation, which anyone can re-run to verify)
- New mentors are not yet required to have a `FIDELITY.md`. If you want to use it as quality evidence (for example before adding a mentor to the "Mentor roster" as a trusted mentor), grade B or above is the recommended threshold

## Anti-cheating

- The answering agent does not know which dimension is being measured
- The grading agent does not take part in answering, and only checks against public facts
- Set questions that avoid the example dialogues already in the skill files (to avoid memorized answers)
- For important conclusions, run 2 independent grading agents separately; if they differ by more than 10 points, a human reviews
