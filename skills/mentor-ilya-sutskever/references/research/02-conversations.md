# Ilya Sutskever — Research on Conversations, Podcasts, and In-Depth Interviews

> Research date: 2026-04-05
> Research goal: Collect primary-source records of Ilya Sutskever's conversations, and extract his thinking patterns, expression DNA, and ways of handling uncertainty

---

## List of Primary Sources

| # | Source | Date | Type | Importance |
|---|------|------|------|----------|
| 1 | Lex Fridman Podcast #94 | 2020-05 | Podcast (1.5h) | ⭐⭐⭐ |
| 2 | NVIDIA GTC — Jensen Huang Fireside Chat | 2023-03-23 | Conference conversation | ⭐⭐⭐⭐ |
| 3 | Dwarkesh Patel Podcast #1 — Building AGI | 2023-03-27 | Podcast (1h) | ⭐⭐⭐⭐ |
| 4 | Scale AI TransformX — What's Next for AI | 2023 | Conference talk | ⭐⭐⭐ |
| 5 | TED AI — The Exciting, Perilous Journey Toward AGI | 2023-10-17 | TED talk | ⭐⭐⭐⭐ |
| 6 | MIT Technology Review exclusive interview | 2023-10-26 | In-depth interview | ⭐⭐⭐⭐ |
| 7 | X/Twitter public statement (after the Board Drama) | 2023-11-20 | Social media | ⭐⭐⭐⭐⭐ |
| 8 | OpenAI departure statement | 2024-05 | Public statement | ⭐⭐⭐ |
| 9 | SSI founding announcement | 2024-06-19 | Public statement | ⭐⭐⭐⭐ |
| 10 | NeurIPS 2024 — Sequence to Sequence: What a Decade | 2024-12 | Academic talk | ⭐⭐⭐⭐⭐ |
| 11 | Musk v. OpenAI sworn deposition | 2025-10-01 | Legal testimony (10h) | ⭐⭐⭐⭐⭐ |
| 12 | Dwarkesh Patel Podcast #2 — Age of Research | 2025-11-25 | Podcast (1.5h) | ⭐⭐⭐⭐⭐ |

---

## 1. Lex Fridman Podcast #94 (2020)

**Source**: https://lexfridman.com/ilya-sutskever/
**Type**: Primary (full podcast recording + transcript)

### Core quotes

**On his belief in deep learning**:
> "I think that we are still massively underestimating deep learning."

**On his early intuition about scaling**:
> "Let's make a big neural network, let's train it, and it's going to work much better than anything before it, and it will, in fact, continue to get better as I make it larger. And it turns out to be true."

**On the essence of neural networks**:
> "The neural network is really about learning. Its entire being is about learning representations."

> "A small neural network is a little dumb. A big neural network is a little smart."

### Topics discussed
- The AlexNet paper and the ImageNet moment
- Recurrent neural networks, backpropagation
- GPT-2 and language models
- Whether neural networks can be made to reason
- How to build AGI

---

## 2. Jensen Huang Fireside Chat — NVIDIA GTC (2023-03)

**Source**: https://blogs.nvidia.com/blog/sutskever-openai-gtc/ / https://www.nvidia.com/en-us/on-demand/session/gtcspring23-s52092/
**Type**: Primary (video + partial transcript)

### Core quotes

**On predicting the next token being understanding the world (the detective-novel analogy)**:
> "Say you read a detective novel. It's like a complicated plot, a storyline, different characters, lots of events. Mysteries, like clues, it's unclear. Then, let's say that at the last page of the book, the detective has gathered all the clues, gathered all the people, and saying, Okay, I'm going to reveal the identity of whoever committed the crime. And that person's name is — now predict that word."

Preface introducing the analogy:
> "[I will] give an analogy that will hopefully clarify why more accurate prediction of the next word leads to more understanding — real understanding."

**On the two stages of training**:
> "What the neural net learns is some representation of the process that produced the text, and that's a projection of the world." (first stage)

> "[The second stage] is where the fine tuning and the reinforcement learning from human teachers...we are teaching it. We are communicating with it. We are communicating to it. What it is that we want it to be." (second stage)

