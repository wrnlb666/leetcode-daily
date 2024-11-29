from typing import List, Tuple, Set
from heapq import heappush, heappop



class Solution:
    def _is_valid(self, visited, row, col, rows, cols):
        return (
                0 <= row < rows and
                0 <= col < cols and 
                (row, col) not in visited
        )


    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        rows, cols = len(grid), len(grid[0])
        directions: List[Tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited: Set[Tuple[int, int]] = set()

        pq: List[Tuple[int, int, int]] = [(grid[0][0], 0, 0)]

        while pq:
            time, i, j = heappop(pq)

            if (i, j) == (rows - 1, cols - 1):
                return time

            if (i, j) in visited:
                continue
            visited.add((i, j))
            
            for dx, dy in directions:
                new_i, new_j = i + dx, j + dy

                if not self._is_valid(visited, new_i, new_j, rows, cols):
                    continue

                wait_time: int = (
                    1 if (grid[new_i][new_j] - time) % 2 == 0 
                    else 0
                )
                new_time = max(grid[new_i][new_j] + wait_time, time + 1)
                heappush(pq, (new_time, new_i, new_j))

        return -1


def main() -> None:
    grid: List[List[int]] = [[0,1,3,2],[5,1,2,5],[4,3,8,6]]
    res: int = Solution().minimumTime(grid)
    print(res)


if __name__ == "__main__":
    main()
