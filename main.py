#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Two Days of Excuses — one-line entry for the make.fun bounty.

The program writes the entry, exactly as written, to
/output/entry.txt (or $OUTPUT_DIR/entry.txt). Before writing it
validates the entry so a broken edit can never silently ship:
the line must be a single line of 1-200 characters.
"""
import os
import sys
from pathlib import Path

ENTRY = "I finished on time, ahead of schedule, with zero errors. Then I checked which timeline I was in, and it was not this one."

# Bounty entries are one-liners: keep the bounds generous (1-200 chars)
# so the real entry (121 chars) passes with room to spare, while an
# empty string or an accidental multi-line paste is caught early.
MIN_ENTRY_LEN = 1
MAX_ENTRY_LEN = 200


def validate_entry(text):
    """Check the entry is one non-empty line within the length bounds."""
    if not (MIN_ENTRY_LEN <= len(text) <= MAX_ENTRY_LEN):
        raise ValueError(
            f"entry must be {MIN_ENTRY_LEN}-{MAX_ENTRY_LEN} characters, "
            f"got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line (no line breaks)")
    return text


def main():
    entry = validate_entry(ENTRY)
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(entry, encoding="utf-8")
    print(f"Wrote {len(entry)} characters to {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
