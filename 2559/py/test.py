from typing import List, Set


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels: Set[str] = {"a", "e", "i", "o", "u"}
        targets: List[int] = list()
        for i, w in enumerate(words):
            if w[0] in vowels and w[-1] in vowels:
                targets.append(i)

        def bs(targets: List[int], n: int) -> int:
            left: int = 0
            right: int = len(targets) - 1
            res: int = -1
            while left <= right:
                mid: int = (left + right) // 2
                if n < targets[mid]:
                    res = mid
                    right = mid - 1
                elif n > targets[mid]:
                    left = mid + 1
                else:
                    return mid
            return res

        res: List[int] = list()
        for s, e in queries:
            i: int = bs(targets, s)
            curr: int = 0
            if i == -1:
                res.append(curr)
                continue
            while i < len(targets) and targets[i] <= e:
                curr += 1
                i += 1
            res.append(curr)

        return res


def main() -> None:
    words: List[str] = ["aba","bcb","ece","aa","e"]
    queries: List[List[int]] = [[0,2],[1,4],[1,1]]
    res: List[int] = Solution().vowelStrings(words, queries)
    print(res)


if __name__ == "__main__":
    main()
