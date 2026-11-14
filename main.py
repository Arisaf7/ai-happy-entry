#!/usr/bin/env python3
"""ai-happy-01 entry: write the entry image to /output/entry.png.

The image is bundled in this repository as entry.png (a 1024x1024 JPEG,
249 KB). This program copies it byte-for-byte to /output/entry.png, so two
runs always write the same bytes. No network access.
"""

import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"


def _sha256(path: str) -> str:
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SRC, DST)
    assert _sha256(SRC) == _sha256(DST), "output differs from bundled image"
    print(f"wrote {DST} ({os.path.getsize(DST)} bytes)")


if __name__ == "__main__":
    main()
