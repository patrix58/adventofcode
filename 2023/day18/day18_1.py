from pathlib import Path
import sys
from matplotlib import pyplot as plt

sys. setrecursionlimit(100_000)

lines = Path(sys.argv[1]).read_text().split("\n")

y, x = 0, 0
directions = {
    "R": (0, 1),
    "L": (0, -1),
    "U": (-1, 0),
    "D": (1, 0),
}
points_y = [0]
points_x = [0]
for line in lines:
    direction, distance, _ = line.split()
    distance = int(distance)
    iy, ix = directions[direction]
    for i in range(1, distance+1):
        points_y.append(y+iy*i)
        points_x.append(x+ix*i)
    y += iy * distance
    x += ix * distance


plt.plot(points_x, points_y)
plt.savefig("plot.jpg")

points = set(zip(points_y, points_x))
visited = []

def dfs(y, x):
    if (y, x) in visited or (y, x) in points:
        return 0
    visited.append((y, x))
    return 1 + sum(dfs(y+iy, x+ix) for iy, ix in directions.values())


print(dfs(100, 100) + len(points))
