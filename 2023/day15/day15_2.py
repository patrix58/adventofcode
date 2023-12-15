from pathlib import Path
import sys

strs = Path(sys.argv[1]).read_text().split(",")

def custom_hash(s):
    h = 0
    for c in s:
        h += ord(c)
        h *= 17
        h %= 256
    return h


boxes = [[] for _ in range(256)]

for s in strs:
    if "=" in s:
        ident, foc = s.split("=")
        foc = int(foc)
        box_nr = custom_hash(ident)
        pos = None
        for p, (i, f) in enumerate(boxes[box_nr]):
            if i == ident:
                pos = p
                break
        if pos is None:
            boxes[box_nr].append((ident, foc))
        else:
            boxes[box_nr][pos] = (ident, foc)
    else:
        ident = s[:-1]
        box_nr = custom_hash(ident)
        pos = None
        for p, (i, f) in enumerate(boxes[box_nr]):
            if i == ident:
                pos = p
                break
        if pos is not None:
            del boxes[box_nr][pos]

res = 0
for i, b in enumerate(boxes):
    for j, (_, f) in enumerate(b):
        res += (i+1) * (j+1) * f

print(res)
