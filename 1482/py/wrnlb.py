from typing import (
    Tuple,
)
import time


class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        def isValid(x):
            total = 0
            currcount = 0
            for b in bloomDay:
                if x>=b:
                    currcount += 1
                else:
                    total += currcount // k
                    if total >= m:
                        return True
                    currcount = 0
            total += currcount // k
            if total >= m:
                return True

        if m*k > len(bloomDay):
            return -1
        left = min(bloomDay)
        right = max(bloomDay)
        while left < right:
            mid = left + (right - left)//2
            if isValid(mid):
                right = mid
            else:
                left = mid + 1
        return left


def main() -> None:
    bloomDay: list[int] = [1,10,2,9,3,8,4,7,5,6]
    m: int = 4
    k: int = 2

    res: int = Solution().minDays(bloomDay, m, k)
    print(res)


if __name__ == "__main__":
    main()
