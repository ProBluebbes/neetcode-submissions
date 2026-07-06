# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        anchor = head = ListNode()
        k = len(lists)
        while True:
            minimum = None
            minIndex = None
            for i in range(k):
                if lists[i] and (minimum is None or lists[i].val < minimum):
                    minimum = lists[i].val
                    minIndex = i
            
            if minimum is None:
                break

            head.next = lists[minIndex]
            lists[minIndex] = lists[minIndex].next
            head = head.next
            head.next = None
        
        return anchor.next

        
