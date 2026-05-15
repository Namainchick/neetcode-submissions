# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        before = None
        while node is not None: 
            temp = node.next 
            if before is None:
                node.next = None
            else:
                node.next = before
            before = node
            node = temp
  

        return before

            