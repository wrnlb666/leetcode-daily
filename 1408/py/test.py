from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res: List[str] = list()
        for i, w1 in enumerate(words):
            for j, w2 in enumerate(words):
                if i == j:
                    continue
                if w1 in w2:
                    res.append(w1)
                    break
        return res


def main() -> None:
    words: List[str] = ["leetcoder","leetcode","od","hamlet","am"]
    res: List[str] = Solution().stringMatching(words)
    print(res)


if __name__ == "__main__":
    main()
