from typing import List, Dict
from collections import defaultdict


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def get_sum(n: int) -> int:
            return sum(map(int, list(str(n))))
        cache: Dict[int, List[int]] = defaultdict(list)
        for n in nums:
            cache[get_sum(n)].append(n)
        res: int = -1
        for _, li in cache.items():
            if len(li) == 1:
                continue
            li.sort()
            res = max(res, li[-1] + li[-2])
        return res


def main() -> None:
    nums: List[int] = [18,43,36,13,7]
    res: int = Solution().maximumSum(nums)
    print(res)


if __name__ == "__main__":
    main()
