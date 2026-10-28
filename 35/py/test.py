class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        index: int = 0
        while index < len(nums):
            curr: int = nums[index]
            if curr >= target:
                return index
            index += 1
        return index
