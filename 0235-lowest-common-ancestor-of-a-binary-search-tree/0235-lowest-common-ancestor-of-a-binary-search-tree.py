# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None

        def helper(root):
            nonlocal res
            if not root: return False
            left = helper(root.left)
            right = helper(root.right)

            mid = root == p or root == q

            if (left and right) or (mid and left) or (mid and right):
                res = root
                
            return mid or left or right
    
        helper(root)
        return res