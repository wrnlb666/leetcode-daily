class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res: set[tuple[int, ...]] = set()
        total: int = 0

        def dfs(path: list[int]) -> None:
            nonlocal total
            if total == target:
                res.add(tuple(sorted(path)))
                return
            if total > target:
                return
            for can in candidates:
                total += can
                path.append(can)
                dfs(path)
                total -= can
                path.pop()

        dfs([])
        return [list(tu) for tu in res]


candidates = [2, 3, 6, 7]
target = 7
print(Solution().combinationSum(candidates, target))
