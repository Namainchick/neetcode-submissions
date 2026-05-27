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

        def search(node,small,big,isLeft):
            if not node:
                return 
            if isLeft:  
                if node.val >= small:
                    self.sol = False
                else:
                    small = node.val  
            else:
                if node.val <= big:
                    self.sol = False
                else:
                    big = node.val

            search(node.left,small,big,True)
            search(node.right,small,big,False)

        search(root.left,root.val,root.val,True)
        search(root.right,root.val,root.val,False)

        return self.sol