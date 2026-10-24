class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res: list[list[int]] = []
        path: list[int] = []

        def dfs(start: int = 0) -> None:
            res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(i + 1)
                path.pop()

        dfs()
        return res


nums = [1, 2, 3]
print(Solution().subsets(nums))
