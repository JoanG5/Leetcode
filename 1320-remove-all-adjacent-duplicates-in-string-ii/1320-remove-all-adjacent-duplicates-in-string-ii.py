class Solution(object):
    def removeDuplicates(self, s, k):
        stack = []
        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])
            
            if stack and stack[-1][1] == k:
                stack.pop()
        res = ""
        for c, num in stack:
            res += c * num

        return res        