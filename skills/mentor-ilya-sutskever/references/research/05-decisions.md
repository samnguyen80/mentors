# Ilya Sutskever: Major Decisions, Turning Points, and Controversial Actions

> Research date: 2026-04-05
> Sources: Wikipedia, TechCrunch, Time, Fortune, Axios, CNBC, Gizmodo, Decrypt, Dwarkesh Patel Podcast, Calcalist, EA Forum, LessWrong, The Neuron, Israel Hayom
> Excluded sources: Zhihu, Baidu Baike, WeChat Official Accounts

---

## 1. Academic Career Decision: Studying under Hinton

### Background
Ilya Sutskever was born in 1986 in Russia (the former Soviet Union), emigrated to Israel at age 5, and moved to Canada at 16. At the University of Toronto he completed his bachelor's in mathematics (2005), master's in computer science (2007), and PhD in computer science (2013).

### Choice
Chose Geoffrey Hinton as his advisor, betting on neural networks in an era when deep learning was still marginalized by mainstream AI academia.

### Logic
Sutskever had an early intuition about the potential of neural networks. Mainstream AI research at the time favored symbolism and statistical methods, and Hinton's connectionist route was considered a minority view. Choosing Hinton meant betting on a direction that was not well regarded.

### Outcome
In 2012, working with Hinton and Alex Krizhevsky, he completed AlexNet, which won the ImageNet competition by a crushing margin and is regarded as the starting point of the deep learning revolution. Hinton later said: "Ilya thought we should do it, Alex made it work, and I got the Nobel prize."

### Key details
- Sutskever believed that neural network performance would improve as data volume grew (the earliest expression of his scaling intuition)
- The arrival of the large-scale ImageNet dataset happened to validate this intuition
- This is the intellectual origin of his later series of scaling bets

**Confidence in facts: high** (cross-validated by multiple primary sources)

---

## 2. Joining Google Brain (2012-2015)

### Background
After AlexNet's success, Sutskever briefly did a postdoc under Andrew Ng at Stanford (about 2 months), then returned to Toronto and joined DNNResearch, founded by Hinton. In 2013 Google acquired DNNResearch, and Sutskever joined Google Brain along with it.

### Choice
Moved from academia to industry, joining the Google Brain team.

### Logic
Google offered compute and data resources that academia could not match. The DNNResearch acquisition was a package deal (Hinton, Krizhevsky, and Sutskever joined together), so it was not entirely an independent personal decision.

### Achievements at Google
- Developed the sequence-to-sequence learning algorithm with Oriol Vinyals and Quoc Viet Le (it became the core framework of modern machine translation and language modeling)
- Took part in early TensorFlow development
- Took part in the AlphaGo paper (as one of the co-authors)

### Outcome
His work at Google laid the technical foundation for his later push of the GPT series at OpenAI, especially the experience with sequence-to-sequence.

**Confidence in facts: high**

---

## 3. Leaving Google, Co-founding OpenAI (2015)

### Background
In late 2015, Elon Musk, Sam Altman, and others were preparing to create a nonprofit AI lab. Sutskever was a key recruitment target.

### Choice
Gave up Google's generous conditions (resources, compute, team) to join a nonprofit AI organization that did not yet exist.

### Decision process [confirmed]
This was not an easy decision. According to Elon Musk's public account in 2023:
- Sutskever wavered repeatedly, several times saying he would join OpenAI, and was talked into staying by DeepMind's Demis Hassabis
- It went back and forth several times before he finally decided to join OpenAI
- Musk said "Ilya joining was the linchpin for OpenAI being ultimately successful"

### Logic
- Sutskever's own account: he enjoyed working at Google, but wanted to do more
- OpenAI's nonprofit structure and its mission to "benefit humanity" may have attracted him
- As Chief Scientist (rather than a member of a large Google team), he could steer the technical direction

### Outcome
- Became one of OpenAI's six board members
- Took the title of Chief Scientist, leading the research direction across the board
- All of OpenAI's later core technical breakthroughs (the GPT series) were completed under his scientific leadership

### Word-and-deed consistency analysis
The idealistic motives at the time of joining (nonprofit, benefit humanity) and OpenAI's later turn toward commercialization created a contradiction that foreshadowed the 2023 board crisis.

