class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ""

        def expand_around_center(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
        
        l = r = 0

        for i in range(len(s)):
            odd = expand_around_center(s, i, i)
            even = expand_around_center(s, i, i + 1)
            max_len = max(odd, even) 
        
            if max_len > r - l:
                    l = i - (max_len - 1) // 2
                    r = i + max_len // 2
        
        return s[l:r+1]