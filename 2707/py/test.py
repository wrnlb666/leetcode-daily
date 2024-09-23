from typing import List, Set
from functools import cache


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n: int = len(s)
        dic: Set[str] = set(dictionary)
        @cache
        def dp(start):
            if start == n:
                return 0
            res: int = dp(start + 1) + 1
            for end in range(start, n):
                curr = s[start: end + 1]
                if curr in dic:
                    res = min(res, dp(end + 1))
            return res
            
        return dp(0)


def main() -> None:
    s: str = "leetscode"
    dictionary: List[str] = ["leet","code","leetcode"]
    res: int = Solution().minExtraChar(s, dictionary)
    print(res)


if __name__ == "__main__":
    main()
