from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows: int = len(grid)
        cols: int = len(grid[0])
        res: int = 0
        for i in range(rows - 2):
            for j in range(cols - 2):
                if grid[i+1][j+1] == 5 and self.isMagic(grid, i, j):
                    res += 1
        return res

    def isMagic(self, grid: List[List[int]], x: int, y: int) -> bool:
        cols: List[int] = [0] * 3
        has: List[bool] = [False] * 10
        for i in range(x, x+3):
            curr: int = 0
            for j in range (y, y+3):
                num: int = grid[i][j]
                if num < 1 or num > 9:
                    return False
                if has[num]:
                    return False
                has[num] = True
                curr += num
                cols[j-y] += num
            if curr != 15:
                return False
        if grid[x][y] + grid[x+2][y+2] != 10:
            return False
        if grid[x][y+2] + grid[x+2][y] != 10:
            return False
        for v in cols:
            if v != 15:
                return False
        return True


def main() -> None:
    grid: List[List[int]] = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
    res: int = Solution().numMagicSquaresInside(grid)
    print(res)


if __name__ == "__main__":
    main()
