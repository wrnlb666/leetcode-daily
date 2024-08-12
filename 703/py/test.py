from typing import List
import heapq


class KthLargest:
    k: int
    nums: List[int]

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = list()
        for i in range(len(nums)):
            self.add(nums[i])

    def add(self, val: int) -> int:
        if len(self.nums) < self.k or val > self.nums[0]:
            heapq.heappush(self.nums, val)
            if len(self.nums) > self.k:
                heapq.heappop(self.nums)
        return self.nums[0]


def main() -> None:
    input = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

    res: List[int] = list()
    k: KthLargest = KthLargest(input[0][0], input[0][1])
    for i in range(1, len(input)):
        res.append(k.add(input[i][0]))
    print(res)


if __name__ == "__main__":
    main()
