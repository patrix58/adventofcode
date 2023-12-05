from pathlib import Path
import sys
from collections import defaultdict

lines = Path(sys.argv[1]).read_text().split("\n")

seeds = [int(e) for e in lines[0].split(":")[1].split()]

print("Building db...")

db = defaultdict(lambda: defaultdict(list))

start = True
sdb = None
for line in lines[2:]:
    if start:
        f, t = line.split()[0].split("-to-")
        sdb = db[f][t]
        start = False
        continue
    if not line:
        start = True
        continue
    sdb.append(tuple(map(int, line.split())))
    

print("Finished")

print("Building path...")
visited = defaultdict(lambda: False)

def dfs(node, path):
    path.append(node)
    if node == "location":
        return True
    visited[node] = True
    for next_node in db[node]:
        if not visited[next_node]:
            if dfs(next_node, path):
                return True
    path.pop()
    visited[node] = False
    return False

path = []
dfs("seed", path)
print("Finished")

print("Checking locations...")

def check_nr(f, t, v):
    for d, s, l in db[f][t]:
        if s <= v < s+l:
            return d+v-s
    return v

mmin = 999999999999
for seed in seeds:
    current = "seed"
    for p in path:
        seed = check_nr(current, p, seed)
        current = p
    mmin = min(mmin, seed)

print(mmin)
