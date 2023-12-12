from pathlib import Path
import sys

lines = Path(sys.argv[1]).read_text().split("\n")

mapping = {"0": ".", "1": "#"}


def check(schema, damages):
    idam = 0
    isch = 0
    c = 0
    while idam < len(damages) and isch < len(schema):
        if schema[isch] == "#":
            c += 1
        elif c:
            if c != damages[idam]:
                return False
            c = 0
            idam += 1
            isch = schema.find("#", isch+1)
            if isch == -1:
                break
            continue
        isch += 1
    if idam < len(damages) and c != damages[idam]:
        return False
    if idam < len(damages) - 1:
        return False
    if idam == len(damages) and schema[isch:].find("#") != -1:
        return False
    return True



def possibilities(schema, damages):
    # print(f"schema = {schema}, damages = {damages}")
    marks = schema.count("?")
    schema = schema.replace("?", "{}")
    p = 0
    for i in range(2**marks):
        bits = f"{{:{marks}b}}".format(i).replace(" ", "0")
        cschema = schema.format(*map(lambda x: mapping[x], bits))
        c = check(cschema, damages)
        p += int(c)
        # if c:
        #     print(cschema)
    return p

s = 0
for line in lines:
    schema, damages = line.split()
    schema = "?".join([schema] * 5)
    damages = ",".join([damages] * 5)
    s += possibilities(schema, list(map(int, damages.split(","))))
print(s)

# print(check(".###.##.#.##", [3, 2, 1]))
