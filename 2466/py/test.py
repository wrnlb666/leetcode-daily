from typing import List, Final


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp: List[int] = [1] + [-1] * (high)
        mod: Final[int] = 10 ** 9 + 7
        
        def dfs(end):
            if dp[end] != -1:
                return dp[end]
            count: int = 0
            if end >= zero:
                count += dfs(end - zero)
            if end >= one:
                count += dfs(end - one)
            dp[end] = count % mod
            return dp[end]
            
        return sum(dfs(end) for end in range(low, high + 1)) % mod


def main() -> None:
    low: int = 3
    high: int = 3
    zero: int = 1
    one: int = 1

    res: int = Solution().countGoodStrings(low, high, zero, one)
    print(res)


if __name__ == "__main__":
    main()
