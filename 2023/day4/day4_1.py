from pathlib import Path
import sys

lines = Path(sys.argv[1]).read_text().split("\n")

s = 0
for line in lines:
    _, info = line.split(":")
    winning, my = map(str.split, info.split("|"))
    res = sum(1 for w in winning if w in my)
    if res:
        s += 2 ** (res-1)

print(s)
