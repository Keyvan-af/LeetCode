import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp will store the smallest tail of all increasing subsequences
        dp = []
        
        for x in nums:
            # Use binary search to find the index in dp where x can replace the current value
            idx = bisect.bisect_left(dp, x)
            
            # If idx is equal to the length of dp, append x to dp
            if idx < len(dp):
                dp[idx] = x
            else:
                dp.append(x)
        
        # The length of dp is the length of the longest increasing subsequence
        return len(dp)