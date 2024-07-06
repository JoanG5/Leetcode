# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}

        def build(left, right):
            if left > right:
                return [None]
            if (left, right) in memo:
                return memo[(left, right)]
            res = []

            for val in range(left, right + 1):
                for leftTree in build(left, val - 1):
                    for rightTree in build(val + 1, right):
                        root = TreeNode(val, leftTree, rightTree)
                        res.append(root)
            memo[(left, right)] = res
            return res
        
        return build(1, n)

