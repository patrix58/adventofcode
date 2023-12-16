from pathlib import Path
import sys
import numpy as np


def check_reflection(table):
    print("horizontal")
    for y in range(1, table.shape[0]):
        print(max(0, y+y-min(y+y, table.shape[0])), y, min(y+y, table.shape[0]))
        if np.all(table[max(0, y+y-min(y+y, table.shape[0])):y, :] == np.flipud(table[y:min(y+y, table.shape[0]), :])):
            return y*100
    print("vertical")
    for x in range(1, table.shape[1]):
        print(max(0, x+x-min(x+x, table.shape[1])), x, min(x+x, table.shape[1]))
        if np.all(table[:, max(0, x+x-min(x+x, table.shape[1])):x] == np.fliplr(table[:, x:min(x+x, table.shape[1])])):
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
