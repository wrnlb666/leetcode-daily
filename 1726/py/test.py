from typing import List
from collections import Counter


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        res: int = 0
        cache: Counter[int] = Counter()
        for i, no in enumerate(nums):
            for j in range(i+1, len(nums)):
                ni: int = nums[j]
                n: int = no * ni
                res += cache[n] * 8
                cache[n] += 1
        # print(cache)
        return res


def main() -> None:
    nums: List[int] = [2,3,4,6,8,12]
    res: int = Solution().tupleSameProduct(nums)
    print(res)


if __name__ == "__main__":
    main()
