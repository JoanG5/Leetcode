class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for node, target, weight in times:
            edges[node].append((weight, target))
        
        visited = set()
        time = 0
        heap = [(0, k)]
        while heap:
            cur_weight, cur_node = heapq.heappop(heap)

            if cur_node in visited:
                continue

            visited.add(cur_node)
            time = cur_weight
            for weight, node in edges[cur_node]:
                heapq.heappush(heap, (time + weight, node))
        
        return time if len(visited) == n else -1