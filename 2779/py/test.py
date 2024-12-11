from typing import List


class Solution:
    def maximumBeauty(self, nums: list[int], k: int) -> int:
        nums.sort()
        left: int = 0
        res: int = 0

        for right in range(len(nums)):
            while nums[right] - nums[left] > 2 * k:
                left += 1
            res = max(res, right - left + 1)

        return res


def main() -> None:
    nums: List[int] = [4,6,1,2]
    k: int = 2
    res: int = Solution().maximumBeauty(nums, k)
    print(res)


if __name__ == "__main__":
    main()
