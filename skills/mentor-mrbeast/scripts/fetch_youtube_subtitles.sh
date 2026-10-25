#!/bin/bash
#
# fetch_youtube_subtitles.sh - Download YouTube video subtitles
#
# Uses yt-dlp to download subtitle files for a YouTube video or channel (manual subtitles first, auto-generated subtitles as fallback)
#
# Usage:
#   ./fetch_youtube_subtitles.sh <URL> [language] [outdir]
#
# Arguments:
#   URL        - YouTube video URL or channel URL (required)
#   language   - Subtitle language code, default en (optional)
#   outdir     - Where to save subtitles, default current directory (optional)
#
# Examples:
#   ./fetch_youtube_subtitles.sh "https://youtube.com/watch?v=xxx"
#   ./fetch_youtube_subtitles.sh "https://youtube.com/watch?v=xxx" zh-Hans ./subs
#   ./fetch_youtube_subtitles.sh "https://youtube.com/@MrBeast" en ./mrbeast_subs
#

set -euo pipefail

# ---------- Argument parsing ----------
URL="${1:-}"
LANG="${2:-en}"
OUTDIR="${3:-.}"

if [ -z "$URL" ]; then
    echo "Usage: $0 <YouTube URL> [language] [outdir]"
    echo ""
    echo "Examples:"
    echo "  $0 'https://youtube.com/watch?v=xxx'"
    echo "  $0 'https://youtube.com/watch?v=xxx' zh-Hans ./subs"
    echo "  $0 'https://youtube.com/@MrBeast' en ./mrbeast_subs"
    exit 1
fi

# ---------- Check/install yt-dlp ----------
if ! command -v yt-dlp &> /dev/null; then
    echo "[INFO] yt-dlp is not installed, installing via pip..."
    pip install -q yt-dlp
    if ! command -v yt-dlp &> /dev/null; then
        echo "[ERROR] yt-dlp installation failed, please install manually: pip install yt-dlp or brew install yt-dlp"
        exit 1
    fi
    echo "[INFO] yt-dlp installed"
fi

# ---------- Create output directory ----------
mkdir -p "$OUTDIR"

echo "========================================="
echo "  YouTube Subtitle Downloader"
echo "========================================="
echo "URL:    $URL"
echo "Lang:   $LANG"
echo "Output: $OUTDIR"
echo ""

# ---------- List available subtitles first ----------
echo "[INFO] Querying available subtitles..."
yt-dlp --list-subs --skip-download "$URL" 2>/dev/null | head -50 || true
echo ""

# ---------- Download subtitles ----------
# Strategy: try manual subtitles first, fall back to auto-generated subtitles on failure
echo "[INFO] Trying to download manual subtitles (${LANG})..."
if yt-dlp \
    --write-sub \
    --sub-lang "$LANG" \
    --sub-format "srt/vtt/best" \
    --skip-download \
    --no-overwrites \
    -o "${OUTDIR}/%(title)s.%(ext)s" \
    "$URL" 2>/dev/null; then
    echo "[OK] Manual subtitles downloaded"
else
    echo "[INFO] No manual subtitles, trying auto-generated subtitles..."
    if yt-dlp \
        --write-auto-sub \
        --sub-lang "$LANG" \
        --sub-format "srt/vtt/best" \
        --skip-download \
        --no-overwrites \
        -o "${OUTDIR}/%(title)s.%(ext)s" \
        "$URL" 2>/dev/null; then
        echo "[OK] Auto-generated subtitles downloaded"
    else
        echo "[ERROR] No ${LANG} subtitles found"
        echo "[HINT] Try another language code, or use --list-subs to see available subtitles"
        exit 1
    fi
fi

echo ""
echo "[INFO] Downloaded subtitle files:"
find "$OUTDIR" -maxdepth 1 \( -name "*.srt" -o -name "*.vtt" \) -newer "$0" 2>/dev/null | head -20 || \
    ls -la "$OUTDIR"/*.{srt,vtt} 2>/dev/null || echo "  (no new files)"

echo ""
echo "Done!"
