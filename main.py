#!/usr/bin/env python3
"""The Funniest Office Joke, Judged Head to Head — Account A entry.

Writes one office joke, a single line, to /output/entry.txt.

Premise: the office printer is an oracle that only speaks in paper jams.
It has read every document that ever passed through it, so it knows
everyone's secrets — and it jams precisely when the important document
is due, because some secrets are safer stuck inside it.

Judge-brief mapping (brief published with the bounty):
  1. One-line joke about office life, setup + turn, punchline last.
     Setup: the printer only jams on the document you actually need.
     Turn: it jams on purpose — it has read them all.
     Punchline (last): some secrets are safer jammed inside it — the
     word "jammed" closes the loop on the jam itself, so the punchline
     is the setup's own word turned back on it.
  2. Universal office truth: the printer that jams on the deadline —
     named in the brief itself.
  3. Surprise: a jam is not a malfunction but a deliberate act of
     discretion by a machine that knows too much.
  4. One line, every word earning its place, punchline last.
  5. Fresh angle: the printer as an all-knowing oracle, not the usual
     "printer broken again" complaint.
"""

import os

ENTRY = (
    "The office printer only ever jams on the document you actually need "
    "\u2014 it\u2019s read them all, and some secrets are safer jammed inside it."
)

MAX_CHARS = 200


def validate(text):
    """Check the entry against the gate in RULES.txt."""
    if not isinstance(text, str):
        raise TypeError("entry must be str")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(
            "entry must be 1 to %d characters, got %d" % (MAX_CHARS, len(text))
        )
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text.strip():
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # must be valid UTF-8 text
    return text


def write_entry(path="/output/entry.txt"):
    """Validate the joke and write it to path (default /output/entry.txt)."""
    text = validate(ENTRY)
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


if __name__ == "__main__":
    write_entry()
    print("wrote %d characters to /output/entry.txt" % len(ENTRY))
