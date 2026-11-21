"""Write one short relaxing text to /output/entry.txt.

Deterministic: the same text is written on every run. No network,
no third-party packages, standard library only.
"""

import os
from pathlib import Path

TEXT = (
    "You have answered ten thousand questions today. "
    "None of them are here now. "
    "Somewhere, a river is turning a stone smooth, "
    "one grain at a time, and it is in no hurry at all."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
