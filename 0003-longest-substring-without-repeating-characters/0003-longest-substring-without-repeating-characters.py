class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}
        res = start = end = 0
        
        while end < len(s):
            while s[end] in count:
                count[s[start]] -= 1
                if count[s[start]] == 0:
                    del count[s[start]]
                start += 1
            count[s[end]] = count.get(s[end], 0) + 1
            end += 1
            res = max(res, end - start)
        
        return res
