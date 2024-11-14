class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        '''
        Go through k and see all nodes connected to it, save it to a set and visited
        Go through all nodes, besides k 
        - If node points to k then add all k neighbors to result 
        Add the neighbors of cur to the result
        return result
        '''
        adj = defaultdict(list)
        for start, end in invocations:
            adj[start].append(end)
        
        kPath = set()
        def dfs(i):
            if i in kPath:
                return
            kPath.add(i)
            for neighbor in adj[i]:
                dfs(neighbor)
        dfs(k)
        connected = False
        for u, v in invocations:
            if v in kPath and u not in kPath:
                connected = True
        
        if connected:
            res = [i for i in range(n)]
        else:
            res = [i for i in range(n) if i not in kPath]
        
        return res
               

        