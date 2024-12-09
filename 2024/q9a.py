s = open("data/p9.txt").read().strip()
diskmap = [int(x) for x in s]


def map2disk(dm):
    if len(dm) % 2 != 0:
        dm.append(0)
    result = []
    for i, (used, free) in enumerate(zip(dm[::2], dm[1::2])):
        result.extend([i] * used)
        result.extend([None] * free)
    return result


def compress(disk):
    f = 0
    end = len(disk) - 1
    while f < end:
        while f < end and disk[f] is not None:
            f += 1
        while f < end and disk[end] is None:
            end -= 1
        disk[f], disk[end] = disk[end], disk[f]
    return disk


def checksum(disk):
    return sum(d * i for i, d in enumerate(disk) if d is not None)


d = compress(map2disk(diskmap))
print(checksum(d))
