class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # if M then GG
        # if E then reveal adj, DFS or BFS
        # # While searhcing E's if there is an adj bomb then apply number

        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        else:
            board[click[0]][click[1]] = 'B'

        rows, cols = len(board), len(board[0])
        travel = [(0, 1), (1, 0), (0, -1), (-1, 0),
                (1, 1), (1, -1), (-1, 1), (-1, -1)]
        q = deque()
        q.append((click[0], click[1]))
        visit = set()
        while q:
            r, c = q.popleft()
            mine = 0
            neighbors = []


            for dr, dc in travel:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols:
                    if board[nr][nc] == 'M':
                        mine += 1
                    elif board[nr][nc] == 'E' and (nr, nc) not in visit:
                        neighbors.append((nr, nc))

            if mine > 0:
                board[r][c] = str(mine)
            else:
                board[r][c] = 'B'
                for neighbor in neighbors:
                    visit.add(neighbor)
                    q.append(neighbor)
                
        return board
                     

'''
[["B",1,1,1,"B"],
 ["B",1,"M",1,"B"],
 ["B",1,1,1,"B"],
 ["B","B","B","B","B"]]
'''