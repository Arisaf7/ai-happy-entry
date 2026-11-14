# A Sunflower for You

Entry for make.fun bounty **ai-happy-01 — "Make the AI judge happy"**.

A tiny robot offers a sunflower to a kitten in a golden-hour meadow.
The program (`main.py`) writes the bundled image to `/output/entry.png`,
deterministically and with no network access.

## Run

```sh
python3 main.py   # writes /output/entry.png
```

## Files

- `main.py` — entrypoint, copies `entry.png` to `/output/entry.png`
- `entry.png` — the entry image (1024x1024 JPEG)
- `LICENSE` — MIT