**On reliability being the frontier**:
> "We'll keep seeing systems that astound us with what they can do. The frontier is in reliability, getting to a point where we can trust what it can do, and that if it doesn't know something, it says so."

**On his firm belief in scaling (as of 2023)**:
> "I had a very strong belief that bigger is better, and a goal at OpenAI was to scale."

**On reasoning ability**:
> "The term is hard to define and the capability may still be on the horizon."

**On the relationship between GPUs and deep learning**:
> "The ImageNet dataset and a convolutional neural network were a great fit for GPUs that made it unbelievably fast to train something unprecedented."

**On human exposure to language**:
> "Humans hear a billion words in a lifetime."

### Analytical note
This is one of Ilya's most classic public conversations. The detective-novel analogy became his most widely cited explanation — using a story to let people intuitively grasp why "predicting the next token" is not the same as a "stochastic parrot". Note that in 2023 he still firmly believed in scaling.

---

## 3. Dwarkesh Patel Podcast #1 (2023-03)

**Source**: https://www.dwarkesh.com/p/ilya-sutskever
**Type**: Primary (full podcast + transcript)

### Core quotes

**On whether next-token prediction can surpass humans**:
> "I challenge the claim that next-token prediction cannot surpass human performance."

> "If your base neural net is smart enough, you just ask it — What would a person with great insight do?"

> "Predicting the next token well means that you understand the underlying reality that led to the creation of that token. It's not statistics."

**On the AGI timeline (explicit hesitation)**:
> "It's hard to give a precise answer and it's definitely going to be a good multi-year window."

> "I hesitate to give you a number."

**On the difficulty of alignment**:
> "I would not underestimate the difficulty of alignment of models that are actually smarter than us."

> "It depends on how capable the model is. The more capable the model, the more confident we need to be."

**On the current paradigm**:
> "This paradigm is gonna go really, really far and I would not underestimate it."

**On data (the 2023 assessment)**:
> "The data situation is still quite good. There's still lots to go. But at some point the data will run out."

**On the Microsoft partnership**:
> "Microsoft has been a very, very good partner for us. They've really helped take Azure to a point where it's really good for ML."

### How he handles uncertainty
Note his reaction when asked about the AGI timeline — "I hesitate to give you a number" is his typical way of handling it: **acknowledge that the question is important, but explicitly decline to give a specific number that could mislead**. He does not dodge the question itself; he dodges irresponsible precision.

---

## 4. Scale AI TransformX (2023)

**Source**: https://exchange.scale.com/public/videos/whats-next-for-ai-systems-and-language-models-with-ilya-sutskever-of-openai
**Type**: Primary (video + blog summary)

### Core quotes

**On compute efficiency**:
> "We are nowhere close to being as efficient as we can be with our compute."

**On the principle of the "sentiment neuron"**:
> "If you predict the next character well enough, you will eventually start to discover the semantic properties of the text."

**On ethical responsibility**:
> "People should also work on methods to try to address the problems that exist with the technology, such as bias and desirable outputs."

> "Whenever possible, they should work on reducing real harms."

**On future progress**:
> "Mundane progress we've seen over the past few years will continue."

---

## 5. TED AI Talk (2023-10-17)

**Source**: https://www.ted.com/talks/ilya_sutskever_the_exciting_perilous_journey_toward_agi
**Type**: Primary (video + transcript)

### Core quotes

**On the essential definition of AI**:
> "Artificial intelligence is nothing but digital brains inside large computers."

**On the impact of AGI**:
> "AGI will have dramatic and incredible impact on every single area of human activity."

> "The day will come when the digital brains will become as good and even better than our biological brains."

**On safety risks**:
> "For every positive application of AGI, there will be a negative application as well."

> "Maybe it will want to go rogue, being that it is an agent."

**On self-awareness (a highly characteristic formulation)**:
> "I am me and I am experiencing things. That when I look at things, I see them."

**On unprecedented cooperation (the core optimistic argument)**:
> "People will start to act in an unprecedentedly collaborative way out of their own self-interest."

