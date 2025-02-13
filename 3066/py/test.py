from typing import List
import heapq


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        res: int = 0
        while (len(nums) >= 2 and nums[0] < k):
            x: int = heapq.heappop(nums)
            y: int = heapq.heappop(nums)
            heapq.heappush(nums, min(x, y) * 2 + max(x, y))
            res += 1
        return res


def main() -> None:
    nums: List[int] = [2,11,10,1,3]
    k: int = 10
    res: int = Solution().minOperations(nums, k)
    print(res)


if __name__ == "__main__":
    main()
