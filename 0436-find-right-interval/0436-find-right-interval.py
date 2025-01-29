class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        for i in range(n):
            intervals[i] = (intervals[i], i)
        intervals.sort()
        res = [-1] * n

        for interval, i in intervals:
            start, end = interval
            left, right = 0, n - 1

            while left <= right:
                mid = (left + right) // 2

                if intervals[mid][0][0] < end:
                    left = mid + 1
                else:
                    right = mid - 1
            
            if left < n and intervals[left][0][0] >= end:
                res[i] = intervals[left][1]
        
        return res
        