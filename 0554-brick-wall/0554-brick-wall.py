class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        hash = {}

        for row in wall:
            edge = 0
            for width in row[:-1]:
                edge += width
                hash[edge] = hash.get(edge,0) + 1
        
        return len(wall) - max(hash.values(), default = 0)