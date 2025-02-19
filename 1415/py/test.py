from typing import List


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        count: int = 0
        res: str = ""
        def rec(s: str) -> None:
            nonlocal count
            nonlocal k
            if len(s) > n or count == k:
                return
            if len(s) == n:
                count += 1
            last: str = s[-1]
            if count == k:
                nonlocal res
                res = s
                return
            if last == 'a' and count != k:
                rec(s+'b')
                rec(s+'c')
            elif last == 'b' and count != k:
                rec(s+'a')
                rec(s+'c')
            elif last == 'c' and count != k:
                rec(s+'a')
                rec(s+'b')
        rec('a')
        if count != k:
            rec('b')
        if count != k:
            rec('c')
        return res


def main() -> None:
    n: int = 3
    k: int = 9
    res: str = Solution().getHappyString(n, k)
    print(res)


if __name__ == "__main__":
    main()
