from typing import List, Set, Tuple


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        rows: int = len(grid)
        cols: int = len(grid[0])

        def count_island():
            visited: Set[Tuple[int, int]] = set()
            count: int = 0
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 1 and (i, j) not in visited:
                        explore_island(i, j, visited)
                        count += 1
            return count

        def explore_island(i: int, j: int, visited: Set[Tuple[int, int]]):
            if (i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0 or (i, j) in visited):
                return
            visited.add((i, j))
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                explore_island(i + di, j + dj, visited)

        if count_island() != 1:
            return 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count_island() != 1:
                        return 1
                    grid[i][j] = 1

        return 2


def main() -> None:
    grid: List[List[int]] = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
    res: int = Solution().minDays(grid)
    print(res)


if __name__ == "__main__":
    main()
