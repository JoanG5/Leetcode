class Solution:
    def reverseWords(self, s: str) -> str:
        start = end = len(s) - 1
        while end >= 0:
            cur = ""
            while end >= 0 and s[end] != " ":
                cur = s[end] + cur
                end -= 1
            s += cur + " "
            while end >= 0 and s[end] == " ":
                end -= 1
         
        while s[start + 1] == " ":
            start += 1
        return s[start + 1:-1]
            

