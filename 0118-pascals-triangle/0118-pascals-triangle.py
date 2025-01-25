class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pas = [[1]]
        if numRows == 1: return pas
        pas.append([1, 1])

        for i in range(2, numRows):
            cur = [1]
            for j in range(len(pas[i - 1]) - 1):
                curNum = pas[i - 1][j] + pas[i - 1][j + 1]
                cur.append(curNum)
            cur.append(1)
            pas.append(cur)
        
        return pas

        '''
        [1]
        [1, 1]
        [1, 2, 1]
        [1, 3, 3, 1]
        [1, 4, 6, 4, 1]
        '''