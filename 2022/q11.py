#!/usr/bin/env python
from parse import parse
from operator import itemgetter
import math

def monkey(data):
    def intlist(s):
        return [int(x) for x in s.split(', ')]

    d = parse(
        'Monkey {num:d}:\n'
        '  Starting items: {items:intlist}\n'
        '  Operation: new = old {op} {rval}\n'
        '  Test: divisible by {divisor:d}\n'
        '    If true: throw to monkey {true_monkey:d}\n'
        '    If false: throw to monkey {false_monkey:d}',
        data, dict(intlist=intlist)).named
    d['inspections'] = 0

    return d

def op(old, op, rval):
    rval = old if rval == 'old' else int(rval)
    return old*rval if op == '*' else old+rval

def run(rounds, worry_div):
    monkeys = [monkey(m) for m in open('data/q11.dat', 'r').read().split('\n\n')]
    mod = math.prod([m['divisor'] for m in monkeys])

    def round(monkey):
        for item in monkey['items']:
            monkey['inspections'] += 1
            item = op(item, monkey['op'], monkey['rval'])
            item = (item // worry_div) % mod
            if item % monkey['divisor'] == 0:
                monkeys[monkey['true_monkey']]['items'].append(item)
            else:
                monkeys[monkey['false_monkey']]['items'].append(item)
        monkey['items'] = []

    for r in range(rounds):
        for m in monkeys:
            round(m)

    active = sorted(monkeys, key=itemgetter('inspections'))[-2:]
    print(f"Monkey business ({rounds} rounds, worry_div: {worry_div}): "
          f"{active[0]['inspections'] * active[1]['inspections']}")

run(20, 3)
run(10000, 1)
