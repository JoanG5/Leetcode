class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        coords = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = 0
        
        def dfs(row, col):
            if not (0 <= row < rows and 0 <= col < cols and grid[row][col] == 1): # IF NOT VALID
                return 0
            grid[row][col] = 0

            return dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1) + 1
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        return res

