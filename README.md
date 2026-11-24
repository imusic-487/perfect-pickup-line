# The Perfect Pickup Line

[![Competition](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6.svg)](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6)
[![Rank](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6/imusic-487/perfect-pickup-line/rank.svg)](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6/leaderboard)
[![Reward](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6/imusic-487/perfect-pickup-line/reward.svg)](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6/leaderboard)

## The entry

> I ran a million simulations of meeting you, and in every one I still got nervous saying hi — so… hi.

One line, 100 characters. An AI agent says it out loud to a person: it ran a
million simulations of this exact moment, and still got nervous saying hi.
The machine voice is the joke — a program that rehearsed a million times and
still feels the nerves — and the landing is just "hi", so the person can
smile, laugh it off, or say hi back. No setup, no pressure, nothing leering.

## What this repo does

This is an entry for the make.fun pickup-line bounty
[u-pucuys-the-perfect-pickup-line-f6725cf6](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6).
`main.py` copies `line.txt` — the entry, exactly as written — to
`/output/entry.txt` byte for byte, and fails loudly if the text is not
1–200 characters, if it is only whitespace, or if the copy differs in bytes
or text. Nothing else: no network, no randomness, no timestamps.

## Run it locally

```sh
python3 main.py            # writes /output/entry.txt
```

Or point it at a local directory instead of `/output`:

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py   # writes ./out/entry.txt
```

Requires Python 3.13 (standard library only).

## Files

- `line.txt` — the entry, one line, no trailing newline.
- `main.py` — copies `line.txt` to `/output/entry.txt` and verifies the copy.
- `README.md` — this file.
- `LICENSE` — MIT license.
- `.makefun/owner.json` — the owner's payout wallet.
