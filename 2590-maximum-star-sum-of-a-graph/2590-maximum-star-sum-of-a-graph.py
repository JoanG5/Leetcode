class Solution(object):
    def maxStarSum(self, vals, edges, k):
        '''
        - Star: a node and all its neighbor nodes
        - - Sort the nodes based on their vals
        - - Get the top k elements added to res
        - return res

        - Create adj list a lil diff tho
        - - Make the edges a heap instead of a list 
        -- Get top k elements and add it to res, swap if larger
        - return res
        '''

        adj = defaultdict(list)
        for start, end in edges:
            heapq.heappush(adj[start], -vals[end])
            heapq.heappush(adj[end], -vals[start])

        res = max(vals)
        for key, arr in adj.items():
            cur = 0
            n = min(k, len(arr))
            cur += vals[key]
            for i in range(n):
                cur += -heapq.heappop(arr)
                res = max(res, cur)
        
        return res

        