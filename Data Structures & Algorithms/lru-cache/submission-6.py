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
            print(node.val)
            return node.val
        else:
            print(-1)
            return -1

    def put(self, key: int, value: int) -> None:
        if self.length == self.capacity:
            node = self.head.next
            temp = self.head.next.next
            self.head.next = temp
            temp.prev = self.head
            del self.hashmap[node.key]
        else:
            self.length += 1

        self.tail.next = Node(value, None, self.tail, key)
        self.hashmap[key] = self.tail.next
        self.tail = self.tail.next
