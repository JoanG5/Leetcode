class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices) - 1):
            buy, sell = prices[i], prices[i + 1]
            if sell > buy:
                res += sell - buy
        return res

