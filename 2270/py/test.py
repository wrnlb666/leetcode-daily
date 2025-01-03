from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        sum_left: int = 0
        sum_right: int = sum(nums)
        res: int = 0
        for i in range(0, len(nums) - 1):
            n: int = nums[i]
            sum_left += n
            sum_right -= n
            if sum_left >= sum_right:
                res += 1
        return res


def main() -> None:
    nums: List[int] = [10,4,-8,7]
    res: int = Solution().waysToSplitArray(nums)
    print(res)


if __name__ == "__main__":
    main()
