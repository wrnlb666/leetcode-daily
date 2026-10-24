class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if len(nums) <= 1:
            return [nums]

        res: list[list[int]] = []
        item: int = nums[-1]
        arrays: list[list[int]] = self.permute(nums[:-1])
        for array in arrays:
            for i in range(len(array) + 1):
                left: list[int] = array[:i]
                right: list[int] = array[i:]
                res.append(left + [item] + right)

        return res


nums = [1, 2, 3]
print(Solution().permute(nums))
