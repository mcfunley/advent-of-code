import numpy as np

data = open("data/p12.txt").read().strip().splitlines()
grid = np.array([list(ln) for ln in data])
turns = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def in_bounds(pos):
    return (pos >= 0).all() and (pos < np.array(grid.shape)).all()


def visit(pos, char):
    if not in_bounds(pos):
        return np.array([0, 1])

    v = grid[tuple(pos)]
    if v == "x":
        return np.array([0, 0])
    if v != char:
        return np.array([0, 1])

    grid[tuple(pos)] = "x"
    return np.array([1, 0]) + sum(visit(pos + turn, char) for turn in turns)


price = 0
while 1:
    try:
        p = np.array(next(zip(*np.where(grid != "."))))
    except StopIteration:
        break

    price += np.prod(visit(p, grid[tuple(p)]))
    grid[grid == "x"] = "."

print(price)
