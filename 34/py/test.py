class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left: int = 0
        right: int = len(nums) - 1
        start: int = right

        while left <= right:
            mid = (left + right) // 2
            curr: int = nums[mid]
            if target <= curr:
                right = mid - 1
                start = mid
            else:
                left = mid + 1

        left: int = 0
        right: int = len(nums) - 1
        end: int = right
        while left <= right:
            mid = (left + right) // 2
            curr: int = nums[mid]
            print(left, mid, right)
            if target < curr:
                right = mid - 1
                end = mid - 1
            else:
                left = mid + 1

        if (
            start > end
            or start < 0
            or end < 0
            or nums[start] != target
            or nums[end] != target
        ):
            start = end = -1
        return [start, end]


nums = [1]
target = 1
print(Solution().searchRange(nums, target))
