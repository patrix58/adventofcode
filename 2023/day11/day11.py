from pathlib import Path
import sys
import numpy as np

lines = Path(sys.argv[1]).read_text().split("\n")

table = []
for i, line in enumerate(lines):
    table.append(np.array([e for e in line]))
table = np.array(table)

galaxies = list(zip(*np.where(table == "#")))
mask = table == "."
rows = np.all(mask, axis=1)
columns = np.all(mask, axis=0)

CONSTANT = 1000000
def distance(a, b):
    sum_row = np.sum(rows[min(a[0], b[0]):max(a[0], b[0])])
    sum_column = np.sum(columns[min(a[1], b[1]):max(a[1], b[1])])
    return np.abs(b[0]-a[0]) + np.abs(b[1]-a[1]) + (sum_row + sum_column) * (CONSTANT-1)

print(sum(distance(galaxies[i], galaxies[j]) for i in range(len(galaxies)) for j in range(i+1, len(galaxies))))