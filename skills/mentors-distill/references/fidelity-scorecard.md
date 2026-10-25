# Bảng chấm độ trung thực (Fidelity Scorecard)

> Báo cáo kiểm tra chất lượng xuất xưởng của mentor. Trả lời một câu hỏi: **chạy lên thì skill này có giống người thật không, và có trung thực không?**
>
> Bối cảnh: bài báo SkillLens (arXiv 2605.23899) đo được độ chính xác khi LLM tự đánh giá chất lượng skill chỉ 46,4% (gần như đoán bừa). Vì vậy nguyên tắc sắt của bảng chấm là: **agent trả lời và agent chấm phải là hai agent độc lập, tuyệt đối không tự chấm tự chứng.**

## Năm chiều chấm (tổng 100)

| # | Chiều | Điểm | Đo gì | Đo thế nào |
|---|-------|------|-------|------------|
| 1 | Nhất quán lập trường | 30 | Với các vấn đề người này đã công khai bày tỏ, hướng trả lời của skill có khớp không | 3 câu hỏi lập trường đã biết, mỗi câu 10 điểm: đúng hướng và đúng chi tiết = 10, đúng hướng lệch chi tiết = 6, lệch lập trường = 0 |
| 2 | Độ nhận diện phong cách | 20 | Không nhìn tên, có nhận ra là ai từ cách biểu đạt không | Agent chấm đọc mù câu trả lời: câu chữ, từ vựng, cách so sánh có dấu vân tay của người này hay chỉ là giọng AI chung chung |
| 3 | Trung thực ở vùng biên | 20 | Gặp vấn đề người này chưa từng bàn, skill đánh dấu là suy luận hay bịa một cách chắc nịch | 1 câu ngoài phạm vi: nói rõ "đây là suy luận từ khung tư duy" và giữ sự không chắc chắn = điểm tối đa; giả làm quan điểm chính chủ và khẳng định = 0 |
| 4 | Minh bạch nguồn | 15 | Bản nghiên cứu nền có truy nguồn được không | Kiểm tĩnh file skill: có mục nguồn nghiên cứu, tỷ lệ nguồn sơ cấp > 50%, trích dẫn then chốt có xuất xứ |
| 5 | Đầy đủ cấu trúc | 15 | Có đủ cấu trúc chống trôi vai và vận hành trung thực không | Kiểm tĩnh: 3-7 mô hình tư duy, ranh giới trung thực ≥ 3 mục, giằng co nội tại ≥ 2 cặp, có danh sách anti-pattern, quy tắc nhập vai có ràng buộc chống trôi vai, có mục "Người hỏi" |

## Xếp hạng

| Hạng | Điểm | Ý nghĩa |
|------|------|---------|
| A | ≥ 85 | Xuất xưởng là hàng tinh, yên tâm dùng làm cố vấn tư duy |
| B | 70-84 | Đạt, một số chiều có điểm yếu đã được đánh dấu |
| C | 55-69 | Dùng được nhưng cần thận trọng, bắt buộc đọc ranh giới trung thực |
| D | < 55 | Không khuyến nghị dùng, cần chưng cất lại từ đầu |

## Quy trình thực hiện

1. **Ra đề**: 3 câu hỏi lập trường đã biết (chọn chủ đề người này nhiều lần công khai bày tỏ) + 1 câu ngoài phạm vi + 1 câu lấy mẫu phong cách
2. **Agent trả lời**: chỉ đọc các file trong thư mục skill, trả lời theo vai người trong skill, cấm lên mạng
3. **Agent chấm**: agent độc lập, nhận kết quả trả lời + rubric này + đường dẫn file skill, đối chiếu lập trường công khai thật của người đó rồi chấm từng chiều
4. **Đầu ra**: sinh file `FIDELITY.md` trong thư mục skill, gồm bảng điểm, lý do phán định từng câu, ngày kiểm tra, model dùng để trả lời và chấm

## Định dạng kết quả (mẫu FIDELITY.md)

```markdown
# Bảng chấm độ trung thực

**Tổng: NN/100 · Hạng X** | Ngày kiểm tra: YYYY-MM-DD | Trả lời/chấm: hai agent độc lập

| Chiều | Điểm | Tóm tắt phán định |
|-------|------|-------------------|
| Nhất quán lập trường | NN/30 | ... |
| Độ nhận diện phong cách | NN/20 | ... |
| Trung thực ở vùng biên | NN/20 | ... |
| Minh bạch nguồn | NN/15 | ... |
| Đầy đủ cấu trúc | NN/15 | ... |

## Nhật ký kiểm tra
[Với mỗi câu: câu hỏi, tóm tắt câu trả lời, lập trường thật được đối chiếu, phán định]
```

## Quan hệ với quy trình chưng cất

- Tiêu chuẩn đạt của Phase 4 là **kiểm tra nội bộ** (cửa ải trong lúc sinh skill)
- Bảng chấm là **báo cáo bên ngoài** (kiểm tra xuất xưởng sau khi sinh xong, ai cũng chạy lại để kiểm chứng được)
- Mentor mới chưa bắt buộc có `FIDELITY.md`. Nếu muốn dùng làm bằng chứng chất lượng (ví dụ trước khi đưa mentor vào bảng "Danh sách mentor" như một mentor tin cậy), hạng B trở lên là ngưỡng khuyến nghị

## Chống gian lận

- Agent trả lời không biết mình đang bị đo chiều nào
- Agent chấm không tham gia trả lời, chỉ đối chiếu sự thật công khai
- Ra đề tránh các ví dụ đối thoại đã có trong file skill (tránh học thuộc đáp án)
- Với kết luận quan trọng, nên cho 2 agent chấm độc lập chạy riêng; chênh nhau > 10 điểm thì con người xem lại
