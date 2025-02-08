from typing import List, Dict
from collections import defaultdict
import heapq


class NumberContainers:
    n2i: Dict[int, List[int]]
    i2n: Dict[int, int]

    def __init__(self) -> None:
        self.n2i = defaultdict(list)
        self.i2n = dict()

    def change(self, index: int, number: int) -> None:
        self.i2n[index] = number
        heapq.heappush(self.n2i[number], index)

    def find(self, number: int) -> int:
        if not self.n2i[number]:
            return -1

        while self.n2i[number]:
            index = self.n2i[number][0]
            if self.i2n.get(index) == number:
                return index
            heapq.heappop(self.n2i[number])
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
