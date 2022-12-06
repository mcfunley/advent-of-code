#!/usr/bin/env python
import re

"""
[P]     [L]         [T]
[L]     [M] [G]     [G]     [S]
[M]     [Q] [W]     [H] [R] [G]
[N]     [F] [M]     [D] [V] [R] [N]
[W]     [G] [Q] [P] [J] [F] [M] [C]
[V] [H] [B] [F] [H] [M] [B] [H] [B]
[B] [Q] [D] [T] [T] [B] [N] [L] [D]
[H] [M] [N] [Z] [M] [C] [M] [P] [P]
 1   2   3   4   5   6   7   8   9
"""

stacks = [
    list('HBVWNMLP'),
    list('MQH'),
    list('NDBGFQML'),
    list('ZTFQMWG'),
    list('MTHP'),
    list('CBMJDHGT'),
    list('MNBFVR'),
    list('PLHMRGS'),
    list('PDBCN'),
]

def move(n, i, j):
    stacks[i], move = stacks[i][:-n], stacks[i][-n:]
    stacks[j].extend(move)

for m in open('data/q5.dat', 'r').readlines():
    n, s1, s2 = [int(x) for x in re.match('move ([0-9]+) from ([0-9]+) to ([0-9]+)', m).groups()]
    move(n, s1-1, s2-1)

print(''.join(s[-1] for s in stacks))
