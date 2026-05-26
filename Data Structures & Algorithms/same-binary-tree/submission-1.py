# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and  not q:
            return True

        self.sol = True

        def compare(a,b):
            if not a and b:
                self.sol = False
                return 
            elif a and not b:
                self.sol = False
                return 
            elif not a and not b:
                return 
        
            if a.val != b.val:
                self.sol = False 

            compare(a.left,b.left)
            compare(a.right,b.right)
        compare(p,q)
        return self.sol



            
