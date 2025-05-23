class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start, end = 0, len(nums)
        count = 0
        while start < end:
            if nums[start] == val:
                nums[start], nums[end - 1] = nums[end - 1], nums[start]
                end -= 1
            else:
                start += 1
        return end 