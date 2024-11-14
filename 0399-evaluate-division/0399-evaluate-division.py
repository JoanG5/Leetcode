class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i in range(len(equations)):
            start, end = equations[i][0], equations[i][1]
            adj[start].append((end, values[i]))
            adj[end].append((start, 1.0/values[i]))

        def dfs(i, end, val):
            if i not in adj or end not in adj:
                return -1.0
            
            if i == end:
                return val

            if i in visited:
                return -1.0

            visited.add(i)
            for neighbor, div in adj[i]:
                if not neighbor in visited:
                    result = dfs(neighbor, end, val * div)
                    if result != -1.0:
                        return result      

            visited.remove(i)
            return -1.0

        res = []
        for x, y in queries:
            visited = set()
            res.append(dfs(x, y, 1.0))
        
        return res