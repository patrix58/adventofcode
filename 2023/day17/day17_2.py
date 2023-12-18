from dataclasses import dataclass
from pathlib import Path
import sys
import numpy as np

table = np.array([[int(e) for e in line] for line in Path(sys.argv[1]).read_text().split("\n")])

@dataclass
class Step:
    pos_yx: tuple[int, int] = (0, 0)
    dir_yx: tuple[int, int] = (0, 1)
    loss: int = 0
    straight: int = 0
    prev: int = -1


MAX_STRAIGHT = 10
MIN_STRAIGHT = 4

loss = {
    (0, 1): [np.full_like(table, -1) for _ in range(MAX_STRAIGHT+1)],
    (0, -1): [np.full_like(table, -1) for _ in range(MAX_STRAIGHT+1)],
    (1, 0): [np.full_like(table, -1) for _ in range(MAX_STRAIGHT+1)],
    (-1, 0): [np.full_like(table, -1) for _ in range(MAX_STRAIGHT+1)],
}
v = [
    Step(),
    Step(),
    Step(),
    Step(),
]
v[1].dir_yx = (0, -1)
v[2].dir_yx = (1, 0)
v[3].dir_yx = (-1, 0)
loss[(0, 1)][0][0, 0] = 0
loss[(0, -1)][0][0, 0] = 1
loss[(1, 0)][0][0, 0] = 2
loss[(-1, 0)][0][0, 0] = 3

dirs = {
    (0, 1): [(0, 1), (1, 0), (-1, 0)],
    (0, -1): [(0, -1), (1, 0), (-1, 0)],
    (1, 0): [(1, 0), (0, 1), (0, -1)],
    (-1, 0): [(-1, 0), (0, 1), (0, -1)],
}

i = 0
while i < len(v):
    e = v[i]
    y, x = e.pos_yx
    for dir in dirs[e.dir_yx]:
        yy, xx = dir
        s = Step()
        s.dir_yx = dir
        s.pos_yx = (y+yy, x+xx)
        s.prev = i
        if s.pos_yx[0] < 0 or s.pos_yx[1] < 0 or s.pos_yx[0] >= table.shape[0] or s.pos_yx[1] >= table.shape[1]:
            continue
        if dir == e.dir_yx:
            s.straight = e.straight+1
            if s.straight > MAX_STRAIGHT:
                continue
        else:
            if e.straight < MIN_STRAIGHT:
                continue
            s.straight = 1
        s.loss = e.loss+table[s.pos_yx]
        j = loss[s.dir_yx][s.straight][s.pos_yx]
        if j == -1 or v[j].loss > s.loss:
            if j < i:
                v.append(s)
                loss[s.dir_yx][s.straight][s.pos_yx] = len(v)-1
            else:
                assert v[j].pos_yx == s.pos_yx
                assert v[j].dir_yx == s.dir_yx
                assert v[j].straight == s.straight
                v[j].loss = s.loss
                v[j].prev = i
    i += 1

min_loss = min(v[ar[table.shape[0]-1, table.shape[1]-1]].loss for k in loss for ar in loss[k][MIN_STRAIGHT:] if ar[table.shape[0]-1, table.shape[1]-1] != -1)
print(min_loss)

charmap = {
    (0, 1): ">",
    (0, -1): "<",
    (1, 0): "v",
    (-1, 0): "^",
}

def backtrack(i):
    if i != -1:
        res = backtrack(v[i].prev)
        res.append((v[i].pos_yx, v[i].dir_yx))
        return res
    else:
        return []

def show(i):
    steps = backtrack(i)
    stable = np.copy(table.astype(str))
    for s in steps:
        stable[s[0]] = charmap[s[1]]
    for r in stable:
        for e in r:
            print(e, end="")
        print()

def print_paths():
    for i, s in enumerate(v):
        if s.pos_yx == (table.shape[0]-1, table.shape[1]-1):
        # if s.pos_yx == (1, 5):
            print(f"min loss {s.loss}")
            show(i)
            print()

def print_loss():
    for y in range(table.shape[0]):
        for x in range(table.shape[1]):
            print(min(v[ar[y, x]].loss for l in loss.values() for ar in l), end=" ")
        print()

# print_paths()
# print_loss()
