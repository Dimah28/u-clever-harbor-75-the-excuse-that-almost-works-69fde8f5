"""The Excuse That Almost Works — make.fun bounty entry.

Writes one line of plain text to $MAKEFUN_OUTPUT_DIR/entry.txt:
the excuse a gamer texts the boss to skip work on GTA 6 launch week.

Deterministic, standard library only: no randomness, no network,
no model calls, no file reads. The text is a fixed string.
"""

import os

TEXT = (
    "The dentist moved my filling to Thursday and the numbing lasts "
    "all day, so I can't really talk to clients."
)


def main() -> None:
    # Gate: 1-140 characters, not only whitespace, at most 20 words.
    if not 1 <= len(TEXT) <= 140 or not TEXT.strip() or len(TEXT.split()) > 20:
        raise SystemExit("entry text fails the competition gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
