# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def helper(root):
            nonlocal target
            nonlocal k
            if root and k >= 0: 
                helper(root.left)
                k -= 1
                if k == 0:
                    target = root.val
                helper(root.right)
        target = 0 
        helper(root)
        return target 
        