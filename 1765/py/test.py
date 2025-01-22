from typing import List, Final


class Solution:
    def highestPeak(self, is_water: List[List[int]]) -> List[List[int]]:
        rows: int = len(is_water)
        columns: int = len(is_water[0])
        INF: Final[int] = rows * columns

        res: List[List[int]] = [[INF] * columns for _ in range(rows)]

        for row in range(rows):
            for col in range(columns):
                if is_water[row][col] == 1:
                    res[row][col] = 0

        for row in range(rows):
            for col in range(columns):
                min_dist = INF

                neighbor_row: int = row - 1
                neighbor_col: int = col
                if self.is_valid_cell(neighbor_row, neighbor_col, rows, columns):
                    min_dist = min(
                        min_dist,
                        res[neighbor_row][neighbor_col],
                    )

                neighbor_row = row
                neighbor_col = col - 1
                if self.is_valid_cell(neighbor_row, neighbor_col, rows, columns):
                    min_dist = min(
                        min_dist,
                        res[neighbor_row][neighbor_col],
                    )

                res[row][col] = min(
                    res[row][col], min_dist + 1
                )

        for row in range(rows - 1, -1, -1):
            for col in range(columns - 1, -1, -1):
                min_dist = INF

                neighbor_row = row + 1
                neighbor_col = col
                if self.is_valid_cell(neighbor_row, neighbor_col, rows, columns):
                    min_dist = min(
                        min_dist,
                        res[neighbor_row][neighbor_col],
                    )

                neighbor_row = row
                neighbor_col = col + 1
                if self.is_valid_cell(neighbor_row, neighbor_col, rows, columns):
                    min_dist = min(
                        min_dist,
                        res[neighbor_row][neighbor_col],
                    )

                res[row][col] = min(
                    res[row][col], min_dist + 1
                )

        return res

    def is_valid_cell(self, row: int, col: int, rows: int, columns: int) -> bool:
        return 0 <= row < rows and 0 <= col < columns


def main() -> None:
    isWater: List[List[int]] = [[0, 1], [0, 0]]
    res: List[List[int]] = Solution().highestPeak(isWater)
    print(res)


if __name__ == "__main__":
    main()
