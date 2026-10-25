# Research on X/Twitter Content Strategy for the AI/Tech Niche

> Research date: 2026-04-06
> Research scope: AI/tech KOL content strategy, build in public, algorithm mechanics, open-source promotion, Chinese developers going global
> Source blacklist: Zhihu, WeChat Official Accounts, Baidu Baike

---

## 1. Core Accounts and Strategy Archetypes in the AI/Tech Niche

### 1.1 Account Archetype Matrix

| Type | Representative Account | Core Strategy | Follower Range |
|------|---------|---------|---------|
| **Build in Public** | @levelsio (Pieter Levels) | Public revenue, daily updates, failure post-mortems | 500K+ |
| **Learn in Public** | @swyx (Shawn Wang) | Making learning notes public, giving feedback | 100K+ |
| **Technical Educator** | @karpathy (Andrej Karpathy) | Explaining AI concepts clearly and accessibly, tutorial videos | 1M+ |
| **AI Agent/Tools** | @steipete (Peter Steinberger) | Live product iteration, technical opinions | 200K+ |
| **Open-Source Project** | @ExaAILabs (Exa) | Viral by-product marketing, API showcases | 50K+ |
| **AI News Aggregator** | @AIHighlight | Daily tool recommendations, quick reports on new models | 100K+ |

