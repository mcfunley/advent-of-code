from itertools import permutations

import numpy as np

data = open("data/p8.txt", "r").read().strip().splitlines()

grid = np.array([list(ln) for ln in data])
frequencies = [f for f in np.unique(grid) if f != "."]
antinodes = np.zeros(grid.shape)


def in_bounds(pos):
    return (pos >= 0).all() and (pos < grid.shape).all()


def mark_antinodes(f):
    fs = np.where(grid == f)
    antinodes[fs] = 1
    coords = [np.array(c) for c in zip(*fs)]
    for p0, p1 in permutations(coords, 2):
        dist = p0 - p1
        p = p0.copy()
        while in_bounds(p + dist):
            p += dist
            antinodes[tuple(p)] = 1


for f in frequencies:
    mark_antinodes(f)


print(int(sum(sum(antinodes))))
