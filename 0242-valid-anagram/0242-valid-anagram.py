class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        count_s, count_t = Counter(s), Counter(t)

        return count_s == count_t
        