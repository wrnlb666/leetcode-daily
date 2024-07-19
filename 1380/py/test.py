from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        res: List[int] = list()
        m: int = len(matrix)
        n: int = len(matrix[0])
        
        def find_min_col(row: int):
            return min(range(n), key=lambda j: matrix[row][j])
        
        def is_max(val: int, col: int):
            return all(matrix[i][col] <= val for i in range(m))
        
        for i in range(m):
            min_col: int = find_min_col(i)
            candidate: int = matrix[i][min_col]
            
            if is_max(candidate, min_col):
                res.append(candidate)
        
        return res


def main() -> None:
    matrix: List[List[int]] = [[3,7,8],[9,11,13],[15,16,17]]
    res: List[int] = Solution().luckyNumbers(matrix)
    print(res)


if __name__ == "__main__":
    main()
