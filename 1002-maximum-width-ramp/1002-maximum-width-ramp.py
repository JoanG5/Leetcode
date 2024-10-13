class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = [0]
        res = 0
        
        for i in range(1, len(nums)):
            val = nums[stack[-1]]
            if val > nums[i]:
                stack.append(i)
        
        for j in range(len(nums) -1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                    i = stack.pop()
                    res = max(res, j - i)
            
        return res
