from pathlib import Path
import sys

lines = Path(sys.argv[1]).read_text().split("\n")

times = list(map(int, lines[0].split(":")[1].split()))
distances = list(map(int, lines[1].split(":")[1].split()))

p = 1
for t, d in zip(times, distances):
    c = 0
    for x in range(1, t):
        c += int((t-x)*x>d)
    # print(c)
    p *= c

print(p)