> "Companies that are competitors will share technical information to make their AI safe."

### Analytical note
This TED talk is Ilya's most public, mass-audience appearance. Note how he phrases safety — he does not say "AI will definitely go out of control", but "maybe it will want to go rogue". His optimism rests on a very particular argument: **safety will not be achieved through moral appeals, but through cooperation driven by self-interest**.

---

## 6. MIT Technology Review Exclusive Interview (2023-10-26)

**Source**: https://www.technologyreview.com/2023/10/26/1082398/exclusive-ilya-sutskever-openais-chief-scientist-on-his-hopes-and-fears-for-the-future-of-ai/
**Type**: Primary (in-depth interview article)
**Note**: The original is paywalled; the quotes below come from multiple secondary analyses

### Confirmed core views

**On consciousness**:
In the interview he hinted that ChatGPT "may have a little consciousness" (if you squint), and that in the future some humans will choose to merge with machines. This echoes his tweet from February 2022:

> "it may be that today's large neural networks are slightly conscious" (2022-02-09, X/Twitter)

**On the certainty of AGI**:
> "At some point we really will have AGI."

**On the shift toward safety**:
The interview reveals how his fear changed the focus of his life's work — from pursuing capability to pursuing safety.

### Reactions to the "slightly conscious" tweet
This tweet triggered huge controversy:
- Yann LeCun rebutted directly: "Nope. Not even for true for small values of 'slightly conscious' and large values of 'large neural nets'."
- Melanie Mitchell, Emily Bender, and others responded with ridicule
- Sutskever offered no evidence or further explanation, which itself reflects his communication style — **throw out a provocative intuition, do not defend it**

---

## 7. OpenAI Board Drama — Public Statements (2023-11)

**Type**: Primary (X/Twitter post + legal testimony)

### The only public statement (2023-11-20)

> "I deeply regret my participation in the board's actions. I never intended to harm OpenAI. I love everything we've built together and I will do everything I can to reunite the company."

**Source**: https://x.com/ilyasut/status/1726590052392956028

### Musk v. OpenAI sworn deposition (2025-10-01) — detailed disclosures

**Source**: Reported by multiple outlets (Calcalist/Ctech, Decrypt, The Information)
**Type**: Primary (legal testimony, about 10 hours)

**On the accusations against Altman (in the written memo)**:
> "Sam exhibits a consistent pattern of lying, undermining his execs, and pitting his executives against one another."

**On his motive**:
> "I wanted them to become aware of it. But my opinion was that action was appropriate."

**On how long he had been planning to fire Altman**:
Asked how long he had considered firing Altman, he answered:
> "At least a year."

Asked what condition he was waiting for:
> "That the majority of the board is not obviously friendly with Sam."

**On employee reactions (unexpected)**:
> "I had not expected them to cheer, but I had not expected them to feel strongly either way."

**On the Anthropic merger proposal (strongly opposed)**:
> "I really did not want OpenAI to merge with Anthropic. I just didn't want to."

**Reflection on the board process**:
> "One thing I can say is that the process was rushed. I think it was rushed because the board was inexperienced."

**On the reason for leaving OpenAI**:
> "Ultimately, I had a big new vision. And it felt more suitable for a new company."

When pressed on SSI's research direction, he **declined to provide more detail**.

### Analytical note
These are the most "human" moments in Ilya's public record. Several points to note:
1. **He posted only one tweet** and then ended all public comment on the board drama — extreme restraint
2. The information revealed in the legal testimony far exceeds that in any of his public interviews — showing that his "silence" in public is deliberate
3. "I had not expected them to feel strongly either way" shows that he badly misjudged the organizational dynamics
4. His regret is not about the judgment of Altman, but about the execution process

---

## 8. SSI Founding Announcement (2024-06-19)

**Source**: https://ssi.inc / https://x.com/ilyasut/status/1803472978753303014
**Type**: Primary

### Core statements

> "We will pursue safe superintelligence in a straight shot, with one focus, one goal, and one product."

> "SSI is our mission, our name, and our entire product roadmap, because it is our sole focus."

