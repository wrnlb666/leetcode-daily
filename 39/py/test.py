class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res: list[list[int]] = []
        path: list[int] = []

        def dfs(total: int, start: int) -> None:
            if total == target:
                res.append(path[:])
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                can = candidates[i]
                total += can
                path.append(can)
                dfs(total, i)
                total -= can
                path.pop()

        dfs(0, 0)
        return res


candidates = [2, 3, 6, 7]
target = 7
print(Solution().combinationSum(candidates, target))
