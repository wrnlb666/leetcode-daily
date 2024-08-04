from typing import List, Tuple
import heapq


class Solution:
    def rangeSum(self, nums, n, left, right):
        hq: List[Tuple[int, int]] = []
        for i in range(n):
            heapq.heappush(hq, (nums[i], i))

        res: int = 0
        mod: int = int(10e9 + 7)
        for i in range(1, right + 1):
            p: Tuple[int, int] = heapq.heappop(hq)
            if i >= left:
                res = (res + p[0]) % mod
            if p[1] < n - 1:
                p = (p[0] + nums[p[1] + 1], p[1] + 1)
                heapq.heappush(hq, p)
        return int(res)


def main() -> None:
    nums: List[int] = [1,2,3,4]
    n: int = 4
    left: int = 1
    right: int = 5

    res: int = Solution().rangeSum(nums, n, left, right)
    print(res)


if __name__ == "__main__":
    main()
