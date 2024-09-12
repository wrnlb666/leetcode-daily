from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s: List[bool] = [False] * 26
        res: int = 0
        for c in allowed:
            s[ord(c) - 0x61] = True
        for word in words:
            for c in word:
                if not s[ord(c) - 0x61]:
                    break
            else:
                res += 1
        return res


def main() -> None:
    allowed: str = "ab"
    words: List[str] = ["ad","bd","aaab","baa","badab"]

    res: int = Solution().countConsistentStrings(allowed, words)
    print(res)


if __name__ == "__main__":
    main()
