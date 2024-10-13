from typing import List, Tuple, DefaultDict
from collections import defaultdict


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        merged: List[Tuple[int, int]] = list()
        for i, num in enumerate(nums):
            for n in num:
                merged.append((n, i))
        merged.sort()

        freq: DefaultDict[int, int] = defaultdict(int)
        left: int = 0
        count: int = 0
        range_start: int = 0
        range_end: int = 10 ** 5 + 1

        for right in range(len(merged)):
            freq[merged[right][1]] += 1
            if freq[merged[right][1]] == 1:
                count += 1

            while count == len(nums):
                cur_range: int = merged[right][0] - merged[left][0]
                if cur_range < range_end - range_start:
                    range_start = merged[left][0]
                    range_end = merged[right][0]

                freq[merged[left][1]] -= 1
                if freq[merged[left][1]] == 0:
                    count -= 1
                left += 1

        return [range_start, range_end]


def main() -> None:
    nums: List[List[int]] = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
    res: List[int] = Solution().smallestRange(nums)
    print(res)


if __name__ == "__main__":
    main()
