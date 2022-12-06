#!/usr/bin/env python
n = 0
for l in open('data/q4.dat', 'r').readlines():
    a1, a2 = [tuple(int(n) for n in x.split('-')) for x in l.strip().split(',')]
    s1 = set(range(a1[0], a1[1]+1))
    s2 = set(range(a2[0], a2[1]+1))
    if len(s1 & s2):
        n += 1
print(n)
