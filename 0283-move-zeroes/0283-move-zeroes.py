class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        [1,3,12,0,0]
                |
                    |
        """
        zero, num = 0, 0

        while zero < len(nums) and num < len(nums):
            while zero < len(nums) and nums[zero] != 0:
                zero += 1
            while num < len(nums) and (nums[num] == 0 or num <= zero):
                num += 1

            if zero < len(nums) and num < len(nums):
                nums[zero], nums[num] = nums[num], nums[zero]


                        
