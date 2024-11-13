# Helper function to find the left bound for j
def binary_search_left(nums, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start

# Helper function to find the right bound for j
def binary_search_right(nums, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] <= target:
            start = mid + 1
        else:
            end = mid - 1
    return end
    
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        count = 0
        n = len(nums)

        for i in range(n - 1):
            # Find the left and right bounds for j using binary search
            left = binary_search_left(nums, i + 1, n - 1, lower - nums[i])
            right = binary_search_right(nums, i + 1, n - 1, upper - nums[i])

            if left <= right:
                count += right - left + 1

        return count


