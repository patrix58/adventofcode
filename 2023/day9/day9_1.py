from pathlib import Path
import sys
import numpy as np


lines = Path(sys.argv[1]).read_text().split("\n")

nrsa = [np.array(list(map(int, line.split()))) for line in lines]

s = 0
for nrs in nrsa:
    s += nrs[-1]
    while not np.all(nrs == nrs[0]):
        nrs = nrs[1:] - nrs[:-1]
        s += nrs[-1]

print(s)    
