from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = Counter(word)
        sorting = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        result = 0

        for i in range(1, len(sorting)+1):
            if i%8 == 0:
                m = (i/8) -1
            else:
                m = i//8
            result = (sorting[i-1][1] * (m+1)) + result
        return int(result)