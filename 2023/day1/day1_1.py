from pathlib import Path
import sys

lines = Path(sys.argv[1]).read_text().split("\n")

s = 0
for line in lines:
    numbers = [int(char) for char in line if "0" <= char <= "9"]
    s += numbers[0] * 10 + numbers[-1]

print(s)
