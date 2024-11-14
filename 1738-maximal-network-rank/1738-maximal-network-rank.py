class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for start, target in roads:
            adj[start].append(target)
            adj[target].append(start)

        res = 0

        for i in range(n):
            for j in range(i + 1, n):
                diff = 0
                for neigh in adj[j]:
                    if neigh == i:
                        diff += 1
                res = max(res, len(adj[i]) + len(adj[j]) - diff)
        
        return res
                
                