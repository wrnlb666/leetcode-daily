class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        def board_init():
            board = []
            for i in range(n):
                row[queens[i]] = "Q"
                board.append("".join(row))
                row[queens[i]] = "."
            return board

        def dfs(row: int):
            if row == n:
                board = board_init()
                res.append(board)
            else:
                for i in range(n):
                    if i in cols or row - i in dia1 or row + i in dia2:
                        continue
                    queens[row] = i
                    cols.add(i)
                    dia1.add(row - i)
                    dia2.add(row + i)
                    dfs(row + 1)
                    cols.remove(i)
                    dia1.remove(row - i)
                    dia2.remove(row + i)

        res = []
        queens = [-1] * n
        cols = set()
        dia1 = set()
        dia2 = set()
        row = ["."] * n
        dfs(0)
        return res


n = 4
print(Solution().solveNQueens(n))
