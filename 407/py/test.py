from typing import List
import heapq


class Cell:
    height: int
    row: int
    col: int

    def __init__(self, height: int, row: int, col: int) -> None:
        self.height = height
        self.row = row
        self.col = col

    def __lt__(self, other) -> bool:
        return self.height < other.height


class Solution:
    def trapRainWater(self, height_map: List[List[int]]) -> int:
        def is_valid_cell(row: int, col: int, row_nums: int, col_nums: int) -> bool:
            return 0 <= row < row_nums and 0 <= col < col_nums

        d_row: List[int] = [0, 0, -1, 1]
        d_col: List[int] = [-1, 1, 0, 0]

        row_nums: int = len(height_map)
        col_nums: int = len(height_map[0])

        visited: List[List[bool]] = [[False] * col_nums for _ in range(row_nums)]

        boundary: List[Cell] = list()

        for i in range(row_nums):
            heapq.heappush(boundary, Cell(height_map[i][0], i, 0))
            heapq.heappush(
                boundary,
                Cell(height_map[i][col_nums - 1], i, col_nums - 1),
            )
            visited[i][0] = visited[i][col_nums - 1] = True

        for i in range(col_nums):
            heapq.heappush(boundary, Cell(height_map[0][i], 0, i))
            heapq.heappush(
                boundary,
                Cell(height_map[row_nums - 1][i], row_nums - 1, i),
            )
            visited[0][i] = visited[row_nums - 1][i] = True

        res: int = 0

        while boundary:
            curr: Cell = heapq.heappop(boundary)
            min_height: int = curr.height

            for dir in range(4):
                n_row: int = curr.row + d_row[dir]
                n_col: int = curr.col + d_col[dir]

                if (
                    is_valid_cell(n_row, n_col, row_nums, col_nums)
                    and not visited[n_row][n_col]
                ):
                    n_height: int = height_map[n_row][n_col]

                    if n_height < min_height:
                        res += min_height - n_height

                    heapq.heappush(
                        boundary,
                        Cell(
                            max(n_height, min_height),
                            n_row,
                            n_col,
                        ),
                    )
                    visited[n_row][n_col] = True

        return res


def main() -> None:
    heightMap: List[List[int]] = [
        [1, 4, 3, 1, 3, 2],
        [3, 2, 1, 3, 2, 4],
        [2, 3, 3, 2, 3, 1],
    ]
    res: int = Solution().trapRainWater(heightMap)
    print(res)


if __name__ == "__main__":
    main()
