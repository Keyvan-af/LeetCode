class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        marked = [False] * n
        score = 0

        while not all(marked):
            min_val = float('inf')
            min_index = -1
            for i in range(n):
                if not marked[i] and nums[i] < min_val:
                    min_val = nums[i]
                    min_index = i

            score += nums[min_index]
            if min_index > 0:
                marked[min_index - 1] = True
            marked[min_index] = True
            if min_index < n-1:
                marked[min_index + 1] = True
        
        return score