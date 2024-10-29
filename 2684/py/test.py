from typing import List
from functools import cache


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        @cache
        def traverse(i: int, j: int) -> int:
            if j + 1 == len(grid[0]):
                return 0
            up: int = 0
            mid: int = 0
            down: int = 0
            if i > 0 and grid[i-1][j+1] > grid[i][j]:
                up = traverse(i-1, j+1) + 1
            if grid[i][j+1] > grid[i][j]:
                mid = traverse(i, j+1) + 1
            if i < len(grid)-1 and grid[i+1][j+1] > grid[i][j]:
                down = traverse(i+1, j+1) + 1
            return max(up, mid, down)

        res: int = 0
        for i in range(len(grid)):
            res = max(res, traverse(i, 0))

        return res


def main() -> None:
    grid: List[List[int]] = [[3,2,4],[2,1,9],[1,1,7]]
    res: int = Solution().maxMoves(grid)
    print(res)


if __name__ == "__main__":
    main()
