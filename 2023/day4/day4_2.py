from pathlib import Path
import sys

lines = Path(sys.argv[1]).read_text().split("\n")
instances = [1] * len(lines)

for i, line in enumerate(lines):
    _, info = line.split(":")
    winning, my = map(str.split, info.split("|"))
    res = sum(1 for w in winning if w in my)
    for j in range(i+1, i+1+res):
        instances[j] += instances[i]
    
print(sum(instances))
