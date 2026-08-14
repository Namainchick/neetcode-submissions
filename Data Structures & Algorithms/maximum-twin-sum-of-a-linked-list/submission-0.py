# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        best = 0
        node = head
        index = 0
        hashmap = {}


        while node:
            hashmap[index] = node
            node = node.next
            index += 1

        n = len(hashmap)
        print(hashmap)

        for i in range(n//2):
            best = max(best,hashmap[i].val+hashmap[n-1-i].val)
            print(hashmap[i].val,hashmap[n-1-i].val)

        return best

