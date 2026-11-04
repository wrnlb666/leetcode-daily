import heapq


class MedianFinder:
    lower: list[int]
    upper: list[int]

    def __init__(self):
        self.lower = []
        self.upper = []

    def _balance(self):
        while len(self.lower) - len(self.upper) > 1:
            tmp = heapq.heappop_max(self.lower)
            heapq.heappush(self.upper, tmp)

        while len(self.upper) - len(self.lower) > 1:
            tmp = heapq.heappop(self.upper)
            heapq.heappush_max(self.lower, tmp)

    def addNum(self, num: int) -> None:
        if not self.lower or num <= self.lower[0]:
            heapq.heappush_max(self.lower, num)
        elif not self.upper or num >= self.upper[0]:
            heapq.heappush(self.upper, num)
        elif len(self.lower) <= len(self.upper):
            heapq.heappush_max(self.lower, num)
        else:
            heapq.heappush(self.upper, num)
        self._balance()

    def findMedian(self) -> float:
        if (len(self.lower) + len(self.upper)) % 2 == 0:
            return (self.lower[0] + self.upper[0]) / 2
        elif len(self.lower) > len(self.upper):
            return self.lower[0]
        else:
            return self.upper[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
