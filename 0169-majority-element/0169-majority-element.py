class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = {}
        res = nums[0]
        for num in nums:
            if num in hash: hash[num] += 1
            else: hash[num] = 1

            if hash[num] > hash[res]:
                res = num
        
        return res