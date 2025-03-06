from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n: int = len(grid)
        arr: List[int] = [0] * n * n
        for li in grid:
            for n in li:
                arr[n - 1] += 1
        res: List[int] = [0, 0]
        for i, n in enumerate(arr):
            if n == 1:
                continue
            if n == 0:
                res[1] = i + 1
            if n == 2:
                res[0] = i + 1
        return res


def main() -> None:
    grid: List[List[int]] = [[1, 3], [2, 2]]
    res: List[int] = Solution().findMissingAndRepeatedValues(grid)
    print(res)


if __name__ == "__main__":
    main()
