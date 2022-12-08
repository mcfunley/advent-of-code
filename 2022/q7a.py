#!/usr/bin/env python
import re
from collections import defaultdict

testdata = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

data = open('data/q7.dat', 'r').readlines()
# data = testdata.splitlines()

sizes = defaultdict(int)
path = None
listing = False

def prefixes():
    return (''.join(path[:i+1]) for i in range(len(path)))

for l in data:
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

    cmd, args = [x.strip() for x in re.match('\$ ([^ ]+)\s?(.*)?', l).groups()]
    match cmd, args:
        case 'cd', '/':
            path = ['/']
        case 'cd', '..':
            path.pop()
        case 'cd', x:
            path.append(x + '/')
        case 'ls', '':
            listing = True
        case _:
            print(f'unknown command: {l}')

print(sum(sz for k, sz in sizes.items() if k != '/'), sizes['/'])
print(sum(sz for sz in sizes.values() if sz <= 100000))
