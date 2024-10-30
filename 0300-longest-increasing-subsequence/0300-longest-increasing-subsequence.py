class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [nums[0]]

        def binary_search(arr, target):
            l, r = 0, len(arr)
            
            while l <= r:
                mid = (l + r) // 2
                if arr[mid] > target:
                    r = mid - 1
                elif arr[mid] < target:
                    l = mid + 1
                else:
                    arr[mid] = target
                    return
            arr[l] = target

        for i in range(1, len(nums)):
            if res[-1] < nums[i]:
                res.append(nums[i])
            else:
                binary_search(res, nums[i])
		
        return len(res)
