class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle) - 2, -1, -1): # rows
            for j in range(len(triangle[i])): # value in rows
                min_sum = min(triangle[i + 1][j], triangle[i + 1][j + 1])
                cur = triangle[i][j]
                triangle[i][j] = cur + min_sum
        
        return triangle[0][0]