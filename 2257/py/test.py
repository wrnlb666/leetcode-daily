from typing import List, Final, Tuple, Set


class Solution:
    UNGUARDED: Final[int]   = 0
    GUARDED: Final[int]     = 1
    GUARD: Final[int]       = 2
    WALL: Final[int]        = 3

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid: List[List[int]] = [[self.UNGUARDED] * n for _ in range(m)]

        for row, col in guards:
            grid[row][col] = self.GUARD

        for row, col in walls:
            grid[row][col] = self.WALL

        def update(row: int, col: int, is_guarded: bool) -> bool:
            if grid[row][col] == self.GUARD:
                return True

            if grid[row][col] == self.WALL:
                return False

            if is_guarded:
                grid[row][col] = self.GUARDED
            return is_guarded

        for row in range(m):
            is_guarded = grid[row][0] == self.GUARD
            for col in range(1, n):
                is_guarded = update(row, col, is_guarded)
            is_guarded = grid[row][n - 1] == self.GUARD
            for col in range(n - 2, -1, -1):
                is_guarded = update(row, col, is_guarded)

        for col in range(n):
            is_guarded = grid[0][col] == self.GUARD
            for row in range(1, m):
                is_guarded = update(row, col, is_guarded)
            is_guarded = grid[m - 1][col] == self.GUARD
            for row in range(m - 2, -1, -1):
                is_guarded = update(row, col, is_guarded)

        count = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == self.UNGUARDED:
                    count += 1
        return count

def main() -> None:
    m: int = 4
    n: int = 6
    guards: List[List[int]] = [[0,0],[1,1],[2,3]]
    walls: List[List[int]] = [[0,1],[2,2],[1,4]]

    res: int = Solution().countUnguarded(m, n, guards, walls)
    print(res)


if __name__ == "__main__":
    main()
