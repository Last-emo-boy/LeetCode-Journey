class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 1:
                return
            grid[i][j] = 1  # mark as water
            for dx, dy in direction:
                dfs(i + dx, j + dy)

        # first, eliminate all lands that connect to the border
        for i in range(m):
            for j in range(n):
                if (i in [0, m - 1] or j in [0, n - 1]) and grid[i][j] == 0:
                    dfs(i, j)

        # second, count all the remaining closed islands
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    count += 1
                    dfs(i, j)

        return count