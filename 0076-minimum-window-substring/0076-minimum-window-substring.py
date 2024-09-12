class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or s == t == "":
            return ""

        counter = {}
        window_check = {}
        for l in t:
            counter[l] = 1 + counter.get(l, 0)
            window_check[l] = 0
        
        l = r = 0
        for i in range(len(s)):
            if s[i] in counter: 
                l = r = i 
                break 
        
        res = ""
        match = 0

        while r < len(s):
            if s[r] in counter:
                window_check[s[r]] += 1
                if window_check[s[r]] == counter[s[r]]: match += 1
            
            while match == len(counter):
                if len(res) > r - l + 1 or res == "":
                    res = s[l:r + 1]

                if s[l] in window_check:
                    window_check[s[l]] -= 1
                    if window_check[s[l]] < counter[s[l]]:
                        match -= 1

                l += 1
                while l < len(s) and s[l] not in counter:
                    l += 1
            r += 1
        
        return res
                

                