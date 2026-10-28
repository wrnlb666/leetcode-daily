class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left: int = 0
        right: int = len(nums) - 1
        last: int = -1

        while left <= right:
            mid = (left + right) // 2
            curr: int = nums[mid]
            # print(nums[left], curr, nums[right])
            if target == curr:
                return mid
            if target < curr:
                right = mid - 1
            if target > curr:
                left = mid + 1
                last = max(last, mid)

        return last + 1


nums = [1, 3, 5, 7, 9, 11]
target = 10
print(Solution().searchInsert(nums, target))
