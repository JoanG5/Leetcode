class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()
        
        def dfs(r, c, i):
            if i >= len(word):
                return True
            
            if 0 <= r < rows and 0 <= c < cols and board[r][c] == word[i] and (r, c) not in visited:
                visited.add((r, c))
                value = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)
                visited.remove((r, c))
                return value
            
            return False

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True
        
        return False