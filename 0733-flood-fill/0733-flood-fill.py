class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        target = image[sr][sc]
        if target == color:
            return image
        
        rows, cols = len(image), len(image[0])
        coords = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def helper(row, col):
            if 0 <= row < rows and 0 <= col < cols and target == image[row][col]: 
                image[row][col] = color
                for x, y in coords:
                    helper(row + x, col + y)
            return
        
        helper(sr, sc)
        return image