from pathlib import Path
import sys
import numpy as np

lines = Path(sys.argv[1]).read_text().split("\n")

table = np.array([[e for e in line] for line in lines])

ttable = np.transpose(table)

for row in ttable:
    hashtag_pos = np.append(np.insert(np.where(row == "#")[0], 0, -1), [ttable.shape[1]])
    for start, end in zip(hashtag_pos[:-1], hashtag_pos[1:]):
        subrow = row[(start+1):end]
        nr_Os = subrow[subrow == "O"].shape[0]
        subrow[:] = np.array(["O"]*nr_Os+["."]*(subrow.shape[0]-nr_Os))

s = 0
for i, row in enumerate(table):
    nr_Os = row[row == "O"].shape[0]
    s += nr_Os * (table.shape[0] - i)

print(s)
