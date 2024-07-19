class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_row = [min(_) for _ in matrix]
        max_col = [max(_) for _ in zip(*matrix)]
        els = []
        for element in max_col:
            if element in min_row:
                els.append(element)
        return els
