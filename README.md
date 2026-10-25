# mentors

An advisory board as Agent Skills: each mentor is a "thinking operating system" (mental models,
decision principles, voice, things they never do, limits) distilled from public sources. Ask a
business or personal question and the `mentors` skill picks the right 1–3 mentors for the domain,
has each of them analyze it, then merges the results into actionable advice.

A Claude Code / Agent Skills advisory board, forked from
[alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) (MIT) and adapted for Sam (Founder & CEO of Avada Group); all skills are written in English, and answers follow the language of the person asking.

## Structure

```
mentors/
├── SKILL.md                     # the "mentors" router: picks mentors, synthesizes advice
└── skills/
    ├── mentors-distill/         # Nuwa: distill a person into a new mentor
    ├── mentor-elon-musk/        # first principles, cost, speed
    ├── mentor-trump/            # negotiation, power, media
    ├── mentor-steve-jobs/       # product, design, focus
    ├── mentor-paul-graham/      # startups, PMF, ideas
    ├── mentor-munger/           # investing, inversion, biases
    ├── mentor-naval/            # building wealth, leverage, life
    ├── mentor-taleb/            # risk, antifragility
    ├── mentor-feynman/          # learning, explaining, scientific thinking
    ├── mentor-karpathy/         # AI engineering
    ├── mentor-ilya-sutskever/   # AI research, scaling
    ├── mentor-zhang-yiming/     # organization, hiring, globalization
    ├── mentor-mrbeast/          # video, YouTube
    ├── mentor-x-growth/         # growth on X/Twitter (topic)
    ├── mentor-sun-yuchen/       # attention-grabbing marketing (ethics warning included)
    └── mentor-tribe-of-mentors/ # the book Tribe of Mentors – Tim Ferriss (topic)
```

## Install (Claude Code)

```bash
git clone https://github.com/samnguyen80/mentors.git ~/mentors
ln -s ~/mentors ~/.claude/skills/mentors
for d in ~/mentors/skills/*/; do ln -s "$d" ~/.claude/skills/$(basename "$d"); done
```

## Usage

```
> Chatty CAC is 120 USD, LTV 400, should we raise the ads budget?   # the router picks the mentors
> Hỏi Munger: có nên mua lại app đối thủ này không?                  # one mentor (ask Munger: should we acquire this competitor's app?)
> Board meeting: should we open a new BU in the Japanese market?     # 4–5 mentors debate
> Tạo mentor Jeff Bezos                                              # mentors-distill (create mentor Jeff Bezos)
```

## Limits

This is a simulation of thinking frameworks from public information, not the figures' real words,
and it is only accurate up to the research date. The `mentor-tribe-of-mentors` set uses only Tim
Ferriss's public sources; the full text of the book (if any) stays on the personal machine and is
not put into the repo.

## Credit & License

Method and the 14 original character research sets: [花叔 (Huashu) / alchaincyf](https://github.com/alchaincyf),
[nuwa-skill](https://github.com/alchaincyf/nuwa-skill), MIT. English adaptation: Sam.
See [LICENSE](LICENSE).
