from collections import defaultdict
from pathlib import Path
import sys

lines = Path(sys.argv[1]).read_text().split("\n")

data = [line.split() for line in lines]

MAP_TO_NUMBER = {
    "J": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "Q": 11,
    "K": 12,
    "A": 13,
}

def unified_id(card):
    freq = defaultdict(int)
    for c in card:
        freq[c] += 1
    freq = list(reversed(sorted(freq.items(), key=lambda x: x[1])))
    freq_c = [f[0] for f in freq]
    freq_f = [f[1] for f in freq]
    try:
        index_j = freq_c.index("J")
        freq_j = freq_f[index_j]
        freq_c.pop(index_j)
        freq_f.pop(index_j)
    except ValueError:
        freq_j = 0
    print(card, end=" ")
    if not freq_c:
        ident = 7
        print("five of a kind")
    elif freq_f == [5] or (freq_c[0] != "J" and freq_f[0] + freq_j == 5):
        ident = 7
        print("five of a kind")
    elif freq_f[0] == 4 or (freq_c[0] != "J" and freq_f[0] + freq_j == 4):
        ident = 6
        print("four of a kind")
    elif freq_f == [3, 2] or (freq_c[0] != "J" and freq_c[1] != "J" and sum(freq_f[:2]) + freq_j == 5):
        ident = 5
        print("full house")
    elif freq_f[0] == 3 or (freq_c[0] != "J" and freq_f[0] + freq_j == 3):
        ident = 4
        print("three of a kind")
    elif freq_f[:2] == [2, 2] or (freq_c[0] != "J" and freq_c[1] != "J" and sum(freq_f[:2]) + freq_j == 4):
        ident = 3
        print("2 pairs")
    elif freq_f[0] == 2 or (freq_c[0] != "J" and freq_f[0] + freq_j == 2):
        ident = 2
        print("1 pair")
    else:
        ident = 1
        print("high card")
    for c in card:
        ident = ident * 14 + MAP_TO_NUMBER[c]
    return ident

data = sorted(data, key=lambda x: unified_id(x[0]))
# print(data)
s = 0
for i, (_, bid) in enumerate(data):
    s += (i+1)*int(bid)

print(s)
