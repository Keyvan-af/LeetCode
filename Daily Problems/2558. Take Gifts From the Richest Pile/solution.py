import heapq
import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap = [-g for g in gifts]
        heapq.heapify(max_heap)

        for _ in range(k):
            max_gifts = -heapq.heappop(max_heap)
            remaining = math.floor(math.sqrt(max_gifts))
            heapq.heappush(max_heap, -remaining)
        
        return -sum(max_heap)