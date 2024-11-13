class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red, blue = defaultdict(list), defaultdict(list)
        for node, target in redEdges:
            red[node].append(target)
        for node, target in blueEdges:
            blue[node].append(target)

        queue = deque()
        queue.append([0, 0, None])
        res = [-1] * n
        visited = set()
        visited.add((0, None))
        while queue:
            curNode, length, color = queue.popleft()    

            if res[curNode] == -1:
                res[curNode] = length
            
            if color != "RED":
                for neigh in red[curNode]:
                    if (neigh, "RED") not in visited:
                        visited.add((neigh, "RED"))
                        queue.append([neigh, length + 1, "RED"])
            if color != "BLUE":
                for neigh in blue[curNode]:
                    if (neigh, "BLUE") not in visited:
                        visited.add((neigh, "BLUE"))
                        queue.append([neigh, length + 1, "BLUE"])
        
        return res
            
