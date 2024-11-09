class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows, cols = len(board), len(board[0])
        travel = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        res = 0
        def dfs(r, c):
            if 0 <= r < rows and 0 <= c < cols and board[r][c] == "X":
                board[r][c] = "."
                for nr, nc in travel:
                    dfs(r + nr, c + nc)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "X":
                    res += 1
                    dfs(r, c)
        
        return res

