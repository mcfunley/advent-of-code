from collections import OrderedDict
from itertools import count, groupby

from pydantic import BaseModel

s = open("data/p9.txt").read().strip()
diskmap = [int(x) for x in s]


def debugprint(lst):
    print("".join(str(x) if x is not None else "." for x in lst))


class FreeBlock(BaseModel):
    index: int
    size: int

    def consume(self, size):
        if size > self.size:
            raise ValueError("Not enough space")
        self.size -= size
        self.index += size


class FreeList(BaseModel):
    blocks: list[FreeBlock] = []

    def add(self, index, size):
        if size > 0:
            self.blocks.append(FreeBlock(index=index, size=size))

    def search(self, size, maxindex) -> int:
        for block in self.blocks:
            if block.index >= maxindex:
                return None

            if block.size >= size:
                index = block.index
                block.consume(size)
                if block.size == 0:
                    self.blocks.remove(block)
                return index
        return None


class Disk(BaseModel):
    freelist: FreeList
    data: list = []

    def __init__(self, diskmap=None):
        super().__init__(freelist=FreeList())

        if len(diskmap) % 2 != 0:
            diskmap.append(0)

        for i, (used, free) in enumerate(zip(diskmap[::2], diskmap[1::2])):
            self.data.extend([i] * used)
            self.freelist.add(len(self.data), free)
            self.data.extend([None] * free)

    def checksum(self):
        return sum(d * i for i, d in enumerate(self.data) if d is not None)

    def compress(self):
        offs = len(self.data)
        for fileid, group in groupby(reversed(self.data.copy())):
            size = len(list(group))
            offs -= size
            if fileid is None:
                continue

            self.relocate(fileid, offs, size)

    def setdata(self, value, offs, size):
        for i in range(offs, offs + size):
            self.data[i] = value

    def relocate(self, fileid, offs, size):
        dest = self.freelist.search(size, offs)
        if dest is None:
            return

        self.setdata(None, offs, size)
        self.setdata(fileid, dest, size)


d = Disk(diskmap)
d.compress()
print(d.checksum())
