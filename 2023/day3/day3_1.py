from pathlib import Path
import sys

schema = Path(sys.argv[1]).read_text().split("\n")


def is_symbol(char):
    return not char.isdigit() and char != "."


nx = [ 0, 0, 1,  1, 1, -1, -1, -1]
ny = [-1, 1, 1, -1, 0,  1, -1,  0]

def check_for_neighbors(i, j):
    for nnx, nny in zip(nx, ny):
        ii = i+nnx
        jj = j+nny
        if ii < 0 or jj < 0 or ii >= len(schema) or jj >= len(schema[0]):
            continue
        yield ii, jj

s = 0
for i, row in enumerate(schema):
    number = ""
    nearby_symbol = False
    for j, e in enumerate(row):
        if e.isdigit():
            number += e
            if not nearby_symbol:
                for ii, jj in check_for_neighbors(i, j):
                    if is_symbol(schema[ii][jj]):
                        nearby_symbol = True
                        break
        else:
            if nearby_symbol:
                s += int(number)
            number = ""
            nearby_symbol = False
    if nearby_symbol:
        s += int(number)

print(s)
