class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])

        for row in range(rows):
            for col in range(row, cols):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        
        for row in range(rows):
            cur = matrix[row]
            left, right = 0, len(cur) - 1
            while left < right:
                cur[left], cur[right] = cur[right], cur[left]
                left += 1
                right -= 1
    
        