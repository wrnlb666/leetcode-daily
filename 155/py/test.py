import heapq
from collections import Counter


class MinStack:
    stack: list[int]
    pq: list[int]
    deleted: Counter[int]

    def __init__(self):
        self.stack = []
        self.pq = []
        self.deleted = Counter()

    def push(self, value: int) -> None:
        self.stack.append(value)
        heapq.heappush(self.pq, value)

    def pop(self) -> None:
        n = self.stack.pop()
        self.deleted[n] += 1

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        while True:
            n = self.deleted[self.pq[0]]
            if not n:
                break
            for _ in range(n):
                n = heapq.heappop(self.pq)
                self.deleted[n] = 0
        return self.pq[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
