from collections import defaultdict

rules = open("data/p5-rules.txt", "r").read().splitlines()
jobs = open("data/p5-jobs.txt", "r").read().splitlines()
jobs = [list(map(int, j.split(","))) for j in jobs]

rulesets = defaultdict(set)
for rule in rules:
    before, target = rule.split("|")
    rulesets[int(target)].add(int(before))


def swap(j: list, a, b):
    ai = j.index(a)
    bi = j.index(b)
    j[ai], j[bi] = j[bi], j[ai]


def fix(job):
    fixed = False
    while 1:
        nfixed = 0
        tasks = set(job)
        seen = set()
        for task in job:
            prereqs = rulesets[task] & tasks
            missing = prereqs - seen
            if len(missing) > 0:
                swap(job, task, missing.pop())
                fixed = True
                nfixed += 1
                break

            seen.add(task)

        if nfixed == 0:
            break

    return fixed, job


fixed_jobs = [job for fixed, job in [fix(j) for j in jobs] if fixed]
print(sum([j[len(j) // 2] for j in fixed_jobs]))
