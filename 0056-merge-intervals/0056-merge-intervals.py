class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        stack = [intervals[0]]

        for start, end in intervals[1::]:
            prevStart, prevEnd = stack[-1]
            if prevEnd >= start:
                stack.pop()
                if prevEnd > end:
                    stack.append([prevStart, prevEnd])
                else:
                    stack.append([prevStart, end])
            else:
                stack.append([start, end])
        
        return stack



        