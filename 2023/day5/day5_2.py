from pathlib import Path
import sys
from collections import defaultdict

lines = Path(sys.argv[1]).read_text().split("\n")

ranges = lines[0].split(":")[1].split()
seeds = [(int(e1), int(e1)+int(e2)) for e1, e2 in zip(ranges[::2], ranges[1::2])]

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

def check_nr(f, t, ranges):
    print("Check ", f, t)
    change = False
    final = []
    i = 0
    while i < len(ranges):
        v1, v2 = ranges[i]
        change = False
        for d, s, l in db[f][t]:
            diff = d - s
            if s <= v1 < v2 < s+l:
                final += [(v1+diff, v2+diff)]
            elif v1 < s < s+l <= v2:
                ranges += [(v1, s), (s+l, v2)]
                final += [(d, d+l)]
            elif s <= v1 < s+l <= v2:
                ranges += [(s+l, v2)]
                final += [(v1+diff, d+l)]
            elif v1 < s < v2 <= s+l:
                ranges += [(v1, s), (d, v2+diff)]
            else:
                continue
            change = True
            break
        if not change:
            final += [(v1, v2)]
        i += 1
    
    print(final)
    return final

mmin = 999999999999
current = "seed"
for p in path[1:]:
    seeds = check_nr(current, p, seeds)
    current = p

# print(seeds)
mmin = min(mmin, min([e[0] for e in seeds]))

print(mmin)
