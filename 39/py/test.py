class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res: list[list[int]] = []
        total: int = 0

        def dfs(path: list[int], start: int) -> None:
            nonlocal total
            if total == target:
                res.append(path[:])
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                can = candidates[i]
                total += can
                path.append(can)
                dfs(path, i)
                total -= can
                path.pop()

        dfs([], 0)
        return res


candidates = [2, 3, 6, 7]
target = 7
print(Solution().combinationSum(candidates, target))
