from collections import defaultdict

rules = open("data/p5-rules.txt", "r").read().splitlines()
jobs = open("data/p5-jobs.txt", "r").read().splitlines()

jobs = [list(map(int, j.split(","))) for j in jobs]

rulesets = defaultdict(set)
for rule in rules:
    before, target = rule.split("|")
    rulesets[int(target)].add(int(before))

valid = []
for j in jobs:
    invalid = False
    tasks = set(j)
    seen = set()
    for task in j:
        prereqs = rulesets[task] & tasks
        if len(prereqs - seen) > 0:
            invalid = True
            break
        seen.add(task)
    if not invalid:
        valid.append(j)

print(sum([j[len(j) // 2] for j in valid]))
