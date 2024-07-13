# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def helper(root, s):
            s += str(root.val)
        
            if not root.left and not root.right:
                res.append(s)
            else:
                s += "->"
            
            if root.left:
                helper(root.left, s)
            if root.right:
                helper(root.right, s)

        res = []
        if root:
            helper(root, "")
        return res
        
            