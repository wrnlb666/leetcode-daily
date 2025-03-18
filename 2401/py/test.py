from typing import List


class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        curr: int = 0
        left: int = 0
        res: int = 0

        for right in range(len(nums)):
            while curr & nums[right] != 0:
                curr ^= nums[left]
                left += 1

            curr |= nums[right]

            res = max(res, right - left + 1)

        return res


def main() -> None:
    nums: List[int] = [1, 3, 8, 48, 10]
    res: int = Solution().longestNiceSubarray(nums)
    print(res)


if __name__ == "__main__":
    main()
