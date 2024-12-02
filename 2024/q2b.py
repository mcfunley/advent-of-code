import numpy as np

lines = open("data/p2.txt", "r").readlines()


def is_safe(xs):
    diffs = [x - y for x, y in zip(xs, xs[1:])]
    if not all(abs(d) > 0 and abs(d) < 4 for d in diffs):
        return False

    if not np.all(np.equal(np.sign(diffs), np.sign(diffs[0]))):
        return False
    return True


safe = 0
for ln in lines:
    xs = [int(x) for x in ln.split()]
    safe += 1 if is_safe(xs) else 0

print(safe)
