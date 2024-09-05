class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        diff = (len(rolls) + n )* mean - sum(rolls)
        if 1 <= diff/n <= 6:
            start = diff//n   
            baghimunde = diff%n
            s = []
            for i in range(n):
                if baghimunde > 0:
                    s.append(start + 1)
                    baghimunde -= 1
                else:
                    s.append(start)
        else:
            s = []

        return s