from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curr: int = nums[0]
        last: int = nums[0]
        res: int = 0
        for i in range(1, len(nums)):
            n: int = nums[i]
            if n <= last:
                res = max(res, curr)
                curr = n
            else:
                curr += n
            last = n
        res = max(res, curr)
        return res


def main() -> None:
    nums: List[int] = [3,6,10,1,8,9,9,8,9]
    res: int = Solution().maxAscendingSum(nums)
    print(res)


if __name__ == "__main__":
    main()
