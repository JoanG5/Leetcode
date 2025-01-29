class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        x = abs(x)
        cur = 0
        ten = 10
        while x > 0:
            r = x % ten
            cur = cur + r / ten
            x = x - r 
            cur *= 10
            ten *= 10
        
        if cur >= 2**31 or cur <= -2**31: return 0

        return -int(cur) if negative else int(cur)

        