> Sources: first-hand observation (X account profile pages) + [Amperly: 31 Best AI Twitter Accounts 2026](https://amperly.com/best-artificial-intelligence-twitter-accounts/) + [X post: Future Stacked AI account recommendations](https://x.com/FutureStacked/status/2018353141465440693)

### 1.2 In-Depth Breakdown of Key Figures

#### Pieter Levels (@levelsio) — Godfather of Build in Public

**Content composition** (first-hand observation):
- **Revenue milestone tweets**: posts a Stripe screenshot every time he hits a new MRR level. For example "$10K MRR after 3 weeks with 318 customers" → lots of retweets
- **Live technical decisions**: trying new models (such as Flux), A/B test results, landing page conversion rates (1% → 4%)
- **Transparency about failure**: openly says that 97% of projects fail
- **Cross-project replication**: openly shares how he copy-pastes strategies from one project to another

**Key data**:
- Current monthly revenue ~$138K/month (November 2025 data)
- PhotoAI accounts for 70% of revenue ($106K/m); the rest includes InteriorAI, RemoteOK, and others
- One TikTok added $7,000 MRR/day for PhotoAI

**Strategic essence**: Build in Public is not "sharing progress"; it is "turning your audience into stakeholders." Audiences who watch you go from 0 to $100K MRR develop an investor mindset: they want you to succeed, so they spread your work on their own.

> Sources: [FastSaaS: How Pieter Levels Built a $3M/Year Business](https://www.fast-saas.com/blog/pieter-levels-success-story/) + [X: @levelsio PhotoAI $10K MRR](https://x.com/levelsio/status/1631715500010135552) + [X: @levelsio PhotoAI $150K/mo](https://x.com/levelsio/status/1850305637303160853)

#### swyx (@swyx) — Learn in Public + Pick Up What They Put Down

**Core ideas**:
1. **Learn in Public**: don't learn in private and then lurk. Write blog posts, make tutorials, ask and answer questions on forums, make YouTube videos — create "learning exhaust"
2. **Pick Up What They Put Down**: industry heavyweights release something new but get little feedback. You write a review/explainer/tutorial and tag them — they will retweet you, because "when others praise my work, I can retweet it all day"
3. **Macro-tweeting**: regularly resurface your own old tweets, especially the predictions that "turned out right"

**In practice**:
- Runs a daily AI newsletter (Latent Space), and Twitter is his "public notebook"
- Tweets exist because he needs a public notebook, the newsletter because he needs a searchable database of AI news, and charts because he needs to explain concepts — **the audience benefit is a by-product**
- Coined the role definition of "AI Engineer"

**Takeaway for Huashu**: swyx's strategy is especially suited to people who have depth but are not original researchers. The core point: **you don't need to invent something new; you need to explain what others invented clearly, and credit the original authors**.

> Sources: [swyx.io: Learn in Public](https://www.swyx.io/learn-in-public) + [swyx.io: Pick Up What They Put Down](https://www.swyx.io/puwtpd) + [swyx.io: How to Thought Lead (2026)](https://www.swyx.io/lead)

#### Andrej Karpathy (@karpathy) — Benchmark for the Technical Educator

**Content traits** (first-hand observation):
- Doesn't chase trends, but every post is deep content
- Admits what he doesn't know, shares the difficulty of learning
- Builds long-term assets with educational videos (YouTube: the Zero-to-Hero AI series)
- Founded Eureka Labs (an AI-native education company), productizing his Twitter educational content

**Why it works**: low frequency, high quality + Feynman-style explanation ability. When Karpathy posts, the whole AI community is watching, because he never posts noise.

> Sources: [X: @karpathy](https://x.com/karpathy) + [karpathy.ai](https://karpathy.ai/) + [Karpathy's three-folder method for a personal AI knowledge base](https://www.digitaltoday.co.kr/en/view/45521/karpathy-reveals-personal-ai-knowledge-base-built-with-three-folders)

#### Peter Steinberger (@steipete) — From iOS Veteran to AI Agent Pioneer

**Transition path**: 13 years of native iOS development (founder of PSPDFKit) → vibe coding in 2025 → OpenClaw (open-source AI Agent) → joined OpenAI in 2026

**Content strategy**:
- Shares technical opinions candidly (such as "Vibe Coding is a slur" — in fact, building things with AI takes skill)
- Publicly shares live OpenClaw development (such as "600 commits yesterday, PRs went from 2700 to 3100")
- After joining OpenAI, he became both an "insider and an outside voice"

> Sources: [OpenClawAI Blog: Vibe Coding Is a Slur](https://openclawai.io/blog/openclaw-creator-advice-playful-building/) + [X: @steipete joining OpenAI](https://x.com/steipete/status/2023154018714100102)

---

## 2. X/Twitter Algorithm Mechanics in 2026 (Must-Know for the AI/Tech Niche)

### 2.1 The Three-Stage Ranking Pipeline

1. **Candidate selection**: from 500 million tweets per day, ~1,500 candidates are selected for each user (50% from accounts they follow, 50% from outside)
2. **Machine-learning ranking**: a neural network analyzes thousands of features and outputs 10 probability labels
3. **Grok-powered update** (January 2026): a transformer model reads every post and video, making 5 billion ranking decisions per day

### 2.2 Signal Weight Formula

| Engagement Type | Weight | Multiple (vs. like) |
|---------|------|-------------------|
| Like | x1 | 1x |
| Bookmark | x10 | 10x |
| Link click | x11 | 11x |
| Profile click | x12 | 12x |
| Reply | x13.5 | 13.5x |
| Retweet | x20 | 20x |
| **Conversation (reply + author reply)** | **x75** | **150x** |

**Key insight**: one quality conversation = the algorithmic value of 150 likes. This explains why AI/tech KOLs actively reply to comments.

### 2.3 Algorithm Points Specific to the AI/Tech Niche

**Engagement velocity is the strongest signal**:
- The first 15-30 minutes of engagement decide everything
- 10+ interactions within 15 minutes → exponential spread
- Fewer than 3 interactions within 15 minutes → the tweet dies
- **Countermeasure**: post when your audience is most active (for the global AI/tech audience: Pacific Time 8-10 AM, which is 23:00-01:00 late at night Beijing time)

**Time decay**: visibility halves every 6 hours. AI news is time-sensitive, so responding quickly is critical.

**External link penalty**:
- Tweets with links lose 30-50% of reach (close to zero engagement for non-Premium users)
- **Fix**: keep links out of the main tweet and put the link in the first reply
- After March 2026, the link penalty was essentially removed for Premium users

**X Premium boost**: paying users get a 2-4x reach boost. For anyone serious about X, this is a necessary investment.

> Sources: [PostEverywhere: How X Algorithm Works 2026](https://posteverywhere.ai/blog/how-the-x-twitter-algorithm-works) + [Teract: Twitter Algorithm 2026 Deep Dive](https://www.teract.ai/resources/twitter-algorithm-2026) + [Sprout Social: Twitter Algorithm 2026](https://sproutsocial.com/insights/twitter-algorithm/)

---

## 3. Content Strategy Specific to the AI/Tech Niche

### 3.1 Content Type and Performance Matrix

| Content Type | Engagement | Suggested Frequency | Example |
|---------|--------|---------|------|
| **Quick review of a new model/product** | Very high | Whenever there's news | "GPT-5.3 just dropped. I tested it on 3 scenarios..." |
| **Build in Public updates** | High | 2-3 times a week | MRR screenshots, feature launches, user feedback |
| **Technical tutorial/Thread** | High | Once a week | An 8-12 tweet tutorial thread |
| **Demo video/GIF** | High | Whenever you have results | 15-30 second product demo |
| **Hot take/controversial opinion** | Medium-high | Use with caution | "Vibe coding is a slur" |
| **Paper breakdown thread** | Medium | Once a week | Unpack the key findings in plain language |
| **Tool comparison/review** | Medium | 2-3 times a month | Screenshots + test result tables |
| **Personal story/reflection** | Medium | Mix in occasionally | Founder journey, career transition |
| **Meme/humor** | Highly variable | Use with caution | AI-related memes |

### 3.2 New Model Releases: Rapid-Response Strategy

The most distinctive opportunity window in the AI niche is the **new model release** (such as GPT-5, Claude Opus, DeepSeek, etc.). This is what sets it apart from other areas of tech.

**Response timeline**:
1. **0-1 hour after release**: post a Quick Take (first reaction + one sharp opinion)
2. **1-6 hours after release**: post Demo/test results (screenshots + GIF)
3. **6-24 hours after release**: post a deep Thread (systematic tests + comparison + opinion)
4. **1-7 days after release**: post a long-form article/video (full review + real-world cases)

**What OpenAI does** (worth borrowing): within minutes of a launch, Sam Altman tweets asking users "what do you want to build with it?" — letting the community produce the content itself, rather than promoting one-way.

> Sources: [FutureSocial: How OpenAI Used Twitter Replies to Create Launch Content](https://futuresocial.beehiiv.com/p/openai-used-twitter-replies-create-launch-content) + first-hand observation

### 3.3 Build in Public Operating Manual

**What to share**:
- MRR milestones + Stripe screenshots (use the [BrandBird MRR Meter](https://www.brandbird.app/tools/twitter-mrr-meter) to generate standardized images)
- Feature launches + demo screenshots/videos
- Failure post-mortems
- Tech stack choices and the reasoning behind them
- Screenshots of user feedback
- Monthly/quarterly recap threads

**What not to share**:
- Exact customer acquisition cost (CAC) and unit economics (competitively sensitive)
- Customers' personal information
- Implementation details of your core competitive advantage

**Formatting tips**:
- Open threads with a Hook: "Week 12 of building [Product]: Hit $2K MRR..."
- Close threads with a CTA: "Follow along for weekly updates"
- Visual content gets 5x more engagement
- Reply to every response within 1 hour

**Case data**:
- AudioPen: built in 12 hours → 100 paying users in 2 days → Product Hunt #1 → $73K revenue in the first 2 months
- SiteGPT: 24K+ Twitter followers → Product Hunt #1 → $15K MRR in month 6 → $95K MRR
- One indie hacker: grew to 2,400 Twitter followers in 4 months → $8K MRR at product launch

> Sources: [OpenTweet: Build in Public Guide](https://opentweet.io/blog/build-in-public-twitter-guide-saas-founders) + [Teract: Twitter Strategy for Indie Hackers 2026](https://www.teract.ai/resources/twitter-strategy-indie-hackers-2026) + [AudioPen Starter Story](https://www.starterstory.com/stories/audiopen) + [SiteGPT Rise to $15K MRR](https://www.indiehackers.com/post/from-side-hustle-to-ai-star-sitegpts-rise-to-15k-mrr-ff15fee186)

### 3.4 Thread Writing Best Practices

**Supporting data**: threads of 8-12 tweets perform 47% better than short threads (Sprout Social 2026 data). Threads overall get 3-5x more engagement than single tweets.

**Structure template** (for AI/tech):

```
Tweet 1 (Hook): a startling number / counterintuitive take + "Thread"
Tweets 2-3: background and problem definition
Tweets 4-8: core argument / steps / findings
Tweets 9-10: hands-on practice / code / screenshots
Tweet 11: summary + key takeaway
Tweet 12: CTA (follow / bookmark / retweet request)
```

**Thread types specific to the AI niche**:
1. **"I tested X and the results surprised me"**: hands-on test threads for new models/tools
2. **"N lessons from going 0 to $XK MRR"**: Build in Public recaps
3. **"This paper changed how I think"**: paper breakdowns
4. **"X vs Y: a deep comparison"**: head-to-head tool/model reviews
5. **"I used AI to do X and saved N hours"**: real-world case studies

> Sources: [AI Free Forever: 15 Best Viral Threads 2026](https://aifreeforever.com/blog/15-best-twitter-thread-examples-that-went-viral) + [Teract: Twitter Algorithm 2026](https://www.teract.ai/resources/twitter-algorithm-2026)

---

## 4. Visual Content Strategy (Code Screenshots, GIFs, Video Demos)

### 4.1 Performance Comparison by Content Format

| Format | Engagement Rate | Best Length/Size | Use Case |
|------|--------|-------------|---------|
| Plain text | 0.1% | 120-130 characters is best | Opinions, hot takes |
| Image/screenshot | 0.08% | 16:9 landscape | Code screenshots, data tables |
| GIF | Medium | 3-8 second loop | Feature demos, interaction effects |
| Video | 0.42% | 15-30 seconds | Product demos, tutorials |
| Thread | 3-5x a single tweet | 8-12 tweets | Deep content, tutorials, reviews |

**Note**: X is the only major platform where text performs as well as video. But video's 0.42% engagement rate is far higher than an image's 0.08%.

### 4.2 Code Screenshot Tools and Tips

- **[Snappify](https://snappify.com/)**: creates polished code presentation images, and you can add an avatar and username
- **[Pika](https://pika.style/templates/code-image)**: generates code screenshots with many themes
- **[Codeshot](https://codeshotapp.com/)**: pick a theme, export in Twitter dimensions

**Key principles**:
- Code screenshots should highlight the key lines; don't paste a full page of code
- Add annotations/highlights to mark the key points
- Treat the first frame as a billboard: bold text, high contrast, a clear promise

### 4.3 Video Demo Best Practices

- **16:9 landscape** is best for demos and screen recordings
- **15-30 seconds** is the best length (maximizes completion rate)
- **Assume viewers watch on mute**: put key information in captions
- **The first frame is the cover**: it acts as a billboard in the feed
- **After posting the main video, reply with a Thread** that adds key points, timestamps, and links

> Sources: [ScriptStorm: Twitter Video Best Practices](https://scriptstorm.ai/blog/twitter-video-best-practices-length-format-engagement) + [Snappify](https://snappify.com/) + [Codeshotapp](https://codeshotapp.com/posts/how-to-share-code-on-twitter/)

---

## 5. Open-Source Project Promotion Strategy

### 5.1 Key Twitter/X Promotion Moves

1. **GitHub Social Preview**: upload a polished promo image in the repo settings so shared links stand out (many projects overlook this)
2. **Keep talking**: the main strategy is to keep yapping — post small updates, your coding journey, technical decisions
3. **Listicle cross-tagging**: write a list article that includes similar projects, and tag each maintainer when you tweet it — they will like/retweet it
4. **Awesome lists**: submit PRs to awesome-xxx lists on GitHub
5. **Multi-platform launch**: post Tuesday to Thursday at Pacific Time 8-10 AM, adapting the copy for each platform

**Core finding**: tweets have a significant positive effect on gaining new stars and new contributors. An active Twitter community plays an important role in attracting new contributors (validated by an academic paper).

### 5.2 Viral By-Product Strategy: Exa's Twitter Wrapped

**Case**: Exa (an AI search engine) gained 1.7 million users through its "Twitter Wrapped" tool.

**What they did**:
- Launched on December 26: an AI analyzes a user's X account and generates a personalized year-in-review, roasts, and predictions for the future
- 500K views within 4 hours
- 4 days later: 59,000 retweets and 13.6 million views

**Why it worked**: same logic as Spotify Wrapped — **naturally shareable personalized content**. Users share their results → friends get curious → they go generate their own → the loop keeps spreading.

**Takeaway**: an AI product can go viral by building a **free, personalized, shareable by-product**. The product itself doesn't need to be viral; you need a viral entry point.

> Sources: [Indie Hackers: Exa Twitter Wrapped](https://www.indiehackers.com/post/tech/exa-an-ai-powered-search-engine-gains-1-7m-users-with-viral-twitter-wrapped-vUAEDrWM4ELz5UHcbyjG) + [DEV: Promoted Open Source Repo to 6K Stars](https://dev.to/wasp/how-i-promoted-my-open-source-repo-to-6k-stars-in-6-months-3li9) + [FreeCodeCamp: 4.5K Stars in 6 Months](https://www.freecodecamp.org/news/how-to-get-more-engagement-with-your-open-source-project/) + [arXiv: Impact of Twitter Mentions on GitHub](https://arxiv.org/html/2401.02755)

---

## 6. X Strategy for Chinese AI Developers Going Global

### 6.1 Success Stories

**Han Xiao (@hanaborxiao) — Founder of Jina AI**:
- Founded Jina AI in 2020 after working on AI at Tencent, headquartered in Berlin, with R&D centers across San Francisco, Beijing, and Shenzhen
- Acquired by Elastic in 2025
- Strategy: mainly English content, open-source community building, speaking at global conferences
- Active on the board of the LF AI Foundation, building international trust through open source

**The DeepSeek team**:
- Founder Liang Wenfeng is extremely low-profile and barely uses social media
- But DeepSeek's technical papers are widely discussed on X (spread by others on their behalf)
- Proves: **when the product itself is good enough, the community will spread it for you**

### 6.2 Special Challenges and Strategies for Chinese Developers

1. **Language barrier**: writing in English is a hurdle that has to be cleared, but it doesn't need to be perfect — the AI niche is more forgiving of non-native speakers
2. **Time zone gap**: posting times need to fit North American/European audiences (Pacific Time 8-10 AM)
3. **Trust building**: open-source contributions are the best international trust asset
4. **Content differentiation**: first-hand information from the Chinese AI ecosystem (such as DeepSeek technical details, domestic AI use cases) is uniquely valuable to international audiences
5. **Bilingual strategy**: run Chinese and English separately, don't mix them

> Sources: [Han Xiao Bio](https://hanxiao.io/about/) + [AI Berlin: Interview Han Xiao](https://ai-berlin.com/blog/article/interview-with-dr-han-xiao-ceo-and-co-founder-of-jina-ai) + [Nature: How China Created DeepSeek](https://www.nature.com/articles/d41586-025-00259-0) + first-hand observation

---

## 7. Topic Categories and Conversion Paths in the AI/Tech Niche

### 7.1 Ten Topic Types (Ranked by Engagement)

1. **Quick reviews of new models/features**: test it first and share an opinion (highest engagement, shortest time window)
2. **Build in Public milestones**: MRR screenshots, user-count breakthroughs (high engagement + high trust-building)
3. **Hands-on tutorial threads**: "How to use X to do Y" (high save rate, good long-tail traffic)
4. **Tool comparison reviews**: "How Claude vs GPT vs Gemini perform in scenario X" (high search value)
5. **Hot takes/controversial opinions**: "Vibe coding is a slur" (high discussion, risky)
6. **Personal failures/lessons**: "I did X and lost Y" (high resonance, builds authenticity)
7. **Paper breakdowns**: unpack in plain language (medium engagement, strong professionalism signal)
8. **Resource roundups**: "The 10 best X tools" (high save rate)
9. **Industry trend predictions**: "5 AI trends for 2026" (highly variable, high payoff if you're right)
10. **Memes/humor**: AI-related jokes (low barrier to spreading, but doesn't build professionalism)

### 7.2 Content-to-Conversion Path

```
X tweet/Thread → personal brand awareness
    |
Blog/Newsletter (deep content) → email list
    |
Product Hunt/GitHub Launch → user acquisition
    |
Paid product/consulting/course → revenue
```

**Key point**: content on X doesn't convert directly; it builds trust and an audience. Conversion happens in deep content (newsletter, blog) and at product launches.

---

## 8. Tactical Cheat Sheet

### 8.1 Posting Cadence

| Content Type | Frequency | Timing |
|---------|------|------|
| Daily tweets (opinions, small updates) | 3-5 a day | 2-3 hours apart |
| Threads (deep content) | 1-2 a week | Tuesday-Thursday |
| Replying to others | 70% of posting volume | All day |
| Quick review of a new model | Whenever there's one | Within 1 hour of release |

### 8.2 Growth Formula

**0-1K followers stage**:
- 70% of your energy on replies, 30% on posting
- Reply to big accounts in your field, adding valuable supplements
- swyx's PUWTPD strategy: write reviews/tutorials for the heavyweights' new work

**1K-10K followers stage**:
- Build content pillars (3-5 fixed topics)
- 1-2 threads a week to establish expertise
- Start Build in Public

**10K+ followers stage**:
- Newsletter/Blog to build deep content assets
- Leverage your existing audience for product launches
- Begin selective partnerships and promotions

### 8.3 Growth Hacks Specific to the AI Niche

1. **A new model's launch day is your Super Bowl**: everyone is scrolling AI news, so your related content naturally gets traffic
2. **Free tools = acquisition entry point**: Exa's Twitter Wrapped, Pieter's many free AI toys
3. **Open source = trust accelerator**: open-source projects earn far more trust on X than closed-source products
4. **Screenshots > descriptions**: always use visual evidence (Stripe screenshots, product demos, code results)
5. **Threads are your long-form weapon**: a Thread on X is the equivalent of a blog post on other platforms
6. **Replies are the most underrated growth lever**: one good reply carries the algorithmic weight of 13.5 likes

---

## 9. How the AI/Tech Niche Differs from General Twitter Strategy

| Dimension | General Twitter | AI/Tech Niche |
|------|------------|------------|
| **Timeliness** | Can be scheduled in advance | New model releases demand hour-level response |
| **Content depth** | Mostly short and fast | Threads and technical breakdowns are the core assets |
| **Visual content** | Beautiful images, infographics | Code screenshots, terminal recordings, demo GIFs |
| **Trust building** | Personal brand story | Open-source contributions + technical depth + revenue transparency |
| **Audience traits** | Broad consumers | Developers/founders (high value but hard to fool) |
| **Link strategy** | Avoid whenever possible | Must share (GitHub/Blog), but put it in a reply |
| **Growth path** | Followers → brand partnerships | Followers → product users/open-source contributors |
| **Internationality** | Clearly localized | The AI community is naturally global, with English as the common language |
| **Validation standard** | Follower count/engagement count | Can you actually build things (ship or shut up) |

---

## 10. Specific Recommendations for Huashu's X Strategy

Based on the research above, and given Huashu's identity (AI Native Coder, indie developer, 300K+ followers on Chinese social media):

1. **Clear positioning**: "a Chinese indie developer building products with AI" — this identity has unique value on English X (first-hand information from the Chinese AI ecosystem + the indie developer narrative)
2. **Suggested content pillars**: Build in Public (product data) + hands-on AI tool tests + a Chinese AI perspective
3. **Rapid response**: when a new model is released, do a quick review from a Chinese developer's perspective (differentiation)
4. **Product as content**: the development stories behind products like Xiaomao Fill Light (小猫补光灯) and GLM Code are a natural fit for Build in Public
5. **Threads as the workhorse**: a weekly Thread, with daily replies as the main activity; don't chase daily posting volume
6. **Visual evidence**: attach a screenshot/GIF/video to every product-related tweet
7. **Separate the two languages**: use English on X, and Chinese on WeChat Official Accounts/Xiaohongshu, without mixing them

---

*Research complete. Sources are noted at the end of each section, distinguishing first-hand observation from second-hand analysis. Core finding: success in the AI/tech niche on X comes not from "content marketing tricks" but from "doing real things and sharing them in public" — Build in Public and Learn in Public are not strategies, they are a way of life.*
