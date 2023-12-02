from pathlib import Path
import sys

lines = Path(sys.argv[1]).read_text().split("\n")

MAX_CUBE = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

s = 0
for line in lines:
    game_desc, info = line.split(":")
    possible = True
    for round in info.split(";"):
        for record in round.split(","):
            nr, color = record.split()
            nr = int(nr)
            if nr > MAX_CUBE[color]:
                possible = False
                break
        if not possible:
            break
    if possible:
        s += int(game_desc.split()[1])

print(s)
