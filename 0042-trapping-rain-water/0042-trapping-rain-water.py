class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        Two pointers
        keep track of largest value on both sides
        takes the min largest
        res += minlargest - cur
        '''
        l, r = 0, len(height) - 1
        maxL = maxR = res = 0

        while l < r:
            maxL = max(maxL, height[l])
            maxR = max(maxR, height[r])
            if maxL < maxR:
                res += maxL - height[l]
                l += 1
            else:
                res += maxR - height[r]
                r -= 1
        
        return res 

