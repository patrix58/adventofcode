from pathlib import Path
import sys
import numpy as np


def check_reflection(table):
    for y in range(1, table.shape[0]):
        up = table[max(0, y+y-min(y+y, table.shape[0])):y, :]
        down = np.flipud(table[y:min(y+y, table.shape[0]), :])
        assert up.shape == down.shape
        if np.sum(up == down) == up.shape[0]*up.shape[1]-1:
            return y*100
    for x in range(1, table.shape[1]):
        left = table[:, max(0, x+x-min(x+x, table.shape[1])):x]
        right = np.fliplr(table[:, x:min(x+x, table.shape[1])])
        assert left.shape == right.shape
        if np.sum(left == right) == left.shape[0]*left.shape[1]-1:
            return x
    raise ValueError(f"No reflection found \n{table}")


lines = Path(sys.argv[1]).read_text().split("\n") + [""]
prev = 0
current = lines.index("")
s = 0
while current:
    table = np.array([[e for e in line] for line in lines[prev:current]])
    s += check_reflection(table)
    prev = current+1
    try:
        current = lines.index("", current+1)
    except:
        break
print(s)
