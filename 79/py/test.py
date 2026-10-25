class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        dirs: list[tuple[int, int]] = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        used: set[tuple[int, int]] = set()

        def dfs(row: int, col: int, index: int) -> bool:
            if board[row][col] != word[index]:
                return False

            if index == len(word) - 1:
                return True

            for dr, dc in dirs:
                nr, nc = row + dr, col + dc
                if (
                    0 <= nr < len(board)
                    and 0 <= nc < len(board[0])
                    and (nr, nc) not in used
                ):
                    used.add((nr, nc))
                    if dfs(nr, nc, index + 1):
                        return True
                    used.remove((nr, nc))

            return False

        for i, row in enumerate(board):
            for j, ch in enumerate(row):
                used.add((i, j))
                if dfs(i, j, 0):
                    return True
                used.remove((i, j))
        return False


board = [["a", "a"]]
word = "aaa"
print(Solution().exist(board, word))
