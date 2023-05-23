class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        if n < 2:
            return s

        # 初始化动态规划数组
        dp = [[False] * n for _ in range(n)]

        start = 0  # 最长回文子串的起始位置
        max_len = 1  # 最长回文子串的长度

        # 单个字符是回文串
        for i in range(n):
            dp[i][i] = True

        # 填充动态规划数组
        for j in range(1, n):
            for i in range(j):
                if s[i] == s[j]:
                    # 首尾字符相同且去掉首尾字符后的子串是回文串
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False

                # 更新最长回文子串的位置和长度
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    start = i

        return s[start:start+max_len]
