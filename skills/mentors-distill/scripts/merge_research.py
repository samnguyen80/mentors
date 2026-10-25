#!/usr/bin/env python3
"""Merge the research output of the 6 agents into the Phase 1.5 checkpoint summary table.

Scans the Markdown files 01-06 in ``references/research/`` to count sources,
the primary/secondary source ratio and the key findings of each dimension.

The patterns recognize English labels as well as the older Vietnamese ones.

Usage:
    python3 merge_research.py <path_to_skill_directory>

Example:
    python3 merge_research.py /Volumes/SamDisk/sources/mentors/skills/mentor-elon-musk

Output: prints the summary table to standard output.
"""

import sys
import re
from pathlib import Path

AGENTS = {
    '01-writings': 'Writings',
    '02-conversations': 'Conversations',
    '03-expression-dna': 'Expression',
    '04-external-views': 'External views',
    '05-decisions': 'Decisions',
    '06-timeline': 'Timeline',
}


def count_sources(content: str) -> dict:
    """Count the sources and the primary/secondary source ratio."""
    # Use the number of URLs to estimate the number of sources.
    urls = re.findall(r'https?://[^\s\)]+', content)

    # Detect primary/secondary source labels.
    primary_markers = len(re.findall(r'sơ cấp|primary|của chính người đó|nguyên văn|trích trực tiếp|by the person themselves|verbatim|direct quote', content, re.IGNORECASE))
    secondary_markers = len(re.findall(r'thứ cấp|secondary|trích lại|tóm tắt|bình luận|phân tích|quoted from|summary|commentary|analysis', content, re.IGNORECASE))

    return {
        'url_count': len(urls),
        'unique_urls': len(set(urls)),
        'primary_markers': primary_markers,
        'secondary_markers': secondary_markers,
    }


def extract_key_findings(content: str, max_items: int = 3) -> list[str]:
    """Take the key findings from the level-2 headings or the first bold items."""
    # Try the level-2 headings first.
    headings = re.findall(r'^##\s+(.+)$', content, re.MULTILINE)
    if headings:
        return headings[:max_items]

    # Fallback: take bold items.
    bolds = re.findall(r'\*\*(.+?)\*\*', content)
    if bolds:
        return bolds[:max_items]

    # Fallback: take the first three non-empty lines.
    lines = [l.strip() for l in content.split('\n') if l.strip() and not l.startswith('#')]
    return [l[:50] + '...' if len(l) > 50 else l for l in lines[:max_items]]


def find_contradictions(files: dict[str, str]) -> list[str]:
    """Simple detection of contradictions across the files."""
    contradictions = []
    # Look for keywords that signal contradiction or controversy.
    for name, content in files.items():
        matches = re.findall(r'(?:mâu thuẫn|ngược lại|nhưng thực tế|tranh cãi|contradict\w*|conversely|in reality|controvers\w*).{0,100}', content, re.IGNORECASE)
        for m in matches:
            contradictions.append(f"{AGENTS.get(name, name)}: {m[:80]}")
    return contradictions[:5]  # At most 5 items.


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 merge_research.py <path_to_skill_directory>")
        sys.exit(1)

    skill_dir = Path(sys.argv[1])
    research_dir = skill_dir / 'references' / 'research'

    if not research_dir.exists():
        print(f"❌ Directory not found: {research_dir}")
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
            rows.append(f"│ {label:<14} │ {'❌ None':<8} │ {'—':<24} │")
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

    # Detect contradictions.
    contradictions = find_contradictions(files)

    # Print the summary table.
    print("┌────────────────┬──────────┬──────────────────────────┐")
    print("│ Category       │ Sources  │ Key findings             │")
    print("├────────────────┼──────────┼──────────────────────────┤")
    for row in rows:
        print(row)
    print("├────────────────┼──────────┼──────────────────────────┤")

    primary_ratio = f"{total_primary}/{total_primary + total_secondary}" if (total_primary + total_secondary) > 0 else "Unlabeled"
    print(f"│ {'Total sources':<14} │ {total_sources:<8} │ {'Primary: ' + primary_ratio:<24} │")

    if contradictions:
        print(f"│ {'Contradictions':<14} │ {f'{len(contradictions)} found':<8} │ {contradictions[0][:24]:<24} │")
    else:
        print(f"│ {'Contradictions':<14} │ {'0 found':<8} │ {'—':<24} │")

    if missing:
        print(f"│ {'Missing':<14} │ {f'{len(missing)} items':<8} │ {', '.join(missing):<24} │")
    else:
        print(f"│ {'Missing':<14} │ {'None':<8} │ {'—':<24} │")

    print("└────────────────┴──────────┴──────────────────────────┘")

    # Summary.
    if total_sources < 10:
        print("\n⚠️ Fewer than 10 sources in total; add research or lower expectations")
    if missing:
        print(f"\n⚠️ Missing categories: {', '.join(missing)}; add research or state it in the honest boundaries")


if __name__ == '__main__':
    main()
