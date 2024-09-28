class Solution:
    def countSubstrings(self, s: str) -> int:
        # Go through each letter
        # for each letter go through the helper function, one for odd and even
        # Starting from the middle if in bounds, 
        # # check if the left and right are equal
        # # If they are then add to the counter, and move left and right one
        # # Else break
        
        def helper(s, l, r):
            palindromes = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                palindromes += 1
                l -= 1
                r += 1
            return palindromes
        
        res = 0

        for i in range(len(s)):
            odd = helper(s, i, i)
            even = helper(s, i, i + 1)
            res += odd + even
        
        return res

