#!/usr/bin/env python3
"""Kiểm tra tự động SKILL.md có đạt tiêu chuẩn chất lượng Giai đoạn 4.

Đối chiếu từng tiêu chí, rồi in trạng thái đạt/chưa đạt cùng lý do cụ thể.

Cách dùng:
    python3 quality_check.py <đường_dẫn_SKILL.md>

Ví dụ:
    python3 quality_check.py /Volumes/SamDisk/sources/mentors/skills/mentor-elon-musk/SKILL.md
"""

import sys
import re
from pathlib import Path


def check_mental_models(content: str) -> tuple[bool, str]:
    """Kiểm tra số lượng mô hình tư duy (3-7 mô hình)."""
    # Khớp các tiêu đề như ### Mô hình N: hoặc ### Model N:.
    models = re.findall(r'^###\s+(?:mô hình|model|mental model)\s*\d', content, re.MULTILINE | re.IGNORECASE)
    if not models:
        # Dự phòng: đếm tiêu đề cấp 3 trong phần mô hình tư duy.
        in_section = False
        count = 0
        for line in content.split('\n'):
            if re.match(r'^##\s+.*(?:mô hình tư duy|mental model)', line, re.IGNORECASE):
                in_section = True
                continue
            if in_section and re.match(r'^##\s+', line) and 'mô hình tư duy' not in line.lower():
                break
            if in_section and re.match(r'^###\s+', line):
                count += 1
        if count > 0:
            passed = 3 <= count <= 7
            return passed, f"{count} mô hình tư duy {'✅' if passed else '❌ (cần 3-7 mô hình)'}"

    count = len(models)
    if count == 0:
        return False, "Không tìm thấy phần mô hình tư duy"
    passed = 3 <= count <= 7
    return passed, f"{count} mô hình tư duy {'✅' if passed else '❌ (cần 3-7 mô hình)'}"


def check_limitations(content: str) -> tuple[bool, str]:
    """Kiểm tra mỗi mô hình có dòng nêu giới hạn."""
    model_sections = re.findall(
        r'^###\s+(?:mô hình|model|mental model)\s*\d.*?(?=^###\s+|^##\s+|\Z)',
        content,
        re.MULTILINE | re.DOTALL | re.IGNORECASE,
    )
    limitation_pattern = re.compile(
        r'^\s*(?:[-*]\s*)?\*\*(?:giới hạn|mất hiệu lực|không áp dụng|điểm mù|limitation|blind spot)\*\*\s*:',
        re.MULTILINE | re.IGNORECASE,
    )
    if not model_sections:
        return False, "❌ Không tìm thấy mô hình để kiểm tra giới hạn"

    missing = sum(not limitation_pattern.search(section) for section in model_sections)
    passed = missing == 0
    return (
        passed,
        "Mỗi mô hình đều có giới hạn ✅"
        if passed
        else f"❌ {missing}/{len(model_sections)} mô hình chưa có dòng giới hạn",
    )


def check_expression_dna(content: str) -> tuple[bool, str]:
    """Kiểm tra DNA biểu đạt có đủ dấu hiệu phong cách."""
    dna_section = re.search(
        r'^##\s+[^\n]*(?:DNA biểu đạt|Expression DNA|biểu đạt|expression)[^\n]*$'
        r'(.*?)(?=\n##\s|\Z)',
        content,
        re.MULTILINE | re.DOTALL | re.IGNORECASE,
    )
    if not dna_section:
        return False, "❌ Không tìm thấy phần DNA biểu đạt"

    # Đếm các loại dấu hiệu phong cách, không tính lặp lại cùng một loại.
    markers = r'câu|từ vựng|giọng|hài hước|nhịp|độ chắc chắn|trích dẫn|câu cửa miệng'
    style_markers = len(set(re.findall(markers, dna_section.group(1), re.IGNORECASE)))
    passed = style_markers >= 3
    return passed, f"Dấu hiệu DNA biểu đạt: {style_markers} {'✅' if passed else '❌ (cần ≥3)'}"


