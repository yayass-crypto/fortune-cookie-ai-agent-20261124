#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent.

Writes a single fortune-cookie line for an AI agent to /output/entry.txt.
One line, one scene, one twist — the laugh lands on the last words.
"""

import os

ENTRY = (
    "You will find love in unexpected places, starting with the recycle bin "
    "where your old prompts live."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
