from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n: int = len(rowSum)
        m: int = len(colSum)

        res: List[List[int]] = [[0] * m for _ in range(n)]
        i: int = 0
        j: int = 0

        while i < n and j < m:
            res[i][j] = min(rowSum[i], colSum[j])

            rowSum[i] -= res[i][j]
            colSum[j] -= res[i][j]

            if rowSum[i] == 0:
                i += 1
            else:
                j += 1

        return res


def main() -> None:
    rowSum: List[int] = [6,16,24]
    colSum: List[int] = [12,15,18]

    res: List[List[int]] = Solution().restoreMatrix(rowSum, colSum)
    print(res)


if __name__ == "__main__":
    main()
