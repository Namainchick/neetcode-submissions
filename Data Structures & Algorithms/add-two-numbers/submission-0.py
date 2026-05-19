# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        over = 0 
        sol = ListNode(0,None)
        sol_head = sol
        while l1 and l2:
            sum = l1.val + l2.val + over
            if sum >= 10:
                sol.next = ListNode(sum - 10)
                over = 1
            else:
                over = 0
                sol.next = ListNode(sum)
            sol = sol.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            sum = l1.val + over
            if sum >= 10:
                sol.next = ListNode(sum - 10)
                over = 1
            else:
                over = 0
                sol.next = ListNode(sum)
            sol = sol.next
            l1 = l1.next


        while l2:
            sum = l2.val + over
            if sum >= 10:
                sol.next = ListNode(sum - 10)
                over = 1
            else:
                over = 0
                sol.next = ListNode(sum)
            sol = sol.next
            l2 = l2.next

        if over == 1:
            sol.next = ListNode(1)
        return sol_head.next
            
        