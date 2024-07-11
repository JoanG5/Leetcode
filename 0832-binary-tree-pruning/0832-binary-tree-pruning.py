# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def helper(root):                                                                                               
            if root:
                root.left = helper(root.left)
                root.right = helper(root.right)

                if not root.right and not root.left and root.val == 0:
                    return None
                return root
            return None
        return helper(root)
         
