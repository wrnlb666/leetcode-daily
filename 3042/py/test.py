from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res: int = 0
        for i in range(len(words)):
            w1: str = words[i]
            for j in range(i + 1, len(words)):
                w2: str = words[j]
                if w2.startswith(w1) and w2.endswith(w1):
                    res += 1
        return res


def main() -> None:
    words: List[str] = ["a", "aba", "ababa", "aa"]
    res: int = Solution().countPrefixSuffixPairs(words)
    print(res)


if __name__ == "__main__":
    main()
