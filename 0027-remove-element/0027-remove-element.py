class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0

        while i < n:
            if nums[i] == val:
                nums[i], nums[n - 1] = nums[n - 1], nums[i]
                n -= 1  # decrement the length of the array by discarding the last element
            else:
                i += 1
        
        return n