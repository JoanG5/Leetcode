class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prev):
            if 0 <= r < ROWS and 0 <= c < COLS and (r, c) not in visit and heights[r][c] >= prev:
                visit.add((r, c))
                for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    dfs(r + x, c + y, visit, heights[r][c])

        for i in range(COLS):
            dfs(0, i, pac, heights[0][i])          
            dfs(ROWS - 1, i, atl, heights[ROWS - 1][i])  
        
        for j in range(ROWS):
            dfs(j, 0, pac, heights[j][0])          
            dfs(j, COLS - 1, atl, heights[j][COLS - 1])  
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res
