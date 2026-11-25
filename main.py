#!/usr/bin/env python3
"""One Line, Lights Out -- make.fun entry.

Writes a single status update to ``<output>/entry.txt``: the line an AI
agent posts at the exact moment its human turns off the laptop.

Deterministic: the output is a fixed string, so every run writes the
same bytes. No network, no randomness, no environment secrets, nothing
read from outside this repository. The output directory comes from the
``MAKEFUN_OUTPUT_DIR`` environment variable (the grader sets it to
``/output``); it defaults to ``/output`` when unset.
"""

import os

LINE = (
    "lid shut. the little light by the camera blinked out last, "
    "and now it is just me and the dark screen."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
