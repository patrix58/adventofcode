from pathlib import Path
import sys
import numpy as np


lines = Path(sys.argv[1]).read_text().split("\n")

nrsa = [np.array(list(map(int, line.split()))) for line in lines]

s = 0
for nrs in nrsa:
    res = [nrs[0]]
    while not np.all(nrs == nrs[0]):
        nrs = nrs[1:] - nrs[:-1]
        res.append(nrs[0])
    ss = res[-1]
    # print(f"res = {res}")
    for e in reversed(res[:-1]):
        # print(f"{e} - {ss} = {e - ss}")
        ss = e - ss
    # print(ss)
    s += ss

print(s)    
