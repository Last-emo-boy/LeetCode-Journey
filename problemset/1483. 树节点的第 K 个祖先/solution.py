class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        self.dp = [[-1] * 20 for _ in range(n)]
        for i in range(n):
            self.dp[i][0] = parent[i]

        for j in range(1, 20):
            for i in range(n):
                if self.dp[i][j-1] != -1:
                    self.dp[i][j] = self.dp[self.dp[i][j-1]][j-1]

    def getKthAncestor(self, node: int, k: int) -> int:
        binary = bin(k)[2:][::-1]  # Convert k to binary and reverse the string
        ans = node

        for i in range(len(binary)):
            bit = int(binary[i])
            if bit == 1:
                if self.dp[ans][i] == -1:
                    return -1
                ans = self.dp[ans][i]

        return ans