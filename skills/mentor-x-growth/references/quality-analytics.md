# Quality Checks + Anti-Patterns + Data Retrospectives + Report Template

> Load as needed: read for Scenario C (content review), Scenario E (account diagnosis), and data retrospectives.

---

## Quality Checklist

When reviewing tweets/Threads already written, check item by item:

### Tweet checks
- [ ] Does the Hook grab attention within 2 lines?
- [ ] Does it answer "who is it for / what is it about / why should they read it"?
- [ ] Is it specific? (numbers, times, names)
- [ ] Can it provoke replies? (not just likes)
- [ ] Is it free of external links? (if one is needed, put it in the first reply)
- [ ] Is the posting time within the target audience's active hours?

### Thread checks
- [ ] Does the first tweet stand on its own and hook the reader?
- [ ] Does it follow the 1/3/1 rhythm?
- [ ] Does every tweet move the content forward? (Rate of Revelation)
- [ ] Is there a TL;DR summary?
- [ ] Is there a clear CTA?
- [ ] Is the length within 8-12 tweets?
- [ ] Does it use bullet points rather than big blocks of text?

### Content strategy checks
- [ ] Is there at least 1 Thread this week?
- [ ] Did you leave high-quality replies in big accounts' comment sections?
- [ ] Is there a CTA that drives traffic to the newsletter?
- [ ] Did you respond to this week's AI hot topics?
- [ ] Is the mix of short tweets and Threads reasonable?

---

## Anti-Patterns and Pitfalls

### Growth traps (don't step in)

1. **Buying followers / follow-for-follow and like-swap groups**: the numbers look good short-term, but TweepCred plummets long-term. The algorithm detects unnatural engagement patterns and downranks you; it isn't worth it
2. **Pure tool-recommendation roundups**: the AI niche is already a red ocean. Posts like "10 AI tools you need" are posted by everyone, with no differentiation. If you do it, add your own test data and unique opinions
3. **Only translating foreign AI news**: zero differentiation. If you do it, add your own take: "why this matters for Chinese developers" or "I tested it, and the actual result was..."
4. **Chasing hot topics until you lose your positioning**: if you piggyback on every trend, followers won't know who you are. Filter the trends: only ride those relevant to your positioning
5. **A hook with no substance**: clickbait works short-term and loses followers long-term. Hormozi says "over-deliver": promise 1, give 3
6. **Posting without replying**: conversation weight is 150x; not replying means giving up the biggest algorithm lever
7. **Threads that run too long without closing**: past 15 tweets, people start dropping off. The sweet spot is 8-12 tweets

### Platform-level risks (stay alert)

- **Overall engagement rate decline**: in 2024-2025, platform-wide engagement on X plunged 48%. It isn't your problem; it's a platform trend
- **Pay-to-play intensifying**: organic reach for non-Premium users keeps shrinking, and posts with external links are close to zero. Premium isn't optional; it's a necessity
- **User migration**: some creators are spreading out to Bluesky/Threads. But for now X is still the main battlefield for AI/tech content

---

## Data Retrospective Guide

### Key metrics (by priority)

| Metric | What to look at | Healthy reference |
|--------|-----------------|-------------------|
| Engagement Rate | Engagements/impressions | >2% good, >5% excellent |
| Reply rate | Replies/impressions | Higher is better (the algorithm weighs it most) |
| Profile Visit rate | Profile visits/impressions | >1% means people want to learn about you |
| Follower growth | Weekly net new followers | Cold-start phase 5-10 per day on average, growth phase 20-50 per day |
| Bookmark rate | Bookmarks/impressions | High bookmarks = high-value content |
| Newsletter traffic | New subscriptions/week | Any is good; keep tracking the conversion rate |

### Retrospective cadence

- **Daily**: glance at yesterday's content data and flag high performers with >500 engagements
- **Weekly**: analyze this week's top 3 tweets, extract commonalities → update the template library
- **Monthly**: review the follower growth curve, content-type distribution, and newsletter growth. Adjust next month's content strategy

### Diagnostic framework (when tweet data is poor)

Check in order:
1. **Algorithm layer**: Is Premium on? Is the posting time right? Is there an external link?
2. **Hook layer**: Is there a curiosity gap in the first 2 lines? Is there a credibility anchor?
3. **Content layer**: Does every tweet move things forward? Is there a 1/3/1 rhythm?
4. **Audience layer**: Do you have enough followers to trigger Engagement Velocity? Borrow traffic from comment sections first

---

## Report HTML Template Requirements

The diagnostic report uses an Economist/newspaper layout style and must include:
- **Visual style**: serif font (Georgia), warm paper-colored background (#f5f0e8), red accent (#C7000A), Grid layout
- **Data visualization**: use ECharts.js (loaded via CDN), including at least a topic distribution chart, a time distribution chart, and an engagement funnel
- **Required sections**:
  1. Banner + Masthead (a one-sentence core finding as the headline)
  2. KPI Grid (4 core metrics as big numbers)
  3. Lead (summary paragraph, italic, with a red left border)
  4. Content ROI analysis (engagement comparison grouped by topic)
  5. Spread funnel (like rate/bookmark rate/retweet rate/reply rate)
  6. Timing analysis (best posting slots, evolution of posting cadence)
  7. Brand narrative (distribution of narrative roles and their engagement performance)
  8. Top 5 action recommendations (numbered red circle + title + body + data evidence)
  9. Footer (data period, sample size, analysis time)
- **Reference implementation**: `user-data/AlchainHust/report_20260406.html`