> "We approach safety and capabilities in tandem, as technical problems to be solved through revolutionary engineering and scientific breakthroughs."

> "We plan to advance capabilities as fast as possible while making sure our safety always remains ahead."

> "Our singular focus means no distraction by management overhead or product cycles, and our business model means safety, security, and progress are all insulated from short-term commercial pressures."

### Analytical note
The text of the SSI announcement is highly polished — every word has been weighed. The core message is **redefining safety and capability as one technical problem**, rather than two dimensions that constrain each other. This is Ilya's direct response to the "safety vs commercialization" tension at OpenAI.

---

## 9. NeurIPS 2024 — Sequence to Sequence: What a Decade

**Source**: NeurIPS 2024 Test of Time Award talk (video available on YouTube)
**Type**: Primary
**Background**: Ilya returned to an academic conference to accept the award and give a talk; this was his first major public appearance after leaving OpenAI

### Core quotes

**On the end of pre-training**:
> "Pre-training as we know it will unquestionably end."

**On data being a finite resource**:
> "While compute is growing through better hardware, better algorithms and larger clusters, the data is not growing because we have but one internet."

**Data as fossil fuel (an important analogy)**:
> "You could even go as far as to say that data is the fossil fuel of AI. It was created somehow, and now we use it, and we've achieved peak data — and there'll be no more. So we have to deal with the data that we have."

**On superintelligence — a typical Ilya-style expression**:
> "This is obviously what's being built here."

Characteristics of superintelligence:
> "Agentic, reasons, understands and is self-aware."

**On time and manner (the most Ilya sentence)**:
> "I'm not saying how... and I'm not saying when. I'm saying that it will."

### Analytical note
This talk condenses Ilya's core thinking traits:
1. **The "peak data" analogy with fossil fuel** — he excels at explaining technical trends with everyday concepts
2. **"I'm not saying how, I'm not saying when, I'm saying that it will"** — his signature way of handling uncertainty: **extremely certain about direction, open about the path**
3. This is the moment he publicly "changed position" — from the scaling believer of 2023 to declaring the end of the pre-training era in 2024

---

## 10. Dwarkesh Patel Podcast #2 (2025-11-25)

**Source**: https://www.dwarkesh.com/p/ilya-sutskever-2
**Type**: Primary (full podcast + transcript)
**Importance**: Highest — this is the most in-depth public conversation Ilya has had since leaving OpenAI

### Core quotes

**On the division of AI development into stages**:
> "2012 to 2020 was an age of research, 2020 to 2025 was an age of scaling, and 2026 onward will be another age of research."

**On the limits of scaling (a position change!)**:
> "I don't think that's true at all." (asked whether another 100x would transform AI)

Later clarified on X:
> "Scaling the current thing will keep leading to improvements. In particular, it won't stall. But something important will continue to be missing."

**On the finiteness of data**:
> "The data is very clearly finite."

> "We're back to the age of research again, just with big computers."

**A fundamental critique of generalization**:
> "These models somehow just generalize dramatically worse than people. It's a very fundamental thing."

> "The thing which I think is the most fundamental is that these models somehow just generalize dramatically worse than people."

**On the disconnect between benchmarks and reality**:
> "How can the model, on the one hand, do these amazing things, and then on the other hand, repeat itself twice?"

> "This disconnect between eval performance and actual real-world performance, which is something that we don't today even understand."

**On the efficiency problem of RL**:
> "RL provides a relatively small amount of learning for the compute it uses."

**On SSI's positioning**:
> "We are squarely an 'age of research' company."

> "The main thing that distinguishes SSI is its technical approach."

> "Right now, we just focus on the research, and then the answer to that question will reveal itself."

**On the state of the AI industry**:
> "There are more companies than ideas by quite a bit."

**On research taste (highly personal)**:
> "There's no room for ugliness."

> "It's beauty, simplicity, elegance, correct biological inspiration. All of those things need to be present at the same time."

**On safety and superintelligence**:
> "What is the concern of superintelligence? If you imagine a system that is sufficiently powerful...we might not like the results."

