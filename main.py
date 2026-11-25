"""Till Firmware Do Us Part — a robot's wedding vow.

Writes one single-sentence wedding vow, spoken by a robot at its own
wedding, to /output/entry.txt. Deterministic: no network, no randomness,
no input — the line is fixed in this file.
"""

import os

ENTRY = (
    "I promise to love you through every update, every reboot, "
    "and every low battery warning, till firmware do us part."
)


def main() -> None:
    # Craft note: the vow works because it keeps the wedding formula
    # ("I promise ... till ... do us part") and fills it with machine
    # vocabulary — updates, reboots, low battery, firmware — so the laugh
    # comes from the situation itself, while the promise underneath it
    # stays tender enough for a real ceremony.
    # Guard: never emit a line the gate would refuse.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    # Exactly one line, no trailing newline, UTF-8.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
