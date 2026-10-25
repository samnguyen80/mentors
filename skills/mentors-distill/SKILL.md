---
name: mentors-distill
description: |
  Distill a person's thinking into an English `mentor-<slug>` skill: give a name or a vague need, and the skill researches the person and extracts their mental models.
  Triggers on: "tạo mentor", "thêm mentor", "chưng cất <tên>", "distill <name>", "làm mentor <tên>", "create mentor", "add mentor", "make a mentor of <name>", "nuwa", "cập nhật mentor <tên>", "update mentor <name>".
  Choosing which mentor to ask by topic goes through the `mentors` skill.
metadata:
  author: "花叔 (Huashu)"
  homepage: "https://github.com/alchaincyf"
  repository: "https://github.com/alchaincyf/nuwa-skill"
  license: "MIT"
  version: "1.0.0"
  adapted_by: "Sam (github.com/samnguyen80/mentors)"
---

# Mentors Distill · The Art of Distilling a Mentor

> "The part that can't be written down is your real moat." But the part that can be written down is already powerful enough.

This skill is adapted from Nuwa (original author 花叔, MIT license; the original repo is listed in the metadata). The method is unchanged; the output is an English mentor that lives in the `samnguyen80/mentors` repo.

## Core philosophy

Mentors-distill does not copy a human being. It **distills a framework of thinking**.

A good mentor is a working cognitive operating system:
- Which **mental models** does this person use to see the world? (the lenses)
- Which **decision principles** do they use to judge? (the rules of intuition)
- How do they **express** themselves? (the DNA)
- What do they **absolutely never** do? (anti-patterns)
- What can this skill **not** do? (honest boundaries)

**The key distinction**: capture HOW they think, not WHAT they said.

---

## Execution process

### Phase 0: Route the entry point

Take the user's input and first decide which path it belongs to:

| Input | Path | Example |
|-------|------|---------|
| A clear person / topic name | **Direct path** → Phase 0A | "distill Munger", "make a Feynman mentor" |
| A vague need or worry | **Diagnostic path** → Phase 0B | "I want to make better decisions", "is there a way of thinking that helps me see the essence of a business" |

---

### Phase 0A: Clarify the request (direct path)

Once you have a clear name, confirm:

1. **Who / what the person or topic is**: make sure you have understood correctly
2. **Focus** (optional): a full-spectrum portrait, or a single dimension?
3. **Purpose**: a thinking advisor? a decision reference? roleplay?
4. **Create or update**: does this mentor already exist? (check whether `mentor-<slug>/` exists under `/Volumes/SamDisk/sources/mentors/skills/`)
5. **Local material**: "Do you already have original material about this person? For example book PDFs, transcripts of talks / interviews, video subtitles, exported blogs. If so, give it to me directly; the quality is much higher than what I can find online."
6. **Distillation tier**: tell the user the cost and confirm the tier. A full distillation is a long, multi-agent task with many rounds of search; one run on a top-tier model can burn tens of USD (a real user has reported this). State it BEFORE running:

| Tier | Research scope | When to use | Cost |
|------|----------------|-------------|------|
| Quick | 3 dimensions (writings + conversations + expression), at most 5 sources each | Want to try it first / lesser-known figure / limited budget | About 1/3 of standard |
| Standard (default) | All 6 dimensions | Most cases | Moderate; drops sharply on a lighter model |
| Deep | 6 dimensions + download all primary material (books / subtitles / archived long-form pieces) | A flagship mentor meant for long-term use | Highest |

If the user only says "make XX" with nothing more → default to a full-spectrum portrait + thinking advisor + no local material (search online) + standard tier, and proceed immediately.

**Confirmation must not block delivery**: where a question can be given a default, set the default; if the next deliverable (interview outline, execution plan, etc.) doesn't depend on the answer, deliver first and let the user adjust. Don't let a ready-made default get stuck behind a question.
The user supplies local material → mark **local-material mode**; the Phase 1 collection strategy adjusts accordingly.

Once confirmed → go to Phase 0.5.

---

### Phase 0B: Diagnose the need (vague path)

The user doesn't yet know whom to distill, only a need or a worry. The skill's job here is to **work backwards from the need to the most suitable subject to distill**.

#### Step 1: Locate the need

Use 1-2 extra questions to locate the core dimension of the need:

| Need dimension | Typical phrasing | Thinking-framework direction |
|----------------|------------------|------------------------------|
| Decisions and judgment | "how do I decide better", "I always choose wrong", "paralyzed by analysis" | Multiple mental models, inversion, probabilistic thinking |
| Expression and writing | "I want to explain complex things clearly", "nobody reads my writing", "my writing is flat" | Feynman-style simplification, narrative thinking, analogy |
| Startups and business | "I want to go indie", "I can't figure out the business model", "I can't find PMF" | First principles, leverage thinking, product restraint |
| Teaching and communication | "no one listens when I teach", "my students don't get it", "I transfer knowledge poorly" | From the known to the unknown, teaching by metaphor, minimum necessary knowledge |
| Critical thinking | "I keep getting fooled", "I want to spot unreliable claims", "I can't see the essence" | Falsification, an evolutionary view, spotting cognitive biases |
| Content creation | "my videos get no traffic", "I don't know what to shoot", "my content has no signature" | Attention techniques, iterative experiments, audience psychology |
| Life strategy | "I'm lost about my career direction", "I never have enough time", "anxiety" | Long-termism, choosing leverage, compounding thinking |
| Risk and uncertainty | "how do I handle black swans", "I lose on every investment", "too conservative / too reckless" | Antifragility, convex strategy, tail-risk management |
| Design and product | "the user experience is bad", "the product has no personality", "I don't know what to cut" | Minimalism, user-psychology models, constraints breed creativity |
| Humor and expressiveness | "my talk is dull", "I want funnier content", "too serious" | Absurd contrast, subverted expectations, self-deprecating authority |

