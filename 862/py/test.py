from typing import List, Tuple
from heapq import heappop, heappush


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        res: int = 999999
        total: int = 0
        prefix: List[Tuple[int, int]] = []

        for i, num in enumerate(nums):
            total += num
            if total >= k:
                res = min(res, i + 1)
            while (prefix and total - prefix[0][0] >= k):
                res = min(res, i - heappop(prefix)[1])
            heappush(prefix, (total, i))

        return -1 if res == 999999 else res


def main() -> None:
    nums: List[int] = [84,-37,32,40,95]
    k: int = 167
    res: int = Solution().shortestSubarray(nums, k)
    print(res)


if __name__ == "__main__":
    main()
