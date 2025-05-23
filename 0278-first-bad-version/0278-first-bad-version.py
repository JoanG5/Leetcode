# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        
        while l < r:
            mid = (l + r) // 2
            if not isBadVersion(mid):
                l = mid + 1
            elif isBadVersion(mid):
                r = mid
        
        return r