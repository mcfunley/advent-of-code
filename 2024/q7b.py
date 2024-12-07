from math import log10

from tqdm import tqdm

data = open("data/p7.txt", "r").readlines()

equations = [
    [int(s), list(map(int, t.split()))]
    for s, t in (line.split(": ") for line in data)
]


def concat(a, b):
    return a * (10 ** int(log10(b) + 1)) + b


def solve(acc, result, numbers):
    if acc is not None and acc > result:
        return 0
    if len(numbers) == 0:
        return result if acc == result else 0
    n, *rest = numbers
    return max(
        [
            solve((acc or 0) + n, result, rest),
            solve((acc or 1) * n, result, rest),
            solve(concat(acc, n) if acc else n, result, rest),
        ]
    )


print(sum(tqdm((solve(None, *eq) for eq in equations), total=len(equations))))
