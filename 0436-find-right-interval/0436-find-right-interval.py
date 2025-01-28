class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        for i in range(n):
            intervals[i] = (intervals[i], i)
        intervals.sort()

        res = [-1] * n

        for i in range(n):
            start, end, index = intervals[i][0][0], intervals[i][0][1], intervals[i][1]
            left, right = 0, n - 1

            while left <= right:
                mid = (left + right) // 2
                nStart = intervals[mid][0][0]
                if nStart < end:
                    left = mid + 1
                else:
                    right = mid - 1
 
            if left < n and intervals[left][0][0] >= end:
                res[index] = intervals[left][1]
        
        return res
