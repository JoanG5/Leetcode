class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        # s = [0] * n 
        # s[0] = nums[0]
        # s[1] = max(s[0], nums[1])
        # s[2] = max(s[1], nums[2] + s[0])
        # s[n] = max(s[n - 1], nums[n] + s[n - 2])

        s = [0] * len(nums)
        s[0], s[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            s[i] = max(s[i - 1], nums[i] + s[i - 2])

        return s[-1] 