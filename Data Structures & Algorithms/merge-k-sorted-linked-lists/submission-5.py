# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        we can use a heap to track the current smallest. 
        If the heap is empy we pop from all lists. 
        now we now head of heap is the smallest. If we also store from which lists it 
        came from we can pop from heap and put the node in again. Because we know that 
        heap will then allway carry the smallest because they are sorted themself and 
        there smallest is already in the heap by the first insertion. If a list is empty
        just keep on doing the rest. 

        For runtime we will have to do number of iteams * log number of lists

        the loop could be while heap is not empty
        """
        node = ListNode()
        dummy = node
        heap = []

        for i in range(len(lists)):
            if lists[i] is not None:
                heapq.heappush(heap,(lists[i].val,i))

        while heap:
            val,i = heapq.heappop(heap)

            node.next = lists[i]
            lists[i] = lists[i].next
            node = node.next
            node.next = None

            if lists[i] != None:
                heapq.heappush(heap,(lists[i].val,i))

        return dummy.next


    

