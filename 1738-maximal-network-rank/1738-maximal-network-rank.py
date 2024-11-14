class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        degree = [0] * n
        connected = [[False] * n for _ in range(n)]
        res = 0
        for road in roads:
            cur, target = road
            degree[cur] += 1
            degree[target] += 1
            connected[cur][target] = True
            connected[target][cur] = True
        
        for i in range(n):
            for j in range(i + 1, n):
                cur_rank = degree[i] + degree[j]

                if connected[i][j]:
                    cur_rank -= 1
            
                res = max(res, cur_rank)
        
        return res
                
                