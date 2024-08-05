from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = Counter(arr)
        m = [item for item, count in counter.items() if count == 1]
        if len(m) >= k:
            return m[k-1]
        else:
            return ""