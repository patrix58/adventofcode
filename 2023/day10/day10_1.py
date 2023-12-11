from pathlib import Path
import sys

table = Path(sys.argv[1]).read_text().split("\n")

start_y = -1
start_x = -1
while start_x == -1:
    start_y += 1
    start_x = table[start_y].find("S")

pos_yx = {
    "|": [(-1, 0), (1, 0)],
    "-": [(0, -1), (0, 1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(0, -1), (1, 0)],
    "F": [(0, 1), (1, 0)],
}

def get_neighbors(pos, y, x):
    for iy, ix in pos:
        yy = y+iy
        xx = x+ix
        if yy < 0 or xx < 0 or yy >= len(table) or xx >= len(table[0]) or table[yy][xx] == ".":
            continue
        yield yy, xx

for symb, pos in pos_yx.items():
    neighbors = list(get_neighbors(pos, start_y, start_x))
    if len(neighbors) < 2:
        continue
    check = [(start_y, start_x) in list(get_neighbors(pos_yx[table[y][x]], y, x))  for y, x in neighbors]
    if check and all(check):
        table[start_y] = table[start_y].replace("S", symb)
        break


v = [(start_y, start_x, 0)]
visited = [[False for _ in range(len(table[0]))] for _ in range(len(table))]
max_step = -1
while v:
    y, x, step = v[0]
    v = v[1:]
    max_step = max(max_step, step)
    for yy, xx in get_neighbors(pos_yx[table[y][x]], y, x):
        if visited[yy][xx]:
            continue
        visited[yy][xx] = True
        v.append((yy, xx, step+1))

print(max_step)
