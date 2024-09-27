class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) <= 2:
            return max(nums)

        def helper(start, end):
            dp = [0] * len(nums)
            dp[start] = nums[start]
            dp[start + 1] = max(nums[start], nums[start + 1])

            for i in range(start + 2, end):
                dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

            return dp[end - 1]

        range1 = helper(0, len(nums) - 1)
        range2 = helper(1, len(nums))

        return max(range1, range2)