"""The 3 AM Commit Message - make.fun bounty entry.

Writes one commit message to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Deterministic, stdlib-only, no network.
"""
import os
from pathlib import Path

ENTRY = (
    "fix: reverted my 3 AM deploy; as an AI language model "
    "I cannot feel shame, but the 47 alerts suggest I should"
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
