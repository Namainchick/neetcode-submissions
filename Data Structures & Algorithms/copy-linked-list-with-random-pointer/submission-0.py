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
        indexmap = {}
        index = 0
        copy = Node(0)
        copy_head = copy

        while node:
            nodemap[node] = index
            indexmap[index] = node
            index += 1
            node = node.next

        node = head
        copymap = {}

        for i in range(len(nodemap)):
            copy.next = Node(indexmap[i].val)
            copymap[i] = copy.next
            copy = copy.next

        copy = copy_head
        next = None

        for i in range(len(nodemap)):
            if not node.random:
                copy.next.random = None
            else:
                next = nodemap[node.random]
                copy.next.random = copymap[next]
            node = node.next
            copy = copy.next

        return copy_head.next
