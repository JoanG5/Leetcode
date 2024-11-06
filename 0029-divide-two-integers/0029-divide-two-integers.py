class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negative = (dividend < 0) ^ (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        cur = dividend

        while cur >= divisor:
            temp = divisor
            mul = 1 
            while cur >= temp:
                cur -= temp
                res += mul
                mul += mul
                temp += temp
        
        if negative:
            res = -res

        return min(2**31 - 1, max(-2**31, res))      