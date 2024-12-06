from typing import List, Set


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ban_set: Set[int] = {b for b in banned if b <= maxSum}
        res: int = 0
        sum: int = 0
        for x in range(1, n+1):
            if x in ban_set:
                continue
            sum += x
            if sum > maxSum:
                break
            res += 1
        return res


def main() -> None:
    banned: List[int] = [11]
    n: int = 7
    maxSum: int = 50

    res: int = Solution().maxCount(banned, n, maxSum)
    print(res)


if __name__ == "__main__":
    main()
