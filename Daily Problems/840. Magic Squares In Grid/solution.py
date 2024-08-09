class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        shape_row = len(grid)
        shape_col = len(grid[0])
        m = 0
        if shape_col >=3 and shape_row >=3:
            r = shape_row - 3
            c = shape_col -3
            if shape_col >= shape_row:
                for i in range(c+1):
                    for j in range(r+1):
                        numbers_1 = [m for m in grid[j][i:3+i]]
                        row_sum_1 = sum([m for m in grid[j][i:3+i]])
                        col_sum_1 = sum([m[i + 0] for m in grid[j:j+3]])
                        
                        numbers_2 = [m for m in grid[j+1][i:3+i]]
                        row_sum_2 = sum([m for m in grid[j+1][i:3+i]])
                        col_sum_2 = sum([m[i + 1] for m in grid[j:j+3]])

                        numbers_3 = [m for m in grid[j+2][i:3+i]]
                        row_sum_3 = sum([m for m in grid[j+2][i:3+i]])
                        col_sum_3 = sum([m[i + 2] for m in grid[j:j+3]])


                        diagonal_1  = sum([grid[m+j][m+i] for m in range(len(grid[j:j+3]))])
                        diagonal_2 = sum([grid[m+j][2-m+i] for m in range(len(grid[j:j+3]))])
                    if row_sum_1 == row_sum_2 == row_sum_3 == col_sum_1 == col_sum_2 == col_sum_3 == diagonal_1 == diagonal_2 and set(numbers_1+ numbers_2 + numbers_3) == {1,2,3,4,5,6,7,8,9}:
                        m = m + 1
            return m

        else:
            return m