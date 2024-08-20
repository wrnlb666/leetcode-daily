from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        length: int = len(piles)
        dp: List[List[int]] = [[0 for _ in range(length + 1)] for _ in range(length + 1)]

        suffix_sum: List[int] = [0 for _ in range(length + 1)]
        for i in range(length - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        for i in range(length + 1):
            dp[i][length] = suffix_sum[i]

        for index in range(length - 1, -1, -1):
            for max_till in range(length - 1, 0, -1):
                for X in range(1, min(2 * max_till, length - index) + 1):
                    dp[index][max_till] = max(
                        dp[index][max_till],
                        suffix_sum[index] - dp[index + X][max(max_till, X)],
                    )
        return dp[0][1]


def main() -> None:
    piles: List[int] = [2,7,9,4,4]
    res: int = Solution().stoneGameII(piles)
    print(res)


if __name__ == "__main__":
    main()
