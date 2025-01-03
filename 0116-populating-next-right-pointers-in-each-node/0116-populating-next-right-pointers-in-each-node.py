"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        BFS
        Create queue
        - GO through the queue
        - For each value in the cur queue make the next the next value in the queue
        return root
        """
        if not root: return root
        queue = deque()
        queue.append([root])
        while queue:
            cur = queue.popleft()
            n = len(cur)
            level = []
            for i in range(n):
                if i + 1 < n:
                    cur[i].next = cur[i + 1]
                else:
                    cur[i].next = None
                
                if cur[i].left and cur[i].right:
                    level.append(cur[i].left)
                    level.append(cur[i].right)
            if level:
                queue.append(level)

            
        return root 
            

        