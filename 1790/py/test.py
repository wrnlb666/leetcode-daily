from typing import Optional


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        c1: Optional[str] = None
        c2: Optional[str] = None
        swapped: bool = False
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if swapped:
                    return False
                if c1 is None:
                    c1 = s1[i]
                    c2 = s2[i]
                else:
                    if c1 != s2[i] or c2 != s1[i]:
                        return False
                    else:
                        swapped = True
        return swapped or c1 is None


def main() -> None:
    s1: str = "bank"
    s2: str = "kanb"
    res: bool = Solution().areAlmostEqual(s1, s2)
    print(res)


if __name__ == "__main__":
    main()
