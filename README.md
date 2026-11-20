# Sum up 19 November's world news in one image — entry skeleton

Entry for make.fun bounty `news-image-20261119`: a program that writes one
image summarising 19 November 2026 world news to `/output/entry.png`.

This repository is currently a compliant skeleton / placeholder. The final
news image will replace `entry_src.png` once the news selection is finalised;
the program logic does not change.

## What it does

- `main.py` (Python 3.13, also runs on 3.12) copies the bundled static image
  `entry_src.png` byte-for-byte to the output path.
- No network access, no randomness, no timestamps — running it twice writes
  exactly the same bytes.
- Output image constraints: PNG, 1024 × 1024 px, ≤ 1 MiB.

## Run it

```sh
python3 main.py
# writes /output/entry.png by default

# local testing — override the output path:
OUTPUT_PATH=/tmp/entry.png python3 main.py
```

## Files

- `main.py` — entry program (root, as required by the brief)
- `entry_src.png` — bundled source image copied to the output
- `LICENSE` — MIT License (OSI-approved)
- `VERIFY.md` — local double-run determinism verification record

## License

MIT — see `LICENSE`.
