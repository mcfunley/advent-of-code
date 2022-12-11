#!/usr/bin/env python
code = open('data/q10.dat', 'r').readlines()

def compile(ops):
    for op in [op.strip().split(' ') for op in ops]:
        match op:
            case ['addx', inc]:
                yield (2, int(inc))
            case ['noop']:
                yield (1, 0)

screen = ['.'] * 40 *6
strength_sum = 0
cycle = 0
x = 1
for ticks, inc in compile(code):
    for _ in range(ticks):
        if abs(x - cycle % 40) < 2:
            screen[cycle] = '#'

        cycle += 1
        if cycle in { 20, 60, 100, 140, 180, 220 }:
            strength_sum += x * cycle
    x += inc

print(strength_sum)

for y in range(6):
    for x in range(40):
        print(screen[y*40 + x], end=' ')
    print('\n')
