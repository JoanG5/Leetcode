class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 40 - 4 1
        # 36 - 8 2
        # 28 - 16 4
        # 12 - 4 1
        # 8 - 8 2

        negative = (dividend < 0) ^ (divisor < 0) 
        d, dv = abs(dividend), abs(divisor)
        cur = d
        res = 0

        while cur >= dv:
            temp = dv
            mul = 1
            while temp <= cur:
                cur -= temp
                temp += temp
                res += mul
                mul += mul

        if negative: 
            res = -res 

        return min(2**31 - 1, max(-2**31, res))
