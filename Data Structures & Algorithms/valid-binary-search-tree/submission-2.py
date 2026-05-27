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

        def search(node,val,isLeft):
            if not node:
                return 
            if isLeft:  
                if node.val >= val:
                    self.sol = False  
            else:
                if node.val <= val:
                    self.sol = False
            search(node.left,val,True)
            search(node.right,val,False)

        search(root.left,root.val,True)
        search(root.right,root.val,False)

        return self.sol