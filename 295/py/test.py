import heapq


class MedianFinder:
    lower: list[int]
    upper: list[int]

    def __init__(self):
        self.lower = []
        self.upper = []

    def addNum(self, num: int) -> None:
        lower, upper = self.lower, self.upper
        if not lower or num <= lower[0]:
            heapq.heappush_max(lower, num)
            if len(lower) - len(upper) > 1:
                heapq.heappush(upper, heapq.heappop_max(lower))
        else:
            heapq.heappush(self.upper, num)
            if len(upper) - len(lower) > 1:
                heapq.heappush_max(lower, heapq.heappop(upper))

    def findMedian(self) -> float:
        lower, upper = self.lower, self.upper
        if (len(lower) + len(upper)) % 2 == 0:
            return (lower[0] + upper[0]) / 2
        elif len(lower) > len(upper):
            return lower[0]
        else:
            return upper[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
