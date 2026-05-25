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
            for i in range(k-1):
                if not node:
                    end.next = start
                    return sol.next
            node = node.next
            end = self.reverseGroup(end, start, k)
            start = node
        

    def reverseGroup(self, node_end, node_start, k):
        start = node_start
        for i in range(k-1):
            next_node = node_start
            node_start = node_start.next 
            node_start = next_node

        node_end.next = node_start
        return start