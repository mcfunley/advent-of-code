import numpy as np

lines = open("data/p1.txt", "r").readlines()
numbers = [(int(x), int(y)) for x, y in (ln.split() for ln in lines)]
left = np.sort([x for x, _ in numbers])
right = np.sort([y for _, y in numbers])
print(sum(np.abs(left - right)))
