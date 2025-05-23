class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        l = r = total =  0

        while l < len(nums) and r < len(nums):
            total += nums[r]
            while total >= target and l <= r:
                res = min(res, (r - l) + 1)
                total -= nums[l]
                l += 1
            r += 1

        return res if res != float('inf') else 0