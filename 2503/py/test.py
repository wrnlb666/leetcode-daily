from typing import List, Final
from queue import PriorityQueue


class Solution:
    DIRECTIONS: Final[List[List[int]]] = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        query_count: int = len(queries)
        res: List[int] = [0] * query_count
        rows: int = len(grid)
        cols: int = len(grid[0])
        total: int = rows * cols

        max_threshold = [0] * (total + 1)
        min_value = [[float("inf")] * cols for _ in range(rows)]

        min_value[0][0] = grid[0][0]
        heap = PriorityQueue()
        heap.put((grid[0][0], 0, 0))
        visited_cells = 0

        while not heap.empty():
            curr = heap.get()

            max_threshold[visited_cells + 1] = curr[0]
            visited_cells += 1

            for dir in self.DIRECTIONS:
                new_row, new_col = (
                    curr[1] + dir[0],
                    curr[2] + dir[1],
                )

                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                    and min_value[new_row][new_col] == float("inf")
                ):
                    min_value[new_row][new_col] = max(curr[0], grid[new_row][new_col])

                    heap.put((min_value[new_row][new_col], new_row, new_col))

        for i in range(query_count):
            threshold = queries[i]
            left, right = 0, total

            while left < right:
                mid = left + (right - left + 1) // 2

                if max_threshold[mid] < threshold:
                    left = mid
                else:
                    right = mid - 1

            res[i] = left

        return res


def main() -> None:
    grid: List[List[int]] = [[5, 2, 1], [1, 1, 2]]
    queries: List[int] = [3]
    res: List[int] = Solution().maxPoints(grid, queries)
    print(res)


if __name__ == "__main__":
    main()
