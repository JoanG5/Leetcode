class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(n):
            res = 0
            for pile in piles:
                res += ceil(pile / n)
            return res

        left = 1
        right = max(piles)
    
        while left < right:
            mid = (left + right) // 2

            if check(mid) <= h:
                res = mid
                right = mid
            else:
                left = mid + 1
        
        return left