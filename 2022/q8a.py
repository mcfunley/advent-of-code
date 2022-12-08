#!/usr/bin/env python
import numpy as np

data = np.array([list(l.strip()) for l in open('data/q8.dat', 'r').readlines()], dtype=int)

ymax, xmax = data.shape
visible = np.ones(data.shape, dtype=int)
visible[1:ymax-1, 1:xmax-1] = 0

def walk(maxes, slices):
    for s in slices:
        visible[s] |= (data[s] > maxes).astype(int)
        maxes = np.maximum(data[s], maxes)

walk(data[0], (np.s_[r] for r in range(1, ymax)))
walk(data[-1], (np.s_[r] for r in reversed(range(1, ymax))))
walk(data[0:ymax, 0], (np.s_[0:ymax, r] for r in range(1, xmax)))
walk(data[0:ymax, -1], (np.s_[0:ymax, r] for r in reversed(range(1, xmax))))

print(f'Visible: {sum(sum(visible))}')

def score(r, c):
    def distance(view):
        return next((i for i, v in enumerate(view, 1) if v >= data[r, c]), len(view))
    row = data[r]
    col = data[0:ymax, c]
    views = [np.flip(row[:c]), row[c+1:], np.flip(col[:r]), col[r+1:]]
    return np.product([distance(v) for v in views])

scores = np.array([[score(r, c) for r in range(ymax)] for c in range(xmax)])
print(f'Highest score: {np.max(scores)}')
