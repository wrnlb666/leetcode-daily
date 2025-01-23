from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows: int = len(grid)
        cols: int = len(grid[0]) if rows > 0 else 0
        res: int = 0


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    can: bool = False

                    for other in range(cols):
                        if other != col and grid[row][other] == 1:
                            can = True
                            break
                    if can:
                        res += 1
                    else:
                        for other in range(rows):
                            if other != row and grid[other][col] == 1:
                                can = True
                                break

                        if can:
                            res += 1

        return res


def main() -> None:
    grid: List[List[int]] = [[1,0],[1,1]]
    res: int = Solution().countServers(grid)
    print(res)


if __name__ == "__main__":
    main()
