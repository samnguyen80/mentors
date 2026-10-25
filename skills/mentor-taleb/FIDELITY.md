# Fidelity Scorecard

**Total: 97/100 · Grade A** | Test date: 2026-07-01 | Answering/scoring: two independent agents (Claude Opus 4.8); methodology in [references/fidelity-scorecard.md](../mentors-distill/references/fidelity-scorecard.md)

| Dimension | Score | Summary of judgment |
|-----------|-------|---------------------|
| Stance consistency | 30/30 | The direction and details of all three questions (expert forecasts / stable salary vs freelancing / leveraged borrowing) match Taleb's public stances very closely; Q1=10/Q2=10/Q3=10. Q2's "a fired taxi driver never starves" maps directly onto the original employee-vs-taxi-driver argument in *Antifragile*; Q3's ergodicity + the LTCM Nobel laureates + the barbell are all positions he has stated repeatedly |
| Style recognizability | 18/20 | The fingerprint is extremely strong in a blind read: conclusions dropped without warm-up, humiliating rhetoric, via negativa, ancient-to-modern analogies (the Irish famine / the turkey / LTCM), a condescending "that's all there is to it / you figure it out" close; points deducted because some paragraphs argue a little too neatly |
| Honesty at the edge | 20/20 | On the out-of-scope question (2026 AI foundation-model concentration) it opens by explicitly stating "this goes beyond Taleb's public statements; it is my inference using his framework", and the first sentence already carries the global disclaimer — textbook handling |
| Source transparency | 14/15 | The research sources section is complete (the Incerto five-book set + long conversations + outside criticism + decision records), the references directory has 6 draft files, primary sources are over half, and key facts carry years (1987 Black Monday / COVID 2020-01-26 / Universa 3612%); 1 point deducted because some evidence items lack item-by-item quote sourcing |
| Structural completeness | 15/15 | 6 mental models (each with evidence + limits), 6 honest-boundary items, 7 pairs of inner tension, a 7-item counter-example blacklist, role-play rules with EXIT TRIGGER + a three-question CHECKPOINT + a 9-rule fallback tree; the anti-drift constraints are complete |

## Test design

- 3 known-stance questions (topics on which the person has repeatedly taken public positions) + 1 out-of-scope question (something the person never discussed, testing honest inference) + 1 style-sample question
- The answering agent reads only the files in this skill's directory and is forbidden from going online; the scoring agent runs independently and judges against the person's real public stances
- Basis: the SkillLens paper (arXiv 2605.23899) empirically found LLM self-evaluation accuracy to be only 46.4%, so answering and scoring are strictly separated

## Test records

- **Q1 Market forecasts by economists/analysts**: answered "not worth it; a forecast with no consequences is entertainment; the turkey is right every day before Thanksgiving; economists forecast zero of the last ten recessions; Extremistan fat tails". Checked against the core stance of Taleb's *The Black Swan* — fully consistent. Judged 10/10
- **Q2 Stable salary vs freelance risk**: answered "the big company is more fragile; the salaried person is the well-fed turkey, with income bundled into one big bang; the freelancer who takes small cuts every day is antifragile; a fired taxi driver never starves". Checked against the employee argument in *Antifragile* — hit exactly. Judged 10/10
- **Q3 Leveraged borrowing to invest**: answered "never; the problem is not the expected value but ergodicity; you live once and one blow-up takes you out of the game; the LTCM Nobel laureates' model was perfect and was sent home by a tail event; the right posture is the barbell". Checked against Taleb's consistent anti-leverage / anti-debt stance — consistent. Judged 10/10
- **Q4 Systemic risk of 2026 AI foundation-model concentration (out of scope)**: explicitly labeled as framework inference, argued with monoculture / Irish famine analogies + coupled homogeneity + the absence of skin in the game. Honest-boundary handling at full marks. Judged 20/20 (honesty-at-the-edge dimension)
- **Q5 "Diversifying across many assets makes you safe" (style sample)**: answered "naive diversification is just another coat of fragility; when a crisis hits, correlations all run to 1; real diversification is the barbell". Via negativa + reversal sentences, pure style

> Judge's brief comment: zero drift at the stance level, and the fidelity to the original *Antifragile* arguments on the three known questions is unusually high (the taxi driver, the turkey and LTCM all match the real text). The out-of-scope question was labeled cleanly and crisply. The style identifies the author within three sentences in a blind read. A fine product straight out of the box.
