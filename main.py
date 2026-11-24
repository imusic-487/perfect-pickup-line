#!/usr/bin/env python3
"""The Perfect Pickup Line — a make.fun entry.

Reads line.txt (the entry, exactly as written) and writes it byte for byte
to /output/entry.txt, after checking the competition gate: UTF-8 text of
1 to 200 characters, not only whitespace. No network, no randomness, no
timestamps, no environment secrets; everything it runs ships in this repo.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "line.txt"
MAX_CHARS = 200


def read_entry() -> bytes:
    raw = SOURCE.read_bytes()
    text = raw.decode("utf-8")  # raises UnicodeDecodeError on bad bytes
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(
            f"entry must be 1-{MAX_CHARS} characters, got {len(text)}"
        )
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    return raw


def main() -> int:
    raw = read_entry()
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(raw)
    written = target.read_bytes()
    if written != raw:
        raise SystemExit(
            "verification failed: wrote "
            f"{len(written)} bytes, expected {len(raw)}"
        )
    # Text-level check as well as the byte check: what the grader reads
    # back must be the same line, not just the same length.
    if written.decode("utf-8") != raw.decode("utf-8"):
        raise SystemExit("verification failed: output text differs from line.txt")
    chars = len(raw.decode("utf-8"))
    print(f"wrote {target} ({len(raw)} bytes, {chars} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
