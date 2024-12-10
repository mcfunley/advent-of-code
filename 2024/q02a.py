import numpy as np

lines = open("data/p2.txt", "r").readlines()

safe = 0
for ln in lines:
    xs = [int(x) for x in ln.split()]
    diffs = [x - y for x, y in zip(xs, xs[1:])]
    if not all(abs(d) > 0 and abs(d) < 4 for d in diffs):
        continue

    if not np.all(np.equal(np.sign(diffs), np.sign(diffs[0]))):
        continue

    safe += 1

print(safe)
