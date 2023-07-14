class Solution:
    def distributeCoins(self, root):
        self.res = 0
        def dfs(node):
            if not node:
                return 0
            L, R = dfs(node.left), dfs(node.right)
            self.res += abs(L) + abs(R)
            return node.val + L + R - 1

        dfs(root)
        return self.res