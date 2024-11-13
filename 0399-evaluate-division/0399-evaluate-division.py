class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        hashmap = defaultdict(dict)
        res = []
        for (x, y), value in zip(equations, values):
            adj[x].append(y)
            adj[y].append(x)
            hashmap[x][y] = value
            hashmap[y][x] = 1.0 / value

        def dfs(i, j, cur, visited):
            if not i in hashmap or j not in hashmap:
                return -1.0
            if i == j:
                return cur

            visited.add(i)
            for neigh in adj[i]:
                if not neigh in visited:
                    result = dfs(neigh, j, cur * hashmap[i][neigh], visited)
                    if result != -1.0:
                        return result
            visited.remove(i)
            return -1.0

        for s, f in queries: 
            res.append(dfs(s, f, 1.0, set()))
        
        return res