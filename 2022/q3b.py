#!/usr/bin/env python

def priority(item):
    c = ord(item)
    return c - 64 + 26 if c < 97 else c - 96

def overlap(ruck):
    i = len(ruck)//2
    ca, cb = ruck[:i], ruck[i:]
    return list(set(ca) & set(cb))

def overlap_priority(ol):
    return sum(priority(c) for c in ol)

def badge(group):
    return set.intersection(*[set(g) for g in group]).pop()

rucks = [l.strip() for l in open('data/q3.dat', 'r').readlines()]
groups = (rucks[i:i+3] for i in range(0, len(rucks), 3))
print(sum(priority(badge(g)) for g in groups))
