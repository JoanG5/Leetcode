# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(root, left):
            if not root:
                return 0
            if not root.left and not root.right:
                if left:
                    return root.val
                else:
                    return 0
            
            left = dfs(root.left, True)
            right = dfs(root.right, False)

            return left + right
    
        return dfs(root, False)