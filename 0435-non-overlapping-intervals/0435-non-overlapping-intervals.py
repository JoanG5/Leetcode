class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        remove = 0
        cur = intervals[0][1]
        for i in range(len(intervals) - 1):
            if cur > intervals[i + 1][0]:
                remove += 1
                cur = min(intervals[i + 1][1], cur)
            else:
                cur = intervals[i + 1][1]
        return remove