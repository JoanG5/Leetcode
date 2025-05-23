class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = 1, 1
        res = [1 for _ in range(len(nums))]

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            #[1, 1, 2, 6]
            res[i] *= postfix
            postfix *= nums[i]
        
        return res