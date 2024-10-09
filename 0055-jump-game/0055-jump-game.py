class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1: return True
        
        dp = [True] + [False] * (len(nums) - 1)

        for i in range(len(nums)):
            print(dp[i])
            if dp[i]:
                for j in range(i + 1, i + nums[i] + 1):
                    if j == len(nums) - 1:
                        return True
                    dp[j] = True
        return False