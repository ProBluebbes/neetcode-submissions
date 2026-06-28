# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1 2 3 4 5 6 7 8 9

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        # find half way point middle inclusive
        while True:
            if not fast.next or not fast.next.next:
                break
            slow = slow.next
            fast = fast.next.next
        
        # reverse second half and split into two
        curr = slow.next
        prev = slow.next = None

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # alternate order
        lcurr = head
        rcurr = prev

        while rcurr:
            ltmp, rtmp= lcurr.next, rcurr.next

            rcurr.next = lcurr.next
            lcurr.next = rcurr

            lcurr, rcurr = ltmp, rtmp