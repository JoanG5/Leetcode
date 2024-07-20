class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = { c:[] for c in range(numCourses)}
        for cor, pre in prerequisites:
            prereq[cor].append(pre)
        
        output = []
        visit, cycle = set(), set()
        def dfs(cor):
            if cor in cycle: return False
            if cor in visit: return True

            cycle.add(cor)
            for pre in prereq[cor]:
                if not dfs(pre):
                    return False
            cycle.remove(cor)
            visit.add(cor)
            output.append(cor)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return output