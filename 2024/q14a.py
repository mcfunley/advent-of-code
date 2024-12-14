import re
from dataclasses import dataclass

import numpy as np

data = open("data/p14.txt").read().strip().splitlines()
shape = np.array([101, 103])


def quadrants():
    q1 = shape // 2
    q4origin = shape - shape // 2
    yield [(0, 0), tuple(q1)]
    yield [(0, q4origin[1]), (q1[0], shape[1])]
    yield [(q4origin[0], 0), (shape[0], q1[1])]
    yield [tuple(q4origin), tuple(shape)]


@dataclass
class Bot:
    p: np.ndarray
    v: np.ndarray


bots = [
    Bot(p=np.array(xs[:2]), v=np.array(xs[2:]))
    for xs in [[int(x) for x in re.findall(r"-?\d+", line)] for line in data]
]


def grid():
    g = np.zeros(shape, dtype=int)
    for bot in bots:
        g[tuple(bot.p)] += 1
    return g


def qscores():
    g = grid()
    for (x0, y0), (x1, y1) in quadrants():
        yield np.sum(g[x0:x1, y0:y1])


for i in range(100):
    for bot in bots:
        bot.p += bot.v
        bot.p %= shape

print(np.prod(list(qscores())))
