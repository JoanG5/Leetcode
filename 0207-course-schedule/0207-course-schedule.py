class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = { c: [] for c in range(numCourses)}
        for cor, pre in prerequisites:
            adj[cor].append(pre)
        
        visited = set()
        def dfs(n):
            if n in visited:
                return False
            if adj[n] == []:
                return True 
            
            visited.add(n)
            for neigh in adj[n]:
                if not dfs(neigh):
                    return False
            
            visited.remove(n)
            adj[n] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True 
            
