class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        self.best = float('inf')
        board = [[0] * m for _ in range(n)]
        self.dfs(board, 0)
        return self.best

    def dfs(self, board, count):
        if count >= self.best: return
        n, m = len(board), len(board[0])
        x, y = -1, -1
        for i in range(n):
            for j in range(m):
                if board[i][j] == 0:
                    x, y = i, j
                    break
            if x != -1: break

        if x == -1:
            self.best = min(self.best, count)
            return

        for size in range(min(n - x, m - y), 0, -1):
            if self.check(board, x, y, size):
                self.fill(board, x, y, size, 1)
                self.dfs(board, count + 1)
                self.fill(board, x, y, size, 0)

    def check(self, board, x, y, size):
        for i in range(x, x + size):
            for j in range(y, y + size):
                if board[i][j]: return False
        return True

    def fill(self, board, x, y, size, val):
        for i in range(x, x + size):
            for j in range(y, y + size):
                board[i][j] = val