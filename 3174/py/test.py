from typing import List


class Solution:
    def clearDigits(self, s: str) -> str:
        res: str = ""
        digits: int = 0
        for c in reversed(s):
            if c.isdigit():
                digits += 1
            elif digits > 0:
                digits -= 1
            else:
                res += c
        return res[::-1]


def main() -> None:
    s = "abc"
    res: str = Solution().clearDigits(s)
    print(res)


if __name__ == "__main__":
    main()
