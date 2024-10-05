class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)  # Using defaultdict to avoid KeyError
        for node, target, weight in times:
            edges[node].append((weight, target))

        heap = [(0, k)]
        time = 0
        visited = set()
        while heap:
            cur_weight, cur_node = heapq.heappop(heap)

            if cur_node in visited:
                continue

            visited.add(cur_node)
            time = cur_weight
            for weight, node in edges[cur_node]:
                if not node in visited:
                    heapq.heappush(heap, (weight + time, node))
        
        return time if len(visited) == n else -1

