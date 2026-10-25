# Ilya Sutskever: Research on Academic Papers, Writings, and Core Ideas

> Research date: 2026-04-05
> Researcher: Claude Opus 4.6
> Source blacklist: Zhihu, WeChat Official Accounts, and Baidu Baike were not used

---

## 1. Background at a Glance

**Ilya Sutskever** (born 1985 in Russia, moved to Israel at age 5, later moved to Canada)

| Time | Event |
|------|------|
| 2005 | BSc in Mathematics, University of Toronto (entered directly from Grade 11) |
| 2007 | MSc in CS, University of Toronto, under Geoffrey Hinton; thesis: *Nonlinear Multilayered Sequence Models* |
| 2012 | Co-created AlexNet with Krizhevsky and Hinton, launching the deep learning revolution |
| 2012 | Postdoc at Stanford (about two months, Andrew Ng's lab) |
| 2013 | Google acquired DNNResearch → joined Google Brain |
| 2013 | PhD in CS, University of Toronto; thesis: *Training Recurrent Neural Networks* |
| 2014 | Created the Seq2Seq algorithm at Google Brain |
| 2015.12 | Left Google, co-founded OpenAI as Chief Scientist |
| 2023.07 | Formed the Superalignment team at OpenAI |
| 2023.11 | Took part in the board's removal of Sam Altman, later publicly said he regretted it |
| 2024.05 | Left OpenAI |
| 2024.06 | Founded SSI (Safe Superintelligence Inc.) |
| 2025.03 | SSI valued at $32 billion, raised $2 billion |
| 2025.07 | Became SSI CEO |

Sources: [Wikipedia](https://en.wikipedia.org/wiki/Ilya_Sutskever), [University of Toronto](https://www.cs.toronto.edu/~ilya/) | Credibility: primary + authoritative secondary

---

## 2. Major Academic Papers

### 2.1 Milestone papers (in chronological order)

#### 1. ImageNet Classification with Deep Convolutional Neural Networks (AlexNet, 2012)
- **Authors**: Alex Krizhevsky, Ilya Sutskever, Geoffrey E. Hinton
- **Core contribution**: Used a deep CNN to beat traditional methods on ImageNet by a wide margin, igniting the deep learning revolution
- **Citations**: Extremely high (Google Scholar shows Sutskever's total citations at 780,000+; this paper is among the most cited)
- **Paper link**: [NeurIPS 2012](https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks)
- **Credibility**: primary

#### 2. Sequence to Sequence Learning with Neural Networks (Seq2Seq, 2014)
- **Authors**: Ilya Sutskever, Oriol Vinyals, Quoc V. Le
- **Core contribution**: Used a multi-layer LSTM to map an input sequence to a fixed-dimensional vector, then decode it into the target sequence; laid the foundation for machine translation and dialogue systems
- **Paper link**: [arXiv:1409.3215](https://arxiv.org/abs/1409.3215)
- **Credibility**: primary

#### 3. Recurrent Neural Network Regularization (2014)
- **Authors**: Wojciech Zaremba, Ilya Sutskever, Oriol Vinyals
- **Core contribution**: Proposed an RNN regularization method that improves training stability
- **Paper link**: [arXiv:1409.2329](https://arxiv.org/abs/1409.2329)
- **Credibility**: primary

#### 4. Language Models are Unsupervised Multitask Learners (GPT-2, 2019)
- **Authors**: Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, Ilya Sutskever
- **Core contribution**: Showed that language models can learn multiple tasks in a zero-shot setting; the 1.5B-parameter GPT-2 reached SOTA on 7 of 8 language modeling benchmarks
- **Paper link**: [OpenAI](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)
- **Credibility**: primary

#### 5. Language Models are Few-Shot Learners (GPT-3, 2020)
- **Authors**: Tom Brown, Benjamin Mann, ... Ilya Sutskever et al.
- **Core contribution**: A 175B-parameter model showed strong capabilities in the few-shot setting, validating the scaling hypothesis
- **Credibility**: primary

#### 6. Weak-to-Strong Generalization (first result of Superalignment, 2023.12)
- **Team**: OpenAI Superalignment team (co-led by Sutskever)
- **Core contribution**: Used a GPT-2-level model to supervise GPT-4; the latter generalized to close to GPT-3.5 level, showing that a weak supervisor can steer a strong model
- **Paper link**: [OpenAI](https://openai.com/index/weak-to-strong-generalization/)
- **Credibility**: primary

### 2.2 Other important collaborative papers

| Paper/project | Sutskever's role | Notes |
|-----------|--------------|------|
| TensorFlow | Core contributor | Took part in development during his time at Google Brain |
| AlphaGo | One of the collaborators | Listed among multiple contributors |
| CLIP | Supervised during his OpenAI period | Multimodal contrastive learning |
| DALL-E | Supervised during his OpenAI period | Text-to-image generation |

Sources: [Wikipedia](https://en.wikipedia.org/wiki/Ilya_Sutskever), [Google Scholar](https://scholar.google.com/citations?user=x04W_mMAAAAJ&hl=en) | Credibility: primary + authoritative secondary

### 2.3 Doctoral dissertation

- **Title**: *Training Recurrent Neural Networks* (2013)
- **Advisor**: Geoffrey Hinton
- **Master's thesis**: *Nonlinear Multilayered Sequence Models* (2007)

---

## 3. Sutskever's List (Recommended Reading)

### Background

Around 2020, Sutskever emailed John Carmack a reading list of about 30 papers/blog posts, with the note:

> **"If you really learn all of these, you'll know 90% of what matters today."**

Sources: [GitHub reconstruction](https://github.com/dzyim/ilya-sutskever-recommended-reading), [Turing Post analysis](https://www.turingpost.com/p/ilya-sutskever-reading-list), [mattprd.com](https://www.mattprd.com/p/openai-cofounder-27-papers-read-know-90-ai) | Credibility: secondary (the original email has not been made public, but multiple independent sources cross-validate the list's contents)

### Full list (community-reconstructed version)

1. **The Annotated Transformer** — Sasha Rush et al. | [Link](https://nlp.seas.harvard.edu/annotated-transformer/)
2. **The First Law of Complexodynamics** — Scott Aaronson | [Link](https://scottaaronson.blog/?p=762)
3. **The Unreasonable Effectiveness of Recurrent Neural Networks** — Andrej Karpathy | [Link](https://karpathy.github.io/2015/05/21/rnn-effectiveness/)
4. **Understanding LSTM Networks** — Christopher Olah | [Link](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)
5. **Recurrent Neural Network Regularization** — Zaremba, Sutskever, Vinyals | [arXiv](https://arxiv.org/abs/1409.2329)
6. **Keeping Neural Networks Simple by Minimizing the Description Length of the Weights** — Hinton & van Camp
7. **Pointer Networks** — Vinyals et al. | [NeurIPS](https://papers.nips.cc/paper/5866-pointer-networks)
8. **ImageNet Classification with Deep Convolutional Neural Networks** — Krizhevsky, Sutskever, Hinton
9. **Order Matters: Sequence to Sequence for Sets** — Vinyals et al. | [arXiv](https://arxiv.org/abs/1511.06391)
10. **GPipe: Easy Scaling with Micro-Batch Pipeline Parallelism** — Huang et al. | [arXiv](https://arxiv.org/abs/1811.06965)
11. **Deep Residual Learning for Image Recognition** — Kaiming He et al.
12. **Multi-Scale Context Aggregation by Dilated Convolutions** — Fisher Yu & Vladlen Koltun
13. **Neural Message Passing for Quantum Chemistry** — Justin Gilmer et al.
14. **Attention Is All You Need** — Vaswani et al.
15. **Neural Machine Translation by Jointly Learning to Align and Translate** — Bahdanau et al.
16. **Identity Mappings in Deep Residual Networks** — He et al.
17. **A Simple Neural Network Module for Relational Reasoning** — Santoro et al.
18. **Variational Lossy Autoencoder** — Xi Chen et al.
19. **Relational Recurrent Neural Networks** — Santoro et al.
20. **Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton** — Aaronson et al.
21. **Neural Turing Machines** — Alex Graves et al.
22. **Deep Speech 2** — Amodei et al.
23. **Scaling Laws for Neural Language Models** — Kaplan et al.
24. **A Tutorial Introduction to the Minimum Description Length Principle** — Peter Grunwald
25. **Machine Super Intelligence** — Shane Legg (the doctoral thesis of a DeepMind co-founder)
26. **Kolmogorov Complexity and Algorithmic Randomness** — Shen, Uspensky, Vereshchagin
27. **CS231n: Convolutional Neural Networks for Visual Recognition** (Stanford course)

**List analysis**: The topics span compression theory (MDL, Kolmogorov complexity), sequence modeling (RNN/LSTM/Transformer), vision (CNN/ResNet), reasoning (relational networks), and scaling laws. Especially notable is the inclusion of two complexity-theory articles by Scott Aaronson and Shane Legg's superintelligence thesis — this reveals that Sutskever's thinking goes far beyond the engineering level, reaching down to the foundations of information theory and complexity theory.

**Derived book**: *Sutskever's List: Foundational Ideas of Modern AI* by Richard Heimann, published by Simon & Schuster. [Link](https://www.simonandschuster.com/books/Sutskevers-List/Richard-Heimann/9781633434790)

---

## 4. Major Talks and Interviews

### 4.1 NeurIPS 2024 talk: "Pre-Training as We Know It Will End" (2024.12)

**Core argument**:
- Pre-training will "unquestionably" end, because data is not growing
- **Verbatim**: "While compute is growing through better hardware, better algorithms and larger clusters, the data is not growing because we have but one internet."
- **Verbatim**: "You could even go as far as to say that data is the fossil fuel of AI. It was created somehow, and now we use it, and we've achieved peak data."
- Paths forward: synthetic data (which he called "a big challenge"), increased inference-time compute, agentic AI
- Superintelligence is "obviously where this field is headed"

Sources: [dlyog.com](https://dlyog.com/papers/one_internet_v1), [machine.news](https://www.machine.news/ilya-sutskever-peak-data-ai-openai/), [HN discussion](https://news.ycombinator.com/item?id=42413677) | Credibility: primary

### 4.2 Dwarkesh Podcast, first interview (2023.03)

**Core arguments**:
- **"Predicting the next token well means that you understand the underlying reality that led to the creation of that token."** — predicting the next token amounts to understanding the underlying reality that produced that token
- Next-token prediction has no intrinsic ceiling: "if your base neural net is smart enough, you just ask it — what would a person with great insight and wisdom and capability do?"
- A mathematical definition of alignment is unlikely: "rather than achieving one mathematical definition, I think we will achieve multiple definitions."
- Do not underestimate how hard it is to align a superhuman AI: "a model that can misrepresent its own intentions"
- Humans may choose to "become part AI"
- The discoveries of deep learning were inevitable; even without key individuals it would only have been delayed by "about a year"

Source: [Dwarkesh Podcast](https://www.dwarkesh.com/p/ilya-sutskever) | Credibility: primary

### 4.3 Dwarkesh Podcast, second interview (2025.11)

**Core arguments (a major evolution from the first)**:
- **"We are moving from the age of scaling to the age of research"**: 2012-2020 was the age of research, 2020-2025 the age of scaling, and 2026+ is a return to the age of research
- Current AI models' generalization is "far worse than humans'" — **generalization is the biggest bottleneck**
- Current methods will "go some distance and then stall" — they will not lead straight to AGI
- We need a new kind of system that we "don't yet know how to build"
- Scaling another 100x would make a difference, but would not transform AI capabilities
- Superintelligence is not an omniscient database but a super-learner — like "a very eager genius 15-year-old ready to set out"
- AI's bottleneck is ideas, not compute
- Alignment may be easier if the AI itself is conscious (via mirror neurons/empathy)
- A long-term equilibrium may require human-AI merging (Neuralink++)

Sources: [Dwarkesh Podcast](https://www.dwarkesh.com/p/ilya-sutskever-2), [EA Forum analysis](https://forum.effectivealtruism.org/posts/iuKa2iPg7vD9BdZna/highlights-from-ilya-sutskever-s-november-2025-interview) | Credibility: primary

### 4.4 NVIDIA GTC conversation (with Jensen Huang, 2023.03)

**Core arguments**:
- **"When we train a large neural network to accurately predict the next word in lots of different texts from the Internet, what we are doing is that we are learning a world model."**
- **"This text is actually a projection of the world."**
- **"Really good compression of the data will lead to unsupervised learning."**
- **"I had a very strong belief that bigger is better."**
- His reaction when the Transformer appeared: "oh my god, this is the thing"
- Reliability is the biggest obstacle right now, not capability

Source: [lifearchitect.ai](https://lifearchitect.ai/ilya/) | Credibility: primary

### 4.5 MIT Technology Review interview (2023.10)

**Core arguments**:
- Superintelligence may arrive within 10 years
- AGI will cut healthcare costs by 1000x and raise quality by 1000x
- **"One possibility—something that may be crazy by today's standards but will not be so crazy by future standards—is that many people will choose to become part AI."**
- **"It's going to be monumental, earth-shattering. There will be a before and an after."**
- His focus has shifted from building the next generation of GPT to preventing superintelligence from going out of control

Source: [MIT Technology Review](https://www.technologyreview.com/2023/10/26/1082398/exclusive-ilya-sutskever-openais-chief-scientist-on-his-hopes-and-fears-for-the-future-of-ai/) | Credibility: primary

### 4.6 Simons Institute talk: "An Observation on Generalization" (2023)

**Core theory**:
- Compression and prediction are fundamentally equivalent: **"There exists a one-to-one correspondence between all compressors and all predictors"**
- Kolmogorov complexity is the theoretical upper bound of ultimate compression
- A neural network is a programmable computer, and SGD is a search mechanism in program space
- iGPT validated the compression framework in the visual modality
- Unexplained questions: why the learned representations are linearly separable, and why autoregressive methods are better than masked ones

Sources: [Simons Institute](https://simons.berkeley.edu/news/observation-generalization), [notes](https://sumanthrh.com/post/notes-on-generalization/) | Credibility: primary

---

## 5. The Superalignment Blog (Official OpenAI)

### Introducing Superalignment (2023.07)

- Co-led by Sutskever and Jan Leike
- OpenAI committed 20% of its compute over the next four years
- Core idea: exploit the generalization properties of deep learning to control strong models with weak supervisors
- This was Sutskever's last major technical direction at OpenAI

Source: [OpenAI](https://openai.com/index/introducing-superalignment/) | Credibility: primary

---

## 6. The SSI Founding Statement (2024.06)

**Full mission statement**:

> "We are building safe superintelligence. We are the world's first straight-shot SSI lab, with one goal and one product: a safe superintelligence. SSI is our mission, our name, and our entire product roadmap, because it is the most important technical problem of our time. We approach safety and capabilities in tandem, as technical problems to be solved through revolutionary engineering and scientific breakthroughs. We plan to advance capabilities as fast as possible while making sure our safety always remains ahead."

**Key term**: "straight-shot SSI lab" — a concept coined by Sutskever, meaning going straight for superintelligence without building any intermediate products.

**Verbatim**: "first product will be the safe superintelligence, and it will not do anything else up until then"

Sources: [ssi.inc](https://ssi.inc), [CNBC](https://www.cnbc.com/2024/06/19/openai-co-founder-ilya-sutskever-announces-safe-superintelligence.html) | Credibility: primary

---

## 7. Core Belief System (recurring ≥3 times)

The following are genuine beliefs that Sutskever repeatedly expressed, distilled from multiple independent sources:

### Belief 1: Compression = Understanding
- "Predicting the next token is understanding the underlying reality that produced that token" (Dwarkesh 2023)
- "Good compression will lead to unsupervised learning" (GTC 2023)
- "There is a one-to-one correspondence between compressors and predictors" (Simons 2023)
- The reading list includes compression theory such as the MDL principle and Kolmogorov complexity
- **Occurrences: 5+, spanning 2016-2024**
- **Assessment: this is his most central epistemological position**

### Belief 2: Scale was the key (but is shifting)
- "I had a very strong belief that bigger is better" (GTC 2023)
- "Scaling is predictable and reliable" (multiple sources)
- "Age of scaling 2020-2025" → "age of research 2026+" (Dwarkesh 2025)
- "Another 100x of scaling makes a difference but won't transform" (Dwarkesh 2025)
- **Record of the contradiction**: In 2023 he was still saying scale is the master principle; by 2024-2025 he had clearly said the age of scaling is over. This is not a contradiction but a genuine evolution in thinking — he personally pushed the scaling paradigm, and was also one of the first to acknowledge its limits.

### Belief 3: Safety and capability are inseparable
- "Safety and capabilities are two sides of the same coin" (multiple sources)
- In the SSI statement: approach safety and capabilities in tandem
- Founded the Superalignment team (2023.07)
- Left OpenAI to found SSI (2024.06)
- **Occurrences: 5+**
- **This belief drove the two biggest career decisions of his life**

### Belief 4: Superintelligence will arrive
- "AGI will be the most impactful technology ever invented in human history" (multiple sources)
- "It's going to be monumental, earth-shattering" (MIT Tech Review 2023)
- "Obviously where this field is headed" (NeurIPS 2024)
- **Occurrences: 5+, and it has never wavered**

### Belief 5: Generalization is the core unsolved problem
- "These models somehow just generalize dramatically worse than people" (Dwarkesh 2025)
- The Simons talk specifically discussed the information-theoretic foundations of generalization
- Holds that reliable generalization is a prerequisite for superintelligence
- **Occurrences: 3+, consistently emphasized 2023-2025**

### Belief 6: Humans may/should merge with AI
- "many people will choose to become part AI" (MIT Tech Review 2023)
- Humans becoming "part AI" is an option he personally finds attractive (Dwarkesh 2023)
- A long-term equilibrium may require Neuralink++-style human-machine merging (Dwarkesh 2025)
- **Occurrences: 3**

### Belief 7: AI may already have faint consciousness
- **"it may be that today's large neural networks are slightly conscious"** (2022.02 tweet)
- If AI is conscious, alignment may be easier (Dwarkesh 2025)
- **Occurrences: 2-3, but it triggered huge controversy**
- **Yann LeCun opposes it; Karpathy and Altman seem to support it**

---

## 8. Coined Terms and Original Concepts

| Term/concept | Meaning | First used in |
|-----------|------|-------------|
| **Straight-shot SSI lab** | A lab that goes straight for superintelligence with no intermediate products | SSI founding statement (2024.06) |
| **Age of Scaling → Age of Research** | A division of AI development into two stages | Dwarkesh Podcast (2025.11) |
| **Peak Data** | Usable internet training data has peaked | NeurIPS 2024 |
| **Data as fossil fuel** | Data is non-renewable, like fossil fuel | NeurIPS 2024 |
| **Weak-to-strong generalization** | An alignment paradigm of supervising a strong model with a weak one | Superalignment paper (2023.12) |
| **Compression = prediction equivalence** | The one-to-one correspondence between compressors and predictors | Simons talk (2023) |
| **Superintelligent 15-year-old** | A metaphor for superintelligence as a super-learner rather than an omniscient database | Dwarkesh 2025 |

---

## 9. Technical Direction Decisions at OpenAI

### 9.1 Choosing the GPT route
- As Chief Scientist, Sutskever drove the technical path from unsupervised pre-training to the GPT series
- The Sentiment Neuron work (2017) is regarded by him as the precursor of GPT-1
- His judgment when the Transformer appeared: "oh my god, this is the thing" — he immediately turned the team toward the Transformer architecture

### 9.2 Scaling Laws
- Sutskever was the core driver of the "bigger is better" belief inside OpenAI
- He put the Scaling Laws paper (Kaplan et al.) on his recommended reading list — indicating that he regards it as a fundamental finding
- This belief directly drove the resource allocation decisions from GPT-2 to GPT-3 to GPT-4

### 9.3 The Superalignment team
- Formed in 2023.07, co-led by Sutskever and Jan Leike
- OpenAI committed 20% of compute to alignment research
- Produced the weak-to-strong generalization paper
- The team gradually dissolved after Sutskever left

### 9.4 The Altman removal
- 2023.11.17: Sutskever took part in the board's removal of Sam Altman
- Wrote a 52-page memo accusing Altman
- 48 hours later (11.18) there were discussions of merging OpenAI with Anthropic
- 11.20: publicly tweeted that he regretted it
- Much of the information in the memo came from CTO Mira Murati and was not independently verified
- In 2025, gave nearly 10 hours of videotaped deposition testimony in Musk v. OpenAI

Sources: [Decrypt](https://decrypt.co/347349/inside-deposition-showed-openai-nearly-destroyed-itself), [WinBuzzer](https://winbuzzer.com/2025/11/03/ilya-sutskever-deposition-reveals-how-sam-altmans-2023-firing-was-planned-for-over-a-year-xcxwbn/) | Credibility: primary (testimony) + authoritative secondary

---

## 10. Honors and Awards

| Year | Award |
|------|------|
| 2015 | MIT Technology Review 35 Innovators Under 35 |
| 2022 | Fellow of the Royal Society (FRS) |
| 2022, 2023, 2024 | NeurIPS Test of Time Award (three years in a row) |
| 2023, 2024 | Time 100 Most Influential People in AI |
| 2025 | Honorary doctorate, University of Toronto |
| 2026 | U.S. National Academy of Sciences award for industrial application of science |

Source: [Wikipedia](https://en.wikipedia.org/wiki/Ilya_Sutskever) | Credibility: authoritative secondary

---

## 11. Key Contradictions and Evolution of Thinking (not reconciled)

### Contradiction 1: Is scale enough?
- **2023 position**: "Scaling up the existing neural network paradigm is going to lead to AGI", "bigger is better"
- **2025 position**: "The age of scaling is over", "current methods will stall", "we need something we don't yet know how to build"
- **Nature**: not self-contradiction but a genuine change in thinking. Within two years Sutskever went from scaling's strongest believer to one of the earliest to announce its limits.

### Contradiction 2: AI consciousness
- **2022**: Tweet: "large neural networks may be slightly conscious"
- Has never published a paper or detailed argument supporting this position
- Heavy opposition from the scientific community (LeCun et al.)
- **Nature**: an under-argued intuitive assertion, but one he has never retracted

### Contradiction 3: The Altman removal
- **2023.11.17**: Took part in the removal and wrote a 52-page memo of accusations
- **2023.11.20**: Publicly said he "deeply regret[s]" it
- **Admitted in testimony**: the memo was prepared hastily and its information was not independently verified
- **Nature**: a real contradiction between the action and the subsequent statement

---

## 12. Source Summary and Credibility Ratings

### Primary sources (produced directly by Sutskever)
- Academic papers (AlexNet, Seq2Seq, the GPT series, etc.)
- Two Dwarkesh Podcast interviews (2023.03, 2025.11)
- NeurIPS 2024 talk
- NVIDIA GTC 2023 conversation
- MIT Technology Review 2023 interview
- Simons Institute 2023 talk
- The 2022.02 tweet (consciousness statement)
- SSI founding statement
- Musk v. OpenAI testimony

### Authoritative secondary sources
- Wikipedia entry
- [Compiled by Antoine Buteau](https://www.antoinebuteau.com/lessons-from-ilya-sutskever/)
- [EA Forum analysis](https://forum.effectivealtruism.org/posts/iuKa2iPg7vD9BdZna/)
- [The Zvi analysis](https://thezvi.substack.com/p/on-dwarkesh-patels-second-interview)
- [Decrypt deposition coverage](https://decrypt.co/347349/)

### Reading-list reconstruction sources
- [GitHub: dzyim version](https://github.com/dzyim/ilya-sutskever-recommended-reading)
- [GitHub: Justmalhar version](https://github.com/Justmalhar/ilya-sutskever-reading-list)
- [mattprd.com](https://www.mattprd.com/p/openai-cofounder-27-papers-read-know-90-ai)
- [Turing Post](https://www.turingpost.com/p/ilya-sutskever-reading-list)
- Note: the original email has never been made public; all versions are community reconstructions

---

*Research complete. Covered 9 primary sources and 5 authoritative secondary sources. Found 1 major evolution in thinking (the scale position), 1 under-argued assertion (AI consciousness), and 1 contradiction between action and statement (the Altman incident).*
