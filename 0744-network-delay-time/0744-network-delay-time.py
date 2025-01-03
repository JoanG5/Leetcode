class Solution(object):
    def networkDelayTime(self, times, n, k):
        adj = defaultdict(list)
        for start, end, time in times:
            adj[start].append((time, end))
        
        heap = [(0, k)]
        res = 0
        seen = set()
        while heap:
            time, cur = heapq.heappop(heap)
            if cur in seen:
                continue
            seen.add(cur)
            res = time
            for nTime, end in adj[cur]:
                if end not in seen:
                    heapq.heappush(heap, (time + nTime, end))

        return res if len(seen) == n else -1

        