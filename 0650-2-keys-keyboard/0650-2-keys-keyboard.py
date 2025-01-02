class Solution(object):
    def minSteps(self, n):
        def helper(n):
            if n < 2:
                return 0
            if n == 2:
                return 2
            
            # steps = n
            for i in range(n // 2, 0, -1):
                if n % i == 0:
                    steps = n // i + helper(i)
                    break
            
            return steps
    
        return helper(n)