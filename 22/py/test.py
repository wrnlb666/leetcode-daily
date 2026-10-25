class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res: list[str] = []
        path: list[str] = []

        def dfs(left: int, right: int) -> None:
            if left == right == n:
                res.append("".join(path))
                return
            if left > n or right > n:
                return
            if left < n:
                path.append("(")
                left += 1
                dfs(left, right)
                left -= 1
                path.pop()
            if right < left:
                path.append(")")
                right += 1
                dfs(left, right)
                right -= 1
                path.pop()
            
        dfs(0, 0)
        return res


n = 3
print(Solution().generateParenthesis(n))
