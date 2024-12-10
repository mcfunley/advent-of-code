data = open("data/p7.txt", "r").readlines()

equations = [
    [int(s), list(map(int, t.split()))]
    for s, t in (line.split(": ") for line in data)
]


def solve(acc, result, numbers):
    if len(numbers) == 0:
        return result if acc == result else 0
    n, *rest = numbers
    return max([solve(acc + n, result, rest), solve(acc * n, result, rest)])


print(sum(solve(0, *eq) for eq in equations))
