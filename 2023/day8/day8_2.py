from pathlib import Path
import sys
import re
import numpy as np

PATTERN = re.compile(r"([A-Z\d]*) = \(([A-Z\d]*), ([A-Z\d]*)\)")

lines = Path(sys.argv[1]).read_text().split("\n")

instr = lines[0]
nodes = []
lefts = []
rights = []
for line in lines[2:]:
    m = PATTERN.match(line)
    assert m, line
    node, left, right = m.groups()
    nodes.append(node)
    lefts.append(left)
    rights.append(right)

nodes = np.array(nodes)
lefts = np.array(lefts)
rights = np.array(rights)

i = 0
currents = np.array([node for node in nodes if node.endswith("A")])
steps = 0
while True:
    # print(f"step = {steps+1}, currents = {currents}")
    if i == len(instr):
        i = 0
    if np.all(np.char.endswith(currents, "Z")):
        break
    pos = np.where(np.isin(nodes, currents))[0]
    # print(f"pos = {pos}")
    # print(f"going {instr[i]}")
    if instr[i] == "L":
        currents = lefts[pos]
    else:
        currents = rights[pos]
    steps += 1
    i += 1

print(steps)
