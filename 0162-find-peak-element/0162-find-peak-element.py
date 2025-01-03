class Solution(object):
    def findPeakElement(self, nums):
        l, r = 0, len(nums) - 1
        mid = 0
        while l < r:
            mid = (l + r) // 2

            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid + 1] > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return mid