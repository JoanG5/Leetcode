class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(t) > len(s):
            return ""
        
        counter = {}
        check = {}
        
        for char in t:
            counter[char] = 1 + counter.get(char, 0)
            check[char] = 0
        
        def valid(dic1, dic2):
            for key in dic1:
                if dic2.get(key, 0) < dic1[key]:
                    return False
            return True
        
        l, r = 0, 0
        res = ""
        
        while l < len(s) and s[l] not in counter:
            l += 1
        r = l
        
        while r < len(s):
            if s[r] in counter:
                check[s[r]] += 1
            
            while valid(counter, check):
                if (r - l + 1 < len(res) or res == ""):
                    res = s[l:r + 1]
                
                if s[l] in counter:
                    check[s[l]] -= 1
                l += 1
                while l < len(s) and s[l] not in counter:
                    l += 1

            r += 1
        
        return res

                