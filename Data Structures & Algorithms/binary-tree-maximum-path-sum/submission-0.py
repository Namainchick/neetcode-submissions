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
        self.best = 0
        def dfs(node, best):
            left,right,mid = 0,0,0
            if node.left:
                left = max(best,best+node.left.val)
            if node.right:
                right = max(best,best + node.right.val)
            if node.right and node.left:
                mid = max(best,node.val + node.left.val + node.right.val)
            best = max(left,right,mid)
            self.best = max(self.best,best)
            if node.left:
                dfs(node.left,best)
            if node.right:
                dfs(node.right,best)

        dfs(root, root.val)

        return self.best
            

