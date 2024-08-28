class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack = [0]
        res  = [0] * len(temperatures)

        for i in range(1, len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                res[stack[-1]] =  i - stack[-1]
                stack.pop()
            stack.append(i)
        
        return res