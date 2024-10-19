class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = { c: [] for c in range(numCourses)}
        for req in prerequisites:
            adj[req[0]].append(req[1])
        
        cycle = set()

        def dfs(n):
            if n in cycle:
                return False
            if adj[n] == []:
                return True
            
            cycle.add(n)
            for neighbor in adj[n]:
                if not dfs(neighbor):
                    return False
            cycle.remove(n)
            adj[n] = []
            return True

        for n in range(numCourses):
            if not dfs(n):
                return False
        return True
