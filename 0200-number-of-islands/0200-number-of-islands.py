class Solution(object):
    def numIslands(self, grid):
        rows, cols = len(grid), len(grid[0])
        travel = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        def dfs(r, c):
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1":
                grid[r][c] = "0"
                for nr, nc in travel:
                    dfs(r + nr, c + nc)
        res = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1": 
                    dfs(r, c)
                    res += 1
        
        return res
