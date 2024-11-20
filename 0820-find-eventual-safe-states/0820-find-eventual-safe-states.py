class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:        
        res = []
        visited = set()
        safe = set()
        def dfs(node):
            if node in visited:
                return False

            if node in safe:
                return True
        
            visited.add(node)
            for neigh in graph[node]:
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

