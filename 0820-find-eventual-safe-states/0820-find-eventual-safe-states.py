class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for i in range(len(graph)):
            for j in graph[i]:
                adj[i].append(j)
        
        res = []
        visited = set()
        safe = set()
        def dfs(node):
            if node in visited:
                return False

            if node in safe:
                return True

            if adj[node] == []:
                return True 
        
            visited.add(node)
            for neigh in adj[node]:
                if not dfs(neigh):
                    visited.remove(node)
                    return False
            safe.add(node)
            visited.remove(node)
            return True

        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        return res

