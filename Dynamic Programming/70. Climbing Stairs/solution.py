class Solution:
    def climbStairs(self, n: int) -> int:
            
        if n <= 1:
            return 1

        # Initialize the base cases
        first = 1
        second = 1

        # Calculate the number of ways for each step up to n
        for i in range(2, n + 1):
            third = first + second
            first = second
            second = third

        return second