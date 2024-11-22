from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        res: int = 0

        for r in matrix:
            fr = [1 - x for x in r]

            curr = sum(
                1 
                for compare_row in matrix 
                if compare_row == r or compare_row == fr
            )

            res = max(res, curr)

        return res


def main() -> None:
    matrix: List[List[int]] = [[0,1],[1,1]]
    res: int = Solution().maxEqualRowsAfterFlips(matrix)
    print(res)


if __name__ == "__main__":
    main()
