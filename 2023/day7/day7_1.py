from collections import defaultdict
from pathlib import Path
import sys

lines = Path(sys.argv[1]).read_text().split("\n")

data = [line.split() for line in lines]

MAP_TO_NUMBER = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}

def unified_id(card):
    freq = defaultdict(int)
    for c in card:
        freq[c] += 1
    freq = list(reversed(sorted(freq.values())))
    if freq == [5]:
        ident = 7
    elif freq[0] == 4:
        ident = 6
    elif freq == [3, 2]:
        ident = 5
    elif freq[0] == 3:
        ident = 4
    elif freq[:2] == [2, 2]:
        ident = 3
    elif freq[0] == 2:
        ident = 2
    else:
        ident = 1
    for c in card:
        ident = ident * 15 + MAP_TO_NUMBER[c]
    return ident

data = sorted(data, key=lambda x: unified_id(x[0]))
s = 0
for i, (_, bid) in enumerate(data):
    s += (i+1)*int(bid)

print(s)
