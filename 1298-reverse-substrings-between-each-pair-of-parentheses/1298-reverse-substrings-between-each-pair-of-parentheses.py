class Solution(object):
    def reverseParentheses(self, s):
        def reverse(l, r):
            while l < r:
                while l < r and s[l] in ["(", ")"]:
                    l += 1
                while l < r and s[r] in ["(", ")"]:
                    r -= 1
                if l < r:
                    s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        s = list(s)
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                start = stack.pop()
                reverse(start, i)
        res = []
        for letter in s:
            if not letter in ["(", ")"]:
                res.append(letter)

        return "".join(res)

            
        