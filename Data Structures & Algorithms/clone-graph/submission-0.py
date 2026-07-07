"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        hashmap = {}
        q = deque([node])
        hashmap[node] = Node(node.val)

        while q:
            n = q.popleft()
            for neighbor in n.neighbors:
                if neighbor not in hashmap:
                    hashmap[neighbor] = Node(neighbor.val)
                    q.append(neighbor)

        for original, clone in hashmap.items():
            for neighbor in original.neighbors:
                clone.neighbors.append(hashmap[neighbor])

        return hashmap[node]
