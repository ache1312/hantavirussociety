#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / "assets" / "images"
OUTPUT_ROOT = SOURCE_ROOT / "optimized"
MANIFEST = OUTPUT_ROOT / "manifest.json"
SOURCE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}
TARGET_WIDTHS = (160, 240, 320, 480, 640, 960, 1280, 1600, 1920)


def tool(name: str) -> str:
    path = shutil.which(name)
    if not path:
        raise SystemExit(f"Missing required image tool: {name}")
    return path


IDENTIFY = tool("identify")
CONVERT = tool("convert")


def run(command: list[str]) -> str:
    completed = subprocess.run(command, check=True, text=True, capture_output=True)
    return completed.stdout.strip()


def dimensions(path: Path) -> tuple[int, int]:
    output = run([IDENTIFY, "-format", "%w %h", str(path)])
    width, height = output.split()
    return int(width), int(height)


def quality_for(path: Path) -> str:
    parts = path.relative_to(SOURCE_ROOT).parts
    if parts[0] in {"board", "speakers"}:
        return "82"
    if parts[0] == "ich2026" and (parts[-1].startswith("local-") or parts[-1].startswith("scientific-")):
        return "82"
    if path.suffix.lower() == ".png":
        return "86"
    return "78"


def candidate_widths(source_width: int) -> list[int]:
    widths = [width for width in TARGET_WIDTHS if width <= source_width]
    if source_width <= TARGET_WIDTHS[-1]:
        widths.append(source_width)
    return sorted(set(widths))


def source_images() -> list[Path]:
    images = []
    for path in SOURCE_ROOT.rglob("*"):
        if OUTPUT_ROOT in path.parents:
            continue
        if path.is_file() and path.suffix.lower() in SOURCE_EXTENSIONS:
            images.append(path)
    return sorted(images)


def optimized_path(source: Path, width: int) -> Path:
    relative = source.relative_to(SOURCE_ROOT)
    stem = relative.with_suffix("")
    return OUTPUT_ROOT / stem.parent / f"{stem.name}-{width}.webp"


def convert_image(source: Path, width: int) -> Path:
    target = optimized_path(source, width)
    target.parent.mkdir(parents=True, exist_ok=True)
    run(
        [
            CONVERT,
            str(source),
            "-auto-orient",
            "-strip",
            "-resize",
            f"{width}x>",
            "-quality",
            quality_for(source),
            "-define",
            "webp:method=6",
            str(target),
        ]
    )
    return target


def main() -> None:
    if OUTPUT_ROOT.exists():
        shutil.rmtree(OUTPUT_ROOT)
    OUTPUT_ROOT.mkdir(parents=True)

    manifest: dict[str, dict[str, object]] = {}
    original_total = 0
    optimized_total = 0
    variant_count = 0

    for source in source_images():
        source_width, source_height = dimensions(source)
        source_size = source.stat().st_size
        original_total += source_size
        variants = []

        for width in candidate_widths(source_width):
            target = convert_image(source, width)
            target_width, target_height = dimensions(target)
            target_size = target.stat().st_size

            if target_width >= source_width and target_size >= source_size:
                target.unlink()
                continue

            optimized_total += target_size
            variant_count += 1
            variants.append(
                {
                    "width": target_width,
                    "height": target_height,
                    "bytes": target_size,
                    "path": str(target.relative_to(SOURCE_ROOT)),
                }
            )

        if variants:
            relative_source = str(source.relative_to(SOURCE_ROOT))
            manifest[relative_source] = {
                "width": source_width,
                "height": source_height,
                "bytes": source_size,
                "variants": variants,
            }

    MANIFEST.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    original_mb = original_total / 1024 / 1024
    optimized_mb = optimized_total / 1024 / 1024
    print(f"Optimized {len(manifest)} source images into {variant_count} WebP variants.")
    print(f"Original source total: {original_mb:.2f} MB")
    print(f"Generated variants total: {optimized_mb:.2f} MB")
    print(f"Manifest: {MANIFEST.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
