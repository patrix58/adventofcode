from pathlib import Path
import sys
import numpy as np

lines = Path(sys.argv[1]).read_text().split("\n")

table = np.array([[e for e in line] for line in lines])
# print(table)

table_north = np.transpose(table)
table_west = table
table_south = np.fliplr(table_north)
table_east = np.fliplr(table)

def calc_power():
    s = 0
    for i, row in enumerate(table):
        nr_Os = row[row == "O"].shape[0]
        s += nr_Os * (table.shape[0] - i)
    return s

ar = []
for cycle in range(250):
    for ctable in (table_north, table_west, table_south, table_east):
        for row in ctable:
            hashtag_pos = np.append(np.insert(np.where(row == "#")[0], 0, -1), [ctable.shape[1]])
            for start, end in zip(hashtag_pos[:-1], hashtag_pos[1:]):
                subrow = row[(start+1):end]
                nr_Os = subrow[subrow == "O"].shape[0]
                subrow[:] = np.array(["O"]*nr_Os+["."]*(subrow.shape[0]-nr_Os))
    # print(f"Cycle {cycle+1}")
    # print(table)
    ar.append(calc_power())

ar = np.array(ar)
# visited = []
# for e in ar:
#     if e not in visited:
#         visited.append(e)
#     else:
#         continue
#     pos = np.where(ar == e)[0]
#     if pos.shape[0] > 1:
#         print(e, pos)
pos = (1000000000-1-121)%18+121
print(ar[121:][pos-1:pos+2])
