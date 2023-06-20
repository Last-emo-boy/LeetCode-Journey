class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        size1, size2 = len(cost), len(cost[0])
        min_cost = [min(cost[i][j] for i in range(size1)) for j in range(size2)]

        dp = [[float('inf')] * (1 << size2) for _ in range(size1 + 1)]
        dp[0][0] = 0

        for i in range(size1):
            for j in range(1 << size2):
                for k in range(size2):
                    new_j = j | (1 << k)
                    dp[i + 1][new_j] = min(dp[i + 1][new_j], dp[i][j] + cost[i][k])

        for j in range(1 << size2):
            for k in range(size2):
                if not ((j >> k) & 1):
                    dp[size1][j | (1 << k)] = min(dp[size1][j | (1 << k)], dp[size1][j] + min_cost[k])

        return dp[size1][(1 << size2) - 1]