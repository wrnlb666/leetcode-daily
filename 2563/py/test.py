from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        res: int = 0
        for i in range(len(nums)):
            low = self.lower_bound(nums, i + 1, len(nums) - 1, lower - nums[i])
            high = self.lower_bound(nums, i + 1, len(nums) - 1, upper - nums[i] + 1)
            res += high - low

        return res


    def lower_bound(self, nums, low, high, element):
        while low <= high:
            mid: int = (high +low) // 2
            if nums[mid] >= element:
                high = mid - 1
            else:
                low = mid + 1
        return low


def main() -> None:
    nums: List[int] = [0,1,7,4,4,5]
    lower: int = 3
    upper: int = 6

    res: int = Solution().countFairPairs(nums, lower, upper)
    print(res)


if __name__ == "__main__":
    main()
