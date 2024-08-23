class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        # Edge case: if there's only one or two steps
        if n == 1:
            return cost[0]
        elif n == 2:
            return min(cost[0], cost[1])
        
        # Initialize the minimum costs for the first two steps
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        # Fill the dp array with minimum costs for each step
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        # The minimum cost to reach the top is the minimum of the last two steps
        return min(dp[n-1], dp[n-2])