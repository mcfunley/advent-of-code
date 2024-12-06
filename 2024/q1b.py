from itertools import groupby

import numpy as np

lines = open("data/p1.txt", "r").readlines()

numbers = [(int(x), int(y)) for x, y in (ln.split() for ln in lines)]
left = np.sort([x for x, _ in numbers])
right = np.sort([y for _, y in numbers])
right_counts = {k: len(list(v)) for k, v in groupby(right)}

score = 0
for n in left:
    score += n * right_counts.get(n, 0)

print(score)
