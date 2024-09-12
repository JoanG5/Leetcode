class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (r + l) // 2

            if nums[mid] >= nums[l]:
                if nums[mid] > target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            
            if nums[mid] == target: return mid
            if nums[l] == target: return l
            if nums[r] == target: return r 
        return -1
                    
