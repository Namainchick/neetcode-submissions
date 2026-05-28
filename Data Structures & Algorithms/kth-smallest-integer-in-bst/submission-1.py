# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
brute force: easiest would be to sort the list and get kth smalles O(nlogn)
using bst: for each calc length and decide where to go
so go till node length is bigger than k but next one is also smaller then k 
ah this is dfs till we hit lowest and then the next kth node is the node we are searching 
"""

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.count = 0
        self.sol = None

        def find(node):
            if not node or self.sol is not None:
                return 

            find(node.left)

            self.count += 1

            if self.count == k:
                self.sol =  node.val
                return 

            find(node.right)
        find(root)
        return self.sol

"""
have to do this again got the right intuition but implementing that into recusive was a little hard but still doable 
"""