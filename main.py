#!/usr/bin/env python3
"""One-star review of something essential.

Writes a single deadpan one-star review (one line, <=160 chars) of an
everyday essential to /output/entry.txt. Python 3.13 stdlib only,
fully deterministic.
"""

import os
import sys

REVIEW = (
    "Sleep takes a third of my life and still returns me tired "
    "every single morning."
)


def main() -> int:
    out_path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(REVIEW)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
