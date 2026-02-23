import os
import sys

print("--- DEBUG BUNDLE STRUCTURE ---")
if getattr(sys, 'frozen', False):
    print(f"Bundle Root: {sys._MEIPASS}") # pyright: ignore[reportAttributeAccessIssue]
    for root, dirs, files in os.walk(sys._MEIPASS): # pyright: ignore[reportAttributeAccessIssue]
        level = root.replace(sys._MEIPASS, '').count(os.sep) # pyright: ignore[reportAttributeAccessIssue]
        indent = ' ' * 4 * (level)
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(f"{subindent}{f}")
print("--- END DEBUG ---")

from qanotz.__main__ import main

if __name__ == "__main__":
    main()