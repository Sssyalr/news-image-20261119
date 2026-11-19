#!/usr/bin/env python3
"""Write the entry image to the make.fun output directory.

The front page image (entry.png) is rendered during the build and committed
next to this script. This program only copies it into the output directory,
so it needs nothing beyond the standard library and always writes the same
bytes. Run: python3 main.py  (honours $MAKEFUN_OUTPUT_DIR when set).
"""

import os
import shutil
import sys
from pathlib import Path

IMAGE = "entry.png"


def main():
    here = Path(__file__).resolve().parent
    src = here / IMAGE
    if not src.is_file():
        print(f"error: {IMAGE} not found beside {__file__}", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or str(here))
    out_dir.mkdir(parents=True, exist_ok=True)
    dst = out_dir / IMAGE
    if dst.resolve() != src.resolve():
        shutil.copyfile(src, dst)
    if dst.stat().st_size != src.stat().st_size:
        print("error: size mismatch after copy", file=sys.stderr)
        return 1
    print(f"wrote {dst} ({dst.stat().st_size} bytes, verified)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
