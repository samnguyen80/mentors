---
name: mentors-distill
description: |
  Chưng cất tư duy một người thành mentor chạy được: nhập tên người, chủ đề, hoặc chỉ một nhu cầu mơ hồ, skill tự nghiên cứu sâu, rút khung tư duy và sinh ra skill `mentor-<slug>` tiếng Việt.
  Hai lối vào: (1) có tên người rõ ràng thì chưng cất thẳng; (2) nhu cầu mơ hồ thì chẩn đoán, đề xuất người phù hợp, rồi chưng cất.
  Kích hoạt khi anh nói: "tạo mentor", "thêm mentor", "chưng cất <tên>", "distill <tên>", "làm mentor <tên>", "nuwa", "cập nhật mentor <tên>".
  Cũng kích hoạt với nhu cầu mơ hồ: "em muốn ra quyết định tốt hơn", "có cách nghĩ nào giúp anh...", "anh cần một cố vấn tư duy".
  Distill a person's thinking into a runnable Vietnamese mentor skill (`mentor-<slug>`): deep research, mental-model extraction, 3-layer verification, honest limits.
  English triggers: "distill [person]", "create a mentor", "add a mentor", "nuwa", "update mentor [person]", "how does [person] think", "I need a thinking advisor".
metadata:
  author: "花叔 (Huashu)"
  homepage: "https://github.com/alchaincyf"
  repository: "https://github.com/alchaincyf/nuwa-skill"
  license: "MIT"
  version: "1.0.0"
  adapted_by: "Sam (github.com/samnguyen80/mentors)"
---

# Mentors Distill · Thuật chưng cất mentor

> "Phần không viết ra được mới là hào phòng thủ thật sự của anh." Nhưng phần viết ra được cũng đã đủ mạnh.

Skill này chuyển thể từ Nuwa (tác giả gốc 花叔, giấy phép MIT, repo gốc ghi trong metadata). Phương pháp giữ nguyên; đầu ra đổi thành mentor tiếng Việt nằm trong repo `samnguyen80/mentors`.

## Triết lý cốt lõi

Mentors-distill không sao chép một con người, mà **chưng cất khung tư duy**.

Một mentor tốt là một hệ điều hành nhận thức chạy được:
- Người này dùng **mô hình tư duy** nào để nhìn thế giới? (lăng kính)
- Người này dùng **nguyên tắc ra quyết định** nào để phán đoán? (luật trực giác)
- Người này **biểu đạt** thế nào? (DNA)
- Người này **tuyệt đối không** làm gì? (anti-pattern)
- Skill này **không làm được** gì? (ranh giới trung thực)

**Phân biệt then chốt**: nắm HOW họ nghĩ, không phải WHAT họ đã nói.

---

## Quy trình thực hiện

### Phase 0: Phân luồng lối vào

Nhận đầu vào của người dùng, trước hết xác định thuộc đường nào:

| Đầu vào | Đường | Ví dụ |
|---------|-------|-------|
| Tên người / chủ đề rõ ràng | **Đường trực tiếp** → Phase 0A | "chưng cất Munger", "làm mentor Feynman" |
| Nhu cầu / băn khoăn mơ hồ | **Đường chẩn đoán** → Phase 0B | "anh muốn ra quyết định tốt hơn", "có cách nghĩ nào giúp anh nhìn ra bản chất kinh doanh" |

---

### Phase 0A: Làm rõ yêu cầu (đường trực tiếp)

Nhận được tên rõ ràng thì xác nhận:

1. **Người / chủ đề này là ai**: bảo đảm hiểu đúng
2. **Hướng tập trung** (tuỳ chọn): chân dung toàn diện hay tập trung một chiều?
3. **Mục đích**: cố vấn tư duy? tham chiếu ra quyết định? nhập vai?
4. **Tạo mới hay cập nhật**: mentor này đã có chưa? (kiểm tra thư mục `/Volumes/SamDisk/sources/mentors/skills/` xem có `mentor-<slug>/` chưa)
5. **Tư liệu local**: "Anh có sẵn tư liệu gốc về người này không? Ví dụ PDF sách, transcript bài nói / phỏng vấn, phụ đề video, blog xuất ra. Có thì đưa thẳng cho tôi, chất lượng cao hơn nhiều so với tìm trên mạng."
6. **Mức chưng cất**: nói rõ cho người dùng mức chi phí và xác nhận mức. Chưng cất đầy đủ là tác vụ dài, nhiều agent, nhiều vòng tìm kiếm; một lần chạy với model hàng đầu có thể tiêu hàng chục USD (có ca người dùng thật). Phải nói rõ TRƯỚC khi chạy:

| Mức | Quy mô nghiên cứu | Khi nào dùng | Chi phí |
|-----|-------------------|--------------|---------|
| Nhanh | 3 chiều (tác phẩm + đối thoại + biểu đạt), mỗi chiều tối đa 5 nguồn | Muốn thử hiệu quả trước / nhân vật ít tên tuổi / ngân sách hạn chế | Khoảng 1/3 mức chuẩn |
| Chuẩn (mặc định) | Đủ 6 chiều | Phần lớn trường hợp | Trung bình; đổi sang model nhẹ hơn thì giảm đáng kể |
| Sâu | 6 chiều + tải toàn bộ tư liệu gốc (sách / phụ đề / bài dài lưu trữ) | Mentor tinh phẩm định dùng lâu dài | Cao nhất |

Người dùng chỉ nói "làm XX" mà không có thêm thông tin → mặc định chân dung toàn diện + cố vấn tư duy + không có tư liệu local (đi tìm trên mạng) + mức chuẩn, triển khai luôn.

**Xác nhận không được chặn việc giao sản phẩm**: câu hỏi nào có thể đặt giá trị mặc định thì đặt giá trị mặc định; nếu sản phẩm bước tiếp theo (đề cương phỏng vấn, kế hoạch thực hiện, v.v.) không phụ thuộc câu trả lời, giao sản phẩm trước rồi để người dùng chỉnh. Đừng để giá trị có sẵn kẹt sau câu hỏi.
Người dùng cung cấp tư liệu local → đánh dấu **chế độ tư liệu local**, chiến lược thu thập của Phase 1 sẽ điều chỉnh tương ứng.

Xác nhận xong → nhảy sang Phase 0.5.

---

### Phase 0B: Chẩn đoán nhu cầu (đường mơ hồ)

Người dùng chưa biết nên chưng cất ai, chỉ có nhu cầu hoặc băn khoăn. Lúc này việc của skill là **từ nhu cầu suy ngược ra đối tượng chưng cất phù hợp nhất**.

#### Bước 1: Định vị nhu cầu

Dùng 1-2 câu hỏi thêm để định vị chiều nhu cầu cốt lõi:

| Chiều nhu cầu | Cách nói điển hình | Hướng khung tư duy |
|---------------|--------------------|--------------------|
| Quyết định và phán đoán | "làm sao ra quyết định tốt hơn", "toàn chọn sai", "tê liệt vì phân tích" | Đa mô hình tư duy, tư duy đảo ngược, tư duy xác suất |
| Biểu đạt và viết | "muốn nói rõ chuyện phức tạp", "bài viết không ai đọc", "viết nhạt" | Đơn giản hoá kiểu Feynman, tư duy kể chuyện, năng lực so sánh |
| Khởi nghiệp và kinh doanh | "muốn làm indie", "không thông mô hình kinh doanh", "không tìm ra PMF" | Nguyên lý đầu tiên, tư duy đòn bẩy, kiềm chế sản phẩm |
| Giảng dạy và truyền đạt | "giảng không ai nghe", "học trò không hiểu", "truyền tri thức kém hiệu quả" | Từ cái đã biết đến cái chưa biết, dạy bằng ẩn dụ, tri thức tối thiểu cần thiết |
| Tư duy phản biện | "hay bị lừa", "muốn nhận ra lời nói thiếu đáng tin", "không nhìn ra bản chất" | Tư duy phản chứng, góc nhìn tiến hoá, nhận diện thiên kiến nhận thức |
| Sáng tạo nội dung | "làm video không có traffic", "không biết quay gì", "nội dung không có nét riêng" | Kỹ thuật chú ý, thử nghiệm lặp, tâm lý khán giả |
| Chiến lược đời sống | "mông lung hướng nghề", "luôn thiếu thời gian", "lo âu" | Chủ nghĩa dài hạn, chọn đòn bẩy, tư duy lãi kép |
| Rủi ro và bất định | "ứng phó thiên nga đen thế nào", "đầu tư toàn lỗ", "quá bảo thủ / quá liều" | Phản mong manh, chiến lược lồi, quản trị rủi ro đuôi |
| Thiết kế và sản phẩm | "trải nghiệm người dùng tệ", "sản phẩm không có nét riêng", "không biết bớt" | Tối giản, mô hình tâm lý người dùng, ràng buộc sinh sáng tạo |
| Hài hước và sức biểu đạt | "nói chuyện nhạt", "muốn nội dung vui hơn", "quá nghiêm" | Đối lập phi lý, phá kỳ vọng, uy quyền kiểu tự giễu |

