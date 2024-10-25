class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        travel = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def helper(r, c):
            if 0 <= r < rows and 0 <= c < cols and board[r][c] == "O":
                board[r][c] = "B"
                for dr, dc in travel:
                    helper(r + dr, c + dc)
        
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and board[r][c] == "O":
                    helper(r, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "B":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
                

