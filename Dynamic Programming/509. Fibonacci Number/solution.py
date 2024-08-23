class Solution:
    def fib(self, n: int) -> int:
        first = 0
        second = 1
        dp = [first, second]
        if n <= 2:
            if n == 2:
                return 1
            if n == 1:
                return 1
        for i in range(2, n+1):
            dp.append(first+second)
            first = second
            second = dp[i]
        return dp[n]