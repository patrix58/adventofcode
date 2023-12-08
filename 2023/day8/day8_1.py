from pathlib import Path
import sys
import re

PATTERN = re.compile(r"([A-Z]*) = \(([A-Z]*), ([A-Z]*)\)")

lines = Path(sys.argv[1]).read_text().split("\n")

instr = lines[0]
db = {}
for line in lines[2:]:
    m = PATTERN.match(line)
    assert m, line
    node, left, right = m.groups()
    db[node] = (left, right)

i = 0
current = "AAA"
steps = 0
while True:
    if i == len(instr):
        i = 0
    if current == "ZZZ":
        break
    if instr[i] == "L":
        current = db[current][0]
    else:
        current = db[current][1]
    steps += 1
    i += 1

print(steps)
