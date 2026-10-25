#!/usr/bin/env python3
"""Gộp kết quả nghiên cứu của 6 tác nhân thành bảng tóm tắt kiểm tra Giai đoạn 1.5.

Quét các tệp Markdown 01-06 trong ``references/research/`` để thống kê số nguồn,
tỷ lệ nguồn sơ cấp/thứ cấp và các phát hiện chính của từng khía cạnh.

Cách dùng:
    python3 merge_research.py <đường_dẫn_thư_mục_skill>

Ví dụ:
    python3 merge_research.py /Volumes/SamDisk/sources/mentors/skills/mentor-elon-musk

Đầu ra: in bảng tóm tắt theo Markdown ra đầu ra chuẩn.
"""

import sys
import re
from pathlib import Path

AGENTS = {
    '01-writings': 'Tác phẩm',
    '02-conversations': 'Đối thoại',
    '03-expression-dna': 'Biểu đạt',
    '04-external-views': 'Góc nhìn ngoài',
    '05-decisions': 'Quyết định',
    '06-timeline': 'Dòng thời gian',
}


def count_sources(content: str) -> dict:
    """Thống kê số nguồn và tỷ lệ nguồn sơ cấp/thứ cấp."""
    # Dùng số URL để ước lượng số nguồn.
    urls = re.findall(r'https?://[^\s\)]+', content)

    # Phát hiện nhãn nguồn sơ cấp/thứ cấp.
    primary_markers = len(re.findall(r'sơ cấp|primary|của chính người đó|nguyên văn|trích trực tiếp', content, re.IGNORECASE))
    secondary_markers = len(re.findall(r'thứ cấp|secondary|trích lại|tóm tắt|bình luận|phân tích', content, re.IGNORECASE))

    return {
        'url_count': len(urls),
        'unique_urls': len(set(urls)),
        'primary_markers': primary_markers,
        'secondary_markers': secondary_markers,
    }


def extract_key_findings(content: str, max_items: int = 3) -> list[str]:
    """Lấy các phát hiện chính từ tiêu đề cấp 2 hoặc mục in đậm đầu tiên."""
    # Thử lấy tiêu đề cấp 2.
    headings = re.findall(r'^##\s+(.+)$', content, re.MULTILINE)
    if headings:
        return headings[:max_items]

    # Dự phòng: lấy mục in đậm.
    bolds = re.findall(r'\*\*(.+?)\*\*', content)
    if bolds:
        return bolds[:max_items]

    # Dự phòng: lấy ba dòng khác rỗng đầu tiên.
    lines = [l.strip() for l in content.split('\n') if l.strip() and not l.startswith('#')]
    return [l[:50] + '...' if len(l) > 50 else l for l in lines[:max_items]]


def find_contradictions(files: dict[str, str]) -> list[str]:
    """Phát hiện đơn giản các điểm mâu thuẫn giữa các tệp."""
    contradictions = []
    # Tìm các từ khóa biểu thị mâu thuẫn hoặc tranh cãi.
    for name, content in files.items():
        matches = re.findall(r'(?:mâu thuẫn|ngược lại|nhưng thực tế|tranh cãi).{0,100}', content, re.IGNORECASE)
        for m in matches:
            contradictions.append(f"{AGENTS.get(name, name)}: {m[:80]}")
    return contradictions[:5]  # Tối đa 5 điểm.


def main():
    if len(sys.argv) < 2:
        print("Cách dùng: python3 merge_research.py <đường_dẫn_thư_mục_skill>")
        sys.exit(1)

    skill_dir = Path(sys.argv[1])
    research_dir = skill_dir / 'references' / 'research'

    if not research_dir.exists():
        print(f"❌ Không tìm thấy thư mục: {research_dir}")
        sys.exit(1)

    files = {}
    rows = []
    total_sources = 0
    total_primary = 0
    total_secondary = 0
    missing = []

    for key, label in AGENTS.items():
        md_file = research_dir / f"{key}.md"
        if not md_file.exists():
            missing.append(label)
            rows.append(f"│ {label:<14} │ {'❌ Thiếu':<8} │ {'—':<24} │")
            continue

        content = md_file.read_text(encoding='utf-8')
        files[key] = content
        stats = count_sources(content)
        findings = extract_key_findings(content)

        total_sources += stats['unique_urls']
        total_primary += stats['primary_markers']
        total_secondary += stats['secondary_markers']

        findings_str = ', '.join(findings) if findings else '—'
        if len(findings_str) > 40:
            findings_str = findings_str[:37] + '...'

        rows.append(f"│ {label:<14} │ {stats['unique_urls']:<8} │ {findings_str:<24} │")

    # Phát hiện mâu thuẫn.
    contradictions = find_contradictions(files)

    # In bảng tóm tắt.
    print("┌────────────────┬──────────┬──────────────────────────┐")
    print("│ Hạng mục       │ Số nguồn │ Phát hiện chính          │")
    print("├────────────────┼──────────┼──────────────────────────┤")
    for row in rows:
        print(row)
    print("├────────────────┼──────────┼──────────────────────────┤")

    primary_ratio = f"{total_primary}/{total_primary + total_secondary}" if (total_primary + total_secondary) > 0 else "Chưa gắn nhãn"
    print(f"│ {'Tổng nguồn':<14} │ {total_sources:<8} │ {'Nguồn sơ cấp: ' + primary_ratio:<24} │")

    if contradictions:
        print(f"│ {'Mâu thuẫn':<14} │ {f'{len(contradictions)} chỗ':<8} │ {contradictions[0][:24]:<24} │")
    else:
        print(f"│ {'Mâu thuẫn':<14} │ {'0 chỗ':<8} │ {'—':<24} │")

    if missing:
        print(f"│ {'Thiếu mục':<14} │ {f'{len(missing)} mục':<8} │ {', '.join(missing):<24} │")
    else:
        print(f"│ {'Thiếu mục':<14} │ {'Không':<8} │ {'—':<24} │")

    print("└────────────────┴──────────┴──────────────────────────┘")

    # Tóm tắt.
    if total_sources < 10:
        print("\n⚠️ Tổng số nguồn <10, nên bổ sung nghiên cứu hoặc hạ kỳ vọng")
    if missing:
        print(f"\n⚠️ Thiếu hạng mục: {', '.join(missing)}; nên bổ sung hoặc nêu rõ trong ranh giới trung thực")


if __name__ == '__main__':
    main()
