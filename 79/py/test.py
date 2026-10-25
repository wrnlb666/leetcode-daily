from collections import Counter


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        dirs: list[tuple[int, int]] = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        total: dict[str, int] = Counter()
        needed: dict[str, int] = Counter(word)
        for row in board:
            total.update(row)
        for ch, count in needed.items():
            if total[ch] < count:
                return False

        if total[word[0]] > total[word[-1]]:
            word = word[::-1]

        del total
        del needed

        def dfs(row: int, col: int, index: int) -> bool:
            if index == len(word) - 1:
                return True

            for dr, dc in dirs:
                nr, nc = row + dr, col + dc
                if (
                    0 <= nr < len(board)
                    and 0 <= nc < len(board[0])
                    and board[nr][nc] == word[index + 1]
                ):
                    curr = board[nr][nc]
                    board[nr][nc] = '@'
                    if dfs(nr, nc, index + 1):
                        return True
                    board[nr][nc] = curr

            return False

        for i, row in enumerate(board):
            for j, ch in enumerate(row):
                if ch == word[0]:
                    curr = ch
                    board[i][j] = '@'
                    if dfs(i, j, 0):
                        return True
                    board[i][j] = curr
        return False


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(Solution().exist(board, word))
