class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for j in range(len(nums)):
            instance = target - nums[j]
            for i in range(len(nums)):
                if i != j:
                    if nums[i] == instance:
                        return [i,j]