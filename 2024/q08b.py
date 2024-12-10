from itertools import permutations

import numpy as np

data = open("data/p8.txt", "r").read().strip().splitlines()

grid = np.array([list(ln) for ln in data])
frequencies = [f for f in np.unique(grid) if f != "."]
antinodes = np.zeros(grid.shape)


def in_bounds(pos):
    return (pos >= 0).all() and (pos < grid.shape).all()


def mark_antinodes(f):
    coords = [np.array(c) for c in zip(*np.where(grid == f))]
    for p0, p1 in permutations(coords, 2):
        p = p0.copy()
        while in_bounds(p):
            antinodes[tuple(p)] = 1
            p += p0 - p1


for f in frequencies:
    mark_antinodes(f)


print(int(sum(sum(antinodes))))
