class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:        
        res = []
        safe = set()
        visited = set()

        def dfs(node):                
            if node in safe:
                safe.add(node)
                return True
            
            if node in visited:
                return False
            
            visited.add(node)
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            safe.add(node)
            visited.remove(node)
            return True 
        
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        
        return res 
        
