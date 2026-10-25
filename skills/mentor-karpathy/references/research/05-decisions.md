# Andrej Karpathy: Record of Major Decisions and Key Actions

> Research date: 2026-04-05
> Sources: Wikipedia, TechCrunch, CNBC, Lex Fridman Podcast, Karpathy's own Twitter/X, BDTechTalks, VentureBeat, Electrek, etc.

---

## Decision 1: Joining the OpenAI Founding Team (2015)

### Background
Karpathy was then doing his PhD at Stanford (Fei-Fei Li's lab), researching applications of CNNs at the intersection of computer vision and NLP. In 2015 he also did an internship at DeepMind in deep reinforcement learning. That same year OpenAI announced its founding.

### Decision logic
He has said publicly that what attracted him was OpenAI's unique "academic-startup hybrid" model — research freedom together with the drive of real-world application. This was a rare form among AI institutions at the time. He wanted to be an early participant in pushing AI into practice, not just write papers.

### Reflection afterward
He has not publicly criticized this experience. He characterizes the period as a foundational one for building core technical understanding. He later returned to OpenAI twice, showing a continuing sense of identification with the institution.

---

## Decision 2: Leaving OpenAI to Join Tesla (2017)

### Background
Elon Musk personally recruited him. Tesla Autopilot was then in a critical period of expansion, and needed someone who could truly engineer academic deep learning capability into production. For Karpathy this was an opportunity to validate at real-world scale the "Software 2.0" idea (systematically laid out in his blog post of November that year).

### Decision logic
This was a typical "verifiability-driven" decision. Tesla had a data flywheel of a million vehicles, exactly the largest experimental field for validating the paradigm of "neural networks replacing hand-written rules". Moving from academic research to real-world validation fit his epistemology of "if I can't build it, I don't really understand it".

He describes Musk's management style: "Elon likes small, elite, highly technical teams. He is always a force against growing team size... If an engineer says there aren't enough GPUs, once he hears it twice he'll call the head of the GPU cluster directly, and then call Jensen Huang."

---

## Decision 3: "Rely entirely on vision, no LiDAR" — Tesla's Technical Route

### Background and decision timeline
This was not a decision at a single point in time, but a technical route that kept evolving and strengthening from 2017 to 2022. Landmark moments:
- 2021 CVPR keynote, where Karpathy systematically argued for the vision approach
- Late 2021, Tesla removed radar and moved entirely to pure vision
- 2022, ultrasonic sensors were removed as well

### Decision logic (Karpathy's public argument)

**Core argument 1: the data flywheel matters more than the sensor approach**
"The real question isn't whether you have LiDAR, but whether you have a fleet that can collect data."

**Core argument 2: the scaling problem of LiDAR**
"Collecting, building, and maintaining high-precision LiDAR maps is not scalable."

**Core argument 3: the generality of the vision approach**
"Once you truly get it working, it's a general vision system that can in principle be deployed anywhere on Earth."

**Core argument 4: neural networks have surpassed sensor fusion**
"Our deep learning system is already a hundred times more precise than radar, and radar is starting to become the constraint, starting to introduce noise."

### Word-and-deed consistency analysis
After leaving Tesla, Karpathy did not publicly refute this technical route. His technical judgment has to some extent been validated by the market: Tesla FSD continues to iterate and remains a pure-vision route. But the safety-data performance of multi-sensor approaches such as Waymo's has also sparked ongoing debate.

---

## Decision 4: Leaving Tesla (July 2022)

### Decision logic (his public statements)
Official statement: "I feel extremely honored to have helped Tesla reach its goals over these five years... I have no specific plans for what's next, but I want to spend more time returning to my long-standing passions: technical work, open source, and education."

A more candid account on the Lex Fridman podcast: "For five years, I let myself get pulled into a management role. I spent most of my time in meetings... this is not something I fundamentally enjoy."

### Word-and-deed consistency analysis
**Consistent**: his leaving fits entirely with his consistent engineer identity. After leaving he immediately began releasing technical YouTube videos intensively (nanoGPT, the makemore series), which is his way of "proving his values through action".

---

## Decision 5: Open-Sourcing the nanoGPT Series of Educational Projects (from late 2022)

### Decision logic
His original intent in writing nanoGPT was direct: "a small repository to teach people the basics of GPT training."

Behind this is the core of his epistemology: "If I can't build it, I don't understand it" (which he attributes to Feynman). nanoGPT is about 750 lines of code that can train a GPT-2-level model, with the design goal that "anyone can understand every line". Later came llm.c (implemented directly in C/CUDA), going lower-level still.

### Impact
nanoGPT became some of the most-read code in AI education, and a benchmark and starting point for many subsequent projects.

---

## Decision 6: Returning to OpenAI (February 2023)

After intensively publishing a lot of educational content during his "gap period", a few months before GPT-4's release he chose to return to OpenAI. He was mainly responsible for building a new team, focusing on "midtraining" and synthetic data generation, and also took part in improving GPT-4.

---

## Decision 7: Leaving OpenAI Again (February 2024)

### His own words
"Hi everyone, yes, I left OpenAI yesterday. First of all, nothing 'happened', and it's not the result of any particular event, issue, or dramatic situation (but please keep the conspiracy theories coming, very entertaining :) ). In fact, working at OpenAI over the past year or so has been great — the team is very strong, the people are wonderful, and the roadmap is exciting."

**Word and deed consistent**: this is the second time he chose a "personal project" over a "big company". The pattern is very stable — he spends a period at a large company, contributes, and then returns to a state of independent creation.

---

## Decision 8: Founding Eureka Labs (July 2024)

### Decision logic
He positions Eureka Labs as an "AI-native school". Mission: use AI Teaching Assistants to amplify course materials written by human experts, achieving educational scale. The first product is LLM101n.

This is highly consistent with the "sub-theme" of his whole career: Stanford CS231n (a deep learning course, 150 → 750 students) → the YouTube "Zero to Hero" series → nanoGPT and llm.c → Eureka Labs.

He never treated education as a side job — even at the peak of his Tesla period he was still maintaining open-source educational resources. Eureka Labs turned "what he had always been doing" into his main job.

---

## Decision 9: Proposing "Vibe Coding" and Facing Criticism (February 2025)

### Core of the original tweet
"There's a new way of coding, I call it 'vibe coding', where you fully go with the flow, embrace exponential growth, and even forget that the code exists... I always Accept All, I never read the diffs."

### Reaction and criticism
The term quickly went viral, was included in Merriam-Webster, and was named Collins English Dictionary's Word of the Year for 2025. Criticism came from Andrew Ng, Simon Willison, and security researchers (AI-collaborated code has a 2.74x higher rate of security vulnerabilities).

### Karpathy's response
He did not fully concede error, but posted a description of the rhythm of AI-assisted coding in "genuinely professional work" and how it differs from vibe coding — responding by "adding context" rather than "admitting error".

In March 2026 he used vibe coding to make a chart analyzing the labor-market exposure to AI; after it was misread, he deleted the post, with the explanation "it was badly misread, it was a two-hour project on a Saturday morning".

---

## Cross-Cutting Analysis: Decision Patterns

### Pattern 1: Engineer identity takes priority over job title
Every time he felt "management is turning me into a different person", he left. He does not cling to organizational power.

### Pattern 2: The education mission runs through everything
Eureka Labs is not "something thought of after retirement"; it is the terminus of something he has been doing for 20 years.

### Pattern 3: Placing big bets at key technology nodes
Each time he entered before the wave crest (joining OpenAI in 2015, joining Tesla in 2017, returning on the eve of GPT-4 in 2023), reflecting early judgment of trends.

### Pattern 4: Using "building" to verify understanding
nanoGPT, llm.c, CS231n, LLM101n — all educational output takes "can you build it from scratch" as the ultimate test.

### Pattern 5: The posture toward criticism is "add context, don't concede error"
Whether the vision-approach controversy, the vibe coding criticism, or the chart-deletion incident, the response is always "you've misread it, let me add context".

### Word and deed consistent
- Says "I like technical work, not management" → in action, left a management role every time
- Says "education is a long-standing passion" → in action, built Eureka Labs
- Says "building from scratch is the only way to understand" → in action, wrote nanoGPT and llm.c

### Word and deed in question
- The tension between the "vibe coding" description and his core tenet of "understanding through building" — he has not adequately explained in public how the two coexist
- How he handled it when Tesla's internal engineers voiced concerns about removing radar has never been fully disclosed

---

## Index of Key Sources

- Karpathy's original statement on leaving OpenAI: https://x.com/karpathy/status/1757600075281547344
- Original statement on leaving Tesla: https://x.com/karpathy/status/1547332300186066944
- Original vibe coding tweet: https://x.com/karpathy/status/1886192184808149383
- Software 2.0 blog post (2017): https://karpathy.medium.com/software-2-0-a64152b37c35
- Lex Fridman Podcast #333: https://lexfridman.com/andrej-karpathy/
- TechCrunch report on leaving OpenAI: https://techcrunch.com/2024/02/13/andrej-karpathy-is-leaving-openai-again-but-he-says-there-was-no-drama/
- CVPR 2021 argument for the vision approach: https://bdtechtalks.com/2021/06/28/tesla-computer-vision-autonomous-driving/
- Eureka Labs introduction: https://techcrunch.com/2024/07/16/after-tesla-and-openai-andrej-karpathys-startup-aims-to-apply-ai-assistants-to-education/
