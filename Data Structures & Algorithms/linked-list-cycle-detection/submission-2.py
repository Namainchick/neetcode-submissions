# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow,fast = head,head

        if not slow and not fast:
            return False

        while slow and fast:

            slow = slow.next
            fast = fast.next
            
            if fast is None:
                return False

            fast = fast.next

            if slow == fast:
                return True

        return False

#got it in 3 min lets see if i can do it more efficient 