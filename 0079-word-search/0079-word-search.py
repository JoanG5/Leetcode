class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()
        def dfs(r, c, index):
            if index >= len(word):
                return True
            if 0 <= r < rows and 0 <= c < cols and word[index] == board[r][c] and not (r, c) in visited:
                visited.add((r, c))
                result = dfs(r + 1, c, index + 1) or dfs(r - 1, c, index + 1) or dfs(r, c + 1, index + 1) or dfs(r, c -1, index + 1)
                visited.remove((r, c))
                return result
      
            return False
                

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0): 
                    return True
        return False
