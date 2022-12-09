#!/usr/bin/env python
import numpy as np

data = open('data/q9.dat', 'r').readlines()
moves = [(d, int(n)) for d, n in (l.strip().split(' ') for l in data)]
directions = { 'R': [1, 0], 'U': [0, -1], 'D': [0, 1], 'L': [-1, 0], }

def follow_move(t, h):
    if max(abs(h - t)) <= 1:
        return [0, 0]
    return [np.sign(d) if abs(d) > 1 else d for d in h - t]

def run(knots):
    segments = [np.zeros(2) for _ in range(knots)]
    tail_positions = { tuple(segments[-1]) }
    for d, n in moves:
        for _ in range(n):
            segments[0] += directions[d]
            for i in range(1, knots):
                segments[i] += follow_move(segments[i], segments[i-1])
            tail_positions.add(tuple(segments[-1]))
    print(len(tail_positions))

run(2)
run(10)
