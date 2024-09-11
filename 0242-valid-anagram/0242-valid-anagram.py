class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        counter1 = {}
        counter2 = {}
        for i in range(len(s)):
            if s[i] in counter1: counter1[s[i]] += 1
            else: counter1[s[i]] = 1
            if t[i] in counter2: counter2[t[i]] += 1
            else: counter2[t[i]] = 1
        
        return counter1 == counter2