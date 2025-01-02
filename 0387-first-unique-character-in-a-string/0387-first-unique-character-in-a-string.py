class Solution(object):
    def firstUniqChar(self, s):
        seen = Counter(s)
        for i in range(len(s)):
            if seen[s[i]] == 1:
                return i
    
        return -1 
        