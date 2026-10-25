#!/usr/bin/env python3
"""
thumbnail_audit.py - Checklist script based on MrBeast's thumbnail theory

Dimensions checked (based on the thumbnail principles MrBeast has shared publicly):
  1. Title/thumbnail complementarity: do they complement rather than repeat each other?
  2. Number of focal points: are there only 1-2 visual focal points?
  3. Amount of text: does the thumbnail text have fewer than 5 words?
  4. Emotional expression: is there a clear facial expression/emotion?
  5. Color contrast: is the color contrast striking enough?

If an image file is provided, PIL is used to analyze color distribution and brightness contrast.

Usage:
  python thumbnail_audit.py --title "I Spent 50 Hours Buried Alive"
  python thumbnail_audit.py --title "..." --image thumbnail.jpg
  python thumbnail_audit.py --title "..." --image thumbnail.jpg -o report.md

Dependencies: Pillow (only needed for image analysis; text-only checks have no dependencies)
"""

import argparse
import sys
from pathlib import Path


# ---------- MrBeast thumbnail principles ----------

REDUNDANCY_WORDS = {
    # If keywords from the title appear heavily in the thumbnail text, they repeat rather than complement each other
    "challenge", "survive", "hours", "days", "dollars", "money",
    "biggest", "world", "first", "last", "never", "impossible",
}

# Emotion-related words (used for title analysis)
EMOTION_WORDS = [
    "shocked", "scared", "amazed", "crying", "screaming", "laughing",
    "surprised", "angry", "terrified", "excited", "happy", "sad",
    "emotional", "insane", "crazy", "unbelievable", "incredible",
    # Chinese emotion words (match data for Chinese-language titles; kept as-is)
    "震惊", "害怕", "惊讶", "哭", "尖叫", "笑", "疯狂", "不敢相信",
]


def check_title_thumbnail_complementarity(title: str, thumb_text: str = "") -> dict:
    """Check whether the title and thumbnail complement (rather than repeat) each other"""
    title_words = set(title.lower().split())
    thumb_words = set(thumb_text.lower().split()) if thumb_text else set()

    if not thumb_text:
        return {
            "score": 3,
            "max": 5,
            "note": "No thumbnail text provided, so a full assessment is not possible. Suggestion: the thumbnail should add information the title does not give.",
        }

    overlap = title_words & thumb_words & REDUNDANCY_WORDS
    overlap_ratio = len(overlap) / max(len(thumb_words), 1)

    if overlap_ratio > 0.5:
        score = 1
        note = f"The thumbnail text heavily repeats the title (repeated words: {', '.join(overlap)}). MrBeast principle: the thumbnail should complement the title, not repeat it."
    elif overlap_ratio > 0.2:
        score = 3
        note = f"Some repetition ({', '.join(overlap)}), but acceptable. Consider having the thumbnail convey information the title does not."
    else:
        score = 5
        note = "The title and thumbnail complement each other well, each conveying different information."

    return {"score": score, "max": 5, "note": note, "overlap": list(overlap)}


def check_text_amount(thumb_text: str = "") -> dict:
    """Check the amount of thumbnail text"""
    if not thumb_text:
        return {
            "score": 4,
            "max": 5,
            "word_count": 0,
            "note": "No thumbnail text provided. MrBeast thumbnails usually have very little text (0-3 words) or none at all.",
        }

    word_count = len(thumb_text.split())
    if word_count == 0:
        score, note = 5, "No text, clean and crisp."
    elif word_count <= 3:
        score, note = 5, f"Only {word_count} word(s), in line with the MrBeast standard."
    elif word_count <= 5:
        score, note = 3, f"{word_count} words, close to the limit. Consider trimming to 3 words or fewer."
    else:
        score, note = 1, f"{word_count} words, too many! MrBeast thumbnails rarely exceed 3-5 words. The less text, the higher the click-through rate."

    return {"score": score, "max": 5, "word_count": word_count, "note": note}


def check_emotion_in_title(title: str) -> dict:
    """Check whether the title implies a clear emotion (an indirect assessment of the thumbnail's emotional needs)"""
    title_lower = title.lower()
    found_emotions = [w for w in EMOTION_WORDS if w in title_lower]

    # Check for exclamation marks and question marks (the full-width variants are kept deliberately: they match CJK titles)
    has_exclamation = "!" in title or "？" in title or "!" in title
    has_question = "?" in title or "？" in title

    if found_emotions:
        score = 5
        note = f"The title clearly implies an emotion ({', '.join(found_emotions[:3])}). The thumbnail should echo it with a facial expression."
    elif has_exclamation or has_question:
        score = 3
        note = "The title has emotional punctuation but no explicit emotion word. The thumbnail needs a facial expression to supply the emotion."
    else:
        score = 2
        note = "The title's emotion is not obvious. MrBeast principle: the thumbnail must have a face with an exaggerated expression, or a clear emotional visual element."

    return {
        "score": score,
        "max": 5,
        "emotions_found": found_emotions,
        "note": note,
    }


