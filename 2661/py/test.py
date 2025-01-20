from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m: int = len(mat)
        n: int = len(mat[0])
        rm: List[int] = [n] * m
        rn: List[int] = [m] * n
        i2n: List[int] = [0] * (m * n +1)
        i2m: List[int] = [0] * (m * n + 1)

        for i, row in enumerate(mat):
            for j, v in enumerate(row):
                i2m[v] = i
                i2n[v] = j

        def check(m: int, n: int) -> bool:
            rm[m] -= 1
            rn[n] -= 1
            if rm[m] == 0 or rn[n] == 0:
                return True
            return False

        for i, v in enumerate(arr):
            if check(i2m[v], i2n[v]):
                return i
        return -1


def main() -> None:
    arr: List[int] = [1,3,4,2]
    mat: List[List[int]] = [[1,4],[2,3]]
    res: int = Solution().firstCompleteIndex(arr, mat)
    print(res)


if __name__ == "__main__":
    main()
