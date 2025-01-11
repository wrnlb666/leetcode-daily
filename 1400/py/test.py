from typing import List


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        table: List[int] = [0] * 26
        for c in s:
            table[ord(c)-97] += 1
        odd: int = 0
        for c in table:
            if c % 2 != 0:
                odd += 1
        if odd > k:
            return False
        return True


def main() -> None:
    s: str = "annabelle"
    k: int = 2
    res: bool = Solution().canConstruct(s, k)
    print(res)


if __name__ == "__main__":
    main()
