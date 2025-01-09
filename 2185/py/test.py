from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        def has_prefix(s: str, pref: str) -> int:
            i: int = 0
            while i < len(s) and i < len(pref):
                if s[i] != pref[i]:
                    return 0
                i += 1
            if i != len(pref):
                return 0
            return 1

        res: int = 0
        for word in words:
            res += has_prefix(word, pref)
        return res


def main() -> None:
    words: List[str] = ["pay","attention","practice","attend"]
    pref: str = "at"
    res: int = Solution().prefixCount(words, pref)
    print(res)


if __name__ == "__main__":
    main()
