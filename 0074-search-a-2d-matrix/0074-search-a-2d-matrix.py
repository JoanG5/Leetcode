class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        '''
        len = rows * cols
        mid - cols = row
        mid % cols = col
        '''

        start, end = 0, rows * cols - 1

        while start <= end:
            mid = (start + end) // 2
            r = mid // cols
            c = mid % cols

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                end = mid - 1
            else:
                start = mid + 1

        return False