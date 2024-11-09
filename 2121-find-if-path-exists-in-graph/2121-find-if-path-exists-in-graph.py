class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = {c: [] for c in range(n)}
        seen = set()
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        
        def dfs(i):
            seen.add(i)
            if i == destination: 
                return True 
            
            for neigh in adj[i]:
                if not neigh in seen: 
                    if dfs(neigh):
                        return True
            
            return False
        
        return dfs(source)
           