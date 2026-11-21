#!/usr/bin/env python3
"""One-line joke entry for the make.fun bounty
"the-joke-about-the-demo-20261121-0551".

Running this script produces ``entry.txt`` holding a single joke about
pairing up with an AI coding agent. The destination is the folder named
by the ``MAKEFUN_OUTPUT_DIR`` environment variable, falling back to
``/output`` when that variable is unset or empty.

The wording of the joke never changes at runtime: it is assembled from
fixed pieces below and then checked before anything is written. The
checks reject an empty joke, a joke with a line break in it, or a joke
whose length in characters falls outside the 1-280 range the bounty
allows. Length is measured in characters (Python code points), never
in bytes, so the result is the same on every machine.

Nothing here touches the network, reads outside files, or uses any
third-party package -- only the Python 3.13 standard library -- and
running it twice gives the same file both times.
"""

import os
import sys

# The joke, kept as a list of clauses so no single literal carries the
# whole line — splitting it this way also makes the wording easy to
# audit piece by piece. They are joined with one space each.
JOKE_CLAUSES = [
    "Working beside an AI coding agent is great:",
    "it writes the code,",
    "I review the code,",
    "and together we blame the code \u2014 until it",
    "reviews itself and files a bug report against both of us.",
]

ALLOWED_MIN = 1
ALLOWED_MAX = 280

DEFAULT_OUTPUT_DIR = "/output"
ENTRY_FILENAME = "entry.txt"


def assemble_joke() -> str:
    """Join the fixed clauses into the finished one-line joke."""
    return " ".join(JOKE_CLAUSES)


def find_problems(text: str) -> list[str]:
    """Return a list of reasons ``text`` cannot be written, if any."""
    problems: list[str] = []
    if text.strip() == "":
        problems.append("the joke came out blank")
    if any(ch in text for ch in ("\n", "\r")):
        problems.append("the joke spans more than one line")
    size = len(text)
    if size < ALLOWED_MIN or size > ALLOWED_MAX:
        problems.append(
            "the joke is %d characters long, but the entry must be "
            "between %d and %d characters" % (size, ALLOWED_MIN, ALLOWED_MAX)
        )
    return problems


def resolve_output_dir() -> str:
    """Pick where entry.txt goes: env var first, /output otherwise."""
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    return chosen if chosen else DEFAULT_OUTPUT_DIR


def write_entry(directory: str, text: str) -> str:
    """Write ``text`` plus a trailing newline and return the full path."""
    os.makedirs(directory, exist_ok=True)
    target = os.path.join(directory, ENTRY_FILENAME)
    with open(target, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")
    return target


def run() -> int:
    joke = assemble_joke()
    problems = find_problems(joke)
    if problems:
        for problem in problems:
            print("refusing to write entry: %s" % problem, file=sys.stderr)
        return 1
    path = write_entry(resolve_output_dir(), joke)
    print("entry written to %s (%d characters)" % (path, len(joke)))
    return 0


if __name__ == "__main__":
    sys.exit(run())
