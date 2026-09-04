# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        lets try dfs
        """

        queue = [(p,q)]

        while queue:
            a,b = queue.pop()

            if not a and not b:
                continue
            if not a or not b or a.val != b.val:
                return False

            queue.append((a.right,b.right))
            queue.append((a.left,b.left))

        return True
