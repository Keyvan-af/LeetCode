class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        m, n = len(word1), len(word2)
        
        # Create a DP table of size (m+1) x (n+1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Initialize base cases
        for i in range(m + 1):
            dp[i][0] = i  # Deleting all characters from word1
        for j in range(n + 1):
            dp[0][j] = j  # Inserting all characters of word2
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # Characters match, no change
                else:
                    dp[i][j] = min(dp[i - 1][j],    # Delete
                                dp[i][j - 1],    # Insert
                                dp[i - 1][j - 1] # Replace
                                ) + 1
        
        # The result is in dp[m][n]
        return dp[m][n]