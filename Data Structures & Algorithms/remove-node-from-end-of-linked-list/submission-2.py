# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        index = 1
        hashmap = {}

        node = head
        while node:
            hashmap[index] = node
            node = node.next
            index += 1

        l = len(hashmap)

        if l - n == 0:          
            return head.next
        
        temp = hashmap.get(l-n+2)
        hashmap[l-n].next = temp
        return head