class Solution:
    def tribonacci(self, n: int) -> int:
        first = 0
        second = 1
        third = 1
        if n < 4:
            if n == 3:
                return 2
            if n==2:
                return 1
            if n == 1:
                return 1
        dp = [first, second, third]
        for i in range(3,n+1):
            dp.append(first+second+third)
            first = second
            second = third
            third = dp[i]

        return dp[n]
