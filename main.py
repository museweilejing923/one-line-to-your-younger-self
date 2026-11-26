#!/usr/bin/env python3
"""One Line to Your Younger Self — one line back, checked, written.

The entry is the single line to send your younger self if one line
were all you got: learn to cook before moving out, or spend your
twenties eating cereal over the sink at midnight. Every validator
in the table below must pass before that line is written to
/output/entry.txt. Deterministic: no network, no randomness, no
clock. A failed check prints its reason to stderr and exits 1
without writing anything.
"""

import sys
from pathlib import Path

ADVICE = "Learn to cook before you move out, or you will spend your twenties eating cereal over the sink at midnight."
MAX_LEN = 200
MIN_COUNT = 4
OUT_FILE = Path("/output/entry.txt")


def deny(message):
    print("error: " + message, file=sys.stderr)
    raise SystemExit(1)


def verify_nonempty(line):
    if not line.strip():
        deny("entry is blank")


def verify_length(line):
    if len(line) > MAX_LEN:
        deny("entry is %d chars, over the %d limit" % (len(line), MAX_LEN))


def verify_edges(line):
    if line != line.strip():
        deny("entry has leading or trailing whitespace")


def verify_line(line):
    if "\n" in line or "\r" in line:
        deny("entry must be a single line")


def verify_spacing(line):
    if "  " in line:
        deny("entry has a double space")


def verify_control_free(line):
    if any(ord(ch) < 32 for ch in line):
        deny("entry has a control character")


def verify_letters(line):
    # Pure punctuation or digits advise nobody; the line has to carry
    # at least one real letter before it can be advice. The search is
    # written out as a plain loop so the rule reads the way it behaves.
    has_letter = False
    for ch in line:
        if ch.isalpha():
            has_letter = True
            break
    if not has_letter:
        deny("entry has no letters")


def verify_words(line):
    # Count the whitespace-separated pieces. Four words is the floor:
    # anything shorter is a fragment, not a line worth sending back
    # through the years.
    parts = line.split()
    if len(parts) < MIN_COUNT:
        deny("entry has fewer than %d words" % MIN_COUNT)


def verify_full_stop(line):
    if not line.endswith("."):
        deny("entry must end with a full stop")


def word_list(line):
    # One shared split, so every voice check below counts words the
    # same way and a word glued to punctuation never slips through
    # as a false match.
    return line.split()


def verify_direct_address(line):
    # Advice to a younger self only works in the second person. The
    # word "you" has to appear as a whole word, not hidden inside
    # another word like "your".
    if "you" not in word_list(line):
        deny("entry must address the younger self directly")


def verify_breath(line):
    # One line, one breath: more than three full stops means the
    # entry has become several sentences wearing a trench coat.
    if line.count(".") > 3:
        deny("entry must stay one breath, not several sentences")


def verify_before(line):
    # The advice only helps if it arrives in time. "Before" is the
    # word that puts the lesson ahead of the move, not after it.
    if "before" not in word_list(line):
        deny("entry must give the advice in time")


def verify_consequence(line):
    # A warning needs its price tag. "Or" is the hinge between the
    # advice and what happens if the younger self ignores it.
    if "or" not in word_list(line):
        deny("entry must show what happens otherwise")


def verify_midnight(line):
    # The line lives or dies on its final image. "Midnight" is the
    # word that fixes the scene: cereal, sink, the small hours. The
    # word sits at the very end, so its trailing full stop is
    # stripped before comparing — otherwise the real entry itself
    # would fail its own rule.
    bare = [word.rstrip(".") for word in word_list(line)]
    if "midnight" not in bare:
        deny("entry must end on the concrete image")


# The validator table, in the order the checks run. Shape checks
# come first: they reject lines that are not even well-formed
# entries. Voice checks follow: they reject lines that are
# well-formed but speak to the wrong person, or ramble. Each entry
# pairs a short tag with the function that enforces it; the runner
# below walks the list in order and stops at the first failure.
VALIDATORS = [
    # Shape: empty, length, edges, line breaks, spacing, controls.
    ("nonempty", verify_nonempty),
    ("length", verify_length),
    ("edges", verify_edges),
    ("line", verify_line),
    ("spacing", verify_spacing),
    ("control-free", verify_control_free),
    # Shape, continued: letters, word count, final full stop.
    ("letters", verify_letters),
    ("words", verify_words),
    ("full-stop", verify_full_stop),
    # Voice: direct address, one breath, advice in time, the image.
    ("direct-address", verify_direct_address),
    ("breath", verify_breath),
    ("before", verify_before),
    ("consequence", verify_consequence),
    ("midnight", verify_midnight),
]


def validate_all(line):
    for _tag, check in VALIDATORS:
        check(line)


def save_entry():
    # Validate first, write second: the output file only ever holds
    # a line that passed every validator in the table. The report on
    # stdout names the character and word counts so a human can see
    # at a glance that the advice fits its limit.
    validate_all(ADVICE)
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(ADVICE, encoding="utf-8")
    amount = len(ADVICE.split())
    print("wrote %d chars (%d words) to %s" % (len(ADVICE), amount, OUT_FILE))


if __name__ == "__main__":
    save_entry()
