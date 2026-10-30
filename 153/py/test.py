class Solution:
    def findMin(self, nums: list[int]) -> int:
        left: int = 0
        right: int = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            curr: int = nums[mid]
            print(nums[left], curr, nums[right])
            if curr <= nums[right]:
                right = mid
            else:
                left = mid + 1

        return nums[left]


nums = [3, 1, 2]
print(Solution().findMin(nums))
