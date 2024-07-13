class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = 0
        n = len(isConnected)
        visited = [False] * n

        def dfs(node):
            visited[node] = True
            for i in range(n):
                if isConnected[node][i] == 1 and not visited[i]:
                    dfs(i)
        
        for i in range(n):
            if not visited[i]:
                dfs(i)
                res += 1

        return res