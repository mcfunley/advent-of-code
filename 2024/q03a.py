import re

data = open("data/p3.txt", "r").read()

muls = re.findall(r"mul\([0-9]+,[0-9]+\)", data)
s = 0
for m in muls:
    gs = re.match(r"mul\(([0-9]+),([0-9]+)\)", m).groups()
    s += int(gs[0]) * int(gs[1])

print(s)
