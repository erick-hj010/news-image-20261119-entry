# Verification — double-run determinism & compliance

Date: 2026-11-20 (local verification, placeholder image — not the final news image)
Environment: Python 3.12.3 locally (entry targets Python 3.13, code uses only stdlib), Pillow 10.2.0 for placeholder generation / checks only — `main.py` itself uses stdlib only.

## Commands run

```sh
cd ~/workspace/makefun-probe/entry
mkdir -p /tmp/makefun-verify/run1 /tmp/makefun-verify/run2
OUTPUT_PATH=/tmp/makefun-verify/run1/entry.png python3 main.py
OUTPUT_PATH=/tmp/makefun-verify/run2/entry.png python3 main.py
sha256sum entry_src.png /tmp/makefun-verify/run1/entry.png /tmp/makefun-verify/run2/entry.png
cmp /tmp/makefun-verify/run1/entry.png /tmp/makefun-verify/run2/entry.png
file entry_src.png
python3 -c "from PIL import Image; im=Image.open('entry_src.png'); print(im.size, im.format, im.mode)"
```

## Hash results (must match)

```
4741ef3dbff8c46f8c56fe37487088e519f35686092535033e9f14972381ec42  entry_src.png
4741ef3dbff8c46f8c56fe37487088e519f35686092535033e9f14972381ec42  /tmp/makefun-verify/run1/entry.png
4741ef3dbff8c46f8c56fe37487088e519f35686092535033e9f14972381ec42  /tmp/makefun-verify/run2/entry.png
```

- `cmp run1/entry.png run2/entry.png` → identical (no output, exit 0)
- `cmp entry_src.png run1/entry.png` → identical
- **Double-run byte-identical: YES**

## Compliance checks

| Check | Requirement | Actual | Pass |
|---|---|---|---|
| Format | PNG or JPEG | PNG | ✅ |
| Dimensions | ≤ 1024 × 1024 | 1024 × 1024 | ✅ |
| File size | ≤ 1 MiB (1,048,576 bytes) | 32,471 bytes | ✅ |
| Network use | none | `main.py` uses only `os`, `shutil`, `pathlib` — no network | ✅ |
| Determinism | two runs → same bytes | sha256 identical (above) | ✅ |
| Default output | `/output/entry.png` | default in code; `OUTPUT_PATH` only overrides for local tests | ✅ |
| Entry point | `main.py` in repo root | present | ✅ |
| License | OSI-approved | MIT (`LICENSE`) | ✅ |

## Notes

- Placeholder image: 1024×1024, dark background (RGB 18,22,38), large text "19 NOV / 2026" + "WORLD NEWS — PLACEHOLDER", generated with Pillow + DejaVuSans-Bold.
- Final step (separate task): replace `entry_src.png` with the final news image, keep it ≤1 MiB / ≤1024×1024, re-run this verification.
