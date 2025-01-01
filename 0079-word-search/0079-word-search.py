class Solution(object):
    def exist(self, board, word):
        travel = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c, i):
            if 0 <= r < rows and 0 <= c < cols and word[i] == board[r][c] and (r, c) not in visited:
                if i == len(word) - 1:
                    return True 
                visited.add((r, c))
                res = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)
                visited.remove((r,c))
                return res 
            return False 
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True 
        return False
            
        