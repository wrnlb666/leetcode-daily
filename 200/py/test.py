class UnionFind:
    grid: list[list[str]]
    parents: list[int]
    count: int
    row: int
    col: int

    def __init__(self, grid: list[list[str]]) -> None:
        self.grid = grid
        self.row = len(grid)
        self.col = len(grid[0])
        self.count = 0
        self.parents = [i for i in range(self.row * self.col)]
        for row in grid:
            for i in row:
                if i == "1":
                    self.count += 1

    def __len__(self) -> int:
        return self.count

    def get_index(self, row: int, col: int) -> int:
        return self.col * row + col

    def find(self, index: int) -> int:
        if self.parents[index] != index:
            self.parents[index] = self.find(self.parents[index])
        return self.parents[index]

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        self.parents[rb] = self.parents[ra]
        self.count -= 1
        return True


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        uf: UnionFind = UnionFind(grid)

        for i, row in enumerate(grid):
            for j, item in enumerate(row):
                if item == "0":
                    continue
                if i != 0 and grid[i - 1][j] == "1":
                    uf.union(uf.get_index(i - 1, j), uf.get_index(i, j))
                if j != 0 and row[j - 1] == "1":
                    uf.union(uf.get_index(i, j - 1), uf.get_index(i, j))

        return len(uf)


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]
print(Solution().numIslands(grid))
