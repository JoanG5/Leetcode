class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        Xcount = Ocount = 0
        
        for row in board:
            for c in row:
                if c == "O":
                    Ocount += 1
                elif c == "X":
                    Xcount += 1

        def check_winner(player):
            # Check rows & columns
            for i in range(3):
                if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
                    return True
            # Check diagonals
            if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
                return True
            return False
        
        xWins = check_winner("X")
        oWins = check_winner("O")
        
        if xWins and oWins: 
            return False  # Both players cannot win at the same time
        if xWins and Xcount != Ocount + 1:
            return False  # "X" must have exactly one more move
        if oWins and Xcount != Ocount:
            return False  # "O" must have equal moves as "X"
        
        return Xcount == Ocount or Xcount == Ocount + 1