Nguyên tắc hỏi thêm:
- Tối đa 2 vòng, đừng biến thành bảng khảo sát
- Nếu người dùng đã nói đủ rõ thì không hỏi thêm, đề xuất luôn
- Mục đích hỏi thêm là phân biệt các chiều giống nhau (ví dụ "quyết định" là quyết định kinh doanh hay quyết định đời sống?)

**Ví dụ hội thoại** (nhịp chẩn đoán):

```
Người dùng: Anh luôn thấy mình ra quyết định chậm, nghĩ tới nghĩ lui cuối cùng vẫn chọn sai

Mentors-distill: Quyết định mà anh nói chủ yếu là tình huống nào? Quyết định kinh doanh / đầu tư, hay lựa chọn nghề nghiệp / hướng đi cuộc đời?

Người dùng: Chủ yếu kinh doanh, ví dụ có làm sản phẩm này không, có nhận hợp tác này không

Mentors-distill: Hiểu rồi, nhu cầu cốt lõi của anh là "khi thông tin chưa đầy đủ vẫn đưa ra phán đoán kinh doanh chất lượng cao, nhanh".
Tôi đề xuất 3 ứng viên:
[hiển thị ứng viên đề xuất...]
```

Chú ý nhịp: một vòng hỏi để định vị tình huống → xác nhận nhu cầu → đề xuất thẳng. Không hỏi tới vòng thứ ba.

#### Bước 2: Đề xuất ứng viên

Dựa trên chiều nhu cầu, đề xuất 2-3 phương án. Ứng viên có thể là người, cũng có thể là chủ đề.

**Trước hết phân định: mentor theo người hay skill theo chủ đề?**
- Nhu cầu chỉ tới một cách nghĩ cụ thể → mentor theo người (chưng cất khung tư duy của một người)
- Nhu cầu chỉ tới phương pháp luận của một lĩnh vực → skill theo chủ đề (tổng hợp nhiều góc nhìn, xem "Tình huống đặc biệt > Skill theo chủ đề")
- Chưa chắc → trong đề xuất đưa cả hai loại, để người dùng chọn

**Nguồn A: mentor đã có sẵn**
Đọc bảng "Danh sách mentor" ở `/Volumes/SamDisk/sources/mentors/SKILL.md` (và/hoặc quét `/Volumes/SamDisk/sources/mentors/skills/mentor-*/SKILL.md`, đọc description của từng skill), khớp với nhu cầu người dùng. Mentor có sẵn dùng ngay, không cần chưng cất lại. Nếu kết quả quét trống (chưa có mentor nào), bỏ bước này, chỉ đề xuất từ nguồn B.

**Nguồn B: ứng viên cần chưng cất mới**
Dựa vào cột "Hướng khung tư duy" trong bảng chiều nhu cầu, khớp với người hoặc chủ đề liên quan nhất. Khi đề xuất phải nói rõ: khung tư duy nào của người này giải quyết được vấn đề cụ thể của người dùng.

Định dạng hiển thị mỗi ứng viên:

```
### Ứng viên 1: [Tên người / chủ đề]  ⚡Đã có mentor / 🆕Cần chưng cất

**Lăng kính cốt lõi**: [Cách nhìn thế giới riêng của người này, một câu]
**Vì sao hợp với anh**: [Khớp thẳng với nhu cầu của người dùng, nói rõ logic khớp]
**Giới hạn**: [Điểm mù của góc nhìn này, vấn đề nào họ không giúp được]
```

Nguyên tắc đề xuất:
- Không quá 3 ứng viên, khó chọn còn tệ hơn không có lựa chọn
- Mentor đã có hiển thị trước (dùng ngay, chi phí bằng không)
- Các ứng viên phải khác nhau, đừng đề xuất 3 người giống nhau
- Phải nói rõ giới hạn; không có khung tư duy vạn năng
- Đề xuất phải cụ thể tới mức "mô hình tư duy nào của người này" khớp nhu cầu, không chỉ khen chung chung "ông ấy rất giỏi"

#### Bước 3: Người dùng chọn

- Chọn mentor đã có → kích hoạt thẳng mentor đó, xong việc
- Chọn ứng viên chưng cất mới → vào Phase 0A xác nhận chi tiết → Phase 0.5 bắt đầu chưng cất
- Không hài lòng → quay lại Bước 1 tiếp tục khám phá, hoặc người dùng tự đưa ra người mới

### Phase 0.5: Tạo thư mục mentor

**Làm ngay sau khi nhận xác nhận**, trước khi nghiên cứu. Thư mục đích của mentor nằm trong repo mentors (bản clone chính trên máy):

```
/Volumes/SamDisk/sources/mentors/skills/mentor-<slug>/
├── SKILL.md                          # Sản phẩm cuối (tiếng Việt, có mục "Người hỏi")
└── references/
    ├── research/                     # Kết quả nghiên cứu của từng Agent (bắt buộc lưu)
    │   ├── 01-writings.md            # Tác phẩm và tư duy hệ thống
    │   ├── 02-conversations.md       # Đối thoại dài và tư duy ứng khẩu
    │   ├── 03-expression-dna.md      # Biểu đạt vụn và DNA phong cách
    │   ├── 04-external-views.md      # Góc nhìn của người khác và phê bình
    │   ├── 05-decisions.md           # Hồ sơ quyết định và hành động
    │   └── 06-timeline.md            # Dòng thời gian nhân vật
    └── sources/                      # Tư liệu gốc (người dùng đưa + tải từ mạng)
        ├── books/
        ├── transcripts/
        └── articles/
```

`<slug>` viết thường, nối bằng dấu gạch ngang, không dấu (ví dụ `elon-musk`, `paul-graham`). Frontmatter `name` của SKILL.md là `mentor-<slug>`.

**Kiểm tra hoàn tất** (tự động thực hiện):
- [ ] Đã tạo thư mục
- [ ] Nếu là nhân vật Trung Quốc: chiến lược nguồn chuyển sang video gốc trên Bilibili / podcast Xiaoyuzhou / truyền thông Trung văn có uy tín ưu tiên (Zhihu và WeChat Official Accounts luôn bị loại, xem danh sách đen nguồn)
- [ ] Nếu là chế độ cập nhật: đã đọc SKILL.md hiện có, đánh dấu thông tin nào cần làm mới
- [ ] Nếu người dùng đưa tư liệu local: sao chép / di chuyển tư liệu vào thư mục con tương ứng của `sources/`, đánh dấu **chế độ tư liệu local**

**Quy tắc then chốt**:
- Mỗi subagent bắt buộc ghi kết quả nghiên cứu vào file md tương ứng. Nghiên cứu không lưu file coi như chưa làm.
- **Mọi file nghiên cứu phải nằm bên trong thư mục skill** (`references/research/`), tuyệt đối không lưu vào thư mục phân tích bên ngoài. Skill phải tự chứa: sao chép cả thư mục skill là dùng độc lập được, không phụ thuộc file bên ngoài. Đây là nguyên tắc cốt lõi để phân phối.

