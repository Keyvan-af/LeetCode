class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = max(nums)
    
        # Step 2: Find the longest subarray where all elements are equal to max_val
        longest = 0
        current_length = 0
        
        for num in nums:
            if num == max_val:
                current_length += 1
                longest = max(longest, current_length)
            else:
                current_length = 0

        return longest