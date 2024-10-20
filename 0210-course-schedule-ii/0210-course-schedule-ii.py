class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = { c: [] for c in range(numCourses)}
        for cor, pre in prerequisites:
            adj[cor].append(pre)

        res = []
        visited = set()
        completed = set()
        def dfs(n):
            if n in completed:
                return True
            if n in visited:
                return False
            
            visited.add(n)
            for neigh in adj[n]:
                if not dfs(neigh):
                    return False
            res.append(n)
            visited.remove(n)
            completed.add(n)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res



 