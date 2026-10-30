class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)

        left: int = 0
        right: int = n - 1
        while left < right:
            mid = (left + right) // 2
            curr: int = nums[mid]
            if curr < nums[right]:
                right = mid
            else:
                left = mid + 1

        k = left
        # print(k)
        index: int = -1

        left: int = 0
        right: int = n - 1
        while left <= right:
            mid = (left + right) // 2
            proj = (mid + k) % n
            curr: int = nums[proj]
            # print(
            #     f"left: {left}:{nums[(left + k) % n]}; "
            #     + f"mid: {mid}:{curr}; "
            #     + f"right: {right}:{nums[(right + k) % n]}"
            # )
            if target == curr:
                index = mid
                break
            if target < curr:
                right = mid - 1
            else:
                left = mid + 1
        return index if index == -1 else (index + k) % n


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(Solution().search(nums, target))
