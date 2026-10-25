#!/usr/bin/env python3
"""Làm sạch tệp phụ đề SRT/VTT thành bản chép lời thuần văn bản.

Loại bỏ mốc thời gian, số thứ tự, dòng lặp và thẻ HTML để tạo văn bản dễ đọc.

Cách dùng:
    python3 srt_to_transcript.py input.srt [output.txt]
    python3 srt_to_transcript.py input.vtt [output.txt]

Nếu không chỉ định tệp đầu ra, mặc định là ``input_transcript.txt``.
"""

import sys
import re
from pathlib import Path


def clean_srt(content: str) -> str:
    """Làm sạch phụ đề định dạng SRT."""
    lines = content.strip().split('\n')
    texts = []

    for line in lines:
        line = line.strip()
        # Bỏ qua dòng số thứ tự (chỉ gồm chữ số).
        if re.match(r'^\d+$', line):
            continue
        # Bỏ qua dòng mốc thời gian.
        if re.match(r'\d{2}:\d{2}:\d{2}', line):
            continue
        # Bỏ qua dòng trống.
        if not line:
            continue
        # Loại bỏ thẻ HTML.
        line = re.sub(r'<[^>]+>', '', line)
        # Loại bỏ dấu vị trí của VTT.
        line = re.sub(r'align:.*$|position:.*$', '', line).strip()
        if line:
            texts.append(line)

    # Khử trùng lặp (phụ đề tự động thường lặp các dòng liên tiếp).
    deduped = []
    for text in texts:
        if not deduped or text != deduped[-1]:
            deduped.append(text)

    # Gộp thành đoạn: nối các câu ngắn liên tiếp, ngắt ở dấu kết câu hoặc đoạn dài.
    result = []
    current = []

    for text in deduped:
        current.append(text)
        # Nếu phần đang tích lũy đủ dài hoặc gặp dấu kết câu, tạo một đoạn.
        joined = ' '.join(current)
        if len(joined) > 200 or re.search(r'[\u3002\uFF01\uFF1F.!?]$', text):
            result.append(joined)
            current = []

    if current:
        result.append(' '.join(current))

    return '\n\n'.join(result)


def clean_vtt(content: str) -> str:
    """Làm sạch phụ đề VTT: bỏ phần đầu rồi xử lý theo logic SRT."""
    # Bỏ phần đầu WEBVTT.
    content = re.sub(r'^WEBVTT.*?\n\n', '', content, flags=re.DOTALL)
    # Bỏ các khối NOTE.
    content = re.sub(r'NOTE.*?\n\n', '', content, flags=re.DOTALL)
    return clean_srt(content)


def main():
    if len(sys.argv) < 2:
        print("Cách dùng: python3 srt_to_transcript.py <input.srt|input.vtt> [output.txt]")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    if not input_path.exists():
        print(f"❌ Không tìm thấy tệp: {input_path}")
        sys.exit(1)

    # Tên tệp đầu ra mặc định.
    if len(sys.argv) >= 3:
        output_path = Path(sys.argv[2])
    else:
        output_path = input_path.parent / f"{input_path.stem}_transcript.txt"

    # Đọc và nhận diện định dạng.
    content = input_path.read_text(encoding='utf-8')

    if input_path.suffix.lower() == '.vtt' or content.startswith('WEBVTT'):
        transcript = clean_vtt(content)
    else:
        transcript = clean_srt(content)

    output_path.write_text(transcript, encoding='utf-8')

    # Thống kê.
    word_count = len(transcript)
    line_count = transcript.count('\n') + 1
    print(f"✅ Đã chuyển đổi: {output_path}")
    print(f"   Số ký tự: {word_count}  Số đoạn: {line_count}")


if __name__ == '__main__':
    main()
