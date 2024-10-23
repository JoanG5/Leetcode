class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        def helper(n):
            output = 0

            while n:
                digit = n % 10
                output += digit ** 2
                n = n // 10
            
            return output 

        while not n in visit:
            visit.add(n)
            n = helper(n)

            if n == 1:
                return True
            
        return False
