import numpy as np

data = open("data/p10.txt", "r").read().strip().splitlines()
grid = np.array([[int(x) for x in list(ln)] for ln in data])
turns = [np.array(t) for t in [(0, 1), (1, 0), (0, -1), (-1, 0)]]


def in_bounds(pos):
    return (pos >= 0).all() and (pos < grid.shape).all()


def rate(pos):
    v = grid[tuple(pos)]
    if v == 9:
        return 1
    return sum(
        rate(pos + t)
        for t in turns
        if in_bounds(pos + t) and grid[tuple(pos + t)] == v + 1
    )


trailheads = zip(*np.where(grid == 0))
print(sum(rate(th) for th in trailheads))
