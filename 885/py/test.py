from typing import List, Tuple


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        map: List[Tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res: List[List[int]] = []

        step: int = 1
        dir: int = 0
        while len(res) < rows * cols:
            for _ in range(2):
                for _ in range(step):
                    if (rStart >= 0 and rStart < rows and cStart >= 0 and cStart < cols):
                        res.append([rStart, cStart])
                    rStart += map[dir][0]
                    cStart += map[dir][1]

                dir = (dir + 1) % 4
            step += 1
        return res


def main() -> None:
    rows: int = 1
    cols: int = 4
    rStart: int = 0
    cStart: int = 0

    res: List[List[int]] = Solution().spiralMatrixIII(rows, cols, rStart, cStart)
    print(res)


if __name__ == "__main__":
    main()
