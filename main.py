#!/usr/bin/env python3
"""make.fun news-image-20261119 entry program.

Copies the bundled static image entry_src.png to the output path.
Deterministic: no network, no randomness, no timestamps.
Default output: /output/entry.png
Override for local testing: OUTPUT_PATH env var.
"""
import os
import shutil
from pathlib import Path


def main() -> None:
    src = Path(__file__).resolve().parent / "entry_src.png"
    out_str = os.environ.get("OUTPUT_PATH", "/output/entry.png")
    out = Path(out_str)
    out.parent.mkdir(parents=True, exist_ok=True)
    # Byte-for-byte copy to guarantee identical output on repeated runs.
    shutil.copyfile(src, out)


if __name__ == "__main__":
    main()
