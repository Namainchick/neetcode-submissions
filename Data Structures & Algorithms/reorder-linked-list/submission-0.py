# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# brute force:
# die eingabe liste immer im wechsel vorne und hinten entfernen und dann 
# in eine ausgabe liste packen. den letzten zu kriegen kostet aber O(n) was das ganze 
# in O(n^2) verwandelt
# wir können es mit einer while loop machen und dann immer turn basiert oder einfach 
# die länge nehmen und dann durch iterieren. Das macht cases und turn einfacher

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        result = ListNode(0,None)
        dummy = ListNode(0,None)
        dummy.next = head

        beore = None
        length = 0

        node = head
        while node:
            length += 1
            node = node.next

        result_head = result

        for i in range(length):
            if i % 2 == 0:
                temp = dummy.next.next 
                dummy.next.next = None
                result.next = dummy.next
                dummy.next = temp 
                result = result.next

            else:
                temp = dummy
                while dummy.next:
                    before = dummy 
                    dummy = dummy.next
                result.next  = dummy
                before.next = None
                dummy = temp
                result = result.next

        head = result_head.next
        






        

