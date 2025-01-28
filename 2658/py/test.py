from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def process(
            grid: List[List[int]], visited: List[List[bool]], row: int, col: int
        ) -> int:
            if (
                row < 0
                or row >= len(grid)
                or col < 0
                or col >= len(grid[0])
                or grid[row][col] == 0
                or visited[row][col]
            ):
                return 0
            visited[row][col] = True
            return (
                grid[row][col]
                + process(grid, visited, row, col + 1)
                + process(grid, visited, row, col - 1)
                + process(grid, visited, row + 1, col)
                + process(grid, visited, row - 1, col)
            )

        rows: int = len(grid)
        cols: int = len(grid[0])
        res: int = 0
        visited: List[List[bool]] = [[False] * cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] > 0 and not visited[row][col]:
                    res = max(
                        res,
                        process(grid, visited, row, col),
                    )

        return res


def main() -> None:
    grid: List[List[int]] = [[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]
    res: int = Solution().findMaxFish(grid)
    print(res)


if __name__ == "__main__":
    main()
