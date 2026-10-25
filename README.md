# mentors

Hội đồng cố vấn dạng Agent Skill: mỗi mentor là một "hệ điều hành tư duy" (mô hình tư duy,
nguyên tắc quyết định, giọng nói, điều không làm, giới hạn) rút từ nguồn công khai. Hỏi một
vấn đề kinh doanh hay cá nhân, skill `mentors` chọn đúng 1–3 mentor theo lĩnh vực, cho từng
người phân tích, rồi gom thành lời khuyên hành động.

A Claude Code / Agent Skills advisory board, forked from
[alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) (MIT) and adapted to Vietnamese.

## Cấu trúc

```
mentors/
├── SKILL.md                     # router "mentors": chọn mentor, tổng hợp lời khuyên
└── skills/
    ├── mentors-distill/         # Nuwa: chưng cất một người thành mentor mới
    ├── mentor-elon-musk/        # first principles, chi phí, tốc độ
    ├── mentor-trump/            # đàm phán, quyền lực, truyền thông
    ├── mentor-steve-jobs/       # sản phẩm, thiết kế, tập trung
    ├── mentor-paul-graham/      # startup, PMF, ý tưởng
    ├── mentor-munger/           # đầu tư, tư duy ngược, thiên kiến
    ├── mentor-naval/            # làm giàu, đòn bẩy, cuộc đời
    ├── mentor-taleb/            # rủi ro, phản mong manh
    ├── mentor-feynman/          # học, giải thích, tư duy khoa học
    ├── mentor-karpathy/         # AI engineering
    ├── mentor-ilya-sutskever/   # nghiên cứu AI, scaling
    ├── mentor-zhang-yiming/     # tổ chức, tuyển người, toàn cầu hoá
    ├── mentor-mrbeast/          # video, YouTube
    ├── mentor-x-growth/         # tăng trưởng X/Twitter (chủ đề)
    ├── mentor-sun-yuchen/       # marketing gây chú ý (có cảnh báo đạo đức)
    └── mentor-tribe-of-mentors/ # sách Tribe of Mentors – Tim Ferriss (chủ đề)
```

## Cài (Claude Code)

```bash
git clone https://github.com/samnguyen80/mentors.git ~/mentors
ln -s ~/mentors ~/.claude/skills/mentors
for d in ~/mentors/skills/*/; do ln -s "$d" ~/.claude/skills/$(basename "$d"); done
```

## Dùng

```
> Chatty CAC 120 USD, LTV 400, có nên tăng ngân sách ads không?   # router tự chọn mentor
> Hỏi Munger: có nên mua lại app đối thủ này không?               # một mentor
> Board meeting: có nên mở BU mới ở thị trường Nhật?               # 4–5 mentor tranh luận
> Tạo mentor Jeff Bezos                                           # mentors-distill
```

## Giới hạn

Đây là mô phỏng khung tư duy từ thông tin công khai, không phải lời thật của các nhân vật,
và chỉ đúng tới thời điểm nghiên cứu. Bộ `mentor-tribe-of-mentors` chỉ dùng nguồn công khai
của Tim Ferriss; toàn văn sách (nếu có) để ở máy cá nhân, không đưa vào repo.

## Credit & License

Phương pháp và 14 bộ nghiên cứu nhân vật gốc: [花叔 / alchaincyf](https://github.com/alchaincyf),
[nuwa-skill](https://github.com/alchaincyf/nuwa-skill), MIT. Bản chuyển thể tiếng Việt: Sam.
Xem [LICENSE](LICENSE).
