class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals)
        remove = 0
        cur = sorted_intervals[0][1]
        for i in range(len(sorted_intervals) - 1):
            if cur > sorted_intervals[i + 1][0]:
                remove += 1
                cur = min(sorted_intervals[i + 1][1], cur)
            else:
                cur = sorted_intervals[i + 1][1]
        return remove