from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1

        q = deque([(0, 0, 1)]) 
        grid[0][0] = 1 

        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        while q:
            i, j, dist = q.popleft()
            if i == j == n - 1:
                return dist
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < n and not grid[x][y]:
                    grid[x][y] = 1 
                    q.append((x, y, dist + 1))
        return -1