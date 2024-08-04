class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums_list = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                sums_list.append(sum(nums[i:j+1]))

        sorted_list = sorted(sums_list)
        mod = 10**9 + 7
        return sum(sorted_list[left-1:right]) % mod