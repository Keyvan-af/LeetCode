class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        m = nums.count(1)
        # create another list for circular list
        num = nums + nums
        counter = []
        for i in range(len(num) - m):
            minus = num[i:i+m].count(1)
            result = m - minus
            counter.append(result)
        return min(counter)