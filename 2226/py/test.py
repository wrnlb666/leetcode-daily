from typing import List
import asyncio


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        max_candies: int = 0
        for candy in candies:
            max_candies = max(max_candies, candy)

        left = 0
        right = max_candies

        while left < right:
            middle = (left + right + 1) // 2

            if self._valid(candies, k, middle):
                left = middle
            else:
                right = middle - 1

        return left

    def _valid(self, candies: List[int], k: int, count: int) -> bool:
        children: int = 0

        for pile in candies:
            children += pile // count

        return children >= k


async def main() -> None:
    candies: List[int] = [5, 8, 6]
    k: int = 3
    res: int = Solution().maximumCandies(candies, k)
    print(res)


if __name__ == "__main__":
    asyncio.run(main())
