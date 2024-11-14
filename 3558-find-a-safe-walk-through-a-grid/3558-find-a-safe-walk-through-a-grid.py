class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        rows, cols = len(grid), len(grid[0])
        paths = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        health = health - 1 if grid[0][0] == 1 else health
        
        queue = deque()
        queue.append((0, 0, health))
        
        visited = set()
        visited.add((0, 0, health))

        while queue:
            r, c, cur_health = queue.popleft()

            if cur_health == 0:
                continue

            if r == rows - 1 and c == cols - 1 and cur_health > 0:
                return True

            for dr, dc in paths:
                nr, nc = r + dr, c + dc 
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc, cur_health - grid[nr][nc]) not in visited:
                    nh = cur_health - grid[nr][nc]
                    queue.append((nr, nc, nh))
                    visited.add((nr, nc, nh))
        
        return False 

            

