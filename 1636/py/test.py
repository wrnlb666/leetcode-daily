from typing import List, Counter
from collections import Counter


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter: Counter[int] = Counter(nums)
        return sorted(nums, key = lambda x: counter[x] * 200 - x)


def main() -> None:
    nums: List[int] = [-24,41,5,-36,-11,23,29,-28,47,30,29,38,-20,-45,50,49,-16,-31,21,-28,40,6,21,6,-36,-31,-50,43,30,0,23,40,40,23,-36,41,50,43,-28,14]
    res: List[int] = Solution().frequencySort(nums)
    print(res)


if __name__ == "__main__":
    main()
