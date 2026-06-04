# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
so this kina looks like dp where you store the best possible but this doesnt work for paths. 
I remember a graph algotigh doing something similar to this but im not sure if this is the right this to do here.
Some thing like bfs but you have to color the nodes. 
Another Idea is just traverse and set the max sum for the node but also tell the neighbours. problem is with trees its hard to go back because its 
like a directed graph. 
The final idea is: a node gets its parent best then we check ok for the node do we store right path or de we store left path or do we store path left to 
right. If parent gives you <0 as best just skip the parent.
"""

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.best = float('-inf')
        def dfs(node):
            if node.left:
                left = max(0,dfs(node.left))
            if node.right:
                right = max(0,dfs(node.right))

            self.best = max(self.best,right+left+node.val)

            return node.val + max(left,right)

        return self.best
            
        dfs(root)

        return self.best

