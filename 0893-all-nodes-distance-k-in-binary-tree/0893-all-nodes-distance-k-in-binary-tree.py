# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return []
            
        output = []
        parents = {}
        # Create a helper function to store parentNode in hashmap
        def helper(curr):
            if not curr:
                return 
            if curr.left:
                parents[curr.left] = curr
                helper(curr.left)
            if curr.right:
                parents[curr.right] = curr
                helper(curr.right)

        helper(root)
        seen = set()
        # Create a second helper function to traverse from target node to parent and child nodes and find nodes k away.

        def helper2(curr, dist):
            if not curr or curr in seen or dist > k:
                return
            seen.add(curr)
            if dist == k:
                output.append(curr.val)
                return 
            if curr in parents:
                helper2(parents[curr], dist + 1)
            helper2(curr.left, dist + 1)
            helper2(curr.right, dist + 1)

        helper2(target, 0)

        return output




        
        

