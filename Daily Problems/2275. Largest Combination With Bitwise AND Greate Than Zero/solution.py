from itertools import combinations

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        n = len(candidates)
        while n > 0:
            for combo in combinations(candidates, n):
                bitwise_and_result = combo[0]
                for num in combo[1:]:
                    bitwise_and_result &= num
                if bitwise_and_result >= 1:
                    return n
                    break
            n -= 1