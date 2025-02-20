from typing import List, Optional, Set


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums_set: Set[str] = set(nums)
        n: int = len(nums)

        def rec(n: int, s: str) -> Optional[str]:
            if len(s) == n:
                if s not in nums_set:
                    return s
                else:
                    return None
            res: Optional[str]
            res = rec(n, s + "0")
            if res is not None:
                return res
            res = rec(n, s + "1")
            return res

        res: Optional[str]
        res = rec(n, "0")
        if res is not None:
            return res
        res = rec(n, "1")
        if res is not None:
            return res
        return ""


def main() -> None:
    nums: List[str] = ["00","01"]
    res: str = Solution().findDifferentBinaryString(nums)
    print(res)


if __name__ == "__main__":
    main()
