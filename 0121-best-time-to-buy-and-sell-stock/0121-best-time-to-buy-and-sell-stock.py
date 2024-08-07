class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        prof = 0
        while right < len(prices):
            dif = prices[right] - prices[left]
            if dif < 0:
                while left < right:
                    left += 1
            if dif > profit:
                profit = dif
            right += 1
        return prof