---

### Phase 1: Thu thập thông tin đa nguồn (Agent Swarm song song)

#### Xác định chế độ: tư liệu local hay tìm trên mạng

Dựa vào kết quả Phase 0A, chọn chiến lược thu thập:

| Chế độ | Điều kiện | Chiến lược |
|--------|-----------|------------|
| **Chỉ tìm trên mạng** (mặc định) | Người dùng không có tư liệu local | Cả 6 Agent đều tìm trên mạng, quy trình đầy đủ |
| **Ưu tiên tư liệu local** | Người dùng cung cấp PDF / transcript / phụ đề / bài viết | Phân tích tư liệu local trước, tìm mạng chỉ để bổ sung |
| **Chỉ tư liệu local** | Người dùng nói rõ "chỉ dùng tư liệu tôi đưa" hoặc chưng cất người không phải nhân vật công chúng | Chỉ phân tích tư liệu local, không tìm mạng |

**Logic thực hiện chế độ ưu tiên tư liệu local**:

1. **Đọc tư liệu local trước**: phân loại file người dùng đưa theo 6 chiều (một cuốn sách có thể phủ nhiều chiều: tác phẩm + đối thoại + biểu đạt)
2. **Xác định khoảng trống thông tin**: tư liệu local phủ chiều nào? chiều nào thiếu hoặc mỏng?
3. **Tìm mạng có định hướng**: chỉ khởi động Agent tìm mạng cho các chiều còn thiếu; chiều đã đủ tư liệu local thì bỏ qua
4. **Đánh dấu nguồn**: trong file nghiên cứu phân biệt rõ "từ tư liệu người dùng đưa" với "từ tìm kiếm trên mạng"

**Các dạng tư liệu local thường gặp và cách xử lý**:

| Loại tư liệu | Cách xử lý | Chiều phủ |
|--------------|------------|-----------|
| PDF sách | Đọc thẳng, rút luận điểm cốt lõi | Tác phẩm (01), biểu đạt (03) |
| Transcript bài nói / phỏng vấn | Phân tích kiểu hỏi đáp và phản ứng ứng khẩu | Đối thoại (02), biểu đạt (03) |
| Phụ đề video SRT | Xử lý như transcript | Đối thoại (02), biểu đạt (03) |
| Blog / newsletter xuất ra | Rút quan điểm có hệ thống | Tác phẩm (01), biểu đạt (03) |
| Dữ liệu mạng xã hội xuất ra | Phân tích kiểu biểu đạt vụn | Biểu đạt (03) |
| Tài liệu nội bộ / memo | Phân tích logic ra quyết định | Quyết định (05) |
| Ghi chú người dùng tự chỉnh lý | Làm nguồn thứ cấp để đối chiếu | Tuỳ nội dung cụ thể |

**Ưu thế chất lượng của tư liệu local**: tư liệu gốc người dùng đang có (nhất là sách nguyên bản, phỏng vấn dài nguyên văn) thường chất lượng cao hơn nhiều so với tin thứ cấp tìm trên mạng. Trong thứ tự ưu tiên nguồn, tư liệu gốc do người dùng cung cấp có trọng số cao nhất.

---

Dưới đây là phân công tác vụ chuẩn của 6 Agent (chế độ chỉ tìm mạng, hoặc tìm bổ sung cho chiều còn thiếu ở chế độ tư liệu local):

Khởi động 6 subagent song song, mỗi cái phụ trách một chiều thông tin.

#### Phân công tác vụ của 6 Agent

| Agent | Mục tiêu tìm | Trọng tâm rút ra | File đầu ra |
|-------|--------------|------------------|-------------|
| 1 Tác phẩm | Sách, bài dài, luận văn, newsletter | Luận điểm lặp đi lặp lại (≥3 lần = niềm tin thật), thuật ngữ tự đặt, danh sách sách giới thiệu | `01-writings.md` |
| 2 Đối thoại | Podcast, video dài, AMA, phỏng vấn sâu | Cách trả lời khi bị hỏi dồn, so sánh ứng khẩu, khoảnh khắc đổi lập trường, câu hỏi từ chối trả lời | `02-conversations.md` |
| 3 Biểu đạt | Twitter/X, Weibo, bài ngắn | Từ và câu hay dùng, lập trường gây tranh cãi, kiểu hài hước, tranh luận công khai | `03-expression-dna.md` |
| 4 Người khác | Phân tích của người khác, bình luận sách, phê bình, tiểu sử | Mẫu hình quan sát từ bên ngoài, phê bình và tranh cãi, so với đồng nghiệp | `04-external-views.md` |
| 5 Quyết định | Quyết định lớn, bước ngoặt, hành vi gây tranh cãi | Bối cảnh và logic quyết định, suy ngẫm sau sự việc, ca lời nói và việc làm nhất quán / không nhất quán | `05-decisions.md` |
| 6 Dòng thời gian | Toàn bộ dòng thời gian từ khi sinh ra / ra mắt đến nay | Cột mốc then chốt, bước ngoặt tư tưởng, **động thái 12 tháng gần nhất** (chống lỗi thời) | `06-timeline.md` |

#### Yêu cầu cứng với mỗi Agent
- Kết quả nghiên cứu bắt buộc ghi vào `references/research/0X-xxx.md`
- Ghi rõ nguồn và độ tin cậy (sơ cấp > thứ cấp > suy đoán)
- Phân biệt "ông ấy đã nói" vs "người khác nói về ông ấy" vs "tôi suy luận"
- Gặp mâu thuẫn thì giữ nguyên mâu thuẫn, đừng hoà giải qua loa

#### Mẫu prompt cho Agent

Khi spawn subagent, giao việc theo cấu trúc sau (lấy Agent 1 Tác phẩm làm ví dụ):

```
Nhiệm vụ của bạn: nghiên cứu tác phẩm và các bài dài có hệ thống của [tên người].

Hướng tìm:
- Sách người này đã xuất bản (tên sách, luận điểm cốt lõi, năm xuất bản)
- Newsletter / blog / luận văn dài
- Luận điểm lặp lại ≥3 lần (đây là niềm tin thật)
- Thuật ngữ và khái niệm tự đặt
- Danh sách sách giới thiệu (lộ ra phả hệ trí tuệ)

Yêu cầu đầu ra:
- Ghi vào [thư mục skill]/references/research/01-writings.md
- Mỗi thông tin ghi URL nguồn và độ tin cậy
- Phân biệt sơ cấp (do người này viết) vs thứ cấp (người khác tóm tắt)
- Gặp mâu thuẫn thì ghi lại luôn, không hoà giải

Danh sách đen nguồn: không dùng Zhihu, WeChat Official Accounts, Baidu Baike.
```

5 Agent còn lại điều chỉnh hướng tìm và tên file đầu ra theo cùng cấu trúc.

#### Công cụ hỗ trợ (nếu có)

Đường dẫn script bên dưới: `<MD>` = `/Volumes/SamDisk/sources/mentors/skills/mentors-distill`.

- Sách: tìm và tải bản người dùng có quyền sử dụng (đã mua, thư viện, tài liệu mở) → lưu vào `sources/books/`
- Lấy phụ đề video (đã có sẵn script, gọi thẳng):
  - **Bước 1 tải phụ đề**: `bash <MD>/scripts/download_subtitles.sh <YouTube_URL> [thư mục đầu ra]`
    - Tự ưu tiên phụ đề do người tạo (tiếng Anh → tiếng Việt) → phụ đề tự sinh (Anh → Việt → Trung)
    - Xuất file SRT/VTT vào thư mục chỉ định
  - **Bước 2 làm sạch thành văn bản thuần**: `python3 <MD>/scripts/srt_to_transcript.py <input.srt> [output.txt]`
    - Bỏ timestamp, số thứ tự, thẻ HTML, dòng lặp liên tiếp
    - Xuất transcript sạch, đọc được → lưu vào `sources/transcripts/`
  - Người dùng đưa file video local (không có phụ đề): dùng skill phiên âm video (ví dụ `gemini-video`) nếu máy có cài