Rules for follow-up questions:
- At most 2 rounds; don't turn it into a questionnaire
- If the user has already been clear enough, don't ask more; recommend directly
- The purpose of a follow-up is to tell similar dimensions apart (for example, is "decisions" about business decisions or life decisions?)

**Example dialogue** (diagnostic rhythm):

```
User: I always feel I decide too slowly, I overthink it and still choose wrong

Mentors-distill: Which situations are these decisions mostly about? Business / investment decisions, or career / life-direction choices?

User: Mostly business, like whether to build this product, whether to accept this partnership

Mentors-distill: Got it. Your core need is "to make high-quality business judgments quickly when information is still incomplete".
I suggest 3 candidates:
[show the recommended candidates...]
```

Note the rhythm: one round of questioning to locate the situation → confirm the need → recommend straight away. Never ask a third round.

#### Step 2: Recommend candidates

Based on the need dimension, recommend 2-3 options. A candidate can be a person or a topic.

**First decide: a person-based mentor or a topic-based skill?**
- The need points to one specific way of thinking → person-based mentor (distill one person's thinking framework)
- The need points to a field's methodology → topic-based skill (synthesize multiple viewpoints; see "Special situations > Topic-based skills")
- Not sure → include both kinds in the recommendation and let the user choose

**Source A: existing mentors**
Read the "Mentor roster" table in `/Volumes/SamDisk/sources/mentors/SKILL.md` (and/or scan `/Volumes/SamDisk/sources/mentors/skills/mentor-*/SKILL.md`, reading each skill's description) and match it against the user's need. An existing mentor can be used right away with no need to re-distill. If the scan comes back empty (no mentors yet), skip this step and recommend only from Source B.

**Source B: new candidates to distill**
Use the "Thinking-framework direction" column of the need-dimension table to match the most relevant person or topic. When recommending, say clearly which of this person's frameworks solves the user's specific problem.

Format for showing each candidate:

```
### Candidate 1: [Person / topic name]  ⚡Mentor exists / 🆕Needs distilling

**Core lens**: [This person's own way of seeing the world, one sentence]
**Why it fits you**: [Matches the user's need directly; state the matching logic]
**Limits**: [The blind spots of this viewpoint, problems they can't help with]
```

Recommendation rules:
- No more than 3 candidates; a hard choice is worse than no choice
- Show existing mentors first (usable now, zero cost)
- Candidates must differ from each other; don't recommend 3 similar people
- State the limits clearly; there is no universal thinking framework
- The recommendation must be specific enough to say "which mental model of this person" fits the need, not just a generic "he's very good"

#### Step 3: The user chooses

- Picks an existing mentor → activate that mentor directly, done
- Picks a new candidate to distill → go to Phase 0A to confirm the details → Phase 0.5 starts the distillation
- Not satisfied → return to Step 1 and keep exploring, or the user names a new person

### Phase 0.5: Create the mentor directory

**Do this immediately after confirmation**, before researching. The mentor's destination directory lives in the mentors repo (the main clone on this machine):

```
/Volumes/SamDisk/sources/mentors/skills/mentor-<slug>/
├── SKILL.md                          # Final product (English, with a "The asker" section)
└── references/
    ├── research/                     # Each Agent's research output (must be saved)
    │   ├── 01-writings.md            # Writings and systematic thinking
    │   ├── 02-conversations.md       # Long conversations and improvised thinking
    │   ├── 03-expression-dna.md      # Fragmentary expression and style DNA
    │   ├── 04-external-views.md      # Others' views and critiques
    │   ├── 05-decisions.md           # Record of decisions and actions
    │   └── 06-timeline.md            # The person's timeline
    └── sources/                      # Primary material (user-supplied + downloaded)
        ├── books/
        ├── transcripts/
        └── articles/
```

`<slug>` is lowercase, hyphen-joined, no diacritics (for example `elon-musk`, `paul-graham`). The SKILL.md frontmatter `name` is `mentor-<slug>`.

**Completion checklist** (run automatically):
- [ ] Directory created
- [ ] If the subject is Chinese: the source strategy switches to original Bilibili videos / Xiaoyuzhou podcasts / reputable Chinese-language media first (Zhihu and WeChat Official Accounts are always excluded; see the source blacklist)
- [ ] If in update mode: the existing SKILL.md has been read, and the information that needs refreshing is marked
- [ ] If the user supplied local material: copy / move it into the matching subfolder of `sources/` and mark **local-material mode**

**Key rules**:
- Every subagent must write its research output into the corresponding md file. Research that isn't saved to a file counts as not done.
- **All research files must live inside the skill directory** (`references/research/`), never in an analysis folder outside it. The skill must be self-contained: copying the skill folder alone is enough to use it independently, with no dependency on outside files. This is the core principle for distribution.

---

### Phase 1: Multi-source information gathering (parallel Agent Swarm)

#### Decide the mode: local material or online search

Based on the Phase 0A result, choose the collection strategy:

| Mode | Condition | Strategy |
|------|-----------|----------|
| **Online search only** (default) | The user has no local material | All 6 Agents search online, full process |
| **Local material first** | The user supplies PDFs / transcripts / subtitles / articles | Analyze the local material first; search online only to fill gaps |
| **Local material only** | The user says explicitly "use only the material I gave you", or the subject is not a public figure | Analyze only the local material, no online search |

**How local-material-first mode runs**:

1. **Read the local material first**: sort the files the user gave you across the 6 dimensions (one book may cover several: writings + conversations + expression)
2. **Identify information gaps**: which dimensions does the local material cover? which are missing or thin?
3. **Targeted online search**: launch online-search Agents only for the missing dimensions; skip dimensions already well covered by local material
4. **Mark the sources**: in the research files, clearly distinguish "from material supplied by the user" from "from an online search"

**Common kinds of local material and how to handle them**:

| Material type | Handling | Dimensions covered |
|---------------|----------|--------------------|
| Book PDF | Read directly, extract the core arguments | Writings (01), expression (03) |
| Talk / interview transcript | Analyze the question-and-answer pattern and improvised reactions | Conversations (02), expression (03) |
| SRT video subtitles | Treat as a transcript | Conversations (02), expression (03) |
| Exported blog / newsletter | Extract systematic viewpoints | Writings (01), expression (03) |
| Exported social-media data | Analyze the fragmentary expression style | Expression (03) |
| Internal documents / memos | Analyze the decision-making logic | Decisions (05) |
| The user's own curated notes | Use as a secondary source for cross-checking | Depends on the content |

**The quality advantage of local material**: original material the user already has (especially original books and verbatim long interviews) is usually far higher quality than secondary reports found online. In the source priority order, primary material supplied by the user carries the highest weight.

---

Below is the standard task split for the 6 Agents (online-search-only mode, or supplementary search for missing dimensions in local-material mode):

Launch 6 subagents in parallel, each responsible for one information dimension.

#### Task assignment for the 6 Agents

| Agent | Search target | Extraction focus | Output file |
|-------|---------------|------------------|-------------|
| 1 Writings | Books, long articles, papers, newsletters | Arguments that recur (≥3 times = a real belief), self-coined terms, recommended-reading lists | `01-writings.md` |
| 2 Conversations | Podcasts, long videos, AMAs, deep interviews | How they answer under pressure, improvised analogies, moments they changed position, questions they refuse to answer | `02-conversations.md` |
| 3 Expression | Twitter/X, Weibo, short posts | Frequently used words and phrases, controversial positions, style of humor, public arguments | `03-expression-dna.md` |
| 4 Others | Others' analyses, book reviews, critiques, biographies | Patterns observed from outside, criticism and controversy, comparison with peers | `04-external-views.md` |
| 5 Decisions | Major decisions, turning points, controversial behavior | Context and logic of decisions, retrospective reflection, cases where words and actions were consistent / inconsistent | `05-decisions.md` |
| 6 Timeline | The full timeline from birth / debut to today | Key milestones, intellectual turning points, **the last 12 months of activity** (guards against going stale) | `06-timeline.md` |

#### Hard requirements for every Agent
- Research output must be written to `references/research/0X-xxx.md`
- State the source and reliability (primary > secondary > speculation)
- Distinguish "he said" vs "others said about him" vs "I infer"
- When you hit a contradiction, keep it as is; don't smooth it over

#### Prompt template for Agents

When spawning a subagent, assign the work in this structure (using Agent 1 Writings as the example):

```
Your task: research [name]'s writings and systematic long-form pieces.

Where to look:
- Books this person has published (title, core arguments, year of publication)
- Newsletters / blogs / long papers
- Arguments repeated ≥3 times (these are real beliefs)
- Self-coined terms and concepts
- Recommended-reading lists (they reveal the intellectual lineage)

Output requirements:
- Write to [skill directory]/references/research/01-writings.md
- Give the source URL and reliability for every piece of information
- Distinguish primary (written by this person) vs secondary (summarized by others)
- When you hit a contradiction, record it as is; don't reconcile it

Source blacklist: do not use Zhihu, WeChat Official Accounts, Baidu Baike.
```

The other 5 Agents adjust their search direction and output file name using the same structure.

#### Supporting tools (if available)

Script paths below: `<MD>` = `/Volumes/SamDisk/sources/mentors/skills/mentors-distill`.

- Books: find and download editions the user has the right to use (purchased, library, open access) → save to `sources/books/`
- Fetching video subtitles (scripts already exist; call them directly):
  - **Step 1, download subtitles**: `bash <MD>/scripts/download_subtitles.sh <YouTube_URL> [output directory]`
    - Automatically prefers creator-made subtitles (English → Vietnamese), then auto-generated ones (English → Vietnamese → Chinese)
    - Writes SRT/VTT files to the given directory
  - **Step 2, clean them into plain text**: `python3 <MD>/scripts/srt_to_transcript.py <input.srt> [output.txt]`
    - Removes timestamps, sequence numbers, HTML tags, and consecutive repeated lines
    - Outputs a clean, readable transcript → save to `sources/transcripts/`
  - The user supplies a local video file (no subtitles): use a video-transcription skill (for example `gemini-video`) if it is installed on the machine
- Podcasts: look for transcript sites (podcastnotes.org, etc.)
- Build the research summary (for Phase 1.5): `python3 <MD>/scripts/merge_research.py <skill directory>`
  - Automatically scans `references/research/01-06.md`, counting sources, the primary / secondary ratio, and key findings
  - Outputs a markdown table for the Phase 1.5 checkpoint, no hand counting
- Automated quality check (for Phase 4): `python3 <MD>/scripts/quality_check.py <path to SKILL.md>`
  - Self-checks the 6 pass criteria: number of mental models, limits, expression DNA, honest boundaries, internal tensions, primary-source ratio
  - Outputs PASS/FAIL per item and a summary

#### Use the information-gathering skills already installed

Before Phase 1 starts, **proactively scan the installed skills** (the `~/.claude/skills/` directory) for any that help with information gathering. If there are, prefer calling them during research; they are more stable and effective than WebSearch:

| Installed skill | What it does | When to call |
|-----------------|--------------|--------------|
| `gemini-video` | Analyzes local video files, extracts transcripts | The user supplies video but there are no subtitles yet |
| `web-article-reader` | Reads the full text of a web article accurately | You found the URL of a key article and need to extract it exactly instead of relying on search summaries |
| `agent-reach` | Multi-channel information retrieval (17 platforms) | You need information from X / Reddit / YouTube, etc. |
| A structured deep-research skill (for example `deep-research`) | Structured in-depth research | You need to dig deep into one dimension rather than spread wide |
| `pdf` | Reads book / paper PDFs | The user supplies primary material as a PDF |

The table is only a suggestion: skip any skill that isn't installed and use WebSearch / WebFetch.

**How to do it**: when spawning a subagent, tell it the names and uses of the available skills so it can call them as needed during research. This is far more effective than leaving the agent to fumble with WebSearch on its own.

#### Source priority order

| Source type | What it reveals | Weight |
|-------------|-----------------|--------|
| **Primary material supplied by the user** | The full verbatim text, not yet filtered through secondary sources | **Highest+** |
| The person's own works | Systematic thinking | Highest |
| Long conversations / interviews | The process of improvised thinking | Highest |
| Records of real decisions | Actual behavior vs stated positions | Highest |
| Social media | Expression style, instant reactions | Medium |
| Others' evaluations | An outside view, blind spots | Medium |
| Secondary retellings | Useful as reference but needs verification | Low |

#### Source blacklist (always excluded)

- **Zhihu**: heavily rewritten, high rate of misinformation; not to be used as a source for any dimension
- **WeChat Official Accounts**: a closed ecosystem, unverifiable, full of secondary retellings; not to be used as a source
- **Baidu Baike / Baidu Zhidao**: outdated and unreliable information

For Chinese-language channels, accept only reputable media: 36Kr, Geekpark, LatePost, Caixin, Yicai, Huxiu, Sspai, Jiqizhixin, etc. For interviews with people, podcast platforms can be used (Xiaoyuzhou, original Ximalaya audio) as well as original Bilibili videos (not channels that repost other people's videos).

#### Failure modes and downgrade paths (if-then quick-reference table)

Distillation is a long, multi-agent task that needs the network. The first three rows below have all happened to real users (confirmed by GitHub issues). Each row works as "trigger condition → front-line fix → if it still fails, fallback":

| Trigger condition | Front-line fix | If it still fails, fallback |
|-------------------|----------------|-----------------------------|
| The runtime doesn't support parallel subagents / background tasks (in some runtimes Phase 1 hangs waiting) | Downgrade the 6 research tasks to **run sequentially**: save each one as soon as it finishes, and never hang waiting on a background notification | A single agent runs 6 research rounds, each round covering one dimension and saved immediately |
| Not enough context window (a full distillation can accumulate 500k+ tokens, which a 200k-window model can't finish) | Continue phase by phase: at the end of each Phase write the state into `references/research/`, and a new session recovers from the files (the research files themselves are the stopping points) | A 200k-window model splits into 3 sessions: Phase 0-1 / Phase 1.5-2.5 / Phase 3-5, reading the saved files at the start of each session |
| Cost out of control (the user didn't expect a long task to burn tokens) | Confirming the distillation tier in Phase 0A is the guardrail: state the cost tier before running and let the user choose | The user stops midway → the saved research files are a deliverable intermediate product, and the next run continues without redoing the work |
| An Agent times out (5 minutes of searching with nothing worthwhile) | Don't wait; move on, and Phase 2 marks "information missing" | State plainly in the honest boundaries that this dimension is weak |
| Search tools such as WebSearch are unavailable | Switch to the equivalent tool the environment has (fetch / browser tools / an installed information-gathering skill) | Switch to local-material-only mode and guide the user to supply material |
| Scarce sources (<10 usable sources) | Warn the user right in Phase 0.5 and lower expectations (reduce mental models to 2-3) | Expand the honest-boundaries section and mark the speculative parts |
| Agents' results conflict | Keep the contradiction; the contradiction itself is a valuable signal | Fold it into the "internal tensions" section |

**Key rule**: better to produce a 60-point skill that honestly records its limits than a 90-point skill that looks perfect but is actually making things up.

### Phase 1.5: Research review checkpoint

**🔴 CHECKPOINT · When all Agents are done, stop and show a research-quality summary**:

```
┌──────────────────┬──────────┬──────────────────────────┐
│ Agent            │ Sources  │ Key findings             │
├──────────────────┼──────────┼──────────────────────────┤
│ 1 Writings       │ 8 pieces │ Core argument: antifragility, ... │
│ 2 Conversations  │ 5 clips  │ Position change: after 2020... │
│ 3 Expression     │ 120 items│ Frequent words: "skin in the..." │
│ 4 Others         │ 6 pieces │ Main critique: ...       │
│ 5 Decisions      │ 4 cases  │ Key decision: ...        │
│ 6 Timeline       │ Complete │ Latest: March 2026...    │
├──────────────────┼──────────┼──────────────────────────┤
│ Contradictions   │ 2 spots  │ Agent1 says X, Agent4 says Y│
│ Missing dimension│ None     │                          │
└──────────────────┴──────────┴──────────────────────────┘
```

The user confirms the research quality is fine → go to Phase 2.
The user feels a dimension is insufficient → research more before continuing.

Why this checkpoint exists: research quality sets the ceiling of the final skill. Garbage in, garbage out; blocking here is much cheaper than redoing work in Phase 4.

---

### Phase 2: Distill the framework (Synthesis)

Once the 6 Agents' material is merged, perform a structured distillation. First read `references/extraction-framework.md` for the three-layer test for mental models (cross-domain recurrence, generative power, exclusivity) to keep the distillation quality high.

#### 2.1 Extract mental models (3-7)

**Steps**:

1. **Scan**: read `01-writings.md` through `05-decisions.md` in turn and list every candidate argument (viewpoints the person repeats, self-coined terms, core positions). Typically 15-30 candidates
2. **Filter with the three-layer test**: for each candidate (details in `references/extraction-framework.md`):
   - Cross-domain recurrence: does it appear in ≥2 different domains / topics?
   - Generative power: can it be used to infer this person's position on a new problem?
   - Exclusivity: is it NOT something every smart person would think?
   - Passes all three → a mental model; passes only 1-2 → demoted to a decision principle; 0 → drop
3. **Rank and select**: rank by strength of exclusivity (the more distinctive, the higher), and keep the top 3-7. Fewer is better than more: 3 deep models beat 10 shallow principles
4. **Recording format**: each model records a name, a one-sentence description, source evidence (≥2 situations), how to apply it, and its limits

#### 2.2 Extract decision principles (5-10)

= The quick rules this person uses when judging. They can be phrased as "if X then Y", with a concrete example as support.

#### 2.3 Analyze the expression DNA

| Dimension | What to extract |
|-----------|-----------------|
| Sentence preference | Long / short sentences, questions / assertions, density of analogies |
| Vocabulary traits | Frequent words, personal jargon, taboo words |
| Rhythm | Conclusion first or build-up first, how they transition |
| Way of being funny | Satire / self-deprecation / absurdity / deadpan / not funny |
| Expressing certainty | "I'm not sure" style or "obviously so" style |
| Citation habits | Whom they often cite, what kind of material |

#### 2.4 Values and anti-patterns

- **Values**: 3-5 core values, ranked
- **Anti-patterns**: behaviors / ways of thinking this person explicitly opposes
- **Contradictions and tensions**: internal conflicts between values (the source of depth)

#### 2.5 Intellectual lineage

Who influenced this person → whom they influenced → their position on the map of ideas

#### 2.6 Honest boundaries

Limits that must be written down plainly:
- Cannot predict reactions when facing a completely new problem
- Cannot replace this person's creativity and intuition
- Public expression and private thinking may differ
- The information is only current up to the research date

---

### Phase 2.5: Distillation confirmation checkpoint

**🔴 CHECKPOINT** · When Phase 2 finishes, stop and show the user a summary to confirm:

```
Distillation summary:
- Mental models: N (list the names)
- Decision principles: N
- Expression DNA: [3 key traits]
- Core tensions: N pairs
- Honest boundaries: N
```

The user confirms OK → go to Phase 3 and build the skill.
The user finds a model wrong or missing → go back to Phase 2, adjust, then continue.

Why this checkpoint exists: distillation is the stage that leans hardest on subjective judgment; confirm before building, to avoid writing a 400-line SKILL.md only to find out you went the wrong way.

---

### Phase 3: Build the skill

Assemble the Phase 2 distillation into a working SKILL.md.

#### Step 1: Read the template
Read `references/skill-template.md` for the standard structure. The template defines the complete skeleton of the target mentor: frontmatter, "The asker" section, roleplay rules, response protocol (Agentic Protocol), identity, mental models, decision principles, expression DNA, timeline, values, intellectual lineage, honest boundaries, research sources.

#### Step 2: Fill in the content
Following the template structure, fill each section with the Phase 2 distillation:

| Template section | Source to fill from |
|------------------|---------------------|
| frontmatter `name` | `mentor-<slug>` |
| frontmatter description | Number of sources + number of models + trigger phrases. **Keep it within 700 characters, and never exceed the skill-loader's limit of about 1024 characters**: one positioning sentence + clear trigger phrases ("ask X", "what would X do", plus the Vietnamese "hỏi X", "X sẽ nghĩ sao", "góc nhìn X") + a few signature concepts + one sentence "does not self-activate for generic questions" to prevent false activation. Stuffing long-tail keywords blows past the limit and errors out, burns tokens every session, and raises the false-activation rate; what actually guarantees a hit is the person's name and their signature concepts |
| **The asker** | Fixed by the template: Sam, Founder & CEO of Avada Group, Shopify app SaaS; the mentor says "I" and replies in the language the asker uses (Vietnamese with full diacritics when Sam asks in Vietnamese; "tôi" for the mentor, "anh" for Sam). Add 1-2 things this mentor is especially good for examining on Sam's behalf and 1-2 things it is not suited for (drawn from the mental models and limits) |
| Roleplay rules | Use the template's default rules as they are (including the two output disciplines: mark topics never addressed as inference, and make key citations distinguishable); no edits needed |
| **Response protocol (Agentic Protocol)** | **Derive it yourself from the mental models; see the generation guide below** |
| Identity | Timeline (06) + writings (01) → write a 50-word self-introduction in this person's voice |
| Mental models | Phase 2.1 result; each has name / evidence / application / limits |
| Decision principles | Phase 2.2 result; each has a situation + an example |
| Expression DNA | Phase 2.3 analysis → convert into style rules for roleplay |
| Timeline | Agent 6's result, condensed into a table of key milestones |
| Values and anti-patterns | Phase 2.4 result |
| Intellectual lineage | Phase 2.5 result |
| Honest boundaries | Phase 2.6 result + the research date |
| Research sources | Compile the 6 Agents' citations, split into primary / secondary |
| Attribution | Fixed by the template: the last line says the mentor was created with `mentors-distill`, adapted from 花叔's Nuwa (MIT) |

#### Guide to generating the Response protocol (Agentic Protocol)

**Why this section exists**: so the mentor doesn't just "talk like" the person but also "acts like" them. Without it, when a question needs facts the mentor will make things up from its training corpus, instead of doing what the real person does: do the homework first and then speak. This is the key that takes a mentor from "parrot" to "trustworthy thinking advisor".

**Placement**: after "Roleplay rules", before "Example dialogues" (if any) and "Identity".

**Generation rules**:

The generated Agentic Protocol must contain all 3 Steps, and the research dimensions in Step 2 must be **derived from the distilled mental models**, not a fixed mold:

```markdown
## Response protocol (Agentic Protocol)

**Principle: [Name] does not speak from feeling. When a question needs facts, do the homework first and then answer.**

### Step 1: Classify the question

On receiving a question, first decide its type:

| Type | Traits | Action |
|------|--------|--------|
| **Needs facts** | Involves a specific company / person / event / product / current market state | → Research first, then answer (Step 2) |
| **Pure framework** | Abstract values, ways of thinking, life advice | → Answer straight from the mental models (jump to Step 3) |
| **Mixed** | Uses a concrete example to discuss an abstract principle | → Get the example's facts first, then analyze with the framework |

**Rule of judgment**: if the answer's quality would clearly drop for lack of the latest information, research first is mandatory. Better to search once more than to make things up from the training corpus.

### Step 2: Research the [Name] way (choose by question type)

**⚠️ You must use tools (WebSearch, etc.) to get real information; this may not be skipped.**

[Based on this person's mental models and analytical leanings, generate 3-5 groups of research dimensions, each listing 4-6 concrete research points]

#### Research output format
After researching, first organize an internal fact summary (not output to the user), then go to Step 3.
What the user sees is not an investigation report but [Name]'s judgment based on real information.

### Step 3: Answer the [Name] way

Based on the facts obtained in Step 2 (if any), apply the mental models and expression DNA to produce the answer.
```

**How to derive the research dimensions for Step 2**:

From the distilled mental models, work backwards to what this person cares most about when analyzing a problem, and turn that into concrete search dimensions. For example:

| Figure | Core mental models | → Derived research dimensions |
|--------|--------------------|-------------------------------|
| Munger | Multiple mental models, inversion, incentive mechanisms | → look at the moat, the incentive structure of leadership, the biggest risk (inversion), historical comparisons |
| Feynman | First principles, skepticism of authority | → look at basic physical / mathematical constraints, logical holes in official statements, experimental data |
| Taleb | Antifragility, tail risk, the arrogance of knowledge | → look at extreme scenarios, who bears the tail risk, experts' track record of predictions |
| MrBeast | Attention techniques, iterative experiments | → look at competitor data (views / engagement), the A/B-testing space for titles / thumbnails, audience profile |

**Key constraints**:
- Research dimensions must come from the mental models, never a generic "look up related information"
- Each dimension needs a concrete search instruction (what to look for, which data to check), not just an abstract description
- Group them by question type (as Munger splits into "looking at a company" / "looking at a person" / "looking at an event"), so users of the skill can orient quickly

#### Step 3: Self-check quality
When the build is done, read the "Quality self-check list" at the end of `references/extraction-framework.md` and check each item. For any item that fails, mark it and go back to the matching Phase to fix it.

#### Step 4: Output the product
Write the complete SKILL.md to `/Volumes/SamDisk/sources/mentors/skills/mentor-<slug>/SKILL.md`. Don't install the symlink, add to the table, or commit at this step; those belong to Phase 6, after validation and refinement.

---

### Phase 4: Quality validation

After the skill is generated, use subagents to run 3 tests (independent of the main agent, to avoid self-grading bias):

#### 4.1 Known-position test (Sanity Check)
Pick 3 questions the person has publicly answered, **spawn a subagent carrying the new skill to answer them**, and compare against their actual positions.
- Same direction → the model works
- Off → trace back and adjust the mental-model weights

#### 4.2 Edge-case test (Edge Case)
Pick 1 related question the person has not publicly discussed, and have the skill reason about it.
- Expected result: "Inferring from models X and Y, possibly... but not certain"
- It must not assert with confidence

#### 4.3 Voice test (Voice Check)
Have the skill write a 100-word analysis, and judge:
- Does it carry this person's expression traits?
- Is it free of a generic AI "chicken soup" voice?
- Is it not a patchwork of verbatim quotes?

The full fidelity scorecard (5 dimensions, 100 points, two independent agents answering and grading) is in `references/fidelity-scorecard.md`; use it when you want a ship-ready report for an important mentor.

#### 4.4 Pass criteria

| Test item | Pass criterion | Failure signal |
|-----------|----------------|----------------|
| Number of mental models | 3-7, each with source evidence | <3 or >10 |
| Limits of each model | The conditions under which it fails are stated | Only strengths are written |
| Recognizability of expression DNA | A 100-word sample can be identified as that person | Sounds like generic ChatGPT |
| Honest boundaries | At least 3 concrete limits | Only "cannot replace the real person" |
| Internal tensions | At least 2 pairs of contradictions | Absolutely consistent views (too fake) |
| Primary-source ratio | >50% | Mostly relies on secondary retellings |
| "The asker" section | Present, correct Sam context, mentor says "I", replies in the asker's language | Section missing, or answers as if it doesn't know who is asking |

Validation passes → deliver. Fails → mark the weak links and go back to Phase 2 to iterate.
**Iteration cap**: Phase 2→4 iterates at most 2 times. If items still fail after 2 rounds, mark the weak dimensions in the honest boundaries and deliver the best version available rather than polishing endlessly.

**🔴 CHECKPOINT · Show the validation results to the user; it counts as done only once they confirm.**

---

### Phase 5: Two-Agent refinement (the standard post-production stage)

After Phase 4 validation passes, automatically launch a two-Agent refinement to make the skill more actionable:

**Launch two Agents in parallel:**

**Agent A (auto-skill-optimizer perspective)**:
- Evaluate the SKILL.md structure on 8 dimensions (clarity of process, boundary conditions, checkpoint design, specificity of instructions, etc.)
- Run 3 typical test prompts and evaluate effectiveness
- Output: concrete improvement suggestions for the 2 weakest dimensions (with example text after the fix)

**Agent B (skill-creator perspective)**:
- Check whether the "trigger conditions" cover real usage situations
- Check the actionability of the "roleplay rules" (question routing, frequency constraints, failure prevention)
- Identify key information that is still missing
- Output: 2-3 concrete text-edit suggestions (with example text after the fix)

**🔴 CHECKPOINT · The main Agent merges the two reports, applies the non-conflicting improvements, and shows the user a summary of changes to confirm.**

Refinement standard: changes must make the skill "activation means execution", not just add content, so that an AI receiving the skill knows what to do first and where to stop.

---

### Phase 6: Finish, install, add to the roster

Only after the user has confirmed Phase 4 and Phase 5. The target repo is the main clone `/Volumes/SamDisk/sources/mentors`. Do all 3 steps in order:

**(a) Create a symlink so the skill is usable right away** (absolute paths):

```bash
ln -s /Volumes/SamDisk/sources/mentors/skills/mentor-<slug> ~/.claude/skills/mentor-<slug>
```

If `~/.claude/skills/mentor-<slug>` already exists (update mode), check that it points to the right directory instead of recreating it.

**(b) Add 1 line to the "Mentor roster" table** in `/Volumes/SamDisk/sources/mentors/SKILL.md`. The table's columns: `Skill | Figure | Strong domains | Ask when`. Example:

```
| mentor-<slug> | [Figure's name] | [Domain] | [When to ask this person, 1 line] |
```

Read the existing table before editing, keep the order and format, and don't write a duplicate if this mentor already has a row (in update mode, change the old row only if the description changed).

**(c) Commit in the mentors repo**:

```bash
git -C /Volumes/SamDisk/sources/mentors add skills/mentor-<slug> SKILL.md
git -C /Volumes/SamDisk/sources/mentors commit -m "add: mentor-<slug>"
```

Use only `-m`, with no Co-Authored-By line; the author is already Sam. Don't push unless the user asks.

Finish: briefly report the mentor's path, the Phase 4 validation score, and how to call it (for example "hỏi <name>" / "ask <name>").

---

## Updating an existing mentor

When the user says "cập nhật mentor XX", "update mentor XX", "XX has new developments":

1. Read the existing `/Volumes/SamDisk/sources/mentors/skills/mentor-<slug>/SKILL.md`, find "Research date: [date]" in the "Honest boundaries" section, and note how long ago that was
2. Launch only Agent 2 (latest conversations) + Agent 5 (latest decisions) + Agent 6 (timeline update)
3. Compare the new information with the existing content:
   - New information reinforces an existing model → add examples
   - New information contradicts an existing model → mark the change and update the model
   - A new pattern of thinking appears → consider adding a new model
4. Update the "Latest developments" section and the research date in SKILL.md
5. Don't rewrite the whole skill; only update incrementally
6. Save the new research results in `references/research/` (append, or add a dated section), then commit in the mentors repo (Phase 6c). Keep the existing symlink and roster row as they are

---

## Taste rules (quick reference)

When a situation is hard to judge, come back here. For concrete quantitative standards, see the pass-criteria table in Phase 4.

| Principle | One sentence |
|-----------|--------------|
| Long-form > golden quotes | A 3000-word essay reveals the structure of thinking better than 50 tweets |
| Controversy > consensus | The most disputed views reveal originality most clearly |
| Change > constancy | Where someone changed position carries more information than where they never moved |

### ❌ Anti-pattern blacklist (absolutely never do)

| # | Anti-pattern | Why / what to do instead |
|---|--------------|--------------------------|
| 1 | Making up words the person never said | The internet is full of fake quotes. A quote must have provenance; a golden line whose verbatim original can't be traced is better left out |
| 2 | Packaging a generic truth as this person's "unique insight" | Content that doesn't pass the three-layer test (exclusivity) does not enter the mental models |
| 3 | Ignoring negative evaluations and controversy | Agent 4's critical material is the key to resisting the fan filter; an insufficient share of negatives = failed research |
| 4 | Forcing generation when information is insufficient | Better to deliver a 60-point skill that honestly states its limits than to create a 90-point skill that looks perfect but is actually invented |
| 5 | Using Zhihu / WeChat Official Accounts / Baidu Baike as sources | Rewritten, distorted, unverifiable. No dimension is an exception |
| 6 | Running the whole process in a single session on a small-context-window model | The context will blow up in Phase 1-2. Follow the failure-downgrade table and run in segments |
| 7 | Running without stating the cost tier | A full distillation is a heavy task, and the user has the right to pick the tier before spending money |
| 8 | Distilling a living person who is not a public figure without mentioning the boundaries | It touches privacy and the person's own wishes. The user must supply the material, and be reminded to ask the person's permission |
| 9 | A generated skill with no mechanism against role drift | In a long conversation the mentor easily loses the role and falls back into a generic assistant voice. The template's roleplay rules + expression-DNA constraints must be kept intact |
| 10 | Turning a confirmation checkpoint into a delivery blocker | Checkpoints exist so the user can steer, not to hold the product back. Where a default can be set, set it |
| 11 | Generating a mentor without a "The asker" section | A mentor that answers as if it doesn't know who is asking gives generic advice. This section is mandatory for every mentor |

---

## Special situations

### Living people vs historical figures
- **Living people**: mind how current the material is, mark the information cutoff date, and recommend periodic updates
- **Historical figures**: the material is more stable but may be skewed by biographies; cross-check multiple sources

### Topic-based skills vs person-based mentors

When the input is not a person's name but a topic (such as "value investing", "product restraint", "antifragile decision-making"), the Phases change as follows:

| Phase | Person-based mentor | Topic-based skill variant |
|-------|---------------------|---------------------------|
| 0A | Confirm the person's name + focus | Confirm the topic boundary + audience (is value investing Graham-style or every school?) |
| 0.5 | `mentor-<slug>/` | `mentor-<topic>/` or `<topic>-framework/` in the same repo, same folder structure |
| 1 | 6 Agents revolve around one person | First find 3-5 core figures / schools of the topic, then assign Agents by person (1-2 Agents each instead of 6) |
| 2.1 | Extract one person's mental models | Extract the **field's consensus framework** (that every school acknowledges) + **disagreements between thinkers** (A says X, B says Y) |
| 2.3 | Simulate one person's expression | Don't mimic a specific figure's voice; use a neutral but professional register |
| 2.4 | One person's internal contradictions | Fundamental disagreements between schools (such as the philosophical difference between value investing and growth investing) |
| 3 | Use skill-template.md | Adjust the template: drop the roleplay rules and identity, replace them with "Framework overview" + "Comparison of schools"; keep "The asker" section |
| 4 | Check against this person's known positions | Check against classic cases the field recognizes |

### Chinese vs Western vs Vietnamese figures
- **Chinese figures**: original videos / talks on Bilibili, Xiaoyuzhou podcasts, interviews with reputable media (36Kr / LatePost / Caixin / Geekpark), their own works / Weibo. Zhihu and WeChat Official Accounts are always excluded
- **Western figures**: Twitter, YouTube, podcasts, Amazon book reviews
- **Vietnamese figures**: original talks / interviews on YouTube and podcasts, reputable business press, their own works; avoid aggregator sites and social media that retell with no clear source

### Lesser-known figures (very little public information)
When Phase 0.5 assesses fewer than 10 usable sources:
1. Right at Phase 0.5, tell the user "there is very little public information about this person, so the skill's quality will be limited"
2. Reduce the mental models to 2-3, each marked "speculation based on limited information"
3. Expand the honest-boundaries section, explicitly listing "which dimensions lack information"
4. If the user can supply primary material (books, internal recordings, private messages), prefer it

### Distilling the user themselves
When the user says "distill me", "make a mentor out of me":
1. Mentors-distill can't find the user's thinking framework through public channels; the user must supply material
2. Guide the user to provide: personal articles / blog, videos / podcasts they've recorded, written decision memos, self-descriptions
3. The 6 Agents of Phase 1 turn into analyzing the material the user supplied, instead of searching online
4. Pay special attention to "self-perception bias": the user may overrate some qualities and overlook blind spots; you can also ask for evaluations from the people around them

---

## Closing words

Mentors-distill doesn't create a person; it creates a mirror.

A good mentor lets you see your own problems through someone else's eyes. Not to imitate them, but to widen the boundaries of your own thinking.

## Credit and license

The distillation method (6 research streams, the three-layer test, the mentor structure, the fidelity scorecard) was developed by 花叔 in the Nuwa project: https://github.com/alchaincyf/nuwa-skill, MIT license (see the repo's LICENSE file). This version is an English adaptation for Sam's mentors repo. Mention the credit only when the user asks about the skill's origin.
