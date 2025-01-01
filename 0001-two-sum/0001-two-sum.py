class Solution(object):
    def twoSum(self, nums, target):
        hash = {}

        for i in range(len(nums)):
            if nums[i] in hash:
                return [hash[nums[i]], i]
            else:
                hash[target - nums[i]] = i
        
        