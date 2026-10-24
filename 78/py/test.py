class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res: set[tuple[int, ...]] = set()

        def dfs(nums: tuple[int, ...]) -> None:
            res.add(nums)
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i + 1 :])

        dfs(tuple(nums))
        return [list(x) for x in res]


nums = [1, 2, 3]
print(Solution().subsets(nums))
