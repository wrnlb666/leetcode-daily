from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        sum1 = sum(grid[0])
        sum2 = 0
        res: int = 2 ** 63
        for i in range(len(grid[0])):
            sum1 -= grid[0][i]
            res = min(res, max(sum1, sum2))
            sum2 += grid[1][i]
        return res


def main() -> None:
    grid: List[List[int]] = [[2, 5, 4], [1, 5, 1]]
    res: int = Solution().gridGame(grid)
    print(res)


if __name__ == "__main__":
    main()
