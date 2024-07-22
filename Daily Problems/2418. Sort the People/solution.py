class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dicts = {heights[i]:names[i] for i in range(len(names))}
        sorted_dicts = sorted(dicts.items(), key=lambda x: x[0], reverse=True)
        result = [name[1] for name in sorted_dicts]
        return result