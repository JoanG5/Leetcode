# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}
        queue = deque()
        queue.append(root)

        # Create connection with parents for each node
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if target == node:
                    targetNode = node
                if node.left:
                    parent[node.left] = node
                    queue.append(node.left)
                if node.right:
                    parent[node.right] = node
                    queue.append(node.right)

        seen = {}
        queue.append(targetNode)
        level = 0

        while queue:
            if level == k:
                return [node.val for node in queue]
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                seen[node] = True
                if node.left and not (node.left in seen):
                    queue.append(node.left)
                if node.right and not (node.right in seen):
                    queue.append(node.right)
                if node in parent and not (parent[node] in seen):
                    queue.append(parent[node])
            level += 1
        return []




        
        

