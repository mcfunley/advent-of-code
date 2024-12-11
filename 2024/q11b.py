from functools import cache

s = "4189 413 82070 61 655813 7478611 0 8"
iterations = 75

stones = [int(x) for x in s.split()]


@cache
def count(x, it):
    if it == iterations:
        return 1

    if x == 0:
        return count(1, it + 1)

    digits = list(str(x))
    if len(digits) % 2 == 0:
        m = len(digits) // 2
        left = count(int("".join(digits[:m])), it + 1)
        right = count(int("".join(digits[m:])), it + 1)
        return left + right

    return count(x * 2024, it + 1)


print(sum(count(x, 0) for x in stones))