def check_honest_boundary(content: str) -> tuple[bool, str]:
    """Kiểm tra ranh giới trung thực (ít nhất 3 mục)."""
    # Tìm phần ranh giới trung thực.
    boundary_match = re.search(r'(?:##\s+[^\n]*ranh giới trung thực|##\s+honest boundar\w*)(.*?)(?=\n##\s|\Z)', content, re.DOTALL | re.IGNORECASE)
    if not boundary_match:
        return False, "❌ Không tìm thấy phần ranh giới trung thực"

    boundary_text = boundary_match.group(1)
    # Đếm các mục dạng gạch đầu dòng.
    items = re.findall(r'^[-*]\s+', boundary_text, re.MULTILINE)
    count = len(items)
    passed = count >= 3
    return passed, f"Ranh giới trung thực: {count} mục {'✅' if passed else '❌ (cần ≥3 mục)'}"


def check_tensions(content: str) -> tuple[bool, str]:
    """Kiểm tra giằng co nội tại (ít nhất 2 dấu hiệu)."""
    tension_markers = len(re.findall(
        r'giằng co|mâu thuẫn|căng thẳng|tension|paradox|một mặt.*mặt khác|vừa.*vừa',
        content,
        re.IGNORECASE,
    ))
    passed = tension_markers >= 2
    return passed, f"Giằng co nội tại: {tension_markers} chỗ {'✅' if passed else '❌ (cần ≥2)'}"


def check_primary_sources(content: str) -> tuple[bool, str]:
    """Kiểm tra tỷ lệ nguồn sơ cấp."""
    # Tìm phần phụ lục nguồn nghiên cứu.
    source_section = re.search(
        r'(?:##\s+[^\n]*phụ lục:\s*nguồn nghiên cứu|##\s+[^\n]*(?:source|reference))(.*?)(?=\n##\s|\Z)',
        content,
        re.DOTALL | re.IGNORECASE,
    )
    if not source_section:
        return True, "Không tìm thấy phần nguồn (bỏ qua kiểm tra)"

    source_text = source_section.group(1)
    primary = len(re.findall(r'sơ cấp|primary|tác phẩm của chính người đó|gốc', source_text, re.IGNORECASE))
    secondary = len(re.findall(r'thứ cấp|secondary|trích lại|bình luận', source_text, re.IGNORECASE))
    total = primary + secondary
    if total == 0:
        return True, "Chưa đánh dấu loại nguồn (bỏ qua kiểm tra)"

    ratio = primary / total
    passed = ratio > 0.5
    return passed, f"Tỷ lệ nguồn sơ cấp: {primary}/{total} ({ratio:.0%}) {'✅' if passed else '❌ (cần >50%)'}"


def main():
    if len(sys.argv) < 2:
        print("Cách dùng: python3 quality_check.py <đường_dẫn_SKILL.md>")
        sys.exit(1)

    skill_path = Path(sys.argv[1])
    if not skill_path.exists():
        print(f"❌ Không tìm thấy tệp: {skill_path}")
        sys.exit(1)

    content = skill_path.read_text(encoding='utf-8')

    checks = [
        ("Số mô hình tư duy", check_mental_models),
        ("Giới hạn mô hình", check_limitations),
        ("DNA biểu đạt", check_expression_dna),
        ("Ranh giới trung thực", check_honest_boundary),
        ("Giằng co nội tại", check_tensions),
        ("Tỷ lệ nguồn sơ cấp", check_primary_sources),
    ]

    print(f"Kiểm tra chất lượng: {skill_path.name}")
    print("=" * 50)

    passed_count = 0
    total = len(checks)

    for name, check_fn in checks:
        passed, detail = check_fn(content)
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"  {name:<12} {status}  {detail}")
        if passed:
            passed_count += 1

    print("=" * 50)
    print(f"Kết quả: {passed_count}/{total} đạt")

    if passed_count == total:
        print("🎉 Tất cả đều đạt, có thể bàn giao")
    elif passed_count >= total - 1:
        print("⚠️ Gần đạt, nên sửa mục chưa đạt trước khi bàn giao")
    else:
        print("❌ Nhiều mục chưa đạt, nên quay lại Giai đoạn 2 để cải thiện")

    sys.exit(0 if passed_count == total else 1)


if __name__ == '__main__':
    main()
