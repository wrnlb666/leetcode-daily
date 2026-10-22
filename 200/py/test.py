class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        parents: list[int] = [i for i in range(len(grid) * len(grid[0]))]

        def get_index(row: int, col: int) -> int:
            return len(grid[0]) * row + col

        def get_val(index: int) -> bool:
            row: int = index // len(grid[0])
            col: int = index % len(grid[0])
            return grid[row][col] == "1"

        def find(index: int) -> int:
            if parents[index] != index:
                parents[index] = find(parents[index])
            return parents[index]

        def union(a: int, b: int) -> bool:
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            parents[ra] = rb
            return True

        for i, row in enumerate(grid):
            for j, item in enumerate(row):
                if item == "0":
                    continue
                if i != 0 and grid[i - 1][j] == "1":
                    union(get_index(i - 1, j), get_index(i, j))
                if j != 0 and row[j - 1] == "1":
                    union(get_index(i, j - 1), get_index(i, j))

        return sum([i == v and get_val(i) for i, v in enumerate(parents)])


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]
print(Solution().numIslands(grid))