def check_title_curiosity_gap(title: str) -> dict:
    """Check whether the title creates a curiosity gap"""
    # (pattern label, keywords). The keywords are match data and include Chinese terms for Chinese-language titles; kept as-is.
    curiosity_patterns = [
        ("Number comparison", ["vs", "versus", "$", "比"]),
        ("Suspense words", ["secret", "mystery", "hidden", "never", "impossible", "秘密", "不可能"]),
        ("Challenge framing", ["challenge", "survive", "last", "endure", "挑战", "坚持"]),
        ("Extreme words", ["world", "biggest", "smallest", "most", "least", "最大", "最小", "最"]),
        ("Time pressure", ["hours", "days", "minutes", "seconds", "小时", "天", "分钟"]),
    ]

    found = []
    title_lower = title.lower()
    for pattern_name, keywords in curiosity_patterns:
        if any(k in title_lower for k in keywords):
            found.append(pattern_name)

    if len(found) >= 3:
        score, note = 5, f"The title has {len(found)} curiosity elements ({', '.join(found)}), very strong!"
    elif len(found) >= 2:
        score, note = 4, f"The title has {len(found)} curiosity elements ({', '.join(found)}), not bad."
    elif len(found) == 1:
        score, note = 3, f"The title has 1 curiosity element ({found[0]}), could be stronger."
    else:
        score, note = 1, "The title lacks a curiosity gap. MrBeast titles usually contain at least 2-3 curiosity elements."

    return {"score": score, "max": 5, "patterns_found": found, "note": note}


