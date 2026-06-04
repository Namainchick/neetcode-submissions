# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node is None:
                result.append("null")
            else:
                result.append(str(node.val))
                queue.append(node.left)   # append even if None
                queue.append(node.right)  # so nulls are recorded

        return ",".join(result)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        tokens = iter(data.split(","))
        it = iter(tokens)
        node = TreeNode(int(next(tokens)))
        root = node
        
        queue = deque([node])

        while queue:
            node = queue.popleft()

            left = next(tokens)
            if left != "null":
                node.left = TreeNode(int(left))
                queue.append(node.left)
            
            right = next(tokens)
            if right != "null":
                node.right = TreeNode(int(right))
                queue.append(node.right)

        return root 
            

"""
was pretty doable only iter and data split was new please redo 
"""
            


