class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        lengths = [1] * n 
        counts = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if lengths[j] +1 > lengths[i]:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[j] +1 == lengths[i]:
                        counts[i] += counts[j]

        longest = max(lengths)
        return sum(counts[i] for i in range(n) if lengths[i] == longest)