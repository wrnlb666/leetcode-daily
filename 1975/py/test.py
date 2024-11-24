from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        res: int = 0
        curr: int = 999999
        count: int = 0

        for line in matrix:
            for v in line:
                res += abs(v)
                if v < 0:
                    count += 1
                curr = min(curr, abs(v))

        if count % 2 != 0:
            res -= 2 * curr

        return res


def main() -> None:
    matrix: List[List[int]] = [[1,-1],[-1,1]]
    res: int = Solution().maxMatrixSum(matrix)
    print(res)


if __name__ == "__main__":
    main()
