class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        rows, cols = len(moveTime), len(moveTime[0])
        heap = [(0, 0, 0)]
        visited = set()

        while heap:
            time, r, c = heapq.heappop(heap)

            if (r, c) in visited:
                continue

            if r == rows - 1 and c == cols - 1:
                return time

            visited.add((r, c))
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols:
                    if time < moveTime[nr][nc]:
                        newTime = moveTime[nr][nc] + 1
                    else:
                        newTime = time + 1
                    heapq.heappush(heap, (newTime, nr, nc))

