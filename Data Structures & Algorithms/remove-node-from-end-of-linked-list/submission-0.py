# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        N = 0

        while curr:
            N += 1
            curr = curr.next

        dummy = ListNode()
        dummy.next = head
        curr = dummy

        i = 0
        while curr:
            if i == (N-n):
                curr.next = curr.next.next
                break
            i += 1
            curr = curr.next

        return dummy.next