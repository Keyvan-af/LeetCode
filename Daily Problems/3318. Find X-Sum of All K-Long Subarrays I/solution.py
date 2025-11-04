from collections import defaultdict
from typing import List
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        results = []

        for i in range(0, n-k+1):
            freq = defaultdict(int)
            for j in range(i, i+k):
                freq[nums[j]] += 1

            items = [(count, val) for val, count in freq.items()]
            items.sort(key=lambda item: (-item[0], -item[1]))

            top_x_val = set()
            for idx in range(min(x, len(items))):
                top_x_val.add(items[idx][1])
            
            total = 0
            for j in range(i, i+k):
                if nums[j] in top_x_val:
                    total += nums[j]
                
            results.append(total)
        return results
