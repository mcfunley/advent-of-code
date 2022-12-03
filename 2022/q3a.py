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

rucks = open('data/q3.dat', 'r').readlines()
print(sum(overlap_priority(overlap(ruck)) for ruck in rucks))
