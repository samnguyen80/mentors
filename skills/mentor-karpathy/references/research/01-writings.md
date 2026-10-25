# Andrej Karpathy: Research on Writings and Core Arguments

> Research date: 2026-04-05
> Note on source types: primary = quoted directly from his own writing/video; secondary = others' paraphrase/summary; inferred = deduced from multiple contexts
> Blacklist: Zhihu, WeChat Official Accounts, Baidu Baike — none were used in this file

---

## 1. Basic Information and Career Trajectory

**Born**: October 23, 1986, in Bratislava, Slovakia; moved with his family to Toronto, Canada at age 15
**Education**:
- University of Toronto: Computer Science + Physics (double major), 2005-2009
- University of British Columbia: Master's in machine learning, 2009
- Stanford University: PhD, advisor Fei-Fei Li, graduated 2015, thesis titled *Connecting Images and Natural Language*

**Career trajectory (key points)**:
- 2015: Created CS231n (Stanford's first deep learning course, grew from 150 to 750 students)
- 2015-2017: Founding member and research scientist at OpenAI
- 2017-2022: Tesla's Director of AI (reporting to Elon Musk), led Autopilot
- July 2022: Left Tesla
- February 2023: Returned to OpenAI
- February 2024: Left OpenAI
- July 2024: Founded Eureka Labs (an AI-native education company)
- February 2026: Released microgpt (training a GPT in 200 lines of pure Python, zero dependencies)

Source: [Wikipedia](https://en.wikipedia.org/wiki/Andrej_Karpathy) (the primary information comes from his own website karpathy.ai)

---

## 2. Complete List of Blog Posts (karpathy.github.io)

| Date | Title | URL | Importance |
|------|------|-----|--------|
| 2026-02-12 | microgpt | karpathy.github.io/2026/02/12/microgpt/ | ⭐⭐⭐⭐⭐ latest major work |
| 2022-03-14 | Deep Neural Nets: 33 years ago and 33 years from now | karpathy.github.io/2022/03/14/lecun1989/ | ⭐⭐⭐⭐ |
| 2021-06-21 | A from-scratch tour of Bitcoin in Python | karpathy.github.io/2021/06/21/blockchain/ | ⭐⭐⭐ |
| 2021-03-27 | Short Story on AI: Forward Pass | karpathy.github.io/2021/03/27/forward-pass/ | ⭐⭐ |
| 2020-06-11 | Biohacking Lite | karpathy.github.io/2020/06/11/biohacking-lite/ | ⭐ |
| 2019-04-25 | A Recipe for Training Neural Networks | karpathy.github.io/2019/04/25/recipe/ | ⭐⭐⭐⭐⭐ practitioner's bible |
| 2018-01-20 | (started posting on Medium instead) | — | turning point |
| 2016-09-07 | A Survival Guide to a PhD | karpathy.github.io/2016/09/07/phd/ | ⭐⭐⭐⭐ |
| 2016-05-31 | Deep Reinforcement Learning: Pong from Pixels | karpathy.github.io/2016/05/31/rl/ | ⭐⭐⭐ |
| 2015-11-14 | Short Story on AI: A Cognitive Discontinuity | karpathy.github.io/2015/11/14/ai/ | ⭐⭐ |
| 2015-10-25 | What a Deep Neural Network thinks about your #selfie | karpathy.github.io/2015/10/25/selfie/ | ⭐⭐ |
| 2015-05-21 | The Unreasonable Effectiveness of Recurrent Neural Networks | karpathy.github.io/2015/05/21/rnn-effectiveness/ | ⭐⭐⭐⭐⭐ classic |
| 2015-03-30 | Breaking Linear Classifiers on ImageNet | karpathy.github.io/2015/03/30/breaking-convnets/ | ⭐⭐ |
| 2014-09-02 | What I learned from competing against a ConvNet on ImageNet | karpathy.github.io/2014/09/02/what-i-learned-from-competing-against-a-convnet-on-imagenet/ | ⭐⭐⭐ |
| 2014-08-03 | Quantifying Productivity | karpathy.github.io/2014/08/03/quantifying-productivity/ | ⭐ |
| 2014-07-03 | Feature Learning Escapades | karpathy.github.io/2014/07/03/feature-learning-escapades/ | ⭐⭐ |
| 2012-10-22 | The state of Computer Vision and AI: we are really, really far away | karpathy.github.io/2012/10/22/state-of-computer-vision/ | ⭐⭐⭐ |
| 2011-04-27 | Lessons learned from manually classifying CIFAR-10 | karpathy.github.io/2011/04/27/manually-classifying-cifar10/ | ⭐⭐ |

**Medium blog**: https://karpathy.medium.com/
Core article:
- [Software 2.0](https://karpathy.medium.com/software-2-0-a64152b37c35) (2017, his most widely cited article)

Source: crawled directly from the blog index page (primary)

---

## 3. In-Depth Analysis of the Core Blog Posts

### 3.1 Software 2.0 (2017, Medium)
**Source**: https://karpathy.medium.com/software-2-0-a64152b37c35 (primary)

**Core argument**:
> "Software 1.0 is the set of instructions humans write by hand in languages like Python/C++; Software 2.0 is the weights of a neural network — a program generated from data by an optimization algorithm."

**Software 1.0 vs 2.0 comparison**:
- SW1.0: the programmer identifies "desired-behavior points" in the problem space and hand-writes explicit rules
- SW2.0: given input-output pairs, an optimization algorithm searches "program space" for the best program (the network weights)

**Advantages of SW2.0** (Karpathy's own argument):
1. Computational homogeneity: every operation is a matrix multiplication, extremely friendly to hardware acceleration
2. Can learn knowledge that humans cannot articulate explicitly
3. Performance keeps improving with data and compute (predictable scaling effects)

**Disadvantages/risks of SW2.0** (Karpathy admits):
- Results are hard to interpret
- Fails silently (silent failure)
- May encode biases in the data

**Domains SW2.0 will eat**: visual recognition, speech processing, image translation, image captioning, game AI, database queries

**Tesla case**: as Autopilot evolved, C++ code was continually deleted and replaced by neural network weights — a concrete example of SW2.0 "eating" SW1.0.

---

### 3.2 The Unreasonable Effectiveness of RNNs (2015)
**Source**: karpathy.github.io/2015/05/21/rnn-effectiveness/ (primary)

**Core argument**:
> "If training vanilla neural nets is optimization over functions, training recurrent nets is optimization over programs."

**Key experiments** (demonstrating the generative ability of RNNs):
- Paul Graham essays: generating structured startup wisdom text
- Shakespeare: learning dialogue structure, speaker names, and complex syntax
- Wikipedia markdown: automatically discovering the wiki link format
- LaTeX math: generating nearly compilable mathematical proofs
- Linux kernel C code: generating functions with correct bracket nesting and variable declarations

**Technical insight**: about 5% of the RNN neurons spontaneously acquire interpretable algorithms (quote detection, URL boundaries, bracket counting) — with no explicit guidance.

---

### 3.3 A Recipe for Training Neural Networks (2019)
**Source**: karpathy.github.io/2019/04/25/recipe/ (primary)

**Core premises** (two key observations):
1. Neural network training is a "leaky abstraction" — it cannot be used as a plug-in; it requires deep understanding
2. Failure is silent — the network will train but perform poorly, with no obvious error message

**Six-stage process**:

**Stage 1: Become one with the data**
- Spend hours inspecting thousands of samples
- Understand distributions, patterns, imbalances, labeling noise

**Stage 2: End-to-end skeleton + baselines**
- Fix the random seed
- Turn off data augmentation
- Verify that the loss at initialization matches expectations
- Establish a human baseline
- Overfit a single batch to verify that the architecture is feasible

**Stage 3: Overfit**
- "Don't be a hero": copy a validated architecture, do not invent your own
- Adam + lr=3e-4 is the most forgiving starting point

**Stage 4: Regularize (ordered by effectiveness)**
1. Get more real data (the most effective)
2. Data augmentation
3. Pretraining
4. Dropout (spatial dropout for ConvNets)
5. weight decay, early stopping

**Stage 5: Tune**
- Random search beats grid search (it better captures differences in sensitivity across parameters)

**Stage 6: Squeeze out the juice**
- Model ensembles (a guaranteed ~2% improvement)
- Train longer than intuition suggests

**Meta-principle**:
> "A 'fast and furious' approach to training neural networks does not work. Success is correlated with patience and attention to detail."

---

### 3.4 Deep Neural Nets: 33 years ago and 33 years from now (2022)
**Source**: karpathy.github.io/2022/03/14/lecun1989/ (primary)

**Core argument**: At the macro level deep learning has barely changed in 33 years — it is still end-to-end optimization of differentiable neural networks with backpropagation. What has changed is scale.

**Orders-of-magnitude comparison**:
- Parameter count: about 1,000,000x
- Volume of pixel data processed: about 100,000,000x
- Training speed: 3,000x faster on consumer hardware (GPUs can add another 100x)

**Sources of the performance gain**:
- Modern optimization tricks (Adam, dropout, data augmentation): ~60% error reduction
- Larger datasets: moderate contribution
- Scale: requires more compute

**The 2055 prediction**:
> Future practitioners will not train models from scratch, but will talk in natural language to giant foundation models, telling the "10,000,000x neural network super-brain" what to do.

---

### 3.5 microgpt (February 2026)
**Source**: karpathy.github.io/2026/02/12/microgpt/, GitHub Gist (primary)

**Core claim**: Implement complete GPT training and inference in 200 lines of pure Python (zero dependencies, no PyTorch, no NumPy, no GPU acceleration) — the culmination of his "decade-long obsession with simplifying LLMs to their bare essentials".

**Contents**: a document dataset, tokenizer, autograd engine, GPT-2-like architecture, Adam optimizer, training loop, inference loop.

**Expression of belief**:
> "Everything else is just efficiency."

This is the latest practice of his "If I can't build it, I don't understand it" belief.

---

## 4. YouTube Teaching Video Series

### The Zero to Hero series (Neural Networks: Zero to Hero)
**Home page**: https://karpathy.ai/zero-to-hero.html (primary)
**GitHub repo**: https://github.com/karpathy/nn-zero-to-hero
**Started**: August 2022
**Philosophy**: language models are the best entry point for learning deep learning — even if the goal is computer vision, everything learned transfers.

| # | Title | Length | Core content |
|---|------|------|---------|
| 1 | The Spelled-Out Intro to Neural Networks and Backpropagation: Building Micrograd | 2h25m | Implement backpropagation from scratch, requiring only high-school calculus |
| 2 | The Spelled-Out Intro to Language Modeling: Building Makemore | 1h57m | A bigram character-level language model, an introduction to PyTorch |
| 3 | Building Makemore Part 2: MLP | 1h15m | Multilayer perceptron, the concepts of overfitting/underfitting |
| 4 | Building Makemore Part 3: Activations & Gradients, BatchNorm | 1h55m | Gradient flow analysis, batch normalization |
| 5 | Building Makemore Part 4: Becoming a Backprop Ninja | 1h56m | Manual backpropagation without autograd |
| 6 | Building Makemore Part 5: Building a WaveNet | 56m | Hierarchical convolutional network architecture |
| 7 | Let's Build GPT: From Scratch, in Code, Spelled Out | 1h56m | Build GPT from scratch, following "Attention is All You Need" |
| 8 | Let's Build the GPT Tokenizer | 2h13m | Implement a BPE tokenizer from scratch, how tokenization affects LLM behavior |

### Other important videos
- **[1hr Talk] Intro to Large Language Models** (November 2023): aimed at a general audience, covering LLM training, the LLM OS analogy, and safety (jailbreak/prompt injection)
- **Deep Dive into LLMs like ChatGPT** (February 2025, 3h31m): an in-depth walk through the full training stack, building a mental model
- **Let's reproduce GPT-2**: reproducing GPT-2 from scratch

---

## 5. Academic Papers (by citations/importance)

Source: dblp.org + Google Scholar entries (secondary; citation counts are approximate values at the time of search)

| Year | Title | Venue | Collaborators | Core contribution |
|------|------|---------|--------|---------|
| 2017 | Deep Visual-Semantic Alignments for Generating Image Descriptions | IEEE TPAMI | Li Fei-Fei | Multimodal alignment (image → natural-language description) |
| 2016 | **DenseCap**: Fully Convolutional Localization Networks for Dense Captioning | CVPR | Justin Johnson, Li Fei-Fei | The dense image captioning task |
| 2016 | Connecting Images and Natural Language (PhD thesis) | Stanford | — | PhD thesis summary |
| 2017 | PixelCNN++: Improving the PixelCNN with Discretized Logistic Mixture | ICLR | Tim Salimans et al. | Generative model improvements |
| 2017 | World of Bits: An Open-Domain Platform for Web-Based Agents | ICML | Tianlin Shi et al. | A web-agent benchmark (early agent research) |
| 2015 | ImageNet Large Scale Visual Recognition Challenge | IJCV | Russakovsky, Deng, Fei-Fei et al. | Defined the ImageNet benchmark |
| 2015 | Visualizing and Understanding Recurrent Networks | CoRR | Justin Johnson, Li Fei-Fei | RNN visualization and interpretation |
| 2015 | Deep visual-semantic alignments for generating image descriptions | CVPR | Li Fei-Fei | Early version of image captioning |
| 2014 | Grounded Compositional Semantics for Finding and Describing Images | TACL | Socher, Le, Manning, Ng | Compositional image-text semantics |
| 2014 | Large-Scale Video Classification with ConvNets | CVPR | Toderici, Li Fei-Fei et al. | Video understanding |
| 2014 | Deep Fragment Embeddings for Bidirectional Image Sentence Mapping | NIPS | Joulin, Li Fei-Fei | Bidirectional image-text embeddings |

**Note**: VGGNet (Very Deep ConvNets for Large-Scale Image Recognition) is the work of Simonyan & Zisserman; what Karpathy took part in was the ImageNet challenge paper, and he is not an author of VGGNet. (Correcting a common misattribution)

**The CS231n course**: created in 2015, Stanford's first deep learning course; the videos are free online, with over 800,000 total views (TIME magazine data).

---

## 6. The Complete Software 1.0 / 2.0 / 3.0 Framework

**Sources**: the 2017 Medium article + the 2025 YC AI Startup School talk (used together, both primary)

In the 2025 YC AI Startup School talk Karpathy extended the framework to three generations:

| Generation | Definition | Programming method | Representative platform |
|------|------|---------|---------|
| Software 1.0 | Explicit instructions humans write in traditional languages | Programmers write code | GitHub |
| Software 2.0 | The weights of a neural network, generated from data by an optimizer | Tune the dataset + run the optimizer | Hugging Face |
| Software 3.0 | LLMs, programmed with natural-language prompts | Write prompts in English | — |

Key assertions:
> "Prompts are now programs that program the LLM."
> "Software 3.0 is eating 1.0/2.0."
> "A huge amount of software will be rewritten."

**Tesla corroboration**: as Autopilot evolved, the neural network kept expanding and the C++ code kept being deleted — a real case of SW2.0 eating SW1.0.

---

## 7. The LLM OS Concept

**Sources**:
- X post, September 2023 (primary): https://x.com/karpathy/status/1707437820045062561
- X post, November 2023 (primary): https://x.com/karpathy/status/1723140519554105733
- 1hr Talk Intro to LLMs (November 2023 video) (primary)

**Core analogy**: an LLM is not a chatbot but the kernel process of a new operating system.

| Traditional OS | LLM OS |
|--------|--------|
| CPU | LLM (the processor) |
| RAM | Context window (working memory) |
| File system | Embedding database (vector retrieval) |
| System calls | Tool calls/API calls |
| Long-running programs | Agents |
| I/O devices | Multimodal input/output (vision, audio) |

---

## 8. Key Terms and Coined Concepts

### 8.1 Vibe Coding (February 2025)
**Source**: https://x.com/karpathy/status/1886192184808149383 (primary)

> "There's a new kind of coding I call 'vibe coding', where you fully give in to the vibes, embrace exponentials, and forget that the code even exists."

**Background**: posted February 6, 2025, mentioning coding by voice commands with Cursor Composer + Sonnet + SuperWhisper.

**Impact**: reported at 4.5 million views; Merriam-Webster listed it under "Slang & Trending" in March 2025; Collins English Dictionary named it its Word of the Year for 2025.

### 8.2 Jagged Intelligence
**Source**: https://x.com/karpathy/status/1882518317585650084 (primary) + 2025 LLM Year in Review (primary)

> "LLMs exhibit amusingly jagged performance characteristics: simultaneously a genius polymath and a confused and cognitively challenged grade schooler, seconds away from getting tricked by a jailbreak."

This is not a training defect but a structural consequence of the RLVR optimization mechanism: capability rises sharply in the specific domains RLVR trains on, forming an uneven capability terrain.

### 8.3 LLMs as "Summoned Ghosts"
**Source**: 2025 LLM Year in Review (primary)

> "LLMs are not evolved animals but summoned ghosts—entities optimized under entirely different constraints than biological intelligence."

The argument: an LLM's neural architecture, training data, training algorithm, and optimization pressure are entirely different from biological intelligence, so they should not be understood from an "animal evolution" perspective, but as "a brand-new type of entity in the space of intelligence".

### 8.4 LLMs' "Anterograde Amnesia"
**Source**: YC AI Startup School 2025 talk (primary)

Compares the LLM to the protagonist of the film *Memento*: lacking the ability to consolidate long-term memory, relying only on the context window.

---

## 9. The Eureka Labs Mission Statement

**Source**: https://eurekalabs.ai/ (primary), published July 16, 2024

**Mission**: build a new kind of AI-native school.

**Core belief**:
> "Subject matter experts who are deeply passionate, great at teaching, infinitely patient and fluent in all languages are very scarce and cannot personally tutor all 8 billion people on demand."

**Solution**: a collaborative Teacher + AI Teaching Assistant model — the teacher designs the course, and the AI assistant is optimized as a tool to guide students through their learning, supporting, leveraging, and scaling the teacher's abilities.

**Vision**:
> "If we are successful, it will be easy for anyone to learn anything, expanding education in both reach (a large number of people learning something) and extent (any one person learning a large amount of subjects, beyond what may be possible today unassisted)."

**First product**: LLM101n: Let's Build A Storyteller (an undergraduate-level course in which students train their own AI)

---

## 10. Learning Philosophy

Sources: Twitter/X posts + the Stanford advice page (primary)

### Core tenet 1: Learning should not be fun
> "Learning is not supposed to be fun. It doesn't have to be actively not fun either, but the primary feeling should be that of effort."

### Core tenet 2: Against the "shortification of learning"
**Source**: https://x.com/karpathy/status/1756380066580455557 (primary, February 2024)

> "There are a lot of videos on YouTube/TikTok etc. that give the appearance of education, but if you look closely they are really just entertainment."

The prescription: close those quick-take tabs and "seek the meal" — textbooks, documentation, papers, manuals, long-form pieces. Allocate a 4-hour window to read, take notes, reread, restate, process, and manipulate the material.

### Core tenet 3: Build to understand
> "If I can't build it, I don't understand it."

This tenet runs through micrograd, makemore, nanoGPT, and microgpt — each time "building by hand from scratch" to prove real understanding.

### Core tenet 4: Read primary sources
His recommended LLM reading list includes reading the original papers directly (Attention is All You Need, GPT-2, InstructGPT, etc.) rather than secondhand interpretations.

---

## 11. Core Views from the Dwarkesh Patel Podcast

**Source**: https://www.dwarkesh.com/p/andrej-karpathy (secondary compilation; the primary is the original podcast)

**AGI timeline**: still 10 years away (not imminent); the problems are solvable but still hard.

**Critique of reinforcement learning** (a counterintuitive view!):
> "Reinforcement learning is terrible."

The argument: outcome-based reward is "sucking supervision through a straw" — compressing a lot of trajectory information into a single reward signal and propagating noise through the entire learning process. Humans do not mainly learn through RL, but through reflection, synthetic data generation (thinking), and distillation during sleep.

**The model collapse problem**: synthetic data generation fails because the model produces a "collapsed" distribution, and repeated self-sampling dangerously narrows diversity. Training a model on content it generated lowers performance, and maintaining entropy requires an external source of entropy (human interaction, diverse experience).

**The Cognitive Core vision**: future systems will separate knowledge from cognition — a "cognitive core" of about 1 billion parameters, stripped of encyclopedic memory but keeping the reasoning algorithm, looking things up when knowledge is needed, like a human.

**The computing-continuity view**: Karpathy rejects a sharp distinction between "AI and ordinary computer science". He believes progress is evolutionary: "we are abstracting ourselves away very, very slowly", like compilers replacing assembly. AGI may appear as continuous improvement rather than a discontinuous leap.

---

## 12. Recurring Core Arguments (true beliefs appearing ≥3 times)

The following are core positions expressed repeatedly across multiple settings, ordered by number of confirmations:

### Argument 1: Building from scratch is the only path to understanding ★★★★★
**Where it appears**: micrograd (video + code), the makemore series, nanoGPT, the microgpt post, the design philosophy of the LLM101n course, PhD advice
**Signature expression**:
> "If I can't build it, I don't understand it."

### Argument 2: Neural network training "fails silently", demanding extreme caution and visualization ★★★★★
**Where it appears**: Recipe for Training NNs (2019), the Zero to Hero course, CS231n materials
**Signature expression**:
> "Neural net training is a leaky abstraction."
> "A 'fast and furious' approach does not work."

### Argument 3: Software is undergoing a fundamental paradigm shift (SW1.0→2.0→3.0) ★★★★★
**Where it appears**: Software 2.0 (2017), 1hr Intro to LLMs (2023), YC Startup School (2025), X posts (multiple)
**Signature expression**:
> "Software 2.0 will eat through Software 1.0."
> "A huge amount of software will be rewritten."

### Argument 4: LLMs are a new kind of computing infrastructure, not a tool ★★★★
**Where it appears**: the LLM OS posts (2023), the 1hr Talk (2023), the YC talk (2025), 2025 LLM Year in Review
**Signature expression**: the LLM is the OS kernel; the context window is RAM; the Memento analogy.

### Argument 5: LLMs are an entirely new kind of entity that cannot be understood through biological/human frameworks ★★★★
**Where it appears**: 2025 LLM Year in Review, the "summoned ghosts" posts (multiple), short-story articles
**Signature expression**:
> "LLMs are not evolved animals but summoned ghosts."
> "Jagged Intelligence"

### Argument 6: AI education needs to be democratized — anyone should be able to learn from the best content ★★★★
**Where it appears**: CS231n open and free, the Zero to Hero series (free), the Eureka Labs mission statement, LLM101n open-sourced
**Signature expression**:
> "If we are successful, it will be easy for anyone to learn anything."

### Argument 7: The essence of deep learning has not changed in 33 years; only scale has changed ★★★
**Where it appears**: 33 years ago and 33 years from now (2022), the Lex Fridman podcast, multiple interviews
**Signature expression**:
> "Not much has changed in 33 years on the macro level."

### Argument 8: Data quality and quantity are SW2.0's core competitive advantage (beyond architectural innovation) ★★★
**Where it appears**: descriptions of the Tesla Data Engine, Recipe for Training NNs ("get more real data is the most effective regularizer"), the Zero to Hero course
**Signature expression**: among regularization methods, "Get more real data" ranks first.

---

## 13. Recommended Reading/Resources (revealing the intellectual lineage)

### Must-read papers (Karpathy's recommended LLM starter list)
Source: karpathy.ai LLM reading list (primary)

1. Attention is All You Need (the original Transformer paper)
2. Language Models are Unsupervised Multitask Learners (the GPT-2 paper)
3. Training Language Models to Follow Instructions (InstructGPT)
4. Llama 2: Open Foundation and Fine-Tuned Chat Models
5. RLAIF: Scaling Reinforcement Learning from Human Feedback with AI
6. Training Compute Optimal Language Models (Chinchilla)
7. Sparks of Artificial General Intelligence: Early Experiments with GPT-4

### Recommended learning resources
- The CS231n notes (written by him)
- The *Deep Learning* textbook (Goodfellow et al.)
- *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (recommended for beginners)
- Read the original papers directly; don't rely only on secondhand interpretations

**Inferred intellectual lineage (inferred)**:
- Identification with Feynman-style teaching ("build from scratch" = "if you can teach it to someone else, you understand it")
- Deep familiarity with LeCun's work (the 33-years-ago post directly reproduces LeCun's 1989 paper)
- Personal correspondence with Bahdanau (inventor of the attention mechanism) (he published the private email exchange, with consent)

---

## 14. Known Contradictions and Tensions (not reconciled, recorded directly)

**Contradiction 1: Criticism of RL vs. praise of RLVR**
- On the Dwarkesh podcast: said "Reinforcement learning is terrible", criticizing outcome-based reward
- In 2025 LLM Year in Review: called RLVR (Reinforcement Learning from Verifiable Rewards) the most important training-paradigm shift of 2025, praising it highly

Possible reconciliation: what he criticizes is traditional RL with sparse reward (such as policy gradient), and what he praises is RLVR with verifiable rewards. But the distinction is not always clear in the original text.

**Contradiction 2: Modest prediction vs. bold vision**
- "AGI still a decade away" (a modest 10-year timeline)
- Yet also describes a future education revolution where "anyone can learn anything" and "a huge amount of software will be rewritten"

This is not necessarily a contradiction, but there is tension: his predictions are relatively conservative, yet his actions (founding Eureka Labs, betting on SW3.0) assume that transformation is imminent.

**Contradiction 3: Opposing the "shortification of learning" vs. producing lots of explanatory videos himself**
He criticizes content on YouTube that gives the feeling of learning but is really entertainment, yet his own Zero to Hero series is itself YouTube video.
A possible distinction: his videos demand a great deal of cognitive investment (2+ hours, requiring hands-on work), the kind that "requires effort" in his definition.

---

## 15. Source Index

| Source | URL | Credibility |
|------|-----|--------|
| Personal blog (karpathy.github.io) | http://karpathy.github.io/ | Primary |
| Medium blog | https://karpathy.medium.com/ | Primary |
| Personal website | https://karpathy.ai/ | Primary |
| Zero to Hero course page | https://karpathy.ai/zero-to-hero.html | Primary |
| X account | https://x.com/karpathy | Primary |
| Eureka Labs website | https://eurekalabs.ai/ | Primary |
| bearblog annual review | https://karpathy.bearblog.dev/ | Primary |
| dblp paper list | https://dblp.org/pid/04/9925.html | Primary (bibliographic database) |
| Google Scholar | https://scholar.google.com/citations?user=l8WuQJgAAAAJ | Primary (bibliographic database) |
| YC Startup School talk summary | https://www.latent.space/p/s3 | Secondary (with full transcript) |
| Dwarkesh podcast | https://www.dwarkesh.com/p/andrej-karpathy | Secondary (with full conversation) |
| Wikipedia biography | https://en.wikipedia.org/wiki/Andrej_Karpathy | Secondary (comprehensively credible) |
| Stanford personal page | https://cs.stanford.edu/people/karpathy/ | Primary |
| vibe coding wiki | https://en.wikipedia.org/wiki/Vibe_coding | Secondary (supplementary confirmation) |
