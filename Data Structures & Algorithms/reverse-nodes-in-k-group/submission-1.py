# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        sol = ListNode()
        start = head
        end = sol
        node = head
        while True:
            for i in range(k):
                if not node:
                    end.next = start
                    return sol.next
                node = node.next
            end = self.reverseGroup(end, start, k)
            start = node
        

    def reverseGroup(self, node_end, node_start, k):
        start = node_start
        prev = None
        for i in range(k):
            next = node_start.next
            node_start.next = prev
            prev = node_start
            node_start = next

        node_end.next = prev
        return start