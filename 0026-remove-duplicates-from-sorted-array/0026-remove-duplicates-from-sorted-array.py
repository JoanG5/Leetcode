class Solution(object):
    def removeDuplicates(self, nums):
        cur = 0
        seen = set()
        for i in range(len(nums)):
            if not nums[i] in seen:
                nums[cur] = nums[i]
                cur += 1
                seen.add(nums[i])
        return cur 