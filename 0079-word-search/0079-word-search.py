class Solution(object):
    def exist(self, board, word):
        rows, cols = len(board), len(board[0])
        seen = set()
        def dfs(r, c, i):
            if 0 <= r < rows and 0 <= c < cols and (r, c) not in seen and board[r][c] == word[i]:
                if i + 1 == len(word):
                    return True
                seen.add((r, c))
                res = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)
                seen.remove((r,c))
                return res
            return False
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        
        return False
        