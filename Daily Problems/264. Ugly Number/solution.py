class Solution:
    def nthUglyNumber(self, n: int) -> int:
        m = [1]
        start = 1
        while n-1 > 0:
            start = start + 1
            x = start
            while x >= 1:
                if x % 3 == 0:
                    x = x / 3
                elif x % 2 == 0:
                    x = x / 2
                elif x % 5 == 0:
                    x = x / 5
                elif x == 1: 
                    m.append(start)
                    n = n - 1
                    break
                else:
                    x = -1
                    break

        return m[-1]