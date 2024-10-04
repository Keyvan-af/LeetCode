class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        m = [() for _ in range(int(len(skill)/2))]
        for i in range(len(m)):
            m[i] = (skill[i], skill[-(i+1)], skill[i]+skill[-(i+1)])
        compare = m[0][2]
        result = []
        for s in m:
            if s[2] != compare:
                return -1
            else:
                result.append((s[0] * s[1]))
        return sum(result)