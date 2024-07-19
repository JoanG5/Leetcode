# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(root, tot):
            if not root:
                return False

            tot += root.val
            
            if not root.left and not root.right:
                return tot == targetSum

            return helper(root.left, tot) or helper(root.right, tot)
        
        return helper(root, 0)
            
