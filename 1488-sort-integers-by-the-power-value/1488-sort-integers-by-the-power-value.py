class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {}
        res = []

        def power(x):
            if x in memo:
                return memo[x]
            elif x == 1:
                return 0
            elif x % 2 == 0:
                memo[x] = 1 + power(x / 2)
            else:
                memo[x] = 1 + power(3 * x  + 1)
            
            return memo[x]
        
        for i in range(lo, hi + 1):
            cur = power(i)
            res.append((cur, i))

        res.sort(key=lambda x:(x[0], x[1]))
        return res[k - 1][1]
        