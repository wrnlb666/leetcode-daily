class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m: int = len(matrix)
        n: int = len(matrix[0])

        def get(index: int) -> int:
            row: int = index // n
            col: int = index % n
            return matrix[row][col]

        left: int = 0
        right: int = m * n - 1

        while left <= right:
            mid = (left + right) // 2
            curr: int = get(mid)
            if target == curr:
                return True
            if target < curr:
                right = mid - 1
            if target > curr:
                left = mid + 1
        return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
print(Solution().searchMatrix(matrix, target))
