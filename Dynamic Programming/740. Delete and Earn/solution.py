class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: 
            return nums[0]
        freq = [0] * (max(nums) + 1)
        for num in nums: 
            freq[num] += num
        m1, m2 = 0, freq[1]
        for i in range(2, len(freq)):
            m3 = freq[i] + m1
            m1, m2 = m2, max(m3, m2)
        return m2