#!/bin/bash
# Download subtitles from a YouTube video.
# Usage: ./download_subtitles.sh <YouTube_URL> [output_directory]
# Prefers creator-made subtitles; falls back to auto-generated ones.
# Language order: English > Vietnamese > Chinese.

set -e

URL="$1"
OUTPUT_DIR="${2:-.}"

if [ -z "$URL" ]; then
    echo "Usage: ./download_subtitles.sh <YouTube_URL> [output_directory]"
    exit 1
fi

mkdir -p "$OUTPUT_DIR"

echo ">>> Checking available subtitles..."
yt-dlp --list-subs --no-download "$URL" 2>/dev/null | tail -20

echo ""
echo ">>> Trying creator-made subtitles (English first)..."

# Attempt 1: creator-made English subtitles.
if yt-dlp --write-subs --sub-langs "en,en-US,en-GB" --sub-format srt --skip-download -o "$OUTPUT_DIR/%(title)s" "$URL" 2>/dev/null; then
    FOUND=$(find "$OUTPUT_DIR" -name "*.srt" -newer /tmp/.ytdlp_marker 2>/dev/null | head -1)
    if [ -n "$FOUND" ]; then
        echo "✅ Downloaded: $FOUND"
        exit 0
    fi
fi

# Attempt 2: creator-made Vietnamese subtitles.
echo ">>> No creator-made English subtitles, trying Vietnamese..."
if yt-dlp --write-subs --sub-langs "vi,vi-VN" --sub-format srt --skip-download -o "$OUTPUT_DIR/%(title)s" "$URL" 2>/dev/null; then
    FOUND=$(find "$OUTPUT_DIR" -name "*.srt" -mmin -1 2>/dev/null | head -1)
    if [ -n "$FOUND" ]; then
        echo "✅ Downloaded: $FOUND"
        exit 0
    fi
fi

# Attempt 3: auto-generated subtitles, in the order English, Vietnamese, then Chinese.
echo ">>> No creator-made subtitles, trying auto-generated subtitles..."
if yt-dlp --write-auto-subs --sub-langs "en,en-US,en-GB,vi,vi-VN,zh-Hans,zh-Hant,zh,zh-CN,zh-TW" --sub-format srt --skip-download -o "$OUTPUT_DIR/%(title)s" "$URL" 2>/dev/null; then
    FOUND=$(find "$OUTPUT_DIR" -name "*.srt" -o -name "*.vtt" 2>/dev/null | head -1)
    if [ -n "$FOUND" ]; then
        echo "✅ Auto-generated subtitles downloaded: $FOUND"
        exit 0
    fi
fi

echo "❌ No usable subtitles found"
exit 1
