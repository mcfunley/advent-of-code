#!/usr/bin/env python
from itertools import count
import sys

chars = []
for i, c in zip(count(1), open('data/q6.dat', 'r').read()):
    if len(chars) < 14:
        chars.append(c)
    else:
        chars = chars[1:] + [c]
        if len(set(chars)) == 14:
            print(i)
            sys.exit(0)
