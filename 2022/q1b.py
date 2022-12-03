#!/usr/bin/env python
data = open('data/q1.dat', 'r').read()
cals = [sum([int(n) for n in x.split()]) for x in data.split('\n\n')]
print(sum(sorted(cals)[-3:]))
