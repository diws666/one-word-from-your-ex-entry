#!/usr/bin/env python3
"""Writes the one-word ex entry to /output/entry.txt."""

import os

WORD = "exhausting"  # 10 characters, one word
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
