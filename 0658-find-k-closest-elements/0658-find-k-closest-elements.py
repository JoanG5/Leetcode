class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) <= k:
            return arr

        l, r = 0, len(arr) - 1

        while l < r:
            mid = (l + r) // 2

            if arr[mid] < x:
                l = mid + 1
            else:
                r = mid 

        left, right = l - 1, l

        while right - left - 1 < k:
            if left < 0:
                right += 1
            elif right >= len(arr):  
                left -= 1
            elif abs(arr[left] - x) <= abs(arr[right] - x): 
                left -= 1
            else:
                right += 1

        return arr[left + 1:right]