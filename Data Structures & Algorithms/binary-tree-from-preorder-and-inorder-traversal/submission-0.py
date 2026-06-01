# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preoder[0])
        mid = inorder.index(preoder[0])
        root.left = self.buildTree(preoder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preoder[mid+1:], inorder[mid+1:])