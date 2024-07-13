class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return mat
        row, col = len(mat), len(mat[0])
        res = [[float('inf') for _ in range(col)] for _ in range(row)]
        queue = deque()

        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    res[i][j] = 0
                    queue.append((i,j))

        coords = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            x, y = queue.popleft()
            for i, j in coords:
                dx, dy = x + i, y + j
                if 0 <= dx < row and 0 <= dy < col:
                    if res[dx][dy] > res[x][y] + 1:
                        res[dx][dy] = res[x][y] + 1
                        queue.append((dx, dy))

        return res 
