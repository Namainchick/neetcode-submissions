# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        self.sol = True
    
        def balance(curr):
            if not curr:
                return 0

            
            
            left = balance(curr.left)
            right = balance(curr.right)

            if abs(left-right) > 1:
                self.sol = False

            return 1 + max(left,right)

        balance(root)

        return self.sol
"""
pretty easy
"""
