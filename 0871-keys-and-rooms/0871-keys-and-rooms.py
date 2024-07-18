class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n

        def dfs(node):
            visited[node] = True
            for i in rooms[node]:
                if not visited[i]:
                    dfs(i)
        
        dfs(0)
        return len(visited) == visited.count(True)