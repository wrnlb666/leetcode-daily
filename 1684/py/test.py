from typing import List, Set


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s: Set[str] = set(x for x in allowed)
        res: int = 0
        for word in words:
            for c in word:
                if c not in s:
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
