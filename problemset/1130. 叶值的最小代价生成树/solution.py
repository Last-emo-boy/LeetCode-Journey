class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[float('inf')]*n for _ in range(n)]
        max_arr = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0
            max_arr[i][i] = arr[i]
        for length in range(2, n+1):
            for i in range(n-length+1):
                j = i + length - 1
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + max_arr[i][k]*max_arr[k+1][j])
                max_arr[i][j] = max(max_arr[i][j-1], arr[j])
        return dp[0][n-1]