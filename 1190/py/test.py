from typing import (
    List,
)


class Solution:
    def reverseParentheses(self, s: str) -> str:
        n: int = len(s)
        lookup_table: List[int] = []
        pair: List[int] = [0] * n

        # find `(`and ``)`
        for i in range(n):
            if s[i] == "(":
                lookup_table.append(i)
            if s[i] == ")":
                j = lookup_table.pop()
                pair[i] = j
                pair[j] = i

        # build new string
        res: List[str] = []
        index: int = 0
        direction: int = 1

        while index < n:
            if s[index] == "(" or s[index] == ")":
                index = pair[index]
                direction = -direction
            else:
                res.append(s[index])
            index += direction

        return "".join(res)


def main() -> None:
    s: str = "a(bcdefghijkl(mno)p)q"
    res: str = Solution().reverseParentheses(s)
    print(res)


if __name__ == "__main__":
    main()
