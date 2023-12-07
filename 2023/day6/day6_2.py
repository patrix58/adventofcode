from pathlib import Path
import sys

lines = Path(sys.argv[1]).read_text().split("\n")

t = int(lines[0].split(":")[1].replace(" ", ""))
d = int(lines[1].split(":")[1].replace(" ", ""))


c = 0
for x in range(1, t):
    c += int((t-x)*x>d)
print(c)
