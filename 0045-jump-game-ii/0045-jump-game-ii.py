class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float(inf)] * len(nums)
        dp[0] = 0
        n = len(nums)
        for i in range(n):
            end = i + nums[i] + 1 if i + nums[i] + 1 <= n else n
            for j in range(i + 1, end):
                dp[j] = min(dp[j], dp[i] + 1)
        print(dp)
        return dp[-1]