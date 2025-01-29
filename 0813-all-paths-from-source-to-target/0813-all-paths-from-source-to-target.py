class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(graph)
        visted = set()

        def dfs(i, cur):
            cur.append(i)
            if i == n - 1:
                res.append(cur[:])
                return
            
            for neigh in graph[i]:
                dfs(neigh, cur)
                cur.pop()
                
        
        dfs(0, [])
    
        return res