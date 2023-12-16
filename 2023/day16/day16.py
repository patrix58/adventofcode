from pathlib import Path
import sys
import numpy as np


lines = Path(sys.argv[1]).read_text().split("\n")

table = np.array([[e for e in line] for line in lines])

dirs = {
    "/": {
        (0, 1): [(-1, 0)],
        (-1, 0): [(0, 1)],
        (0, -1): [(1, 0)],
        (1, 0): [(0, -1)],
    },
    "\\": {
        (0, 1): [(1, 0)],
        (1, 0): [(0, 1)],
        (-1, 0): [(0, -1)],
        (0, -1): [(-1, 0)],
    },
    "|": {
        (1, 0): [(1, 0)],
        (-1, 0): [(-1, 0)],
        (0, 1): [(1, 0), (-1, 0)],
        (0, -1): [(1, 0), (-1, 0)],
    },
    "-": {
        (1, 0): [(0, -1), (0, 1)],
        (-1, 0): [(0, -1), (0, 1)],
        (0, 1): [(0, 1)],
        (0, -1): [(0, -1)],
    },
    ".": {
        (1, 0): [(1, 0)],
        (-1, 0): [(-1, 0)],
        (0, -1): [(0, -1)],
        (0, 1): [(0, 1)],
    },
}

def simulate_beams(beams, show=False):
    tdb = [[{
        (0, 1): False,
        (0, -1): False,
        (1, 0): False,
        (-1, 0): False
    } for _ in range(table.shape[1])] for _ in range(table.shape[0])]

    assert len(tdb) == len(table) and len(tdb[0]) == len(table[0])
    while beams:
        next_beams = []
        for (y, x), dir in beams:
            tdb[y][x][dir] = True
            next_dirs = dirs[table[y, x]][dir]
            for iy, ix in next_dirs:
                yy = y+iy
                xx = x+ix
                if yy < 0 or xx < 0 or yy >= table.shape[0] or xx >=table.shape[1] or tdb[yy][xx][(iy, ix)]:
                    continue
                next_beams.append(((yy, xx), (iy, ix)))
        beams = next_beams

    if show:
        for r in tdb:
            for e in r:
                if any(e.values()):
                    print("#", end="")
                else:
                    print(".", end="")
            print()

    return sum([any(e.values()) for r in tdb for e in r])

mmax = 0
for y in range(table.shape[0]):
    mmax = max(mmax, simulate_beams([((y, 0), (0, 1))]))
    mmax = max(mmax, simulate_beams([((y, table.shape[1]-1), (0, -1))]))
for x in range(table.shape[1]):
    mmax = max(mmax, simulate_beams([((0, x), (1, 0))]))
    mmax = max(mmax, simulate_beams([((table.shape[0]-1, x), (-1, 0))]))
print(mmax)