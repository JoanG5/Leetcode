class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = 1
        for i in range(1, len(nums)):
            cur = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    cur = max(cur, dp[j] + 1)
            dp[i] += cur
                    
        return max(dp)

