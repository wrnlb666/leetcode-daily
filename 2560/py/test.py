from typing import List
import asyncio


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        left: int = 1
        right: int = max(nums)
        while left < right:
            mid: int = (left + right) // 2
            curr: int = 0
            i: int = 0
            while i < len(nums):
                if nums[i] <= mid:
                    curr += 1
                    i += 2
                else:
                    i += 1
            if curr >= k:
                right = mid
            else:
                left = mid + 1
        return left


async def main() -> None:
    nums: List[int] = [2, 3, 5, 9]
    k: int = 2
    res: int = Solution().minCapability(nums, k)
    print(res)


if __name__ == "__main__":
    asyncio.run(main())
