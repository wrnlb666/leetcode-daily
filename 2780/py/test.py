from typing import List, Dict
from collections import defaultdict


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        first: Dict[int, int] = defaultdict(int)
        second: Dict[int, int] = defaultdict(int)
        n = len(nums)

        for num in nums:
            second[num] += 1

        for i in range(n):
            num = nums[i]
            second[num] -= 1
            first[num] += 1

            if first[num] * 2 > i + 1 and second[num] * 2 > n - i - 1:
                return i

        return -1


def main() -> None:
    nums: List[int] = [2, 1, 3, 1, 1, 1, 7, 1, 2, 1]
    res: int = Solution().minimumIndex(nums)
    print(res)


if __name__ == "__main__":
    main()
