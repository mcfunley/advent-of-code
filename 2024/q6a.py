import numpy as np

data = open("data/p6.txt", "r").read()
grid = np.array([list(x) for x in data.strip().splitlines()])


def in_bounds(pos):
    return (pos >= 0).all() and (pos < grid.shape).all()


pos = np.argwhere(grid == "^")[0]
vec = np.array([-1, 0])
turns = {
    (-1, 0): (0, 1),
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0),
}

while in_bounds(pos):
    while in_bounds(pos + vec) and grid[tuple(pos + vec)] == "#":
        vec = turns[tuple(vec)]
    grid[tuple(pos)] = "X"
    pos += vec

print(np.count_nonzero(grid == "X"))
