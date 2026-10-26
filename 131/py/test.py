class Solution:
    def partition(self, s: str) -> list[list[str]]:
        n: int = len(s)
        res: list[list[str]] = []
        path: list[str] = []

        map: list[list[bool]] = [[True] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                map[i][j] = s[i] == s[j] and map[i + 1][j - 1]

        def dfs(index: int) -> None:
            if index == n:
                res.append(path[:])
                return

            for i in range(index, n):
                curr: str = s[index : i + 1]
                if map[index][i]:
                    path.append(curr)
                    dfs(i + 1)
                    path.pop()

        dfs(0)
        return res


s = "aab"
print(Solution().partition(s))
