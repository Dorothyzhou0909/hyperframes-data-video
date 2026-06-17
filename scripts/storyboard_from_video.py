#!/usr/bin/env python3
"""Extract representative frames from a video and stack them vertically."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def parse_times(value: str) -> list[str]:
    times = [part.strip() for part in value.split(",") if part.strip()]
    if not times:
        raise argparse.ArgumentTypeError("--times must contain at least one timestamp")
    return times


def run(command: list[str]) -> None:
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as exc:
        raise SystemExit(exc.returncode) from exc


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("video", type=Path, help="Rendered MP4 or other ffmpeg-readable video")
    parser.add_argument("output", type=Path, help="Output PNG path")
    parser.add_argument("--times", required=True, type=parse_times, help="Comma-separated timestamps, e.g. 2.1,7.6,14.7")
    parser.add_argument("--ffmpeg", default=None, help="Path to ffmpeg. Defaults to ffmpeg on PATH")
    args = parser.parse_args()

    ffmpeg = args.ffmpeg or shutil.which("ffmpeg")
    if not ffmpeg:
        print("ffmpeg not found. Pass --ffmpeg /path/to/ffmpeg.", file=sys.stderr)
        return 2

    video = args.video.expanduser().resolve()
    output = args.output.expanduser().resolve()
    if not video.exists():
        print(f"video not found: {video}", file=sys.stderr)
        return 2

    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="data-video-storyboard-") as tmp:
        tmpdir = Path(tmp)
        frames: list[Path] = []
        for index, timestamp in enumerate(args.times, start=1):
            frame = tmpdir / f"frame-{index:02d}.png"
            run([ffmpeg, "-y", "-ss", timestamp, "-i", str(video), "-frames:v", "1", str(frame)])
            frames.append(frame)

        inputs: list[str] = []
        labels: list[str] = []
        for index, frame in enumerate(frames):
            inputs.extend(["-i", str(frame)])
            labels.append(f"[{index}:v]")
        filter_complex = "".join(labels) + f"vstack=inputs={len(frames)}[v]"
        run([ffmpeg, "-y", *inputs, "-filter_complex", filter_complex, "-map", "[v]", "-frames:v", "1", str(output)])

    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