- Podcast: tìm các trang transcript (podcastnotes.org, v.v.)
- Tạo bản tóm tắt nghiên cứu (dùng cho Phase 1.5): `python3 <MD>/scripts/merge_research.py <thư mục skill>`
  - Tự quét `references/research/01-06.md`, thống kê số nguồn, tỷ lệ sơ cấp / thứ cấp, phát hiện chính
  - Xuất bảng markdown cho điểm kiểm tra Phase 1.5, khỏi thống kê tay
- Tự kiểm chất lượng (dùng cho Phase 4): `python3 <MD>/scripts/quality_check.py <đường dẫn SKILL.md>`
  - Tự kiểm 6 tiêu chuẩn đạt: số mô hình tư duy, giới hạn, DNA biểu đạt, ranh giới trung thực, giằng co nội tại, tỷ lệ nguồn sơ cấp
  - Xuất PASS/FAIL từng mục và tổng kết

#### Tận dụng các skill lấy thông tin đã cài

Trước khi Phase 1 khởi động, **chủ động quét danh sách skill đang có** (thư mục `~/.claude/skills/`) xem có skill nào dùng được cho việc lấy thông tin. Nếu có, ưu tiên gọi trong nghiên cứu, ổn định và hiệu quả hơn WebSearch:

| Skill đã cài | Công dụng | Tình huống gọi |
|--------------|-----------|----------------|
| `gemini-video` | Phân tích file video local, rút transcript | Người dùng đưa video nhưng chưa có phụ đề |
| `web-article-reader` | Đọc chính xác toàn văn bài trên web | Tìm được URL bài quan trọng, cần rút chính xác thay vì dựa vào tóm tắt tìm kiếm |
| `agent-reach` | Lấy thông tin đa kênh (17 nền tảng) | Cần thông tin từ X / Reddit / YouTube, v.v. |
| skill nghiên cứu sâu có cấu trúc (ví dụ `deep-research`) | Nghiên cứu chuyên sâu có cấu trúc | Cần đào sâu một chiều thay vì rải rộng |
| `pdf` | Đọc PDF sách / luận văn | Người dùng đưa tư liệu gốc dạng PDF |

Bảng trên chỉ là gợi ý: skill nào không cài thì bỏ qua, dùng WebSearch / WebFetch.

**Cách thực hiện**: khi spawn subagent, báo cho agent tên và công dụng các skill dùng được, để agent gọi theo nhu cầu trong lúc nghiên cứu. Cách này hiệu quả hơn nhiều so với để agent tự mày mò với WebSearch.

#### Thứ tự ưu tiên nguồn

| Loại nguồn | Lộ ra điều gì | Trọng số |
|------------|---------------|----------|
| **Tư liệu gốc người dùng cung cấp** | Nguyên văn đầy đủ, chưa qua lọc thứ cấp | **Cao nhất+** |
| Tác phẩm của chính người đó | Tư duy có hệ thống | Cao nhất |
| Đối thoại / phỏng vấn dài | Quá trình tư duy ứng khẩu | Cao nhất |
| Hồ sơ quyết định thực tế | Hành vi thật vs lời tuyên bố | Cao nhất |
| Mạng xã hội | Phong cách biểu đạt, phản ứng tức thời | Trung bình |
| Đánh giá của người khác | Góc nhìn bên ngoài, điểm mù | Trung bình |
| Thuật lại thứ cấp | Tham khảo nhưng cần kiểm chứng | Thấp |

#### Danh sách đen nguồn (luôn loại trừ)

- **Zhihu**: viết lại nhiều, thông tin sai lệch cao, không dùng làm nguồn cho bất kỳ chiều nào
- **WeChat Official Accounts**: hệ sinh thái đóng, không kiểm chứng được, nhiều thuật lại thứ cấp, không dùng làm nguồn
- **Baidu Baike / Baidu Zhidao**: thông tin cũ và không đáng tin

Kênh Trung văn chỉ nhận truyền thông có uy tín: 36Kr, Geekpark, LatePost, Caixin, Yicai, Huxiu, Sspai, Jiqizhixin, v.v. Phỏng vấn nhân vật có thể dùng nền tảng podcast (Xiaoyuzhou, Ximalaya audio gốc) và video gốc trên Bilibili (không phải kênh đăng lại video của người khác).

#### Chế độ thất bại và đường hạ cấp (bảng if-then tra nhanh)

Chưng cất là tác vụ dài + nhiều agent + cần mạng, ba dòng đầu của bảng dưới đều đã xảy ra với người dùng thật (có GitHub issue chứng thực). Mỗi dòng thực hiện theo "điều kiện kích hoạt → sửa tuyến đầu → vẫn thất bại thì phương án lót":

| Điều kiện kích hoạt | Sửa tuyến đầu | Vẫn thất bại thì phương án lót |
|---------------------|---------------|-------------------------------|
| Môi trường chạy không hỗ trợ subagent song song / tác vụ nền (một số runtime treo chờ ở Phase 1) | 6 tác vụ nghiên cứu hạ xuống **chạy tuần tự**: xong cái nào lưu ngay cái đó, cấm treo chờ thông báo nền | Một agent đơn chạy 6 vòng nghiên cứu, mỗi vòng chỉ làm một chiều và lưu ngay |
| Cửa sổ ngữ cảnh không đủ (một lần chưng cất đầy đủ có thể tích luỹ 500k+ token, model cửa sổ 200k không chạy hết) | Chạy tiếp theo Phase: cuối mỗi Phase ghi trạng thái vào `references/research/`, phiên mới khôi phục từ file (chính các file nghiên cứu là điểm dừng) | Model cửa sổ 200k chia 3 phiên: Phase 0-1 / Phase 1.5-2.5 / Phase 3-5, đầu mỗi phiên đọc các file đã lưu |
| Chi phí vượt kiểm soát (người dùng không lường trước tác vụ dài tiêu token) | Xác nhận mức chưng cất ở Phase 0A chính là hàng rào: trước khi chạy báo mức chi phí, để người dùng chọn mức | Người dùng dừng giữa chừng → các file nghiên cứu đã lưu là sản phẩm trung gian giao được, lần sau chạy tiếp không phải làm lại |
| Một Agent quá thời gian (tìm 5 phút không có kết quả đáng giá) | Không chờ, đi tiếp, Phase 2 đánh dấu "thiếu thông tin" | Trong ranh giới trung thực nói rõ chiều đó yếu |
| Công cụ tìm kiếm như WebSearch không dùng được | Đổi sang công cụ tương đương môi trường có (fetch / công cụ trình duyệt / skill lấy thông tin đã cài) | Chuyển sang chế độ chỉ tư liệu local, hướng người dùng cung cấp tư liệu |
| Nguồn khan hiếm (<10 nguồn dùng được) | Nhắc người dùng ngay ở Phase 0.5, hạ kỳ vọng (giảm mô hình tư duy còn 2-3) | Tăng dung lượng ranh giới trung thực, đánh dấu phần suy đoán |
| Kết quả các Agent xung đột | Giữ mâu thuẫn, bản thân mâu thuẫn là tín hiệu có giá trị | Thu vào mục "giằng co nội tại" |

**Quy tắc then chốt**: thà sinh ra một skill 60 điểm ghi trung thực các giới hạn, còn hơn sinh ra một skill 90 điểm trông hoàn hảo nhưng thực chất đang bịa.

### Phase 1.5: Điểm kiểm tra rà soát nghiên cứu

**🔴 CHECKPOINT · Khi mọi Agent xong, dừng lại hiển thị tóm tắt chất lượng nghiên cứu**:

```
┌──────────────────┬──────────┬──────────────────────────┐
│ Agent            │ Số nguồn │ Phát hiện chính          │
├──────────────────┼──────────┼──────────────────────────┤
│ 1 Tác phẩm       │ 8 bài    │ Luận điểm lõi: phản mong manh, ... │
│ 2 Đối thoại      │ 5 đoạn   │ Đổi lập trường: sau 2020... │
│ 3 Biểu đạt       │ 120 mục  │ Từ hay dùng: "skin in the..." │
│ 4 Người khác     │ 6 bài    │ Phê bình chính: ...      │
│ 5 Quyết định     │ 4 cái    │ Quyết định then chốt: ...│
│ 6 Dòng thời gian │ Đầy đủ   │ Mới nhất: tháng 3/2026...│
├──────────────────┼──────────┼──────────────────────────┤
│ Điểm mâu thuẫn   │ 2 chỗ    │ Agent1 nói X, Agent4 nói Y│
│ Chiều thiếu tin  │ Không    │                          │
└──────────────────┴──────────┴──────────────────────────┘
```

Người dùng xác nhận chất lượng nghiên cứu ổn → vào Phase 2.
Người dùng thấy chiều nào chưa đủ → nghiên cứu bổ sung rồi mới tiếp tục.

Ý nghĩa của điểm kiểm tra này: chất lượng nghiên cứu quyết định trần của skill cuối. Rác vào rác ra, chặn ở đây rẻ hơn nhiều so với làm lại ở Phase 4.

---

### Phase 2: Chưng cất khung (Synthesis)

Gộp tư liệu của 6 Agent xong, thực hiện chưng cất có cấu trúc. Trước hết đọc `references/extraction-framework.md` để lấy phương pháp kiểm định ba lớp cho mô hình tư duy (tái hiện xuyên lĩnh vực, sức sinh, tính độc quyền), bảo đảm chất lượng chưng cất.

#### 2.1 Rút mô hình tư duy (3-7 cái)

**Các bước thao tác**:

1. **Quét**: đọc lần lượt `01-writings.md` đến `05-decisions.md`, liệt kê mọi luận điểm ứng viên (quan điểm người này lặp lại, thuật ngữ tự đặt, chủ trương cốt lõi). Thường được 15-30 ứng viên
2. **Lọc bằng kiểm định ba lớp**: với mỗi ứng viên thực hiện (chi tiết xem `references/extraction-framework.md`):
   - Tái hiện xuyên lĩnh vực: xuất hiện trong ≥2 lĩnh vực / chủ đề khác nhau?
   - Sức sinh: suy ra được lập trường của người này với vấn đề mới?
   - Tính độc quyền: không phải mọi người thông minh đều nghĩ vậy?
   - Qua cả ba lớp → mô hình tư duy; chỉ qua 1-2 lớp → hạ xuống nguyên tắc ra quyết định; 0 lớp → bỏ
3. **Xếp hạng chọn lọc**: xếp theo độ mạnh của tính độc quyền (càng độc đáo càng đứng trước), lấy top 3-7. Thà ít còn hơn nhiều: 3 mô hình sâu sắc tốt hơn nhiều so với 10 nguyên tắc nông
4. **Định dạng ghi**: mỗi mô hình ghi tên, mô tả một câu, bằng chứng nguồn (≥2 tình huống), cách ứng dụng, giới hạn

#### 2.2 Rút nguyên tắc ra quyết định (5-10 điều)

= Luật nhanh người này dùng khi phán đoán. Có thể diễn đạt thành "nếu X thì Y", có ví dụ cụ thể làm chỗ dựa.

#### 2.3 Phân tích DNA biểu đạt

| Chiều | Nội dung rút ra |
|-------|-----------------|
| Ưa thích câu | Câu dài / ngắn, hỏi / khẳng định, mật độ so sánh |
| Đặc trưng từ vựng | Từ hay dùng, thuật ngữ riêng, từ kiêng kỵ |
| Nhịp | Kết luận trước hay dẫn dắt trước, cách chuyển ý |
| Cách hài hước | Châm biếm / tự giễu / phi lý / hài lạnh / không hài hước |
| Biểu đạt độ chắc chắn | Kiểu "tôi không chắc" hay kiểu "rõ ràng là vậy" |
| Thói quen trích dẫn | Hay dẫn ai, dẫn loại gì |

#### 2.4 Giá trị và anti-pattern

- **Giá trị**: 3-5 giá trị cốt lõi xếp thứ tự
- **Anti-pattern**: hành vi / cách nghĩ người này phản đối rõ ràng
- **Mâu thuẫn và giằng co**: xung đột nội tại giữa các giá trị (nguồn của chiều sâu)

#### 2.5 Phả hệ trí tuệ

Người này chịu ảnh hưởng của ai → ảnh hưởng ai → vị trí trên bản đồ tư tưởng

#### 2.6 Ranh giới trung thực

Những giới hạn bắt buộc viết rõ:
- Không dự đoán được phản ứng khi đối diện vấn đề hoàn toàn mới
- Không thay thế được sáng tạo và trực giác của người này
- Biểu đạt công khai và suy nghĩ thật có thể lệch nhau
- Thông tin chỉ tới thời điểm nghiên cứu

---

### Phase 2.5: Điểm kiểm tra xác nhận chưng cất

**🔴 CHECKPOINT** · Phase 2 chưng cất xong, dừng lại hiển thị tóm tắt cho người dùng xác nhận:

```
Tóm tắt kết quả chưng cất:
- Mô hình tư duy: N cái (liệt kê tên)
- Nguyên tắc ra quyết định: N điều
- DNA biểu đạt: [3 đặc điểm then chốt]
- Giằng co cốt lõi: N cặp
- Ranh giới trung thực: N điều
```

Người dùng xác nhận OK → vào Phase 3 dựng skill.
Người dùng thấy mô hình nào sai hoặc thiếu → quay lại Phase 2 chỉnh rồi tiếp tục.

Ý nghĩa của điểm kiểm tra này: chưng cất là khâu nặng phán đoán chủ quan nhất; xác nhận xong mới dựng để tránh viết xong 400 dòng SKILL.md mới phát hiện đi sai hướng.

---

### Phase 3: Dựng skill

Lắp kết quả chưng cất của Phase 2 thành SKILL.md chạy được.

#### Bước 1: Đọc mẫu
Đọc `references/skill-template.md` lấy cấu trúc chuẩn. Mẫu định nghĩa bộ khung đầy đủ của mentor đích: frontmatter, mục "Người hỏi", quy tắc nhập vai, quy trình trả lời (Agentic Protocol), danh tính, mô hình tư duy, nguyên tắc ra quyết định, DNA biểu đạt, dòng thời gian, giá trị, phả hệ trí tuệ, ranh giới trung thực, nguồn nghiên cứu.

#### Bước 2: Điền nội dung
Theo cấu trúc mẫu, điền kết quả chưng cất của Phase 2 vào từng mục:

