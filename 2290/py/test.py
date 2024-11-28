from typing import List, Deque, Tuple, Final
from collections import deque


class Solution:
    dirs: List[Tuple[int, int]] = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def minimumObstacles(self, grid: List[List[int]]) -> int:
        def _is_valid(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        MAX_DIST: Final[int] = 999_999
        m, n = len(grid), len(grid[0])

        dist: List[List[int]] = [[MAX_DIST] * n for _ in range(m)]
        dist[0][0] = 0

        deque_cells: Deque[Tuple[int, int, int]] = deque([(0, 0, 0)])

        while deque_cells:
            obstacles, row, col = deque_cells.popleft()

            for dr, dc in self.dirs:
                new_row, new_col = row + dr, col + dc

                if (
                        _is_valid(new_row, new_col) and
                        dist[new_row][new_col] == MAX_DIST
                ):
                    if grid[new_row][new_col] == 1:
                        dist[new_row][new_col] = obstacles + 1
                        deque_cells.append((obstacles + 1, new_row, new_col))
                    else:
                        dist[new_row][new_col] = obstacles
                        deque_cells.appendleft((obstacles, new_row, new_col))

        return dist[m - 1][n - 1]


def main() -> None:
    grid: List[List[int]] = [[0,1,1],[1,1,0],[1,1,0]]
    res: int = Solution().minimumObstacles(grid)
    print(res)
    

if __name__ == "__main__":
    main()
