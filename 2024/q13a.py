import re

from scipy.optimize import linprog

data = open("data/p13.txt").read()
matches = re.finditer(
    r"Button A: X\+(\d+), Y\+(\d+)\n"
    r"Button B: X\+(\d+), Y\+(\d+)\n"
    r"Prize: X=(\d+), Y=(\d+)",
    data,
)

problems = ([int(x) for x in m.groups()] for m in matches)

tokens = 0

for ax, ay, bx, by, x, y in problems:
    A_eq = [
        [ax, bx],
        [ay, by],
    ]
    b_eq = [x, y]

    result = linprog([3, 1], A_eq=A_eq, b_eq=b_eq, bounds=[(0, 100), (0, 100)])

    if result.success:
        a, b = [x.round().astype(int) for x in result.x]
        if a * ax + b * bx == x and a * ay + b * by == y:
            tokens += 3 * a + b

print(tokens)
