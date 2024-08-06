class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def helper(open, closed):
            if open == n and closed == n:
                res.append("".join(stack))
                return
            
            if open < n:
                stack.append("(")
                helper(open + 1, closed)
                stack.pop()
            
            if closed < open:
                stack.append(")")
                helper(open, closed + 1)
                stack.pop()
            
        helper(0, 0)
        return res


