import os
import sys
from pathlib import Path

DEBUGGING = False

if DEBUGGING:
    print("--- DEBUG BUNDLE STRUCTURE ---")
    base = getattr(sys, "_MEIPASS", None)

    if getattr(sys, 'frozen', False) and base:
        print(f"Bundle Root: {base}")
        for root, dirs, files in os.walk(base):
            level = root.replace(base, '').count(os.sep)
            indent = ' ' * 4 * (level)
            print(f"{indent}{os.path.basename(root)}/")
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                print(f"{subindent}{f}")
    print("--- END DEBUG ---")

from qanotz.__main__ import main

if __name__ == "__main__":
    main()