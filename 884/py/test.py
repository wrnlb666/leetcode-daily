from typing import List
from collections import Counter


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        c: Counter[str] = Counter(s1.split(' ') + s2.split(' '))
        res: List[str] = list()
        for k, v in c.items():
            if v == 1:
                res.append(k)
        return res


def main() -> None:
    s1: str = "this apple is sweet"
    s2: str = "this apple is sour"
    res: List[str] = Solution().uncommonFromSentences(s1, s2)
    print(res)


if __name__ == "__main__":
    main()
