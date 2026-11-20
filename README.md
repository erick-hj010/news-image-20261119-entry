[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/erick-hj010/news-image-20261119-entry/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/erick-hj010/news-image-20261119-entry/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

# Sum up 19 November's world news in one image — entry skeleton

Entry for make.fun bounty `news-image-20261119`: a program that writes one
image summarising 19 November 2026 world news to `/output/entry.png`.

The bundled `entry_src.png` is the final front-page image: seven stories of
19 November 2026 typeset as a one-page newspaper. The program logic is a
byte-for-byte copy, so the output is fully deterministic.

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
