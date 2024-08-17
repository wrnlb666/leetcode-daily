from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows: int = len(points)
        cols: int = len(points[0])
        previous_row: List[int] = points[0]

        for row in range(1, rows):
            left_max = [0] * cols
            right_max = [0] * cols
            current_row = [0] * cols

            left_max[0] = previous_row[0]
            for col in range(1, cols):
                left_max[col] = max(left_max[col - 1] - 1, previous_row[col])

            right_max[-1] = previous_row[-1]
            for col in range(cols - 2, -1, -1):
                right_max[col] = max(right_max[col + 1] - 1, previous_row[col])

            for col in range(cols):
                current_row[col] = points[row][col] + max(
                    left_max[col], right_max[col]
                )

            previous_row = current_row

        return max(previous_row)


def main() -> None:
    points: List[List[int]] = [[1,2,3],[1,5,1],[3,1,1]]
    res: int = Solution().maxPoints(points)
    print(res)


if __name__ == "__main__":
    main()
