#!/usr/bin/env python
data = open('data/q1.dat', 'r').read()
print(max([sum([int(n) for n in x.split()]) for x in data.split('\n\n')]))
