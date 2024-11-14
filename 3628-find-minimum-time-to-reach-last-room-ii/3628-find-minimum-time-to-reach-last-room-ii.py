class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        rows, cols = len(moveTime), len(moveTime[0])
        heap = [(0, 0, 0, 1)]
        visited = set()
        
        while heap:
            time, r, c, step = heapq.heappop(heap)
 
            if (r, c, step) in visited:
                continue
            
            if r == rows - 1 and c == cols - 1:
                return time
            
            visited.add((r, c, step))
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols:
                    if time < moveTime[nr][nc]:
                        newTime = step + moveTime[nr][nc]
                    else:
                        newTime = step + time
                    new_step = 2 if step == 1 else 1
                    heapq.heappush(heap, (newTime, nr, nc, new_step))
                    