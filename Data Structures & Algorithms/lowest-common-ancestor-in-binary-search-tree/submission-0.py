# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        big = max(p.val,q.val)
        small = min(p.val,q.val)

        while True:
            if root.val <= big and root.val >= small:
                return root
            elif root.val > small:
                root = root.left
            else:
                root = root.right