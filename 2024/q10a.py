import numpy as np

data = open("data/p10.txt", "r").read().strip().splitlines()
grid = np.array([[int(x) for x in list(ln)] for ln in data])
turns = [np.array(t) for t in [(0, 1), (1, 0), (0, -1), (-1, 0)]]


def in_bounds(pos):
    return (pos >= 0).all() and (pos < grid.shape).all()


def hike(trailhead):
    vgrid = np.full(grid.shape, None)

    def legal(pos, v):
        return (
            in_bounds(pos)
            and vgrid[tuple(pos)] is None
            and grid[tuple(pos)] == v + 1
        )

    def _hike(pos):
        v = grid[tuple(pos)]
        vgrid[tuple(pos)] = v
        if v == 9:
            return
        for t in turns:
            if legal(pos + t, v):
                _hike(pos + t)

    _hike(trailhead)
    return vgrid


def score(vgrid):
    return sum(sum(vgrid == 9))


trailheads = zip(*np.where(grid == 0))
print(sum([score(hike(th)) for th in trailheads]))
