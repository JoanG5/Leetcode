class Solution(object):
    def decodeString(self, s):
        cur = 0
        t = ""
        stack = []

        for c in s:
            if c.isdigit():
                cur = cur * 10 + int(c)
            elif c == "[":
                stack.append((cur, t))
                t = ""
                cur = 0
            elif c == "]":
                num, last = stack.pop()
                t = last + num * t
            else:
                t += c
        
        return t
        