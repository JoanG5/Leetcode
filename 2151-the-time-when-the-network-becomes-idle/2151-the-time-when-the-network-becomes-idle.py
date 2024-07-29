class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        time_track = [float("inf")] * len(patience)
        time_track[0] = 0
        heap = []
        heappush(heap,(0,0))

        while heap:
            time, node = heappop(heap)
            for neighbor in graph[node]:
                if time + 1 < time_track[neighbor]:
                    heappush(heap,(time + 1, neighbor))
                    time_track[neighbor] = time + 1

        max_time_needed = 0
        for i in range(1, len(time_track)):
            
            time_needed = 2 * time_track[i]
            
            msgs_sent = ceil(time_needed / patience[i])
           
            total_time_needed = (patience[i]) * (msgs_sent-1) + time_needed
            max_time_needed = max(max_time_needed, total_time_needed)

        return max_time_needed + 1