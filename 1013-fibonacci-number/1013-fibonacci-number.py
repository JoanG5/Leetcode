class Solution:
    def fib(self, n: int) -> int:
        memo = {0: 0, 1: 1}

        for i in range(n + 1):
            memo[i + 2] = memo[i] + memo[i + 1]
        
        return memo[n]


        