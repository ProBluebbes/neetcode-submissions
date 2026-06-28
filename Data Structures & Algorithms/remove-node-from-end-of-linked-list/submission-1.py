# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = potential = dummy = ListNode()
        dummy.next = head
        N = -1

        while curr:
            N += 1
            if N > n:
                potential = potential.next
            curr = curr.next

        potential.next = potential.next.next
        return dummy.next