class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[m-1][n-1] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m-1 and j == n-1: continue

                if i + 1 >= m:
                    dVal = 0
                else:
                    dVal = dp[i + 1][j]
                if j + 1 >= n:
                    rVal = 0
                else:
                    rVal = dp[i][j + 1]
                
                dp[i][j] = rVal + dVal

        return dp[0][0]
                