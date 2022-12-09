#!/usr/bin/env python
import numpy as np

data = open('data/q9.dat', 'r').readlines()
moves = ((d, int(n)) for d, n in (l.strip().split(' ') for l in data))

def tailmove(t, h):
    if max(abs(h - t)) <= 1:
        return [0, 0]
    return [np.sign(d) if abs(d) > 1 else d for d in h - t]

h = np.zeros(2)
t = np.zeros(2)
tailpositions = { tuple(t) }
directions = { 'R': [1, 0], 'U': [0, -1], 'D': [0, 1], 'L': [-1, 0], }

for d, n in moves:
    for _ in range(n):
        h += directions[d]
        t += tailmove(t, h)
        tailpositions.add(tuple(t))

print(len(tailpositions))