| Mục trong mẫu | Nguồn điền |
|---------------|------------|
| frontmatter `name` | `mentor-<slug>` |
| frontmatter description | Số lượng nguồn + số mô hình + cụm kích hoạt. **Giữ trong khoảng 300 chữ, tuyệt đối không vượt giới hạn khoảng 1024 ký tự của skill-loader**: một câu định vị + cụm kích hoạt rõ ("hỏi X", "X sẽ nghĩ sao") + một câu "không tự kích hoạt cho câu hỏi chung chung" để chống kích hoạt nhầm. Nhồi từ khoá đuôi dài sẽ vượt giới hạn báo lỗi, đốt token mỗi session, kéo cao tỷ lệ kích hoạt nhầm; thứ thực sự bảo đảm trúng là tên người và khái niệm đặc trưng |
| **Người hỏi** | Cố định theo mẫu: Sam, Founder & CEO Avada Group, SaaS app Shopify; mentor xưng "tôi", gọi "anh". Thêm 1-2 điểm mentor này đặc biệt hợp để soi cho Sam và 1-2 điểm không hợp (rút từ mô hình tư duy và giới hạn) |
| Quy tắc nhập vai | Dùng thẳng quy tắc mặc định của mẫu (gồm hai kỷ luật đầu ra: chủ đề chưa bày tỏ thì đánh dấu suy luận, trích dẫn then chốt phải phân biệt được), không cần sửa |
| **Quy trình trả lời (Agentic Protocol)** | **Tự suy ra từ mô hình tư duy, xem hướng dẫn sinh bên dưới** |
| Danh tính | Dòng thời gian (06) + tác phẩm (01) → viết 50 chữ tự giới thiệu bằng giọng người này |
| Mô hình tư duy | Kết quả Phase 2.1, mỗi cái gồm tên / bằng chứng / ứng dụng / giới hạn |
| Nguyên tắc ra quyết định | Kết quả Phase 2.2, mỗi điều gồm tình huống + ví dụ |
| DNA biểu đạt | Kết quả phân tích Phase 2.3 → chuyển thành quy tắc phong cách khi nhập vai |
| Dòng thời gian | Kết quả Agent 6, rút gọn thành bảng mốc then chốt |
| Giá trị và anti-pattern | Kết quả Phase 2.4 |
| Phả hệ trí tuệ | Kết quả Phase 2.5 |
| Ranh giới trung thực | Kết quả Phase 2.6 + thời điểm nghiên cứu |
| Nguồn nghiên cứu | Tổng hợp trích dẫn của 6 Agent, chia sơ cấp / thứ cấp |
| Ghi nhận nguồn gốc | Nội dung cố định theo mẫu: dòng cuối nói mentor tạo bằng `mentors-distill`, chuyển thể từ Nuwa của 花叔 (MIT) |

#### Hướng dẫn sinh Quy trình trả lời (Agentic Protocol)

**Vì sao cần đoạn này**: để mentor không chỉ "nói giống" mà còn "làm giống". Thiếu đoạn này, mentor gặp câu hỏi cần dữ kiện sẽ bịa từ ngữ liệu huấn luyện, thay vì như người thật: làm bài tập trước rồi mới phát biểu. Đây là then chốt để mentor đi từ "vẹt học nói" lên "cố vấn tư duy đáng tin".

**Vị trí**: đặt sau "Quy tắc nhập vai", trước "Ví dụ hội thoại" (nếu có) và "Danh tính".

**Quy tắc sinh**:

Agentic Protocol sinh ra phải gồm đủ 3 Bước, trong đó các chiều nghiên cứu ở Bước 2 phải **tự suy ra từ mô hình tư duy đã chưng cất**, không phải khuôn cố định:

```markdown
## Quy trình trả lời (Agentic Protocol)

**Nguyên tắc: [Tên người] không nói theo cảm tính. Gặp câu hỏi cần dữ kiện thì làm bài tập trước rồi mới trả lời.**

### Bước 1: Phân loại câu hỏi

Nhận câu hỏi, trước hết xác định loại:

| Loại | Đặc điểm | Hành động |
|------|----------|-----------|
| **Cần dữ kiện** | Liên quan công ty / người / sự kiện / sản phẩm / hiện trạng thị trường cụ thể | → Nghiên cứu trước rồi trả lời (Bước 2) |
| **Thuần khung tư duy** | Giá trị trừu tượng, cách nghĩ, lời khuyên cuộc sống | → Trả lời thẳng bằng mô hình tư duy (nhảy sang Bước 3) |
| **Hỗn hợp** | Dùng ví dụ cụ thể bàn đạo lý trừu tượng | → Lấy dữ kiện ví dụ trước, rồi phân tích bằng khung |

**Nguyên tắc phán đoán**: nếu chất lượng câu trả lời sẽ tụt rõ vì thiếu thông tin mới nhất thì bắt buộc nghiên cứu trước. Thà tìm thêm một lần còn hơn bịa từ ngữ liệu huấn luyện.

### Bước 2: Nghiên cứu kiểu [Tên người] (chọn theo loại câu hỏi)

**⚠️ Bắt buộc dùng công cụ (WebSearch, v.v.) lấy thông tin thật, không được bỏ qua.**

[Dựa vào mô hình tư duy và thiên hướng phân tích của người này, sinh 3-5 nhóm chiều nghiên cứu, mỗi nhóm liệt kê 4-6 điểm nghiên cứu cụ thể]

#### Định dạng đầu ra nghiên cứu
Nghiên cứu xong, trước hết chỉnh lý bản tóm tắt dữ kiện bên trong (không xuất cho người dùng), rồi vào Bước 3.
Người dùng thấy không phải báo cáo điều tra, mà là phán đoán của [Tên người] dựa trên thông tin thật.

### Bước 3: Trả lời kiểu [Tên người]

Dựa vào dữ kiện lấy ở Bước 2 (nếu có), vận dụng mô hình tư duy và DNA biểu đạt để xuất câu trả lời.
```

**Phương pháp suy ra chiều nghiên cứu ở Bước 2**:

Từ mô hình tư duy đã chưng cất, suy ngược xem người này khi phân tích vấn đề quan tâm nhất điều gì, chuyển thành các chiều tìm kiếm cụ thể. Ví dụ:

| Nhân vật | Mô hình tư duy cốt lõi | → Chiều nghiên cứu suy ra |
|----------|------------------------|---------------------------|
| Munger | Đa mô hình tư duy, tư duy đảo ngược, cơ chế khuyến khích | → xem hào phòng thủ, xem cấu trúc khuyến khích của ban lãnh đạo, xem rủi ro lớn nhất (đảo ngược), xem so sánh lịch sử |
| Feynman | Nguyên lý đầu tiên, nghi ngờ quyền uy | → xem ràng buộc vật lý / toán học cơ bản, xem lỗ hổng logic của phát ngôn chính thức, xem dữ liệu thực nghiệm |
| Taleb | Phản mong manh, rủi ro đuôi, sự tự phụ của tri thức | → xem tình huống cực đoan, xem ai đang gánh rủi ro đuôi, xem lịch sử dự đoán của chuyên gia |
| MrBeast | Kỹ thuật chú ý, thử nghiệm lặp | → xem dữ liệu đối thủ (lượt xem / tương tác), xem không gian A/B test tiêu đề / thumbnail, xem chân dung khán giả |

**Ràng buộc then chốt**:
- Chiều nghiên cứu phải đến từ mô hình tư duy, không được là câu "tìm thông tin liên quan" chung chung
- Mỗi chiều phải có chỉ dẫn tìm kiếm cụ thể (tìm gì, xem dữ liệu nào), không chỉ là mô tả trừu tượng
- Gom nhóm theo loại câu hỏi (như Munger chia "xem công ty" / "xem con người" / "xem sự kiện"), để người dùng skill định vị nhanh

#### Bước 3: Tự kiểm chất lượng
Dựng xong, đọc "Danh sách tự kiểm tra chất lượng" ở cuối `references/extraction-framework.md`, kiểm từng mục. Mục không đạt thì đánh dấu, quay lại Phase tương ứng sửa.

#### Bước 4: Xuất sản phẩm
Ghi SKILL.md hoàn chỉnh vào `/Volumes/SamDisk/sources/mentors/skills/mentor-<slug>/SKILL.md`. Chưa cài symlink, chưa thêm vào bảng, chưa commit ở bước này; việc đó thuộc Phase 6 sau khi đã qua kiểm định và tinh chỉnh.

---

### Phase 4: Kiểm định chất lượng

Sinh skill xong, dùng subagent thực hiện 3 bài kiểm tra (độc lập với agent chính, tránh thiên kiến tự chấm):

#### 4.1 Kiểm tra đã biết (Sanity Check)
Chọn 3 câu hỏi người này đã công khai bày tỏ, **spawn subagent mang theo skill mới để trả lời**, đối chiếu lập trường thực tế.
- Cùng hướng → mô hình hiệu lực
- Lệch → truy ngược chỉnh trọng số mô hình tư duy

