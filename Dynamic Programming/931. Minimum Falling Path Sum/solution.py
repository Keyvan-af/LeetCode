class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for i in range(len(matrix)-2, -1, -1):
            for j in range(len(matrix[i])):
                if j == 0:
                    matrix[i][j] += min(matrix[i+1][j+1], matrix[i+1][j])
                elif j == len(matrix[i])-1:
                    matrix[i][j] += min(matrix[i+1][j-1], matrix[i+1][j])
                else:
                    matrix[i][j] += min(matrix[i+1][j-1], matrix[i+1][j+1], matrix[i+1][j])

        return min(matrix[0])