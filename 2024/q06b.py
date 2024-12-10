from collections import defaultdict

import numpy as np
from tqdm import tqdm

data = open("data/p6.txt", "r").read()

turns = {
    (-1, 0): (0, 1),
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0),
}


def detect_loop(grid):
    def in_bounds(pos):
        return (pos >= 0).all() and (pos < grid.shape).all()

    def obstacle(pos):
        return in_bounds(pos) and grid[tuple(pos)] in {"#", "O"}

    pos = np.argwhere(grid == "^")[0]
    vec = np.array([-1, 0])
    posvectors = defaultdict(set)

    while in_bounds(pos):
        while obstacle(pos + vec):
            vec = turns[tuple(vec)]

        if tuple(vec) in posvectors[tuple(pos)]:
            return True
        posvectors[tuple(pos)].add(tuple(vec))

        pos += vec

    return False


grid = np.array([list(x) for x in data.strip().splitlines()])
candidates = 0
with tqdm(total=grid.shape[0] * grid.shape[1]) as pbar:
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            pbar.update(1)

            if grid[i, j] != ".":
                continue
            grid[i, j] = "O"
            if detect_loop(grid):
                candidates += 1
            grid[i, j] = "."

print(candidates)
