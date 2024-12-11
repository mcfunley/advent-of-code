s = "4189 413 82070 61 655813 7478611 0 8"
# s = "125 17"
stones = [int(x) for x in s.split()]


def blink(ss):
    for s in ss:
        if s == 0:
            yield 1
        else:
            digits = list(str(s))
            if len(digits) % 2 == 0:
                m = len(digits) // 2
                yield int("".join(digits[:m]))
                yield int("".join(digits[m:]))
            else:
                yield s * 2024


for _ in range(25):
    stones = blink(stones)

print(sum(1 for _ in stones))
