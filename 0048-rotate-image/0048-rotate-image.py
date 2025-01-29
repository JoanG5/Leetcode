class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])

        for row in range(rows):
            for col in range(row, cols):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        for row in range(rows):
            left, right = 0, len(matrix[0]) - 1

            while left < right:
                matrix[row][left], matrix[row][right] = matrix[row][right], matrix[row][left]
                left += 1
                right -= 1
        
        