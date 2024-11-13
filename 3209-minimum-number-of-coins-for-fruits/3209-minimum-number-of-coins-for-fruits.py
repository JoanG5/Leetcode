class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        '''
        s = [0, 3, 4, ]
        '''
        n = len(prices)
        s = [0] + [float('inf')] * n

        for i in range(1, len(prices) + 1):
            for j in range(i, min(i + i, n) + 1):
                s[j] = min(s[j], prices[i - 1] + s[i - 1])
        
        return s[n]
