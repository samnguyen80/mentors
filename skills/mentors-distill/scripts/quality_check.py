#!/usr/bin/env python3
"""Automatically check whether a SKILL.md meets the Phase 4 quality standard.

Checks each criterion, then prints pass/fail status with a concrete reason.

The patterns recognize the English headings and labels of the current template
as well as the older Vietnamese ones, so existing mentors keep working.

Usage:
    python3 quality_check.py <path_to_SKILL.md>

Example:
    python3 quality_check.py /Volumes/SamDisk/sources/mentors/skills/mentor-elon-musk/SKILL.md
"""

import sys
import re
from pathlib import Path


def check_mental_models(content: str) -> tuple[bool, str]:
    """Check the number of mental models (3-7 models)."""
    # Match headings such as "### Model N:" or "### Mô hình N:".
    models = re.findall(r'^###\s+(?:mô hình|model|mental model)\s*\d', content, re.MULTILINE | re.IGNORECASE)
    if not models:
        # Fallback: count level-3 headings inside the mental-models section.
        in_section = False
        count = 0
        for line in content.split('\n'):
            if re.match(r'^##\s+.*(?:mô hình tư duy|mental model)', line, re.IGNORECASE):
                in_section = True
                continue
            if in_section and re.match(r'^##\s+', line) and not re.search(r'mô hình tư duy|mental model', line, re.IGNORECASE):
                break
            if in_section and re.match(r'^###\s+', line):
                count += 1
        if count > 0:
            passed = 3 <= count <= 7
            return passed, f"{count} mental models {'✅' if passed else '❌ (need 3-7 models)'}"

    count = len(models)
    if count == 0:
        return False, "Mental models section not found"
    passed = 3 <= count <= 7
    return passed, f"{count} mental models {'✅' if passed else '❌ (need 3-7 models)'}"


def check_limitations(content: str) -> tuple[bool, str]:
    """Check that each model has a line stating its limits."""
    model_sections = re.findall(
        r'^###\s+(?:mô hình|model|mental model)\s*\d.*?(?=^###\s+|^##\s+|\Z)',
        content,
        re.MULTILINE | re.DOTALL | re.IGNORECASE,
    )
    limitation_pattern = re.compile(
        r'^\s*(?:[-*]\s*)?\*\*(?:giới hạn|mất hiệu lực|không áp dụng|điểm mù|limitations?|limits?|blind spots?)\*\*\s*:',
        re.MULTILINE | re.IGNORECASE,
    )
    if not model_sections:
        return False, "❌ No models found to check for limits"

    missing = sum(not limitation_pattern.search(section) for section in model_sections)
    passed = missing == 0
    return (
        passed,
        "Every model has a limit ✅"
        if passed
        else f"❌ {missing}/{len(model_sections)} models have no limit line",
    )


def check_expression_dna(content: str) -> tuple[bool, str]:
    """Check that the expression DNA has enough style markers."""
    dna_section = re.search(
        r'^##\s+[^\n]*(?:DNA biểu đạt|Expression DNA|biểu đạt|expression)[^\n]*$'
        r'(.*?)(?=\n##\s|\Z)',
        content,
        re.MULTILINE | re.DOTALL | re.IGNORECASE,
    )
    if not dna_section:
        return False, "❌ Expression DNA section not found"

    # Count distinct kinds of style markers, ignoring repeats of the same kind.
    markers = (
        r'câu|từ vựng|giọng|hài hước|nhịp|độ chắc chắn|trích dẫn|câu cửa miệng'
        r'|sentence|vocabulary|voice|tone|humou?r|rhythm|pacing|certainty|confidence|citation|quot(?:e|ation)|catchphrase'
    )
    style_markers = len(set(m.lower() for m in re.findall(markers, dna_section.group(1), re.IGNORECASE)))
    passed = style_markers >= 3
    return passed, f"Expression DNA markers: {style_markers} {'✅' if passed else '❌ (need ≥3)'}"


def check_honest_boundary(content: str) -> tuple[bool, str]:
    """Check the honest boundaries (at least 3 items)."""
    # Find the honest-boundaries section.
    boundary_match = re.search(r'(?:##\s+[^\n]*ranh giới trung thực|##\s+honest boundar\w*)(.*?)(?=\n##\s|\Z)', content, re.DOTALL | re.IGNORECASE)
    if not boundary_match:
        return False, "❌ Honest boundaries section not found"

    boundary_text = boundary_match.group(1)
    # Count the bullet items.
    items = re.findall(r'^[-*]\s+', boundary_text, re.MULTILINE)
    count = len(items)
    passed = count >= 3
    return passed, f"Honest boundaries: {count} items {'✅' if passed else '❌ (need ≥3 items)'}"


def check_tensions(content: str) -> tuple[bool, str]:
    """Check the internal tensions (at least 2 markers)."""
    tension_markers = len(re.findall(
        r'giằng co|mâu thuẫn|căng thẳng|tension|paradox|contradiction|inner conflict|one hand.*other hand|on the one hand.*on the other|một mặt.*mặt khác|vừa.*vừa',
        content,
        re.IGNORECASE,
    ))
    passed = tension_markers >= 2
    return passed, f"Internal tensions: {tension_markers} spots {'✅' if passed else '❌ (need ≥2)'}"


def check_primary_sources(content: str) -> tuple[bool, str]:
    """Check the share of primary sources."""
    # Find the research-sources appendix.
    source_section = re.search(
        r'(?:##\s+[^\n]*phụ lục:\s*nguồn nghiên cứu|##\s+[^\n]*(?:source|reference))(.*?)(?=\n##\s|\Z)',
        content,
        re.DOTALL | re.IGNORECASE,
    )
    if not source_section:
        return True, "No sources section found (check skipped)"

    source_text = source_section.group(1)
    primary = len(re.findall(r'sơ cấp|primary|tác phẩm của chính người đó|gốc|original', source_text, re.IGNORECASE))
    secondary = len(re.findall(r'thứ cấp|secondary|trích lại|bình luận|commentary', source_text, re.IGNORECASE))
    total = primary + secondary
    if total == 0:
        return True, "Source types not labeled (check skipped)"

    ratio = primary / total
    passed = ratio > 0.5
    return passed, f"Primary-source ratio: {primary}/{total} ({ratio:.0%}) {'✅' if passed else '❌ (need >50%)'}"


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 quality_check.py <path_to_SKILL.md>")
        sys.exit(1)

    skill_path = Path(sys.argv[1])
    if not skill_path.exists():
        print(f"❌ File not found: {skill_path}")
        sys.exit(1)

    content = skill_path.read_text(encoding='utf-8')

    checks = [
        ("Mental models", check_mental_models),
        ("Model limits", check_limitations),
        ("Expression DNA", check_expression_dna),
        ("Honest bounds", check_honest_boundary),
        ("Tensions", check_tensions),
        ("Primary srcs", check_primary_sources),
    ]

    print(f"Quality check: {skill_path.name}")
    print("=" * 50)

    passed_count = 0
    total = len(checks)

    for name, check_fn in checks:
        passed, detail = check_fn(content)
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"  {name:<14} {status}  {detail}")
        if passed:
            passed_count += 1

    print("=" * 50)
    print(f"Result: {passed_count}/{total} passed")

    if passed_count == total:
        print("🎉 All checks passed, ready to hand over")
    elif passed_count >= total - 1:
        print("⚠️ Almost there, fix the failing item before handing over")
    else:
        print("❌ Many items failed, go back to Phase 2 to improve")

    sys.exit(0 if passed_count == total else 1)


if __name__ == '__main__':
    main()
