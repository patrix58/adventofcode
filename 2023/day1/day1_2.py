from pathlib import Path
import sys

lines = Path(sys.argv[1]).read_text().split("\n")

CONFIG = {
    0: ["0"],
    1: ["1", "one"],
    2: ["2", "two"],
    3: ["3", "three"],
    4: ["4", "four"],
    5: ["5", "five"],
    6: ["6", "six"],
    7: ["7", "seven"],
    8: ["8", "eight"],
    9: ["9", "nine"],
}

s = 0
for line in lines:
    res = {digit:[line.find(i) for i in ids if line.find(i) != -1] for digit, ids in CONFIG.items()}
    for digit in res:
        res[digit].extend([line.rfind(i) for i in CONFIG[digit] if line.rfind(i) != -1])
    mmin = 99999999999999999
    min_dig = -1
    mmax = -1
    max_dig = -1
    c = 0
    for digit, pos in res.items():
        if not pos:
            continue
        c += len(pos)
        if min(pos) < mmin:
            mmin = min(pos)
            min_dig = digit
        if max(pos) > mmax:
            mmax = max(pos)
            max_dig = digit
    # if "qkoneighttwoonesixeightfive2tzmrtpcthreefour" in line:
    #     print(min_dig * 10 + max_dig)
    assert min_dig != -1
    assert max_dig != -1
    s += min_dig * 10 + max_dig


print(s)
