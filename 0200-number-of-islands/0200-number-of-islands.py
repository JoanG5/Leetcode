class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        coords = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = 0

        def dfs(row, col):
            if 0 <= row < rows and 0 <= col < cols and grid[row][col] == "1":
                grid[row][col] = "0"
                for x, y in coords:
                    dfs(row + x, col + y)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i, j)
        
        return res


        