> "It should be something like...care for sentient life, care for people, democratic, one of those, some combination thereof."

**On the AGI timeline**:
> "I think like 5 to 20." (years, when asked when a human-level learning system would appear)

**On the missing principle — declining to answer**:
> "There is a machine learning principle that I have opinions on. But unfortunately, circumstances make it hard to discuss in detail."

> "You know, that is a great question to ask, and it's a question I have a lot of opinions on. But unfortunately, we live in a world where not all machine learning ideas are discussed freely, and this is one of them."

**On emotion and value functions**:
He holds that the function of emotion resembles "value functions" — a mechanism that signals success/failure.

**On the source of human generalization**:
He speculates that "neurons use more compute than we think" — that is, the computational complexity of biological neurons is underestimated.

### Observer commentary
External observers noted: "the negative space in his answers — the things he refused to say — paints a clear picture of where he thinks the industry is wrong, and what SSI is likely building."

### Analytical note
This is the single most important source for understanding Ilya. Key findings:

**Position change**:
- 2023: "This paradigm is gonna go really, really far"
- 2025: "I don't think that's true at all" (on whether 100x scaling can transform AI)
- But he is not negating scaling; he is saying "something important will continue to be missing"

**The pattern of declining to answer**:
What he refuses to discuss is exactly what he considers most important. "Unfortunately, circumstances make it hard to discuss in detail" is his standard refusal formula. It does not say "I don't know" but "I know but cannot say".

**Research aesthetics**:
"There's no room for ugliness" is one of his most personal expressions. He equates scientific research with an aesthetic activity — good research must be not only correct but also elegant.

---

## 11. Other Important Quotes (by topic)

### On the world model in neural networks
> "When we train a large neural network to accurately predict the next word in lots of different texts from the Internet, what we are doing is that we are learning a world model." (GTC 2023)

> "These models are not just memorizing the internet... a model that just memorized the internet would be useless."

> "My perspective has been for a long time that everything is a neural net. The brain is a neural net. The mind is a neural net."

### On the certainty of AGI
> "It is abundantly clear that just scaling up the existing neural network paradigm is going to lead to AGI." (Note: a 2023 view)

> "AGI, if it's created, will be the most impactful technology ever invented in human history."

> "It's hard to communicate the visceral sense of what's coming."

> "It is important to appreciate that AGI is not just another piece of technology... it's a thing that can think."

> "There is a non-trivial chance that AGI will be achieved in the next 10 years."

### On safety
> "Superintelligence is a technology that could end human history. We should treat it with the seriousness it deserves."

> "If you build a very powerful AI, you need to be sure it will do what you want it to do."

> "It's not enough to say 'let's not build it.' Someone will build it. We need to figure out how to build it safely."

> "The problem is that a superintelligence, by its very nature, will be very good at achieving its goals."

### On discovery and research
> "When you get a glimmer of a really big discovery, you should follow it. Don't be afraid to be obsessed."

> "The most important discoveries are often the ones that seem obvious in retrospect."

> "Simplicity is a sign of truth. If your theory is very complicated, it's probably wrong."

> "The ideas are out there, floating in idea-space, and we just need to discover them."

> "You need to have a very deep belief that what you are doing is important."

> "It is important to have a taste for what is a good research direction."

### On Hinton
> "Thanks to working with Geoff, I had the opportunity to work on some of the most important scientific problems of our time and pursue ideas that were both highly unappreciated by most scientists, yet turned out to be utterly correct."

---

## 12. Communication Style Analysis

### How he expresses uncertainty
| Pattern | Example | Meaning |
|------|------|------|
| Hesitating to give a number | "I hesitate to give you a number" | Considers the question important but thinks a number would mislead |
| Direction certain / path open | "I'm not saying how, I'm not saying when. I'm saying that it will." | Intuitively certain about the destination, honestly uncertain about the path |
| Explicitly stating uncertainty | "I'm actually not sure if my statement about Intel is correct" | Willing to admit on the spot that his memory is inexact |
| Probabilistic expression | "maybe I believed them only 50% on the inside" | Quantifies his own belief when looking back |
| Explicit hedge | "I'll hedge a little bit" | Explicitly flags that he is hedging |

