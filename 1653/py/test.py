from typing import List


class Solution:
    def minimumDeletions(self, s: str) -> int:
        n: int = len(s)
        dp: List[int] = [0 for _ in range(n + 1)]
        b_count: int = 0

        for i in range(n):
            if s[i] == "b":
                dp[i + 1] = dp[i]
                b_count += 1
            else:
                dp[i + 1] = min(dp[i] + 1, b_count)

        return dp[n]


def main() -> None:
    s: str = "aababbab"
    res: int = Solution().minimumDeletions(s)
    print(res)


if __name__ == "__main__":
    main()
