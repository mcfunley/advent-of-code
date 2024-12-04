import numpy as np

lines = open("data/p4.txt", "r").readlines()


def charat(p):
    x, y = p
    if x < 0 or x >= len(lines[0]) or y < 0 or y >= len(lines):
        return ""
    return lines[y][x]


def check(p):
    c = charat(p)
    a = charat(p + (-1, -1)) + c + charat(p + (1, 1))
    b = charat(p + (1, -1)) + c + charat(p + (-1, 1))
    if (a == "MAS" or a == "SAM") and (b == "MAS" or b == "SAM"):
        return 1
    return 0


xmases = 0
for x in range(len(lines[0])):
    for y in range(len(lines)):
        xmases += check(np.array([x, y]))

print(xmases)
