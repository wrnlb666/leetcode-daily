class Solution:
    def partition(self, s: str) -> list[list[str]]:
        n: int = len(s)
        res: list[list[str]] = []
        path: list[str] = []

        def dfs(index: int) -> None:
            if index == n:
                res.append(path[:])
                return

            for i in range(index, n):
                curr: str = s[index : i + 1]
                if curr and curr == curr[::-1]:
                    path.append(curr)
                    dfs(i + 1)
                    path.pop()

        dfs(0)
        return res


s = "aab"
print(Solution().partition(s))
