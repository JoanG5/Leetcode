class Solution:
    def reverseWords(self, s: str) -> str:
        s_words = s.split()
        res = ""
        for w in s_words[::-1]:
            res += w + " "
        
        return res[:-1]
