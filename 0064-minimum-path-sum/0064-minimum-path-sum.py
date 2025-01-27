class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        c = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        rows, cols = len(grid), len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if row == col == 0:
                    c[0][0] = grid[0][0]
                elif row == 0:
                    c[row][col] = grid[row][col] + c[row][col - 1]
                elif col == 0:
                    c[row][col] = grid[row][col] + c[row - 1][col]
                else:
                    c[row][col] = grid[row][col] + min(c[row - 1][col], c[row][col - 1])
        
        return c[-1][-1]
    

        
