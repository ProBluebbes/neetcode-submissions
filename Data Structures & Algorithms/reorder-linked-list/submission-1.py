# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1 2 3 4 5 6 7 8

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        # find half way point middle inclusive
        while True:
            if not fast.next or not fast.next.next:
                break
            slow = slow.next
            fast = fast.next.next
        
        # reverse second half and split into two
        curr = slow.next
        slow.next = None
        anchor = ListNode()

        while curr:
            tmp = curr.next
            curr.next = anchor.next
            anchor.next = curr
            curr = tmp

        # alternate order
        lcurr = head
        rcurr = anchor.next

        while rcurr:
            ltmp = lcurr.next
            rtmp = rcurr.next

            rcurr.next = lcurr.next
            lcurr.next = rcurr

            lcurr = ltmp
            rcurr = rtmp