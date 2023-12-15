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

res = 0
for s in strs:
    res += custom_hash(s)

print(res)
