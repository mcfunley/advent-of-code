import numpy as np

data = open("data/p12.txt").read().strip().splitlines()
grid = np.array([list(ln) for ln in data])
turns = [(0, 1), (1, 0), (0, -1), (-1, 0)]
diags = [(1, 1), (1, -1), (-1, 1), (-1, -1)]


def in_bounds(pos):
    return (pos >= 0).all() and (pos < np.array(grid.shape)).all()


def val(pos):
    return grid[tuple(pos)].upper() if in_bounds(pos) else "."


def visited(char):
    return char.lower()


def is_corner(pos, diag, char):
    dv = val(pos + diag)
    av0 = val(pos + (diag[0], 0))
    av1 = val(pos + (0, diag[1]))
    return (dv != char and av0 == char and av1 == char) or (
        av0 != char and av1 != char
    )


def count_corners(pos, char):
    return sum(1 if is_corner(pos, diag, char) else 0 for diag in diags)


def visit(pos, char):
    if not in_bounds(pos) or grid[tuple(pos)] != char:
        return np.array([0, 0])

    grid[tuple(pos)] = visited(char)
    return np.array([1, count_corners(pos, char)]) + sum(
        [visit(pos + turn, char) for turn in turns]
    )


price = 0
while 1:
    try:
        p = np.array(next(zip(*np.where(grid != "."))))
    except StopIteration:
        break

    char = grid[tuple(p)]
    price += np.prod(visit(p, char))
    grid[grid == char.lower()] = "."

print(price)
