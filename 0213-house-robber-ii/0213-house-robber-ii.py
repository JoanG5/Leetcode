class Solution:
    def rob(self, nums: List[int]) -> int:
        # s[0] = nums[0]
        # s[1] = max(nums[0], nums[1])
        # s[2] = max(nums[2] + s[0], s[1])
        # s[n-1] = max(nums[n-1] + s[n-3], s[n-2])
        # s[n] = max(nums[n] + (s[n - 2] - nums[0]), s[n - 1])
        if len(nums) == 0: return 0
        if len(nums) <= 2: return max(nums)

        def helper(start, end):
            s = [0] * len(nums)
            s[start] = nums[start]
            s[start + 1] = max(nums[start], nums[start + 1])

            for i in range(start + 2, end):
                s[i] = max(nums[i] + s[i - 2], s[i - 1])

            return s[end - 1]
        
        range1 = helper(0, len(nums)-1)
        range2 = helper(1, len(nums))

        return max(range1, range2)
