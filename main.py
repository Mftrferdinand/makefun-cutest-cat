#!/usr/bin/env python3
"""
Cutest cat entry for make.fun bounty cutest-cat-01
Copies pre-selected adorable kitten image to output
"""

import shutil
from pathlib import Path


def main():
    source = Path(__file__).parent / "cat_source.jpg"
    output = Path("/output/entry.png")
    output.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(source, output)
    print(f"Copied cute cat to {output}")


if __name__ == "__main__":
    main()
