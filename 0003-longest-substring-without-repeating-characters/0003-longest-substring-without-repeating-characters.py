class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = {}
        start = max_length = 0

        for end in range(len(s)):
            while s[end] in hash:
                del hash[s[start]]
                start += 1
            
            hash[s[end]] = 1
            max_length = max(max_length, len(hash))

        return max_length


        