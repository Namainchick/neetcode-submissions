"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
"""
brute forece:
the problem is how we know in the copy list which pointer to point to for the 
random pointer. Maybe safe node with their indeces in a hashmap. this will take n^2
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node = head
        nodemap = {}
        copy = Node(0)
        copy_head = copy

        while node:
            temp = Node(node.val)
            copy.next = temp
            nodemap[node] = temp
            copy = copy.next
            node = node.next

        node = head
        copy = copy_head

        for i in range(len(nodemap)):
            if node.random is None:
                pass
            else:
                copy.next.random = nodemap[node.random]
            node = node.next
            copy = copy.next

        return copy_head.next

# better approach but same runtime. Using only one map from original to copy. But s
# same approach