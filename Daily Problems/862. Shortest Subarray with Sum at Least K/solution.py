from collections import deque
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        
        # Compute prefix sum
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        # Deque to store indices of prefix_sum
        dq = deque()
        min_length = float('inf')
        
        for i in range(n + 1):
            # Check if there's a subarray ending at index i with a sum >= k
            while dq and prefix_sum[i] - prefix_sum[dq[0]] >= k:
                min_length = min(min_length, i - dq.popleft())
            
            # Maintain monotonicity of the deque
            while dq and prefix_sum[i] <= prefix_sum[dq[-1]]:
                dq.pop()
            
            dq.append(i)
        
        return min_length if min_length != float('inf') else -1