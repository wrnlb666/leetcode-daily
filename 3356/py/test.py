from typing import List


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        res: int = 0
        if not any(nums):
            return res
        for s, e, v in queries:
            for i in range(s, e+1):
                nums[i] -= min(v, nums[i])
            res += 1
            if not any(nums):
                return res
        return -1


def main() -> None:
    nums: List[int] = [2, 0, 2]
    queries: List[List[int]] = [[0, 2, 1], [0, 2, 1], [1, 1, 3]]
    res: int = Solution().minZeroArray(nums, queries)
    print(res)


if __name__ == "__main__":
    main()
