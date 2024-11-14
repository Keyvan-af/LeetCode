import math

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def can_distributed(x):
            stores_needed = sum(math.ceil(q/x) for q in quantities)
            return stores_needed <= n

        left, right = 1 , max(quantities)

        while left < right:
            mid = (left + right) // 2
            if can_distributed(mid):
                right = mid
            else: 
                left = mid + 1
            
        return left