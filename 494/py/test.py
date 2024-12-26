from typing import List, Tuple, Dict


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache: Dict[Tuple[int, int], int] = dict()
        def dfs(nums_slice: List[int], index: int, curr_sum: int, target: int) -> int:
            if (index, curr_sum) in cache:
                return cache[(index, curr_sum)]
            res: int = 0
            if index == len(nums_slice):
                if curr_sum == target:
                    res += 1
                    return res
                return res
            curr: int = nums_slice[index]
            res += dfs(nums_slice, index + 1, curr_sum + curr, target)
            res += dfs(nums_slice, index + 1, curr_sum - curr, target)
            cache[(index, curr_sum)] = res
            return res
        return dfs(nums, 0, 0, target)


def main() -> None:
    nums: List[int] = [41,1,7,20,44,13,4,8,21,4,45,37,18,47,8,17,10,4,27,26]
    target: int = 38
    res: int = Solution().findTargetSumWays(nums, target)
    print(res)


if __name__ == "__main__":
    main()
