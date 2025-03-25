from typing import List


class Solution:
    def checkValidCuts(self, n: int, rectangles: list[list[int]]) -> bool:
        def check(rectangles: list[list[int]], dim: int) -> bool:
            res: int = 0
            rectangles.sort(key=lambda rect: rect[dim])
            end: int = rectangles[0][dim + 2]

            for i in range(1, len(rectangles)):
                rect: List[int] = rectangles[i]
                if end <= rect[dim]:
                    res += 1
                end = max(end, rect[dim + 2])

            return res >= 2

        return check(rectangles, 0) or check(rectangles, 1)


def main() -> None:
    n: int = 5
    rectangles: List[List[int]] = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]
    res: bool = Solution().checkValidCuts(n, rectangles)
    print(res)


if __name__ == "__main__":
    main()
