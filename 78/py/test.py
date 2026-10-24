class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def rec(nums: tuple[int, ...]) -> set[tuple[int, ...]]:
            res: set[tuple[int, ...]] = set()

            if len(nums) <= 1:
                return {tuple(nums)}

            for i in range(len(nums)):
                left = nums[:i]
                right = nums[i + 1 :]
                curr = left + right
                res.add(curr)
                res = res.union(rec(curr))

            return res

        sets = rec(tuple(nums))
        sets.add(())
        sets.add(tuple(nums))
        res = [list(x) for x in sets]
        return res


nums = [1, 2, 3]
print(Solution().subsets(nums))
