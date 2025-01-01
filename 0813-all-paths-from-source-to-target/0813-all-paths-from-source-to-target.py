class Solution(object):
    def allPathsSourceTarget(self, graph):
        res = []
        n = len(graph)
        cycle = set()
        def dfs(i, cur):
            if i in cycle:
                return

            if i == n - 1:
                cur.append(i)
                res.append(cur)
                return

            cur.append(i)
            cycle.add(i)

            for neigh in graph[i]:
                dfs(neigh, cur[:])
            
            cycle.remove(i)
            
        dfs(0, [])
        return res
        