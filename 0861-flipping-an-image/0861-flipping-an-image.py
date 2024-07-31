class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # rows, cols = len(image), len(image[0])
        # res = []
        # for i in range(rows):
        #     row = []
        #     for j in range(cols - 1, -1 , -1):
        #         if image[i][j] == 1: 
        #             row.append(0)
        #         else: 
        #             row.append(1)
        #     res.append(row)
        # return res

        rows, cols = len(image), len(image[0])
        for i in range(rows):
            l, r = 0, cols - 1
            while l <= r:
                image[i][r], image[i][l] = image[i][l], image[i][r]
                l += 1
                r -= 1
        
        for i in range(rows):
            for j in range(cols):
                if image[i][j] == 1: image[i][j] = 0
                else: image[i][j] = 1
        return image

