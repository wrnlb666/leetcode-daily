from typing import List, Set


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels: Set[str] = {"a", "e", "i", "o", "u"}
        prefix: List[int] = [0]
        curr: int = 0
        for w in words:
            if w[0] in vowels and w[-1] in vowels:
                curr += 1
            prefix.append(curr)

        res: List[int] = list()
        for s, e in queries:
            res.append(prefix[e+1] - prefix[s])
        return res


def main() -> None:
    words: List[str] = ["aba","bcb","ece","aa","e"]
    queries: List[List[int]] = [[0,2],[1,4],[1,1]]
    res: List[int] = Solution().vowelStrings(words, queries)
    print(res)


if __name__ == "__main__":
    main()
