class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def helper(left, right, replace):
            if replace > 1:
                return False
            
            while left < right:
                if s[left] != s[right]:
                    return helper(left + 1, right, replace + 1) or helper(left, right - 1, replace + 1)
                
                left += 1
                right -= 1
            
            return True
        
        return helper(0, len(s) - 1, 0)