**Confidence in facts: high** (Musk's testimony as a primary source)

---

## 4. OpenAI Technical Route Decisions

### 4a. Choosing the GPT/Transformer route

**Background**: OpenAI explored multiple approaches early on (including reinforcement learning, robotics, etc.). Sutskever pushed the language model route based on large-scale unsupervised pre-training.

**Key bets**:
- Large-scale unsupervised text pre-training can unlock general capabilities
- The Transformer architecture (proposed in Google's 2017 "Attention is All You Need" paper) is suited to large-scale scaling
- GPT-1 (2018) → GPT-2 (2019) → GPT-3 (2020) → GPT-4 (2023) were all completed under Sutskever's scientific leadership

**Confidence in facts: high**

### 4b. The bet on the Scaling Hypothesis

**Background**: In 2020, Sutskever led OpenAI's research on neural scaling laws, establishing the power-law relationship between model performance and scale (parameter count, data volume, compute).

**Choice**: Bet OpenAI's core strategy on "bigger is better".

**Logic**:
- This can be traced back to the intuition of the AlexNet period: performance improves with data scale
- Scaling laws provided a mathematized predictive framework
- Pushed this direction together with Dario Amodei (who later left to found Anthropic) and others

**Outcome**:
- The success of GPT-3 and GPT-4 validated the scaling hypothesis
- OpenAI for a time became the global leader in AI

**Later change of position** [important contradiction]:
- December 2024 NeurIPS talk: declared "pre-training as we know it will end", and put forward the concept of "peak data" ("we have but one internet")
- November 2025 Dwarkesh Patel interview: said explicitly "2020-2025 was the age of scaling, and from 2026 we enter the age of research"
- Asked whether 100x more scaling would change everything, answered "I don't think that's true"
- Later clarified on X: scaling the current approach will still bring improvements, but "something important will continue to be missing"

**Word-and-deed consistency analysis**:
This is a major change of position. Sutskever went from a core driver of scaling to a questioner of it. But this is not necessarily a contradiction — he may believe that scaling genuinely worked in 2020-2025 and has only now hit a ceiling. The question is: what is he doing at SSI? If not scaling, what is the new direction he is betting on? He declines to say.

**Confidence in facts: high** (public talks and interviews)

---

## 5. The November 2023 Board Incident [most important]

This is the most controversial decision of Sutskever's career, and also the event with the most information.

### 5a. Preparation beforehand (at least a year)

**Confirmed facts** (source: the October 1, 2025 sworn deposition, nearly 10 hours):
- Sutskever spent at least a year considering removing Altman
- The condition he was waiting for was "the majority of the board is not obviously friendly with Sam"
- He wrote a 52-page memo, organized in brief form, accusing Altman of:
  - "a consistent pattern of lying"
  - "undermining his execs"
  - "pitting his execs against one another"
- The memo was sent to the independent directors via disappearing emails to prevent leaks
- CTO Mira Murati took screenshots and saved parts of the memo

**Key weak points** [note]:
- Sutskever admitted in testimony that the accusations in the memo "came almost entirely from a single source: CTO Mira Murati"
- He admitted he did not cross-verify with other executives
- He admitted that what he relied on was "secondhand knowledge"
- Reflecting afterward: "In hindsight, I realize that I didn't know it"

**Confidence in facts: high** (sworn deposition)

### 5b. The removal (November 17, 2023)

**Timeline**:
- November 17: the board announced Altman's firing
- November 18 (the next day): discussions began about merging with Anthropic
- November 20: Sutskever publicly said he "deeply regrets" his role
- November 21: Altman was reinstated

**Sutskever's motives** [multiple sources]:
1. **Safety concerns**: Sutskever believed Altman was pushing AI deployment and commercialization too fast, with excessive risk
2. **Management issues**: the lying and manipulation documented in the memo
3. **Structural contradiction**: nonprofit mission vs commercialization pressure

**The Anthropic merger plan** [confirmed]:
- Within 48 hours of Altman being fired, the board discussed merging with Anthropic
- Board member Helen Toner was "the most supportive" of the merger
- Toner even said "destroying OpenAI could be consistent with the mission"
- Sutskever himself explicitly opposed the merger: "I really did not want OpenAI to merge with Anthropic. I just didn't want to."
- Anthropic raised practical obstacles, and the plan did not advance

**Confidence in facts: high** (sworn deposition)

### 5c. Employee backlash and regret

**Confirmed facts**:
- 738 of 770 employees signed a petition demanding Altman's reinstatement
- Multiple executives resigned immediately
- Sutskever admitted: "I had not expected them to feel strongly either way" (he had expected employees not to care)
- He then posted publicly on X that he "deeply regrets" taking part

**Sutskever's after-the-fact assessment of the process**:
- Admitted the process was "rushed"
- The reason was "the board was inexperienced"

### 5d. Word-and-deed consistency analysis

**Points of contradiction**:
1. Spent a year carefully preparing the removal, yet did not do basic cross-verification of information (relying on a single source, Murati)
2. Claimed to fight for safety, yet "deeply regrets" it just three days after acting
3. Opposed the Anthropic merger (showing he did not want to destroy OpenAI), yet launched an action that nearly destroyed OpenAI
4. The 52-page memo shows deliberation, but his prediction of the employee reaction was completely off

**Possible explanations**:
- His core concern (AI safety) is real, but his execution ability falls far short
- He is a scientist rather than a manager/politician, and badly underestimated organizational dynamics
- "deeply regrets" may have been more a strategic statement (to preserve his own position) than a genuine change of mind

**Confidence in facts: high** (direct testimony and public statements)

---

## 6. Leaving OpenAI (May 2024)

### Background
After the November 2023 incident, Sutskever's position at OpenAI became awkward. He kept the title of Chief Scientist, but his actual influence had been marginalized.

### Choice
Formally announced on May 14, 2024 that he was leaving OpenAI.

### Public statements
- X post: "The company's trajectory has been nothing short of miraculous, and I'm confident that OpenAI will build AGI that is both safe and beneficial under the leadership of @sama"
- Later said in a Calcalist interview: "Ultimately, I had a big new vision...it felt more suitable for a new company"

### Collapse of the Superalignment team
- A few days after Sutskever left, Superalignment team co-lead Jan Leike also resigned
- Leike publicly criticized that OpenAI's "safety culture and processes have taken a backseat to shiny products"
- Leike said the team was "under-resourced" and "sailing against the wind"
- OpenAI then dissolved the entire Superalignment team
- The team was formed in 2023, with a commitment of 20% of compute at the time

### Word-and-deed consistency analysis
- The public statement on leaving was extremely friendly (praising Altman's leadership), in sharp contrast to his earlier 52-page accusatory memo
- Possible reasons: an equity agreement requiring that he not criticize publicly, or a strategic choice
- Jan Leike's resignation statement indirectly corroborates that Sutskever's long-standing safety concerns were genuine

**Confidence in facts: high**

---

## 7. Founding SSI (June 2024 to present)

### 7a. The founding decision

**Time**: announced June 19, 2024

**Co-founders**:
- Daniel Gross (former Apple AI lead, Y Combinator partner)
- Daniel Levy (former OpenAI researcher)

**Offices**: Palo Alto + Tel Aviv

**Core positioning**: "Our first product will be the safe superintelligence, and it will not do anything else up until then"

### 7b. Fundraising strategy

**Timeline**:
- September 2024: raised $1 billion (a16z, Sequoia, DST Global, SV Angel)
- March 2025: raised another $2 billion at a $32 billion valuation (Greenoaks Capital led with $500 million, joined by Alphabet, NVIDIA, a16z, Lightspeed, DST Global)
- As of 2025: about 20 employees, zero revenue, a $32 billion valuation

**Fundraising logic**: almost entirely dependent on Sutskever's personal reputation. No product, no revenue, no public technical roadmap.

### 7c. Operating strategy

**Confirmed**:
- No products, no services, only one thing: safe superintelligence
- In April 2025 reached a partnership with Google Cloud, gaining TPU compute
- Sutskever declines to disclose any technical details

**Leadership changes** (mid-2025):
- Meta tried to acquire SSI and was rejected by Sutskever
- In July 2025, co-founder Daniel Gross left to join Meta Superintelligence Labs
- Sutskever took over as CEO, and Daniel Levy was promoted to President

### 7d. Word-and-deed consistency analysis

**Contradictions and questions**:

1. **Safety vs commerce**: Sutskever left OpenAI because commercialization pressure affected safety. But SSI accepted $3 billion in venture capital, and the investors surely expect returns. How long can "insulated from short-term commercial pressures" last?

2. **A scaling skeptic who depends on compute**: If the scaling era is over, why does he still need Google TPUs and $3 billion? What exactly is SSI doing?

3. **The time-pressure paradox**: He criticizes OpenAI for being too hasty, but SSI itself faces pressure too — it cannot spend 20 years on "patient research", or investors will not tolerate it.

4. **Transparency**: Publicly advocates AI safety and the public's right to know, yet keeps SSI's technical direction completely secret.

5. **Co-founder attrition**: Daniel Gross was poached by Meta just over a year after SSI's founding, suggesting there may be problems with team cohesion or direction.

**Confidence in facts: medium-high** (fundraising data confirmed, but there is almost no public information on technical direction and internal state)

---

## 8. Evolution of Philosophical Position (across all decisions)

### Early period (2012-2020): pure technological optimism
- Believed scaling would unlock everything
- Pushed the GPT series to keep growing

### Middle period (2020-2023): safety awakening
- Pushed for the formation of the Superalignment team
- Increasingly worried about AI's existential risk
- 2023 MIT Technology Review interview: discussed the possibility of humans merging with machines

### Late period (2024-present): philosophical turn
- NeurIPS 2024: "pre-training as we know it will end"
- Dwarkesh Patel 2025 interview:
  - AI development could reach superhuman level in 5-20 years
  - Discussed the necessity of emotion for cognition (citing the case of brain-damaged patients who lost the capacity for emotion)
  - AI agents may need "intrinsic concern for sentient beings"
  - If most conscious entities in the future are AI, "caring about sentient life dilutes human primacy"
  - The long-term equilibrium may be human-machine merging

### External criticism
- The safety strategy depends on AI having sentience, an unverified philosophical assumption
- "safe superintelligence" may not exist in an absolute sense
- The deeper reason for the shift from a firm driver of scaling to a questioner of it is unclear

---

## 9. Summary: Sutskever's Decision Patterns

### Consistent traits
1. **Intuition-driven**: from AlexNet to GPT to SSI, his major decisions were based on strong intuition rather than thorough verification
2. **A scientist's mindset**: good at technical judgment, but repeatedly miscalculates in organizational management and political maneuvering
3. **Idealistic undertone**: whether joining OpenAI or founding SSI, there is a genuine sense of mission driving him
4. **A tendency toward an information cocoon**: the 52-page memo relied on a single source; completely misjudged the employee reaction

### List of contradictions
| Domain | Early position | Later position/behavior | Degree of contradiction |
|------|----------|---------------|----------|
| Scaling | Core driver | Declared the era over | Medium (explainable as cognitive evolution) |
| OpenAI mission | Nonprofit idealism | Praised Altman's leadership on leaving | High (in conflict with the 52-page accusation) |
| Safety action | Launched the removal | Deeply regrets three days later | High |
| Transparency | Advocates public right to know | SSI is entirely secret | Medium-high |
| Commercialization | Criticized OpenAI's commercialization | SSI accepted $3 billion in VC | Medium (different structure but similar pressure) |

### To watch
- What exactly is SSI researching? What is his "big new vision"?
- How long can the model of a $32 billion valuation with zero revenue last?
- After Daniel Gross's departure, will SSI's direction change?
- Will Sutskever's view that "emotion is necessary for cognition" show up in SSI's technical route?

---

## Sources

### Primary sources (sworn testimony / his own statements / public talks)
- Ilya Sutskever sworn deposition (October 1, 2025, Elon Musk v. OpenAI)
- NeurIPS 2024 talk
- Dwarkesh Patel podcast interview (November 2025)
- Calcalist Tech interview
- X/Twitter public statements

### Authoritative media reports
- [TechCrunch: Ilya Sutskever departs](https://techcrunch.com/2024/05/14/ilya-sutskever-openai-co-founder-and-longtime-chief-scientist-departs/)
- [Time: Sutskever leaves OpenAI](https://time.com/6978195/ilya-sutskever-leaves-open-ai/)
- [Fortune: Sutskever deeply regrets](https://fortune.com/2023/11/20/ilya-sutskever-openai-cofounder-deeply-regrets-resign/)
- [Axios: Sutskever regrets firing](https://www.axios.com/2023/11/20/sam-altman-fired-openai-board-illya-sutsever-regrets)
- [CNBC: SSI founding](https://www.cnbc.com/2024/06/19/openai-co-founder-ilya-sutskever-announces-safe-superintelligence.html)
- [CNBC: Sutskever becomes CEO](https://www.cnbc.com/2025/07/03/ilya-sutskever-is-ceo-of-safe-superintelligence-after-meta-hired-gross.html)
- [Gizmodo: Deposition details](https://gizmodo.com/former-openai-exec-explains-why-he-tried-to-do-a-coup-against-sam-altman-2000680769)
- [Decrypt: Inside the deposition](https://decrypt.co/347349/inside-deposition-showed-openai-nearly-destroyed-itself)
- [The Neuron: Secret memo and Anthropic merger](https://www.theneuron.ai/explainer-articles/ilya-sutskevers-secret-memo-and-the-plot-to-merge-openai-with-anthropic)
- [Israel Hayom: SSI in Tel Aviv](https://www.israelhayom.com/2025/03/06/a-secret-ai-startup-in-tel-aviv-got-30b-this-israeli-raised-pioneer-did-it/)
- [Wikipedia: Ilya Sutskever](https://en.wikipedia.org/wiki/Ilya_Sutskever)
- [Wikipedia: Safe Superintelligence Inc.](https://en.wikipedia.org/wiki/Safe_Superintelligence_Inc.)
- [EA Forum: Dwarkesh interview highlights](https://forum.effectivealtruism.org/posts/iuKa2iPg7vD9BdZna/highlights-from-ilya-sutskever-s-november-2025-interview)
