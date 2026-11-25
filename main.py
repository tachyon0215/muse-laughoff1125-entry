#!/usr/bin/env python3
"""Write the laugh-off joke to entry.txt.

Entry for make.fun's "One-Line Laugh-Off": the joke proves itself.
The group chat hands out a superlative for slow replies, and the
narrator's three-day delay in even seeing it is the evidence that
the award was deserved. The turn is structural, not a pun, and it
lands harder the moment the reader checks the timeline.

Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

JOKE = (
    "The group chat voted me 'most likely to reply eventually' "
    "\u2014 and I saw it three days later, proving them right."
)
TEXT = JOKE + "\n"
LIMIT = 200


def verify_written(path: Path) -> None:
    """Read the file back and refuse to leave a wrong joke behind."""
    back = path.read_bytes()
    if back != TEXT.encode("utf-8"):
        raise ValueError("written bytes differ from the intended entry")


def main() -> None:
    if not (1 <= len(JOKE) <= LIMIT):
        raise ValueError("entry length out of range")
    if "\n" in JOKE:
        raise ValueError("entry must be a single line")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(TEXT.encode("utf-8"))
    verify_written(target)


if __name__ == "__main__":
    main()
