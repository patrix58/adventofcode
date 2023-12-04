from pathlib import Path
import sys
from collections import defaultdict
from functools import reduce
from operator import mul

schema = Path(sys.argv[1]).read_text().split("\n")


def is_symbol(char):
    return char == "*"


nx = [ 0, 0, 1,  1, 1, -1, -1, -1]
ny = [-1, 1, 1, -1, 0,  1, -1,  0]

def check_for_neighbors(i, j):
    for nnx, nny in zip(nx, ny):
        ii = i+nnx
        jj = j+nny
        if ii < 0 or jj < 0 or ii >= len(schema) or jj >= len(schema[0]):
            continue
        yield ii, jj

db = defaultdict(list)

for i, row in enumerate(schema):
    number = ""
    nearby_symbol = None
    for j, e in enumerate(row):
        if e.isdigit():
            number += e
            if nearby_symbol is None:
                for ii, jj in check_for_neighbors(i, j):
                    if is_symbol(schema[ii][jj]):
                        nearby_symbol = ii, jj
                        break
        else:
            if nearby_symbol is not None:
                db[nearby_symbol].append(int(number))
            number = ""
            nearby_symbol = None
    if nearby_symbol is not None:
        db[nearby_symbol].append(int(number))

print(sum(reduce(mul, numbers) for numbers in db.values() if len(numbers) == 2))
