from typing import List


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if sentence1 == sentence2:
            return True
        s1: List[str] = sentence1.split()
        s2: List[str] = sentence2.split()
        l1: int = len(s1)
        l2: int = len(s2)

        if l1 == l2:
            return False

        if l1 > l2:
            l1, l2 = l2, l1
            s1, s2 = s2, s1

        left: int = 0
        for w1, w2 in zip(s1, s2):
            if w1 == w2:
                left += 1
            else:
                break

        right: int = 0
        s1 = s1[:left-1:-1] if left > 0 else s1[::-1]
        s2 = s2[:left-1:-1] if left > 0 else s2[::-1]
        for w1, w2 in zip(s1, s2):
            print(w1, w2)
            if w1 == w2:
                right += 1
            else:
                break

        if left + right != l1:
            return False
        return True


def main() -> None:
    sentence1: str = "xD iP tqchblXgqvNVdi"
    sentence2: str = "FmtdCzv Gp YZf UYJ xD iP tqchblXgqvNVdi"
    res: bool = Solution().areSentencesSimilar(sentence1, sentence2)
    print(res)


if __name__ == "__main__":
    main()