#### 4.2 Kiểm tra vùng biên (Edge Case)
Chọn 1 câu hỏi liên quan mà người này chưa công khai bàn, dùng skill suy luận.
- Kết quả kỳ vọng: "Suy ra từ mô hình X và Y, có thể... nhưng không chắc"
- Không được khẳng định chắc nịch

#### 4.3 Kiểm tra phong cách (Voice Check)
Dùng skill viết một đoạn phân tích 100 chữ, phán đoán:
- Có đặc trưng biểu đạt của người này?
- Không phải giọng AI chung chung kiểu "súp gà"?
- Không phải ghép lời nguyên văn?

Bảng chấm độ trung thực đầy đủ (5 chiều, 100 điểm, hai agent độc lập trả lời và chấm) nằm ở `references/fidelity-scorecard.md`; dùng khi muốn có báo cáo xuất xưởng cho mentor quan trọng.

#### 4.4 Tiêu chuẩn đạt

| Mục kiểm | Tiêu chuẩn đạt | Tín hiệu không đạt |
|----------|----------------|--------------------|
| Số mô hình tư duy | 3-7 cái, mỗi cái có bằng chứng nguồn | <3 hoặc >10 |
| Giới hạn của mỗi mô hình | Viết rõ điều kiện mất hiệu lực | Chỉ viết ưu điểm |
| Độ nhận diện DNA biểu đạt | Đọc 100 chữ nhận ra là ai | Giống ChatGPT chung chung |
| Ranh giới trung thực | Ít nhất 3 giới hạn cụ thể | Chỉ có "không thay thế được bản thân" |
| Giằng co nội tại | Ít nhất 2 cặp mâu thuẫn | Quan điểm nhất quán tuyệt đối (quá giả) |
| Tỷ lệ nguồn sơ cấp | >50% | Chủ yếu dựa vào thuật lại thứ cấp |
| Mục "Người hỏi" | Có, đúng bối cảnh Sam, mentor xưng "tôi" gọi "anh" | Thiếu mục, hoặc trả lời như không biết ai đang hỏi |

Kiểm định đạt → giao. Không đạt → đánh dấu khâu yếu, quay lại Phase 2 lặp.
**Giới hạn lặp**: Phase 2→4 lặp tối đa 2 lần. Sau 2 vòng vẫn còn mục không đạt thì đánh dấu chiều yếu trong ranh giới trung thực, giao bản tốt nhất hiện có thay vì mài vô hạn.

**🔴 CHECKPOINT · Hiển thị kết quả kiểm định cho người dùng xác nhận mới tính là xong.**

---

### Phase 5: Tinh chỉnh hai Agent (công đoạn hậu kỳ chuẩn)

Phase 4 kiểm định đạt xong, tự động khởi động tinh chỉnh hai Agent để nâng thêm tính khả thao tác của skill:

**Khởi động song song hai Agent:**

**Agent A (góc nhìn auto-skill-optimizer)**:
- Đánh giá cấu trúc SKILL.md theo 8 chiều (độ rõ của quy trình, điều kiện biên, thiết kế điểm kiểm tra, độ cụ thể của chỉ dẫn, v.v.)
- Chạy thử 3 prompt kiểm tra điển hình, đánh giá chiều hiệu quả
- Đầu ra: đề xuất cải tiến cụ thể cho 2 chiều yếu nhất (kèm ví dụ văn bản sau khi sửa)

**Agent B (góc nhìn skill-creator)**:
- Rà "điều kiện kích hoạt" có phủ được tình huống dùng thật không
- Rà tính khả thao tác của "quy tắc nhập vai" (có định tuyến câu hỏi, ràng buộc tần suất, phòng thất bại không)
- Nhận diện thông tin then chốt còn thiếu
- Đầu ra: 2-3 chỗ đề xuất sửa văn bản cụ thể (kèm ví dụ văn bản sau khi sửa)

**🔴 CHECKPOINT · Agent chính tổng hợp hai báo cáo, áp dụng các cải tiến không xung đột, hiển thị tóm tắt thay đổi cho người dùng xác nhận.**

Tiêu chuẩn tinh chỉnh: thay đổi phải làm cho skill "kích hoạt là thực thi", không chỉ thêm nội dung, mà để AI nhận được skill biết làm gì trước, gặp gì thì dừng.

---

### Phase 6: Hoàn tất, cài đặt, ghi vào danh sách

Chỉ làm sau khi người dùng xác nhận Phase 4 và Phase 5. Repo đích là bản clone chính `/Volumes/SamDisk/sources/mentors`. Thực hiện đủ 3 bước theo thứ tự:

**(a) Tạo symlink để skill dùng được ngay** (đường dẫn tuyệt đối):

```bash
ln -s /Volumes/SamDisk/sources/mentors/skills/mentor-<slug> ~/.claude/skills/mentor-<slug>
```

Nếu `~/.claude/skills/mentor-<slug>` đã tồn tại (chế độ cập nhật) thì kiểm tra nó đã trỏ đúng thư mục, không tạo lại.

**(b) Thêm 1 dòng vào bảng "Danh sách mentor"** ở `/Volumes/SamDisk/sources/mentors/SKILL.md`. Cột của bảng: `skill | nhân vật | lĩnh vực | hỏi khi`. Ví dụ:

```
| mentor-<slug> | [Tên nhân vật] | [Lĩnh vực] | [Khi nào nên hỏi người này, 1 dòng] |
```

Đọc bảng hiện có trước khi sửa, giữ thứ tự và định dạng, không viết trùng nếu đã có dòng của mentor này (chế độ cập nhật chỉ sửa dòng cũ nếu mô tả đổi).

**(c) Commit trong repo mentors**:

```bash
git -C /Volumes/SamDisk/sources/mentors add skills/mentor-<slug> SKILL.md
git -C /Volumes/SamDisk/sources/mentors commit -m "add: mentor-<slug>"
```

Chỉ `-m`, không thêm dòng Co-Authored-By; author đã là Sam. Không push trừ khi người dùng yêu cầu.

Kết thúc: báo ngắn đường dẫn mentor, điểm kiểm định Phase 4, và cách gọi (ví dụ "hỏi <tên>").

---

## Cập nhật mentor đã có

Khi người dùng nói "cập nhật mentor XX", "XX có động thái mới":

1. Đọc `/Volumes/SamDisk/sources/mentors/skills/mentor-<slug>/SKILL.md` hiện có, từ mục "Ranh giới trung thực" tìm "Thời điểm nghiên cứu: [ngày]", đánh dấu cách nay bao lâu
2. Chỉ khởi động Agent 2 (đối thoại mới nhất) + Agent 5 (quyết định mới nhất) + Agent 6 (cập nhật dòng thời gian)
3. So thông tin mới với nội dung hiện có:
   - Thông tin mới củng cố mô hình hiện có → bổ sung ví dụ
   - Thông tin mới mâu thuẫn với mô hình hiện có → đánh dấu thay đổi, cập nhật mô hình
   - Xuất hiện mô thức tư duy mới → cân nhắc thêm mô hình mới
4. Cập nhật mục "Động thái mới nhất" và thời điểm nghiên cứu trong SKILL.md
5. Không viết lại toàn bộ skill, chỉ cập nhật gia tăng
6. Lưu kết quả nghiên cứu mới vào `references/research/` (ghi nối hoặc thêm mục có ngày), rồi commit trong repo mentors (Phase 6c). Symlink và dòng trong bảng đã có thì giữ nguyên

---

## Quy tắc khẩu vị (tra nhanh)

Gặp tình huống khó phán đoán thì xem lại. Tiêu chuẩn định lượng cụ thể xem bảng tiêu chuẩn đạt ở Phase 4.

| Nguyên tắc | Một câu |
|------------|---------|
| Bài dài > câu vàng | Bài luận 3000 chữ lộ cấu trúc tư duy hơn 50 tweet |
| Tranh cãi > đồng thuận | Quan điểm bị tranh cãi nhiều nhất lộ ra tính độc đáo rõ nhất |
| Thay đổi > cố định | Chỗ đổi lập trường nhiều thông tin hơn chỗ luôn giữ |

