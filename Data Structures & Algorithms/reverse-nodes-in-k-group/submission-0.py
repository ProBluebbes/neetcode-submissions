# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        leadAnchor = leadHead = ListNode()
        groupHead = curr = head
        groupLen = 0

        while curr:
            groupLen += 1
            if groupLen == k:
                nextGroupHead = curr.next
                start = reverseKNodes(groupHead, k)
                leadHead.next = start
                leadHead = groupHead
                groupHead = nextGroupHead
                groupLen = 0
                curr = nextGroupHead
            else:
                curr = curr.next

        leadHead.next = groupHead
        return leadAnchor.next

def reverseKNodes(head, k):
    anchor = ListNode()
    curr = head
    for i in range(k):
        tmp = curr.next
        curr.next = anchor.next
        anchor.next = curr
        curr = tmp
    return anchor.next
