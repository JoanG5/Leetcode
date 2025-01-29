class Solution:
    def decodeString(self, s: str) -> str:
        cur = 0
        stack = []
        res = ""

        for c in s:
            if c.isdigit():
                cur = cur * 10 + int(c)
            elif c == '[':
                stack.append((cur, res))
                res = ''
                cur = 0
            elif c == ']':
                num, curS = stack.pop()
                res = curS + res * num 
            else:
                res += c

        return res

