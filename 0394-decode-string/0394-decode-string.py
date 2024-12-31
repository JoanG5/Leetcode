class Solution(object):
    def decodeString(self, s):
        stack = []
        t = ""
        cur = 0

        for c in s:
            if c.isdigit():
                cur = cur * 10 + int(c)
            elif c == "[":
                stack.append((cur, t))
                t = ''
                cur = 0    
            elif c == "]":
                num, nt = stack.pop()
                t = nt + num * t
            else:
                t += c
        return t