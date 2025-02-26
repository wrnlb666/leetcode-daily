from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        def find_max(nums: List[int]) -> int:
            res: int = 0
            curr: int = 0
            for n in nums:
                curr += n
                res = max(curr, res)
                if curr < 0:
                    curr = 0
            return res
        def find_min(nums: List[int]) -> int:
            res: int = 0
            curr: int = 0
            for n in nums:
                curr += n
                res = min(curr, res)
                if curr > 0:
                    curr = 0
            return res
        return max(find_max(nums), -find_min(nums))


def main() -> None:
    nums: List[int] = [1,-3,2,3,-4]
    res: int = Solution().maxAbsoluteSum(nums)
    print(res)


if __name__ == "__main__":
    main()
