# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0 
        def helper(root, counter):
            if not root.left and not root.right:
                return counter

            if root.left and root.right:
                return min(helper(root.left, counter + 1), helper(root.right, counter + 1)) 
            elif root.left:
                return helper(root.left, counter + 1)
            else:
                return helper(root.right, counter + 1)

        return helper(root, 1)