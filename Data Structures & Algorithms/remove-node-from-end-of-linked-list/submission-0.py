# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# first approach would be brute forece storing all nodes    
# with their indeces in map for example. Then going to that 
# node and delete it O(n). Cant get better than that i guess 
# i see hashap isnt even needed jsut getting the length is all we need


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        node = head
        #calc length
        while node:
            length += 1
            node = node.next
        #get index in list
    
        dummy = ListNode(0, head)
        node = dummy
        
        #go to node before
        for i in range(length-n):
            node = node.next 

        node.next = node.next.next

        return dummy.next