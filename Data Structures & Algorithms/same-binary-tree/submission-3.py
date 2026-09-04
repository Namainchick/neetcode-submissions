# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def compare(a,b):
            if not b and not a:
                return True
            if not b or not a:
                return False
            if a.val != b.val:
                return False

            return (compare(a.right,b.right) and compare(a.left,b.left))

        return compare(p,q)

            
            
            

            
            