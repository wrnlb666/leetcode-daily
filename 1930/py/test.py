from typing import List, Set, Tuple


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        string: List[int] = list(map(lambda c: ord(c) - 97, s))
        left: List[int] = [0] * 26
        right: List[int] = [0] * 26

        left[string[0]] = 1
        for i in range(1, len(string)):
            c: int = string[i]
            right[c] += 1

        res: int = 0
        cache: Set[Tuple[int, int]] = set()
        for i in range(1, len(string) - 1):
            c: int = string[i]
            right[c] -= 1
            for j in range(26):
                if min(left[j], right[j]) != 0:
                    if (j, c) not in cache:
                        res += 1
                        cache.add((j, c))
            left[c] += 1

        return res


def main() -> None:
    s: str = "bbcbaba"
    res: int = Solution().countPalindromicSubsequence(s)
    print(res)


if __name__ == "__main__":
    main()
