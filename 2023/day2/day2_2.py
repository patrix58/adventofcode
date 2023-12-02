from pathlib import Path
import sys
from functools import reduce
from operator import mul

lines = Path(sys.argv[1]).read_text().split("\n")

s = 0
for line in lines:
    max_cube = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    _, info = line.split(":")
    for round in info.split(";"):
        for record in round.split(","):
            nr, color = record.split()
            nr = int(nr)
            max_cube[color] = max(max_cube[color], nr)
    s += reduce(mul, max_cube.values())

print(s)
