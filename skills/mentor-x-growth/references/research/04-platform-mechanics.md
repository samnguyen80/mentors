# X/Twitter Platform Algorithm Mechanics Research

> Research date: 2026-04-06
> Data coverage: the full evolution from the first open-sourcing in 2023 to the second open-sourcing in January 2026
> Information grading: 🟢 officially published / verifiable in open-source code | 🟡 reported by authoritative media / data analysis | 🔴 speculation from community testing

---

## 1. Evolution of the Recommendation Algorithm Architecture

### 1.1 The three-stage pipeline

🟢 **Source: open-source code on GitHub**

X's recommendation system uses a three-stage pipeline architecture, with a clear line of descent from the first open-sourcing in 2023 (`twitter/the-algorithm`) to the 2026 Grok version (`xai-org/x-algorithm`):

| Stage | Function | Implementation |
|-------|----------|----------------|
| **Candidate Sourcing** | Narrow hundreds of millions of posts down to about 1,500 candidates | in-network (content from accounts you follow) + out-of-network (ML retrieval) |
| **Ranking** | Predict engagement probability for the candidates and score them | Phoenix (Grok transformer model) |
| **Filtering & Blending** | Deduplication, diversity assurance, ad insertion | Home Mixer orchestration layer |

- Source: [GitHub - xai-org/x-algorithm](https://github.com/xai-org/x-algorithm) | [GitHub - twitter/the-algorithm](https://github.com/twitter/the-algorithm)

### 1.2 Grok takes over recommendations entirely (October 2025 → open-sourced January 2026)

🟢 **Source: Elon Musk's tweets + GitHub release**

**Timeline:**
- **September 2025**: Musk announced "The algorithm will be purely AI by November" and promised to open-source it every two weeks
- **October 2025**: Grok began fully replacing the traditional heuristics
- **November 2025**: The Following feed also switched to Grok ranking
- **January 20, 2026**: xAI released `xai-org/x-algorithm` on GitHub, officially open-sourcing the Rust rewrite

**Key changes:**
- Rewritten from Scala into a hybrid architecture of **Rust (62.9%) + Python (37.1%)**
- The core transformer architecture comes from Grok-1, adapted for the recommendation use case
- Grok "reads every post and watches every video" (processing 100M+ pieces of content a day)
- A commitment to push code updates plus developer notes every 4 weeks

- Source: [Elon Musk's tweet](https://x.com/elonmusk/status/1969081066578149547) | [@XEng tweet](https://x.com/XEng/status/2013471689087086804) | [TechCrunch report](https://techcrunch.com/2026/01/20/x-open-sources-its-algorithm-while-facing-a-transparency-fine-and-grok-controversies/) | [Social Media Today](https://www.socialmediatoday.com/news/x-formerly-twitter-switching-to-fully-ai-powered-grok-algorithm/803174/)

### 1.3 The four core modules (2026 open-source release)

🟢 **Source: code and README in the GitHub repository**

| Module | Language | Function |
|--------|----------|----------|
| **Home Mixer** | Rust | Orchestration layer; receives gRPC requests and coordinates the whole pipeline |
| **Thunder** | Rust | In-memory post store; consumes Kafka events and serves sub-millisecond in-network content lookups |
| **Phoenix** | Python/JAX | The Grok transformer ranking engine; predicts engagement probability |
| **Candidate Pipeline** | Rust | A reusable framework: Sources fetch → Hydrators enrich → Filters filter → Scorers score → Selector returns TopN |

- Source: [xai-org/x-algorithm README](https://github.com/xai-org/x-algorithm/blob/main/README.md) | [Phoenix README](https://github.com/xai-org/x-algorithm/blob/main/phoenix/README.md) | [DeepWiki analysis](https://deepwiki.com/xai-org/x-algorithm)

### 1.4 Promptable Feeds

🟡 **Source: Musk's tweets + media reports**

Users can adjust their Feed with natural-language instructions, for example "Show me more tech innovations, less politics". This is a product of Grok being embedded directly into the recommendation engine.

- Musk announced the feature in September 2025
- The January 2026 open-source release includes the promptable feeds interface
- Source: [WebProNews](https://www.webpronews.com/xs-promptable-algorithm-musks-bid-to-hand-users-the-feed-controls/) | [Social Media Today](https://www.socialmediatoday.com/news/x-formerly-twitter-moving-to-personalized-ai-powered-algorithm/760698/)

---

## 2. Engagement Weight Formula

### 2.1 Exact weights (verifiable in open-source code)

🟢 **Source: xai-org/x-algorithm open-source code + confirmed by Social Media Today**

X is the only major social platform to have open-sourced its recommendation algorithm twice, and its engagement weights are fully public:

| Engagement type | Weight | Relative multiple (vs Like) | Notes |
|-----------------|--------|-----------------------------|-------|
| **Conversation reply** (Reply + author engagement) | +75 | **150x** | Your reply gets a reply or like from the original post's author |
| **Reply** | +13.5 | **27x** | An ordinary reply |
| **Profile click** | +12.0 | **24x** | A user clicks through to your profile and likes or replies |
| **Conversation deep-click** | +11.0 | **22x** | A user clicks into the conversation and replies or likes |
| **Dwell time (Dwell > 2min)** | +10.0 | **20x** | A user clicks into the conversation and stays more than 2 minutes |
| **Retweet** | +1.0 | **2x** | A repost |
| **Like** | +0.5 | **1x (baseline)** | The baseline value |
| **Bookmark** | ~+10 | **~20x** | Inferred from community analysis, not an official exact value |

**Core insight: conversation depth crushes everything else.** A reply chain that draws in the author's engagement is worth more than 150 likes.

⚠️ **About the weight data across versions**:
- The weights from the first open-sourcing in 2023 differ slightly from the 2026 version
- Figures like "Reply 27x, Retweet 40x" cited in early community analysis came from simplified calculations on the 2023 version
- In the 2026 version the Retweet weight drops sharply (from ~20x to ~2x) and the conversation weight rises further
- This document goes by the 2026 open-source release

- Source: [Social Media Today](https://www.socialmediatoday.com/news/x-formerly-twitter-open-source-algorithm-ranking-factors/759702/) | [posteverywhere.ai source-code analysis](https://posteverywhere.ai/blog/how-the-x-twitter-algorithm-works) | [Typefully analysis](https://typefully.com/blog/x-algorithm-open-source)

### 2.2 Negative signals (penalty mechanisms)

🟢 **Source: open-source code**

| Negative signal | Penalty weight | Effect |
|-----------------|----------------|--------|
| **Report** | -369x | Distribution is almost removed outright |
| **Block/Mute/Show Less** | -74x | Sharply reduces recommendations to that user |

🟡 **Source: media analysis**

| Negative signal | Penalty effect |
|-----------------|----------------|
| **External links** | Reach down 30-50%; since March 2025, link posts from non-Premium accounts have had median engagement of zero |
| **More than 2 hashtags** | Reach down about 40%, flagged as a spam signal |
| **Repeated content/links** | Visibility is reduced gradually, and in severe cases triggers a shadow ban |

- Source: [posteverywhere.ai](https://posteverywhere.ai/blog/how-the-x-twitter-algorithm-works) | [Tweet Archivist](https://www.tweetarchivist.com/how-twitter-algorithm-works-2025)

---

## 3. The Visibility Boost from a Premium Subscription

### 3.1 Algorithmic boost multipliers

🟢 **Source: confirmed in open-source code**

| Scenario | Premium boost | Notes |
|----------|---------------|-------|
| **In-network (followers' Feed)** | **4x** | The chance your post shows up in the Feed of people who follow you is multiplied by 4 |
| **Out-of-network (non-followers' Feed)** | **2x** | The chance your post shows up in the Feed of people who don't follow you is multiplied by 2 |

### 3.2 Real-world data

🟡 **Source: Buffer's analysis of 18.8M posts + media reports**

- Premium accounts get about **10 times** the reach per post of ordinary accounts
- The gap for Premium+ accounts has widened further since 2025
- Premium replies rank higher by default in discussions under popular posts (Q1 2026 data shows 30-40% higher reply exposure)
- Since March 2026, posts from non-Premium accounts that include external links have had median engagement of zero

### 3.3 The relationship between TweepCred and Premium

🟡 **Source: Circleboom analysis**

Premium subscribers get an instant +100 TweepCred boost, going from a starting point of -128 to -28, which greatly shortens the account's cold-start period.

- Source: [Circleboom](https://blog-content.circleboom.com/does-x-premium-boost-algorithm/) | [posteverywhere.ai](https://posteverywhere.ai/blog/how-the-x-twitter-algorithm-works) | [Buffer data](https://buffer.com/resources/data-best-content-format-social-media/)

---

## 4. TweepCred Account Reputation Score

🟢 **Source: the TweepCred module in the open-source code**

### 4.1 Basic mechanics

- Every X account has an invisible reputation score: **TweepCred**
- Range: **-128 to +100**
- Starting value for a new account: **-128**
- Minimum threshold for normal distribution: **+17** (below this, content is throttled)
- Premium subscribers instantly get a **+100 boost**

### 4.2 Influencing factors

🟡 **Source: community reverse-engineering analysis**

TweepCred is a PageRank-like weighted composite score determined by the following factors:

| Factor | Direction |
|--------|-----------|
| Following/follower ratio | Following far more than followers → negative |
| Engagement quality | High-quality conversations → positive |
| Account history | Older account + consistent behavior → positive |
| Tweet language and Bio | Complete profile → positive |
| Consistency of posting style | Sudden large changes → negative |
| **Grok tone scoring (new in 2025)** | Positive/constructive content → positive |

⚠️ **New change in 2025**: Grok AI now scores the **tone (sentiment)** of every post, and positive, constructive content gets more distribution.

- Source: [Circleboom TweepCred analysis](https://circleboom.com/blog/tweepcred-what-it-is-why-it-matters-and-how-to-increase-your-score-on-x-twitter/) | [Radaar](https://www.radaar.io/resources-121/blog-388/are-you-ready-to-discover-the-hidden-x-algorithm-secrets-behind-tweepcred-shadow-hierarchy-and-dwell-time-in-2025-15361/)

---

## 5. How Different Content Types Are Treated

### 5.1 Text vs video: is X the only platform where text crushes video?

🟡 **Source: Buffer's analysis of 45M+ posts + multiple media outlets**

**Conclusion: it's more complicated than that, and the data conflict.**

| Data source | Conclusion |
|-------------|------------|
| Buffer 2025-2026 data | Median engagement rate of text posts (0.48%) is slightly higher than video |
| Multiple SEO/marketing agencies | Native video gets about 10x more engagement + algorithmically favored distribution |
| 2026 social media strategy report | User preference for short video (37%) and text (36%) is nearly even |

**A more accurate statement**: among major social platforms, X is the one where **text posts perform closest to, or even beyond, video**, but you can't simply say "text crushes video." At the algorithm level, native video does get a distribution boost; but in actual engagement rate, high-quality text posts hold their own against video.

### 5.2 Algorithmic preference by content type

🟡 **Source: synthesis of multiple analyses**

| Content type | Algorithmic treatment |
|--------------|----------------------|
| **Plain text posts** | Consistently the highest engagement rate, especially good for sparking conversation |
| **Native video (<2:20)** | Gets a distribution boost; completion rate is the key signal |
| **Image posts** | Increase dwell time, a positive signal |
| **External link posts** | ⚠️ Severely penalized: reach down 30-50%, nearly invisible for non-Premium accounts |
| **Quote Tweet** | Weighted higher than a plain retweet |
| **Thread (long tweet chain)** | Engagement across many posts accumulates; strong overall effect |

- Source: [Buffer](https://buffer.com/resources/data-best-content-format-social-media/) | [Sprout Social](https://sproutsocial.com/insights/twitter-algorithm/) | [SocialBee](https://socialbee.com/blog/twitter-algorithm/)

---

## 6. Key Time Windows

### 6.1 The golden 30 minutes and Engagement Velocity

🟡 **Source: consensus across multiple analytics firms**

- The **first 30 minutes** are the decisive window: the engagement velocity in this period determines whether the algorithm pushes the post into a larger traffic pool
- The broader **first 2 hours** also matter a great deal
- **Velocity > total volume**: 100 likes in 10 minutes > 500 likes accumulated over 3 days
- The core logic of the algorithm: early engagement = quality stamp

### 6.2 Dwell Time

🟢 **Source: weight definitions in the open-source code**

- A user spending more than 2 minutes on your post/conversation = +10 weight (about 20x a Like)
- Short dwell time is treated as low-quality content and leads the algorithm to suppress it
- This means **long posts that people want to read to the end** are favored by the algorithm over **short content that gets scrolled past in a flick**

### 6.3 Best posting times

🟡 **Source: Buffer's analysis of 1M posts + Sprout Social + SocialPilot's analysis of 50,000 accounts**

| Dimension | Recommendation |
|-----------|----------------|
| **Best time window** | Weekdays 9AM-2PM (local time), second best 12PM-6PM |
| **Best days** | Tuesday, Wednesday, Thursday (Tuesday is best) |
| **Worst day** | Saturday |
| **Posting frequency** | **3-5 posts/day** is the optimal range, spaced 2-3 hours apart |
| **Frequency ceiling** | More than 5 posts/day actually slows growth |
| **Frequency floor** | Fewer than 1 post/day gives clearly insufficient growth |

⚠️ The above is data for global English-speaking users. Chinese-language creators need to adjust for their target audience's time zone (for example, for readers in China, Beijing time maps to roughly 9PM-2AM EST).

- Source: [Buffer](https://buffer.com/resources/best-time-to-post-on-twitter-x/) | [Sprout Social](https://sproutsocial.com/insights/best-times-to-post-on-twitter/) | [SocialPilot](https://www.socialpilot.co/insights/best-time-to-post-on-twitter) | [Tweet Archivist](https://www.tweetarchivist.com/twitter-posting-frequency-guide-2025)

---

## 7. Shadow Bans

### 7.1 The four types

🟡 **Source: shadowban detection tools + community analysis**

| Type | What it looks like |
|------|--------------------|
| **Search Suggestion Ban** | Your username doesn't appear in search suggestions |
| **Search Ban** | Your posts don't appear in search results |
| **Ghost Ban** | Your replies are invisible to others |
| **Reply Deboosting** | Your replies are collapsed under "Show more replies" |

### 7.2 Trigger conditions

🟡 **Source: Pixelscan + multiple guides**

| Behavior | Risk level |
|----------|------------|
| Mass following/unfollowing in a short time | 🔴 High (mass unfollowing can trigger a 3-month shadowban) |
| Liking 200+ posts within 1 hour | 🔴 High (automated detection) |
| Replying in bulk to people who don't follow you | 🟡 Medium |
| Posting the same link/hashtag repeatedly | 🟡 Medium |
| Using suspicious third-party tools | 🔴 High |
| Posting content that many people report | 🔴 High (-369x penalty) |

### 7.3 Detection methods

- Online tool: [shadowban.yuzurisa.com](https://shadowban.yuzurisa.com/) detects all 4 kinds of restrictions from a username
- Manual verification: ask someone who doesn't follow you to search for your username or look for your replies

### 7.4 Recovery methods

🟡 **Source: consensus across multiple guides**

1. **Stop immediately** the behavior that triggered it (not gradually reduce, but stop completely)
2. Delete duplicate, low-quality posts and posts with too many links/hashtags
3. Revoke authorization for suspicious third-party apps
4. **Wait 48-72 hours** (automatic shadowbans usually lift in this window)
5. Full recovery cycle: **2-14 days**
6. During recovery, keep posting normally, at low frequency and high quality

- Source: [Pixelscan guide](https://pixelscan.net/blog/twitter-shadowban-2025-guide/) | [Tweet Archivist](https://www.tweetarchivist.com/twitter-shadowban-complete-guide-2025) | [Multilogin](https://multilogin.com/blog/twitter-shadow-bans/)

---

## 8. Ads and Organic Growth

### 8.1 Paid vs organic performance

🟡 **Source: WebFX + media reports**

| Metric | Paid promotion | Organic posting |
|--------|----------------|-----------------|
| Average CTR | 1-3% | 0.5-1.5% |
| Premium account reach | — | ~10x that of an ordinary account |
| Engagement on non-Premium link posts | — | 0 (after March 2026) |

### 8.2 Key findings

🟡 **Source: multiple analyses**

- Paid and organic algorithms **run independently**; there is no penalty of "spending money lowers your organic traffic"
- But the structural trend is that organic reach keeps declining (a platform-wide phenomenon, not only X)
- New followers gained through ads **do affect** how later organic posts perform (more followers → more in-network distribution)
- A Premium subscription is essentially the **lowest-cost form of "ad spend"**: the 4x/2x visibility boost far exceeds what ads at an equivalent price would deliver

- Source: [WebFX](https://www.webfx.com/blog/social-media/x-twitter-marketing-benchmarks/) | [Avenue Z](https://avenuez.com/blog/2025-2026-x-twitter-organic-social-media-guide-for-brands/)

---

## 9. The Impact of Community Notes

### 9.1 Effect on post performance

🟢 **Source: University of Washington study (September 2025)**

| Metric | Change after receiving a Community Note |
|--------|-----------------------------------------|
| Reposts | **Down 46%** |
| Likes | **Down 44%** |
| Views | Less affected (the Feed algorithm does not actively downrank posts with Notes) |

### 9.2 Key details

- X does **not** actively reduce distribution of posts with a Community Note at the algorithm level
- The drop comes mainly from **changes in user behavior**: after seeing the Note, users repost and like less
- The **timeliness** of the Note is critical: a Note added after 48 hours has almost no effect (the content has already finished spreading)
- Notes have the biggest effect on **manipulated media** (fake photos/videos)

### 9.3 Implications for creators

🔴 **Speculation/strategy suggestions**

- When posting factual claims that could spark controversy, make sure you have sources
- A Community Note doesn't directly cut algorithm weight, but it **indirectly kills engagement** (reposts -46%)
- A post tagged with a Note keeps its view count, but its spread is cut in half
- Constructive, sourced content is less likely to be tagged

- Source: [University of Washington study](https://www.washington.edu/news/2025/09/18/community-notes-x-false-information-viral/) | [Wikipedia - Community Notes](https://en.wikipedia.org/wiki/Community_Notes)

---

## 10. Core Takeaways for Content Creators

### 10.1 Algorithm optimization priorities (ranked by ROI)

| Priority | Strategy | Basis |
|----------|----------|-------|
| **P0** | Spark conversation and reply to every comment | Conversation reply weight 150x |
| **P0** | Subscribe to Premium | 4x/2x visibility + TweepCred boost + link post visibility |
| **P1** | Ignite engagement in the first 30 minutes | Engagement velocity determines distribution volume |
| **P1** | Write long posts that make people stop and read | Dwell Time weight 20x |
| **P2** | Post on weekdays 9AM-2PM | The data-validated best time window |
| **P2** | Avoid external links (or put them in the replies) | 30-50% reach penalty |
| **P3** | Keep a positive/constructive tone | Grok tone scoring affects distribution |
| **P3** | Keep hashtags to ≤2 | More than 2 triggers a spam flag |

### 10.2 Absolute no-go zones

| Behavior | Consequence |
|----------|-------------|
| Mass following/unfollowing in a short time | 3-month shadowban |
| Using automation tools to fake engagement | Permanent damage to account reputation |
| Frequently posting external links (non-Premium) | Posts become nearly invisible |
| Posting content that gets reported | -369x penalty, content disappears outright |
| Suddenly changing your posting pattern | TweepCred drops |

### 10.3 X's unique advantages (compared with other platforms)

- **The only major platform to open-source its algorithm twice**: you can optimize precisely
- **Friendly to text content**: unlike other platforms, it doesn't force you into video
- **Conversation-driven**: it genuinely rewards deep exchange rather than surface-level engagement
- **Promptable Feeds**: users can customize recommendations, which means high-quality vertical content has long-tail value

---

## Appendix: Source List

### Official / primary sources
- [xai-org/x-algorithm GitHub](https://github.com/xai-org/x-algorithm) — the Grok-version algorithm open-sourced in January 2026
- [twitter/the-algorithm GitHub](https://github.com/twitter/the-algorithm) — the version first open-sourced in 2023
- [Elon Musk's tweet (2025.09)](https://x.com/elonmusk/status/1969081066578149547) — announced the algorithm would become purely AI
- [@XEng tweet (2026.01)](https://x.com/XEng/status/2013471689087086804) — announced the open-sourcing of the new algorithm

### Authoritative media reports
- [TechCrunch: X open sources its algorithm](https://techcrunch.com/2026/01/20/x-open-sources-its-algorithm-while-facing-a-transparency-fine-and-grok-controversies/)
- [Social Media Today: Key ranking factors](https://www.socialmediatoday.com/news/x-formerly-twitter-open-source-algorithm-ranking-factors/759702/)
- [Social Media Today: Grok algorithm shift](https://www.socialmediatoday.com/news/x-formerly-twitter-switching-to-fully-ai-powered-grok-algorithm/803174/)

### Data analysis
- [Buffer: Best content format 2026 (analysis of 45M+ posts)](https://buffer.com/resources/data-best-content-format-social-media/)
- [Buffer: Best time to post (analysis of 1M posts)](https://buffer.com/resources/best-time-to-post-on-twitter-x/)
- [Sprout Social: Twitter algorithm 2026](https://sproutsocial.com/insights/twitter-algorithm/)
- [University of Washington: Community Notes study](https://www.washington.edu/news/2025/09/18/community-notes-x-false-information-viral/)

### In-depth community analysis
- [posteverywhere.ai: source-code walkthrough](https://posteverywhere.ai/blog/how-the-x-twitter-algorithm-works)
- [Typefully: algorithm update analysis](https://typefully.com/blog/x-algorithm-open-source)
- [Circleboom: in-depth TweepCred explainer](https://circleboom.com/blog/tweepcred-what-it-is-why-it-matters-and-how-to-increase-your-score-on-x-twitter/)
- [nibzard: Rust+Python architecture analysis](https://nibzard.github.io/twitter-algorithm-tufte/)
- [ByteByteGo: algorithm architecture diagrams](https://blog.bytebytego.com/p/the-algorithm-that-powers-your-x)
- [Pixelscan: Shadowban guide](https://pixelscan.net/blog/twitter-shadowban-2025-guide/)
- [DeepWiki: x-algorithm repository analysis](https://deepwiki.com/xai-org/x-algorithm)
