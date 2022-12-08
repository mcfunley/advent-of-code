#!/usr/bin/env python
import re
from collections import defaultdict

sizes = defaultdict(int)
path = None
listing = False

def prefixes():
    return (''.join(path[:i+1]) for i in range(len(path)))

for l in open('data/q7.dat', 'r').readlines():
    if listing:
        if l.startswith('$'):
            listing = False
        elif l.startswith('dir '):
            continue
        else:
            sz = int(re.match('([0-9]+).*', l).groups()[0])
            for p in prefixes():
                sizes[p] += sz
            continue

    match [x.strip() for x in re.match('\$ ([^ ]+)\s?(.*)?', l).groups()]:
        case 'cd', '/':
            path = ['/']
        case 'cd', '..':
            path.pop()
        case 'cd', x:
            path.append(x + '/')
        case 'ls', _:
            listing = True
        case _:
            print(f'unknown command: {l}')

print(sum(sz for sz in sizes.values() if sz <= 100000))

total_space = 70000000
used_space = sizes['/']
free_goal = 30000000
goal = free_goal - (total_space - used_space)
print(min(sz for sz in sizes.values() if sz >= goal))
