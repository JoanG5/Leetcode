class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {c: [] for c in range(numCourses)}
        for cor, pre in prerequisites:
            adj[pre].append(cor)
        
        def dfs(cor):
            if cor not in prereqMap:
                prereqMap[cor] = set()
                for prereq in adj[cor]:
                    prereqs = dfs(prereq)
                    for p in prereqs:
                        prereqMap[cor].add(p)
                prereqMap[cor].add(cor)
            return prereqMap[cor]
        
        prereqMap = {}
        for cor in range(numCourses):
            dfs(cor)
        
        res = []
        for u, v in queries:
            res.append(u in prereqMap[v])
        return res