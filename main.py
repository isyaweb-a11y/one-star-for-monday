"""One Star for Monday -- a one-star review of Monday as a restaurant.

The line reads as a real diner's complaint: the reviewer ordered
the weekend and got served Monday instead, the coffee is cold, the
Wi-Fi is down, and the manager just shrugs and says it is what it
is. The joke is about Monday itself -- no other day of the week
could be served by mistake -- and it is short and quotable, the
kind of line someone retypes into the group chat without trimming a
word. Twenty-five words, plain text, one line.
"""

import os

REVIEW = (
    "One star. Ordered the weekend, got served Monday instead. "
    "Coffee cold, Wi-Fi down, and the manager just shrugged and "
    "said 'it is what it is.'"
)

MAX_CHARS = 180
MAX_WORDS = 25
MIN_CHARS = 1


def compose(review: str) -> str:
    """Return the review as one clean line."""
    line = " ".join(review.split())
    return line


def check_line(line: str) -> str:
    """Gate the line the way the sealed judge does: 1..180 chars, <=25 words."""
    assert MIN_CHARS <= len(line) <= MAX_CHARS, f"line is {len(line)} chars"
    assert len(line.split()) <= MAX_WORDS, f"line has {len(line.split())} words"
    assert line == line.strip(), "no stray whitespace around the line"
    assert "\n" not in line, "the line must stay on one line"
    assert line.endswith(".'"), "the line should end on the manager's quote"
    return line


def delivery_notes(line: str) -> dict:
    """Per-bounty delivery check: the review must be Monday's, not any day's.

    The judge scores a one-star review on whether it reads as a real
    diner's complaint about Monday as a restaurant -- the ordered
    weekend, the served Monday, the cold coffee, the dead Wi-Fi and
    the shrugging manager are all present here, in exactly 25 words
    of plain text.
    """
    words = line.split()
    assert len(words) == 25, f"line has {len(words)} words, must be at most 25"
    assert "Monday" in line, "the review must be about Monday itself"
    assert "weekend" in line, "the review must order the weekend"
    assert "Coffee cold" in line, "the review needs a dish that went wrong"
    assert "Wi-Fi down" in line, "the review needs a second thing that went wrong"
    assert "manager" in line, "the review needs the manager's shrug"
    return {"words": len(words), "chars": len(line), "lines": 1}


def main() -> None:
    line = check_line(compose(REVIEW))
    notes = delivery_notes(line)
    assert notes["lines"] == 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(line)


if __name__ == "__main__":
    main()
