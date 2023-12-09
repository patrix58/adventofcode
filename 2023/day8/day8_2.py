from pathlib import Path
import sys
import re

PATTERN = re.compile(r"([A-Z\d]*) = \(([A-Z\d]*), ([A-Z\d]*)\)")

lines = Path(sys.argv[1]).read_text().split("\n")

instr = lines[0]

db = {}
for line in lines[2:]:
    m = PATTERN.match(line)
    assert m, line
    node, left, right = m.groups()
    db[node] = (left, right)


currents = [node for node in db if node.endswith("A")]
nrzs = len([node for node in db if node.endswith("Z")])
zzs = {}

for current in currents:
    zs = {}
    scurrent = current
    zzs[scurrent] = []
    steps = 0
    i = 0
    while len(zzs[scurrent]) < nrzs and steps < 1_000_000:
        if i == len(instr):
            i = 0
        if current.endswith("Z"):
            if current in zs and zs[current] is not None:
                zzs[scurrent].append((current, zs[current], steps - zs[current]))
                zs[current] = None
            elif current not in zs:
                zs[current] = steps

        if instr[i] == "L":
            current = db[current][0]
        else:
            current = db[current][1]
        steps += 1
        i += 1

print(zzs)

nrs = [e[0][1] for e in zzs.values()]

def lnko(a, b):
    r = a % b
    while r:
        a = b
        b = r
        r = a % b
    return b

p = 1
for nr in nrs:
    p *= nr // lnko(p, nr)

print(p)
