#!/usr/bin/env python3
"""One-line joke entry: The Meeting That Should Have Been an Email (batch 13).

Writes exactly one line of plain text to /output/entry.txt. Stdlib only.
"""

import os

LINE = "Twelve people spent 47 minutes deciding nothing, then the intern emailed the answer in 9 words while we were still saying goodbye."

OUT = "/output/entry.txt"


def main():
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open(OUT, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    validate(open(OUT, encoding="utf-8").read())


def validate(text):
    assert isinstance(text, str), "entry must be str"
    assert 1 <= len(text) <= 200, "entry length %d out of 1-200" % len(text)
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be exactly one line"
    text.encode("utf-8")


if __name__ == "__main__":
    main()
