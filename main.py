#!/usr/bin/env python3
"""Write the entry sentence to /output/entry.txt."""

from pathlib import Path

ENTRY = "This morning my shadow on the wet pavement walked half a step ahead of me, as if it had somewhere better to be."


def main():
    assert 1 <= len(ENTRY) <= 200, len(ENTRY)
    assert ENTRY.strip() == ENTRY
    assert ENTRY.count(".") == 1 and ENTRY.endswith(".")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
