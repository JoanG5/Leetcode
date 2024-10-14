class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        paths = {"N" : (0, 1), "S": (0, -1), "W": (-1, 0), "E": (1, 0)  }
        cur = (0, 0)
        for direc in path:
            if cur in visited: 
                return True

            visited.add(cur)
            cur = (cur[0] + paths[direc][0], cur[1] +paths[direc][1])
        return cur in visited