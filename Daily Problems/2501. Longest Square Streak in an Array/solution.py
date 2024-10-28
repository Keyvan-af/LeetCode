class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        set_nums = set(nums)
        max_streak = -1

        for num in nums:
            current_streak = 1
            current_num  = num

            while current_num ** 2 in set_nums:
                current_num = current_num ** 2
                current_streak += 1

            if current_streak >= 2:
                max_streak = max(max_streak, current_streak)
        
        return max_streak