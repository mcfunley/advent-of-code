import numpy as np

lines = open("data/p2.txt", "r").readlines()


def is_safe(xs):
    diffs = np.array([x - y for x, y in zip(xs, xs[1:])])
    diffmag = np.abs(diffs)
    if not np.all((diffmag > 0) & (diffmag < 4)):
        return False

    if not np.all(np.sign(diffs) == np.sign(diffs[0])):
        return False
    return True


safe = 0
for ln in lines:
    xs = [int(x) for x in ln.split()]

    if is_safe(xs):
        safe += 1
        continue

    for i in range(len(xs)):
        if is_safe(xs[:i] + xs[i + 1 :]):
            safe += 1
            break

print(safe)
