#!/bin/bash
# Tải phụ đề từ video YouTube.
# Cách dùng: ./download_subtitles.sh <YouTube_URL> [thư_mục_đầu_ra]
# Ưu tiên phụ đề do người tạo; nếu không có thì tải phụ đề tự động.
# Thứ tự ngôn ngữ: tiếng Anh > tiếng Việt > tiếng Trung.

set -e

URL="$1"
OUTPUT_DIR="${2:-.}"

if [ -z "$URL" ]; then
    echo "Cách dùng: ./download_subtitles.sh <YouTube_URL> [thư_mục_đầu_ra]"
    exit 1
fi

mkdir -p "$OUTPUT_DIR"

echo ">>> Đang kiểm tra phụ đề có sẵn..."
yt-dlp --list-subs --no-download "$URL" 2>/dev/null | tail -20

echo ""
echo ">>> Đang thử tải phụ đề do người tạo (ưu tiên tiếng Anh)..."

# Lần thử 1: phụ đề tiếng Anh do người tạo.
if yt-dlp --write-subs --sub-langs "en,en-US,en-GB" --sub-format srt --skip-download -o "$OUTPUT_DIR/%(title)s" "$URL" 2>/dev/null; then
    FOUND=$(find "$OUTPUT_DIR" -name "*.srt" -newer /tmp/.ytdlp_marker 2>/dev/null | head -1)
    if [ -n "$FOUND" ]; then
        echo "✅ Tải thành công: $FOUND"
        exit 0
    fi
fi

# Lần thử 2: phụ đề tiếng Việt do người tạo.
echo ">>> Không có phụ đề tiếng Anh do người tạo, đang thử tiếng Việt..."
if yt-dlp --write-subs --sub-langs "vi,vi-VN" --sub-format srt --skip-download -o "$OUTPUT_DIR/%(title)s" "$URL" 2>/dev/null; then
    FOUND=$(find "$OUTPUT_DIR" -name "*.srt" -mmin -1 2>/dev/null | head -1)
    if [ -n "$FOUND" ]; then
        echo "✅ Tải thành công: $FOUND"
        exit 0
    fi
fi

# Lần thử 3: phụ đề tự động, theo thứ tự tiếng Anh, tiếng Việt rồi tiếng Trung.
echo ">>> Không có phụ đề do người tạo, đang thử phụ đề tự động..."
if yt-dlp --write-auto-subs --sub-langs "en,en-US,en-GB,vi,vi-VN,zh-Hans,zh-Hant,zh,zh-CN,zh-TW" --sub-format srt --skip-download -o "$OUTPUT_DIR/%(title)s" "$URL" 2>/dev/null; then
    FOUND=$(find "$OUTPUT_DIR" -name "*.srt" -o -name "*.vtt" 2>/dev/null | head -1)
    if [ -n "$FOUND" ]; then
        echo "✅ Tải phụ đề tự động thành công: $FOUND"
        exit 0
    fi
fi

echo "❌ Không tìm thấy phụ đề khả dụng"
exit 1
