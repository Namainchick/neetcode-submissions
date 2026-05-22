class Node:

    def __init__(self, val, next, prev, key):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.hashmap = {}
        self.head = Node(0,None,None,0)
        self.tail = self.head

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            if node.next:
                node.prev.next = node.next
                node.next.prev = node.prev
                node.next = None
                node.prev = self.tail
                self.tail.next = node
                self.tail = self.tail.next
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value 
            if node.next:
                node.prev.next = node.next
                node.next.prev = node.prev
                node.next = None
                node.prev = self.tail
                self.tail.next = node
                self.tail = self.tail.next
            return 

        if self.length == self.capacity:
            node = self.head.next
            self.head.next = node.next
            if node.next:
                node.next.prev = self.head
            else:
                self.tail = self.head  # ← Liste ist jetzt leer
            del self.hashmap[node.key]
        else:
            self.length += 1

        self.tail.next = Node(value, None, self.tail, key)
        self.hashmap[key] = self.tail.next
        self.tail = self.tail.next

#bomboclaat