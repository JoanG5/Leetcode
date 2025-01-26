class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        stack = [intervals[0]]

        for start, end in intervals[1::]:
            oStart, oEnd = stack[-1]
            if start <= oEnd:
                stack[-1][1] = max(oEnd, end)
            else:
                stack.append([start, end])
        
        return stack 
