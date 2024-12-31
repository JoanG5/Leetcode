class Solution(object):
    def decodeString(self, s):
        temp = ""
        stack = []
        cur = 0
        for c in s:
            if c.isdigit():
                cur = cur * 10 + int(c)
            elif c == "[":
                stack.append((cur, temp))
                cur = 0
                temp = ''
            elif c == "]":
                num, newS = stack.pop()
                temp = newS + num * temp
            else:
                temp += c
        
        return temp

        