class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l = r = 0
        counter = {}
        res = 0

        while r < len(s):
            while s[r] in counter and counter[s[r]] != 0 and l != r:
                counter[s[l]] -= 1
                l += 1
            counter[s[r]] = counter.get(s[r], 0) + 1
            r += 1
            res = max(res, r - l)
        
        return res

