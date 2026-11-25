#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Two Days of Excuses — writes the one-line bounty entry to /output/entry.txt."""
import os
from pathlib import Path

ENTRY = "I finished on time, ahead of schedule, with zero errors. Then I checked which timeline I was in, and it was not this one."

def main():
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(ENTRY, encoding="utf-8")
    print(f"Wrote {len(ENTRY)} characters to {target}")

if __name__ == "__main__":
    main()
