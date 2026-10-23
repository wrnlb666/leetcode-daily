class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        res: int = 0
        queue: list[tuple[int, int]] = []
        remaining: int = 0
        for i, row in enumerate(grid):
            for j, n in enumerate(row):
                if n == 1:
                    remaining += 1
                if n == 2:
                    queue.append((i, j))

        while queue and remaining != 0:
            new_queue: list[tuple[int, int]] = []
            res += 1

            for rotted in queue:
                r, c = rotted
                if r != 0 and grid[r - 1][c] == 1:
                    grid[r - 1][c] = 2
                    remaining -= 1
                    new_queue.append((r - 1, c))
                if r != len(grid) - 1 and grid[r + 1][c] == 1:
                    grid[r + 1][c] = 2
                    remaining -= 1
                    new_queue.append((r + 1, c))
                if c != 0 and grid[r][c - 1] == 1:
                    grid[r][c - 1] = 2
                    remaining -= 1
                    new_queue.append((r, c - 1))
                if c != len(grid[0]) - 1 and grid[r][c + 1] == 1:
                    grid[r][c + 1] = 2
                    remaining -= 1
                    new_queue.append((r, c + 1))

            queue = new_queue

        if remaining == 0:
            return res
        return -1


grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
print(Solution().orangesRotting(grid))
