class Solution:
    MAPPING: dict[str, str]

    def __init__(self) -> None:
        self.MAPPING = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

    def letterCombinations(self, digits: str) -> list[str]:
        res: list[str] = []

        def dfs(path: list[str]):
            if len(path) == len(digits):
                res.append("".join(path))
                return
            curr: str = digits[len(path)]
            for ch in self.MAPPING[curr]:
                path.append(ch)
                dfs(path)
                path.pop()

        dfs([])
        return res


digits = "23"
print(Solution().letterCombinations(digits))
