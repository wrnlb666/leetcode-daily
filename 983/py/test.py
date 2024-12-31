from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last_day: int = days[-1]
        dp: List[int] = [0] * (last_day + 1)

        i: int = 0
        for day in range(1, last_day + 1):
            if day < days[i]:
                dp[day] = dp[day - 1]
            else:
                i += 1
                dp[day] = min(
                    dp[day - 1] + costs[0],
                    min(
                        dp[max(0, day - 7)] + costs[1], dp[max(0, day - 30)] + costs[2]
                    ),
                )
        return dp[last_day]


def main() -> None:
    days: List[int] = [1,4,6,7,8,20]
    costs: List[int] = [2,7,15]

    res: int = Solution().mincostTickets(days, costs)
    print(res)


if __name__ == "__main__":
    main()
