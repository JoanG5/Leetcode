class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # c(0, 0) = text1[0] == text2[0]: 1 else: 0
        # c(1, 0) = c(0, 0) 
        # c(0, 1) = c(0, 0)
        # c(1, 1) = text1[1] == text2[1]: 1 + c(0, 0) else: max(c(0, 1), c(1, 0))
        # c(i, j) = text1[i] == text2[j]: 1 + c(i - 1, j - 1) else: max(c(i, j - 1), c(i - 1, j))
        dp = [[0 for _ in range(len(text2))] for _ in range(len(text1))]
        dp[0][0] = 1 if text1[0] == text2[0] else 0

        def helper(x, y):
            if x == 0 and y == 0:
                dp[0][0] = 1 if text1[0] == text2[0] else 0
            elif text1[x] == text2[y]:
                if x - 1 < 0 or y - 1 < 0:
                    prev = 0
                else:
                    prev = dp[x - 1][y - 1]
                    
                dp[x][y] = prev + 1
            else:
                if x - 1 < 0: 
                    prev1 = 0
                else: 
                    prev1 = dp[x - 1][y]

                if y - 1 < 0: 
                    prev2 = 0
                else: 
                    prev2 = dp[x][y - 1]

                dp[x][y] = max(prev1, prev2)
        
        for i in range(len(text1)):
            for j in range(len(text2)):
                helper(i, j)

        return dp[-1][-1]



