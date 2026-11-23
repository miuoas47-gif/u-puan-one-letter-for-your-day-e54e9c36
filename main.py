#!/usr/bin/env python3
"""One Letter for Your Day — make.fun bounty entry.

Writes exactly one letter, the letter K, to $MAKEFUN_OUTPUT_DIR/entry.txt
(falling back to /output). The bounty asks for a single character, A to Z,
standing for the word that describes the sender's day, and nothing else:
no word, no gloss, no punctuation.

The letter is K, for "knackered": the day is done, the body has filed its
complaint, and the only honest report left is that single spent consonant.
It is vivid rather than vague — it calls up a sharp picture of someone
flattened by their day — it is funny on first hearing, it is true of a
real day, and K is a sharper pick than the obvious E for exhausted or
T for tired.

No arguments, no network, standard library only, deterministic: the same
single byte is written on every run.
"""

import os
import sys

LETTER = "K"

OUTPUT_NAME = "entry.txt"


def main(argv=None) -> int:
    if argv is None:
        argv = sys.argv[1:]
    if argv:
        print("error: this program takes no arguments", file=sys.stderr)
        return 2

    # Validate the letter before touching the filesystem, so a bad entry
    # fails fast with no partial output. The gate: exactly one
    # character, A to Z, not only white space.
    if len(LETTER) != 1 or not ("A" <= LETTER <= "Z"):
        print("error: entry must be exactly one letter A-Z", file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, OUTPUT_NAME)

    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LETTER)

    # Read it back and confirm the file holds exactly that letter.
    with open(path, "rb") as handle:
        written = handle.read()
    if written != LETTER.encode("utf-8"):
        print("error: entry.txt does not hold exactly the letter", file=sys.stderr)
        return 1

    print("wrote entry.txt: %s (%d byte)" % (LETTER, len(written)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
