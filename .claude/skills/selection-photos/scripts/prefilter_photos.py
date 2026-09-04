#!/usr/bin/env python3
"""Pre-filter a folder of raw Instagram photos (e.g. an Apify scrape dump)
before the qualitative visual review.

Pure standard library — no Pillow/ImageMagick dependency, so it runs
anywhere Python 3 runs. Reads just enough of each file's header to get its
pixel dimensions (JPEG, PNG, WEBP), flags files that are technically unusable
for image-to-video (too low resolution, corrupt/unreadable, extreme aspect
ratio), and ranks the rest by resolution so the qualitative review (done by
reading the actual images) focuses on the strongest candidates first instead
of wasting attention on a folder that might hold hundreds of scraped photos.

Usage:
    python3 prefilter_photos.py /path/to/raw/photos/folder [--min-side 1080]

Prints a JSON report to stdout: {"candidates": [...], "rejected": [...]}
"""
import argparse
import json
import os
import struct
import sys

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}


def get_image_size(path: str):
    """Return (width, height) or None if the file can't be parsed."""
    with open(path, "rb") as f:
        head = f.read(32)

        # PNG
        if head[:8] == b"\x89PNG\r\n\x1a\n":
            w, h = struct.unpack(">II", head[16:24])
            return w, h

        # JPEG — scan markers for the first SOF segment
        if head[:2] == b"\xff\xd8":
            f.seek(2)
            while True:
                marker_bytes = f.read(2)
                if len(marker_bytes) < 2 or marker_bytes[0] != 0xFF:
                    return None
                marker = marker_bytes[1]
                if marker in (0xD8, 0x01) or 0xD0 <= marker <= 0xD7:
                    continue
                seg_len_bytes = f.read(2)
                if len(seg_len_bytes) < 2:
                    return None
                seg_len = struct.unpack(">H", seg_len_bytes)[0]
                if marker in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
                              0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                    data = f.read(5)
                    if len(data) < 5:
                        return None
                    h, w = struct.unpack(">HH", data[1:5])
                    return w, h
                f.seek(seg_len - 2, os.SEEK_CUR)

        # WEBP (VP8/VP8L/VP8X)
        if head[:4] == b"RIFF" and head[8:12] == b"WEBP":
            chunk = head[12:16]
            if chunk == b"VP8 ":
                w, h = struct.unpack("<HH", head[26:30])
                return w & 0x3FFF, h & 0x3FFF
            if chunk == b"VP8L":
                b0, b1, b2, b3 = head[21], head[22], head[23], head[24]
                w = 1 + (((b1 & 0x3F) << 8) | b0)
                h = 1 + (((b3 & 0xF) << 10) | (b2 << 2) | (b1 >> 6))
                return w, h

    return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("folder")
    parser.add_argument("--min-side", type=int, default=1080,
                         help="Résolution minimale du plus petit côté (px)")
    parser.add_argument("--max-aspect", type=float, default=2.2,
                         help="Ratio largeur/hauteur (ou inverse) max toléré")
    args = parser.parse_args()

    if not os.path.isdir(args.folder):
        print(f"Dossier introuvable : {args.folder}", file=sys.stderr)
        sys.exit(1)

    candidates = []
    rejected = []

    for name in sorted(os.listdir(args.folder)):
        ext = os.path.splitext(name)[1].lower()
        if ext not in IMAGE_EXTENSIONS:
            continue
        path = os.path.join(args.folder, name)
        size = get_image_size(path)
        file_size_kb = round(os.path.getsize(path) / 1024, 1)

        if size is None:
            rejected.append({"file": name, "reason": "dimensions illisibles / fichier corrompu"})
            continue

        w, h = size
        short_side = min(w, h)
        aspect = max(w, h) / min(w, h) if min(w, h) else 999

        if short_side < args.min_side:
            rejected.append({
                "file": name, "width": w, "height": h,
                "reason": f"résolution trop faible ({short_side}px < {args.min_side}px)",
            })
            continue
        if aspect > args.max_aspect:
            rejected.append({
                "file": name, "width": w, "height": h,
                "reason": f"ratio extrême ({aspect:.2f}:1)",
            })
            continue

        candidates.append({
            "file": name, "width": w, "height": h,
            "short_side": short_side, "file_size_kb": file_size_kb,
        })

    candidates.sort(key=lambda c: c["short_side"], reverse=True)

    print(json.dumps({"candidates": candidates, "rejected": rejected}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
