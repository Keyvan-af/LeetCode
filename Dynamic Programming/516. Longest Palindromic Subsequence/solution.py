class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        # Fill the DP table
        for i in range(n - 1, -1, -1):  # start from the end of the string
            dp[i][i] = 1  # Every single character is a palindrome of length 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        
        # The answer is in dp[0][n-1]
        return dp[0][n - 1]