# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        [0, 1, 2, 3, 4, 5, 6]

        [0, 6, 1, 5, 2, 4, 3] 

        this should just be 2 pointers once we turned linked list into list
        """

        array = {}

        node = head
        index = 0
        turn = True
        dummy = ListNode()

        while node:
            array[index] = node
            index += 1
            node = node.next

        print(array)

        l, r = 0, len(array) - 1
        print(l,r)

        while l <= r:
            if turn:
                dummy.next = array[l]
                l += 1
            else:
                dummy.next = array[r]
                r -= 1

            dummy = dummy.next
            turn = not turn 

        dummy.next = None
        








