# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = 0
        sum1 = 0
        curr1 = l1
        while curr1:
            sum1 += curr1.val * (10**n1)
            curr1 = curr1.next
            n1 += 1

        n2 = 0
        sum2 = 0
        curr2 = l2
        while curr2:
            sum2 += curr2.val * (10**n2)
            curr2 = curr2.next
            n2 += 1
        
        anchor = ListNode()
        sumstr = str(sum1 + sum2)
        for c in sumstr:
            curr = ListNode(int(c), anchor.next)
            anchor.next = curr

        return anchor.next
