class Solution(object):
    def decodeString(self, s):
        stack = []
        temp = ''
        cur = 0
        for c in s:
            if c.isdigit():
                cur = cur * 10 + int(c)
            elif c == "[":
                stack.append((cur, temp))
                cur = 0
                temp = ''
            elif c == "]":
                num, prev_s = stack.pop()
                temp = prev_s + num * temp
            else:
                temp = temp + c
        
        return temp