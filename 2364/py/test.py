from typing import List
from collections import Counter


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        count: Counter[int] = Counter()
        res: int = 0
        for i, n in enumerate(nums):
            res += i - count[n-i]
            count[n-i] += 1
        return res


def main() -> None:
    nums: List[int] = [1,2,3,4,5]
    res: int = Solution().countBadPairs(nums)
    print(res)


if __name__ in {"__main__", "__mp_main__"}:
    main()
