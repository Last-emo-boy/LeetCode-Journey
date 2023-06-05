class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        rows = [','.join(map(str, row)) for row in grid]
        cols = [','.join(map(str, [grid[i][j] for i in range(n)])) for j in range(n)]

        return sum(row == col for row in rows for col in cols)