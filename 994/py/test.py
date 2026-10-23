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

        dirs: list[tuple[int, int]] = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue and remaining != 0:
            new_queue: list[tuple[int, int]] = []
            res += 1

            for rotted in queue:
                r, c = rotted
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < len(grid)
                        and 0 <= nc < len(grid[0])
                        and grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 2
                        new_queue.append((nr, nc))
                        remaining -= 1

            queue = new_queue

        if remaining == 0:
            return res
        return -1


grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
print(Solution().orangesRotting(grid))
