from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m = len(box)
        n = len(box[0])
        res = [["" for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                res[i][j] = box[j][i]

        for i in range(n):
            res[i].reverse()

        for j in range(m):
            lowest_row_with_empty_cell = n - 1
            for i in range(n - 1, -1, -1):
                if res[i][j] == "#":
                    res[i][j] = "."
                    res[lowest_row_with_empty_cell][j] = "#"
                    lowest_row_with_empty_cell -= 1
                if res[i][j] == "*":
                    lowest_row_with_empty_cell = i - 1

        return res


def main() -> None:
    box: List[List[str]] = [["#",".","#"]]
    res: List[List[str]] = Solution().rotateTheBox(box)
    print(res)


if __name__ == "__main__":
    main()
