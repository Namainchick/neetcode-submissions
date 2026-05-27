# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.counter = 0

        def count(node,highest):
            if not node:
                return 

            if node.val >= highest:
                self.counter += 1

            highest = max(node.val, highest)
            
            count(node.left, highest)
            count(node.right, highest)

        count(root,-1)

        return self.counter