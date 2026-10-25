class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res: list[list[str]] = []
        path: list[str] = []

        def dfs(index: int) -> None:
            if index == len(s):
                res.append(path[:])
                return

            for i in range(index, len(s) + 1):
                curr: str = s[index:i]
                if curr and curr == curr[::-1]:
                    path.append(curr)
                    dfs(i)
                    path.pop()

        dfs(0)
        return res


s = "aab"
print(Solution().partition(s))