def analyze_image(image_path: str) -> dict:
    """Use PIL to analyze the image's color and contrast"""
    try:
        from PIL import Image, ImageStat
    except ImportError:
        return {
            "available": False,
            "note": "Pillow is not installed, skipping image analysis. Install: pip install Pillow",
        }

    path = Path(image_path)
    if not path.exists():
        return {"available": False, "note": f"Image file not found: {image_path}"}

    try:
        img = Image.open(path)
    except Exception as e:
        return {"available": False, "note": f"Cannot open image: {e}"}

    # Convert to RGB
    if img.mode != "RGB":
        img = img.convert("RGB")

    stat = ImageStat.Stat(img)
    width, height = img.size

    # Average brightness
    avg_brightness = sum(stat.mean) / 3

    # Brightness standard deviation (contrast indicator)
    avg_stddev = sum(stat.stddev) / 3

    # Color saturation analysis
    hsv_img = img.convert("HSV")
    hsv_stat = ImageStat.Stat(hsv_img)
    avg_saturation = hsv_stat.mean[1]

    # Dominant-tone analysis (simplified: compare the center region with the edges)
    center_crop = img.crop((width // 4, height // 4, 3 * width // 4, 3 * height // 4))
    center_stat = ImageStat.Stat(center_crop)
    center_brightness = sum(center_stat.mean) / 3

    # Assessment
    results = {
        "available": True,
        "size": f"{width}x{height}",
        "brightness": {
            "average": round(avg_brightness, 1),
            "score": 5 if 80 < avg_brightness < 200 else 3 if 50 < avg_brightness < 230 else 1,
            "note": "Brightness is moderate" if 80 < avg_brightness < 200 else "Too dark or too bright",
        },
        "contrast": {
            "stddev": round(avg_stddev, 1),
            "score": 5 if avg_stddev > 60 else 3 if avg_stddev > 40 else 1,
            "note": "Strong contrast" if avg_stddev > 60 else "Medium contrast" if avg_stddev > 40 else "Insufficient contrast; the thumbnail may not stand out at small sizes",
        },
        "saturation": {
            "average": round(avg_saturation, 1),
            "score": 5 if avg_saturation > 100 else 3 if avg_saturation > 60 else 2,
            "note": "High color saturation" if avg_saturation > 100 else "Medium color saturation" if avg_saturation > 60 else "Colors are washed out; consider increasing saturation",
        },
        "center_focus": {
            "center_brightness": round(center_brightness, 1),
            "edge_contrast": round(abs(center_brightness - avg_brightness), 1),
            "note": "Clear contrast between the center and the edges" if abs(center_brightness - avg_brightness) > 15 else "Little contrast between the center and the edges; the focal point may not stand out enough",
        },
    }
    return results


def generate_report(title: str, thumb_text: str = "", image_path: str = None) -> str:
    """Generate the full audit report"""
    complementarity = check_title_thumbnail_complementarity(title, thumb_text)
    text_amount = check_text_amount(thumb_text)
    emotion = check_emotion_in_title(title)
    curiosity = check_title_curiosity_gap(title)

    image_analysis = analyze_image(image_path) if image_path else None

    # Compute the total score
    scores = [complementarity["score"], text_amount["score"], emotion["score"], curiosity["score"]]
    if image_analysis and image_analysis.get("available"):
        scores.append(image_analysis["brightness"]["score"])
        scores.append(image_analysis["contrast"]["score"])
        scores.append(image_analysis["saturation"]["score"])

    total = sum(scores)
    max_total = len(scores) * 5

    lines = []
    lines.append("# Thumbnail Audit Report\n")
    lines.append(f"**Title**: {title}")
    if thumb_text:
        lines.append(f"**Thumbnail text**: {thumb_text}")
    if image_path:
        lines.append(f"**Image**: {image_path}")
    lines.append(f"\n**Total score**: {total}/{max_total} ({total/max_total*100:.0f}%)\n")

    # Grade
    pct = total / max_total * 100
    if pct >= 80:
        grade = "A - Excellent, high click-through potential"
    elif pct >= 60:
        grade = "B - Good, room for optimization"
    elif pct >= 40:
        grade = "C - Passable, needs focused improvement"
    else:
        grade = "D - Needs a redo"
    lines.append(f"**Grade**: {grade}\n")

    # Individual checks
    lines.append("## 1. Title/Thumbnail Complementarity ({}/{})\n".format(complementarity["score"], complementarity["max"]))
    lines.append(complementarity["note"])
    lines.append("")

    lines.append("## 2. Thumbnail Text Amount ({}/{})\n".format(text_amount["score"], text_amount["max"]))
    lines.append(text_amount["note"])
    lines.append("")

    lines.append("## 3. Emotional Expression ({}/{})\n".format(emotion["score"], emotion["max"]))
    lines.append(emotion["note"])
    lines.append("")

    lines.append("## 4. Curiosity Gap ({}/{})\n".format(curiosity["score"], curiosity["max"]))
    lines.append(curiosity["note"])
    lines.append("")

    # Image analysis
    if image_analysis:
        if image_analysis.get("available"):
            lines.append(f"## 5. Image Technical Analysis (size: {image_analysis['size']})\n")
            b = image_analysis["brightness"]
            c = image_analysis["contrast"]
            s = image_analysis["saturation"]
            cf = image_analysis["center_focus"]
            lines.append(f"- **Brightness** ({b['score']}/5): average {b['average']} - {b['note']}")
            lines.append(f"- **Contrast** ({c['score']}/5): std dev {c['stddev']} - {c['note']}")
            lines.append(f"- **Saturation** ({s['score']}/5): average {s['average']} - {s['note']}")
            lines.append(f"- **Focal point**: center-edge difference {cf['edge_contrast']} - {cf['note']}")
        else:
            lines.append(f"## 5. Image Analysis\n")
            lines.append(f"Skipped: {image_analysis['note']}")
        lines.append("")

    # MrBeast thumbnail checklist
    lines.append("## MrBeast Thumbnail Golden Rules\n")
    lines.append("- [ ] Is the thumbnail clear and legible on a small phone screen?")
    lines.append("- [ ] Are there only 1-2 visual focal points (not cluttered)?")
    lines.append("- [ ] Is there a face with a strong emotion?")
    lines.append("- [ ] Does the thumbnail trigger the urge of 'I have to click and watch this'?")
    lines.append("- [ ] Does the title and thumbnail combination create an information gap?")
    lines.append("- [ ] Does it stand out enough next to other videos published around the same time?")
    lines.append("")

    # Improvement suggestions
    lines.append("## Improvement Suggestions\n")
    suggestions = []
    if complementarity["score"] < 4:
        suggestions.append("Have the thumbnail convey information the title does not (e.g. if the title states the challenge, the thumbnail shows the result or the most dramatic moment)")
    if text_amount["score"] < 4:
        suggestions.append("Reduce the thumbnail text, ideally to 0-3 words; tell the story visually rather than with text")
    if emotion["score"] < 4:
        suggestions.append("Add a face photo with an exaggerated expression to the thumbnail; the stronger the emotion, the better")
    if curiosity["score"] < 4:
        suggestions.append("Add curiosity elements to the title, such as numbers, extreme words, or time pressure")
    if image_analysis and image_analysis.get("available"):
        if image_analysis["contrast"]["score"] < 4:
            suggestions.append("Increase the image contrast so the thumbnail stays clear and striking at small sizes")
        if image_analysis["saturation"]["score"] < 4:
            suggestions.append("Increase color saturation so the image pops on the YouTube home page")

    if suggestions:
        for i, s in enumerate(suggestions, 1):
            lines.append(f"{i}. {s}")
    else:
        lines.append("Overall performance is excellent, keep it up!")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Audit tool based on MrBeast's thumbnail theory",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='Examples:\n  python thumbnail_audit.py --title "I Survived 50 Hours In Antarctica"\n  python thumbnail_audit.py --title "..." --thumb-text "50 HOURS" --image thumb.jpg',
    )
    parser.add_argument("--title", required=True, help="Video title")
    parser.add_argument("--thumb-text", default="", help="Text on the thumbnail (if any)")
    parser.add_argument("--image", help="Path to the thumbnail image file (optional)")
    parser.add_argument("-o", "--output", help="Output report file path")
    args = parser.parse_args()

    report = generate_report(args.title, args.thumb_text, args.image)

    if args.output:
        Path(args.output).write_text(report, encoding="utf-8")
        print(f"[OK] Report saved to: {args.output}")
    else:
        print(report)


if __name__ == "__main__":
    main()
