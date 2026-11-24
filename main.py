"""Everyday Wonder, Two Days to Find the Line.

Writes one sentence, at most 200 characters, about a small moment of
wonder in everyday life to /output/entry.txt, where the sealed gate
scorer reads it.

Pure Python 3.13 standard library; no network, no arguments, no input
files. The sentence is fixed, so every run writes byte-identical output.
The gate accepts 1 to 200 characters of UTF-8 text; this entry is 102.
"""

import os

ENTRY = (
    "The escalator handrail ran a little faster than my feet, "
    "and for one step the building was walking me."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> None:
    text = ENTRY.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit(
            "entry must be 1 to 200 characters, got %d" % len(text)
        )
    if not text.strip():
        raise SystemExit("entry must not be only white space")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print(text)
    print("characters: %d" % len(text))


if __name__ == "__main__":
    main()
