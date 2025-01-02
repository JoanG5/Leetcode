# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        def helper(root):
            if not root:
                return True
            
            left = helper(root.left)
            right = helper(root.right)

            if root.left and root.val <= root.left.val:
                return False
            if root.right and root.val >= root.right.val:
                return False
            
            return left and right 
        
        return helper(root)