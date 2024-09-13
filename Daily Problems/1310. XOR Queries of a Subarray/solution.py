class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        results = []
        for i in queries:
            res = arr[i[0]:i[1]+1]
            result = 0
            for num in res:
                result ^= num
            results.append(result)
        return results