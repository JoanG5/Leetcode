class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0
        coords = [(0,1), (1, 0), (0, -1), (-1, 0)]

        def dfs(x, y):
            if 0 <= x < rows and 0 <= y < cols and grid[x][y] == "1":
                grid[x][y] = "0"
                for dx, dy in coords:
                    dfs(x + dx, y + dy)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
        
        return count 
        


        
