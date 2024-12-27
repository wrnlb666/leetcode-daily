from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        table: List[int] = [0 for _ in values]
        table[0] = values[0]
        res: int = 0

        for i in range(1, len(values)):
            curr_right: int = values[i] - i
            res = max(res, table[i-1] + curr_right)
            curr_left: int = values[i] + i
            table[i] = max(table[i-1], curr_left)

        return res



def main() -> None:
    values: List[int] = [8,1,5,2,6]
    res: int = Solution().maxScoreSightseeingPair(values)
    print(res)


if __name__ == "__main__":
    main()
