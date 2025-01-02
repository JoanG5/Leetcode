# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        def helper(root, max, min):
            if not root:
                return True
            
            if root.val >= max or root.val <= min: return False

            return helper(root.right, max, root.val) and helper(root.left, root.val, min) 
        
        return helper(root, float('inf'), -float('inf'))