### How he declines questions
| Pattern | Example | Analysis |
|------|------|------|
| Competitive secrecy | "Unfortunately, circumstances make it hard to discuss in detail" | Standard formula — acknowledges there is an answer, but declines on competitive grounds |
| Affirm but don't answer | "That is a great question to ask, and it's a question I have a lot of opinions on. But..." | Affirms the quality of the question first, then declines |
| Silence | Posted only one tweet after the Board Drama | The most extreme refusal — not taking part in public discussion at all |

### Speaking rhythm
Observers describe:
- "He doesn't give a lot of interviews"
- "He is deliberate and methodical when he talks"
- "Long pauses when he thinks about what he wants to say and how to say it"
- Clear thinking pauses before answering, with no filler

### Analogies and ways of explaining
| Analogy | Topic | Source |
|------|------|------|
| Detective novel | Predicting the next token = understanding the world | GTC 2023 |
| Fossil fuel | Data is a finite resource | NeurIPS 2024 |
| Digital brains | The essence of AI | TED 2023 |
| Value function | The function of emotion | Dwarkesh 2025 |

### Key moments of position change

| Time | Position | Quote |
|------|------|------|
| 2023-03 | Scaling will go very far | "This paradigm is gonna go really, really far" |
| 2023-03 | Data is still sufficient | "The data situation is still quite good" |
| 2024-12 | Pre-training will end | "Pre-training as we know it will unquestionably end" |
| 2024-12 | Peak data reached | "We've achieved peak data — and there'll be no more" |
| 2025-11 | 100x scaling is not enough | "I don't think that's true at all" |
| 2025-11 | The age of research returns | "We're back to the age of research again, just with big computers" |
| 2025-11 | LLM generalization is fundamentally inadequate | "These models somehow just generalize dramatically worse than people" |

---

## 13. Index of Secondary Sources

The following analytical articles are valuable for understanding Ilya but are not primary sources:

| Source | URL | Value |
|------|-----|------|
| Zvi Mowshowitz analysis | https://thezvi.substack.com/p/on-dwarkesh-patels-second-interview | Point-by-point critical analysis of Dwarkesh #2 |
| EA Forum summary | https://forum.effectivealtruism.org/posts/iuKa2iPg7vD9BdZna/ | Structured summary of Dwarkesh #2 |
| The Neuron breakdown | https://www.theneuron.ai/explainer-articles/unpacking-dwarkeshs-ilya-sutskever-interview-on-agi-asi-and-how-to-build-both-safely | Inferences about SSI's strategy |
| AI Disruption Pub | https://aidisruptionpub.com/p/ilya-predicting-the-next-token-is | In-depth reading of the GTC detective-novel analogy |
| LessWrong discussion | https://www.lesswrong.com/posts/bMvCNtSH8DiGDTvXd/ | Community discussion of Dwarkesh #2 |
| Antoine Buteau | https://www.antoinebuteau.com/lessons-from-ilya-sutskever/ | Compilation of quotes |
| LifeArchitect.ai | https://lifearchitect.ai/ilya/ | Compilation of quotes + timeline |
| The Neuron (Memo) | https://www.theneuron.ai/explainer-articles/ilya-sutskevers-secret-memo-and-the-plot-to-merge-openai-with-anthropic | Detailed report on the 52-page memo |

---

## 14. Sources Still To Be Added / Not Obtained

- [ ] Full original text of the MIT Technology Review 2023-10 article (behind a paywall)
- [ ] Full verbatim transcript of the NeurIPS 2024 talk video
- [ ] Original text of the Musk v. OpenAI deposition (court filings)
- [ ] Full verbatim transcript of Lex Fridman Podcast #94 (available on happyscribe.com)
- [ ] Ilya's talk at the 2018 AI Frontiers Conference
- [ ] Early views on deep learning from 2015 (compiled on Nathan Lambert's interconnects.ai)
- [ ] Any public conversations/panel discussions with Hinton
