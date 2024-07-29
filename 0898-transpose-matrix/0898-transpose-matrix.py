class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        res = []
        for i in range(cols):
            row = []
            for j in range(rows):
                row.append(matrix[j][i])
            res.append(row)
        return res