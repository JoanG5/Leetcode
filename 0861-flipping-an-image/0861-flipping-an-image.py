class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        res = []
        for i in range(rows):
            row = []
            for j in range(cols - 1, -1 , -1):
                if image[i][j] == 1: 
                    row.append(0)
                else: 
                    row.append(1)
            res.append(row)
        return res