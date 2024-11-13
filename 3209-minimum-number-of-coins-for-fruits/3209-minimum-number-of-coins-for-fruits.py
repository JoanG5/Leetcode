class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        '''
        Min number of coins on index i
        s[1] = p[1]
        s[2] = s[1] + p[2], s[1] + p[3], s[1] + p[4] 
        s[3] = s[2] + p[3], s[2] + p[4], s[2] + p[5], s[2] + p[6] 
        '''
        n = len(prices)
        s = [0] + [float('inf')] * n
        for i in range(1, n + 1):
            for j in range(i, min(i + i, n) + 1):
                s[j] = min(s[j], s[i - 1] + prices[i - 1])
        
        return s[-1]
