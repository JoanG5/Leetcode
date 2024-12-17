class Solution(object):
    def maximumImportance(self, n, roads):
        '''
        - Create adj
        - Sort by num of neighbors
        - Give numbers in decreasing order 
        - Add to result
        '''
        adj = defaultdict(list)
        for start, end in roads:
            adj[start].append(end)
            adj[end].append(start)
        
        sorted_nodes = sorted(adj.keys(), key=lambda k: len(adj[k]), reverse=True)
        importance = {}
        order = n
        for i in range(len(sorted_nodes)):
            importance[sorted_nodes[i]] = order
            order -= 1

        res = 0
        for start, end in roads:
            res += importance[start] + importance[end]
        
        return res