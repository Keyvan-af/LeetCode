class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
            m = len(grid)
            n = len(grid[0])

            # Create a dp array with the same dimensions as the grid
            dp = [[0] * n for _ in range(m)]

            # Initialize the starting point
            dp[0][0] = grid[0][0]

            # Fill in the first row
            for j in range(1, n):
                dp[0][j] = dp[0][j-1] + grid[0][j]

            # Fill in the first column
            for i in range(1, m):
                dp[i][0] = dp[i-1][0] + grid[i][0]

            # Fill in the rest of the dp table
            for i in range(1, m):
                for j in range(1, n):
                    dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

            # The minimum path sum is in the bottom-right corner
            return dp[m-1][n-1]