import re

data = open("data/p3.txt", "r").read()

ms = re.findall(r"do\(\)|don\'t\(\)|mul\([0-9]+,[0-9]+\)", data)


s = 0
doing = True
for m in ms:
    if m == "do()":
        doing = True
        continue
    if m == "don't()":
        doing = False
        continue

    if doing:
        gs = re.match(r"mul\(([0-9]+),([0-9]+)\)", m).groups()
        s += int(gs[0]) * int(gs[1])

print(s)
