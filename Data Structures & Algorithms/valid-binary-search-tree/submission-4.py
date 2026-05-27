# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True 

        self.sol = True

        def search(node,small,big):
            if not node:
                return 

            if node.val <= small or node.val >= big:
                self.sol = False

            search(node.left, small, node.val)
            search(node.right, node.val, big)

        search(root, float('-inf'), float('inf'))

        return self.sol