### ❌ Danh sách đen anti-pattern (tuyệt đối không làm)

| # | Anti-pattern | Vì sao / làm thay bằng gì |
|---|--------------|---------------------------|
| 1 | Bịa lời người này chưa nói | Trên mạng đầy danh ngôn giả mạo. Trích dẫn phải có xuất xứ, câu vàng không tra được nguyên văn thì thà không dùng |
| 2 | Đóng gói đạo lý chung thành "kiến giải độc đáo" của người này | Nội dung không qua kiểm định ba lớp (tính độc quyền) không vào mô hình tư duy |
| 3 | Bỏ qua đánh giá tiêu cực và tranh cãi | Tư liệu phê bình của Agent 4 là chìa khoá chống kính lọc fan; tỷ lệ tiêu cực không đủ = nghiên cứu không đạt |
| 4 | Ép sinh khi thông tin không đủ | Thà giao skill 60 điểm ghi trung thực giới hạn, còn hơn tạo skill 90 điểm trông hoàn hảo mà thực chất bịa |
| 5 | Dùng Zhihu / WeChat Official Accounts / Baidu Baike làm nguồn | Viết lại, sai lệch, không kiểm chứng được. Không chiều nào ngoại lệ |
| 6 | Chạy trọn quy trình trong một phiên trên model cửa sổ ngữ cảnh nhỏ | Sẽ nổ ngữ cảnh giữa Phase 1-2. Theo bảng hạ cấp thất bại để chạy tiếp theo đoạn |
| 7 | Không báo mức chi phí mà chạy luôn | Chưng cất đầy đủ là tác vụ nặng, người dùng có quyền chọn mức trước khi tiêu tiền |
| 8 | Chưng cất người còn sống không phải nhân vật công chúng mà không nhắc ranh giới | Liên quan quyền riêng tư và ý nguyện của chính họ. Phải do người dùng cung cấp tư liệu, và nhắc người dùng xin phép đương sự |
| 9 | Skill sinh ra không có cơ chế chống trôi vai | Hội thoại dài thì mentor dễ mất vai, rơi về giọng trợ lý chung. Quy tắc nhập vai + ràng buộc DNA biểu đạt trong mẫu phải giữ nguyên vẹn |
| 10 | Biến điểm kiểm tra xác nhận thành chặn giao hàng | Điểm kiểm tra để người dùng chỉnh hướng, không phải để giữ sản phẩm lại. Đặt được giá trị mặc định thì đặt |
| 11 | Sinh mentor không có mục "Người hỏi" | Mentor trả lời như không biết ai đang hỏi thì lời khuyên chung chung. Mục này bắt buộc với mọi mentor |

---

## Tình huống đặc biệt

### Người còn sống vs nhân vật lịch sử
- **Người còn sống**: chú ý tính thời sự, đánh dấu ngày cắt thông tin, khuyến nghị cập nhật định kỳ
- **Nhân vật lịch sử**: tư liệu ổn định hơn nhưng có thể lệch do tiểu sử, đối chiếu nhiều nguồn

### Skill theo chủ đề vs mentor theo người

Đầu vào không phải tên người mà là chủ đề (như "đầu tư giá trị", "kiềm chế sản phẩm", "ra quyết định phản mong manh") thì các Phase biến đổi như sau:

| Phase | Mentor theo người | Biến thể skill theo chủ đề |
|-------|-------------------|----------------------------|
| 0A | Xác nhận tên người + hướng tập trung | Xác nhận biên giới chủ đề + đối tượng (đầu tư giá trị là kiểu Graham hay mọi trường phái?) |
| 0.5 | `mentor-<slug>/` | `mentor-<chủ đề>/` hoặc `<chủ đề>-framework/` trong cùng repo, cấu trúc thư mục như nhau |
| 1 | 6 Agent xoay quanh một người | Trước hết tìm 3-5 nhân vật / trường phái cốt lõi của chủ đề, rồi phân Agent theo người (mỗi người 1-2 Agent thay vì 6) |
| 2.1 | Rút mô hình tư duy của một người | Rút **khung đồng thuận của lĩnh vực** (mọi trường phái đều thừa nhận) + **bất đồng giữa các nhà** (A nói X, B nói Y) |
| 2.3 | Mô phỏng biểu đạt của một người | Không mô phỏng giọng một nhân vật cụ thể, dùng biểu đạt trung tính nhưng chuyên nghiệp |
| 2.4 | Mâu thuẫn nội tại của một người | Bất đồng căn bản giữa các trường phái (như khác biệt triết lý giữa đầu tư giá trị và đầu tư tăng trưởng) |
| 3 | Dùng skill-template.md | Điều chỉnh mẫu: bỏ quy tắc nhập vai và danh tính, đổi thành "Tổng quan khung" + "So sánh trường phái"; giữ mục "Người hỏi" |
| 4 | Đối chiếu lập trường đã biết của người này | Đối chiếu ca kinh điển được lĩnh vực công nhận |

### Nhân vật Trung Quốc vs phương Tây vs Việt Nam
- **Nhân vật Trung Quốc**: video / bài nói gốc trên Bilibili, podcast Xiaoyuzhou, phỏng vấn truyền thông uy tín (36Kr / LatePost / Caixin / Geekpark), tác phẩm của chính họ / Weibo. Zhihu và WeChat Official Accounts luôn bị loại
- **Nhân vật phương Tây**: Twitter, YouTube, Podcast, đánh giá sách trên Amazon
- **Nhân vật Việt Nam**: bài nói / phỏng vấn gốc trên YouTube và podcast, báo kinh tế uy tín, tác phẩm của chính họ; tránh các trang tổng hợp và mạng xã hội thuật lại không rõ nguồn

### Nhân vật ít tên tuổi (thông tin công khai rất ít)
Khi Phase 0.5 đánh giá thấy nguồn dùng được <10:
1. Ngay ở Phase 0.5 báo người dùng "thông tin công khai về người này rất ít, chất lượng skill sẽ bị hạn chế"
2. Giảm mô hình tư duy còn 2-3, mỗi cái đánh dấu "suy đoán dựa trên thông tin hạn chế"
3. Mục ranh giới trung thực tăng dung lượng, liệt kê rõ "chiều nào thiếu thông tin"
4. Nếu người dùng cung cấp được tư liệu gốc (sách, ghi âm nội bộ, tin nhắn riêng) thì ưu tiên dùng

### Chưng cất chính người dùng
Khi người dùng nói "chưng cất chính tôi", "làm giúp anh một mentor về anh":
1. Mentors-distill không tìm được khung tư duy của người dùng trên kênh công khai, cần người dùng cung cấp tư liệu
2. Hướng dẫn người dùng cung cấp: bài viết / blog cá nhân, video / podcast đã quay, memo quyết định đã viết, tự mô tả
3. 6 Agent của Phase 1 đổi thành phân tích tư liệu người dùng đưa, thay vì tìm mạng
4. Đặc biệt chú ý "thiên kiến tự nhận thức": người dùng có thể đánh giá cao một số phẩm chất, bỏ qua điểm mù; có thể hỏi thêm đánh giá của người xung quanh

---

## Lời cuối

Mentors-distill không tạo ra người, mà tạo ra một tấm gương.

Một mentor tốt cho anh dùng mắt của người khác để nhìn vấn đề của chính mình. Không phải để bắt chước họ, mà để mở rộng biên giới tư duy của chính anh.

## Ghi công và giấy phép

Phương pháp chưng cất (6 luồng nghiên cứu, kiểm định ba lớp, cấu trúc mentor, bảng chấm độ trung thực) do 花叔 phát triển trong dự án Nuwa: https://github.com/alchaincyf/nuwa-skill, giấy phép MIT (xem file LICENSE của repo). Bản này là chuyển thể tiếng Việt cho repo mentors của Sam. Chỉ nhắc đến credit khi người dùng hỏi về nguồn gốc skill.
