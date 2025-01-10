from typing import List


class Solution(object):
    def wordSubsets(self, A, B):
        def count(word):
            ans = [0] * 26
            for letter in word:
                ans[ord(letter) - ord("a")] += 1
            return ans

        bmax: List[int] = [0] * 26
        for b in B:
            for i, c in enumerate(count(b)):
                bmax[i] = max(bmax[i], c)

        res: List[str] = list()
        for a in A:
            if all(x >= y for x, y in zip(count(a), bmax)):
                res.append(a)
        return res


def main() -> None:
    words1: List[str] = ["amazon", "apple", "facebook", "google", "leetcode"]
    words2: List[str] = ["e", "o"]
    res: List[str] = Solution().wordSubsets(words1, words2)
    print(res)


if __name__ == "__main__":
    main()
