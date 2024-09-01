class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid = obstacleGrid
        m = len(grid)
        n = len(grid[0])

        # If the starting point or the ending point has an obstacle, return 0
        if grid[0][0] == 1 or grid[m-1][n-1] == 1:
            return 0

        # Initialize dp array
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        # Fill the first row
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] if grid[0][j] == 0 else 0

        # Fill the first column
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] if grid[i][0] == 0 else 0

        # Fill the rest of the dp array
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 0

        return dp[m-1][n-1]

