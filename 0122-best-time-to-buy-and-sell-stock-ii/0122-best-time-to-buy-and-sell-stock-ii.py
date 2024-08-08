class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        start = end = 0
        for i in range(len(prices) - 1):
            print(end)
            if prices[end] < prices[i + 1]:
                end = i + 1
            else:
                profit += (prices[end] - prices[start])
                start = end = i + 1

        if end == len(prices) - 1: profit += (prices[end] - prices[start])

        return profit
