#!/usr/bin/env python3
"""Entry point for news-image-20261119.

Copies the pre-rendered front page (entry.png, shipped in this repo) to
the output directory make.fun asks for. Standard library only: the
scoring sandbox has no third-party packages, so this file imports
nothing beyond os, shutil, sys and pathlib.
"""
import os
import shutil
import sys
from pathlib import Path


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    src = Path(__file__).resolve().parent / "entry.png"
    if not src.is_file():
        print("entry.png not found beside main.py", file=sys.stderr)
        return 1
    dest = Path(out_dir) / "entry.png"
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dest)
    if dest.stat().st_size != src.stat().st_size:
        print("copy failed: size mismatch", file=sys.stderr)
        return 1
    print("wrote " + str(dest) + " (" + str(dest.stat().st_size) + " bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
