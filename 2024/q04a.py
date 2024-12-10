import numpy as np

lines = open("data/p4.txt", "r").readlines()

directions = np.array(
    [
        (-1, -1),
        (0, -1),
        (1, -1),
        (-1, 0),
        (1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
    ]
)


def charat(p):
    x, y = p
    if x < 0 or x >= len(lines[0]) or y < 0 or y >= len(lines):
        return None
    return lines[y][x]


def find(p, direction, s):
    c, rest = s[0], s[1:]
    if charat(p) != c:
        return 0

    if len(rest) == 0:
        return 1

    return find(p + direction, direction, rest)


xmases = 0
for x in range(len(lines[0])):
    for y in range(len(lines)):
        for d in directions:
            xmases += find((x, y), d, "XMAS")

print(xmases)
